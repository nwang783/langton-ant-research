"""Independent geometric macro generation, cyclic gap enumeration and white histories."""
from pathlib import Path
from itertools import product,combinations
from collections import defaultdict,Counter
import json,hashlib
R=Path(__file__).resolve().parents[1];dirs=(1j,1,-1j,-1);mac={}
for h in dirs:
 for winding,size in[(0,4),(-1,8),(1,8)]:
  choices=[]
  for letters in product('RL',repeat=size):
   word=''.join(letters);p=0j;d=h;times=[]
   for t,c in enumerate(word):
    d*=(-1j if c=='R'else 1j);p+=d
    if p.imag==0 and int(p.real)%4==0:times.append(t+1)
   if p==4*winding and times==[size]:choices.append((word,d))
  assert len(choices)==(4 if winding==0 else 6);mac[h,winding]=choices
counts=Counter();survivors=[]
for positive in combinations(range(1,6),2):
 windings=(-1,)+tuple(int(i in positive)for i in range(1,6))
 for h0 in dirs:
  stack=[(0,h0,0,0,(),())]
  while stack:
   i,h,k,t,words,center=stack.pop()
   if i==6:
    counts['all']+=1;assert k==1 and t==36
    if h!=h0:continue
    counts['heading']+=1
    if ''.join(c for _,c in sorted(center))!='RLRLRL':continue
    counts['center']+=1
    p=0j;d=h0;groups=defaultdict(list)
    for time,c in enumerate(''.join(words)):
     x,y=int(p.real),int(p.imag);groups[x%4,y].append((time-36*(x//4),c));d*=(-1j if c=='R'else 1j);p+=d
    assert p==4 and d==h0 and len(groups[0,0])==6
    if all(''.join(c for _,c in sorted(hist))==('RL'*((len(hist)+1)//2))[:len(hist)]for hist in groups.values()):survivors.append(''.join(words))
    continue
   w=windings[i]
   for word,hh in mac[h,w]:stack.append((i+1,hh,k+w,t+len(word),words+(word,),center+((t-36*k,word[0]),)))
assert counts=={'all':552960,'heading':276480,'center':4320}and not survivors
C=R/'periodic_classification_new/check_axis_four_period36_equality.json';J=json.loads(C.read_bytes());assert J['program_sequences']==counts['all']and J['heading_restoring']==counts['heading']and J['center_white_legal']==counts['center']and J['accepted']==survivors
out=dict(status='PASS complete independent axis-four period36 equality enumeration',counts=dict(counts),accepted=survivors,candidate_sha256=hashlib.sha256(C.read_bytes()).hexdigest(),scope='Uses KR, LC and independently checked five-first-return cost32 to reduce to six gaps. Complete white history on the full drift cylinder; no other period scan or all-period no-front conclusion. Necessary all-cap axis-four P>=40.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
