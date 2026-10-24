"""Exact five-core residual-token replay on physically feasible marked DCV words."""
import json,sys
from pathlib import Path
W={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'};MARK='LLLLRLRRRRL';dirs=(1j,1,-1j,-1)
def trace(w):
 p=0j;h=0;first={};last={};odd=set()
 for t,c in enumerate(w):
  if last.get(p)==c:return None
  first.setdefault(p,(c,t));last[p]=c;odd.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
 return p,h,first,last,odd
core={p for p,(c,t)in trace(MARK)[2].items()if c=='L'}
def xy(p):return[int(p.real),int(p.imag)]
def packets(s):
 out=[]
 for c in s:
  if c=='C':assert out;out[-1]+='C'
  else:out.append(c)
 return out
cache={}
def geom(a):
 if a not in cache:
  w=''.join(W[c]for c in a);p,h,_,last,odd=trace(w);_,_,first,_,_=trace(w+MARK);nc={p+q*(-1j)**h for q in core};b={q for q,(c,t)in first.items()if c=='L'};o=b^odd;ei=b-core;eo=o-nc;assert not ei&eo;assert all(last[q]=='R'for q in eo)
  cache[a]=(p,h,sorted(ei,key=lambda q:(q.real,q.imag)),sorted(eo,key=lambda q:(q.real,q.imag)),odd)
 return cache[a]
def replay(s):
 A=packets(s);w=''.join(W[c]for c in s);t=trace(w+MARK)
 if t is None:return None
 seed={q for q,(c,n)in t[2].items()if c=='L'};assert core<=seed;B=set(seed);E={q:None for q in seed-core};p=0j;h=0;steps=[]
 for j,a in enumerate(A):
  d,dh,ins,outs,odd=geom(a);ip=[p+q*(-1j)**h for q in ins];op=[p+q*(-1j)**h for q in outs];oldpose=xy(p)+[h]
  assert all(q in E for q in ip);assert all(q not in E for q in op)
  consumed=[{'point':xy(q),'producer':E.pop(q)}for q in ip]
  for k,q in enumerate(op):E[q]={'packet_index':j,'packet':a,'output_slot':k,'pose':oldpose}
  B.symmetric_difference_update({p+q*(-1j)**h for q in odd});p+=d*(-1j)**h;h=(h+dh)%4;nc={p+q*(-1j)**h for q in core};assert nc<=B and set(E)==B-nc
  steps.append({'packet':a,'pose':oldpose,'inputs':consumed,'outputs':[xy(q)for q in op],'entry_root_inputs':sum(c['producer']is None for c in consumed)})
 return {'word':s,'seed_mass':len(seed),'seed':[xy(q)for q in sorted(seed,key=lambda q:(q.real,q.imag))],'packets':steps}
if __name__=='__main__':
 S=sys.argv[1:]or['DCCCV','DDCDCDCDV','DCVCCVV','DVCCVCDDCD'];R=[replay(s)for s in S];Path('dcv_residual_resource_controls.json').write_text(json.dumps(R,indent=2))
 for r in R:
  print(r['word'],'mass',r['seed_mass'])
  for j,z in enumerate(r['packets']):print(j,z['packet'],'inputs',[(q['point'],q['producer']and(q['producer']['packet_index'],q['producer']['packet'],q['producer']['output_slot']))for q in z['inputs']])
