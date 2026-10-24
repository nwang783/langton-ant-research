from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util,json
R=Path('/workspace/shared/langton');s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS

def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return *q,h
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def hit(a,b,c,d):
 u,v,zz=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  ss,tt=Q(det(zz,v),den),Q(det(zz,u),den)
  return(ss,tt)if 0<=ss<=1 and 0<=tt<=1 else None
 if det(zz,u):return None
 k=0 if v[0]else 1;lo,hi=sorted((Q(a[k]-c[k],v[k]),Q(b[k]-c[k],v[k])));lo,hi=max(Q(0),lo),min(Q(1),hi)
 if lo>hi:return None
 pt=(c[0]+lo*v[0],c[1]+lo*v[1]);j=0 if u[0]else 1;ss=Q(pt[j]-a[j],u[j]);return(ss,lo,hi)

res=[]
for A,S,hole in [('Q',{(-3,-3),(-2,-3),(-1,-3),(-1,-2)},(0,-2))]:
 geo=l.literal_geometry(W[A]);ep=tuple(geo['endpoint']);norm=lambda q:l.rot(sub(q,ep[:2]),2);poses=[(0,0,0),after(W['F']),ep];pp=[(*norm(p[:2]),(p[2]+2)%4)for p in poses];vv=list(map(z,pp));fore=list(zip(vv,vv[1:]));rows=[]
 for atom in'DCVU':
  full=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M);rawtr=l.trace(W[atom]);writes=[(p,t)for p,(c,t)in rawtr['last'].items()if c=='R']
  for k in range(6):
   if atom=='C'and k==5:continue
   h=(-k)%4
   for write,t in writes:
    head=sub(hole,l.rot(write,h));r=dict(A=A,hole=hole,atom=atom,k=k,h=h,head=head,write=write,R_tick=t)
    if(sum(head)+h)%2:r['why']='sector'
    elif k==0 and head[1]<0:r['why']='N0_y_negative'
    elif k==1 and head[1]<1:r['why']='W1_below_y1'
    elif any(l.rot(sub(q,head),-h)in tr['first']or l.rot(sub(q,head),-h)in l.K for q in S):r['why']='current_hook_context_hit'
    else:
     ch=(z((*head,h)),z(after(W[atom],(*head,h))));hits=[(j,hh)for j,(a,b)in enumerate(fore)if(hh:=hit(a,b,*ch))is not None]
     if hits:r['why']='earlier_FOREIGN_contact';r['hits']=[(j,tuple(str(v)for v in hh))for j,hh in hits]
     else:r['why']='NECESSARY';r['exit']=after(W[atom],(*head,h))
    rows.append(r)
 print(A,'all',len(rows),Counter(r['why']for r in rows),'remaining',[(r['atom'],r['k'],r['head'],r['R_tick'],r.get('exit'))for r in rows if r['why']=='NECESSARY'])
 res+=rows

A='Q';hole=(0,-2);target=(0,-1,3);geom=l.literal_geometry(W[A]);ep=tuple(geom['endpoint']);old=add(ep[:2],l.rot(hole,2));trA=l.trace(W[A]+l.M)
assert old==(-4,-2)and trA['last'][old]==('L',56)and list(old)not in geom['outputs']and hole not in l.K
prec=[]
for atom,head,inp in [('D',(1,-2,3),(0,1)),('V',(3,-2,3),(0,3)),('U',(4,-1,3),(-1,4))]:
 assert after(W[atom],head)==target and inp in map(tuple,l.literal_geometry(W[atom])['inputs'])
 assert add(head[:2],l.rot(inp,3))==hole and l.rot(sub(hole,head[:2]),-3)not in l.K
 fr=l.trace(W[atom]+l.M)['first'][inp];assert fr==('L',len(W[atom])+1)
 prec.append(dict(actual_previous_RAW=atom,actual_previous_head=head,needed_hole_input=inp,physical_read_owner=o.describe(atom,fr[1]),must_be_BLACK_before_predecessor_ENTRY=True))
