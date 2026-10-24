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

Ssets={'F':{(0,0),(0,1),(-3,-1),(-2,-1)}}
for A,S in Ssets.items():
 geom=l.literal_geometry(W[A]);ep=tuple(geom['endpoint']);norm=lambda q:l.rot(sub(q,ep[:2]),2);poses=[(0,0,0),ep];pp=[(*norm(p[:2]),(p[2]+2)%4)for p in poses];verts=list(map(z,pp));segs=list(zip(verts,verts[1:]));out=[];seen=set();total=0;cols=Counter()
 for atom in'DCVU':
  g=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
  for h in range(4):
   c,d=z((0,0,h)),z(after(W[atom],(0,0,h)))
   for a,b in segs:
    u,v=sub(b,a),sub(d,c)
    corners=[tuple(Q(a[k]+ss*u[k]-c[k]-tt*v[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)]
    bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)]
    for x in range(bounds[0][0],bounds[0][1]+1):
     for y in range(bounds[1][0],bounds[1][1]+1):
      if(x+y+h)%2:continue
      key=(atom,x,y,h)
      if key in seen:continue
      cc,dd=add(c,(2*x,2*y)),add(d,(2*x,2*y));hits=[(j,hh)for j,(aa,bb)in enumerate(segs)if(hh:=hit(aa,bb,cc,dd))is not None]
      if not hits:continue
      if any(hh[1]==0 and not(hh[0]==1 and j==len(segs)-1 and (x,y,h)==(0,0,0)and(len(hh)==2 or hh[2]==0))for j,hh in hits):continue
      hits=[(j,hh)for j,hh in hits if hh[1]>0]
      if not hits:continue
      seen.add(key);total+=1;head=(x,y)
      core=[q for q in S if l.rot(sub(q,head),-h)in l.K]
      white=[q for q in S if(vv:=l.rot(sub(q,head),-h))in tr['first']and tr['first'][vv][0]=='R']
      if core:cols['CORE']+=1
      elif white:cols['WHITE']+=1
      else:
       lost=[q for q in S if list(l.rot(sub(q,head),-h))in g['inputs']];out.append(dict(atom=atom,head=head,h=h,hook_inputs=sorted(lost),contacts=[(j,tuple(str(q)for q in hh))for j,hh in hits]));cols['compatible']+=1
 print(A,'total',total,'counts',cols,'remaining',len(out),'MISS',sum(not r['hook_inputs']for r in out))
 print(out)

