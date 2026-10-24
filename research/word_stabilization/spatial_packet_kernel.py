"""No-seed spatial-pair kernel for non-C packets A C^k, k<=2.
Packet grammar requires every nonempty C suffix to be followed by V.
This is exploratory until a stable certificate receives independent replay.
"""
from verify_macro_word import D as RAW,rot,check
from pathlib import Path
import json,time
start=time.time();LETTERS='abcdefghijkl';WORDS={a:b+'C'*k for a,(b,k)in zip(LETTERS,[(b,k)for b in'UVQB'for k in range(3)])};D={}
for a,w in WORDS.items():
 trace=[];p=(0,0);h=0
 for b in w:
  for z in RAW[b]['trace']:
   x,y=rot(z['p'],h);trace.append({'p':(p[0]+x,p[1]+y),'c':z['c']})
  x,y,dh=RAW[b]['end_pose'];x,y=rot((x,y),h);p=p[0]+x,p[1]+y;h=(h+dh)%4
 D[a]={'trace':trace,'end_pose':(*p,h)}
F={};FIRST={};LAST={}
for a in LETTERS:
 first={};last={}
 for z in D[a]['trace']:q=tuple(z['p']);first.setdefault(q,z['c']);last[q]=z['c']
 F[a]=set(first);FIRST[a]=first;LAST[a]=last

def end(a,p=(0,0),h=0):
 x,y,dh=D[a]['end_pose'];x,y=rot((x,y),h);return((p[0]+x,p[1]+y),(h+dh)%4)
def pair(a,p,h,b,q,k):
 x,y=rot((q[0]-p[0],q[1]-p[1]),(-h)%4);return(a,b,x,y,(k-h)%4)
def feasible(w):
 if any(len(WORDS[a])>1 and WORDS[b][0]!='V'for a,b in zip(w,w[1:])):return False
 raw=''.join(WORDS[a]for a in w)+('V'if len(WORDS[w[-1]])>1 else'')
 try:check(raw)
 except AssertionError:return False
 return True
GOOD2={a+b for a in LETTERS for b in LETTERS if feasible(a+b)}
CAND=set()
for a in LETTERS:
 for b in LETTERS:
  for h in range(4):
   for q in F[a]:
    for z in F[b]:
     dx,dy=rot(z,h);x,y=q[0]-dx,q[1]-dy
     if(x+y-h)%2==0:CAND.add((a,b,x,y,h))
KEYS=sorted(CAND);ID={k:i for i,k in enumerate(KEYS)}
SHORT=set()
for a in LETTERS:
 p,h=end(a)
 for b in LETTERS:
  if a+b in GOOD2:SHORT.add((a,b,*p,h))
  for c in LETTERS:
   if feasible(a+c+b):q,k=end(c,p,h);SHORT.add((a,b,*q,k))
S={ID[k]for k in CAND-SHORT};BOUND={};CONFLICT={};READERS={}
for key in KEYS:
 a,b,x,y,h=key;i=ID[key];p=(x,y);conflicts=[]
 for q,c in FIRST[b].items():
  dx,dy=rot(q,h);z=(x+dx,y+dy)
  if LAST[a].get(z)==c:conflicts.append(z)
 CONFLICT[i]=conflicts;options=[];pc,hc=end(a)
 for c in LETTERS:
  if a+c not in GOOD2:continue
  for d in LETTERS:
   if d+b not in GOOD2:continue
   hd=(h-D[d]['end_pose'][2])%4;dx,dy=rot(D[d]['end_pose'][:2],hd);pd=(x-dx,y-dy)
   options.append((ID.get((a,d,*pd,hd),-1),ID.get(pair(c,pc,hc,b,p,h),-1),ID.get(pair(c,pc,hc,d,pd,hd),-1)))
 BOUND[i]=options
 for q in conflicts:
  if q in READERS:continue
  readers=set()
  for c in LETTERS:
   for hc in range(4):
    for z in F[c]:
     dx,dy=rot(z,hc);p=(q[0]-dx,q[1]-dy)
     if(sum(p)-hc)%2==0:readers.add((c,*p,hc))
  READERS[q]=readers

def certify(i,S):
 if all(any(p in S for p in option)for option in BOUND[i]):return('neighbors',)
 a,b,x,y,h=KEYS[i]
 for q in CONFLICT[i]:
  for c,cx,cy,ch in READERS[q]:
   if ID.get((a,c,cx,cy,ch),-1)not in S and ID.get(pair(c,(cx,cy),ch,b,(x,y),h),-1)not in S:break
  else:return('equal-read',*q)
 return None

MARK={}
for b in LETTERS:
 if len(WORDS[b])==1:continue
 base=WORDS[b][0];p=RAW[base]['end_pose'];dx,dy=rot((-1,0),p[2]);q=p[0]+dx,p[1]+dy
 assert q not in{tuple(z['p'])for z in RAW[base]['trace']};assert FIRST[b][q]=='L';MARK[b]=q

def targets(S):
 out=[]
 for key in KEYS:
  a,b,x,y,h=key
  if b not in MARK:continue
  dx,dy=rot(MARK[b],h);q=x+dx,y+dy
  if q in F[a] and ID[key]not in S:out.append(key)
 return out
print('WORDS',WORDS,flush=True)
print('INITIAL',len(CAND),'short',len(SHORT&CAND),'S',len(S),'open completed-C input pair types',len(targets(S)),'seconds',round(time.time()-start,2),flush=True)
r=0
while True:
 proofs={i:certify(i,S)for i in S};N={i for i,v in proofs.items()if v is not None}
 print('ROUND',r,'S',len(N),'removed',len(S-N),'open C-input pairs',len(targets(N)),'seconds',round(time.time()-start,2),flush=True)
 if N==S:break
 S=N;r+=1
out={'words':WORDS,'candidate_count':len(CAND),'short_pair_count':len(SHORT&CAND),'rounds':r,'kernel':[list(KEYS[i])+[proofs[i]]for i in sorted(S)],'unexcluded_completed_C_input_pairs':targets(S)}
Path(__file__).with_name('spatial_packet_kernel.json').write_text(json.dumps(out,indent=2))
print('DONE',len(S),'seconds',time.time()-start,flush=True)
