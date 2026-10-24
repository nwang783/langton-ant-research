from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';p=SELF.with_name('check_returned_V_source_reduction_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('mins=')[0],ns)
W,M,walk,xy,raw,I,O=[ns[k]for k in('W','M','walk','xy','raw','I','outputs')];names=['D','DC','V','VC','VCC','U','UC','UCC']
def advance(label,p=0j,h=0):
 for a in label:
  w=W[a]
  for c in w:h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
 return p,h
p,h=advance('UC');assert(p,h)==(5j,3);p,h=advance('D',p,h);assert(p,h)==(-1+6j,3);selected=p;oldC,hh=advance('D',p,h);assert(oldC,hh)==(-2+7j,3);end,he=advance('DC',p,h);assert(end,he)==(-3+7j,2)
slot=3+1j;t=selected+slot*1j;assert t==-2+9j and t==oldC+2*1j and slot in O['DC'];last=[(i,c)for i,(q,h,c)in enumerate(raw['DC']['reads'])if q==slot];assert last[-1]==(18,'R') and 18-len(W['D'])==8
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,s.split()[:8]))for s in CP.read_text().splitlines()};young=[];cnt=Counter()
for age in range(3):
 h=(-age)%4
 for ci,cn in enumerate(names):
  for q in I[cn]:
   p=slot-q*(-1j)**h;key=(1,ci,*xy(p),h,*xy(slot),age)
   reason='sector'if(int(p.real+p.imag)+h)%2 else'signed_COUNT5'
   if reason=='signed_COUNT5':assert key in COUNT
   young.append((key,reason));cnt[reason]+=1
assert len(young)==69 and cnt=={'sector':40,'signed_COUNT5':29}
pre=[]
for n in['D','V','U']:
 assert raw[n]['p'].imag>0 and raw[n]['h']==0
 for q in I[n]:
  required=t.imag-q.imag;assert required>=5 and required>-1;pre.append((n,xy(q),int(required)))
assert len(pre)==8
post=[];p=3-1j
for j in range(3):
 assert p==3+(4*j-1)*1j;inputs={p+q for q in I['U']};assert all(q.real in[2,3]for q in inputs)and t not in inputs;post.append((xy(p),sorted(map(xy,inputs))));p,h=advance('U',p,0)
assert(p,h)==(3+11j,0);local=t-p;assert local==-5-2j;qraw=walk(W['Q']);visits=[(i,c)for i,(q,h,c)in enumerate(qraw['reads'])if q==local];assert visits[0]==(53,'R') and 53<len(W['Q'])
mp=D/'Q_UC_D_common_output_guard_manifest.json';mf=json.loads(mp.read_text())
for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in mf['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS remaining Q/UC+D branch excluded for arbitrary prebreaker N length','manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'all69_actual_full_input_min3_queries':young,'query_counts':dict(cnt),'all8_prebreaker_input_height_requirements':pre,'all3_forced_U_input_lists':post,'common_output':xy(t),'DC_output_slot':xy(slot),'genuine_DC_last_R_tick':18,'own_C_tick':8,'Q_first_read':{'cell':xy(local),'tick0':53,'read1':54,'turn':'R'},'analytic':['The genuine UC frame gives selectedDC entry(-1,6,W) at clock1, its ownC1 entry(-2,7,W) still clock1, and full exit(-3,7,S) atclock2. The common outputt(-2,9) is actual fullDC slot(3,1), lastR18=ownC1 R8. AtomicC1 and containing fullDC source entry clocks coincide; there is no transplanted birth-age offset.','All69 full consumer/input placements at source-entry ages0,1,2 are directly sector-inactive or exact COUNT5 exclusions. Thus any packet entering before originalclock4 cannot retire this identity, including a packet whose ownC tail completes at4 and any marker-owned residual input. The identity argument uses full input retirement, not an assertion that physical L must precede the next marker.','At clock4 an arbitrary prebreaker N run ends at(3,-1,N). Every N base raisesy, so all earlier entries havey<=-1. All eight actual D/V/U external input roles require heady>=5 to reach t_y9. The forced right-breaker suffix consists of exactlythree plainU entries(3,-1),(3,3),(3,7), all inputsx2/3, missingt_x=-2. No further C can precedeQ at that clock. These exhaust every possible first consumer, including full-tail cases entering earlier.','The original same black output remains current atQ(3,11,N). Q first reads its local(-5,-2) at actualRAW53/read54 asR; there is no earlier foreign visit to clear it. This contradicts the mandatory source history before any postforeign age law is invoked. The independently legal suffixUUUQC lacks that obligatory source output and is not invalidated as a standalone control.','Combining this one branch with the signed current-support cuts and prior horizon guards excludes all C-side UC parent rows. Six/six/four necessary DC/VC interfaces remain forF/Q/B. No complete old-C/contact exclusion or bound on their earlier histories follows.'],'scope':mf['scope'],'dependencies':mf['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
