from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';ns={'__file__':str(SELF)};exec((SELF.parent/'check_foreign_kinked_barrier_turn_independent.py').read_text().split('geometries=[]')[0],ns)
walk,W,M,xy=[ns[k]for k in('walk','W','M','xy')];names=['D','DC','V','VC','VCC','U','UC','UCC'];K={-1-1j,-1,-1j,0,1}
raw={n:walk(''.join(W[c]for c in n))for n in names};ctx={n:walk(''.join(W[c]for c in n)+M)for n in names}
I={n:{q for q,b in ctx[n]['req'].items()if b}-K for n in names};O={};ports=[];fresh=[];heads=[]
for n in names:
 rr=raw[n];EK={rr['p']+q*(-1j)**rr['h']for q in K};O[n]=({q for q,b in ctx[n]['req'].items()if b}^rr['odd'])-EK
 last={q:(i,c)for i,(q,h,c)in enumerate(rr['reads'])}
 for q in O[n]:assert last[q][1]=='R'and q.imag>=0;fresh.append((n,xy(q),last[q][0]))
 actual={q:i for q,(i,c)in last.items()if c=='L'and q.imag<=0 and q not in O[n]|EK}
 desired={-1:1,-1-1j:2,-1j:3}
 if n=='DC':desired|={0:12,1:13}
 assert actual==desired
 for q,i in actual.items():
  phys=q*1j;assert phys.real>=0;ports.append((n,xy(q),i,xy(phys)))
  for cn in ['D','V','U']:
   for slot in I[cn]:
    head=phys-slot*(-1j);active=(sum(xy(q+slot))%2==0)
    heads.append((n,xy(q),cn,xy(slot),xy(head),active))
assert len(ports)==26 and len(fresh)==68 and len(heads)==208 and sum(z[-1]for z in heads)==120
steps={n:xy(raw[n]['p']*1j)for n in ['D','V','U']};assert steps=={'D':(-1,1),'V':(-3,1),'U':(-4,0)}
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,s.split()[:8]))for s in CP.read_text().splitlines()};young=[];cnt=Counter()
for age in [0,1]:
 h=(-age)%4
 for si,sn in enumerate(names):
  for ci,cn in enumerate(names):
   for out in O[sn]:
    for slot in I[cn]:
     p=out-slot*(-1j)**h;key=(si,ci,*xy(p),h,*xy(out),age)
     if (sum(xy(p))+h)%2:reason='sector'
     elif sn.count('C')>age:reason='incomplete_full_source'
     else:assert key in COUNT;reason='COUNT5'
     cnt[reason]+=1;young.append((key,reason))
assert len(young)==3128
A=json.loads((D/'W_deleted_port_boundary.json').read_text());assert Counter((r['actual_W_fullproducer'],tuple(r['deletion_cell_in_fullproducer_frame']),r['last_actual_L_tick0'],tuple(r['W_physical_offset_from_producer_head']))for r in A['all26_full_exit_right_supported_actual_deletion_ports'])==Counter(ports)
mp=D/'W_deleted_port_boundary_manifest.json';mf=json.loads(mp.read_text())
for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in mf['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS ordered actual W-deletion sites cannot be E external residual inputs before first foreign','manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'actual_deletion_roles':ports,'all68_fresh_export_roles':fresh,'all208_forbidden_head_roles':heads,'plain_W_steps':steps,'all3128_young_queries':young,'young_counts':dict(cnt),'analytic':['Every recorded site is a genuine final RAW L and is absent from the deleting FULL packet output and FULL exit core. Thus its previous lifetime is destroyed, including any factor-entry or older producer identity. A full packet cannot overlap another full packet, so there is no older in-progress source that finishes later.','At W orientation every recorded deletion has physical x>=its source head x. All full outputs, including own C tails, have source-local y>=0, hence physical x<=their own W head x. Every later W source head has strictly smaller x; a positive tail ends that W run. This excludes all later W full output origins with no length cap.','If the cell subsequently becomes a genuine external residual input, take the last completed full packet that exports that current identity. A transient active-core R write is not an omitted source: when the identity first becomes external, the completed packet places it in full O, whose every member was independently verified to have a real final RAW R. No assertion of persistent physical whiteness follows.','Only S/E source-entry clocks2/3 remain, versus E consumer3, hence full-source ages1/0. All3128 full-output/input alignments are sector-inactive, incomplete-source, or an exact signed COUNT5 exclusion. Marker-only E inputs are still actual entry residual identities, not invented extra executed reads.','The resulting208 forbidden head/input roles include all D/V/U external slots, not merely a distinguished slot. The ordered list of actual W producers and deletion sites remains unbounded. No foreign-input, returned-packet, core/guard influence, path-barrier or second-foreign extension is inferred.'],'scope':mf['scope'],'dependencies':mf['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],cnt)
