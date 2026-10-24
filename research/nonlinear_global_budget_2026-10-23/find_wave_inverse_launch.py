#!/usr/bin/env python3
"""Finite backward-prefix search; only future-wave-unread initial cells adjustable.
A positive result is an exact complete-field inverse-H certificate, never inferred
from a timeout or local match. Bounded negative result is only bounded scope.
"""
from pathlib import Path
from collections import defaultdict,deque
import runpy,json,time
ROOT=Path(__file__).parent;C=runpy.run_path(str(ROOT/'certify_prepared_travelling_wave.py'));E=C['E'];N=json.loads((ROOT/'prepared_wave_five_band_normal_form.json').read_text());J=json.loads((ROOT/'prepared_travelling_wave_certificate.json').read_text());B={tuple(j)for j in N['full_black_orbit_profiles']};basecap={tuple(q)for q in N['finite_XOR_cap']};V=E['V'];p=tuple(N['pose'][0]);h=N['pose'][1];startp=(p[0]-V[h][0],p[1]-V[h][1]);starth=(h+2)%4
# Exact full future READ membership, including finite eligibility fringe.
G=defaultdict(list);pp=p;hh=h
for i,ch in enumerate(J['word']):
 x,y=pp;t=x-y;a=x%14;k=(x-a)//14;G[t,a].append(k);hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
G={j:min(k)for j,k in G.items()}
def future_read(q):
 x,y=q;j=(x-y,x%14);return j in G and (x-x%14)//14>=G[j]
def initial(q):return ((q[0]-q[1],q[0]%2)in B)^(q in basecap)
def color(q,rows,F):return ((q[0]-q[1],q[0]%2)in B)^(q in F)
C['cert_parallel'].__globals__['color']=color
# All exact time-reversed standardB phases, not spatialoppositeH.
targets=defaultdict(list);tr=(0,-26)
for i,(q,head)in enumerate(zip(E['PH'],E['HD'])):
 qi=(q[0]+tr[0]-V[head][0],q[1]+tr[1]-V[head][1]);hi=(head+2)%4;w=''.join('L'if E['H'][(i-1-j)%104]=='R'else'R'for j in range(104));targets[qi[0]-qi[1],qi[0]%2,hi].append((i,w))
def goal(q,h,edits,flips):
 f=basecap^edits^flips
 for i,w in targets.get((q[0]-q[1],q[0]%2,h),[]):
  # Fastnecessary16-turn prefix check on wholefield.
  qq=q;hh=h;temp=set();ok=True
  for ch in w[:16]:
   if color(qq,{},f)^(qq in temp)!=(ch=='L'):ok=False;break
   E['toggle'](temp,qq);hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];qq=(qq[0]+v[0],qq[1]+v[1])
  if not ok:continue
  cert=C['cert_parallel']({},f,q,h,w)
  if cert:return{'original_H_phase':i,'inverse_word':w,'certificate':cert}
 return None
queue=deque([(startp,starth,frozenset(),frozenset(),frozenset(),'')]);count=0;found=None;start=time.time();maxdepth=32;maxnodes=150000;depthcounts=defaultdict(int)
while queue and count<maxnodes:
 q,h,edits,flips,seen,word=queue.popleft();count+=1;depthcounts[len(word)]+=1
 g=goal(q,h,set(edits),set(flips))
 if g:
  found={'prefix':word,'backward_pose':[list(q),h],'initial_wave_XOR_edits':sorted(edits),'prefix_flip_mask':sorted(flips),**g};break
 if len(word)==maxdepth:continue
 constrained=future_read(q)or q in seen
 init=initial(q)^(q in edits);b=init^(q in flips)
 choices=[b]if constrained else[b,not b]
 for wanted in choices:
  ee=set(edits)
  if wanted!=b:E['toggle'](ee,q)
  ff=set(flips);E['toggle'](ff,q);hh=(h+(-1 if wanted else 1))%4;v=V[hh];qq=(q[0]+v[0],q[1]+v[1]);u=qq[0]+qq[1];t=qq[0]-qq[1]
  if not(-60<=u<=30 and -12<=t<=20):continue
  queue.append((qq,hh,frozenset(ee),frozenset(ff),seen|{q},word+('L'if wanted else'R')))
report={'scope':'Bounded finite inverse-prefix search on fixed normalform; only cells outside ENTIREfuturewaveREAD set edited. Negative is not no-launch.','result':found,'nodes':count,'queue_remaining':len(queue),'depth_counts':dict(depthcounts),'bounds':{'depth':maxdepth,'nodes':maxnodes,'u':[-60,30],'t':[-12,20]},'elapsed_seconds':time.time()-start};(ROOT/'wave_inverse_launch_search.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
