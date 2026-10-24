"""Six attained D-entry foreign/returned-V mechanisms; exact finite reverse closure.
Uses minimal returned V+M11 for predecessor rejection, not a chosen long suffix.
Full returned VC+M11 is separately physically attained on finite black boards.
"""
from pathlib import Path
from fractions import Fraction
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];W=json.loads(QP.read_text())['macro_words'];M='LLLLRLRRRRL';VEL=((0,1),(1,0),(0,-1),(-1,0));ids=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate('DCVUFQB')}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def at(q,p,h):return add(p,rot(q,h))
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def literal(word):
 p=(0,0);h=0;par=set();rq={};rd={};first={}
 for t,ch in enumerate(word):
  b=(ch=='L')^(p in par)
  if p in rq and rq[p]!=b:return dict(feasible=False,tick=t,cell=p,first_read=first[p],required_initial=b,original_initial=rq[p])
  if p not in rq:rq[p]=b;first[p]=[t,ch]
  rd.setdefault(p,[]).append([t,ch]);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEL[h])
 return dict(feasible=True,requirements=rq,reads=rd,parity=par,endpoint=[*p,h])
def physical(word,initial):
 board=set(initial);p=(0,0);h=0;log=[]
 for t,expected in enumerate(word):
  b=p in board;turn='L'if b else'R';assert turn==expected;log.append(dict(tick=t,cell=p,black_before=b,turn=turn,heading_before=h));board.symmetric_difference_update({p});h=(h+(-1 if turn=='L'else 1))%4;p=add(p,VEL[h])
 return board,log,[*p,h]
def walk(ns):
 p=(0,0);h=0;t=0;atoms=[]
 for n in ns:
  a=literal(W[mp[n]]['word']);ep=tuple(a['endpoint'][:2]);dh=a['endpoint'][2];atoms.append(dict(atom=n,entry=[*p,h],tick=t,start=center(p,h),end=center(at(ep,p,h),(h+dh)%4)));p=at(ep,p,h);h=(h+dh)%4;t+=len(W[mp[n]]['word'])
 return atoms
# Exact rational point contacts; all checked pairs are noncollinear here.
def meet(a,b,c,d):
 u=sub(b,a);v=sub(d,c);w=sub(c,a);cross=lambda q,r:q[0]*r[1]-q[1]*r[0];den=cross(u,v)
 if den:
  s=Fraction(cross(w,v),den);t=Fraction(cross(w,u),den)
  return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 # collinear overlap test via dominant coordinate, preserving point overlaps.
 if cross(w,u):return None
 k=0 if u[0]else 1
 if not u[k]:return None
 x,y=sorted((Fraction(c[k]-a[k],u[k]),Fraction(d[k]-a[k],u[k])));lo=max(0,x);hi=min(1,y)
 if lo>hi:return None
 if lo<hi:return('overlap',lo,hi)
 q=add(a,(u[0]*lo,u[1]*lo));kk=0 if v[0]else 1;t=Fraction(q[kk]-c[kk],v[kk]);return(lo,t)
