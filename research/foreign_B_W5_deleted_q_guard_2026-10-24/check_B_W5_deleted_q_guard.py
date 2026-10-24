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
for A,S,hole in [('B',{(-2,-4),(-1,-4),(0,-4),(0,-3)},(-1,-3))]:
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

A='B';hole=(-1,-3);target=(1,-2,3);geom=l.literal_geometry(W[A]);ep=tuple(geom['endpoint']);old=add(ep[:2],l.rot(hole,2));trA=l.trace(W[A]+l.M)
assert old==(-2,-2)and trA['last'][old]==('L',60)and list(old)not in geom['outputs']and hole not in l.K
local=l.rot(sub(hole,target[:2]),-target[2]);fr=l.trace(W['U']+l.M)['first'][local];assert local==(-1,2)and fr==('L',13)
necessary=[r for r in res if r['why']=='NECESSARY'];assert len(necessary)==5
assert{(r['atom'],r['k'],tuple(r['head']),r['R_tick'],tuple(r['exit']))for r in necessary}=={('D',4,(-3,-3),8,(-2,-2,0)),('C',3,(-2,-1),7,(-1,-1,0)),('C',4,(-3,-3),8,(-3,-2,3)),('V',4,(-3,-3),8,(-2,0,0)),('U',4,(-3,-3),8,(-3,1,0))}
for r in necessary:
 x,y,h=r['exit']
 if h==0:
  assert r['k']+(r['atom']=='C')==4 and y+1>target[1]
  r['final_endpoint_cut']='remaining_C5_raises_y_and_N_W_heads_cannot_descend_to_target'
 else:
  assert r['atom']=='C'and r['k']==4 and h==3 and x<target[0]
  r['final_endpoint_cut']='C5_exits_left_of_target_and_remaining_W_x_strictly_decreases'
assert len(res)==208 and Counter(r['why']for r in res)=={'sector':104,'current_hook_context_hit':62,'N0_y_negative':18,'W1_below_y1':18,'NECESSARY':5,'earlier_FOREIGN_contact':1}
result=dict(status='AUTHOR_B_W5_GENUINE_DELETED_HOLE_FUNDING_GUARD_PENDING_REVIEW',scope='After actualB followed by arbitrary ordinary RAWs and actual terminalM11, U(1,-2,W) at Cclock5 cannot be the FIRST ordinary B-proxy-contact atom. No U ancestry or absence of ordinary-ordinary contacts required; only no earlierB contact. No Q/other gate/secondforeign/simplicity/capture result.',source_B_hole=dict(postforeign_cell=hole,actual_B_cell=old,last_actual_L_tick0=60,last_actual_L_read1=61,absent_B_O_and_exitCORE=True,WHITE_after_B_RAW=True),target=dict(U_head=target,needed_external_BLACK_input=local,actual_first_input_owner=o.describe('U',13)),all208_last_RAW_R_origin_deadline_and_context_alignments=res,counts=dict(Counter(r['why']for r in res)),all5_final_source_RAW_exit_endpoint_cuts=necessary,core_write_exhaustiveness='A required BLACK cell that was actually L-deleted byB must have a later actual R; choose the last R before targetENTRY. It lies in a completed earlier actual RAW, final R at that coordinate. Every final-RAW-R location is included, including CORE writes, not only O. A sourceC at clock5 cannot complete before target5. Actual marker reads are owned by subsequent RAWs and are included.',hook_context_exclusion='Before firstB contact the SAME fourhook IDs remainCURRENT by715. A firstWHITE or entryCORE hit is impossible; a TRUEBLACK input would lose one at producerEXIT and hence force an earlierB contact. Thus every earlier producer complete context mustMISSthehook. No postforeign age law is used.',no_word_depth_or_rail_length_cap_or_current_CORE_omission=True)
Path('/workspace/shared/langton/foreign_B_W5_deleted_q_guard_2026-10-24/B_W5_deleted_q_guard.json').write_text(json.dumps(result,indent=2)+'\n')
print('B W5 Ugate blocked by its actual L60 deleted lower-q hole:208 exhaustive final-R roles leave5 sources;all5 fail remaining-head endpoint bounds.')
