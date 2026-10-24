from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'foreign_U_raw_ages34_2026-10-23'
ns={'__file__':str(R/'audits/check_foreign_U_tag_interfaces_independent.py')};exec(Path(ns['__file__']).read_text().split('results={}')[0],ns)
G,W,K,L,at,xy=(ns[k]for k in('G','W','K','L','at','xy'));guards={-1j,-1};assert G['U']['rawreads'][-1][-1]==(1,'L')and G['U']['rawreads'][-1j][-1]==(3,'L')
for a in'DCVU':assert all(q.imag>=0 and q.real+q.imag>=0 for q in G[a]['O'])
assert G['C']['I']==set()and G['C']['O']=={1+2j,2,2+1j}
rows=[]
for h in(2,1,0):
 for q in guards:
  for a in('DVUC'if h else'DVU'):
   for slot in G[a]['O']:
    p=q-slot*(-1j)**h;ep=p+G[a]['p']*(-1j)**h;hits=L&{p+z*(-1j)**h for z in G[a]['ctx']}
    if(int(p.real+p.imag)+h)%2:why='sector'
    elif hits:why='held_star'
    elif h==2:
     assert(q,a,slot,p)==(-1,'U',-1+2j,-2+2j);assert slot in G[a]['I']and G[a]['rawreads'][slot][:2]==[(13,'L'),(21,'R')];why='strict_earlier_same_cell_residual'
    elif h==1:raise AssertionError('unexpected E origin')
    else:assert ep.imag>=2;why='N_endpoint_y_at_least2'
    rows.append((h,xy(q),a,xy(slot),xy(p),xy(ep),why))
co={h:Counter(r[-1]for r in rows if r[0]==h)for h in(2,1,0)};assert co[2]=={'sector':18,'held_star':19,'strict_earlier_same_cell_residual':1}and co[1]=={'sector':20,'held_star':18}and sum(co[0].values())==32 and co[0]['N_endpoint_y_at_least2']==4
prior=json.loads((R/'foreign_U_star_predecessors_2026-10-23/foreign_U_star_predecessors.json').read_text());gates={}
for r in prior['rows']:
 if r['reason']!='necessary_interface_not_asserted_attained':continue
 a=r['foreign'];p=complex(*r['foreign_pose'][:2]);h=r['foreign_pose'][2]
 if h not in(0,1):continue
 tags=L&{at(q,p,h)for q in G[a]['I']};rawtags={q for q in tags if(q-p)*(1j)**h in G[a]['rawreads']}
 if not rawtags:continue
 inputs={at(q,p,h)for q in G[a]['I']};hit=inputs&guards;assert hit
 if h==0:assert p.imag<0
 gates[(a,*xy(p),h)]=[xy(q)for q in hit]
assert len(gates)==24 and Counter(k[-1]for k in gates)=={1:15,0:9}
assert{(x,y)for a,x,y,h in gates if h==0}=={(3,-3),(2,-2),(5,-3)}
m=D/'manifest.json';sha=hashlib.sha256(m.read_bytes()).hexdigest();assert sha=='9fdbb997d06af051d91b8e907df8dbfe175dfd34d8e8b70a7b74a78278bc887b'
for f,h in json.loads(m.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
report={'status':'PASS no first-foreign RAW original-U-star effect at C ages3/4','manifest_sha256':sha,'role_counts':{str(h):dict(c)for h,c in co.items()},'gates':[{'pose':k,'guard_inputs':v}for k,v in gates.items()],'analytic':['Both guarded cells were actually deleted by creating U. Any later current residual outside active core must arise through a genuine subsequent net-output event, not untouched entry stock or mere transient core occupancy. Literal N-y and W-H cones exclude all origins through the first two C increments, including actual internal source tails.','At S phase the only unblocked output role is U(-2,2,S) recycled q at physical c=(-1,0). Its same physical cell is a true residual INPUT readL13 before outputR21. Earliest new residual rebirth therefore cannot be this role. This is a well-founded finite-history descent, not a claim that the physical cell remains white during all fine steps. E phase has no role, including actual C4 outputs.','All15 E RAW-erosion gates require one of these cells as a black residual input. At age4 only plain N D/V/U output producers can finish before foreign; all4 unblocked roles finish at y>=2, while all9 N RAW gates have negative y. N zero-C motion cannot lower y. Positive-C source tails overshoot the actual full foreign entry and are not ignored.','Combining separately signed ages0..2 and marker lower clocks gives necessary source-entry C age>=5 for any first-foreign original-star RAW retirement or marker-only absorption. This is not attainment at5, an all-age erosion exclusion, or postforeign permanence.'],'scope':'Genuine U/UC/UCC creator, uninterrupted actual complete8 history to its FIRST foreign. No first-center-contact premise, age scan, global seven-word budget or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(co)
