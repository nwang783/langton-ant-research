"""Discovery/certificate generator for a SAME-family forbidden spatial-pair kernel.
Earlier macro is C-free; later macro may also be a terminal C.
A fixed point proves impossibility by least macro-index gap, not by bounded search.
"""
from verify_macro_word import D,rot,check
from pathlib import Path
import json,time
CF='CUVQB';TARGETS=CF;start=time.time()
MARKS={a:set(map(tuple,v))for a,v in json.load(open(Path(__file__).with_name('cfree_kernel_current_marks.json'))).items()}
F={};FIRST={};LAST={}
for a in TARGETS:
 first={};last={}
 for z in D[a]['trace']:
  q=tuple(z['p']);first.setdefault(q,z['c']);last[q]=z['c']
 F[a]=set(first);FIRST[a]=first;LAST[a]=last

def end(a,p=(0,0),h=0):
 x,y,dh=D[a]['end_pose'];x,y=rot((x,y),h);return((p[0]+x,p[1]+y),(h+dh)%4)
def pair(a,p,h,b,q,k):
 x,y=rot((q[0]-p[0],q[1]-p[1]),(-h)%4);return(a,b,x,y,(k-h)%4)
def feasible(w):
 try:check(w)
 except AssertionError:return False
 return True
GOOD2={a+b for a in CF for b in TARGETS if feasible(a+b)}
# Every possible overlapping, correctly aligned pair.
CAND=set()
for a in CF:
 for b in TARGETS:
  for h in range(4):
   for q in F[a]:
    for z in F[b]:
     dx,dy=rot(z,h);x,y=q[0]-dx,q[1]-dy
     if True:CAND.add((a,b,x,y,h))
# Gaps1 and2 have to be excluded from a proposed forbidden family.
SHORT=set()
for a in CF:
 p,h=end(a)
 for b in TARGETS:
  if a+b in GOOD2:SHORT.add((a,b,*p,h))
  for c in CF:
   if feasible(a+c+b):
    q,k=end(c,p,h);SHORT.add((a,b,*q,k))
S=CAND-SHORT
DIRECT=set();BOUND={};CONFLICT={};READERS={}
for a,b,x,y,h in CAND:
 key=(a,b,x,y,h);p=(x,y)
 if b!='C' and any((x+rot(q,h)[0],y+rot(q,h)[1])in F[a]for q in MARKS[b]):DIRECT.add(key)
 conflicts=[]
 for q,c in FIRST[b].items():
  dx,dy=rot(q,h);z=(x+dx,y+dy)
  if LAST[a].get(z)==c:conflicts.append(z)
 CONFLICT[key]=conflicts
 options=[]
 pc,hc=end(a)
 for c in CF:
  if a+c not in GOOD2:continue
  for d in CF:
   if d+b not in GOOD2:continue
   hd=(h-D[d]['end_pose'][2])%4;dx,dy=rot(D[d]['end_pose'][:2],hd);pd=(x-dx,y-dy)
   options.append(((a,d,*pd,hd),pair(c,pc,hc,b,p,h),pair(c,pc,hc,d,pd,hd)))
 BOUND[key]=options
 for q in conflicts:
  if q in READERS:continue
  readers=set()
  for c in CF:
   for hc in range(4):
    for z in F[c]:
     dx,dy=rot(z,hc);p=(q[0]-dx,q[1]-dy)
     if True:readers.add((c,*p,hc))
  READERS[q]=readers
DIRECT=set()

def certify(key,S):
 if key in DIRECT:return('marked',)
 if all(any(p in S for p in option)for option in BOUND[key]):return('neighbors',)
 a,b,x,y,h=key
 for q in CONFLICT[key]:
  for c,cx,cy,ch in READERS[q]:
   if(a,c,cx,cy,ch)not in S and pair(c,(cx,cy),ch,b,(x,y),h)not in S:break
  else:return('equal-read',*q)
 return None

def targets(S):
 out=[]
 for key in CAND:
  a,b,x,y,h=key
  if b!='V':continue
  dx,dy=rot((1,2),h);q=x+dx,y+dy
  if q in F[a] and key not in S:out.append(key)
 return out
print('INITIAL',len(CAND),'short',len(SHORT&CAND),'direct',len(DIRECT),'S',len(S),'open V-tip pair types',len(targets(S)),flush=True)
r=0
while True:
 proofs={k:certify(k,S)for k in S};N={k for k,v in proofs.items()if v is not None}
 print('ROUND',r,'S',len(N),'removed',len(S-N),'open V-tip pairs',len(targets(N)),'seconds',round(time.time()-start,2),flush=True)
 if N==S:break
 S=N;r+=1
out={'candidate_count':len(CAND),'short_pair_count':len(SHORT&CAND),'direct_count':len(DIRECT),'rounds':r,'kernel':[list(k)+[proofs[k]]for k in sorted(S)],'unexcluded_V_tip_pairs':sorted(targets(S))}
Path(__file__).with_name('spatial_pair_kernel_full_five.json').write_text(json.dumps(out,indent=2))
print('DONE',len(S),'seconds',time.time()-start,flush=True)
