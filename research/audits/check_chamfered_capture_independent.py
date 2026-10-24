"""Exact two-parameter all-future check from independently rebuilt seed reads.
No author family construction, inverse time formula or pair filtering is used.
"""
from pathlib import Path
import json,sys,time,hashlib
B=Path('/workspace/shared/langton');P=B/'causal_reduction/unit_scale/chamfered_capture_certificate.json';D=json.loads(P.read_text())
sys.path.insert(0,str(B/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'))
from isl_exact import Context
C=Context(max_operations=100000000);start=time.monotonic()
def xy(z):return round(z.real),round(z.imag)
def lin(cs,vs):return '('+'+'.join(f'{a}*{v}' for a,v in zip(cs,vs))+')'
def trace(w,h):
 p=0j;out=[]
 for j,c in enumerate(w):out.append((p,c,j));h*=(-1j if c=='R' else 1j);p+=h
 return out,p,h
# Rebuild all R-output seed families directly from four literal sides.
seed=[];pos=[0j,0j,0j];h=1+0j
for side in range(4):
 for text,var in [('LRRL',0),('RL',1),('R',None)]:
  slots,d,end=trace(text,h)
  if var is not None:assert end==h
  for q,c,j in slots:
   if c=='R':seed.append(dict(x=(*[xy(z)[0] for z in pos[:2]],xy(d)[0],xy(pos[2]+q)[0]),y=(*[xy(z)[1] for z in pos[:2]],xy(d)[1],xy(pos[2]+q)[1]),bound=('r' if var==0 else 'k' if var==1 else '1')))
  if var is None:pos[2]+=d
  else:pos[var]+=d
  h=end
assert pos==[0j,0j,0j] and h==1
words=D['words'];assert words['H']==json.loads((B/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];assert [len(words[t]) for t in ('P','V','C','H')]==[50,20,257,104]
stages=[(words['P'],0,1),(words['V'],1,-1),(words['C'],0,1),(words['H'],None,None)]
fam=[];pos=[0j,0j];clock=[0,0];h=1+0j
for si,(word,a,b) in enumerate(stages):
 slots,d,end=trace(word,h)
 if a is None:
  assert pos==[2+0j,1+4j] and clock==[20,287] and h==1j and end==h and d==-2+2j
 elif a:assert end==h and d!=0 and a*10+b>0
 else:assert b==1
 for off,c,j in slots:
  fam.append(dict(x=(xy(pos[0])[0],xy(d)[0],xy(pos[1]+off)[0]),y=(xy(pos[0])[1],xy(d)[1],xy(pos[1]+off)[1]),t=(clock[0],len(word),clock[1]+j),a=a,b=b,c=c,s=si,j=j))
 if a is None:break
 pos=[pos[0]+a*d,pos[1]+b*d];clock=[clock[0]+a*len(word),clock[1]+b*len(word)];h=end
assert len(fam)==431

def bound(f,v):return f'{v}>=0' if f['a'] is None else f'0<={v}<{f["a"]}*r+{f["b"]}'
pairs=hits=0
for fi,f in enumerate(fam):
 C.reset_operations();base='r>=10 and k>=10 and '+bound(f,'n');dom=C.set('{[r,k,n]:'+base+'}')
 x,y,t=[lin(f[key],('r','n','1')) for key in ('x','y','t')]
 terms=[]
 for g in seed:
  X,Y=[lin(g[key],('r','k','j','1')) for key in ('x','y')]
  terms.append(f'(exists(j:0<=j<{g["bound"]} and {x}={X} and {y}={Y}))')
 color=C.set('{[r,k,n]:'+base+' and ('+' or '.join(terms)+')}')
 for g in fam:
  X,Y,T=[lin(g[key],('r','m','1')) for key in ('x','y','t')]
  prior=C.set('{[r,k,n]:'+base+' and exists(m:'+bound(g,'m')+f' and {x}={X} and {y}={Y} and {T}<{t})'+'}')
  pairs+=1
  if not prior.is_empty():hits+=1;color=color.subtract(prior).union(prior.subtract(color)).coalesce()
 bad=dom.subtract(color) if f['c']=='L' else color
 assert bad.is_empty(),(fi,str(bad))
 if fi%100==0:print('families',fi,'pairs',pairs,'seconds',time.monotonic()-start,flush=True)
controls=[]
for r,k in [(10,10),(10,100),(100,10),(11,15),(40,25)]:
 frame=('LRRL'*r+'RL'*k+'R')*4;reads,_,_=trace(frame,1);board={z for z,c,j in reads if c=='L'};p=0j;h=1;n=0
 for text,count in [(frame,1)]+[(w,100 if a is None else a*r+b) for w,a,b in stages]:
  if text==words['H']:assert (n,p,h)==(36*r+8*k+291,2*r+1+4j,1j)
  for _ in range(count):
   for c in text:
    assert (p in board)==(c=='L'),(r,k,n,c)
    board.symmetric_difference_update({p});h*=(-1j if c=='R' else 1j);p+=h;n+=1
 controls.append(dict(r=r,k=k,read_count=n,tail_periods=100))
out=dict(status='PASS all r,k>=10 and all future reads',candidate_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),literal_seed_output_families=len(seed),read_families=len(fam),all_ordered_pairs_including_self=pairs,nonempty_prior_relations=hits,tail_time_after_frame=[20,287],tail_time_from_original=[36,8,291],tail_pose='(2r+1,4,N)',tail_drift=[-2,2],controls=controls,seconds=time.monotonic()-start,scope='Specified two-parameter finite seed family only; sufficient phase and thresholds, not minimal or global.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
