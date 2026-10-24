#!/usr/bin/env python3
"""Finite preprocessing of arbitrary literal affine-count lap expressions.
This supplement does not change the frozen exact-validator input contract.
"""
from quadratic_lap_validator import *

def word_geometry(word,heading=0):
    p=(0,0);h=heading
    for t in word:
        h=(h+(1 if t=='R'else-1))%4;p=add(p,D[h])
    return p,(h-heading)%4

def normalize(blocks,heading=0,name='normalized'):
    blocks=list(blocks)
    assert blocks and all(w and set(w)<=set('LR') and a>=0 and b>=0 for w,a,b in blocks)
    skipped=0
    if not any(b for w,a,b in blocks):
        if not any(a for w,a,b in blocks):
            return dict(rejected=True,reason='empty event domain, not an infinite ant path')
        blocks=[(w,a,a+b)for w,a,b in blocks];skipped=1
    for index,(w,a,b)in enumerate(blocks):
        if not a:continue
        drift,rotation=word_geometry(w)
        if rotation:
            n=max(0,(8-b+a-1)//a)
            return dict(rejected=True,reason='nonrestoring unbounded word power contains impossible w^8',
                        block=index,witness_lap=n+skipped,power=8,word=w)
        if drift==(0,0):
            n=max(0,(2-b+a-1)//a)
            return dict(rejected=True,reason='zero-drift restored unbounded word contains impossible w^2',
                        block=index,witness_lap=n+skipped,power=2,word=w)
    theta=sum(b*word_geometry(w)[1]for w,a,b in blocks)%4
    grouped=1
    if theta:
        blocks=[(w,4*a,a*s+b)for s in range(4)for w,a,b in blocks];grouped=4
    P=Program(blocks,heading,name)
    if theta:assert P.A==(0,0)
    return dict(rejected=False,program=P,skipped_initial_empty_laps=skipped,
                original_lap_rotation=theta,original_laps_per_group=grouped)

def main():
    examples=[('nonrestoring_variable_power',[('R',1,1)]),
              ('zero_drift_variable_power',[('RRRR',1,1)]),
              ('rotating_laps',[('LRRL',1,1),('R',0,1)]),
              ('quadratic_restored_laps',[('LRRL',1,1)]),
              ('empty_first_lap',[('LRRL',1,0)])]
    records=[]
    for name,blocks in examples:
        out=normalize(blocks,1,name)
        if out['rejected']:records.append(dict(name=name,**out));continue
        P=out.pop('program');literal=P.literal(6)
        # Expand the unnormalized definition directly for comparison.
        p=(0,0);h=1;raw=[];start=out['skipped_initial_empty_laps']
        for n in range(start,start+6*out['original_laps_per_group']):
            for w,a,b in blocks:
                for j in range(a*n+b):
                    for t in w:
                        raw.append((p,h,t));h=(h+(1 if t=='R'else-1))%4;p=add(p,D[h])
        assert [(p,h,t)for e,p,h,t in literal]==raw
        records.append(dict(name=name,**out,A=P.A,B=P.B,physical_read_comparisons=len(raw)))
    assert records[0]['rejected'] and records[1]['rejected']
    assert records[2]['A']==(0,0) and records[2]['original_laps_per_group']==4
    assert records[3]['A']!=(0,0) and records[4]['skipped_initial_empty_laps']==1
    report=dict(status='PASS literal affine-lap normalization controls',records=records,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                scope='Preprocessing only; does not claim any new accepted finite-seed infinite model.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
