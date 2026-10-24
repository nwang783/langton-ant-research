from pathlib import Path
from collections import defaultdict
import hashlib,json
R=Path('/workspace/shared/langton');OUT=Path(__file__).parent
MP=R/'causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json'
CP=R/'causal_reduction/unit_scale/prepared1564_source_endpoint_family.json'
NP=R/'nonlinear_global_budget_2026-10-23/prepared_wave_five_band_normal_form.json'
m=json.loads(MP.read_text());c=json.loads(CP.read_text());n=json.loads(NP.read_text())
w=m['stages'][15]['word'];assert m['seed_mass']==184 and len(w)==1564
D=((0,1),(1,0),(0,-1),(-1,0))
def trace(word,p,h):
 rows=[]
 for i,b in enumerate(word):
  rows.append((i,p,h,b));h=(h+(1 if b=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return rows,(p,h)
def rot(q,h):
 x,y=q;return ((x,y),(y,-x),(-x,-y),(-y,x))[h]
rows,end=trace(w,(-6,-6),0);assert end==((8,8),0)
Q=((1,18),(1,19),(2,18),(2,19));expected={
 Q[0]:[(0,1497,'R')],Q[1]:[(0,1490,'L'),(0,1498,'R')],
 Q[2]:[(0,1492,'L'),(0,1496,'R'),(0,1500,'L'),(0,1504,'R')],
 Q[3]:[(0,1491,'R'),(0,1495,'L'),(0,1499,'R')]}
A={}
for q in Q:
 hits=[]
 for i,p,h,b in rows:
  dx,dy=q[0]-p[0],q[1]-p[1]
  if dx==dy and dx%14==0:hits.append((dx//14,i,b))
 assert hits==expected[q] and hits[-1][-1]=='R';A[str(q)]=hits
at=trace(w[:1505],(-6,-6),0)[1];assert at==((3,18),1)
o=rot((1,-1),at[1]);w2=(2*at[0][0]+o[0],2*at[0][1]+o[1]);assert w2==(5,35)
cont,ce=trace(c['after_checkpoint_word'],(-6,-6),0)
assert len(cont)==56504 and min(sum(p)for i,p,h,b in cont)==-137
assert ce==((-104,-24),0) and c['threshold_N']==4
assert 21-6*28==-147 and -147 < -137
assert sorted({x-y for x,y in Q})==[-18,-17,-16]
tail,te=trace(c['capture_word'],ce[0],ce[1]);assert len(tail)==104
assert te==((-106,-26),0)
TH=(min(x-y for i,(x,y),h,b in tail),max(x-y for i,(x,y),h,b in tail))
assert TH==(-86,-76)==tuple(c['outgoing_read_normal_hull'])
assert set(range(TH[0],TH[1]+1)).isdisjoint(x-y for x,y in Q)
# Derive every edge of the canonical settled standard band from its exact profiles.
profiles=set(map(tuple,n['full_black_orbit_profiles']))
profile={p for p in profiles if -40<=p[0]<=-30};assert len(profile)==12
assert all(not ({(t,0),(t,1)}<=profile and any(a==t-1 for a,b in profile) and any(a==t+1 for a,b in profile)) for t in range(-41,-28))
def edge(q):
 x,y=q
 if (x+y)%2==0:e=((x+y-2)//2,(x-y)//2+20),((x+y)//2,(x-y)//2+20)
 else:e=((x+y-1)//2,(x-y-1)//2+20),((x+y-1)//2,(x-y+1)//2+20)
 return tuple(sorted(e))
def predicted(e):
 (u,v),(s,t)=e
 if v==t and v in (0,5):return s==u+1
 if v==t and v in (1,2,3,4):return s==u+1 and u%2==1
 if u==s and t==v+1:
  return (v in (0,1,4) and u%2==1) or (v==2 and u%2==0)
 return False
seen=set()
for x in range(-100,101):
 for t,p in profile:
  if x%2==p:seen.add(edge((x,x-t)))
assert all(predicted(e)for e in seen)
# Every predicted edge in a central exact period is present; no hidden tooth edges.
for u in range(-8,8):
 for v in range(-1,7):
  for e in [tuple(sorted(((u,v),(u+1,v)))),tuple(sorted(((u,v),(u,v+1))))]:
   assert (e in seen)==predicted(e),(e,e in seen,predicted(e))
res={'status':'PASS exact all-parameter permanent unit-island countercontrol',
 'original_seed_mass':184,'domain':'N>=6','permanent_island_lower_bound':'N-5',
 'square_SW_base':[1,18],'square_drift':[14,14],'copy_range':'0<=j<=N-6',
 'all_copy_slot_alignments':A,'complete_black_after_phase':1504,
 'pose_after_phase1504':[[3,18],1],'doubled_w_after_phase1504':w2,
 'fixed_continuation_length':56504,'continuation_min_u_normalized':-137,
 'square_max_u_at_last_safe_copy':'28N-147','infinite_tail_read_normal_hull':TH,
 'square_read_normals':[-18,-17,-16],'standard_profile_forest':True,
 'scope':'Generic physical permanent islands, not genuine complete-eight U-producer cycles.',
 'source_sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(MP,CP,NP)}}
(OUT/'permanent_unit_islands_controls.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