assert len(out)==7
expected={('D',(-4,-1),1),('V',(-6,-1),1),('U',(-7,-2),1),('U',(-4,0),2),('U',(-3,1),2),('D',(-1,0),1),('U',(0,-2),0)}
assert{(r['atom'],tuple(r['head']),r['h'])for r in out}==expected
win=json.load(open(R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json'))['all44_exact_source_target_C_window_rows']
ports=[]
for atom in'DVU':
 for inp in map(tuple,l.literal_geometry(W[atom])['inputs']):
  sExit=after(W[atom],(*l.rot((-inp[0],-inp[1]),2),2));eExit=after(W[atom],(*l.rot((-inp[0],-inp[1]),1),1))
  assert sExit[1]<=0 and eExit[1]<=0 and inp[1]>=1 and inp[0]>=-1
  ports.append(dict(atom=atom,input=inp,S_RAW_exit_relative_tag=sExit,E_RAW_exit_relative_tag=eExit))
geomF=l.literal_geometry(W['F']);epF=tuple(geomF['endpoint']);OF={l.rot(sub(tuple(p),epF[:2]),2)for p in geomF['outputs']};trF=l.trace(W['F']+l.M)
terminal=[];proper=[]
for r in out:
 firstt=min(Q(c[1][1])for c in r['contacts']);first=[c for c in r['contacts']if Q(c[1][1])==firstt];old_s={Q(c[1][0])for c in first};assert len(old_s)==1;ss=next(iter(old_s))
 if ss==1:
  assert(r['atom'],tuple(r['head']),r['h'])in{('D',(-1,0),1),('U',(0,-2),0)}
  r.update(actual_outgoing_owner='firstpostV_at_FOREIGN_EXIT_not_incomingF',route='signed_a227_all_firstpostV_source_contacts');terminal.append(r);continue
 assert ss<1
 w=next(x for x in win if x['source_class']=='Fprefix'and x['contact_atom']==r['atom']);kk=[k for k in w['allowed_C_counts_before_contact_ENTRY']if(-k)%4==r['h']];assert len(kk)==1;clock=kk[0]
 assert clock in(2,3);head=tuple(r['head']);g=add(head,(-1,-3)if clock==2 else(1,-1));assert g in OF and g[1]<=-1 and head[1]>g[1]
 original=add(epF[:2],l.rot(g,2));last=trF['last'][original];assert last[0]=='R'and last[1]<len(W['F'])
 loc=l.rot(sub(g,head),-r['h']);fr=l.trace(W[r['atom']]+l.M)['first'][loc];assert fr[0]=='R'and fr[1]<len(W[r['atom']])
 assert(loc,fr[1])==((1,3),26)if clock==2 else(loc,fr[1])==((1,1),6)
 r.update(actual_outgoing_owner='Fprefix',exact_ordinary_C_clock=clock,initial_SAME_FOREIGN_output_reserve=dict(postforeign_cell=g,F_cell=original,last_R_tick0=last[1],last_R_read1=last[1]+1,external_CURRENT_at_F_exit=True),target_white_local=loc,actual_first_R_owner=o.describe(r['atom'],fr[1]),route='negative_y_current_output_coordinate_reserve_then_actual_RAW_WHITE_contradiction');proper.append(r)
assert len(proper)==5 and len(terminal)==2
assert l.literal_geometry(W['C'])['inputs']==[]
result=dict(status='AUTHOR_FIRSTPOSTV_F_PIECE_FIRST_CONTACT_CLOSURE_PENDING_RESERVE_SCOPE_BINDING_AND_REVIEW',scope='Actual U-entry complete8 prefix then FIRSTF and immediate firstpostV; a GLOBAL first new ordinary proxy contact cannot be owned by Fpiece. Arbitrary later ordinaryRAW length, actualterminalM11. Signed sourceV handles FOREEXIT terminals separately. No postFOREIGN full8 or atomcountbound; initial source-history scope of signed portableF reserve is retained. Other firstpostletters/sourceclasses/secondFOREIGN notclaimed.',actual_F_head_poses_normalized_to_exitN=pp,actual_F_piece_vertices=verts,held_current_before_first_contact=[(0,0),(0,1),(-3,-1),(-2,-1)],all62_closed_contact_head_count=total,exact_context_classification=dict(cols),all5_proper_Fsource_lower_output_guards=proper,all2_FOREIGN_EXIT_contacts_owned_by_firstpostV=terminal,all8_trueinput_RAW_exit_bounds_for_negative_y_reserve=ports,portable_coordinate_reserve='InitialCURRENTg withgy<=-1 cannotfirstlose inN0/W1. Its S2 lossRAWexit_y<=gy and laterS heads cannotrise to target_y>gy. ForE3, S loss followedC3 lowersy, E loss also exits_y<=gy, and E heads cannotrise. Thereforeg remainsCURRENT at either targetENTRY. This includes external-toCORE inputs and usesC I0.',all_actor_white_guards_inside_actual_RAW=True,no_FOREIGN_piece_window_on_terminal_b1_cases=True,no_arbitrary_tail_simplicity_or_other_firstpost_letter_or_secondFOREIGN_coverage_capture=True)
Path('/workspace/shared/langton/firstpostV_F_piece_first_contact_2026-10-24/F_piece_contact.json').write_text(json.dumps(result,indent=2)+'\n')
print('F firstpostV:62 heads->55 currentcolour cuts;2 terminals ownedbyV;5 properFsource S2/E3 cases all blocked by genuine negative-y F-output endpoint reserves.')
