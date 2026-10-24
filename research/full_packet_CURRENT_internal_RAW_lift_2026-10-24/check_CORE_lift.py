"""Physical identity bookkeeping, no new ant-language exclusion."""
from pathlib import Path
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
def ld(n,p):
 s=importlib.util.spec_from_file_location(n,R/p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=ld('l','word_stabilization/check_foreign_return_interfaces.py');o=ld('o','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS
C=l.trace(W['C']);core=[]
for q in sorted(l.K):
 f=C['first'][q];assert f[0]=='L'and f[1]<6;core.append(dict(incoming_CORE_cell=q,actual_C_first_L_tick0=f[1],actual_C_first_L_read1=f[1]+1))
rows=[]
for full in ['D','DC','V','VC','VCC','U','UC','UCC']:
 for i in range(1,len(full)):
  assert full[i]=='C';rows.append(dict(actual_full_packet=full,internal_RAW_cut_after=full[:i],actual_next_RAW_inside_same_packet='C',all5_CORE_originals_physically_deleted_before_same_full_completion=True))
assert len(rows)==7
out=dict(status='AUTHOR_FROZEN_PENDING_REVIEW',scope='Only SAME physical identities in actual complete-eight full packets; no new maturity or proxy-contact theorem.',all5_actual_next_C_CORE_first_L_reads=core,all7_internal_RAW_cut_interfaces=rows,lemma='If a SAME identity is CURRENT at an actual full-packet entry or its true fresh birth and is again CURRENT as that SAME identity at the full exit, it was CURRENT at every intermediate RAW cut after birth. Physical death is irreversible for that birth label. Any intermediate CORE capture is physically deleted by the next actual C in its first six reads before full completion, so cannot reappear as the SAME final CURRENT identity. A recoloring by R has a new label. For a plain full BASE there is no internal cut.',application_to_b224='Before FIRSTFOREIGN, signed original source-bud min5 supplies SAME bud CURRENT at all actual full cuts through source-entry age4. The actual completed full word containing an earlier physical writer therefore supplies this internal-RAW currentness too. Own creatingU C tails preserve the SAME bud by literal last-R equality; their direct preservation remains separately checked. This justifies the independently CURRENT anchor inside physical hole-origin filters without identifying CORE absorption with immediate physical death.',not_claimed=['No claim of currentness from mere final BLACK color','No invariant across a consuming foreign','No CORE-to-physical-death shortcut at the earlier cut','No uncompleted positive-C packet may be treated as completed before the foreign'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'word_stabilization/check_foreign_return_interfaces.py']})
(H/'CORE_lift.json').write_text(json.dumps(out,indent=2)+'\n');print('Same-full-packet CURRENT lift:5 real CORE L reads and7 internal cuts; no source/age conclusion by itself.')
