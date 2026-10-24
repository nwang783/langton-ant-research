#!/usr/bin/env python3
"""Independent exhaustive inventory, including all first-letter cycles.
No imports from construction or prior checking code.
"""
import itertools,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def walk(w):
    x=y=0;vx,vy=0,1;vis={};bad=None
    for t,a in enumerate(w):
        if (x,y) in vis and vis[x,y][1]==a and bad is None:
            bad=(t,vis[x,y][0],x,y,a)
        vis[x,y]=(t,a)
        vx,vy=(vy,-vx) if a=='R' else (-vy,vx)
        x+=vx;y+=vy
    return (x,y,vx,vy),bad

def first_bad(w):
    x=y=0;vx,vy=0,1;vis={}
    for t,a in enumerate(w):
        if (x,y) in vis and vis[x,y][1]==a:
            return (t,vis[x,y][0],x,y,a)
        vis[x,y]=(t,a)
        vx,vy=(vy,-vx) if a=='R' else (-vy,vx)
        x+=vx;y+=vy
    return None

def main():
    geom={a:[] for a in 'RL'};legal={a:[] for a in 'RL'}
    for letters in itertools.product('LR',repeat=9):
        w=''.join(letters);pose,bad=walk(w)
        for a,expected in [('R',(3,0,1,0)),('L',(-3,0,-1,0))]:
            if pose==expected:
                geom[a].append(w)
                if bad is None:legal[a].append(w)
    assert [len(geom[a]) for a in 'RL']==[24,24]
    assert [len(legal[a]) for a in 'RL']==[9,9]
    records=[];roots={0:0,1:0,2:0};latest={0:0,1:0,2:0};pairs=0;cyclespairs=0
    for u,v in itertools.product(legal['R'],legal['L']):
      outer={'R':u,'L':v}
      for s,t in itertools.product(geom['R'],geom['L']):
        pairs+=1;sub={a:''.join(outer[c] for c in w) for a,w in [('R',s),('L',t)]}
        swap=(sub['R'][0]=='L' and sub['L'][0]=='R')
        cyclespairs+=swap
        for root in 'RL':
            if sub[root][0]==root:period=1
            elif swap:period=2
            else:period=0
            # sub^2(root) has length 6561 and begins with root for both cycle
            # types. It is a genuine nested prefix of the limit fixed by
            # sub^period. Some two-cycle conflicts first occur after 201.
            prefix=''.join(sub[c] for c in sub[root])
            assert period==0 or prefix[0]==root
            bad=first_bad(prefix)
            assert bad is not None,(u,v,s,t,root,period)
            roots[period]+=1;latest[period]=max(latest[period],bad[0])
            records.append([u,v,s,t,root,period,*bad])
    original=json.loads((ROOT/'causal_reduction/morphic_candidates/probe_alternating_nine_substitutions.json').read_text())
    known={(original['phase_options'][r['outer_phase']][0],original['phase_options'][r['outer_phase']][1],original['inner_phase_options'][r['inner_phase']][0],original['inner_phase_options'][r['inner_phase']][1],r['root']):(r['time'],r['previous_time'],*r['cell'],r['turn']) for r in original['records']}
    assert len(known)==49248
    for r in records:
        if r[5]==1:assert known[tuple(r[:5])]==tuple(r[6:])
    body=json.dumps(records,separators=(',',':'))
    artifact=Path(__file__).with_suffix('.records.json');artifact.write_text(body+'\n')
    out=dict(phase_pairs=pairs,transient_first_letter_roots=roots[0],prolongable_rooted_cases=roots[1],composite_swap_phase_pairs=cyclespairs,additional_two_cycle_roots=roots[2],latest_conflict_by_cycle_length=latest,all_source_prolongable_conflicts_match=True,records=len(records),records_sha256=hashlib.sha256((body+'\n').encode()).hexdigest(),record_file=str(artifact.relative_to(ROOT)),scope='Every literal S-squared R and S-squared L image of every retained composite S. Excludes all ant-legal words containing one complete such image, and all substitution-subshift limits. Not higher phase periods or phase-coupled multi-curve systems.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
