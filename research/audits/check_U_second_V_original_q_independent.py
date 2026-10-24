from pathlib import Path
from collections import Counter
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];P=R/'U_second_V_original_q_frontier_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='d9ab9c0dd926bf27f9563a849f6d3e21016d45f3f1849c43335108835879cfcc';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(P/f)==h
ref=json.loads((P/'original_q_frontier.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_U_second_creator_bud_guards_independent.py'))};exec(Path(ns['__file__']).read_text().split('\nsource=[]')[0],ns)
W,M,K,L,walk,xy,raw=[ns[k]for k in('W','M','K','L','walk','xy','raw')];q=-1+2j;gA=-1+4j;center=lambda p,h:2*p+(-1-1j)*(-1j)**h
source_q=[]
for b in('U','UC','UCC'):
 r=raw[b];hist=[(i,ch)for i,(p,h,ch)in enumerate(r['reads'])if p==q];assert hist[-1][1]=='R';source_q.append({'source':b,'q_reads':hist})
pairs=[]
for b in('D','DC','V','VC','VCC','U','UC','UCC'):
 r=walk(''.join(W[a]for a in'UCC'+b)+M);pairs.append((b,r['feasible']))
assert [b for b,ok in pairs if ok]==['V','VC'];ucc=walk(W['U']+2*W['C']);assert(ucc['p'],ucc['h'])==(-1+5j,2)
for b in('V','VC'):
 rr=walk(''.join(W[x]for x in b));assert [(i,c)for i,(p,h,c)in enumerate(rr['reads'])if p==1j][-1]==(11,'R')
cleanup=-1+5j;cleanup_h=2;assert cleanup+1j*(-1j)**cleanup_h==gA
helper=cleanup+4j*(-1j)**cleanup_h;hh=(cleanup_h+2)%4;assert(helper,hh)==(-1+1j,0)
Vraw=walk(W['V']);he=helper+Vraw['p'];assert center(he,Vraw['h'])==-1+7j and center(helper,0)==-3+1j
rows=[];remain=[];old=ns['ref']['remaining12_necessary_states'] if 'remaining12_necessary_states'in ns['ref']else json.loads((R/'U_second_contact_creator_bud_guards_2026-10-24/creator_bud_guards.json').read_text())['remaining12_necessary_states']
for z in old:
 a,b1,b2=z['foreign'],z['first'],z['second'];p=complex(*z['foreign_pose'][:2]);h=z['foreign_pose'][2];rot=(-1j)**h;age=z['true_preforeign_age'];ctx=walk(W[a]+W[b1]+W[b2]+M);loc=(gA-p)/rot;assert ctx['req'][loc]is False
 birthreq=next((i,c)for i,(pp,hh,c)in enumerate(ctx['reads'])if pp==loc);assert birthreq[1]=='R'
 east={2,2+1j}&{p+v*rot for v in K};cut=bool(east)
 if cut:assert(a,p,h,b1,age,east)==('F',3+0j,1,'C',3,{2,2+1j})
 else:
  prefix=walk(W[a]+W[b1]);fctx=walk(W[a]+M);assert all((u-p)/rot not in {pp for pp,hh,c in prefix['reads']}for u in L|{q});assert all((u-p)/rot not in fctx['req']for u in L)
  assert not(L|{q})&{4j-v for v in K};remain.append(z)
 rows.append({'foreign':a,'first':b1,'foreign_pose':z['foreign_pose'],'true_age':age,'gA_first_required_R':birthreq,'east_core_cut':cut})
assert len(remain)==11 and Counter(z['true_preforeign_age']for z in remain)=={3:2,4:9}
vr=walk(W['V']);vc=walk(W['V']+M);vp=4j;vh=2;vrot=-1;qe=(q-vp)/vrot;we=(1j-vp)/vrot;assert(qe,we)==(1+2j,3j)
qh=[(i,c)for i,(p,h,c)in enumerate(vc['reads'])if p==qe];wh=[(i,c)for i,(p,h,c)in enumerate(vc['reads'])if p==we];assert qh==[(13,'L'),(17,'R'),(21,'L')]and wh==[(19,'L')]
exitp=vp+vr['p']*vrot;exith=(vh+vr['h'])%4;exitK={exitp+x*(-1j)**exith for x in K};assert{q,1j}<=exitK and not{0,1,1+1j}&exitK
for u in(0,1,1+1j):assert(u-vp)/vrot not in{p for p,h,c in vr['reads']}
out={'status':'PASS12-to11 preforeign ancestry reduction and conditional tagged secondV reset','manifest':sha(mf),'source_q_last_R_preservation':source_q,'complete_UCC_next_packets':pairs,'fresh_cleanup_A_birth_tick0':11,'only_cleanup_A_consumer_pose':[-1,1,0],'consumer_chord':[[-3,1],[-1,7]],'all12_rows':rows,'remaining11':remain,'second_V_q_history':qh,'second_V_w_history':wh,'second_V_RAW_length':len(W['V']),'actual_RAW_exit':[*xy(exitp),exith],'analytic_review':[
'The east-pair exclusion is strictly before foreign at true clock3, below the signed first genuine breaker clock4. Only F3,0E with firstC has both original east identities in foreignentryK. No east law crosses foreign.',
'All12 actual combined before-masks require gA=(-1,4) WHITE at foreignentry. If original recycledq had first retired earlier, signed1954/2027 forces genuine fullV/VC at(-1,5,S), clock2, creating fresh A=gA at its R11 and preserving it through its own tail. Signed2043 is an all-age SAME-original A channel, with held-r justification, not a selected-slot guessed minimum: first A consumer is V/VC relative(0,4,S), exact age2. Its creator-frame V base chord ends at the old creating U exit vertex after two intervening Cs and cleanup, forbidden by old U-entry simplicity. This law is used only inside the complete-eight prefix. Consequently no preforeign retirement/replacement/core absorption of originalq is possible.',
'All eight literal UCC full successors were rebuilt; onlyV/VC survive, and UCC actual full exit is precisely the required q-cleanup entry. A foreign at clocks3/4 cannot be immediate at the full UCC clock2 cut. Thus UCC is excluded, U/UC remain necessary. This does not assert any of the11 histories attained.',
'For each of11 remaining masks, executed A+firstRAW misses all five original identities and actual secondV entryK misses them. Foreign completecontext misses the star. Therefore the same five are CURRENT at CUT2 by read absence, not by a postforeign age law.',
'Originalq is physically L13/read14 then its cell R17/read18 into EXITCORE; replacementL21 belongs nextwordtick3/read4. Originalw is unread through V RAW18, alive but EXITCORE, and its physicalL19 belongs nextwordtick1/read2. Three other SAME-original star identities remain CURRENT at RAWexit. The q replacement is not a residual output and aliveCORE is not CURRENT. No second-contact closure, tail permanence or postforeign q-role rigidity is claimed.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
