"""Conditional full-family upper-input freshness model with fused color/origin.
CLI BASE.json PREFIX H.tsv 'all|x,y;x,y'. Every watched cell is retained.
Codes: 0 white, 1 black unknown, 2 black outer-source, 3 black internal.
H must cover EVERY HB-admitted producer->upper-input geometry for kept types.
No member of H is asserted proved by this generator.
"""
from pathlib import Path
import json,sys,hashlib,itertools
from resource_profile import load_profile
base,out,hf=map(Path,sys.argv[1:4]);J=json.loads(base.read_text());profile,data,meta=load_profile(J['resource_profile_file']);G=data['geometry']['geometry'];F=data['ordinary'];FP=data['protected'];H={tuple(map(int,l.split()[:7]))for l in hf.read_text().splitlines()if l.strip()};upper={(-1,4),(0,2),(0,3)};targets={a for a in J['keep']if G[a]['name']in ('U','UC','UCC')};watch=set(map(tuple,J['points']))if sys.argv[4]=='all'else{tuple(map(int,c.split(',')))for c in sys.argv[4].split(';')};assert watch<=set(map(tuple,J['points']))
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
needed=set()
for a in J['keep']:
 for q in G[a]['outputs']:
  for b in targets:
   assert upper<=set(map(tuple,G[b]['inputs']))
   for z in upper:
    for h in range(4):
     zz=rot(z,h);p=(q[0]-zz[0],q[1]-zz[1]);r=(a,b,*p,h,*q)
     if (sum(p)+h)%2==0 and r[:5]not in F and r not in FP:needed.add(r)
assert needed<=H,('incomplete family',len(needed-H));n=0;cells=[]
for i,q in enumerate(J['points']):
 bits=2 if tuple(q)in watch else 1;cells.append({'cell':q,'old_color_bit':i,'offset':n,'bits':bits,'watched':bits==2});n+=bits
assert n<=50,'fused model exceeds current engine cap'
sp,sk,sv=J['start'];nk=nv=0
for c in cells:
 i=c['old_color_bit'];off=c['offset'];bits=c['bits'];q=c['cell']
 if bits==1:
  if sk>>i&1:nk|=1<<off;nv|=((sv>>i)&1)<<off
 elif q in G[J['source']]['outputs']:
  assert sk>>i&1 and sv>>i&1;nk|=3<<off;nv|=2<<off
 else:
  nk|=2<<off
  if sk>>i&1:nk|=1<<off;nv|=((sv>>i)&1)<<off
T=[]
for sid,to,k,v,f,goal,a in J['transitions']:
 x,y,h=J['poses'][sid];branches=[(0,0)];flip=clear=reset=0
 for c in cells:
  i=c['old_color_bit'];off=c['offset'];bits=c['bits'];touched=(k>>i)&1
  if bits==1:
   if touched:branches=[(kk|(1<<off),vv|(((v>>i)&1)<<off))for kk,vv in branches]
   if f>>i&1:flip|=1<<off
   continue
  if not touched:assert not(f>>i&1);continue
  initial=(v>>i)&1;z=rot((c['cell'][0]-x,c['cell'][1]-y),-h);isupper=a in targets and z in upper
  assert not isupper or initial==1
  if not initial:allowed=[(3,0)]
  elif isupper:allowed=[(3,1),(3,2)]if goal else[(3,1)]
  else:allowed=[(1,1),(3,2)] # disjoint cover of1,2,3
  branches=[(kk|(mk<<off),vv|(mv<<off))for kk,vv in branches for mk,mv in allowed]
  clear|=3<<off
  final=3 if list(z)in G[a]['outputs']else initial^((f>>i)&1)
  reset|=final<<off
 for kk,vv in branches:T.append([sid,to,kk,vv,flip,clear,reset,goal,a])
new={**J,'n':n,'start':[sp,nk,nv],'transitions':T,'format':'guarded_reset_fused_upper_freshness_v1','base_model_file':str(base),'base_model_sha256':hashlib.sha256(base.read_bytes()).hexdigest(),'candidate_hypothesis_file':str(hf),'candidate_hypothesis_sha256':hashlib.sha256(hf.read_bytes()).hexdigest(),'candidate_hypotheses':sorted(H),'required_full_family':sorted(needed),'origin_cells':cells,'upper_inputs':sorted(upper),'upper_target_types':sorted(targets),'origin_encoding':{'white':0,'black_unknown':1,'black_outer':2,'black_internal':3},'conditional_scope':'least-gap full upper-input family; target prefixes uniformly permitted; no outer-origin hypothesis at outer goal'}
out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {J['out']+1} {len(T)} {len(J['reentry'])}\n");f.write(' '.join(map(str,new['start']))+'\n')
 for r in T:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,J['reentry']))+'\n')
print(json.dumps({'variables':n,'positions':J['out']+1,'transitions':len(T),'watched_cells':len(watch),'required_hypotheses':len(needed)}))
