"""Bounded existing-corpus check of the proposed U-entry simplicity corollary."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent
D=json.loads((R/'chronology_dcuv/literal_factor_dfa_k7.json').read_text());G=json.loads((R/'chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
IDS=(0,1,4,5,6,7,8,9)

def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def touch(a,b):
 p,q=a;r,s=b;u,v=sub(q,p),sub(s,r);w=sub(r,p);d=cross(u,v)
 if d:
  ns,nt=cross(w,v),cross(w,u)
  if d<0:d,ns,nt=-d,-ns,-nt
  return 0<=ns<=d and 0<=nt<=d
 if cross(w,u):return False
 return all(max(min(p[k],q[k]),min(r[k],s[k]))<=min(max(p[k],q[k]),max(r[k],s[k])) for k in (0,1))
def atomic(w):
 p,h=(0,0),0;e=[]
 for full in w:
  for a in [G[full]['name'][0]]+['C']*G[full]['name'].count('C'):
   start=add((2*p[0],2*p[1]),rot((-1,-1),h));v=(0,1) if a=='C' else G[0 if a=='D' else 4 if a=='V' else 7]['endpoint'][:2]
   p=add(p,rot(v,h));h=(h-int(a=='C'))%4;end=add((2*p[0],2*p[1]),rot((-1,-1),h));e.append((start,end))
 return e
words=[tuple(w) for w in D['states'] if w and w[0] in (7,8,9)]
for i,w in enumerate(D['states']):
 if len(w)==6 and w[0] in (7,8,9):words.extend(tuple(w+[a]) for a,t in zip(IDS,D['transitions'][D['state_to_class'][i]]) if t>=0)
words=sorted(set(words),key=lambda w:(len(w),w));hits=[]
for wi,w in enumerate(words):
 e=atomic(w)
 pair=next(((i,j) for j in range(len(e)) for i in range(max(0,j-1)) if touch(e[i],e[j])),None)
 if pair:
  hits.append({'word':w,'names':[G[a]['name'] for a in w],'nonadjacent_contact_pair':pair});break
result={'scope':'Existing k7 literal corpus only; no negative theorem.','total_U_entry_saved_words':len(words),'checked_words':wi+1,'hits':hits}
(R/'chronology_dcuv/U_entry_k7_center_contact_lookup.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
