from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');P=R/'second_old_C_age3_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='2b32bc1646d39e827a2d99a92ea0c65208ee6ff68be4a3e1296ab9718458ac41';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(P/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
ref=json.loads((P/'C_age3_source_reserve.json').read_text());base=R/'audits/check_old_V_second_age1_independent.py';ns={'__file__':str(base)};exec(base.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet')];raw=lambda s:''.join(W[a]for a in s)
D=R/'core_periodicity_new/chronology_dcuv';G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];ids=(0,1,4,5,6,7,8,9);index={G[i]['name']:j for j,i in enumerate(ids)};orig={G[i]['name']:i for i in ids};HB={tuple(map(int,l.split()[:7]))for l in(D/'protected_patch2.tsv').read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in(D/'critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};I={};O={}
for i in ids:
 name=G[i]['name'];t=tr(raw(name));ec={t['p']+q*rot(t['h'])for q in K};O[name]={q for q,(ch,tt)in t['last'].items()if ch=='R'and q not in ec};ctx=tr(raw(name)+M);I[name]={q for q,b in ctx['req'].items()if b and q not in K};assert set(map(tuple,G[i]['inputs']))==set(map(tuple,map(xy,I[name])))and set(map(tuple,G[i]['outputs']))==set(map(tuple,map(xy,O[name])))
selection=[('DC',1,[(2,0),(2,3),(3,1),(3,2)]),('VC',1,[(2,1),(3,4)]),('VCC',1,[(2,1),(3,4)]),('VCC',2,[(2,5),(-1,5),(1,6)]),('UC',1,[(1,2),(2,5)]),('UCC',1,[(1,2),(2,5)]),('UCC',2,[(1,6),(-2,6),(0,7)])]
assert len(ref['all7_genuine_C_roles_and18_same_identity_source_reserves'])==7
counter=Counter();crossings=[];allkeys=[];norm={};qu=ref['all1794_exact_source_output_consumer_queries'];qindex=0
for(full,j,slots),role in zip(selection,ref['all7_genuine_C_roles_and18_same_identity_source_reserves']):
 before=full[0]+'C'*(j-1);e=tr(raw(before));tau=1-j;N=3-tau;c=full.count('C');ft=tr(raw(full));assert (role['actual_full'],role['selected_C_index1'],role['actual_prefix_before_selected_C'],role['selected_C_pose_in_full_frame'],role['actual_full_ENTRY_clock'],role['actual_full_ENTRY_age_at_FOREIGN'],role['actual_full_completion_clock'])==(full,j,before,[*xy(e['p']),e['h']],tau,N,tau+c)
 norm[full,j]=[]
 for slot,reserve in zip(slots,role['selected_reserves'],strict=True):
  q=complex(*slot);assert q in O[full];assert ft['last'][q][0]=='R';cell=(q-e['p'])/rot(e['h']);assert reserve['full_output_slot']==list(slot)and reserve['actual_last_R_tick0']==ft['last'][q][1]and reserve['normalized_selected_C_cell']==xy(cell);norm[full,j].append(cell);indices=[]
  for age in range(N+1):
   h=(-age)%4
   for ci in ids:
    consumer=G[ci]['name']
    for inp in G[ci]['inputs']:
     z=q-complex(*inp)*rot(h);x,y=xy(z);hb=(orig[full],ci,x,y,h,*slot);ck=(index[full],index[consumer],x,y,h,*slot,age)
     if age<c:why='source_full_not_yet_completed; remaining source atoms are input-free C'
     elif age+consumer.count('C')>N:why='consumer_full_cannot_complete_before_actual_FOREIGN_entry'
     elif(x+y+h)%2:why='signed_conserved_sector'
     elif hb in HB:why='signed_HB_clause'
     elif ck in COUNT:why='signed_COUNT5_clause'
     else:
      assert(full,age,consumer,h)==('DC',3,'V',1)
      assert(slot,(x,y),tuple(inp))in{((2,0),(-1,0),(0,3)),((2,0),(0,1),(1,2)),((3,1),(0,1),(0,3))}
      atom='D'if(x,y)==(-1,0)else'C';oldstart=0j if atom=='D'else tr(W['D'])['p'];oldend=tr(W[atom],oldstart)['p'];vend=tr(W['V'],z,h)
      a=center(oldstart,0);b=center(oldend,0 if atom=='D'else 3);u=center(z,h);v=center(vend['p'],vend['h']);hit=meet(a,b,u,v);assert hit is not None
      # Direct independent exact line parameters and strict intersection.
      cr=lambda u,v:int(u.real*v.imag-u.imag*v.real)
      from fractions import Fraction as F
      s=F(cr(u-a,v-u),cr(b-a,v-u));t=F(cr(u-a,b-a),cr(b-a,v-u));assert 0<s<1 and 0<t<1;point=a+float(s)*(b-a);assert xy(point)==([0,0]if atom=='D'else[2,2]);crossings.append([full,slot,consumer,[x,y,h],atom,xy(point),[s.numerator,s.denominator],[t.numerator,t.denominator]])
      why='proper_crossing_of_actual_past_source_atomic_chord'
     row=qu[qindex];assert(row['full_source'],row['output'],row['actual_full_source_age'],row['consumer_full'],row['consumer_input_slot'],row['consumer_full_pose'],row['HB_key'],row['count5_key'],row['FOREIGN_full_source_age_deadline'],row['consumer_full_completion_age'],row['exclusion'])==(full,list(slot),age,consumer,inp,[x,y,h],list(hb),list(ck),N,age+consumer.count('C'),why)
     counter[why]+=1;indices.append(qindex);qindex+=1
  assert reserve['all_query_indices']==indices
assert qindex==1794 and dict(counter)==ref['exact_query_classification']and len(crossings)==3
# Whole actual foreign context masks, derived from separately signed geometry.
ob=json.loads((R/'second_contact_signed_obligations_2026-10-24/signed_current_obligations.json').read_text());bases=[b for b in ob['all267_foreign_typed_base_rows']if(b['old'],b['n'])==('C',3)];assert len(bases)==54 and all(b['reason']=='keep'for b in bases)
sup=ref['all378_role_specific_actual_before_mask_conflicts'];assert len(sup)==378
keys=lambda b:(b['A'],b['b1'],b['b2'],tuple(b['pa']),tuple(b['p2']))
for full,j,_ in selection:
 rows=[r for r in sup if(r['actual_full_source'],r['selected_C_index1'])==(full,j)];assert len(rows)==54
 assert{(r['foreign'],r['first'],r['second'],tuple(r['FOREIGN_pose']),tuple(r['second_pose']))for r in rows}==set(map(keys,bases))
 for r in rows:
  tokens=r['foreign']+r['first']+r['second'];tt=tr(raw(tokens)+M);assert not tt['bad'];p=complex(*r['FOREIGN_pose'][:2]);h=r['FOREIGN_pose'][2];first={}
  for tick,(q,hh,ch)in enumerate(tt['reads']):first.setdefault(q,(ch,tick))
  got=[]
  for q in norm[full,j]:
   local=(q-p)/rot(h)
   if local in K:got.append((tuple(xy(q)),'SAME CURRENT external residual in FOREIGN entryK',None))
   elif local in first and first[local][0]=='R':got.append((tuple(xy(q)),'SAME CURRENT BLACK identity required WHITE at actual combined first read',first[local][1]))
  assert got and set(got)=={(tuple(w['reserve']),w['contradiction'],w.get('combined_tick0'))for w in r['all_guaranteed_same_CURRENT_witnesses']}
  for w in r['all_guaranteed_same_CURRENT_witnesses']:
   if 'combined_tick0'not in w:continue
   tick=w['combined_tick0'];owner=w['actual_read_owner'];lo=0
   for k,a in enumerate(tokens):
    if tick<lo+len(W[a]):assert(owner['actual_atom_index0'],owner['actual_atom'],owner['atom_start_tick0'],owner['canonical']['context_tick0'])==(k,a,lo,tick-lo);break
    lo+=len(W[a])
   else:assert owner['actual_atom']=='next actual word'and owner['next_word_tick0']==tick-lo and owner['next_word_read_number1']==tick-lo+1
report={'status':'PASS entire old-C true atomic preforeign-age3 FIRST SECOND-RAW source slice, all genuine containing roles','manifest_sha256':sha(mf),'script_sha256':sha(Path(__file__)),'dependencies':m['dependencies'],'full_roles':7,'same_identity_reserves':18,'query_counts':dict(counter),'three_strict_actual_source_chord_crossings':crossings,'real_role_mask_rows':378,'analytic_review':['All eight complete raw+M input sets independently reconstructed, including marker/core capture; every selected reserve is a real final-R full output outside actual exitK','C2 full-entry=-1 and foreign-full-age4, source completion ages and input-free mandatory C tails are retained. Consumer full completion deadline applies because FIRSTforeign begins at a complete G8 boundary, not inside an unfinished packet','All1794 possible full input alignments rebuilt with compact/actual IDs. Only three DC atage3 plainV survivors, each has a strict actual past D/C chord crossing under signed old U-entry simplicity','CURRENT loss includes first CORE absorption via the preceding fullpacket genuine I slot, not just physical residual retirement. Marker-only inputs retained; unresolved alive-CORE qualification389fec is not used to invent death','Every54 actual geometry mask is independently blocked in all7roles. Four-output DC cohort sublemma is reader/contact-owner independent at COMPLETE foreign source age3 boundaries only'],'not_claimed':['arbitrary atomic-cut currentness','postforeign maturation','complete second simplicity','general trajectory language coverage']}
f=R/'audits/old_C_age3_reserve_independent.json';f.write_text(json.dumps(report,indent=2)+'\n');print(sha(f));print(report['status'])
