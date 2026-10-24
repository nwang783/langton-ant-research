"""Bounded negative-control search, NOT a freshness certificate.
Literal macro words only; geometry and complete prefix consistency rebuilt.
Every prefix starts non-C. At each possible first C, test CV and CCV now.
"""
import sys,time,json,hashlib,re
from collections import Counter
from pathlib import Path
WORDS={
 'C':'LLLLRLRRRRLRRRR',
 'V':'LLLLRLRRRRLRRLRRRR',
 'U':'LLLLRLRRRRLRLLLLRRRRLRRLRRRR',
 'Q':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRRLRRRR',
 'B':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR'}
DIRS=((0,1),(1,0),(0,-1),(-1,0))
def rotate(p,h):
 x,y=p
 return ((x,y),(y,-x),(-x,-y),(-y,x))[h]
DATA={};LAST_PHASE={};PATH=[];CATEGORIES=Counter();SHORTEST={};PATTERNS=Counter();UNBALANCED=[]
for a,w in WORDS.items():
 first={};last={};lastphase={};x=y=h=0
 for i,c in enumerate(w):
  p=(x,y);v=(c=='L')
  if p in last:assert last[p]!=v
  first.setdefault(p,v);last[p]=v;lastphase[p]=(i,c)
  h=(h+(1 if c=='R'else-1))%4;dx,dy=DIRS[h];x+=dx;y+=dy
 LAST_PHASE[a]=lastphase
 for h0 in range(4):
  DATA[a,h0]=(tuple((rotate(p,h0),v,last[p])for p,v in first.items()),rotate((x,y),h0),(h+h0)%4)
last={};nodes=0;tests=0;terminal_old=0;witness=None
DEPTH=int(sys.argv[1])if len(sys.argv)>1 else 18
CAP=int(sys.argv[2])if len(sys.argv)>2 else 2000000
start=time.monotonic();counts=[0]*(DEPTH+1)
def apply(a,pose):
 x,y,h=pose;items,d,nh=DATA[a,h];undo=[]
 for (dx,dy),first,end in items:
  p=(x+dx,y+dy);old=last.get(p)
  if old is not None and old==first:return None
 for (dx,dy),first,end in items:
  p=(x+dx,y+dy);undo.append((p,last.get(p)));last[p]=end
 return((x+d[0],y+d[1],nh),undo)
def rollback(undo):
 for p,old in undo:
  if old is None:del last[p]
  else:last[p]=old

def classify(prefix,pose,q):
 for j in range(len(PATH)-1,-1,-1):
  a,sp=PATH[j];ql=rotate((q[0]-sp[0],q[1]-sp[1]),(-sp[2])%4)
  if ql not in LAST_PHASE[a]:continue
  phase,ch=LAST_PHASE[a][ql];assert ch=='R'
  suffix=prefix[j:]+'C';match=re.fullmatch(r'([UV]+)CC([UV]+)C',suffix)
  balanced=bool(match and all(match[1].count(a)==match[2].count(a)for a in 'UV'))
  key=(a,phase,(sp[2]-pose[2])%4,balanced);CATEGORIES[key]+=1;PATTERNS[suffix]+=1
  if key not in SHORTEST or len(suffix)<len(SHORTEST[key]):SHORTEST[key]=suffix
  if not balanced and len(UNBALANCED)<100:UNBALANCED.append(dict(prefix=prefix,source_index=j,source_macro=a,source_phase=phase,relative_heading=key[2],suffix=suffix))
  return
 raise AssertionError('lost last writer')

def completion(prefix,pose):
 global tests,terminal_old,witness
 dx,dy=rotate((-1,0),pose[2]);q=(pose[0]+dx,pose[1]+dy)
 if q not in last:return False
 z=apply('C',pose)
 if z is None:return False
 terminal_old+=1;classify(prefix,pose,q);p1,u1=z
 for suffix in ('V','CV'):
  p=p1;undos=[];okay=True
  for a in suffix:
   z=apply(a,p)
   if z is None:okay=False;break
   p,undo=z;undos.append(undo)
  tests+=1
  if okay:witness={'word':prefix+'C'+suffix,'marker':q,'first_C_index':len(prefix),'end_pose':p};print('WITNESS',json.dumps(witness),flush=True)
  for undo in reversed(undos):rollback(undo)
  if okay:rollback(u1);return True
 rollback(u1);return False

def search(prefix,pose):
 global nodes
 nodes+=1;counts[len(prefix)]+=1
 if nodes>CAP:raise RuntimeError('resource cap')
 if prefix and prefix[-1]!='C' and completion(prefix,pose):return True
 if len(prefix)==DEPTH:return False
 for a in 'CVUQB' if prefix else 'VUQB':
  z=apply(a,pose)
  if z is None:continue
  p,undo=z
  PATH.append((a,pose));yes=search(prefix+a,p);PATH.pop();rollback(undo)
  if yes:return True
 return False
status='bounded search exhausted'
try:
 if search('',(0,0,0)):status='counterexample'
except RuntimeError:status='resource cap; no conclusion'
out={'status':status,'max_prefix_macros':DEPTH,'node_cap':CAP,'nodes':nodes,'feasible_prefix_counts':counts,'reused_feasible_first_Cs':terminal_old,'completion_tests':tests,'witness':witness,'seconds':time.monotonic()-start,'words_sha256':hashlib.sha256(json.dumps(WORDS,sort_keys=True).encode()).hexdigest()}
out['source_categories']=[{'macro':k[0],'phase':k[1],'heading_relative_to_C':k[2],'balanced_CC':k[3],'count':v,'shortest_suffix':SHORTEST[k]}for k,v in sorted(CATEGORIES.items())]
out['distinct_suffixes']=len(PATTERNS);out['suffix_counts']=dict(PATTERNS);out['unbalanced_examples']=UNBALANCED
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
