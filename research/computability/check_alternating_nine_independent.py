#!/usr/bin/env python3
"""No-import replay of two-level scale-three composite fixed-point exclusion."""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def draw(word):
    z=0j;v=1j;seen={};failure=None
    for time,c in enumerate(word):
        if z in seen and seen[z][1]==c and failure is None:
            failure=(time,seen[z][0],int(z.real),int(z.imag),c)
        seen[z]=(time,c)
        v*=(-1j if c=='R' else 1j);z+=v
    return z,v,failure

def main():
    geom={'R':[],'L':[]};legal={'R':[],'L':[]}
    for mask in range(512):
        w=''.join('RL'[(mask>>j)&1] for j in range(9))
        z,v,f=draw(w)
        for c,zz,vv in [('R',3,1),('L',-3,-1)]:
            if z==zz and v==vv:
                geom[c].append(w)
                if f is None:legal[c].append(w)
    for a in (geom,legal):
        for c in a:a[c].sort()
    assert [len(geom[c]) for c in 'RL']==[24,24]
    assert [len(legal[c]) for c in 'RL']==[9,9]
    checks={};largest=-1;phasepairs=0
    for u in legal['R']:
      for v in legal['L']:
       outer={'R':u,'L':v}
       for s in geom['R']:
        for t in geom['L']:
         phasepairs+=1;comp={'R':''.join(outer[c] for c in s),'L':''.join(outer[c] for c in t)}
         for root in 'RL':
          if comp[root][0]!=root:continue
          w=''.join(comp[c] for c in comp[root][:3])[:202]
          f=draw(w)[2];assert f is not None
          checks[u,v,s,t,root]=f;largest=max(largest,f[0])
    src=json.loads((ROOT/'causal_reduction/morphic_candidates/probe_alternating_nine_substitutions.json').read_text())
    for row in src['records']:
        u,v=src['phase_options'][row['outer_phase']];s,t=src['inner_phase_options'][row['inner_phase']]
        f=checks[u,v,s,t,row['root']]
        assert f==(row['time'],row['previous_time'],*row['cell'],row['turn'])
    assert len(checks)==len(src['records'])==49248
    out=dict(status='PASS INDEPENDENT COMPLETE REPLAY',geometric_per_turn=24,outer_legal_per_turn=9,phase_pairs=phasepairs,prolongable_rooted_cases=len(checks),latest_conflict=largest,all_source_first_conflicts_match=True,scope='Composite fixed points with prolongable R or L root; not first-letter cycles of the composite or a general phase-coupled multi-curve system.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
