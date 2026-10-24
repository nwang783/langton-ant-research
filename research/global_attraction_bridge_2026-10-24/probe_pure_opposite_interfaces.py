from pathlib import Path
import json
exec(Path('check_transverse_first_contact_quotient.py').read_text().split('out=[];class_words={}')[0])
refs=json.loads((P/'OPPOSITE_TRANSVERSE_JOIN_PROBES.json').read_text())['records'];outputs=[]
for ref in refs:
 z=tuple(ref['poses'][5][0]);q=tuple(ref['first_contact']['cell']);r,phi=divmod(ref['first_contact']['relative_last']-182,104);fringe=set(C)
 for v in Q[:phi]:
  if v in fringe:fringe.remove(v)
  else:fringe.add(v)
 base=add(z,(-2*r,2*r));finite={add(base,rot(v,3))for v in fringe};generators=[(w,(2,2),None)for w in W]+[(add(z,rot(w,3)),(-2,2),r-1)for w in W]
 def initial(p):
  b=p in finite
  for a,v,bound in generators:
   d=sub(p,a)
   if d[0]%v[0]==0 and d[1]==(d[0]//v[0])*v[1] and(bound is None or d[0]//v[0]<=bound):b=not b
  return b
 changes=set();p=q;h=0;word='';poses=[p];phases={U[i:]+U[:i]for i in range(104)};res=(sum(z)%4,(z[0]-z[1])%4);result=None
 for t in range(200000):
  black=initial(p)^(p in changes);word+='L'if black else'R'
  if p in changes:changes.remove(p)
  else:changes.add(p)
  h=(h+(-1 if black else 1))%4;p=add(p,DXY[h]);poses.append(p)
  if t>=312 and t%104==0 and word[-104:]in phases and word[-312:]==word[-104:]*3:
   try:dr,tests=infinite_tail(generators,finite^changes,p,h,word[-104:])
   except AssertionError:continue
   k=t
   while k>=0 and word[k]==word[-104:][(k-t-1)%104]:k-=1
   result=dict(status='CANONICAL',residue=res,cut=t+1,exact_onset=k+1,tail=word[-104:],drift=dr,pose=[p,h],transient=word[:k+1],parity_tests=sum(len(x['critical_copies'])for x in tests));break
 if result is None:
  periodic=[]
  for T in [104,1564,4352]:
   if word[-T:]*3==word[-3*T:]:periodic.append(dict(period=T,drift=sub(poses[-1],poses[-1-T])))
  result=dict(status='UNKNOWN',residue=res,reads=len(word),periodic_suffix=periodic,pose=[p,h],tail_words={str(T):word[-T:]for T in[104,1564,4352]})
 outputs.append(result);print({k:v for k,v in result.items()if k not in['transient','tail','tail_words']},flush=True)
(P/'PURE_OPPOSITE_INTERFACES_PROBES.json').write_text(json.dumps(outputs,indent=2)+'\n')
