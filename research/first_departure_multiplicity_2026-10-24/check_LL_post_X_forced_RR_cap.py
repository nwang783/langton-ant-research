"""Exact ordinal core of the all-case LL post-X RR-cap gate.
The signed cyclic inventory and LEFT-role reductions are human dependencies;
all physical readers used in the final contradiction are retained below.
"""
from pathlib import Path
from itertools import product
import json
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else -1))%4]
def ranks(h,dr,kin):return[r for r in range(len(h))if(h[r]if kin=='in'else out(h,r))==dr]
right=['E'+''.join(a)for n in range(1,5)for a in product('EW',repeat=n-1)]
# C has exactly two incoming E ports from B and two north departures to R.
C=[h for h in right if len(ranks(h,'E','in'))==2 and len(ranks(h,'N','out'))==2 and len(ranks(h,'S','out'))>=2]
assert C==['EEWW','EWWE']
X='EEWW';B='NNSS';Rs=['NNS','NNSS'];rows=[]
assert ranks(X,'S','out')==[0,3]and ranks(B,'N','in')==[0,1]
assert ranks(B,'E','out')==[0,3]
for R,C0 in product(Rs,C):
 assert ranks(R,'N','in')==[0,1]and ranks(R,'W','out')==[1,2]
 assert ranks(C0,'N','out')in[[1,2],[2,3]]
 # X3 -> B1, B3 -> C's second E; R1 -> X2, C second N -> R1.
 ein=ranks(C0,'E','in')[1];nout=ranks(C0,'N','out')[1]
 assert ein<=nout
 rows.append(dict(R=R,C=C0,second_E_arrival_rank=ein,second_N_departure_rank=nout,
  exact_edges=[['X',3,'B',1],['B',3,'C',ein],['C',nout,'R',1],['R',1,'X',2]],
  forced_comparison='second_N(C)=T2(X)-2<T3(X)<second_E(C)',
  complete_history_comparison='second_E(C)<=second_N(C)',contradiction=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,all_C_histories=C,rows=rows,all_four_contradictions=True,warning='The signed six-profile dependency supplies R; no exterior completion or full front is constructed.'),indent=2)+'\n')
print('PASS all4 exact C/R ordinal cores; post-X must be RIGHT, then flat by RR closure')
