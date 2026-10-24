"""Discovery relaxation with FROZEN label classes. Rebuild final certificates afresh.
CLI QUOTIENT.json NEW_H.tsv PREFIX. H must be a subset of original H.
"""
import json,sys,hashlib
from pathlib import Path
from resource_profile import load_profile
inp,hf,out=map(Path,sys.argv[1:]);J=json.loads(inp.read_text());B=json.loads(Path(J['base_model_file']).read_text());profile,data,meta=load_profile(J['resource_profile_file']);G=data['geometry']['geometry'];F=data['ordinary'];FP=data['protected']|{tuple(map(int,l.split()[:7]))for l in Path(J['extra_guard_file']).read_text().splitlines()if l.strip()};H={tuple(map(int,l.split()[:7]))for l in hf.read_text().splitlines()if l.strip()};assert H<={tuple(r)for r in J['candidate_hypotheses']}
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def cubes(bad,bits):
 def rec(i,k,v,bs):
  if not bs:return[(k,v)]
  if i==bits:return[]
  bit=1<<i;return rec(i+1,k|bit,v,[x for x in bs if not x&bit])+rec(i+1,k|bit,v|bit,[x for x in bs if x&bit])
 return rec(0,0,0,list(bad))
T=[]
# The reset operator does not depend on H. Recover it from any original branch.
ops={}
for sid,to,k,v,f,c,r,goal,a in J['transitions']:ops[sid,to,f,goal,a]=(c,r)
for sid,to,k,v,f,goal,a in B['transitions']:
 x,y,h=B['poses'][sid];cc=[(k,v)]
 for L in J['producer_label_classes']:
  q=L['cell'];z=rot((q[0]-x,q[1]-y),-h)
  if list(z)not in G[a]['inputs']:continue
  bad=set()
  for ci,cl in enumerate(L['classes']):
   allbad=True
   for lab in cl['members']:
    if lab is None:allbad=False;break
    px,py,hh=lab['pose'];rel=rot((x-px,y-py),-hh);row=(lab['packet'],a,*rel,(h-hh)%4,*G[lab['packet']]['outputs'][lab['slot']])
    if not(row[:5]in F or row in FP or(row in H and(not goal or not lab['outer_origin']))):allbad=False;break
   if allbad:bad.add(ci)
  if bad:cc=[(kk|(ck<<L['offset']),vv|(cv<<L['offset']))for kk,vv in cc for ck,cv in cubes(bad,L['bits'])]
 key=sid,to,f,goal,a
 # If every original class combination was rejected there may be no branch.
 # Reconstruct the reset from literal full context and producer class maps.
 clear=reset=0
 for L in J['producer_label_classes']:
  z=rot((L['cell'][0]-x,L['cell'][1]-y),-h);context={tuple(r[:2])for r in G[a]['requirements']}
  if z in context:clear|=((1<<L['bits'])-1)<<L['offset']
  if list(z)in G[a]['outputs']:
   match=[i for i,l in enumerate(L['exact_codes'])if i and not l['outer_origin']and l['packet']==a and l['slot']==G[a]['outputs'].index(list(z))and l['pose']==[x,y,h]];assert len(match)==1
   clear|=((1<<L['bits'])-1)<<L['offset'];reset|=L['exact_codes_to_class'][match[0]]<<L['offset']
 if key in ops:assert ops[key]==(clear,reset)
 T.extend([sid,to,kk,vv,f,clear,reset,goal,a]for kk,vv in cc)
J.update(transitions=T,candidate_hypothesis_file=str(hf),candidate_hypothesis_sha256=hashlib.sha256(hf.read_bytes()).hexdigest(),candidate_hypotheses=[list(r)for r in sorted(H)],discovery_relaxed_frozen_classes=True)
out.with_suffix('.json').write_text(json.dumps(J,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{J['n']} {J['out']+1} {len(T)} {len(J['reentry'])}\n");f.write(' '.join(map(str,J['start']))+'\n')
 for r in T:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,J['reentry']))+'\n')
print(json.dumps({'transitions':len(T),'variables':J['n'],'hypotheses':len(H)}))