CU=l.trace(W['C']+W['U']+l.M);assert not CU['feasible']
nec=[r for r in res if r['why']=='NECESSARY'];assert len(nec)==5
assert{(r['atom'],r['k'],tuple(r['head']),r['R_tick'])for r in nec}=={('C',2,(2,-2),8),('V',2,(2,-2),8),('U',2,(2,-2),8),('V',4,(0,-4),12),('U',4,(1,-5),22)}
CORE=[];reader=[]
for r in nec:
 atom=r['atom'];head=(*r['head'],r['h']);ee=after(W[atom],head)
 if r['k']==4:
  assert ee==(1,-1,0)and l.rot(sub(hole,ee[:2]),-ee[2])==(-1,-1)
  for nxt in'DCVU':assert l.trace(W[nxt]+l.M)['first'][(-1,-1)]==('L',2)
  CORE.append(dict(donor=r,actual_RAW_exit=ee,hole_in_exitCORE=(-1,-1),obligatory_next_actual_word_L_tick0=2,next_read1=3,must_precede_C5_and_W5_reader=True,cut='not_a_valid_LAST_R_funder_because_next_real_L2_deletes_it'))
 else:
  assert head==(2,-2,2)and tuple(r['write'])==(2,0)
  source=(z(head),z(ee));assert list(r['write'])in l.literal_geometry(W[atom])['outputs']
  for p in prec:
   readAtom=p['actual_previous_RAW'];hp=tuple(p['actual_previous_head']);ch=(z(hp),z(after(W[readAtom],hp)));local_head=l.rot(sub(hp[:2],head[:2]),-head[2]);relh=(hp[2]-head[2])%4
   record=dict(donor_RAW=atom,donor_entry=head,donor_true_C_clock=2,reader_previous_RAW=readAtom,reader_entry=hp,reader_true_C_clock=5,source_relative_reader=(local_head[0],local_head[1],relh),actual_donor_chord=source,actual_reader_chord=ch)
   if readAtom=='D'and atom in'VU':
    assert(local_head,relh)==((1,0),1)
    rlocal=l.rot(sub(head[:2],hp[:2]),-hp[2]);assert rlocal==(0,-1)and rlocal in l.K
    record.update(cut='fresh_donor_SAME_r_or_LEFT_current_through_trueK3_in_reader_ENTRY_CORE',fresh_donor_tag=head[:2],reader_CORE_local=rlocal,actual_donor_to_reader_C_clock=3)
   else:
    hh=hit(*source,*ch);assert hh is not None
    if atom=='C'and readAtom=='D':
     assert source[1]==ch[0]and hh[0]==1 and hh[1]==0
     record.update(cut='nonadjacent_repeated_actual_C_EXIT_at_reader_ENTRY',source_exit_C_clock=3,reader_entry_C_clock=5)
    else:
     assert hh[1]>0
     record.update(cut='earlier_contact_already_inside_previous_RAW',old_s=str(hh[0]),new_t=str(hh[1]),source_entry_vertex_owned_by_actual_outgoing_donor=hh[0]==0)
   reader.append(record)
assert len(reader)==9 and Counter(r['cut']for r in reader)=={'fresh_donor_SAME_r_or_LEFT_current_through_trueK3_in_reader_ENTRY_CORE':2,'nonadjacent_repeated_actual_C_EXIT_at_reader_ENTRY':1,'earlier_contact_already_inside_previous_RAW':6}
assert len(res)==208 and Counter(r['why']for r in res)=={'sector':104,'current_hook_context_hit':59,'N0_y_negative':18,'W1_below_y1':18,'NECESSARY':5,'earlier_FOREIGN_contact':4}
out=dict(status='AUTHOR_Q_W5_GENUINE_DELETED_CORE_FUNDING_CLOSURE_PENDING_REVIEW',scope='ActualQ plus arbitrary ordinaryRAW suffix and actualterminalM11 cannot completeU(0,-1,W)atCclock5 if the Q+ordinary executed proxy through that ENTRY is SIMPLE. This supplies GLOBAL-first-contact use. No initialU/fullG8 or rail/depth bound; no earlier-selfcontact-independent assertion.',source_Q_hole=dict(postforeign_cell=hole,Q_cell=old,last_own_L_tick0=56,last_own_L_read1=57,absent_O_and_exitCORE=True,WHITE_after_Q=True),all3_actual_immediate_previous_RAW_BLACK_hole_obligations=prec,actual_C_U_noncontinuation=CU,all208_last_RAW_R_origin_deadline_and_hook_FOREIGN_constraints=res,counts=dict(Counter(r['why']for r in res)),both_N4_CORE_births_obligatorily_deleted_by_real_next_L2=CORE,all9_S2_donor_by_actual_predecessor_cases=reader,last_R_exhaustiveness='A physically WHITE Q-deleted hole needs a genuinely later R. Choose lastR before actual D/V/U reader ENTRY. It is a completed earlier RAW finalR at that cell; all such R positions include CORE writes. Sources with a later own/next L and no later R cannot fund required BLACK. Actual sourceC deadlines are retained.',fresh_guard_scope='Only new V/U born AFTERQ and ordinary SIMPLE source-to-reader subarcs use signed9cfdd2c8. The reader is prior to the alleged GLOBAL first contact, so its proxy cut is genuinely simple. No old8 age crossesQ, and no prior ordinary selfcontacts are allowed by this guard premise.',no_word_tree_depth_or_rail_bound_or_unread_CORE_omission=True,no_B_other_gate_hookMISS_or_secondFOREIGN_or_global_simplicity_capture_claim=True)
Path('/workspace/shared/langton/foreign_Q_W5_deleted_core_guard_2026-10-24/Q_W5_deleted_core_guard.json').write_text(json.dumps(out,indent=2)+'\n')
print('Q W5 Ugate blocked under SIMPLE executed prefix:208 allCORE lastR origins,2 nextL2 deaths,9 source/reader cases=7 earliergeometry+2 genuine freshdonor CORE guards.')
