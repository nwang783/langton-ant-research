#!/usr/bin/env python3
"""One genuinely transverse standard attack on COMPLETE actual15324 output.
Infinite prepared profile discovery, not a finite-seed realization.
"""
from pathlib import Path
from collections import defaultdict
from math import gcd
import json,sys,hashlib,time
P=Path('/workspace/shared/langton');O=Path(__file__).parent
J=json.loads((P/'causal_reduction/unit_scale/prepared15324_known_output_consumers.json').read_text())
S={tuple(q) for q in J['sources']['actual_five_band_15324_output']['complete_output_profiles']}
V=((0,1),(1,0),(0,-1),(-1,0))
def rot(q):return(-q[1],q[0])
def color(q,F):return (((q[0]-q[1],q[0]%78) in S) ^ (q in F))
def step(F,p,h):
 c='L' if color(p,F) else 'R';F.symmetric_difference_update({p});h=(h+(-1 if c=='L' else 1))%4;v=V[h];return(p[0]+v[0],p[1]+v[1]),h,c

def base():
 B=set();p=(0,0);h=0
 for _ in range(9977):
  c=p in B;B.symmetric_difference_update({p});h=(h+(-1 if c else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
 entry=p;h0=h;read=set();bb=set(B)
 for _ in range(104):
  read.add(p);c=p in bb;bb.symmetric_difference_update({p});h=(h+(-1 if c else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
 return {(q[0]-entry[0],q[1]-entry[1]) for q in B&read},h0

def suffixperiod(w):
 w=w[-300000:];pi=[0]*len(w)
 for i in range(1,len(w)):
  j=pi[i-1]
  while j and w[i]!=w[j]:j=pi[j-1]
  if w[i]==w[j]:j+=1
  pi[i]=j
 return len(w)-pi[-1]

def certify(F,p,h,w):
 p0=p;h0=h;G=defaultdict(list)
 slots=[]
 for i,c in enumerate(w):
  slots.append((p,i,c));h=(h+(-1 if c=='L' else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
 d=(p[0]-p0[0],p[1]-p0[1])
 if h!=h0 or not d[0] or d[0]!=d[1]:return None
 s=abs(d[0])
 for q,i,c in slots:
  a=q[0]%s;G[q[0]-q[1],a].append(((q[0]-a)//d[0],i,c))
 FI=defaultdict(set)
 for q in F:
  a=q[0]%s;FI[q[0]-q[1],a].add((q[0]-a)//d[0])
 checks=0
 for(t,a),g in G.items():
  g.sort(key=lambda z:(-z[0],z[1]));mn=min(z[0]for z in g);mx=max(z[0]for z in g)
  if any(x[2]==y[2]for x,y in zip(g,g[1:])):return None
  for n in range(mn,mx):
   c=next(z[2]for z in g if z[0]<=n);q=(a+n*d[0],a-t+n*d[1]);checks+=1
   if color(q,F)!=(c=='L'):return None
  per=78//gcd(s,78);tests=set(range(mx,mx+per)) | {n for n in FI[t,a] if n>=mx}
  # All finite-exception n and enough unaffected representatives of each residue.
  for r in range(per):
   n=mx+r
   while n in FI[t,a]:n+=per
   tests.add(n)
  for n in tests:
   q=(a+n*d[0],a-t+n*d[1]);checks+=1
   if color(q,F)!=(g[0][2]=='L'):return None
 return {'period':len(w),'drift':d,'read_orbits':len(G),'complete_input_checks':checks,'normal_read_hull':[min(q[0]-q[1]for q,i,c in slots),max(q[0]-q[1]for q,i,c in slots)]}

def main(u=0,steps=1000000):
 started=time.time();assert u%2==0;p=((u-80)//2,(u+80)//2);B,h=base();h=(h-1)%4;F={(p[0]+rot(q)[0],p[1]+rot(q)[1])for q in B};initialF=set(F);initialp=p;initialh=h;out=[]
 for _ in range(steps):p,h,c=step(F,p,h);out.append(c)
 w=''.join(out);per=suffixperiod(w);report={'scope':__doc__,'incoming_u':u,'initial_pose':[initialp,initialh],'complete_profile_black_classes':len(S),'steps':steps,'suffix_period':per,'final_pose':[p,h],'finite_xor_mass':len(F),'elapsed':time.time()-started}
 if per<150000:
  i=len(w)-1
  while i>=per and w[i]==w[i-per]:i-=1
  st=i-per+1;report['periodic_sample_begin']=st
  F=set(initialF);p=initialp;h=initialh
  for c in w[:st]:p,h,cc=step(F,p,h);assert cc==c
  cw=w[st:st+per];report['word']=cw;report['candidate_pose']=[p,h];report['certificate']=certify(F,p,h,cw)
 (O/f'transverse15324_u{u}.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k!='word'},indent=2))
if __name__=='__main__':main(*[int(s)for s in sys.argv[1:]])
