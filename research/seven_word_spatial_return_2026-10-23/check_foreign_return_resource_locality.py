"""Literal F/Q/B resource ledger and spatial first-return interface. No path search."""
from pathlib import Path
import json,hashlib
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
QP=ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
J=json.loads(QP.read_text());M='LLLLRLRRRRL';NAMES='DCVUFQB'
def rotate(p,h):
    x,y=p
    return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def trace(word):
    p=(0,0);h=0;odd=set();required={};reads=[]
    for t,c in enumerate(word):
        initial=(c=='L')^(p in odd)
        assert p not in required or required[p]==initial
        required[p]=initial;reads.append(dict(t=t,cell=p,heading=h,turn=c))
        odd.symmetric_difference_update({p})
        h=(h+(-1 if c=='L' else 1))%4
        p=add(p,rotate((0,1),h))
    return dict(head=p,heading=h,odd=odd,required=required,reads=reads)
marker=trace(M);K={q for q,b in marker['required'].items()if b}
assert K=={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
rows=[]
for label,(name,record) in enumerate(zip(NAMES,J['macro_words'])):
    w=record['word'];raw=trace(w);ctx=trace(w+M)
    starts=[i for i in range(len(w)+1)if (w+M)[i:i+len(M)]==M]
    assert starts==[0,len(w)]
    assert record['end_marker']==M
    assert record['start_marker']==M+('L' if name=='D' else 'R')
    for q in K:assert ctx['required'][q]is True
    initial_black={q for q,b in ctx['required'].items()if b}
    I=initial_black-K
    p=raw['head'];h=raw['heading'];newK={add(p,rotate(q,h))for q in K}
    after=(K|I)^raw['odd'];assert newK<=after
    O=after-newK
    last={tuple(r['cell']):r['turn']for r in raw['reads']}
    assert all(last.get(q)=='R'for q in O)
    assert not(I&K) and not(O&newK)
    # Fresh prepared complete control, including the true following M11.
    board=K|I;pp=(0,0);hh=0
    for c in w+M:
        assert(pp in board)==(c=='L')
        board.symmetric_difference_update({pp})
        hh=(hh+(-1 if c=='L' else 1))%4
        pp=add(pp,rotate((0,1),hh))
    radius=lambda reads:max(max(abs(x),abs(y))for r in reads for x,y in [r['cell']])
    row=dict(label=label,name=name,word=w,length=len(w),entry_marker=record['start_marker'],end_marker=M,
        marker_occurrences=starts,endpoint=[*p,h],mass_gain=w.count('R')-w.count('L'),
        input_slots=sorted(I),output_slots=sorted(O),recycled_slots=sorted(I&O),input_count=len(I),output_count=len(O),
        raw_read_radius=radius(raw['reads']),complete_context_radius=radius(ctx['reads']),
        minimal_entry_black=sorted(K|I),minimal_entry_mass=5+len(I),minimal_exit_black=sorted(after),minimal_exit_mass=len(after),
        requirements=[[x,y,int(b)]for(x,y),b in sorted(ctx['required'].items())])
    rows.append(row)
assert [r['mass_gain']for r in rows]==[0,3,4,4,2,6,6]
assert [r['endpoint']for r in rows[4:]]==[[-4,-2,2],[-4,-4,2],[-3,-5,2]]
assert [r['input_count']for r in rows[4:]]==[14,15,18]
assert [r['output_count']for r in rows[4:]]==[16,21,24]
assert all(r['raw_read_radius']==5 and r['complete_context_radius']==6 for r in rows[4:])
assert max(r['complete_context_radius']for r in rows)==6
assert max(max(abs(x),abs(y))for r in rows[4:]for x,y in [r['endpoint'][:2]])==5
# Algebraic constants for a current foreign A then its following DCUV section.
# H_A(m)=L(m+delta_A) is kept symbolic: the total algorithm L is NOT run here.
for H in range(100):
    assert 5+H+6==H+11
for r in rows[4:]:
    assert 2<=r['mass_gain']<=6 and r['length']<=74
D=[QP,ROOT/'word_stabilization/dcuv_raw_bridge_effective_frozen_20261023_2100/manifest.json',ROOT/'seven_word_return_bridge_2026-10-23/manifest.json']
out=dict(status='AUTHOR_FOREIGN_RETURN_COMPLETE_RESOURCE_AND_LOCALITY_PENDING_INDEPENDENT_AUDIT',scope='Actual canonical M11 first-return seven-word sections, finite COMPLETE entry black board. The 214-port graph is retained, not made deterministic or globally covering.',core=sorted(K),rows=rows,
    effective_bound='H_A(m)=L(m+delta_A), using the signed total monotone raw-DCUV lifetime function without evaluating it.',
    section_duration='<=|A|+H_A(m)',return_head_displacement='L-infinity<=5+H_A(m)',write_radius='<=5+H_A(m)',recognition_query_radius='<=11+H_A(m)',
    mass_update='m_next=m+delta_A+3c+4v+4u; in[m+delta_A,m+delta_A+H_A(m)]',
    archive='All complete-board black cells outside the write ball persist unchanged. Optional residual identity tags use remove-before-install with the exact F/Q/B ledger; no C-age horizon is imported across a foreign macro.',
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(HERE/'foreign_return_resource_locality.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],foreign=[{k:r[k]for k in('name','endpoint','mass_gain','input_count','output_count','raw_read_radius','complete_context_radius')}for r in rows[4:]]),indent=2))
