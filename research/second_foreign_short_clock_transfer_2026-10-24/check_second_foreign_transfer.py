"""Actual two-foreign controls and endpoint-exhaustive C0/C1 loss obligation.
No first-foreign simplicity induction, ordinary rail-depth cutoff or
postforeign old-eight maturity law is used.
"""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def spell(word):return ''.join(W[a]for a in word)
def owner(word,t):
 off=0
 for i,a in enumerate(word):
  if t<off+len(W[a]):return dict(atom_index0=i,atom=a,own_tick0=t-off,own_read_number1=t-off+1,turn=W[a][t-off])
  off+=len(W[a])
 return dict(owner='actual following word supplied by M11',next_word_tick0=t-off,next_word_read_number1=t-off+1,turn=l.M[t-off])
STAR={(0,0),(0,1),(1,0),(1,1)}
HOOKS={'F':{(-3,-1),(-2,-1)},'Q':{(-3,-3),(-2,-3),(-1,-3),(-1,-2)},'B':{(-2,-4),(-1,-4),(0,-4),(0,-3)}}

def selected_ids(A):
 ut=l.trace(W['U']);fr=l.trace(W[A]);p1=after(W[A],(0,4,0));ep=after(W[A]);out={}
 for g in STAR:out['old_U_'+str(g)]=dict(cell=g,birth_tick0=ut['last'][g][1],source='first genuine U',own_R_tick0=ut['last'][g][1])
 for g in HOOKS[A]:
  cell=add(p1[:2],l.rot(g,p1[2]));local=l.rot(sub(cell,(0,4)),0);assert fr['last'][local][0]=='R'and list(local)in l.literal_geometry(W[A])['outputs']
  out['first_foreign_'+str(g)]=dict(cell=cell,birth_tick0=len(W['U'])+fr['last'][local][1],source='first '+A,source_postEXIT_coordinate=g,own_R_tick0=fr['last'][local][1])
 return out
@lru_cache(None)
def perms(d,v,u):
 if d+v+u==0:return ('',)
 out=[]
 if d:out+=['D'+q for q in perms(d-1,v,u)]
 if v:out+=['V'+q for q in perms(d,v-1,u)]
 if u:out+=['U'+q for q in perms(d,v,u-1)]
 return tuple(out)
