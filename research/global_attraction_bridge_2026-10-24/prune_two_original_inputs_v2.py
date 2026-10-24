"""Total mathematical <=2/first-three original-cohort interface.
Execution callers may supply a finite comparison budget; exhaustion is UNKNOWN,
not a negative result. Unbounded mathematical termination uses the signed
all-position at-most-two-black canonical theorem, never capture of the full input.
"""
from check_return_permanent_output_debt import DXY,future
from blank_collision_operator import H
PHASES={H[i:]+H[:i]for i in range(104)}

def comparison_certificate(seed,p=(0,0),h=0,budget=None):
 assert len(seed)<=2
 B={q:-i-1 for i,q in enumerate(sorted(seed))};pos=[];turns=[];first={};t=0
 while budget is None or t<budget:
  pos.append(p);first.setdefault(p,t);old=B.pop(p,None)
  if old is None:B[p]=t;h=(h+1)%4;turns.append('R')
  else:h=(h-1)%4;turns.append('L')
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1]);t+=1
  if t>=312 and t%104==0:
   w=''.join(turns[-104:])
   if w in PHASES and ''.join(turns[-312:])==w*3:
    try:fw,dr,_,tests=future(B,p,h)
    except AssertionError:continue
    if fw not in PHASES:continue
    w=fw
    reads=[];pp=p;hh=h
    for ch in w:
     reads.append(pp);hh=(hh+(1 if ch=='R'else-1))%4;pp=(pp[0]+DXY[hh][0],pp[1]+DXY[hh][1])
    return dict(seed=sorted(seed),prefix_length=t,prefix_word=''.join(turns),prefix_reads=pos,prefix_first=first,tail_pose=[p,h],tail_word=w,tail_reads=reads,tail_drift=dr,tail_black=sorted(B),ray_tests=tests)
 raise RuntimeError('UNKNOWN: supplied comparison execution budget exhausted')

def first_omitted_hit(cert,omitted):
 answer=None;dx,dy=cert['tail_drift']
 for q in omitted:
  time=cert['prefix_first'].get(q)
  for i,r in enumerate(cert['tail_reads']):
   a,b=q[0]-r[0],q[1]-r[1]
   if a%dx==0 and b==(a//dx)*dy and a//dx>=0:
    tt=cert['prefix_length']+104*(a//dx)+i;time=tt if time is None else min(time,tt)
  if time is not None and(answer is None or time<answer[0]):answer=(time,q)
 return answer

def prune2(board,p=(0,0),h=0,budget=None):
 original=set(board);selected=set();hits=[];comparisons=[]
 while True:
  cert=comparison_certificate(selected,p,h,budget);hit=first_omitted_hit(cert,original-selected)
  comparisons.append(dict(selected=sorted(selected),certified_prefix=cert['prefix_length'],tail_word=cert['tail_word'],tail_pose=cert['tail_pose'],tail_drift=cert['tail_drift'],ray_tests=cert['ray_tests'],first_omitted_hit=hit))
  if hit is None:
   # The omitted ORIGINAL bits are never read. Preserve every one in the real tail field.
   B=set(board);pp=p;hh=h
   for ch in cert['prefix_word']:
    old=pp in B;assert old==(ch=='L')
    if old:B.remove(pp);hh=(hh-1)%4
    else:B.add(pp);hh=(hh+1)%4
    pp=(pp[0]+DXY[hh][0],pp[1]+DXY[hh][1])
   w,dr,_,tests=future({q:i for i,q in enumerate(B)},pp,hh);assert w==cert['tail_word']and dr==cert['tail_drift']
   return dict(kind='EXACT whole original pruning <=2',relevant=sorted(selected),contacts=hits,comparisons=comparisons,full_board_tail=dict(cut=cert['prefix_length'],pose=[pp,hh],word=w,drift=dr,black=sorted(B),ray_tests=tests))
  t,q=hit;assert not hits or t>hits[-1]['time'];hits.append(dict(time=t,cell=q));selected.add(q)
  if len(selected)==3:return dict(kind='AT LEAST THREE original inputs',contacts=hits,comparisons=comparisons)

def sparse_interior_radius_test(board,R,p=(0,0),h=0,budget=None):
 assert R>=0
 inside={q for q in board if max(abs(q[0]-p[0]),abs(q[1]-p[1]))<=R}
 if len(inside)>2:raise ValueError('Unsupported: more than two current BLACK cells in the chosen box')
 cert=comparison_certificate(inside,p,h,budget);hit=first_omitted_hit(cert,set(board)-inside)
 return dict(rho_at_input_le_R=hit is None,first_outside_original_contact=hit,inside_black=sorted(inside),comparison_tail_cut=cert['prefix_length'])
