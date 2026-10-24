"""Exact all-K overlap of the prescribed return strand and actual outgoing output."""
from pathlib import Path
import json
P=Path(__file__).parent
j=json.loads((P/'FIXED_BAND_WIDE_OUTPUT_CHECKED.json').read_text());Q=j['period_read_positions'];U=j['period_word']
W=json.loads((P/'MOVING_CAPACITY_REGRESSION_CHECKED.json').read_text())['actual_permanent_phase_cells']
rows=[]
for r in W:
    x,y=r['cell'];align=[]
    for i,q in enumerate(Q):
        dx,dy=x-(q[0]-8),y-q[1]
        if dx!=dy or dx%2:continue
        m=dx//2
        # v=j+m. Every alignment has m>=3, so every j>=0 is eligible
        # after the true phase14 entry; no negative/initial-copy branch is dropped.
        assert m>=3
        align.append(dict(copy_offset=m,phase=i,time_constant=104*m+i-14,turn=U[i]))
    first=min(align,key=lambda a:a['time_constant']) if align else None
    rows.append(dict(outgoing_phase=r['phase'],outgoing_cell=r['cell'],return_alignments=align,first=first))
found={tuple(r['outgoing_cell']):r['first']['time_constant'] for r in rows if r['first']}
assert found=={(5,8):311,(6,8):312,(6,7):313,(6,9):325}
assert all(r['first']['turn']=='R' for r in rows if r['first'])
tests=[]
for K in (3,4,10,80,10**9):
    # Count nonnegative j with 104j+c<104K exactly, without expansion.
    counts={str(q):max(0,(104*K-1-c)//104+1) for q,c in found.items()}
    assert sum(counts.values())==4*K-11
    tests.append(dict(K=K,anchor_counts=counts,periodic_output_contacts_before_nominal_marker=4*K-11))
out=dict(status='AUTHOR exact prescribed-strand inventory; independent audit pending',
         periodic_output_anchor_count=12,rows=rows,parameter_tests=tests,
         count_formula='4K-11 for K>=3, excluding the launch-cap cohort and excluding the destination read',
         earliest_bulk_obstruction=dict(offset_after_original_return=311,cell=[5,8],birth=271,wanted='R',actual_if_still_black='L'),
         scope='Required clearing/contact inventory for the specified nominal104 return strand. Not a lower bound on contacts of an arbitrary rerouted continuation.')
(P/'SHIFTED_WAKE_CONTACT_INVENTORY_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
