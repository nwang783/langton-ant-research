from pathlib import Path
from fractions import Fraction
from collections import Counter
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'causal_archive_spatial_lifetime_2026-10-23';K={q for q,b in walk(mark)[2].items()if b};G={};IDS=(0,1,4,5,6,7,8,9)
for s in IDS:
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];bl={q for q,b in req.items()if b};G[s]=(bl-K,(bl^flip)-{e+rotation(q,h)for q in K})
assert sum(len(I)for I,O in G.values())==23 and sum(len(O)for I,O in G.values())==68
STEPS={rotation(z,h)for z in(1+1j,1+3j,4j)for h in range(4)};assert len(STEPS)==12
# Reconstruct actual corrected-center atomic displacements, including C.
atomC=raws[1][len(raws[0]):]
for word,z in[(raws[0],1+1j),(raws[4],1+3j),(raws[7],4j),(atomC,1+1j)]:
 e,h,_,_=walk(word);assert 2*e+rotation(-1-1j,h)-(-1-1j)==2*z

def det(a,b):return int(a.real*b.imag-a.imag*b.real)
def intersection(d,s,v):
 den=det(d,v)
 if den:
  t=Fraction(det(s,v),den);q=Fraction(det(s,d),den);return 0<=t<=1 and 0<=q<=1
 if det(s,d):return False
 if d==0j:
  if det(-s,v):return False
  f=(lambda z:int(z.real))if v.real else(lambda z:int(z.imag));return 0<=Fraction(f(-s),f(v))<=1
 f=(lambda z:int(z.real))if d.real else(lambda z:int(z.imag));a,b=sorted([Fraction(f(s),f(d)),Fraction(f(s+v),f(d))]);return max(a,0)<=min(b,1)

def candidates(d,margin=4):
 dx,dy=xy(d);found={}
 for x in range(min(0,dx)-margin,max(0,dx)+margin+1):
  for y in range(min(0,dy)-margin,max(0,dy)+margin+1):
   if(x+y)%2:continue
   s=complex(x,y);vs={v for v in STEPS if intersection(d,s,v)}
   if vs:found[(x,y)]=sorted(map(xy,vs))
 return found
cache={};rows=[];raw=0
for a,(ia,oa)in G.items():
 for o in oa:
  for b,(ib,ob)in G.items():
   for i in ib:
    for h in range(4):
     raw+=1;p=o-rotation(i,h)
     if(sum(xy(p))+h)%2:continue
     d=p+(rotation(-1-1j,h)+1+1j)/2;dx,dy=xy(d);assert d==complex(dx,dy)and(dx+dy)%2==0
     if d not in cache:cache[d]=candidates(d)
     M=len(cache[d]);bound=0 if d==0 else 4*M+11;rounded=0 if d==0 else bound-((bound+h)%4)
     rows.append(dict(source=a,output=xy(o),consumer=b,input=xy(i),heading=h,head=xy(p),delta=xy(d),M=M,bound=bound,rounded=rounded))
assert raw==6256 and len(rows)==3128 and len(cache)==72
assert max(map(len,cache.values()))==71 and max(r['bound']for r in rows)==295 and max(r['rounded']for r in rows)==294
maximizers=[r for r in rows if r['M']==71];assert len(maximizers)==3
for r in maximizers:assert r['source']==9 and r['output']==(0,7)and r['consumer']in(7,8,9)and r['input']==(-1,4)and r['heading']==2 and r['head']==(-1,11)and r['delta']==(0,12)and r['rounded']==294
# Compare all exact geometric candidate sets and role bounds, not just maxima.
author=json.loads((D/'thin_chord_lifetime_controls.json').read_text())
for x in author['all_candidate_entry_sites']:
 d=complex(*x['center_delta']);theirs={tuple(e['entry']):sorted(map(tuple,e['touching_vectors']))for e in x['entries']};assert cache[d]==theirs
for d in cache:assert candidates(d,5)==cache[d]
key=lambda r:(r['source'],tuple(r['output']),r['consumer'],tuple(r['input']),r['heading'])
theirs={(r['source'],tuple(r['output']),r['consumer'],tuple(r['input']),r['relative_heading']):(r['candidate_entry_count'],r['geometric_C_bound'],r['rounded_C_age_bound'])for r in author['all_roles']}
assert all(theirs[key(r)]==(r['M'],r['bound'],r['rounded'])for r in rows)
from math import gcd
for delta,sites in cache.items():
 x,y=xy(delta);du,dv=(x+y)//2,(x-y)//2;assert len(sites)<=25+4*max(abs(x),abs(y))+gcd(abs(du),abs(dv))
p=D/'thin_chord_spatial_lifetime.md';sha=hashlib.sha256(p.read_bytes()).hexdigest()
out=dict(status='PASS independent thin closing bridge and exact294-C produced lifetime',note_sha256=sha,raw_alignments=raw,sector_roles=len(rows),distinct_deltas=len(cache),maximum_M=71,geometric_bound=295,rounded_bound=294,maximizers=maximizers,geometry=[dict(delta=xy(d),sites=[dict(entry=s,vectors=v)for s,v in sorted(cs.items())])for d,cs in sorted(cache.items(),key=lambda z:xy(z[0]))],analytic_bridge='Finite simple P gives a small endpoint disk for B-W with no crossing. Candidate chords within span4 form a finite universe; positive distances of all chords disjoint from[A,B] permit uniform sufficiently small generic perturbation. W-A crosses only Q(d), at most once per actual distinct entry site. All other bridge/P contacts are excluded generically, so k<=M. Closing corners and atomic lift give n<=4k+11.',linear_bound='Under Lambda-to-Z2 coordinates D, swept-square area16+4L1(D), boundary16+2g gives M<=25+4L1(D)+g. Thus n<=16||d||infty+4g+111<=20||d||infty+111.',scope='Same simple retained factor, source FULL entry to consumer FULL entry C age; no entry-root age bound, global C/U budget or capture. Current produced IDs older than294 are unread for the remainder of that factor.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha,len(rows),len(cache),maximizers)
