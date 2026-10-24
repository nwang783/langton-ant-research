"""Exact reader-count and physical rank-reversal check for one3-phase rail.
Full d=(-3,-3), all P open. No period, width, cap or drift scan.
"""
from pathlib import Path
from itertools import product
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def rr(h,d,k):return[i for i in range(len(h))if(h[i]if k=='in'else out(h,i))==d]
def words(ax):return[''.join(x)for n in range(1,5)for x in product(ax,repeat=n)]
l0=[h for h in words('EW')if len(rr(h,'W','in'))==0 and len(rr(h,'S','out'))==2]
l2=[h for h in words('EW')if len(rr(h,'W','in'))==2 and len(rr(h,'S','out'))==0]
assert set(l0)=={'EEE','EEEE'}and set(l2)=={'WEW','WEWE'}
qq=[]
for a,b in product(l0,l2):
 ni=len(rr(b,'N','out'));eo=len(rr(a,'E','in'))
 for h in words('NS'):
  if len(rr(h,'N','in'))==ni and len(rr(h,'E','out'))==eo:qq.append(dict(L0=a,L2=b,Q=h,N_in=ni,E_out=eo))
assert qq==[dict(L0='EEE',L2='WEW',Q=h,N_in=3,E_out=3)for h in ['NNNS','NSNN']]
traces=[]
for r in qq:
 hs={(0,0):'NSSN',(-1,0):r['L2'],(-1,1):r['Q'],(0,1):r['L0']};route=[((0,0),2)];cur=route[0]
 for _ in range(4):
  p,a=cur;d=out(hs[p],a);q=p[0]+V[d][0],p[1]+V[d][1];j=rr(hs[p],d,'out').index(a);b=rr(hs[q],d,'in')[j];cur=(q,b);route.append(cur)
 assert route==[((0,0),2),((-1,0),0),((-1,1),0),((0,1),0),((0,0),1)]
 traces.append(dict(complete_histories=[dict(cell=p,history=h)for p,h in hs.items()],actual_four_R_route=route))
h='SNNSN';assert len(rr(h,'N','in'))==3 and len(rr(h,'E','out'))==3 and rr(h,'N','in')[0]==1
obj=dict(scope=__doc__,full_drift=[-3,-3],fixed_RIGHT_rail=[dict(cell=[0,0],history='NSSN'),dict(cell=[1,1],history='NSN'),dict(cell=[2,2],history='NNN')],derived_helper_domains=dict(L0=l0,L2=l2),all_next_reader_count_completions=qq,literal_rank_reversals=traces,uncapped_local_counterprofile=dict(history=h,N_in=3,E_out=3,first_N_rank=1),warning='Exact fixed-rail obstruction only. The5-read counterprofile is not a full rail extension or front. Older/farther stock remains arbitrary; one of the three displayed helpers must exceed4.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS two helper domains -> two Q profiles -> universal4-R backward-rank return')
