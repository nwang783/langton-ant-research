"""Exact finite-cap realizability checks for closed words in a supplied macro grammar.
Only the enumerated cycle lengths are excluded when no candidate is found.
"""
import json,sys,itertools,argparse
from pathlib import Path
from collections import defaultdict,Counter
from periodic_wake_fronts import D,T,W,add,orbit_key,background,certify_period
HERE=Path(__file__).resolve().parent
G=json.loads((HERE.parent/'word_stabilization/single_k_rrrllrllrlr_port_quotient.json').read_text())
adj=defaultdict(list)
for a,k,b in G['quotient_edges']:adj[a].append((k,b))
words=[m['word']for m in G['macro_words']]
F={(W+W)[i:i+10]for i in range(104)}

def compatible_caps(w):
 p=(0,0);h=0;ps=[]
 for c in w:
  ps.append(p);h=(h+(1 if c=='R' else -1))%4;p=add(p,D[h])
 if h or not p[0] or abs(p[0])!=abs(p[1]):return [],'not_diagonal'
 L=len(w);out=[]
 for hh in range(4):
  def rot(q):
   for _ in range(hh):q=(q[1],-q[0])
   return q
  drift=rot(p)
  if drift[0]!=drift[1]:continue
  reads=[rot(q)for q in ps];gr=defaultdict(list)
  for i,q in enumerate(reads):
   c,k=orbit_key(q,drift);gr[c].append((k,i,w[i]))
  for seq in gr.values():
   seq.sort(key=lambda z:(-z[0],z[1]))
   if any(a[2]==b[2]for a,b in zip(seq,seq[1:])):break
  else:
   Lclass=[c for c,seq in gr.items()if seq[0][2]=='L']
   if not Lclass:
    if len(w)%104==0 and w==(w[:104]*(len(w)//104)) and w[:104] in W+W:
     continue
    raise AssertionError(('NONSTANDARD finite-white periodic candidate',w,drift))
   # One required-L orbit must hit the transverse span of T. This is exhaustive.
   t0=Lclass[0][0]-Lclass[0][1]
   for offset in range(-3-t0,8-t0):
    for parity in (0,1):
     q=(parity,parity-offset)
     if (hh-q[0]-q[1])%2!=1:continue
     if any(background(add(add(c,q),(n*drift[0],n*drift[1])))!=(seq[0][2]=='L')for c,seq in gr.items()for n in(0,1)):continue
     cap=set()
     for c,seq in gr.items():
      mn=min(k for k,i,s in seq);mx=max(k for k,i,s in seq)
      for n in range(mn,mx):
       s=next(s for k,i,s in seq if k<=n)
       cell=add(add(c,q),(n*drift[0],n*drift[1]))
       if background(cell)!=(s=='L'):cap.add(cell)
     cert=certify_period(w,q,hh,cap);assert cert
     ww=w*max(3,(11+2*L-1)//L)
     bad=[ww[i:i+10]not in F for i in range(L)]
     cert['K_per_period']=sum(bad[i-1]and bad[i]for i in range(L))
     out.append({'pose':[q,hh],'cap':sorted(cap),'certificate':cert})
 return out,'diagonal'

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--depth',type=int,default=10);args=ap.parse_args()
 seen=set();stats=Counter();found=[]
 for start in range(G['classes']):
  colors={}
  def walk(s,ks,p,h):
   stats['feasible_prefixes']+=1
   if ks and s==start:
    canonical=min(tuple(ks[i:]+ks[:i])for i in range(len(ks)))
    if canonical not in seen:
     seen.add(canonical);w=''.join(words[k]for k in ks);caps,kind=compatible_caps(w);stats[kind]+=1
     if caps:
      hit={'macro_cycle':ks[:],'word':w,'realizations':caps};found.append(hit);print(json.dumps(hit),flush=True)
   if len(ks)<args.depth:
    for k,t in adj[s]:
     changes=[];pp=p;hh=h;valid=True
     for ch in words[k]:
      old=colors.get(pp)
      if old==ch:
       valid=False;break
      changes.append((pp,old));colors[pp]=ch
      hh=(hh+(1 if ch=='R' else -1))%4;pp=add(pp,D[hh])
     if valid:walk(t,ks+[k],pp,hh)
     else:stats['infeasible_pruned']+=1
     for cell,old in reversed(changes):
      if old is None:del colors[cell]
      else:colors[cell]=old
  walk(start,[],(0,0),0)
 out={'scope':'closed macro cycles through stated number of macro edges only; finite-cap realizability test exact for each word','max_macro_edges':args.depth,'cycles':len(seen),'stats':dict(stats),'found':found}
 (HERE/'wake_macro_cycles.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k!='found'},indent=2),flush=True)
if __name__=='__main__':main()
