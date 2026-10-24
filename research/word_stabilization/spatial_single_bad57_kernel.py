"""Exact least-index-gap pair kernel for the six N-to-N return words.
Source read support is raw; target read support includes required next N marker.
No claim is made merely from failure of the discovery fixed point.
"""
from pathlib import Path
import json,time
start=time.time();M=json.load(open('spaced_two_marker_macros.json'))['macros'];N='RRRLLRLLRRRR';G=json.load(open('single_bad57_scc_grammar.json'));AL=tuple(G['alphabet']);G2={tuple(x)for x in G['pairs']};G3={tuple(x)for x in G['triples']};STEPS=(1j,1,-1j,-1)
def trace(w):
 p=0j;h=0;first={};last={}
 for c in w:
  if last.get(p)==c:return None
  first.setdefault(p,c);last[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=STEPS[h]
 return first,last,p,h
RAW={a:trace(M[a]['word'])for a in AL};TAR={a:trace(M[a]['word']+M[a]['end_marker'])for a in AL};F={a:set(RAW[a][0])for a in AL};TF={a:set(TAR[a][0])for a in AL}
def rot(z,h):return z*((-1j)**h)
def end(a,p=0j,h=0):return p+rot(RAW[a][2],h),(h+RAW[a][3])%4
def pair(a,p,h,b,q,k):
 d=rot(q-p,-h);return(a,b,int(d.real),int(d.imag),(k-h)%4)
def key(a,b,p,h):return(a,b,int(p.real),int(p.imag),h)
def aligned(p,h):return(int(p.real+p.imag)-h)%2==0
def feasible(w):
 if len(w)==2 and tuple(w)not in G2:return False
 if len(w)==3 and tuple(w)not in G3:return False
 return trace(''.join(M[a]['word']for a in w)+M[w[-1]]['end_marker'])is not None
GOOD2={(a,b)for a in AL for b in AL if feasible((a,b))};CAND=set()
for a in AL:
 for b in AL:
  for h in range(4):
   for q in F[a]:
    for z in TF[b]:
     p=q-rot(z,h)
     if aligned(p,h):CAND.add(key(a,b,p,h))
SHORT=set()
for a in AL:
 p,h=end(a)
 for b in AL:
  if(a,b)in GOOD2:SHORT.add(key(a,b,p,h))
  for c in AL:
   if feasible((a,c,b)):
    q,k=end(c,p,h);SHORT.add(key(a,b,q,k))
S=CAND-SHORT;BOUND={};CONFLICT={};READERS={}
for k in CAND:
 a,b,x,y,h=k;p=complex(x,y);cf=[p+rot(q,h)for q,c in TAR[b][0].items()if RAW[a][1].get(p+rot(q,h))==c];CONFLICT[k]=cf;options=[];pc,hc=end(a)
 for c in AL:
  if(a,c)not in GOOD2:continue
  for d in AL:
   if(d,b)not in GOOD2:continue
   hd=(h-RAW[d][3])%4;pd=p-rot(RAW[d][2],hd)
   options.append((key(a,d,pd,hd),pair(c,pc,hc,b,p,h),pair(c,pc,hc,d,pd,hd)))
 BOUND[k]=options
 for q in cf:
  if q in READERS:continue
  rr=set()
  for c in AL:
   for hc in range(4):
    for z in F[c]:
     pp=q-rot(z,hc)
     if aligned(pp,hc):rr.add((c,int(pp.real),int(pp.imag),hc))
  READERS[q]=rr
def cert(k,S):
 if all(any(p in S for p in op)for op in BOUND[k]):return('neighbors',)
 a,b,x,y,h=k
 for q in CONFLICT[k]:
  for c,cx,cy,ch in READERS[q]:
   if(a,c,cx,cy,ch)not in S and pair(c,complex(cx,cy),ch,b,complex(x,y),h)not in S:break
  else:return('equal-read',int(q.real),int(q.imag))
 return None
print('INITIAL',AL,len(CAND),len(SHORT&CAND),'GOOD2',sorted(GOOD2),flush=True);r=0
while True:
 proof={k:cert(k,S)for k in S};SS={k for k,v in proof.items()if v is not None};print('ROUND',r,'kernel',len(SS),'removed',len(S-SS),'seconds',round(time.time()-start,2),flush=True)
 if SS==S:break
 S=SS;r+=1
fresh={};open_alignments={}
for b in AL:
 fresh[b]=[];open_alignments[b]={}
 for q,c in TAR[b][0].items():
  if c!='L':continue
  pending=[]
  for a in AL:
   for h in range(4):
    for old in F[a]:
     p=old-rot(q,h);k=key(a,b,p,h)
     if aligned(p,h)and k not in S:pending.append(k)
  if not pending:fresh[b].append([int(q.real),int(q.imag)])
  else:open_alignments[b][str((int(q.real),int(q.imag)))]=sorted(set(pending))
out={'alphabet':AL,'source':'raw macro','target':'raw macro followed by its required end marker','candidate_count':len(CAND),'short_count':len(SHORT&CAND),'good_pairs':sorted(GOOD2),'rounds':r,'kernel':[list(k)+[proof[k]]for k in sorted(S)],'fresh_first_L_sites':fresh,'open_first_L_alignments':open_alignments};Path('spatial_single_bad57_kernel.json').write_text(json.dumps(out,indent=2));print('FRESH',fresh,'seconds',time.time()-start,flush=True)
