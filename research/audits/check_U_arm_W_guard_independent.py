from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'U_arm_W_contact_or_persistence_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'manifest.json')=='bb6eb6b56ff4e153a949b2193bf495a0bd3ee8d14c14ec3eb73cadf2025af27c'
for f,h in json.loads((D/'manifest.json').read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'arm_W_guard.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,G,rot,center,xy,meet=[ns[k]for k in('W','M','K','tr','G','rot','center','xy','meet')]
raw=lambda s:''.join(W[a]for a in s)
full=('D','DC','V','VC','VCC','U','UC','UCC');geom=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];inputs={}
for a in full:
 z=tr(raw(a)+M);ii=sorted((q for q,b in z['req'].items() if b and q not in K),key=lambda q:(q.real,q.imag));inputs[a]=ii
 stored=next(r for r in geom if r['name']==a)
 assert set(map(tuple,map(xy,ii)))==set(map(tuple,stored['inputs']))
assert sum(map(len,inputs.values()))==23
arm=1+2j;COUNT={tuple(map(int,l.split()[:8])) for l in (R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()}
keys={}
for src in ('U','UC','UCC'):
 z=tr(raw(src));exitK={z['p']+rot(z['h'])*k for k in K}
 assert z['last'][arm]==('R',17) and arm not in exitK
 for n in range(4):
  h=(-n)%4
  for con in full:
   for inp in inputs[con]:
    p=arm-rot(h)*inp;key=(full.index(src),full.index(con),*xy(p),h,*xy(arm),n)
    why='sector' if (int(p.real+p.imag)+h)%2 else 'signed_COUNT5'
    if why=='signed_COUNT5':assert key in COUNT
    keys[key]=why
assert len(keys)==276 and Counter(keys.values())==Counter(sector=138,signed_COUNT5=138)
assert keys=={tuple(r['key']):r['reason'] for r in J['preFOREIGN_current_guard']['all276_exact_age0_through3_input_queries']}
a=center(0,0);b=center(G['U']['p'],G['U']['h']);wrows=[];nrows=[]
for con in 'DVU':
 for inp in inputs[con]:
  p=arm-rot(3)*inp;z=tr(W[con],p,3);end=xy(z['p'])+[z['h']]
  sector=(int(p.real+p.imag)+3)%2
  hit=None if sector else meet(a,b,center(p,3),center(z['p'],z['h']))
  if not sector:assert con=='U' and hit is not None and 0<hit[0]<1 and 0<hit[1]<=1
  first=next((i,ch) for i,(q,h,ch) in enumerate(tr(W[con]+M)['reads']) if q==inp)
  wrows.append(dict(atom=con,input=xy(inp),head=xy(p)+[3],exit=end,sector=bool(sector),contact=None if hit is None else list(map(str,hit)),input_first_tick=first[0]))
  pn=arm-inp;zz=tr(W[con],pn,0);assert zz['p'].real>=1 and zz['p']!=2j
  nrows.append((con,tuple(xy(inp)),tuple(xy(pn)+[0]),tuple(xy(zz['p'])+[zz['h']])))
assert len(wrows)==8 and sum(z['sector'] for z in wrows)==6
assert {tuple(z['contact']) for z in wrows if z['contact']}=={('3/4','3/4'),('1/2','1')}
for r in J['all8_plain_W_first_loss_input_roles']:
 q=next(z for z in wrows if z['atom']==r['consumer'] and z['input']==r['input_cell'])
 assert q['head']==r['consumer_pose'] and q['exit']==r['actual_RAW_exit']
 if q['contact']:assert q['contact']==[r['old_source_s'],r['new_t']]
assert set(nrows)=={(r['consumer'],tuple(r['input_cell']),tuple(r['consumer_pose']),tuple(r['actual_RAW_exit'])) for r in J['all8_N_plain_arm_input_RAW_exit_obligations']}
# C complete RAW+M has no residual I; every exit-core cell not in entryK was first read WHITE.
cc=tr(W['C']+M);cr=tr(W['C']);cek={cr['p']+rot(cr['h'])*k for k in K}
assert not {q for q,v in cc['req'].items() if v and q not in K}
assert all(cc['req'].get(q) is False for q in cek-K)
rows=[];counts=Counter();marker=[]
for b3 in 'VU':
 assert arm in {3j+rot(3)*k for k in K}
 for b1,b2 in product('DCVU',repeat=2):
  n=3-(b1+b2).count('C');h=(-n)%4
  for A in 'FQB':
   z=tr(raw(A+b1+b2),h=h);pa=3j-z['p'];assert z['h']==3
   ctx=tr(W[A]+M,pa,h);hits=[(i,ch) for i,(q,hh,ch) in enumerate(ctx['reads']) if q==arm]
   key=(A,b1,b2,b3,tuple(xy(pa)+[h]),n)
   if hits:
    i,ch=hits[0];assert ch=='R' and b1=='D' and i>=len(W[A]);off=i-len(W[A]);assert off in (6,7)
    physical=tr(raw(A+b1+b2),pa,h);assert physical['reads'][i][0]==arm and physical['reads'][i][2]=='R'
    kind='first_R';marker.append((key,i,off,off+1))
   elif n==3:kind='W_W'
   elif n==1:assert b1==b2=='C';kind='C_C'
   elif b1=='C':kind='C_W'
   else:
    assert b2=='C';first=tr(raw(A+b1),pa,h);assert(first['p'],first['h'])==(2j,0);kind='N_C'
   counts[kind]+=1;rows.append((key,kind))
assert len(rows)==96 and counts['first_R']==12
assert {r[0] for r in rows}=={(r['foreign'],r['first'],r['second'],r['third'],tuple(r['foreign_pose']),r['true_preFOREIGN_age']) for r in J['all96_exact_inverse_FOREIGN_two_prior_RAW_interfaces']}
report=dict(status='PASS portable SAME U-arm zero-C W contact-or-persistence and scoped THIRD V/U0,3W application',manifest=sha(D/'manifest.json'),young_queries=276,plain_W_roles=wrows,plain_N_exits=nrows,third_inverse_count=96,class_counts=dict(counts),actual_marker_reads=marker,analytic_scope=['The complete ordinary input interface includes marker-owned CURRENT-to-CORE capture; first CURRENT loss is not identified with physical death. The two legal W-loss atoms contact the creating U chord by their own RAW completion, so only preceding contact-free atoms preserve the arm.','All genuine U/UC/UCC R17 identities survive own tails and the signed age0..3 full-input query excludes loss before a completed FIRST-foreign boundary; no source age law is used after that boundary.','Twelve first-R contradictions occur in actual b1 D at zero-based ticks6/7, human reads7/8, not foreign RAW. Remaining84 foreign complete contexts MISS. C has no residual input and no old residual export to its exit core; N-pre-C exit0,2N is incompatible with all8 arm-loss alignments. SAME arm therefore opposes THIRD entryK.','Only old-U global-FIRST THIRD targets V/U0,3W; no full third simplicity, arbitrary-tail persistence through contact, or postforeign age.'])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS',sha(S.with_suffix('.json')))
