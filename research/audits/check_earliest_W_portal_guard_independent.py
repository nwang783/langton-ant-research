from pathlib import Path
from fractions import Fraction
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';mp=D/'earliest_W_portal_ancestry_guard_manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='e74dca08ba5962577861c1fbb4435456399467b231671372a34328f160d1ebaa'
for f,h in json.loads(mp.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in json.loads(mp.read_text())['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
ns={'__file__':str(SELF.parent/'check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns);W,M,walk,dirs,xy=[ns[x]for x in('W','M','walk','dirs','xy')]
def word(tokens):return ''.join(W[a]for token in tokens for a in token)
def geometry(w):
 p=0j;h=0;reads=[]
 for ch in w:reads.append((p,h,ch));h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 return p,h,reads
def normalized_pose(tokens,source):
 p,h,_=geometry(word(tokens));s,sh,_=geometry(word([source[:-1]]));return xy((p-s)*1j**sh), (h-sh)%4
# Universal T=2 endpoint equations are identities in unrestricted integer B>=1.
# Affine pairs are constant, coefficient-of-B.
add=lambda x,y:(x[0]+y[0],x[1]+y[1]);mul=lambda c,x:(c*x[0],c*x[1])
endpoint=[]
for source in('V','U'):
 A=(2,1)if source=='V'else(0,1);B=(0,1)
 exitx=add(mul(-1,A),(-1 if source=='V'else -2,0));exity=add(B,(0 if source=='V'else -1,0))
 for foreign,last,target in [('Q','V',(4,-5)),('B','U',(5,-4))]:
  n=(4 if source=='V' else 3,1);laststep=(3,-1)if last=='V'else(4,0)
  assert add(add(exitx,n),(laststep[0],0))==(target[0],0)
  assert add(add(exity,mul(-1,n)),(laststep[1],0))==(target[1],0)
  assert n[0]+1>=4
  endpoint.append({'source':source,'foreign':foreign,'D_count':{'constant':n[0],'B_coefficient':1},'last':last})
# Exact immutable suffix conflicts, with no intervening rewrite at the deleted cell.
guards=[]
for seq,tick in[(('D','V','Q'),93),(('D','U','B'),113)]:
 raw=word(seq);full=raw+W['C']+M;a=walk(full);assert not a['feasible']and(a['i'],a['q'],a['first'])==(tick,-1+0j,1)
 p,h,rr=geometry(full[:tick+1]);at=[(i,z)for i,(q,hh,z)in enumerate(rr)if q==-1];assert at==[(1,'L'),(tick,'L')]
 assert tick-len(raw)==1 and len(raw)in(92,112)
 guards.append({'tokens':seq,'RAW_end_tick0':len(raw),'conflict_tick0':tick,'returned_C_tick0':1,'returned_C_read1':2,'cell':[-1,0],'all_reads_through_conflict':at})
# The first-W rule is D-family; both D and DC require this same D+M prefix.
roles=[]
for source,tick,q,old in[('VCC',59,3j,19),('UCC',69,-1+4j,29)]:
 for first in('D','DC'):
  s=word([source,first])+M;a=walk(s);assert not a['feasible']and(a['i'],a['q'],a['first'])==(tick,q,old)
  _,_,rr=geometry(s[:tick+1]);hits=[(i,ch)for i,(p,h,ch)in enumerate(rr)if p==q];assert hits==[(old,'L'),(tick,'L')]
  roles.append({'source':source,'first_W_packet':first,'conflict_tick0':tick,'cell':xy(q),'physical_owner':'next word tick1/read2'if first=='D'else'own C-tail tick1/read2'})
# Independent endpoint-driven 25 exact words, not a W or T3 exhaustion.
attempts=[]
for source in('DC','VC','UC','VCC','UCC'):
 for module in[('D','UCC','V'),('D','U','VCC','V','V')]:
  for f,last in[('Q','V'),('B','U')]:
   tokens=[source,*module,*(['D']*4),last,f,'C'];assert normalized_pose(tokens[:-2],source)==((4,-5),1)if f=='Q'else normalized_pose(tokens[:-2],source)==((5,-4),1)
   assert normalized_pose(tokens[:-1],source)==((0,-1),3);a=walk(word(tokens)+M);assert not a['feasible'];attempts.append({'tokens':tokens,'conflict_tick0':a['i'],'cell':xy(a['q']),'first_tick0':a['first']})
 tokens=[source,'D','V','U','VCC','V','V',*(['D']*5),'V','F','C'];assert normalized_pose(tokens[:-2],source)==((2,-5),1)and normalized_pose(tokens[:-1],source)==((0,-1),3)
 a=walk(word(tokens)+M);assert not a['feasible'];attempts.append({'tokens':tokens,'conflict_tick0':a['i'],'cell':xy(a['q']),'first_tick0':a['first']})
assert len(attempts)==25
ref=json.loads((D/'earliest_W_portal_ancestry_guard.json').read_text())
for a,b in zip(attempts,ref['all25_endpoint_and_actual_portal_selected_candidate_histories']):assert a['tokens']==b['tokens']and a['conflict_tick0']==b['literal_conflict']['conflict_read']and list(a['cell'])==b['literal_conflict']['cell']
positives=[]
for c in ref['both_genuine_U_entry_regression_controls_replayed']:
 w=word(c['full_packet_sequence'])+M;assert walk(w)['feasible'];bb={complex(*q)for q in c['complete_finite_seed']};p=0j;h=0;hits=[];tag=complex(*c['source_tag_physical_site'])
 for t,ch in enumerate(w):
  assert(p in bb)==(ch=='L')
  if p==tag:hits.append([ch,t])
  bb.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 assert hits==c['source_tag_all_actual_reads'];positives.append({'sequence':c['full_packet_sequence'],'seed_mass':len(c['complete_finite_seed']),'tag_reads':hits})
out={'status':'PASS earliest-portal T>=3 guard, with D-family necessary-prefix clarification','manifest_sha256':mh,'four_unbounded_T2_endpoint_identities':endpoint,'immutable_returned_C_guards':guards,'four_D_and_DC_containing_role_guards':roles,'twenty_five_prescribed_failures':attempts,'two_genuine_positive_controls':positives,'analytic':['Signed complementary indices give remaining E weight1 for Q or2 for B when T=2. Actual final packet is V/U for Q, U for B; nonnegative weights then force exactly D^n,V,Q or D^n,U,B, with no later D. No C can remain in this E-clock3 stage. All earlier N/W/S stages are arbitrary.','At source T2, V has A=B+2 and U has A=B. The exact affine endpoint equations force n=B+4 or B+3. First earlier W D gives B>=1. Therefore every proposed pop contains the last D,V,Q or D,U,B, regardless the unrestricted preceding history.','Those suffixes delete a cell by D tick1 L and next require it at actual returned C tick1 L without any intervening read. This is a returned-C/complete-context contradiction, not a foreign-RAW grammar ban. Together with prior F T>=3, every spent portal has T>=3, so the earliest possible portal stays its original lifetime through this first return.','For old source C2(VCC/UCC), the first W BASE is D-family, not necessarily a plain full D. Both D and DC have the necessary D+actual M11 prefix and both fail the same immutable read; for DC the conflicting read is owned C-tail tick1/read2, for D it is the next actual word tick1/read2. Thus the role exclusion is sound with this explicit qualification.','The25 prescribed complete histories fail at their actual intended endpoint configurations, but they do not exhaust arbitrary W words or all T3 histories. Both genuine plain-source U-entry regression controls remain positive. No removed S run or withdrawn seal premise is used.'],'scope':'Three exact first returned raw-C residues only. Remaining old C roles C1 of DC/VC/UC after the separately signed C1-double-tail closure. No generic return closure, at-most-one spending, whole-ledger contraction or capture.'}
ep=D/'earliest_W_D_family_clarification_manifest.json';eh=hashlib.sha256(ep.read_bytes()).hexdigest();assert eh=='fa37a2b361e010bd506e86903ca7617ce1db8ef33f331cf0cba92381a933b7b4'
for f,h in json.loads(ep.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out['mandatory_D_family_clarification_manifest_sha256']=eh
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
