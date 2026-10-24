"""Exact source identities and deliberate corruption controls for the certificates."""
from pathlib import Path
import json
from ant_exact import *

def main():
    assert len(P)==13 and len(D)==12 and len(W)==104 and len(LEGAL10)==84
    core=certify_period(P,(0,0),2,W)
    assert core and core['drift']==(2,-2)
    B=set(P);p=(0,0);h=2
    for c in W:p,h,actual=step(B,p,h);assert actual==c
    moved={(x+2,y-2) for x,y in P}
    assert not (moved&D)
    assert B==moved|D and p==(2,-2) and h==2
    for a in D:
        for b in D:
            if a!=b:assert multiple((a[0]-b[0],a[1]-b[1]),DRIFT) is None
        for b in P:
            k=multiple((a[0]-b[0],a[1]-b[1]),DRIFT)
            assert k is None or k<1
    blank=set();bp=(0,0);bh=0
    for _ in range(9977):bp,bh,c=step(blank,bp,bh)
    assert bp==(-15,10) and bh==3 and len(blank)==715
    blank_cert=certify_period(blank,bp,bh,W)
    assert blank_cert and blank_cert['drift']==(-2,-2)
    for c in W:bp,bh,actual=step(blank,bp,bh);assert actual==c
    wrong=set(P);wrong.symmetric_difference_update({(0,0)})
    assert certify_period(wrong,(0,0),2,W) is None
    changed=('R' if W[0]=='L' else 'L')+W[1:]
    assert certify_period(P,(0,0),2,changed) is None
    remote=(2*10**30,-2*10**30)
    assert certify_period(P|{remote},(0,0),2,W) is None
    assert certify_period(P|{(10**30,0)},(0,0),2,W)
    out={'core_cells':13,'deposit_cells':12,'period':104,'ten_factors':84,
         'core_infinite_certificate':core,'source_recurrence':'exact disjoint identity passed',
         'deposit_full_translation_classes':'distinct; all backward deposits avoid P',
         'blank_time':9977,'blank_complete_mass':715,'blank_infinite_certificate':blank_cert,
         'negative_controls':['wrong current bit rejected','altered word rejected',
                              'blocker at 10^30 periods rejected'],
         'positive_control':'remote cell off every future phase ray accepted'}
    Path(__file__).with_name('reference_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
