"""Exact old-V THIRD true ages zero/one: genuine fields, finite endpoint equations,
all word orders, real prepared controls and naturally closed full-eight predecessor trees.
No arbitrary depth bound or postforeign maturity is used.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import permutations
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def raw(tokens):return ''.join(W[a]for a in tokens)
def after(word,p=(0,0,0)):
 pos,h=p[:2],p[2]
 for c in word:h=(h+(1 if c=='R'else-1))%4;pos=add(pos,l.DIRS[h])
 return*pos,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(atom,p):return z(p),z(after(W[atom],p))
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(q,v),den),Q(det(q,u),den)
  return dict(old_s=str(s),new_t=str(t),point=[str(Q(a[k])+s*u[k])for k in(0,1)])if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(Q(0),lo)),str(min(Q(1),hi))])if max(0,lo)<=min(1,hi)else None

def physical_owner(tokens,tick):
 t=0
 for i,a in enumerate(tokens):
  if tick<t+len(W[a]):return dict(actual_atom_index0=i,actual_atom=a,canonical=o.describe(a,tick-t))
  t+=len(W[a])
 assert 0<=tick-t<len(l.M)
 return dict(actual_atom='next actual word',tick0=tick-t,read_number1=tick-t+1,turn=l.M[tick-t])
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];sources={g['name']:g for g in(G[4],G[5])};beta=(1,-1)
qmin=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text());assert all(q['certified_minimum_C_age']>=2 for q in qmin['slots'].values())
sourcefacts=[]
for n,src in((0,'V'),(1,'V'),(1,'VC')):
 sg=sources[src];tr=l.trace(sg['word']);assert beta not in tr['first'];facts=[]
 for cell in map(tuple,sg['outputs']):
  turn,tick=tr['last'][cell];assert turn=='R';facts.append(dict(SAME_full_source_output_cell=cell,last_R_birth_tick0=tick,birth_read_number1=tick+1,rule='all23 genuine full-produced input slots have certified minimum>=2, applied only before first foreign at full ENTRY age0 or1',source_own_C_tail_preserved=True))
 sourcefacts.append(dict(actual_full_source=src,source_ENTRY_clock=0,source_full_completion_clock=src.count('C'),true_FOREIGN_clock=n,all_current_outputs=facts))
prior=[]
for full in('D','DC','V','VC','VCC','U','UC','UCC'):
 word=raw(full);ep=after(word);slot=add(ep[:2],l.rot(beta,ep[2]));tr=l.trace(word);assert tr['last'][slot]==('R',len(word)-2)and list(slot)in l.literal_geometry(word)['outputs'];prior.append(dict(actual_previous_full=full,actual_previous_full_ENTRY_clock=-full.count('C'),actual_final_atomic_EXIT_clock=0,SAME_beta_oldV_local=beta,actual_previous_full_output_slot=slot,birth_tick0=len(word)-2,birth_read_number1=len(word)-1,post_EXIT_age_at_FOREIGN='zero or one',rule='signed1325 true atomic EXIT consumer-start minimum3; old source V/VC RAW misses beta'))
AP=R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json';angles=[q for q in json.loads(AP.read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces']if q['old_source']=='V'and q['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']in(0,1)];assert Counter(q['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']for q in angles)=={0:37,1:64}
a,b=chord('V',(0,0,0));u=sub(b,a);boxes=[];poses=[];rows=[]
def conflicts(cells,tr,pa,tokens):
 hits=[]
 for cell in sorted(cells):
  loc=l.rot(sub(cell,pa[:2]),-pa[2]);f=tr['first'].get(loc)
  if loc in l.K:hits.append(dict(SAME_CURRENT_cell=cell,foreign_local=loc,reason='outside-core original current identity in FOREIGN entry K'))
  elif f and f[0]=='R':hits.append(dict(SAME_preFOREIGN_BLACK_cell=cell,foreign_local=loc,reason='actual first combined read requires WHITE',combined_tick0=f[1],actual_owner=physical_owner(tokens,f[1])))
 return hits
for angle in angles:
 b1,b2,b3=angle['first'],angle['second'],angle['third'];n=angle['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];K=angle['total_ordinary_C_before_third'];h=angle['third_heading_relative_old'];hA=angle['true_FOREIGN_heading_relative_old'];c,d=chord(b3,(0,0,h));v=sub(d,c);den=det(u,v);corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)];boxes.append(dict(angle=angle,rational_corners=[[[q.numerator,q.denominator]for q in p]for p in corners],integer_bounds=bounds))
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-K)%2:continue
   zz=sub(add(c,(2*x,2*y)),a)
   if den:s,t=Q(det(zz,v),den),Q(det(zz,u),den)
   else:
    assert b3=='V'and K==2 and v==u
    if det(zz,u):continue
    s,t=Q(0),-Q(zz[0],u[0])
   if not(0<=s<1 and 0<t<=1):continue
   p3=(x,y,h);poses.append(dict(angle=angle,third_pose=p3,old_s=str(s),third_t=str(t),parallel_onset=not bool(den)))
   for A in'FQB':
    de=after(raw(A+b1+b2),(0,0,hA));pa=(x-de[0],y-de[1],hA);tokens=A+b1+b2+b3;tr=l.trace(raw(tokens)+l.M)
    for src,sg in sources.items():
     if src.count('C')>n:continue
     row=dict(src=src,n=n,A=A,b1=b1,b2=b2,b3=b3,pa=pa,p3=p3,totalK=K,old_s=str(s),third_t=str(t))
     if not tr['feasible']:row.update(classification='immutable_local_literal_conflict',conflict=tr)
     else:
      cc=conflicts(set(map(tuple,sg['outputs']))|{beta},tr,pa,tokens);row.update(classification='genuine_preFOREIGN_field_cut'if cc else'endpoint_obligation',all_initial_field_conflicts=cc)
     rows.append(row)
assert len(rows)==1419
assert Counter((r['n'],r['src'],r['classification'])for r in rows)=={(0,'V','immutable_local_literal_conflict'):113,(0,'V','genuine_preFOREIGN_field_cut'):163,(0,'V','endpoint_obligation'):63,(1,'V','immutable_local_literal_conflict'):73,(1,'V','genuine_preFOREIGN_field_cut'):386,(1,'V','endpoint_obligation'):81,(1,'VC','immutable_local_literal_conflict'):73,(1,'VC','genuine_preFOREIGN_field_cut'):386,(1,'VC','endpoint_obligation'):81}
words=[];counts=[]
for rowid,r in enumerate(rows):
 if r['classification']!='endpoint_obligation':continue
 x,y,_=r['pa'];n=r['n']
 if n==0:
  dx,dy=x-1,y-3
  if dx<0 or dy<0:continue
  for vn in range(dx+1):
   dn=dx-vn;rest=dy-dn-3*vn
   if rest<0 or rest%4:continue
   un=rest//4;counts.append(dict(rowid=rowid,n=n,dN=dn,vN=vn,uN=un))
   for N in sorted(set(permutations('D'*dn+'V'*vn+'U'*un))):
    if N and not(N[-1]=='U'or N[-1]=='V'and r['A']!='B'):continue
    if not N and r['A']=='B':continue
    T='V'+''.join(N)+r['A']+r['b1']+r['b2']+r['b3'];tr=l.trace(raw(T)+l.M);words.append(dict(rowid=rowid,row=r,Nrun=''.join(N),Wrun='',T=T,feasible=tr['feasible'],conflict=None if tr['feasible']else tr))
 else:
  budget=y-4
  if budget<0:continue
  for dn in range(budget+1):
   for vn in range(budget//3+1):
    for un in range(budget//4+1):
     if r['src']=='VC'and(dn or vn or un):continue
     if r['src']=='V'and dn+vn+un==0:continue
     rem=budget-dn-3*vn-4*un
     if rem<0:continue
     for dw in range(rem+1):
      vw=rem-dw;num=1+dn+vn-dw-3*vw-x
      if num<0 or num%4:continue
      uw=num//4
      if dw+vw+uw==0:continue
      counts.append(dict(rowid=rowid,n=n,dN=dn,vN=vn,uN=un,dW=dw,vW=vw,uW=uw))
      for N in sorted(set(permutations('D'*dn+'V'*vn+'U'*un))):
       for WR in sorted(set(permutations('D'*dw+'V'*vw+'U'*uw))):
        if WR[0]=='U':continue
        if not(WR[-1]=='U'or WR[-1]=='V'and r['A']!='B'):continue
        body=('VC'if r['src']=='VC'else'V'+''.join(N)+'C')+''.join(WR);T=body+r['A']+r['b1']+r['b2']+r['b3'];tr=l.trace(raw(T)+l.M);words.append(dict(rowid=rowid,row=r,Nrun=''.join(N),Wrun=''.join(WR),T=T,feasible=tr['feasible'],conflict=None if tr['feasible']else tr))
assert Counter((w['row']['n'],w['row']['src'],w['feasible'])for w in words)=={(0,'V',False):75,(0,'V',True):2,(1,'V',False):8,(1,'V',True):8,(1,'VC',False):56,(1,'VC',True):40}
positives=[w for w in words if w['feasible']];assert len(positives)==50 and len({w['T']for w in positives})==50
reverse=[]
for w in positives:
 T=w['T'];nodes=[]
 for text in(T,'D'+T):
  queries=[]
  for p in('D','DC','V','VC','VCC','U','UC','UCC'):
   tr=l.trace(raw(p+text)+l.M);queries.append(dict(actual_full_predecessor=p,feasible=tr['feasible'],conflict=None if tr['feasible']else tr))
  nodes.append(dict(actual_word=text,all8_complete_predecessor_queries=queries,complete_survivor_set=[r['actual_full_predecessor']for r in queries if r['feasible']]))
 assert nodes[0]['complete_survivor_set']==['D']and nodes[1]['complete_survivor_set']==[];reverse.append(dict(original_positive=T,n=w['row']['n'],naturally_closed_nodes=nodes,no_U_before_selected_source=True,later_U_after_source_not_claimed_excluded=True))
# Actual finite complete boards, not prepared requirements alone. A true incoming
# beta is R8-born in each D-prepended control; in the unprepended control beta is
# an expressly black older initial root, not mislabelled as an R-born identity.
def physical_control(w,prepend):
 T=('D'if prepend else'')+w['T'];body=raw(T);tr=l.trace(body+l.M);assert tr['feasible'];source_index=1 if prepend else 0;starts=[];pose=(0,0,0);tick=0
 for i,a0 in enumerate(T):starts.append((tick,pose));tick+=len(W[a0]);pose=after(W[a0],pose)
 source_pose=starts[source_index][1];beta_cell=add(source_pose[:2],l.rot(beta,source_pose[2]));seed={p for p,(c,t)in tr['first'].items()if c=='L'}
 if not prepend:assert beta_cell not in tr['first']or tr['first'][beta_cell][0]=='L';seed.add(beta_cell)
 board=set(seed);labels={p:('initial',None)for p in seed};pose=(0,0,0);reads=[];ai=T.index(w['row']['A']);cutA=starts[ai][0];source_start=starts[source_index][0];source_full=w['row']['src'];sg=sources[source_full];births={add(source_pose[:2],l.rot(tuple(q),source_pose[2])):source_start+l.trace(sg['word'])['last'][tuple(q)][1]for q in sg['outputs']};snapshot=None
 for t,c0 in enumerate(body+l.M):
  p=pose[:2];assert(p in board)==(c0=='L');prior_id=labels.get(p)
  if c0=='L':board.remove(p);labels.pop(p)
  else:board.add(p);labels[p]=('R',t)
  reads.append(dict(tick0=t,read_number1=t+1,cell=p,turn=c0,before_identity=prior_id,after_identity=labels.get(p),physical_owner=physical_owner(T,t)));pose=after(c0,pose)
  if t+1==cutA:
   Kcut={add(pose[:2],l.rot(q,pose[2]))for q in l.K};assert all(labels.get(q)==('R',b0)and q not in Kcut for q,b0 in births.items());assert beta_cell not in Kcut
   if prepend:assert labels.get(beta_cell)==('R',8)
   else:assert labels.get(beta_cell)==('initial',None)
   snapshot=dict(cut_before_tick0=cutA,foreign_entry_pose=pose,SAME_source_original_R_outputs=[dict(cell=q,birth_tick0=b0,CURRENT_outside_K=True)for q,b0 in sorted(births.items())],incoming_beta_cell=beta_cell,beta_identity=labels[beta_cell],beta_CURRENT=True)
 assert snapshot
 pieces=[];pose=(0,0,0)
 for i,a0 in enumerate(T):
  if a0 in'FQB':
   mid=after(W['F'],pose);pieces.append(dict(atom=i,label=a0+'F56',a=z(pose),b=z(mid)))
   if a0!='F':pieces.append(dict(atom=i,label=a0+'tail',a=z(mid),b=z(after(W[a0],pose))))
  else:pieces.append(dict(atom=i,label=a0,a=z(pose),b=z(after(W[a0],pose))))
  pose=after(W[a0],pose)
 third_index=len(T)-1;old_segment=chord('V',source_pose);new_segment=chord(T[-1],starts[third_index][1]);hit=contact(*old_segment,*new_segment);assert hit and hit.get('old_s')=='0'and hit.get('new_t')=='1'
 checks=[]
 for j,q in enumerate(pieces):
  for i,p in enumerate(pieces[:j]):
   h0=contact(p['a'],p['b'],q['a'],q['b']);adj=j==i+1 and h0 and h0.get('old_s')=='1'and h0.get('new_t')=='0';checks.append(dict(old_piece=i,new_piece=j,contact=h0,true_adjacent_endpoint=bool(adj)))
 return dict(tokens=T,actual_selected_old_source_index0=source_index,actual_selected_full_source=source_full,complete_seed=sorted(seed),all_other_initial_cells_WHITE=True,initial_black_mass=len(seed),all_actual_RAW_plus_M11_reads=reads,RAW_length=len(body),total_executed_reads=len(reads),actual_final_M11_not_assumed_before_RAW_exit=True,source_foreign_cut=snapshot,third_contact_with_actual_old_V=hit,contact_outgoing_source_owner='selected old V, not earlier incoming D',repaired_proxy_pieces=pieces,all_proxy_pair_checks=checks,genuine_U_entry_before_selected_source=False,later_U_if_present_is_after_selected_source=True)
controls=[physical_control(w,p)for w in positives for p in(False,True)]
assert len(controls)==100
paths=[GP,AP,R/'third_ordinary_local_interface_2026-10-24/manifest.json',R/'audits/third_local_interface_independent.json',R/'audits/dcuv_count5_replay/queries.json',R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',R/'audits/check_atomic_exit_bud_independent.json',R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_OLD_V_THIRD_TRUE_AGES0_1_COMPLETE_ANCESTRY_PENDING_REVIEW',scope='Only global FIRST contact by THIRD ordinary RAW with outgoing OLD V source at true source ENTRY to firstFOREIGN age0 or1, source full V or VC completed. Initial full-eight factor begins U and contains selected source. No later-U ancestry, postFOREIGN age, overall THIRD simplicity or arbitrary-tail result.',genuine_source_current_fields=sourcefacts,all8_prior_full_final_atomic_EXIT_beta_roles=prior,all101_signed_angle_boxes=boxes,all_contact_pose_labels=poses,all1419_actual_source_typed_before_masks=rows,all_exact_endpoint_count_solutions=counts,all189_endpoint_exhaustive_whole_words=words,all50_naturally_closed_complete_predecessor_trees=reverse,all100_complete_board_controls=controls,counts=dict(angle_choices=101,source_mask_rows=1419,endpoint_rows=225,endpoint_words=189,positive_words=50,natural_reverse_nodes=100,all8_reverse_queries=800,physical_complete_controls=100),conclusion='Every endpoint-compatible literal word either fails directly or is one of50 prepared positives whose complete predecessor tree is exactly T<-D,T and then empty. None has a U before selected oldV. Later internal U letters are after selected source and do not provide its uninterrupted-eight U-entry ancestry.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'young_ancestry.json').write_text(json.dumps(out,indent=2)+'\n');print('Old V THIRD ages0/1:101 angles,1419 source masks,225 endpoint rows,77+112 whole words,50 prepared positives; all100 nodes/800 complete predecessor queries naturally close D then empty.100 actual boards replayed.')
