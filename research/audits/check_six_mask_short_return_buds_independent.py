from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ns={'__file__':str(SELF.parent/'check_U_first_helper_ports_independent.py')};exec((SELF.parent/'check_U_first_helper_ports_independent.py').read_text().split('rows=[];gates=[];adjacent_rejects=[]')[0],ns)
globals().update({k:ns[k]for k in ('ROOT','G','rotation','xy','walk','raws','mark')})
D=ROOT/'core_periodicity_new';B=D/'six_mask_short_return_buds_frozen_20261023_2046';m=json.loads((B/'manifest.json').read_text())
for x in m['files']:assert hashlib.sha256((B/x['file']).read_bytes()).hexdigest()==x['sha256']
for f,h in m['dependencies'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
# Own raw first-read clock, including the actual marker.
first={};p=0j;h=0;dirs=(1j,1,-1j,-1)
for i,c in enumerate(raws[9]+mark):
 first.setdefault(p,(c,i));h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
req=walk(raws[9]+mark)[2];rows=[]
for a,p,h,age,expected in ((1,-5+1j,0,4,(-3+4j,65)),(5,-4+7j,1,5,(1+5j,34))):
 ep=p+rotation(G[a]['end'],h);eh=(h+G[a]['h'])%4
 bud=ep+rotation(1-1j,eh);slot=rotation(bud-p,-h);target=rotation(-ep,-eh);th=(-eh)%4;gap=age-1
 assert slot in G[a]['O'] and (gap,th)in ((3,1),(4,0)) and target.real<=0
 assert bud not in G[9]['I'] and req[bud] is False
 assert (bud,first[bud][1])==expected and first[bud][0]=='R'
 rows.append(dict(producer=a,pose=[*xy(p),h],source_age=age,exit=[*xy(ep),eh],post_exit_Cgap=gap,target_in_exit_frame=[*xy(target),th],bud=xy(bud),true_source_output=xy(slot),creator_first_read=first[bud]))
out=dict(status='PASS two exact short-return bud exclusions only',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),rows=rows,analytic='Each actual source exit has an actual predecessor atom installing its true full-output bud. Signed1505 keeps that identity current at the creator entry for the corresponding3C E/X<=0 or4C N/X<=0 cut. The complete creator ledger has no such input and prescribes its initial color white, impossible while that residual identity persists.',scope='DC exact age4 and VC exact age5 only; larger congruent8+/9+ remain unexcluded. No V1/U1 event closure or prefix attainment.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(rows)
