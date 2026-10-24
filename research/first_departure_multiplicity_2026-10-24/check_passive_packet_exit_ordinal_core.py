"""Correct physical four-edge ordinal collision at a proposed passive
singleton immediately after the unique flat-passive LL packet.
"""
from pathlib import Path
import json
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def rr(h,d,k):return[r for r in range(len(h))if(h[r]if k=='in'else out(h,r))==d]
A,E,R='EWWE','NNSS','NNSS';rows=[]
assert rr(A,'S','out')==[0,1]and rr(E,'S','in')==[2,3]
assert rr(E,'E','out')==[0,3]
assert rr(R,'W','out')==[1,2]and rr(A,'W','in')==[1,2]
for C in ['EEWW','EWWE']:
 ei=rr(C,'E','in')[1];no=rr(C,'N','out')[1]
 assert ei<=no and rr(R,'N','in')==[0,1]
 rows.append(dict(C=C,edges=[['A',1,'E',3],['E',3,'C',ei],['C',no,'R',1],['R',1,'A',1]],forced_cycle_duration=4,contradiction='C.secondE<=C.secondN but secondE=A1+2 and secondN=A1-2'))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,rows=rows,all_physical_directions_checked=True,warning='Cyclic role reductions are separate signed human dependencies; no actual factor or whole front is constructed.'),indent=2)+'\n');print('PASS both literal C ordinal contradictions')
