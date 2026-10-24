"""Exact geometric projection of supplied finite repeated words onto an augmented-hull record clock. Physical word legality is a separate premise."""
import json,sys
from pathlib import Path
P=Path(__file__).parent;U=P.parent/'causal_reduction/unit_scale'
V=[(0,1),(1,0),(0,-1),(-1,0)]
def trace(w,p=(0,0),h=1):
 q=[]
 for c in w:
  q.append(p);h=(h+(1 if c=='R' else -1))%4;dx,dy=V[h];p=(p[0]+dx,p[1]+dy)
 return q,p,h

def dot(p,a):return (p[1],p[0],-p[1],-p[0])[a]
def project(seed,p,h,stages):
 M=[max(dot(q,a)for q in seed|{p})for a in range(4)];T=0;regions=[]
 for name,w,C in stages:
  q,e,hh=trace(w,p,h);P0=len(w);d=(e[0]-p[0],e[1]-p[1]);assert C==1 or hh==h
  phases={};first=[]
  for a in range(4):
   vals=[dot(v,a)for v in q];B=max(vals);dd=dot(d,a);old=M[a]
   for i,v in enumerate(vals):
    if v>old:first.append((T+i,a));old=max(old,v)
   if dd>0 and C!=1:
    prefix=-10**100
    for i,v in enumerate(vals):
     if v>prefix and v>B-dd:
      lo=max(1,(M[a]-v)//dd+1)
      if C is None or lo<C:phases.setdefault(lo,[]).append((i,a))
     prefix=max(prefix,v)
   M[a]=max(M[a],B+(C-1)*dd if C and dd>0 else B)
  if first:regions.append(dict(stage=name,start=T,period=P0,lo=0,hi=1,phases=sorted((t-T,a)for t,a in first)))
  active=[];cuts=sorted(phases)
  for j,k in enumerate(cuts):
   active=sorted(active+phases[k]);end=cuts[j+1]if j+1<len(cuts)else C
   if end is None or k<end:regions.append(dict(stage=name,start=T,period=P0,lo=k,hi=end,phases=active[:]))
  if C is None:break
  T+=P0*C;p=(p[0]+C*d[0],p[1]+C*d[1]);h=hh
 return regions

def stats(reg,H):
 prev=None;count=0;long=[];tot=0
 for r in reg:
  P0,T,lo,hi,ph=r['period'],r['start'],r['lo'],r['hi'],r['phases'];n=None if hi is None else hi-lo
  # No two axis events can occur at one unit step.
  assert len(set(i for i,a in ph))==len(ph)
  first=T+P0*lo+ph[0][0]
  if prev is not None and first-prev>H:count+=1;long.append((prev,first,first-prev,r['stage'],'entry'))
  for (i,a),(j,b)in zip(ph,ph[1:]):
   if j-i>H:
    if n is None:count='infinite'
    elif count!='infinite':count+=n
    long.append((T+P0*lo+i,T+P0*lo+j,j-i,r['stage'],n))
  dg=P0+ph[0][0]-ph[-1][0]
  if dg>H and (n is None or n>1):
   if n is None:count='infinite'
   elif count!='infinite':count+=n-1
   long.append((T+P0*lo+ph[-1][0],T+P0*(lo+1)+ph[0][0],dg,r['stage'],None if n is None else n-1))
  if n is None:prev=None;break
  prev=T+P0*(hi-1)+ph[-1][0];tot+=n*len(ph)
 return dict(count=count,long=long,finite_event_count=tot)

def load(f,n):
 D=json.load(open(U/f));ev=lambda v:v[0]*n+v[1];seed={(ev(x),ev(y))for x,y in D['seed_families']};p=(ev(D['initial_pose']['x_N_constant']),ev(D['initial_pose']['y_N_constant']));h=D['initial_pose']['heading'];st=[(f'{i}:{s["kind"]}',s['word'],ev(s['count_N_constant']))for i,s in enumerate(D['stages'])]
 if f.startswith('prepared1564'):
  if n>=4:E=json.load(open(U/'prepared1564_source_endpoint_family.json'));w=E['after_checkpoint_word']
  else:E=json.load(open(U/f'prepared1564_endpoint_N{n}.json'));w=E['continuation_word']
  st.append(('end_response',w,1));st.append(('tail',E['capture_word'],None))
 else:st.append(('tail',D['tail_word'],None))
 return seed,p,h,st
