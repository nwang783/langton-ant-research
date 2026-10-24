"""Exact first leftover-input event for a supplied COMPLETE finite-prefix/canonical-tail certificate.
Finite control, but unbounded finite cohort geometry and exact segment lengths are retained.
"""
from check_return_permanent_output_debt import DXY,future
from blank_collision_operator import contains,materialize,H as CANON

def geometry(p,h,w):
 reads=[];heads=[]
 for ch in w:
  reads.append(p);heads.append(h);h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return reads,heads,p,h

def reference(seed,p,h,prefix,word):
 assert word in {CANON[i:]+CANON[:i]for i in range(104)}
 B=set(seed);q=p;hh=h
 for ch in prefix:
  assert(q in B)==(ch=='L')
  B.symmetric_difference_update({q});hh=(hh+(1 if ch=='R'else-1))%4;q=(q[0]+DXY[hh][0],q[1]+DXY[hh][1])
 fw,dr,_,tests=future({v:i for i,v in enumerate(B)},q,hh);assert fw==word
 P,PH,ep,eh=geometry(p,h,prefix);Q,QH,end,head=geometry(q,hh,word)
 assert head==hh and(end[0]-q[0],end[1]-q[1])==dr
 first={}
 for i,v in enumerate(P):first.setdefault(v,i)
 odd=set()
 for v in Q:odd.symmetric_difference_update({v})
 return dict(seed=set(seed),pose=(p,h),prefix=prefix,P=P,PH=PH,first=first,L=len(prefix),terminal=B,tail_pose=(q,hh),word=word,Q=Q,QH=QH,dr=dr,odd=odd,parity_tests=tests)

def first_hit(ref,A):
 answer=None;dx,dy=ref['dr']
 for v in A:
  t=ref['first'].get(v)
  for i,q in enumerate(ref['Q']):
   x,y=v[0]-q[0],v[1]-q[1]
   if x%dx==0 and y==(x//dx)*dy and x//dx>=0:
    tt=ref['L']+104*(x//dx)+i;t=tt if t is None else min(t,tt)
  if t is not None and(answer is None or t<answer[0]):answer=(t,v)
 return answer

def emitted_field(ref,t):
 if t<=ref['L']:
  B=set(ref['seed'])
  for q in ref['P'][:t]:B.symmetric_difference_update({q})
  return[(q,(0,0),1)for q in sorted(B)]
 k,r=divmod(t-ref['L'],104);dx,dy=ref['dr'];terms=[(q,(0,0),1)for q in sorted(ref['terminal'])]
 if k:terms.extend((q,(dx,dy),k)for q in sorted(ref['odd']))
 partial=set()
 for q in ref['Q'][:r]:partial.symmetric_difference_update({(q[0]+k*dx,q[1]+k*dy)})
 terms.extend((q,(0,0),1)for q in sorted(partial));return terms

def perturbation_event(ref,extra):
 A=set(extra);assert not(A&ref['seed']);hit=first_hit(ref,A)
 if hit is None:return dict(kind='CERTIFIED unchanged complete future',retained_unread_extra=sorted(A),reference_prefix_length=ref['L'],word=ref['word'],drift=ref['dr'])
 t,q=hit;terms=emitted_field(ref,t);assert not contains(terms,q)
 if t<ref['L']:hin=ref['PH'][t]
 else:hin=ref['QH'][(t-ref['L'])%104]
 hout=(hin-1)%4;pout=(q[0]+DXY[hout][0],q[1]+DXY[hout][1])
 new=terms+[(v,(0,0),1)for v in sorted(A)]+[(q,(0,0),1)]
 return dict(kind='EXACT first original-extra collision',time=t,cell=q,incoming_heading=hin,actual_turn='L',new_pose=(pout,hout),new_full_field_terms=new,remaining_original_extra=sorted(A-{q}))
