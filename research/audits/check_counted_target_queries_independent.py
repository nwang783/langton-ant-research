from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1];W=P/'word_stabilization'
def rows(p,n):return {tuple(map(int,l.split()[:n])) for l in p.read_text().splitlines()}
ordinary=rows(W/'seven_sub_dcv_star4_kernel.tsv',5)
base=rows(W/'dcv_protected_patch2_kernel.tsv',7)
count=rows(W/'dcv_protected_kinematic_count_signedbase.tsv',8)
c=[0,1,2,3,0,1,2]
cases=json.loads((W/'dcv_conditional_confinement_optimized.json').read_text())['unproved_bad_transfers']
result=[]
for i,r in enumerate(cases,1):
 a,b=r['source_packet'],r['target_packet'];x,y,h=r['target_pose'];qx,qy=r['source_output'];t=(a,b,x,y,h,qx,qy)
 assert t[:5] not in ordinary and t not in base
 low=[]
 for k in range(4):
  impossible=k<c[a] or (h+k)%4!=0
  assert impossible or (*t,k) in count,(i,k)
  low.append('count/heading' if impossible else 'signed counted clause')
 assert (*t,4) not in count,i
 result.append({'index':i,'query':t,'low_count_exclusions':low,'overflow_excluded':False})
# Independently reconstruct raw movement and center increments from actual literals.
lines=(P/'audits/dcv_packet_literal.input').read_text().splitlines();words=[l.split()[0] for l in lines[1:8]]
D=words[0];C=words[1][len(D):];V=words[4]
def endpoint(w):
 p=0j;h=1j
 for s in w:h*=(-1j if s=='R' else 1j);p+=h
 return p,h
controls=[]
for name,w,expected in [('D',D,1+1j),('C',C,1+1j),('V',V,1+3j)]:
 p,h=endpoint(w);offset=-.5-.5j;center=p+offset*h/1j-offset
 assert center==expected,(name,p,h,center)
 controls.append({'macro':name,'word':w,'center_increment':[center.real,center.imag]})
files=['word_stabilization/dcv_protected_kinematic_count_signedbase.tsv','word_stabilization/seven_sub_dcv_star4_kernel.tsv','word_stabilization/dcv_protected_patch2_kernel.tsv','word_stabilization/dcv_conditional_confinement_optimized.json','word_stabilization/dcv_protected_count_kinematics.md','audits/check_counted_protected_clauses_independent.cpp']
out={'status':'PASS all 276 low-count queries excluded; all 69 overflow queries remain','cases':result,'center_controls':controls,'sha256':{p:hashlib.sha256((P/p).read_bytes()).hexdigest()for p in files}}
(P/'audits/counted_target_queries_independent.json').write_text(json.dumps(out,indent=2))
print(out['status'])
