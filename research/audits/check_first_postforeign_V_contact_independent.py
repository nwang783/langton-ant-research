from pathlib import Path
from fractions import Fraction
from collections import Counter
import hashlib,json,math
S=Path(__file__);R=S.parents[1];D=R/'first_postforeign_V_first_contact_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='a2277dae57ba6084fd0bc27f5d85b02d3165e9ffc574fabe9049195ca4ca7ee0'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'first_V_contact.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet,pieces,cross=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces','cross')]
I={a:{q for q,b in tr(W[a]+M)['req'].items()if b and q not in K}for a in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
src=tr(W['V']);exitK={src['p']+rot(src['h'])*q for q in K};VO={q for q,(c,t)in src['last'].items()if c=='R'and q not in exitK};pair={0j,1j};FS={-3-1j,-2-1j};BG=-1-2j;hole=-1+0j
assert VO=={0j,1j,1+0j,2+0j,2+1j,2+2j}
assert {(tuple(xy(q)),t)for q,(c,t)in src['last'].items()if q in VO}=={(tuple(z['SAME_first_V_output']),z['actual_last_R_tick0'])for z in J['all6_actual_source_R_birth_facts']}

def chord(a,p=0j,h=0):z=tr(W[a],p,h);return center(p,h),center(z['p'],z['h'])
old=chord('V');FORE={}
for A in'FQB':
 z=tr(W[A]);FORE[A]=[((u-2*z['p'])/rot(z['h']),(v-2*z['p'])/rot(z['h']))for u,v in pieces(A)]
assert FORE['F']==[(-7-3j,-1-1j)]and FORE['Q']==[(-7-7j,-1-5j),(-1-5j,-1-1j)]and FORE['B']==[(-5-9j,1-7j),(1-7j,-1-1j)]
for a in'DCVU':
 z=tr(W[a]);ctx=tr(W[a]+M);ek={z['p']+rot(z['h'])*q for q in K}
 for q in ek-K:assert q in ctx['req']and(not ctx['req'][q]or q in I[a])
def hits(held,a,p,h,alltouch=False):
 ctx=tr(W[a]+M);out=[]
 for q in sorted(held,key=lambda z:(z.real,z.imag)):
  loc=(q-p)/rot(h);first=next(((c,t)for t,(z,hh,c)in enumerate(ctx['reads'])if z==loc),None)
  if loc in K or first and(alltouch or first[0]=='R'):out.append(dict(SAME_tag=xy(q),local=xy(loc),role='ENTRY_CORE'if loc in K else first[0],first=list(first)if first else None))
 return out
def cmp_hits(got,ref):
 assert got==[{k:z[k]for k in('SAME_tag','local','role','first')}for z in ref]
 for z in ref:
  if z['first']:
   c,t=z['first'];o=z['actual_owner'];assert o['context_tick0']==t and o['turn']==c and o['context_read_number1']==t+1
   if t>=o['RAW_length']:assert o['owner']=='next actual word RAW'and o['owner_tick0']==t-o['RAW_length']
# Independent parallelogram cover including positive parallel onset; old terminal assigned outgoing.
windows={r['contact_atom']:r['allowed_C_counts_before_contact_ENTRY']for r in J['all4_signed_sourceV_contact_C_windows']};assert windows=={'D':[3,4,5,6],'C':[3,4,5,6],'V':[3,4,5],'U':[2,3,4,5]};geos=[];boxes=[]
a,b=old;u=b-a
for atom in'DCVU':
 for ck in windows[atom]:
  h=(-ck)%4;c,d=chord(atom,0j,h);v=d-c;den=cross(u,v);corners=[(a+s*u-c-t*v)/2 for s in(0,1)for t in(0,1)];bounds=[(math.floor(min(getattr(z,ax)for z in corners)),math.ceil(max(getattr(z,ax)for z in corners)))for ax in('real','imag')];boxes.append((atom,ck,bounds))
  for x in range(bounds[0][0],bounds[0][1]+1):
   for y in range(bounds[1][0],bounds[1][1]+1):
    if(x+y+h)%2:continue
    p=complex(x,y);delta=c+2*p-a
    if den:
     s=Fraction(cross(delta,v),den);t=Fraction(cross(delta,u),den)
     if not(0<=s<1 and 0<t<=1):continue
     kind='nonparallel'
    else:
     if cross(delta,u):continue
     assert atom=='V'and ck==4 and u==v;s=Fraction(0);t=-Fraction(int(delta.real),int(u.real))
     if not(0<t<=1):continue
     kind='same_direction_first_positive_onset'
    geos.append((atom,ck,xy(p)+[h],str(s),str(t),kind))
assert len(geos)==39 and len(boxes)==15
assert geos==[(g['target'],g['K'],g['pose'],g['old_s'],g['new_t'],g['kind'])for g in J['all39_outgoing_owned_geometries']]
for (a,ck,box),ref in zip(boxes,J['all15_exact_contact_boxes']):assert a==ref['target']and ck==ref['K']and [list(q)for q in box]==ref['integer_bounds']
remain=[]
for g in J['all39_outgoing_owned_geometries']:
 a=g['target'];p=complex(*g['pose'][:2]);h=g['pose'][2];hh=hits(pair,a,p,h);cmp_hits(hh,g['pair_entry_conflicts']);ti=[]
 for q in sorted(pair,key=lambda z:(z.real,z.imag)):
  loc=(q-p)/rot(h)
  if loc in I[a]:ti.append((xy(q),xy(loc)))
 assert ti==[(z['SAME_tag'],z['local'])for z in g['pair_TRUE_inputs_during_contact']]
 if not hh:remain.append((a,g['K'],p,h))
assert len(remain)==8
# Actual F births and first-V miss.
for r in J['SAME_F_tag_births']:
 tag=complex(*r['postFOREIGN_cell']);f=tr(W['F']);phys=f['p']+rot(f['h'])*tag;assert tag in FS and xy(phys)==r['actual_F_cell']and f['last'][phys]==('R',r['last_R_tick0'])and r['last_R_tick0']in(46,47)and tag not in tr(W['V']+M)['req']
def rolekey(row,tagfield,atomfield,slotfield):return(tuple(row[tagfield]),row[atomfield],tuple(row[slotfield]),row['pose'][2])
frows={rolekey(r,'lost_SAME_F_tag','consumer','input_slot'):r for r in J['all64_coupled_F_two_tag_first_loss_roles']};fc=Counter();seen=set()
for tag in FS:
 for a in'DCVU':
  for inp in I[a]:
   for h in range(4):
    key=(tuple(xy(tag)),a,tuple(xy(inp)),h);seen.add(key);r=frows[key];p=tag-rot(h)*inp;assert r['pose']==xy(p)+[h]
    if(int(p.real+p.imag)+h)%2:kind='sector'
    else:
     ph=hits(pair,a,p,h,True);fh=hits(FS,a,p,h);ch=[meet(*z,*chord(a,p,h))for z in FORE['F']+[old]]
     if ph:kind='would_change_guarded_V_pair_before_contact';cmp_hits(ph,r['pair_touches'])
     elif fh:kind='SAME_F_reserve_initial_CORE_or_WHITE';cmp_hits(fh,r['F_conflicts'])
     else:
      kind='actual_earlier_F_or_V_proxy_contact';assert any(ch);assert p!=src['p']or h!=src['h'];assert any(z and z[0]!='OVERLAP'and z[1]>0 for z in ch)
    assert r['classification']==kind;fc[kind]+=1
assert seen==set(frows)and len(seen)==64
# Physical hole repair: all first-R RAW positions, including current-core writes.
rrows={(r['ordinary_RAW'],tuple(r['first_R_local']),r['pose'][2]):r for r in J['all104_physical_first_R_repair_roles_for_F_hole']};seen=set();rc=Counter();assert src['last'][hole]==('L',1)
for a in'DCVU':
 raw=tr(W[a]);first={q:next((i,c)for i,(z,h,c)in enumerate(raw['reads'])if z==q)for q in raw['req']}
 for loc,(t,c)in first.items():
  if c!='R':continue
  for h in range(4):
   key=(a,tuple(xy(loc)),h);seen.add(key);r=rrows[key];p=hole-rot(h)*loc;assert r['pose']==xy(p)+[h]and r['first_R_tick0']==t
   if(int(p.real+p.imag)+h)%2:kind='sector'
   else:kind='would_touch_SAME_guarded_BLACK_identity_before_contact';hh=hits(pair|FS,a,p,h,True);assert hh;cmp_hits(hh,r['held_touches'])
   assert r['classification']==kind;rc[kind]+=1
assert seen==set(rrows)and len(seen)==104
for r in J['all4_F_D_E3_actual_immediate_predecessor_guards']:
 a=r['actual_previous_RAW'];p=complex(*r['pose'][:2]);h=r['pose'][2];z=tr(W[a],p,h);assert(z['p'],z['h'])==(-1+0j,1);hh=hits(pair|FS,a,p,h,True);cmp_hits(hh,r['preserved_guard_touches'])
 if a=='C':assert any(q['SAME_tag']==[0,1]and q['role']=='ENTRY_CORE'for q in hh)
 else:assert any(complex(*q['SAME_tag'])in FS and q['role']=='R'for q in hh)
# B g all32 earlier CURRENT loss roles and exact endpoint obligations.
b=tr(W['B']);phys=b['p']+rot(b['h'])*BG;assert b['last'][phys]==('R',67)and BG not in tr(W['V']+M)['req'];bc=Counter();bs=[]
for r in J['all32_B_g_earlier_CURRENT_loss_roles']:
 a=r['consumer'];inp=complex(*r['slot']);h=r['pose'][2];assert inp in I[a];p=BG-rot(h)*inp;assert r['pose']==xy(p)+[h];z=tr(W[a],p,h);assert r['RAW_EXIT']==xy(z['p'])+[z['h']]
 if(int(p.real+p.imag)+h)%2:kind='sector'
 else:
  hh=hits(pair,a,p,h,True);ch=[meet(*s,*chord(a,p,h))for s in FORE['B']+[old]]
  if hh:kind='pair_must_MISS_before_target';cmp_hits(hh,r['pair_touches'])
  elif any(ch):kind='earlier_B_or_V_proxy_contact';assert p!=src['p']or h!=src['h'];assert any(v and v[0]!='OVERLAP'and v[1]>0 for v in ch)
  else:kind='endpoint_obligation';bs.append((a,p,h,z['p']))
 assert r['classification']==kind;bc[kind]+=1
assert{(a,p,h)for a,p,h,e in bs}=={('D',-1-3j,0),('U',-2+0j,2),('U',-2+2j,2)}
for a,p,h,e in bs:
 if h==0:assert p.imag<src['p'].imag
 else:assert e.imag-1<-1
for a in'DVU':
 for h in(0,1,2,3):
  z=tr(W[a],0j,h)
  if h==0 or h==3:assert z['p'].imag>=0
  else:assert z['p'].imag<=0
assert tr(W['C'],0j,2)['p'].imag==-1
# Entire six-output first-loss cover, retaining only A and bud gates.
coh={rolekey(r,'lost_SAME_V_output','consumer','slot'):r for r in J['all192_entire_V_cohort_first_loss_roles']};cc=Counter();seen=set();gates=[]
for tag in VO:
 for a in'DCVU':
  for inp in I[a]:
   for h in range(4):
    key=(tuple(xy(tag)),a,tuple(xy(inp)),h);seen.add(key);r=coh[key];p=tag-rot(h)*inp;assert r['pose']==xy(p)+[h]
    if(int(p.real+p.imag)+h)%2:kind='sector'
    else:
     hh=hits(VO,a,p,h);contact=meet(*old,*chord(a,p,h))
     if hh:kind='initial_SAME_cohort_CORE_or_WHITE';cmp_hits(hh,r['conflicts'])
     elif contact is not None:
      kind='actual_earlier_source_V_proxy_contact';assert(p,h)!=(src['p'],src['h'])
      # A t=0 return cannot be the actual immediate source successor (different head/heading),
      # so its entry already repeats an earlier proxy vertex.
     else:kind='noncontact_first_loss_gate';gates.append((tag,a,p,h))
    assert r['classification']==kind;cc[kind]+=1
assert seen==set(coh)and len(seen)==192 and dict(cc)=={'sector':96,'initial_SAME_cohort_CORE_or_WHITE':86,'actual_earlier_source_V_proxy_contact':5,'noncontact_first_loss_gate':5}
assert{(tag,a,p,h)for tag,a,p,h in gates}=={(1j,'V',4j,2),(1j,'U',-1+5j,2),(2+2j,'D',3+2j,3),(2+2j,'V',5+2j,3),(2+2j,'U',6+3j,3)}
# Genuine physical tree, exact principal turns and all marker ownership.
edge=lambda q:(2*q-1-1j,2*q+1+1j)if int(q.real+q.imag)%2==0 else(2*q-1+1j,2*q+1-1j)
bridge=[5+5j,3+3j,5+1j,3-1j,1+1j,2j];assert list(map(xy,bridge))==J['genuine_current_bud_bridge_reversed'];edges=list(zip(bridge,bridge[1:]))
for (u,v),tag in zip(edges,[2+2j,2+1j,2+0j,1+0j,1j]):
 e,f=edge(tag);assert meet(e,f,u,v)is not None
 if tag!=1j:assert{e,f}=={u,v}
 else:assert meet(*old,e,f)==(Fraction(1,2),Fraction(1,2))
for j,(u,v)in enumerate(edges):
 for i,(e,f)in enumerate(edges[:j]):
  hit=meet(e,f,u,v);assert hit is None or(j==i+1 and f==u and hit==(1,0))
 hit=meet(bridge[-1],old[1],u,v);assert hit is None or hit==(0,1)
beta=math.atan(1/3);theta={'D':math.pi/4,'C':math.pi/4,'V':math.pi/2-beta,'U':math.pi/2}
for a in'DCVU':
 for b in'DCVU':
  z=tr(W[a]);u,v=chord(a);s,t=chord(b,z['p'],z['h']);angle=math.atan2(((t-s)/(v-u)).imag,((t-s)/(v-u)).real);assert abs(angle-(theta[b]-theta[a]+(math.pi/2 if a=='C'else 0)))<1e-12
for r in J['all3_bud_gate_Jordan_and_EXIT_interfaces']:
 a=r['consumer'];p=complex(*r['pose'][:2]);h=r['pose'][2];z=tr(W[a],p,h);assert(z['p'],z['h'])==(2+3j,3)and center(z['p'],z['h'])==bridge[0];assert{q for q in VO if(q-p)/rot(h)in I[a]}=={2+2j}
 local=(2+2j-p)/rot(h);assert local not in tr(W[a])['req'];ctx=tr(W[a]+M);assert ctx['reads'][len(W[a])+1][0]==local and ctx['reads'][len(W[a])+1][2]=='L';assert local in I[a]
 for i,(u,v)in enumerate(edges):hit=meet(*chord(a,p,h),u,v);assert hit is None or(i==0 and hit==(1,0))
 vectors=[chord(a,p,h)[1]-chord(a,p,h)[0]]+[v-u for u,v in edges]+[old[1]-bridge[-1]];closing=0
 for (u,v),rec in zip(zip(vectors,vectors[1:]),r['exact_closing_principal_joins']):
  ratio=v/u;ang=math.atan2(ratio.imag,ratio.real);cf=rec['principal_pi_over4_beta'];assert abs(ang-cf[0]*math.pi/4-cf[1]*beta)<1e-12;assert xy(u)==rec['incoming']and xy(v)==rec['outgoing'];closing+=ang
 assert abs(theta[a]-theta['V']+closing+math.pi/2)<1e-12
 assert{ck for ck in range(0,10)if abs(abs(ck*math.pi/2+theta[a]-theta['V']+closing)-2*math.pi)<1e-12}=={5}
# Every final typed route independently evaluates its actual held entry/WHITE condition.
hooks={'Q':{-3-3j,-2-3j,-1-3j,-1-2j},'B':{-2-4j,-1-4j,-4j,-3j}};jc=Counter();assert len(J['all117_FOREIGN_typed_disjoint_exclusion_routes'])==117;seen=set()
for r in J['all117_FOREIGN_typed_disjoint_exclusion_routes']:
 gi=r['geometry_index0'];A=r['foreign'];assert(gi,A)not in seen;seen.add((gi,A));g=J['all39_outgoing_owned_geometries'][gi];a=g['target'];p=complex(*g['pose'][:2]);h=g['pose'][2];ck=g['K'];assert(r['target'],r['pose'],r['K'])==(a,g['pose'],ck)
 if hits(pair,a,p,h):kind='SAME_V_pair_entry_cut'
 elif hits(hooks.get(A,set()),a,p,h):kind='SAME_Q_B_hook_entry_cut'
 elif ck==5:kind='K5_full_V_cohort_bud_reserve_ENTRY_CORE_cut';assert p.imag<3 and h==3 and any(z['role']=='ENTRY_CORE'for z in hits(VO,a,p,h))
 elif A=='F':
  if hits(FS,a,p,h):kind='coupled_SAME_F_two_tag_entry_cut'
  elif ck==3:kind='coupled_F_actual_last_predecessor_cut';assert(a,p,h)==('D',-1+0j,1)
  else:kind='coupled_F_unrepaired_WHITE_core_hole_cut';assert(ck,a,p,h)==(4,'U',-2j,0);assert tr(W[a])['reads'][13][0]==hole-p and tr(W[a])['reads'][13][2]=='L'
 else:kind='B_g_first_loss_endpoint_guard_WHITE_cut';assert(A,ck,a,p,h)==('B',3,'U',-2-1j,1);assert tr(W[a])['reads'][6][0]==(BG-p)/rot(h)and tr(W[a])['reads'][6][2]=='R'
 assert kind==r['route'];jc[kind]+=1
out=dict(status='PASS arbitrary-length GLOBAL-first-contact exclusion for first immediate postforeign V outgoing source only',manifest=sha(MF),script=sha(S),geometry_count=39,typed_count=117,F_first_loss_counts=dict(fc),hole_R_origin_counts=dict(rc),B_first_loss_counts=dict(bc),whole_V_first_loss_counts=dict(cc),final_routes=dict(jc),analytic_review=['The signed postforeign-V windows count actual Cs from this source entry, with no extra foreign half-turn. Exact parallelogram enumeration retains old start, new terminal and positive same-direction V onset; old s1 belongs to the actual outgoing next source. 31 of39 are entry conflicts, with true pair inputs DURING contact explicitly allowed.','Nonterminal guardian applies at every earlier SIMPLE marked cut admitting its actual next complete ordinary RAW+M. Thus prior pair input is impossible, while contact input remains allowed. Actual F R46/R47 outputs and Q/B hooks are not substituted by arbitrary prepared black bits. F reserve proof uses earliest loss of either tag and allows simultaneous inputs; all current/core capture slots are complete.','The F WHITE hole is not a residual tag. After actual V L1, its earliest later physical R must be the first RAW read of that cell, since any earlier L would itself require a prior repair. All104 roles include CORE writes and all52 sector-valid cases touch a guarded original BLACK identity before the candidate entry. A C predecessor of F-D hits A CORE; other predecessors require an F tag WHITE.','B R67 first loss leaves exactly N0 D or two S2 U endpoints. Exact monotone N/S/E motions and the one remaining C exclude them before the sole E3 target. Marker absorption is CURRENT loss even while the original is physically alive in CORE.','For K5 choose earliest loss among ALL six genuine V outputs. Only earlier A loss (forbidden by guardian) or three bud gates remain. Held physical output tree is simple; source partial chord and final consumer meet only intended endpoints. Fresh signed ordinary current-edge barrier prevents all intervening contacts with the tree. Source-relative initial segment is checked geometrically, not assumed to predate its births.','All16 ordinary principal joins telescope; the actual reversed tree closing angles give (K-1)pi/2. Jordan and K>=0 force K5. The three gates end at actual2,3,W, retain bud aliveCORE until next read2, and cannot reach y2/1 W targets without another C. Therefore full six-output CURRENT state holds at candidate ENTRY, not through the contact.','Closed endpoint at source-V terminal with new t0 is not discarded as adjacency: the only such classified consumer has a different actual head/heading from the immediate source exit, so this is already a repeated earlier corrected vertex. Ordinary terminal adjacency is not declared forbidden.','This closes only outgoing owner FIRST immediate postFIRSTforeign V under genuine U-entry complete8 ancestry and chronological GLOBAL-first-contact scope. Later V sources, other postforeign sources, foreign/older sources, arbitrary-tail simplicity, second foreign, language coverage and capture remain open.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
