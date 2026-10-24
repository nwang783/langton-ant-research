"""Literal endpoint and core-value arithmetic; LN supplies source completeness."""
from pathlib import Path
import hashlib,json
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json'
RP=W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json'
G=json.loads(GP.read_text())['geometry'];R=json.loads(RP.read_text())
A=(0,22,20,10)
assert R['core_offsets']==list(A) and R['target']==7
assert R['target_global_phase']==1 and R['record_threshold']==30
T={(a,h):t for a,h,t in R['created_peaks']}
def rot(p,h):
 x,y=p
 return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def end(p,h,a):
 x,y,dh=G[a]['endpoint'];dx,dy=rot((x,y),h)
 return (p[0]+dx,p[1]+dy,(h+dh)%4)
def Q(p):
 x,y,h=p
 return 2*(y-x)+A[(h+1)%4]
source=(-1,0,3)
target_end=end((0,0),0,7)
vcc_end=end(source[:2],source[2],6)
assert target_end==(0,4,0) and vcc_end==(-5,0,1)
assert Q(target_end)==Q(vcc_end)==30
rows=[]
for a in (4,5,6):
 e=end(source[:2],source[2],a)
 rows.append(dict(packet=a,name=G[a]['name'],source=source,exit=e,
                  exit_core_value=Q(e),created_peak=2+T[a,0]))
assert [r['created_peak']for r in rows]==[10,22,30]
O=dict(status='AUTHOR_U1_YOUNG_VCC_BRANCH_STRICT_RECORD_BLOCKED',
       scope='LN plus the existing normalized U1 strict-record premise only; V and VC remain.',
       core_offsets=A,threshold=30,target_end=target_end,source_alternatives=rows,
       dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in [GP,RP,Path(__file__).resolve()]})
P=W/'chronology_dcuv/u1_record_young_pair_reduction.json'
P.write_text(json.dumps(O,indent=2)+'\n')
print({'threshold':30,'target_end':target_end,'VCC_exit':vcc_end,'source_alternatives':rows})
