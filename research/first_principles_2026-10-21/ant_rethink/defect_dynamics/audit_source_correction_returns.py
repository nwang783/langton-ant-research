"""Replay each source correction that physically revisits either old gate.

Starts from the complete initial finite seed; does not use saved checkpoints.
Compares each return with the complete read footprint of that gate's original
canonical phase-72 response. This comparison is an obstruction to directly
reusing that response, not a claim that another controller cannot exist.
"""
import json
from pathlib import Path
from double_reversal import *

ROOT=Path(__file__).resolve().parent
data=[json.loads(s) for s in (ROOT/'source_correction_probe.jsonl').read_text().splitlines()]
q1,q2=markers(50,100)
gates=(q1,q2);impacts=(5272,66998)
b=set(SEED)|set(gates);p=(0,0);h=REF['heading'];refs={};foot={q1:set(),q2:set()}
for t in range(impacts[1]+RECOVERY):
    for q,ti in zip(gates,impacts):
        if t==ti:
            assert p==q
            refs[q]=(set(b),h)
        if ti<=t<ti+RECOVERY:foot[q].add(p)
    p,h,c=step(b,p,h)

out=[]
for rec in data[1:]:
    if not(rec['q1_visits'] or rec['q2_visits']):continue
    qi=tuple(rec['correction']);b=set(SEED)|set(gates)|{qi};p=(0,0);h=REF['heading'];returns=[]
    for t in range(rec['first_read']+rec['elapsed']):
        if t>=rec['first_read'] and p in gates:
            rb,rh=refs[p]
            diff=sorted(z for z in foot[p] if (z in b)!=(z in rb))
            returns.append({'time':t,'gate':p,'heading':h,'original_heading':rh,
                            'black':p in b,'original_black':p in rb,
                            'original_response_footprint_size':len(foot[p]),
                            'footprint_color_mismatch_count':len(diff),
                            'mismatch_sample':diff[:12]})
        p,h,c=step(b,p,h)
    nt=tail(b,p,h)
    assert nt is not None and nt['drift']==tuple(rec['drift'])
    assert sum(r['gate']==q1 for r in returns)==rec['q1_visits']
    assert sum(r['gate']==q2 for r in returns)==rec['q2_visits']
    out.append({'initial_black':sorted(set(SEED)|set(gates)|{qi}),
                'correction':qi,'end_time':rec['first_read']+rec['elapsed'],
                'end':p,'heading':h,'certified_drift':nt['drift'],
                'returns':returns})
answer={'status':'all_six_gate_revisiting_cases_independently_replayed',
        'cases':out}
(ROOT/'source_correction_return_audit.json').write_text(json.dumps(answer,indent=2)+'\n')
print(json.dumps(answer,indent=2))
