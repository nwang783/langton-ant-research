"""Independent literal output reconstruction and assembly of previously signed relations."""
from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/U_q_youngest_shadow_frozen_20261023_1717'
manifest=json.loads((B/'manifest.json').read_text())
for f in manifest['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
M=json.loads((B/'dependency_minclock.json').read_text());A=json.loads((B/'dependency_atomic_record.json').read_text())
K={q for q,b in walk(mark)[2].items() if b};I=[-1+1j,-1+2j,-1+4j,2j,3j];z=-1+3j;outputs={}
for src in (0,1,4,5,6,7,8,9):
 e,h,_,flip=walk(raws[src]);req=walk(raws[src]+mark)[2];before={q for q,b in req.items()if b};outputs[src]=(before^flip)-{e+rotation(q,h)for q in K}
 if src in (7,8,9):assert before-K==set(I)and req[z]is False and not(set(I)&set(walk(mark)[2]))
shadow=json.loads((ROOT/'audits/check_U_white_shadow_independent.json').read_text());covers=[{complex(*p)for p in pair}for pair in shadow['minimal_covers']]
def rebuild(c,h):
 r=c['last_producer'];x,y,hh=r['head'];assert hh==h
 O={complex(x,y)+rotation(q,h)for q in outputs[r['packet']]};mask=sum(1<<i for i,q in enumerate(I)if q in O)
 assert mask==r['output_mask']==c['minimum_age_input_mask'] and c['birth_packets']==1
 assert c['older_input_mask']&mask==0 and c['older_input_mask']|mask==31
 cover=[sorted(map(xy,p))for p in covers if p<=O]
 return dict(heading=h,packet=r['packet'],pose=r['head'],mask=mask,outputs=sorted(map(xy,O)),cover=cover,excluded=z in O and bool(cover))
raw2=next(x for x in M['phases']if x['heading']==2);R=[rebuild(c,2)for c in raw2['completed_abstract_states']]
assert {(r['packet'],tuple(r['pose']),r['mask'])for r in R}=={(s,(1,3,2),26)for s in (7,8,9)}and all(r['excluded']for r in R)
rows=[rebuild(c,p['heading'])for p in M['U1_strict_record_phases']for c in p['completed_abstract_states']]
counts=lambda filt:[sum(r['heading']==h and filt(r)for r in rows)for h in range(4)]
assert counts(lambda r:True)==[4,3,3,6]and counts(lambda r:not r['excluded'])==[4,3,0,4]
assert {(r['packet'],tuple(r['pose']),r['mask'])for r in rows if r['excluded']}=={*( (s,(1,3,2),26)for s in (7,8,9)),(7,(0,1,3),27),(8,(0,1,3),27)}
removed={(r['source'],tuple(r['pose']),r['youngest_input_mask'])for r in A['removed_q_youngest_templates']}
assert removed=={(r['packet'],tuple(r['pose']),r['mask'])for r in rows if r['heading']==0}
assert all(r['atomic_source_peak']==30 and r['C_age_residue']==0 and r['excluded_under_enlarged_history']for r in A['removed_q_youngest_templates'])
out=dict(status='PASS independent literal reconstruction and dependency-bound joint-shadow assembly',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),raw_phase_two=R,original_strict_counts=counts(lambda r:not r['excluded']),enlarged_history_counts=counts(lambda r:not r['excluded']and r['heading']!=0),strict_rows=rows,scope='Produced q youngest among all target identities, finite positive C age. Global residue-two exclusion independent of record. Original strict U1 eleven templates; separate enlarged-history seven. No q-older exclusion, merger budget or capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in ('raw_phase_two','strict_rows')})
