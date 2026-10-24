"""One lookup in the existing fixed k7 corpus; no enlarged language or cap."""
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
ns={'__file__':str(ROOT/'check_four_C_center_contact_gate.py')};exec((ROOT/'check_four_C_center_contact_gate.py').read_text().split('# Canonical first-contact geometry')[0],ns)
G,rot,add,sub,det,VECTORS=[ns[k] for k in ['G','rot','add','sub','det','VECTORS']]

def atomic(word):
 p,h,clock=(0,0),0,0;edges=[]
 for wi,full in enumerate(word):
  for a in [G[full]['name'][0]]+['C']*G[full]['name'].count('C'):
   start=add((2*p[0],2*p[1]),rot((-1,-1),h));op,oh,oc=p,h,clock
   p=add(p,rot((0,1) if a=='C' else VECTORS[a],h));h=(h-int(a=='C'))%4;clock+=int(a=='C')
   end=add((2*p[0],2*p[1]),rot((-1,-1),h))
   edges.append({'atom':a,'packet_index':wi,'pose':(*op,oh),'clock':oc,'start':start,'end':end})
 return edges

def first_contacts(edges):
 contacts=[]
 for j,b in enumerate(edges):
  for i,a in enumerate(edges[:max(0,j-1)]):
   u,v=sub(a['end'],a['start']),sub(b['end'],b['start']);w=sub(b['start'],a['start']);de=det(u,v)
   if de:
    s,t=F(det(w,v),de),F(det(w,u),de)
    if not (0<=s<=1 and 0<=t<=1):continue
   else:
    if det(w,u):continue
    k=0 if v[0] else 1;t0,t1=F(-w[k],v[k]),F(u[k]-w[k],v[k]);low,high=max(F(0),min(t0,t1)),min(F(1),max(t0,t1))
    if low>high:continue
    t=low;point=add(b['start'],(t*v[0],t*v[1]));k=0 if u[0] else 1;s=F(point[k]-a['start'][k],u[k])
   contacts.append((j+t,i+s,i,j,s,t))
 if not contacts:return []
 low=min(r[0] for r in contacts);return [r for r in contacts if r[0]==low]
D=json.loads((ROOT/'chronology_dcuv/literal_factor_dfa_k7.json').read_text())
words=sorted((tuple(w) for w in D['states']),key=lambda w:(len(w),w))
for w in D['states']:
 if len(w)==6:
  c=D['state_to_class'][D['states'].index(w)] if False else None
# Generate exact saved legal length7 extensions from the minimized transition table.
for i,w in enumerate(D['states']):
 if len(w)==6:
  row=D['transitions'][D['state_to_class'][i]]
  words.extend(tuple(w+[a]) for a,t in zip(D['keep'] if isinstance(D['keep'],list) else [0,1,4,5,6,7,8,9],row) if t>=0)
words=sorted(set(words),key=lambda w:(len(w),w));diagnostic=Counter();hits=[]
for wi,w in enumerate(words):
 e=atomic(w);candidate=False
 for bi,b in enumerate(e):
  for ai,a in enumerate(e[:max(0,bi-1)]):
   if b['clock']-a['clock']!=5 or a['atom'] not in ('D','C'):continue
   hh=(b['pose'][2]-a['pose'][2])%4;pp=rot(sub(b['pose'][:2],a['pose'][:2]),-a['pose'][2])
   if hh==3 and ((b['atom'] in ('D','C') and pp==(0,-1)) or (a['atom']=='D' and b['atom']=='U' and pp==(1,0))):candidate=True
 if not candidate:continue
 diagnostic['candidate_words']+=1
 for t,sigma,ai,bi,s,tlocal in first_contacts(e):
  if s==1:ai+=1;s=F(0)
  if tlocal==0:bi-=1;tlocal=F(1)
  a,b=e[ai],e[bi];pp=rot(sub(b['pose'][:2],a['pose'][:2]),-a['pose'][2]);hh=(b['pose'][2]-a['pose'][2])%4
  if b['clock']-a['clock']==5 and hh==3 and a['atom'] in ('D','C') and ((b['atom'] in ('D','C') and pp==(0,-1)) or (a['atom']=='D' and b['atom']=='U' and pp==(1,0))):
   ini,conf=ns['requirements'](''.join(G[x]['word'] for x in w));assert conf is None
   hit={'word':w,'names':[G[x]['name'] for x in w],'mass':sum(ini.values()),'seed':sorted(p for p,v in ini.items() if v),'earlier_edge':ai,'later_edge':bi,'s':str(s),'t':str(tlocal),'relative_pose':(*pp,hh),'edges':e};hits.append(hit)
   print('HIT',hit['names'],hit['mass'],ai,bi,pp,hh,flush=True)
   break
 if hits:break
print('CHECKED existing words',wi+1,'of',len(words),'diagnostic',dict(diagnostic),'hits',len(hits))
(ROOT/'chronology_dcuv/five_C_touch_k7_lookup.json').write_text(json.dumps({'scope':'Bounded existing k7 corpus lookup only; no negative theorem.','checked_words':wi+1,'total_saved_words':len(words),'diagnostic':dict(diagnostic),'hits':hits},indent=2)+'\n')
