"""Exact local missing-corner obstruction for ONE frozen OPEN F interface.
Read its numeric certificate; enumerate only complete WHITE histories1..8 at one cell.
Not a front, period, or global multiplicity scan.
"""
from pathlib import Path
from itertools import product
import json,hashlib
src=Path('/workspace/shared/langton/autonomous_controllers_2026-10-24/cap4_multiply_used_F_open_interface.json');z=json.loads(src.read_text());p=list(map(tuple,z['named_classes']));h=dict(zip(p,z['complete_named_heading_words']));t=z['representative_clocks'];P=z['clock_period'];assert z['full_drift']==[2,-2]
# Fixed physical L face LL(1,1): p=(1,1), q=(2,1), r=(2,2), s=(1,2).
# q is class(0,3)+d; r is unknown class(0,4)+d.
assert h[1,1]=='SSNS'and h[0,3]=='EEWE'and h[1,2]=='WWEW'
tp=t['7:3'];tq=t['8:3']+P;ts=t['9:3'];assert tq==tp+1 and tp==ts+1
Tin3=tq+1;Tout3=ts-1;assert Tin3-Tout3==4
H='NESW'
def output(w,i):return H[(H.index(w[i])+(1 if i%2==0 else-1))%4]
rows=[];feasible=[]
for n in range(1,9):
 for hh in product('NS',repeat=n):
  w=''.join(hh);inc=[i for i,x in enumerate(w)if x=='N'];dep=[i for i in range(n)if output(w,i)=='W']
  if len(inc)!=3 or len(dep)!=3:continue
  ir,orr=inc[2],dep[2];ok=ir==orr+1
  row=dict(headings=w,length=n,third_incoming_N_rank=ir,third_outgoing_W_rank=orr,can_have_input_minus_output_four=ok)
  rows.append(row)
  if ok:feasible.append(row)
assert {r['headings']for r in rows if r['length']<=4}=={'NNSN','SNNN'}
assert not any(r['length']in(5,6)for r in rows)
assert {r['headings']for r in feasible if r['length']==7}=={'NSSSSNN','SSNSSNN','SSSSNNN'}
assert min(r['length']for r in feasible)==7
obj=dict(scope=__doc__,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),physical_face_lower_left=[1,1],known_physical_histories={'1,1':'SSNS','2,1':'EEWE','1,2':'WWEW'},unknown_physical_cell=[2,2],unknown_quotient_class=[0,4],incoming_third_N_time=Tin3,outgoing_third_W_time=Tout3,required_difference=Tin3-Tout3,cap4_profiles=[r for r in rows if r['length']<=4],all_local_port_profiles_through8=rows,minimal_satisfying_profiles=[r for r in feasible if r['length']==7],minimum_reads=7,limitations='This rejects cap<=6 completion of the ONE named partial interface. It does not prove all F cycles are single-used, refute any all-cap theorem, construct a physical board factor, or assert seven-read exterior completion exists.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
