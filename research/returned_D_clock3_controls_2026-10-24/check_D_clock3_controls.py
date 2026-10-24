"""Two attained clock-three D-entry first-returned-contact mechanisms.
Uses minimal returned atom+M11 for predecessor rejection, not a chosen long suffix.
Actual returned C,D or completed returned VC continuations are physically replayed.
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

shorts=('DCDDCVVCDDUFC','DCDDCDDDCDDDDUFV')
completions=('D','C')
expected_nodes=(((),('D',),('DC','D'),('V','D'),('D','DC','D')),((),('V',)))
expected_edges=(({():['D'],('D',):['DC','V'],('DC','D'):['D'],('V','D'):[],('D','DC','D'):[]}),({():['V'],('V',):[]}))
controls=[];pred=[]
for case,(ns,completion,nodes,edges) in enumerate(zip(shorts,completions,expected_nodes,expected_edges)):
 raw=''.join(W[mp[n]]['word'] for n in ns+completion);word=raw+M
 v=literal(word);assert v['feasible'];initial={q for q,b in v['requirements'].items() if b};final,log,ep=physical(word,initial);assert ep==v['endpoint']
 atoms=walk(ns);fi=next(i for i,a in enumerate(atoms) if a['atom']=='F');A=atoms[fi];P=atoms[fi+1]
 assert sum(a['atom']=='C' for a in atoms[:fi])==3
 assert (A['entry'],P['entry']) in (([2,-5,1],[0,-1,3]),([3,-4,1],[1,0,3]))
 pieces=[dict(source=i,kind=a['atom'],start=a['start'],end=a['end']) for i,a in enumerate(atoms[:fi+1])]
 # Foreign is F, whose actual repaired proxy is this single F56 chord.
 for i,a in enumerate(pieces):
  for j,b in enumerate(pieces[i+1:],i+1):
   z=meet(tuple(a['start']),tuple(a['end']),tuple(b['start']),tuple(b['end']))
   if j==i+1:assert z==(1,0),(case,i,j,z)
   else:assert z is None,(case,i,j,z)
 contacts=[]
 for i,a in enumerate(pieces):
  z=meet(tuple(a['start']),tuple(a['end']),tuple(P['start']),tuple(P['end']))
  if z is not None:contacts.append(dict(earlier_piece=i,source_atom=a['kind'],parameters=[str(x) for x in z]))
 assert len(contacts)==2 and contacts[-1]['parameters']==['1','0']
 assert contacts[0]['earlier_piece']==0 and contacts[0]['parameters']==(['0','1'] if case==0 else ['1/2','1/2'])
 # All eight full predecessor choices at EVERY feasible node, until leaves
 # have no choices. No artificial depth cap: this is the entire reverse tree.
 for prefix in nodes:
  good=[];prefixraw=''.join(G[next(i for i in ids if G[i]['name']==n)]['word'] for n in prefix)
  minimal=prefixraw+''.join(W[mp[n]]['word'] for n in ns)+M
  assert literal(minimal)['feasible']
  for gi in ids:
   q=literal(G[gi]['word']+minimal)
   if q['feasible']:good.append(G[gi]['name']);result=dict(feasible=True,initial_mass=sum(q['requirements'].values()))
   else:result=q
   pred.append(dict(control=case,already_prepended_full_packets=prefix,earlier_full_packet=G[gi]['name'],result=result))
  assert good==edges[prefix],(case,prefix,good)
  assert all((n,*prefix) in nodes for n in good)
 assert all(not any(n.startswith('U') for n in prefix) for prefix in nodes)
 controls.append(dict(case=case,minimal_raw_word=ns,complete_prescribed_continuation=ns+completion,initial_black_board=sorted(initial),initial_mass=len(initial),RAW_length=len(raw),all_fine_reads=log,final_mass=len(final),foreign=A,returned=P,old_plus_foreign_proxy=pieces,returned_contacts=contacts,source_D_common_cell=[2,0],all_source_D_common_reads=[dict(context_tick0=t,context_read_number1=t+1,turn=ch) for t,ch in v['reads'][(2,0)]],all_feasible_reverse_nodes=nodes,scope='Actual complete finite D-entry board; no U-entry lift of this FIXED minimal word through any complete-eight prefix. Not an all-word obstruction at the target pose.'))
assert len(pred)==56 and [c['initial_mass'] for c in controls]==[34,35]
# Preserve the two earlier failed prescribed connectors, not as exclusions.
failed=[]
for ns in ('DCDCVVCDUFC','DCDCDUCDUFV'):
 q=literal(''.join(W[mp[a]]['word'] for a in ns)+M);assert not q['feasible'];failed.append(dict(raw_word=ns,first_conflict=q))
D=[GP,QP,R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact_manifest.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Two clock-three D-entry first-returned-contact geometries are attained by actual complete finite boards and completed ordinary continuations. Both fixed minimal words have complete finite reverse predecessor closure without a U-family node. Necessary target geometries remain OPEN for different U-entry histories; no all-word or returned-simplicity claim.',read_convention='tick0 is zero-based; read number1 is one-based. M11 is the verified prefix of the actual following word, not an executed extra word.',two_actual_controls=controls,all56_full_eight_reverse_predecessor_queries=pred,two_failed_earlier_prescribed_connectors=failed,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in D})
(H/'D_clock3_controls.json').write_text(json.dumps(o,indent=2)+'\n');print('Two actual completed boards, masses34/35; all56 predecessor queries close without any U-family prefix.')
