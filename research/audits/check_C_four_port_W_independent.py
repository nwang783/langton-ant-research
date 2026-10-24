from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'C_four_port_W_transport_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=json.loads((D/'manifest.json').read_text())
for f,h in man['files'].items():assert sha(D/f)==h
for f,h in man['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'four_port_W_transport.json').read_text())
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,G,rot,center,xy,meet,cross=[ns[k]for k in('W','M','K','tr','G','rot','center','xy','meet','cross')]
raw=lambda s:''.join(W[a]for a in s);full=('D','DC','V','VC','VCC','U','UC','UCC');IDS=(0,1,4,5,6,7,8,9)
HB={tuple(map(int,l.split()[:7])) for l in (R/'core_periodicity_new/chronology_dcuv/protected_patch2.tsv').read_text().splitlines()}
COUNT={tuple(map(int,l.split()[:8])) for l in (R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()}
geo=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
def inventory(s):
 z=tr(raw(s));ctx=tr(raw(s)+M);ek={z['p']+rot(z['h'])*k for k in K}
 ii={q for q,v in ctx['req'].items() if v and q not in K};oo={q for q,(c,t) in z['last'].items() if c=='R' and q not in ek}
 # Any old residual newly occupying exitK is either an actual residual input or a first-WHITE contradiction.
 for q in ek-K:assert q in ctx['req'] and (q in ii or ctx['req'][q] is False)
 return ii,oo,z,ctx,ek
inv={s:inventory(s) for s in full+('F','Q','B','C')}
for s in full:
 jj=next(g for g in geo if g['name']==s);assert inv[s][0]=={complex(*q) for q in jj['inputs']} and inv[s][1]=={complex(*q) for q in jj['outputs']}
ports={'beta':1-1j,'q':2+0j,'arm':2+1j,'bud':1+2j};queries={};crossings=[];roles=[]
for src,selected in [('DC',1),('VC',1),('VCC',1),('VCC',2),('UC',1),('UCC',1),('UCC',2)]:
 before=src[0]+'C'*(selected-1);z=tr(raw(before));N=3+selected-1;sc=src.count('C');si=full.index(src)
 for label,cell in ports.items():
  output=z['p']+rot(z['h'])*cell;assert output in inv[src][1];assert inv[src][2]['last'][output][0]=='R'
  roles.append((src,selected,label,xy(output),inv[src][2]['last'][output][1]))
  for age in range(N+1):
   h=(-age)%4
   for con in full:
    ci=full.index(con)
    for inp in inv[con][0]:
     p=output-rot(h)*inp;hb=(IDS[si],IDS[ci],*xy(p),h,*xy(output));ck=(si,ci,*xy(p),h,*xy(output),age)
     if age<sc:why='source_full_not_yet_completed; remaining source atoms are input-free C'
     elif age+con.count('C')>N:why='consumer_full_cannot_complete_before_actual_FOREIGN_entry'
     elif (int(p.real+p.imag)+h)%2:why='signed_conserved_sector'
     elif hb in HB:why='signed_HB_clause'
     elif ck in COUNT:why='signed_COUNT5_clause'
     else:
      assert src=='DC' and age==3 and con=='V' and h==1
      old='D' if p==-1 else 'C';po=0j if old=='D' else G['D']['p'];ho=0
      cv=tr(W['V'],p,h);hit=meet(center(po,ho),center(tr(W[old],po,ho)['p'],tr(W[old],po,ho)['h']),center(p,h),center(cv['p'],cv['h']))
      assert hit is not None and 0<hit[0]<1 and 0<hit[1]<1
      why='proper_crossing_of_actual_past_source_atomic_chord';crossings.append((src,xy(output),xy(p),xy(inp),old,list(map(str,hit))))
     key=(src,selected,label,age,con,tuple(xy(inp)),tuple(xy(p)+[h]));queries[key]=why
assert len(roles)==28 and len(queries)==2760 and len(crossings)==3
actual=Counter(queries.values());assert dict(actual)==J['uniform_query_classification']
# Bind each exact source-role query, rather than just the class counts.
for role in J['all7_real_C_roles_with_uniform_four_CURRENT_reserves']:
 src=role['actual_full'];sel=role['selected_C_index1'];assert role['actual_full_ENTRY_age_at_FOREIGN']==sel+2 and role['actual_full_ENTRY_clock']==1-sel
 for reserve in role['selected_reserves']:
  label=next(k for k,q in ports.items() if xy(q)==reserve['normalized_selected_C_cell'])
  for qi in reserve['all_query_indices']:
   r=J['all2760_exact_uniform_reserve_queries'][qi];key=(src,sel,label,r['actual_full_source_age'],r['consumer_full'],tuple(r['consumer_input_slot']),tuple(r['consumer_full_pose']))
   assert queries[key]==r['exclusion']
# Complete first-touch inventory.
first=[];compatible={}
for atom in 'DVU':
 ii,oo,z,ctx,ek=inv[atom]
 for name,q in ports.items():
  for inp in ii:
   p=q-rot(3)*inp;blocked=[];cons=[]
   for other,c in ports.items():
    local=(c-p)/rot(3)
    if local in K or ctx['req'].get(local) is False:blocked.append(other)
    elif local in ii:cons.append(other)
   end=tr(W[atom],p,3);key=(atom,name,tuple(xy(inp)),tuple(xy(p)+[3]));first.append((key,bool(blocked)))
   if not blocked:
    assert not set(cons)&{'beta','q'} and end['p'].imag>=2
    for low in ('beta','q'):
     local=(ports[low]-p)/rot(3);assert local not in ctx['req'] and local not in ek
    compatible[atom,tuple(xy(p)+[3])]=(tuple(xy(end['p'])+[end['h']]),tuple(cons))
assert len(first)==32 and len(compatible)==9 and sum(not b for k,b in first)==11
assert {(r['first_input_packet'],r['alleged_first_touched_port'],tuple(r['actual_true_input_slot']),tuple(r['actual_W_entry'])):bool(r['blocked_by_held_cohort']) for r in J['all32_first_cohort_input_alignments']}==dict(first)
assert set(compatible)=={(r['packet'],tuple(r['entry'])) for r in J['all9_distinct_color_compatible_first_touch_poses']}
lowrows=[]
for low in ('beta','q'):
 for atom in 'DVU':
  for inp in inv[atom][0]:
   p=ports[low]-rot(3)*inp;assert p.imag<=(0 if low=='beta' else 1);lowrows.append((low,atom,tuple(xy(inp)),tuple(xy(p)+[3])))
assert set(lowrows)=={(r['lower_port'],r['consumer'],tuple(r['true_input_slot']),tuple(r['required_W_entry'])) for r in J['all16_possible_lower_port_consumer_heads']}
assert {a:tuple(xy(tr(W[a],h=3)['p'])+[3]) for a in 'DVU'}=={'D':(-1,1,3),'V':(-3,1,3),'U':(-4,0,3)}
# Exact source-relative global-first-contact window and outgoing endpoint geometry.
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows']
for target in 'DCVU':
 r=next(x for x in angles if x['source_class']=='preFOREIGN_ordinary' and x['source_atom']=='C' and x['contact_atom']==target)
 assert all(k<=3 for k in r['allowed_C_counts_before_contact_ENTRY'])
a=center(0,0);b=center(G['C']['p'],G['C']['h']);targets=[]
for atom in 'DCVU':
 z=tr(W[atom],h=3);c=center(0,3);d=center(z['p'],z['h']);corners=[(a+s*(b-a)-c-t*(d-c))/2 for s,t in product((0,1),repeat=2)]
 for x in range(math.floor(min(q.real for q in corners)),math.ceil(max(q.real for q in corners))+1):
  for y in range(math.floor(min(q.imag for q in corners)),math.ceil(max(q.imag for q in corners))+1):
   if (x+y+3)%2:continue
   p=complex(x,y);hit=meet(a,b,c+2*p,d+2*p)
   if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
   assert x>=0;blocked=[]
   for name in ('beta','q'):
    local=(ports[name]-p)/rot(3)
    if local in K or inv[atom][3]['req'].get(local) is False:blocked.append(name)
   assert blocked;targets.append((atom,(x,y,3),str(hit[0]),str(hit[1])))
assert len(targets)==6
assert {(r['atom'],tuple(r['actual_W_entry']),str(F(*r['old_s'])),str(F(*r['new_t']))) for r in J['all6_outgoing_owned_old_C_contact_targets']}==set(targets)
# FOREIGN complete-context MISS really excludes both entry and exit cores.
for A in 'FQB':
 assert K<=set(inv[A][3]['req']) and inv[A][4]<=set(inv[A][3]['req']) and inv[A][1]<=set(inv[A][3]['req'])
fhits=[];poses={};hc=Counter()
for A in 'FQB':
 for name,q in ports.items():
  for inp in inv[A][0]:
   p=q-rot(1)*inp;block=any((z-p)/rot(1) in K or inv[A][3]['req'].get((z-p)/rot(1)) is False for z in ports.values())
   reason='conserved_source_C_sector' if (int(p.real+p.imag)+1)%2 else 'held_four_port_color_conflict' if block else 'necessary_FOREIGN_HIT_pose'
   hc[reason]+=1;fhits.append(((A,name,tuple(xy(inp)),tuple(xy(p)+[1])),reason))
   if reason=='necessary_FOREIGN_HIT_pose':
    end=tr(W[A],p,1);assert end['h']==3 and end['p'].real<=0
    if end['p'].real==0:assert (A,p,end['p'])==('F',2-5j,-1j)
    poses[A,tuple(xy(p)+[1])]=tuple(xy(end['p'])+[3])
assert len(fhits)==188 and len(poses)==19 and hc==Counter(conserved_source_C_sector=94,held_four_port_color_conflict=71,necessary_FOREIGN_HIT_pose=23)
assert dict(fhits)=={(r['foreign'],r['aligned_current_port'],tuple(r['true_FOREIGN_input']),tuple(r['actual_E_entry'])):r['classification'] for r in J['all188_possible_FOREIGN_input_four_port_HIT_alignments']}
assert poses=={(r['foreign'],tuple(r['E_entry'])):tuple(r['actual_W_RAW_exit']) for r in J['all19_necessary_FOREIGN_HIT_pose_x_cone_exclusions']}
# Literal complete prepared upper-loss control, preserving every other black cell.
r=J['actual_prepared_upper_loss_regression_not_a_genuine_C_history'];B={complex(*q):('tag',n) if complex(*q) in ports.values() else ('old',n) for n,q in enumerate(r['complete_initial_BLACK'])};p=complex(*r['initial_head'][:2]);h=r['initial_head'][2];tagids={name:B[q] for name,q in ports.items()};reads={k:[] for k in ports}
assert len(B)==13
for t,ch in enumerate(W['U']+M):
 assert (p in B)==(ch=='L')
 for name,q in ports.items():
  if p==q:reads[name].append((t,ch))
 if ch=='L':B.pop(p)
 else:B[p]=('R',t)
 h=(h+(1 if ch=='R' else -1))%4;p+=ns['V'][h]
 if t==27:
  assert sorted(map(xy,B))==r['RAW_exit']['complete_BLACK']
  for name in ('beta','q'):assert B[ports[name]]==tagids[name] and ports[name] not in {p+rot(h)*k for k in K}
assert reads['beta']==reads['q']==[] and reads['bud'][0]==(14,'L') and sorted(map(xy,B))==r['complete_physical_BLACK_after_prefix']
report=dict(status='PASS all-length old-C true preFIRSTforeign age3 outgoing GLOBAL-FIRST-contact exclusion',manifest_sha256=sha(D/'manifest.json'),proof_sha256=sha(D/'four_port_W_transport.md'),independent_checker_sha256=sha(S),source_roles=roles,reserve_queries=2760,classifications=dict(actual),three_actual_past_source_crossings=crossings,first_touch_alignments=32,compatible_poses=9,lower_input_heads=16,targets=targets,foreign_hit_alignments=188,foreign_hit_classes=dict(hc),foreign_hit_poses=19,prepared_regression_reads=reads,analytic_scope=['Uniform four ports are real full outputs in each of7C1/C2 roles, with actual selectedC and full-source clocks kept distinct. Source/consumer full-completion deadlines and all signed clauses reconstructed; only3 prior DC midpoint crossings remain. This is exclusively preFOREIGN currentness.','Signed outgoing C tangent gives totalK<=3; true preA3 therefore leaves no returned C before target. Arbitrary plain W length remains. All32 first-touch alignments include marker/current-to-CORE absorption;9 compatible poses only remove upper tags, completely miss lower beta/q and exit y>=2. Later beta/q loss would require entry y<=0/1, impossible under W nondecreasingy.','FOREIGN completeMISS preserves external status because entire exitK lies in its complete context. HIT is not omitted:188 exact input alignments yield19 poses,18 negative-x exits cannot reach nonnegative-x targets. SoleF2,-5E allows only immediateD/C contact, invoking signed genuine-U-entry one-RAW simplicity rather than new age law.','Global-FIRST/outgoing endpoint assumptions essential; no contacts after an earlier break, other oldsource/age, secondFOREIGN, arbitrary-tail simplicity or attraction. Prepared13cell upper-loss control prevents all-four-permanence overclaim.'])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS',sha(S.with_suffix('.json')))
