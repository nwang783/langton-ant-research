"""Five genuine UC shifted-boundary CURRENT star/cycle support fences.
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

CP=R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json';CAT=json.loads(CP.read_text())
def edge(q):
 x,y=q
 return ((2*x-1,2*y-1),(2*x+1,2*y+1)) if (x+y)%2==0 else ((2*x-1,2*y+1),(2*x+1,2*y-1))
def path_to_low(cells,start):
 graph={}
 for cell in cells:
  a,b=edge(cell);graph.setdefault(a,[]).append((b,cell));graph.setdefault(b,[]).append((a,cell))
 assert start in graph
 low=min(graph,key=lambda p:(p[1],p[0]));todo=[start];prev={start:None}
 for p in todo:
  for q,cell in graph[p]:
   if q not in prev:prev[q]=(p,cell);todo.append(q)
 assert low in prev
 verts=[low];es=[];q=low
 while prev[q] is not None:p,cell=prev[q];es.append(cell);verts.append(p);q=p
 return low,list(reversed(verts)),list(reversed(es))
rows=[]
for ix,word,use_cycle in((15,'DDD',False),(15,'V',False),(30,'DD',False),(15,'DD',True),(30,'D',True)):
 height=sum({'D':1,'V':3}[c]for c in word);x=len(word);p=(-5-x,-height);h=1
 assert (sum(p)+h)%2==0
 r=CAT['old_source_contact_cases'][ix];fp=tuple(r['foreign_pose'][:2]);rh=r['returned_pose'][2];rp=tuple(r['returned_pose'][:2]);lower=2*fp[1]+1
 ucenter=center(p,h);L={at(q,p,h)for q in((0,0),(0,1),(1,0),(1,1))};Z={at(q,p,h)for q in((1,0),(1,1),(2,0),(2,1))};cells=L|Z if use_cycle else L
 gate=at((3,-1),p,h);gate_EP=add(gate,rot((0,4),h));assert gate[1]==fp[1] if use_cycle else True
 if use_cycle:
  dx=fp[0]-gate[0];assert dx==10 and dx%4!=0
 else:dx=None
 # UC entry age-1; sole first breaker has source age4 => selected-D clock3.
 # Same E y forces only plain U advances4x from that entry to foreign.
 low,verts,es=path_to_low(cells,ucenter);assert low[1]<=lower
 ctx=literal(W[4]['word']+W[mp[r['returned_atom']]]['word']+M)['requirements']
 assert all(rot(sub(q,fp),-1) not in ctx for q in cells)
 # Explicit geometric disjointness of all SAME current edges from F and
 # the returned closed segment. No unsafe collapsed foreign or ghost edge.
 f=walk('F')[0];fstart=center(fp,1);fend=add((2*fp[0],2*fp[1]),rot((-7,-3),1));q=(-1,-1)if ix==15 else(0,0)
 assert center(rp,rh)==fend
 for cell in cells:
  a,b=edge(cell);assert meet(a,b,fstart,fend)is None and meet(a,b,fend,q)is None
 rows.append(dict(catalogue_id=ix,actual_last_positive_C_packet='UC',following_actual_N_run=word,UC_entry=[*p,h],U_entry_center_strictly_inside_by_horizon=ucenter,loop_support_y2=lower,held_cells=sorted(cells),held_graph_path_vertices=verts,held_graph_path_cells=es,path_endpoint_not_strictly_above_support=low,uses_original_cycle=use_cycle,conditional_first_breaker=dict(pose=[*gate,h],source_entry_inclusive_C_age=4,selected_D_clock=3,full_consumer_must_be_plain_U=True,same_y_foreign=True,required_horizontal_gap=dx,allowed_gap_is_positive_multiple_of4=True)if use_cycle else None,foreign_and_returned_context_miss_all_same_ids=True,explicit_foreign_and_returned_edge_intersections='none',contradiction='Connected SAME current edge path starts inside Jordan interior and ends on/outside supporting line, but cannot meet any boundary segment.'))
D=[GP,QP,CP,R/'returned_D_Jordan_ancestry_horizon_2026-10-24/manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/current_residual_barrier_frozen_20261023_1822/manifest.json',R/'core_periodicity_new/causal_cycle_renewal_20261023_1841/manifest.json',R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_PENDING_INDEPENDENT_AUDIT',scope='Five shifted UC boundary cases of TWO D-source chronological-FIRST-returned-contact residues. CURRENT physical edge path, no historical connector. Three permanent-star support contradictions; two intact-cycle support contradictions with exact age4 gate ruled out by10 mod4. No cycle fuel, no permanent-all-cycles, no postforeign age law.',five_exact_current_fence_guards=rows,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'D_UC_current_fence_guards.json').write_text(json.dumps(o,indent=2)+'\n');print('Five CURRENT UC star/cycle support fences; cycle cases10mod4 exclude their only prior first breaker.')
