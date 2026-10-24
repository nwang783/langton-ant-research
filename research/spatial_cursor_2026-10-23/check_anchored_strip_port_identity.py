from pathlib import Path
import json,sys,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
M184=json.loads((ROOT/'causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json').read_text())
M394=json.loads((ROOT/'causal_reduction/unit_scale/prepared4352_two_phase_manifest.json').read_text())
D=((0,1),(1,0),(0,-1),(-1,0));f=lambda a:3**abs(a)-1

def J(p,h,c,axis='u'):
 z=p[0]+(p[1] if axis=='v' else -p[1]);e=(1 if h in(0,1) else -1) if axis=='v' else (1 if h in(1,2) else -1)
 return f(z-c)//2 if e*(z-c)>=0 else -3*f(z-c)//2

def trace(w,p,h,cA=-1,cB=0,k=0,axis='u'):
 start=p,h;P=N=0;run=[]
 for ch in w:
  z=p[0]+(p[1] if axis=='v' else -p[1]);side=z>=k;c=cB if side else cA
  if not run or run[-1]!=side:run.append(side)
  old=p,h;h=(h+(1 if ch=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1]);zz=p[0]+(p[1] if axis=='v' else -p[1]);N+=(zz>=k)!=side;P+=J(p,h,c,axis)-J(*old,c,axis)
 z0=start[0][0]+(start[0][1] if axis=='v' else -start[0][1]);zt=p[0]+(p[1] if axis=='v' else -p[1]);a=k-cA;b=cB-k
 kappa=(3**a+3**(b+1)-4)//2
 delta=J(p,h,cB if zt>=k else cA,axis)-J(*start,cB if z0>=k else cA,axis)
 assert P==delta+kappa*N
 return {'length':len(w),'start':[list(start[0]),start[1]],'end':[list(p),h], 'crossings':N,'port_debt':P,'streaks':len(run),'delta_piecewise_head':delta,'kappa':kappa}
H=M184['stages'][0]['word'];W=M184['stages'][-1]['word'];G=[s for s in M394['stages'] if s['kind']=='wave'][0]['word'];R=M394['stages'][-1]['word']
records={
 'standard104_SW':trace(H,(0,0),3),
 'wave1564':trace(W,(-6,-6),0),
 'wave4352':trace(G,(-2,3),3),
 'return15324':trace(R,(117,111),0)}
assert [(d['crossings'],d['port_debt']) for d in records.values()]==[(8,8),(4,4),(66,66),(326,326)]
# Exhaust literal one-step formula for both axes, headings, turns, boundary
# locations, and several fixed center distances. No reachability search.
local=0
for axis in ('u','v'):
 for h in range(4):
  for ch in 'LR':
   for k in range(-2,3):
    for a in range(1,4):
     for b in range(3):
      for x in range(-3,4):
       for y in range(-3,4):
        trace(ch,(x,y),h,k-a,k+b,k,axis);local+=1
seed13={(q[0][1]-33,q[1][1]-70) for q in M184['seed_families'][:13]}
assert len(seed13)==13 and {(-1,0),(0,0)}<=seed13
sys.path.insert(0,str(ROOT/'computability'))
from periodic_tail_checker import State,first_mismatch
assert first_mismatch(State(frozenset(seed13),(0,0),3),H) is None
for manifest in (M184,M394):
 for value in (-1,0):
  assert any(q[0][0]==q[1][0] and q[0][1]-q[1][1]==value for q in manifest['seed_families'])
# Full all-parameter crossing arithmetic from signed literal stage manifests.
full_affine={}
for file in ('prepared1564_uniform_support_manifest.json','prepared4352_two_phase_manifest.json','prepared4352_capture_manifest.json'):
 manifest=json.loads((ROOT/'causal_reduction/unit_scale'/file).read_text());total=[0,0];ordinary=[0,0];stage_counts=[]
 for st in manifest['stages']:
  p0=(st['start_x_N_constant'][1],st['start_y_N_constant'][1]);h0=st['heading']
  assert st['start_x_N_constant'][0]==st['start_y_N_constant'][0]
  info=trace(st['word'],p0,h0);a,b=st['count_N_constant']
  if a or b>1:
   assert info['end'][0][0]-info['end'][0][1]==p0[0]-p0[1] and info['end'][1]==h0
  C=info['crossings'];total[0]+=a*C;total[1]+=b*C
  if st['kind'] in ('H','H-prefix','SW-standard','SW-partial'):
   ordinary[0]+=a*C;ordinary[1]+=b*C
  stage_counts.append({'kind':st['kind'],'one_word_crossings':C,'count_affine':[a,b]})
 full_affine[file]={'all_crossings':total,'supplied_standard_crossings':ordinary,
  'residual_crossings':[total[i]-ordinary[i] for i in range(2)],'stage_counts':stage_counts}
assert full_affine['prepared1564_uniform_support_manifest.json']['all_crossings']==[144,559]
assert full_affine['prepared1564_uniform_support_manifest.json']['residual_crossings']==[4,69]
assert full_affine['prepared4352_two_phase_manifest.json']['all_crossings']==[1148,3498]
assert full_affine['prepared4352_two_phase_manifest.json']['residual_crossings']==[524,1786]
assert full_affine['prepared4352_capture_manifest.json']['all_crossings']==[1148,3944]
assert full_affine['prepared4352_capture_manifest.json']['residual_crossings']==[524,2232]
# Exact initial-head common-center corrections on the signed affine families.
assert J((0,0),0,-37)-J((-37,0),3,-37)==-3*f(37)//2
assert J((6,0),0,25)-J((25,0),3,25)==f(19)//2
assert J((30,0),0,25)-J((25,0),3,25)==-3*f(5)//2
out={'status':'all exact literal identities passed','one_step_identity_checks':local,
 'standard13_all_future_H_certificate':True,'period_records':records,'full_manifest_crossings':full_affine,
 'scope':'Actual anchored cut-crossing ledger; debt bound still requires independent exposure control.',
 'source_manifests':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json',ROOT/'causal_reduction/unit_scale/prepared4352_two_phase_manifest.json']}}
(OUT/'anchored_strip_port_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
