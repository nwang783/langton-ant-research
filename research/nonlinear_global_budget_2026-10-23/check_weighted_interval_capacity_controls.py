#!/usr/bin/env python3
"""Finite controls and explicit countercontrols for the CONDITIONAL weighted
spatial interval ledger. Analytic inequalities, not these samples, give its
scope. No universal anchor, confinement or refunded-cap bound is inferred.
"""
from pathlib import Path
import json,hashlib
P=Path(__file__).parent;M=20000000;V=((0,1),(1,0),(0,-1),(-1,0))
H=json.loads((P.parent/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];A=json.loads((P/'prepared_travelling_wave_certificate.json').read_text());B=json.loads((P/'second_prepared_wave_certificate.json').read_text())
factors={''.join(H[(i+j)%104]for j in range(10))for i in range(104)}
def trace(w,p=(0,0),h=0):
 out=[]
 for ch in w:
  out.append((p,h,ch));h=(h+(1 if ch=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1]
 return out,p,h
def wb_delta(rows,c,R):
 tot=0
 for q,_,ch in rows:
  d=abs(q[0]-c[0])+abs(q[1]-c[1]);assert d<=R;tot+=(1 if ch=='R'else-1)*(M+R-d)
 return tot
def infer(rows):
 first={};par=set()
 for q,_,ch in rows:
  w=(ch=='L')^(q in par)
  if q in first:assert first[q]==w
  else:first[q]=w
  par.symmetric_difference_update({q})
 return {q for q,w in first.items()if w}
def invhist(B,p,h):
 B=set(B);rev=[]
 for _ in range(10):
  v=V[h];q=p[0]-v[0],p[1]-v[1];ch='R'if q in B else'L';B.symmetric_difference_update({q});h=(h-(1 if ch=='R'else-1))%4;p=q;rev.append(ch)
 return ''.join(reversed(rev))
def count(w,hist):
 bad=hist not in factors;k=0
 for ch in w:
  hist=(hist+ch)[-10:];b=hist not in factors;k+=bad and b;bad=b
 return k
positive=[]
for name,w,start,h in [('H',H,(0,0),i)for i in range(4)]+[('w1564',A['word'],tuple(A['wave_pose'][0]),A['wave_pose'][1]),('w4352',B['word'],tuple(B['wave_pose'][0]),B['wave_pose'][1])]:
 rows,_,_=trace(w,start,h);delta=wb_delta(rows,(0,0),10000);assert delta>=len(w)
 positive.append({'word':name,'heading':h,'length':len(w),'black_gain':w.count('R')-w.count('L'),'weighted_black_gain':delta})
negative=[]
for n in[3,4,11,50]:
 w='RLLR'*n;rows,_,_=trace(w);S=infer(rows);assert S=={(1,y)for y in range(2*n)}
 center=(1,n);delta=wb_delta(rows,center,4*n+10);assert delta==-2*n
 k=count(w,invhist(S,(0,0),0));assert k>=4*n-10
 negative.append({'n':n,'input_mass':len(S),'anchor':'rounded seed bounding-box center(1,n)','weighted_black_gain':delta,'Phi_increase':-delta,'true_history_K':k,'status':'actual legal outward transport refutes automatic inwardness for this anchor'})
# Every S arm of the full signed spiral is inward at c=(-n-1,n),
# while inner east arms move away from c=(0,0). Literal geometry is rebuilt.
spiral=[]
for n in[2,4,11,30]:
 p=(0,0);h=0;allrows=[];details=[]
 for k in range(n):
  j=n-k
  for a,corner in enumerate(['L','RLL','L','L']):
   rows,p,h=trace('RLLR'*j,p,h);di=wb_delta(rows,(-n-1,n),10*n+20);assert di==2*j
   dh=wb_delta(rows,(0,0),10*n+20)
   if a==3 and k>=1:assert dh==-2*j
   details.append([k,a,j,di,dh]);allrows+=rows;rr,p,h=trace(corner,p,h);allrows+=rr
 S=infer(allrows);assert len(S)==11*n+2
 spiral.append({'n':n,'initial_mass':len(S),'every_inward_arm_gain_is_2j':True,'head_anchor_has_outward_inner_east_arms':True,'arm_values':[{'circuit':k,'arm':a,'periods':j,'correct_anchor_delta':di,'head_anchor_delta':dh}for k,a,j,di,dh in details]})
# Exact cyclic H spans for finite repaint lower bounds.
canonical,_,_=trace(H,(0,0),1);spans=[]
from collections import defaultdict
for phase in range(104):
 pp,hh,_=canonical[phase];rr,_,_=trace(H[phase:]+H[:phase],pp,hh);gg=defaultdict(list)
 for (x,y),_,_ in rr:gg[x-y,x%2].append(x//2)
 spans.append(max(max(g)-min(g)for g in gg.values()))
assert min(spans)==2 and max(spans)==3
out={'standard_all_cyclic_phase_maximum_slot_spans':spans,'scope':__doc__,'M':M,'analytic_positive_word_guard':M>=4352**2+4352,'positive_bulk_controls':positive,
 'actual_seed_centroid_anchor_countercontrols':negative,'signed_spiral_anchor_controls':spiral,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'weighted_interval_capacity_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS local weighted inequalities; both natural fixed-anchor countercontrols retained')