# Exact complete-context FIRST-L targets include true external inputs AND
# entryCORE physical reads. No held-color/current assumption filters them.
# That deliberately also covers old originals aliveCORE at second ENTRY.
allfamilies={};goal_records=[];tuple_records=[];family_stats={}
for c in(0,1):
 words={}
 for A in'FQB':
  p1=after(W[A],(0,4,0));ids=selected_ids(A);h=(p1[2]-c)%4;assert h==(2 if c==0 else 1);goals={}
  for A2 in'FQB':
   tr=l.trace(W[A2]+l.M)
   for name,ident in ids.items():
    tag=ident['cell']
    for slot,(turn,t)in tr['first'].items():
     if turn!='L':continue
     p=(*sub(tag,l.rot(slot,h)),h)
     if(sum(p[:2])+h)%2:continue
     goals.setdefault((A2,*p[:2]),[]).append(dict(selected_ID=name,physical_cell=tag,second_foreign_first_L_local=slot,actual_first_L_owner=o.describe(A2,t),is_ENTRY_CORE=slot in l.K))
  goal_records.append(dict(C_count=c,first_foreign=A,post_first_FOREIGN_entry=p1,goal_count=len(goals),all_exact_goals=[dict(second_foreign=A2,entry=(gx,gy,h),witnesses=rs)for(A2,gx,gy),rs in sorted(goals.items())]))
  localcount=0
  for(A2,gx,gy),witnesses in sorted(goals.items()):
   if c==0:
    dx,dy=p1[0]-gx,p1[1]-gy
    if dx<0 or dy<0:continue
    for v in range(dx+1):
     d=dx-v;rem=dy-d-3*v
     if rem<0 or rem%4:continue
     u=rem//4;tuple_records.append(dict(C_count=0,first_foreign=A,second_foreign=A2,second_entry=(gx,gy,h),S_counts=(d,v,u)))
     for seq in perms(d,v,u):
      word='U'+A+seq+A2;words[word]=dict(first_foreign=A,second_foreign=A2,S_rail=seq,E_rail='',C_count=0,second_entry=(gx,gy,h),loss_witnesses=witnesses);localcount+=1
   else:
    dy=p1[1]-1-gy
    if dy<0:continue
    for vs in range(dy//3+1):
     for us in range(dy//4+1):
      for ds in range(dy-3*vs-4*us+1):
       rem=dy-ds-3*vs-4*us
       for ve in range(rem+1):
        de=rem-ve;dx=gx-p1[0]+ds+vs-de-3*ve
        if dx<0 or dx%4:continue
        ue=dx//4;tuple_records.append(dict(C_count=1,first_foreign=A,second_foreign=A2,second_entry=(gx,gy,h),S_counts=(ds,vs,us),E_counts=(de,ve,ue)))
        for pre in perms(ds,vs,us):
         for post in perms(de,ve,ue):
          word='U'+A+pre+'C'+post+A2;words[word]=dict(first_foreign=A,second_foreign=A2,S_rail=pre,E_rail=post,C_count=1,second_entry=(gx,gy,h),loss_witnesses=witnesses);localcount+=1
  family_stats[c,A]=dict(goals=len(goals),words=localcount)
 records=[]
 for word,meta in sorted(words.items()):
  # Actual endpoint equations, not just multiset labels, are verified on
  # every generated spelling, including empty ordinary rails.
  p=after(spell(word[:-1]));assert p==tuple(meta['second_entry']);t=l.trace(spell(word)+l.M);assert not t['feasible']
  records.append(dict(word=word,endpoint_data=meta,immutable_conflict=t,previous_owner=owner(word,t['previous_read']),conflicting_owner=owner(word,t['conflict_read'])))
 allfamilies[c]=records
assert len(allfamilies[0])==25 and len(allfamilies[1])==1278
assert[(family_stats[c,A]['goals'],family_stats[c,A]['words'])for c in(0,1)for A in'FQB']==[(97,11),(112,8),(112,6),(102,948),(117,240),(117,90)]
# Completeness of marker-owned CURRENT-toCORE loss: every old BLACK
# external cell swallowed into a foreign's exitCORE is a FIRST-L input of
# RAW+actualM11 unless genuinely written during that RAW.
capture=[]
for A in'FQB':
 t=l.trace(W[A]+l.M);raw=l.trace(W[A]);ep=after(W[A]);Kout={add(ep[:2],l.rot(q,ep[2]))for q in l.K}
 for g in sorted(Kout):
  if g not in l.K and g not in raw['last']:assert g in t['first']and t['first'][g][0]=='L'
  capture.append(dict(foreign=A,actual_EXIT_CORE_cell=g,in_ENTRY_CORE=g in l.K,actual_RAW_last_read=raw['last'].get(g),actual_complete_first_requirement=t['first'].get(g)))
assert len(capture)==15
# Prescribed smallest nonempty zero-C ordinary sections: exactly one V/U,
# retaining the literal V->F/Q and U->F/Q/B possibilities. These are finite
# controls, not a claim that all zero-C words were searched for existence.
minimal=[];positive=[]
for A in'FQB':
 for b,targets in [('V','FQ'),('U','FQB')]:
  for A2 in targets:
   word='U'+A+b+A2;t=l.trace(spell(word)+l.M)
   if not t['feasible']:
    minimal.append(dict(word=word,feasible=False,conflict=t,previous_owner=owner(word,t['previous_read']),conflicting_owner=owner(word,t['conflict_read'])));continue
   ids=selected_ids(A);seed={q for q,(c,k)in t['first'].items()if c=='L'};B={q:('initial',q)for q in seed};p=(0,0,0);tick=0;cuts=[];IDreads={name:[]for name in ids}
   for i,a in enumerate(word):
    for k,c in enumerate(W[a]):
     cell=p[:2];assert(cell in B)==(c=='L')
     for name,ident in ids.items():
      if cell==tuple(ident['cell']):IDreads[name].append(dict(global_tick0=tick,atom_index0=i,atom=a,own_tick0=k,turn=c,SAME_original_before_read=B.get(cell)==ident['birth_tick0']))
     if c=='L':del B[cell]
     else:B[cell]=tick
     p=after(c,p);tick+=1
    if i>=1:
     K={add(p[:2],l.rot(q,p[2]))for q in l.K};state=[]
     for name,ident in sorted(ids.items()):
      g=tuple(ident['cell']);same=B.get(g)==ident['birth_tick0'];state.append(dict(ID=name,cell=g,birth_tick0=ident['birth_tick0'],same_physically_BLACK=same,CURRENT=same and g not in K,alive_CORE=same and g in K))
     assert all(q['CURRENT']for q in state);cuts.append(dict(after_atom_index0=i,atom=a,RAW_cut_tick0=tick,actual_head=p,selected_ID_state=state))
   for k,c in enumerate(l.M):
    cell=p[:2];assert(cell in B)==(c=='L')
    for name,ident in ids.items():
     if cell==tuple(ident['cell']):IDreads[name].append(dict(global_tick0=tick,owner='actual following word via M11',next_tick0=k,next_read_number1=k+1,turn=c,SAME_original_before_read=B.get(cell)==ident['birth_tick0']))
    if c=='L':del B[cell]
    else:B[cell]=tick
    p=after(c,p);tick+=1
   assert all(B.get(tuple(ident['cell']))==ident['birth_tick0']for ident in ids.values())
   z=dict(word=word,feasible=True,complete_seed=sorted(seed),seed_mass=len(seed),all_physical_reads=tick,RAW_length=len(spell(word)),RAW_cuts=cuts,all_selected_identity_reads=IDreads,all_selected_ids_physically_BLACK_after_actual_M11=True,M11_final_fine_cut_NOT_called_a_marked_CORE_cut=True)
   positive.append(z);minimal.append(dict(word=word,feasible=True,seed_mass=len(seed)))
assert len(minimal)==15 and[(q['word'],q['seed_mass'],q['all_physical_reads'])for q in positive]==[('UQUF',44,187),('UBVF',44,187),('UBUF',47,197)]
# Direct finite proxy verification of the three attained controls. The
# actual F56 cut inside Q/B is a fine endpoint, NOT a new marked CORE.
from fractions import Fraction as Q

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def meet(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if de:
  ss,tt=Q(det(q,v),de),Q(det(q,u),de)
  return dict(old_s=str(ss),new_lo=str(tt),new_hi=str(tt))if 0<=ss<=1 and 0<=tt<=1 else None
 if det(q,u):return None
 k=0 if v[0]else 1;lo,hi=sorted((Q(a[k]-c[k],v[k]),Q(b[k]-c[k],v[k])));lo,hi=max(Q(0),lo),min(Q(1),hi)
 if lo>hi:return None
 pt=add(c,(lo*v[0],lo*v[1]));j=0 if u[0]else 1;ss=Q(pt[j]-a[j],u[j]);return dict(old_s=str(ss),new_lo=str(lo),new_hi=str(hi))
for control in positive:
 p=(0,0,0);segments=[]
 for i,a in enumerate(control['word']):
  start=p
  if a in'FQB':
   mid=after(W['F'],p);segments.append(dict(atom_index0=i,atom=a,piece='Fprefix',start=z(start),end=z(mid)))
   end=after(W[a],p)
   if a!='F':segments.append(dict(atom_index0=i,atom=a,piece=a+'tail',start=z(mid),end=z(end)))
  else:
   end=after(W[a],p);segments.append(dict(atom_index0=i,atom=a,piece='ordinary',start=z(start),end=z(end)))
  p=end
 pairs=[]
 for i,A in enumerate(segments):
  for j in range(i+1,len(segments)):
   B=segments[j];m=meet(A['start'],A['end'],B['start'],B['end'])
   if j==i+1:
    assert A['end']==B['start']and m==dict(old_s='1',new_lo='0',new_hi='0')
   else:assert m is None
   pairs.append(dict(earlier_piece=i,later_piece=j,intersection=m,legal_adjacent_join=j==i+1))
 control['actual_repaired_proxy_pieces']=segments;control['all_closed_piece_pair_checks']=pairs;control['finite_OPEN_proxy_simple_through_second_FOREIGN_RAW']=True
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Actual initial plain genuine U, immediate first foreign A inF/Q/B, then any ordinary RAW section with exactly0 or1 C, then complete second foreign A2 plus actual followingM11. Earlier U-star and selected first-foreign hooks cannot physically lose their SAME R-born IDs during second RAW or its supplied actualM11. No global/simple or firstforeign-induction premise. This does NOT cover arbitrary first-prefix, ownC before firstforeign, or >=2 C interforeign sections.',selected_id_definitions={A:selected_ids(A)for A in'FQB'},selected_foreign_hook_coordinates_postEXIT={A:sorted(S)for A,S in HOOKS.items()},all_necessary_second_FOREIGN_FIRST_L_goals=goal_records,all_exact_nonnegative_count_tuples=tuple_records,all25_zero_C_immutable_words=allfamilies[0],all1278_one_C_immutable_words=allfamilies[1],all15_foreign_EXIT_CORE_capture_checks=capture,endpoint_completeness='After firstA, head hS. At0C use S drifts D(-1,-1),V(-1,-3),U(0,-4), so d+v=x1-gx and d+3v+4u=y1-gy. At1C use S rail, actual C increment(0,-1), then E rail: dS+3vS+4uS+dE+vE=y1-1-gy and4uE=gx-x1+dS+vS-dE-3vE. All remaining counts are nonnegative. Target coordinates come from EVERY actual RAW+M FIRST-L slot, including CORE reads, on ANY chosen original identity. These exact finite budgets bound counts as a consequence of endpoint, never by an imposed rail depth. Every ordering of each count multiset is generated.',identity_loss_completeness='An original SAME BLACK identity physically present at secondENTRY can only first be readL. If it becomes aliveCORE at secondRAW EXIT before physical deletion, canonical complete-context input coverage supplies its actual following FIRST-L marker read, included in the goal set. ENTRYCORE reads are deliberately included too, so no earlier ordinary capture is erased. If an ID already died/reborn in the ordinary section, it is not the SAME original and is not claimed protected.',all15_prescribed_minimal_nonempty_zero_C_controls=minimal,all3_genuine_complete_two_FOREIGN_positive_controls=positive,restoration_obligation='Within this exact genuine U,A starting family, any completed second-foreign SAME-ID loss of these chosen old reserves requires at least TWO ordinary Cs between the foreigners. This is only a necessary obligation, not an attained age2 loss or a bound on later identity restoration.',open_two_C='At twoCs the S/E/N endpoint system has opposite vertical directions and unbounded rail cancellation. No complete twoC or longer classification is claimed. Prescribed finite final-N subfamilies are exploratory only and are not dependencies.',not_claimed=['No induction of firstforeign simplicity through secondforeign.','No original Ustar or hook is assumed to survive a secondforeign in general.','No arbitrary first U-family own-tail/earlier-prefix extension.','No global twoforeign path simplicity, capture, sourceoutput seal or foreign-count budget.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'second_foreign_transfer.json').write_text(json.dumps(out,indent=2)+'\n');print('SecondFOREIGN C0/C1 selected loss:25+1278 endpoint-exhaustive immutable words; three actual UQUF/UBVF/UBUF controls preserve selected original IDs. >=2C necessary only in stated starting family.')