shorts=('DCDVFV','DDCDUFV','DCDDUQV','DCVVQV','DDCVUQV','DCVUBV')
controls=[];pred=[]
for ns in shorts:
 shortword=''.join(W[mp[n]]['word']for n in ns)+M;fullns=ns+'C';rawword=''.join(W[mp[n]]['word']for n in fullns);word=rawword+M;v=literal(word);assert v['feasible'];initial={q for q,b in v['requirements'].items()if b};final,log,ep=physical(word,initial);assert ep==v['endpoint']
 atoms=walk(ns);fi=next(k for k,a in enumerate(atoms)if a['atom']in('F','Q','B'));A=atoms[fi];P=atoms[fi+1];assert P['atom']=='V'and P['entry']==[-1,0,1];assert sum(a['atom']=='C'for a in atoms[:fi])==1
 tag=(2,0);reads=v['reads'][tag];assert reads[0]==[8,'R']and reads[1]==[P['tick']+19,'L'];assert len([z for z in reads if z[0]<P['tick']])==1
 # Old path plus actual repaired foreign pieces, not unsafe whole Q/B chord.
 pieces=[dict(source=k,kind=a['atom'],start=a['start'],end=a['end'])for k,a in enumerate(atoms[:fi])]
 p=tuple(A['entry'][:2]);h=A['entry'][2];cut=add((2*p[0],2*p[1]),rot((-7,-3),h))
 pieces.append(dict(source=fi,kind='foreign_F56_prefix',start=A['start'],end=cut))
 if A['atom']!='F':pieces.append(dict(source=fi,kind='foreign_actual_tail',start=cut,end=A['end']))
 else:assert cut==A['end']
 for i,a in enumerate(pieces):
  for j,b in enumerate(pieces[i+1:],i+1):
   z=meet(tuple(a['start']),tuple(a['end']),tuple(b['start']),tuple(b['end']))
   if j==i+1:assert z==(1,0),(ns,i,j,z)
   else:assert z is None,(ns,i,j,z)
 contact=[]
 for k,a in enumerate(pieces):
  z=meet(tuple(a['start']),tuple(a['end']),tuple(P['start']),tuple(P['end']))
  if z is not None:contact.append(dict(earlier_piece=k,source=a['source'],parameters=[str(x)for x in z]))
 assert contact[0]==dict(earlier_piece=0,source=0,parameters=['1/2','1/2'])
 assert contact[-1]['parameters']==['1','0'];assert len(contact)==2
 controls.append(dict(short_raw_word=ns,complete_returned_VC_word=fullns,initial_black_board=sorted(initial),initial_mass=len(initial),RAW_length=len(rawword),actual_M11_length=11,all_fine_reads=log,final_mass=len(final),foreign=A,returned_V=P,source_D_birth=[8,'R'],source_D_tag=tag,all_tag_reads=reads,retirement_owner='returned VC actual C-tail RAW phase1, whole returned packet phase19; minimal V-only convention would be following M11 phase1 / exit-core absorption',preforeign_literal_C_clock=1,old_plus_repaired_foreign_proxy=pieces,returned_V_contacts=contact,earliest_new_contact=dict(old_outgoing_atom='D',old_parameter='1/2',returned_parameter='1/2',doubled_point=[0,0]),scope='attained finite D-entry control, not a U-entry history'))
 for extra in(0,1):
  allowed=[]
  for gi in ids:
   pword=G[gi]['word']+W[0]['word']*extra+shortword;check=literal(pword)
   if check['feasible']:allowed.append(gi);res=dict(feasible=True,initial_mass=sum(check['requirements'].values()))
   else:res=check
   pred.append(dict(short_control=ns,already_prepended_D=extra,earlier_full_packet=G[gi]['name'],result=res))
  assert allowed==([0]if extra==0 else[])
assert len(controls)==6 and len(pred)==96
assert[control['initial_mass']for control in controls]==[24,28,29,26,30,32]
# Explicit positive one-D extension for each minimal control, physically checked.
extensions=[]
for ns in shorts:
 w=W[0]['word']+''.join(W[mp[n]]['word']for n in ns+'C')+M;a=literal(w);assert a['feasible'];b={q for q,x in a['requirements'].items()if x};end,log,ep=physical(w,b);extensions.append(dict(raw_word='D'+ns+'C',initial_black_board=sorted(b),initial_mass=len(b),all_actual_D_tags=[dict(cell=q,reads=a['reads'][q])for q in((2,0),(3,1))],scope='one actual preceding plain D allowed; a second arbitrary old-eight predecessor is impossible'))
D=[GP,QP,R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact_manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Six attained finite D-entry foreign/returned-VC mechanisms break ordinary common-bud/produced-input age constraints across foreign, with actual source tags and repaired proxy contacts. Each MINIMAL returned-V+M11 control has exact reverse closure: only one preceding D allowed, then no earlier full-eight packet. Thus none has any U-entry lift within an uninterrupted complete-eight prefix. Not a universal foreign barrier or U-entry countercontrol.',six_actual_controls=controls,ninety_six_complete_eight_predecessor_rows=pred,six_positive_single_D_extensions=extensions,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'D_entry_controls.json').write_text(json.dumps(o,indent=2)+'\n');print('Six actual D-entry controls, full returned VC+M11, masses24/28/29/26/30/32;96 minimal-prefix predecessor checks close after one allowedD.')
