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

result=[]
for A,S in [('Q',{(-3,-3),(-2,-3),(-1,-3),(-1,-2)}),('B',{(-2,-4),(-1,-4),(0,-4),(0,-3)})]:
 geom=l.literal_geometry(W[A]);ep=tuple(geom['endpoint']);norm=lambda q:l.rot(sub(q,ep[:2]),2)
 O={norm(tuple(p))for p in geom['outputs']};assert S<=O and not S&l.K
 poses=[(0,0,0),after(W['F']),ep];pp=[(*norm(p[:2]),(p[2]+2)%4)for p in poses];verts=list(map(z,pp));segs=list(zip(verts,verts[1:]));rows=[];births=[]
 trace=l.trace(W[A]+l.M)
 for p in sorted(S):
  old=add(ep[:2],l.rot(p,2));last=trace['last'][old];assert last[0]=='R'
  births.append(dict(postforeign_cell=p,original_A_cell=old,last_R_tick0=last[1],last_R_read1=last[1]+1,actual_source_O=True,cut_external_CURRENT=True))
 for atom in'DVU':
  g=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
  for h in range(4):
   for p in sorted(S):
    for inp in map(tuple,g['inputs']):
     head=sub(p,l.rot(inp,h));row=dict(tag=p,atom=atom,input=inp,heading=h,head=head)
     if(sum(head)+h)%2:row['reason']='sector'
     else:
      core=[q for q in sorted(S)if l.rot(sub(q,head),-h)in l.K]
      white=[q for q in sorted(S)if(v:=l.rot(sub(q,head),-h))in tr['first']and tr['first'][v][0]=='R']
      if core:row.update(reason='held_CURRENT_in_entry_CORE',witnesses=core)
      elif white:row.update(reason='held_BLACK_first_required_WHITE',witnesses=white)
      else:
       chord=(z((*head,h)),z(after(W[atom],(*head,h))));contacts=[]
       for j,(aa,bb)in enumerate(segs):
        hh=hit(aa,bb,*chord)
        if hh and not(hh[0]==1 and hh[1]==0 and(len(hh)==2 or hh[2]==0)):
         contacts.append(dict(piece_index0=j,old_s=str(hh[0]),new_t=str(hh[1]),new_t_upper=str(hh[2])if len(hh)==3 else None))
       assert contacts,(A,row)
       row.update(reason='ordinary_consumer_chord_contacts_actual_FOREIGN_proxy',contacts=contacts,ordinary_chord=chord)
     rows.append(row)
 assert len(rows)==128
 result.append(dict(foreign=A,actual_normalized_FOREIGN_head_poses=pp,actual_piece_vertices=verts,guaranteed_same_original_hook_tags=births,all128_input_first_CURRENT_loss_alignments=rows,counts=dict(Counter(r['reason']for r in rows))))
 assert l.literal_geometry(W['C'])['inputs']==[]
positive=[]
for A in'QB':
 T='U'+A+'VCCV';word=''.join(W[c]for c in T)+l.M;tr=l.trace(word);assert tr['feasible']
 black={p for p,(c,t)in tr['first'].items()if c=='L'};seed=set(black);ids={p:('seed',p)for p in black};p=(0,0);h=0;cuts=[];offset=0;endpoints={}
 for i,c in enumerate(T):offset+=len(W[c]);endpoints[offset]=(i,c)
 target=next(r for r in result if r['foreign']==A);tagids={};tags=[]
 for tick,c in enumerate(word):
  assert(p in black)==(c=='L')
  if c=='L':black.remove(p);ids.pop(p)
  else:black.add(p);ids[p]=('R',tick)
  h=(h+(1 if c=='R'else-1))%4;p=add(p,l.DIRS[h])
  if tick+1 in endpoints:
   i,atom=endpoints[tick+1]
   if i==1:
    tags=[add(p,l.rot(tuple(r['postforeign_cell']),h))for r in target['guaranteed_same_original_hook_tags']];tagids={q:ids[q]for q in tags}
   if i>=1:
    K={add(p,l.rot(k,h))for k in l.K}
    assert all(q in black and ids[q]==tagids[q]and q not in K for q in tags)
    cuts.append(dict(after_atom_index0=i,atom=atom,head=(*p,h),all4_same_original_ids_external_CURRENT=True))
 positive.append(dict(word=T,complete_seed=sorted(seed),seed_mass=len(seed),actual_total_reads=len(word),hook_original_R_ids=[[q,tagids[q]]for q in tags],all5_actual_RAW_cut_tag_checks=cuts))
print([(r['foreign'],r['counts'])for r in result])
Path('/workspace/shared/langton/foreign_Q_B_hook_contact_reserve_2026-10-24/hook_contact_reserve.json').write_text(json.dumps(dict(status='AUTHOR_FIXED_SUBSET_CONTACT_OR_CURRENT_RESERVE_PENDING_REVIEW',scope='An actual Q/B, actual ordinary RAW suffix and actual terminalM11. SAME four source-output identities remain CURRENT at every ordinary entry preceding the first nonadjacent contact with that FOREIGN proxy. No U ancestry, C-age or global prefix simplicity required; no second foreign extension.',foreign_cases=result,two_genuine_U_entry_positive_controls=positive,C_has_zero_external_input=True,no_kernel_iteration_assumed_in_proof=True,no_physical_WHITE_permanence_or_simplicity_or_capture=True),indent=2)+'\n')
