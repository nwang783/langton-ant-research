from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'word_stabilization/U_foreign_prefix_arm_guard_frozen_20261023_2207'
old=R/'audits/check_U_foreign_prefix_buds_independent.py';env={'__file__':str(old)};exec(old.read_text().split('COUNT=')[0],env)
W,M,walk,center,xy,inv,names=(env[k]for k in('W','M','walk','center','xy','inv','names'));meet=env['ns']['meet']
CT={tuple(map(int,line.split()[:8]))for line in(R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()}
L={0,1j,1,1+1j};arm=1+2j;lastp=1+4j;lasth=1;C=walk(W['C']);assert(lastp+C['p']*(-1j), (lasth+C['h'])%4)==(2+4j,0)
local=(arm-lastp)/(-1j);assert local==2 and next((i,ch)for i,(q,h,ch)in enumerate(C['reads'])if q==local)==(8,'R')
rows=[];survivors=[];contacts=[]
for source in('U','UC','UCC'):
 assert arm in inv[source]['outputs']
 for n in range(8):
  h=(-n)%4;turn=(-1j)**h
  for target in names:
   for slot in inv[target]['inputs']:
    p=arm-slot*turn;key=(names.index(source),names.index(target),*xy(p),h,*xy(arm),min(n,5));ctx={p+q*turn for q in inv[target]['full']['req']};base=walk(W[target[0]]);bc0=center(p,h);bc1=bc0+(center(base['p'],base['h'])-center(0,0))*turn;hit=meet((-1,-1),(-1,7),xy(bc0),xy(bc1))
    if(int(p.real+p.imag)+h)%2:why='sector'
    elif key in CT:why='signed_count5'
    elif ctx&L:why='permanent_left_star_complete_context'
    elif n+target.count('C')>8:why='full_tail_after_foreign'
    elif hit is not None:
     why='earlier_closed_source_U_chord_contact';assert n>source.count('C') and(p,h)!=(4j,0);contacts.append((source,target,n,xy(p),h,str(hit)))
    else:
     why='endpoint_obligation';ep=p+inv[target]['p']*turn;eh=(h+inv[target]['h'])%4
     assert(n,target,p,ep,eh)in((6,'D',1+3j,2j,2),(6,'V',1+5j,2j,2),(6,'U',6j,2j,2));survivors.append((source,target,n,xy(p),h,xy(ep),eh))
    rows.append((source,target,n,xy(slot),xy(p),h,why))
counts=Counter(r[-1]for r in rows);assert len(rows)==552 and counts=={'sector':276,'signed_count5':189,'permanent_left_star_complete_context':69,'earlier_closed_source_U_chord_contact':9,'endpoint_obligation':9}
a=json.loads((D/'U_foreign_prefix_arm_guard.json').read_text());expected={(r['source'],r['consumer'],r['age'],tuple(r['input']),tuple(r['pose'][:2]),r['pose'][2],r['reason'])for r in a['queries']};assert set(rows)==expected
steps=[inv[a]['p']for a in('D','V','U')];assert all((z*(-1)).imag<=0 and(z*(-1j)).imag<=0 for z in steps);assert(C['p']*(-1)).imag==-1 and 2-1<4
manifest=D/'manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='50563fd304a2a84cd68bbefc194e6459466a90ef563b1036111c78b05c79b312'
for name,value in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==value
out={'status':'PASS last two genuine U-source common-F-prefix contacts excluded by arm retirement and one-C cone','manifest_sha256':sha,'counts':dict(counts),'closed_source_contacts':contacts,'surviving_endpoint_obligations':survivors,'analytic':['A required before-white arm at the actual last C must have retired in some earlier full packet whose entry clock is0..7. The full retiring packet may itself contain that last C; only completion by foreign clock8 is imposed.','The complete literal input inventory covers core exchange and marker-owned input roles. Signed COUNT5 overflow is applied at min(age,5) with the actual heading and placement retained. Permanent-star COMPLETE-context hits are invalid even when a tag would be an ordinary black input.','Each of the nine geometric cuts is a closed contact with the earlier creating U chord. Its consumer starts strictly after source full completion, excluding the true adjacent-endpoint exception.','All nine remaining cases are plain D/V/U at age6 with full exit(0,2,S). Exactly one C precedes last-C entry(1,4,E): S zero-run,C_S,E zero-run has y<=1, so cannot reach y4 at any zero-run length.','Together with the signed predecessor, bud and renewal-return assembly this closes the U-source common-F-prefix chronological first-contact class, respecting outgoing-source endpoint assignment.'],'scope':'No Q/B-tail or D/C/V-source closure, later foreign permanence, generic seven-word coverage or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)
