"""Independent complete equality reconstruction after the analytic all-drift reduction."""
from pathlib import Path
from itertools import product,combinations
from collections import defaultdict,Counter
import hashlib,json
R=Path(__file__).resolve().parents[1];dirs=(1j,1,-1j,-1);results=[]
for b in(1,-1,3):
 drift=complex(3,b);mac={}
 for h in dirs:
  for winding,size in[(0,4),(0,8),(-1,6),(1,6)]:
   choices=[]
   for letters in product('RL',repeat=size):
    word=''.join(letters);p=0j;d=h;times=[]
    for t,c in enumerate(word):
     d*=(-1j if c=='R'else 1j);p+=d;x,y=int(p.real),int(p.imag)
     if x%3==0 and 3*y==b*x:times.append(t+1)
    if p==drift*winding and times==[size]:choices.append((word,d))
   mac[h,winding,size]=choices
 layouts=[((1,6),)+tuple((0,8 if i==long else 4)for i in range(4))for long in range(4)]
 layouts +=[((-1,6),)+tuple((1,6)if i in positive else(0,4)for i in range(1,5))for positive in combinations(range(1,5),2)]
 counts=Counter();accepted=[]
 for blocks in layouts:
  for h0 in dirs:
   stack=[(0,h0,0,0,(),())]
   while stack:
    i,h,k,t,words,center=stack.pop()
    if i==5:
     counts['all']+=1;assert k==1 and t==26
     if h!=h0:continue
     counts['heading']+=1
     if ''.join(c for _,c in sorted(center))!='RLRLR':continue
     counts['center']+=1;p=0j;d=h0;groups=defaultdict(list)
     for time,c in enumerate(''.join(words)):
      x,y=int(p.real),int(p.imag);q=x//3;groups[x%3,y-b*q].append((time-26*q,c));d*=(-1j if c=='R'else 1j);p+=d
     assert p==drift and d==h0 and len(groups[0,0])==5
     if all(''.join(c for _,c in sorted(hist))==('RL'*((len(hist)+1)//2))[:len(hist)]for hist in groups.values()):accepted.append(''.join(words))
     continue
    w,size=blocks[i]
    for word,hh in mac[h,w,size]:stack.append((i+1,hh,k+w,t+size,words+(word,),center+((t-26*k,word[0]),)))
 assert not accepted
 results.append(dict(full_drift=[3,b],counts=dict(counts),accepted=accepted))
C=R/'periodic_classification_new/check_global_period26_equality.json';J=json.loads(C.read_text())
for a,j in zip(results,J['cases']):
 assert a['full_drift']==j['full_drift']and a['counts']==dict(all=j['program_sequences'],heading=j['heading_restoring'],center=j['center_white_legal'])and j['accepted']==a['accepted']
out=dict(status='PASS full three-family period26 equality replay; analytic reduction independently reviewed',cases=results,candidate_sha256=hashlib.sha256(C.read_bytes()).hexdigest(),scope='Complete nonzero WHITE translating fronts have period>=28, using prior unrestricted structural dependencies. No104 minimality, realized P28 front, general front exclusion or capture claim.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
