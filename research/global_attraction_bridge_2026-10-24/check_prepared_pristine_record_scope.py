"""Exact affine blocking witnesses for prepared184 waves and20-cell long-flight interiors."""
import json
from pathlib import Path
from fractions import Fraction
from check_fresh_record_trap_bridge import geometry,D
P=Path(__file__).parent;ROOT=P.parent
J=json.loads((ROOT/'causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json').read_text())
def val(a,n):return a[0]*n+a[1]
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def nonnegative(a,lo,hi=None):return val(a,lo)>=0 and(a[0]>=0 or hi is not None and val(a,hi)>=0)
def restrict(dom,a):
 lo,hi=dom;A,B=a
 if A==0:return dom if B>=0 else None
 if A>0:
  z=Fraction(-B,A);lo=max(dom[0],-((-z.numerator)//z.denominator))
 else:
  z=Fraction(-B,A);v=z.numerator//z.denominator;hi=v if hi is None else min(hi,v)
 return None if hi is not None and lo>hi else(lo,hi)
def eq(a):
 if not a[0]:return(1,None)if not a[1]else None
 z=Fraction(-a[1],a[0]);return(z.numerator,z.numerator)if z.denominator==1 and z>=1 else None
def inter(a,b):
 if a is None or b is None:return None
 lo=max(a[0],b[0]);hi=b[1]if a[1]is None else a[1]if b[1]is None else min(a[1],b[1]);return None if hi is not None and lo>hi else(lo,hi)
def query(q):
 families=[]
 for si,s in enumerate(J['stages'][:-1]):
  Q,dr,hh=geometry((0,0),s['heading'],s['word']);sx=s['start_x_N_constant'];sy=s['start_y_N_constant'];st=s['start_time_N_constant'];cnt=s['count_N_constant']
  for i,p in enumerate(Q):
   if s['kind']=='H':
    ja=Fraction(q[0][0]-sx[0],dr[0]);jb=Fraction(q[0][1]-sx[1]-p[0],dr[0]);assert ja.denominator==1
    if jb.denominator!=1:continue
    j=(int(ja),int(jb));dom=eq((sy[0]+dr[1]*j[0]-q[1][0],sy[1]+p[1]+dr[1]*j[1]-q[1][1]))
    if dom is not None:dom=restrict(dom,j)
    if dom is not None:dom=restrict(dom,(cnt[0]-j[0],cnt[1]-1-j[1]))
    tm=(st[0]+len(Q)*j[0],st[1]+len(Q)*j[1]+i)
   else:
    dom=inter(eq((sx[0]-q[0][0],sx[1]+p[0]-q[0][1])),eq((sy[0]-q[1][0],sy[1]+p[1]-q[1][1])));j=(0,0);tm=(st[0],st[1]+i)
   if dom is not None:families.append(dict(stage=si,phase=i,copy=j,time=tm,domain=dom,turn=s['word'][i]))
 candidates=[x for x in families if x['domain'][0]<=1 and(x['domain'][1]is None or x['domain'][1]>=1)];last=max(candidates,key=lambda x:val(x['time'],1));assert last['domain']==(1,None)and last['turn']=='R'
 assert all(nonnegative(sub(last['time'],f['time']),*f['domain'])for f in families)
 return dict(cell=q,last_read=last,all_read_families=families)
NORM=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
WIT=[((56,230),(56,183)),((-56,-215),(-56,-187)),((56,203),(56,212)),((-56,-177),(-56,-227)),((56,228),(56,187)),((-56,-182),(-56,-227)),((56,230),(56,178)),((28,67),(28,139))]
wave=J['stages'][-1];Q,pe,he=geometry((-6,-6),wave['heading'],wave['word']);dr=(pe[0]+6,pe[1]+6);assert dr==(14,14)
out184=[]
for n,q in zip(NORM,WIT):
 projection=lambda x:sum(n[j]*x[j]for j in range(2));a=projection(dr);mx=max(map(projection,Q));mh=(a,mx-a)if a>0 else(0,mx);bw=tuple(sum(n[j]*q[j][u]for j in range(2))for u in range(2));margin=sub(bw,mh);assert nonnegative((margin[0],margin[1]-1),1)
 z=query(q);z.update(normal=n,maximum_head_projection=mh,strict_margin=margin);out184.append(z)
# Twenty-cell: use exact182-step reference and supplied standard word.
G={(0,-1),(1,1),(2,2),(1,3)};B=set(G);p=(0,0);h=1;A=''
for t in range(182):
 c='L'if p in B else'R';A+=c;B^={p};h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
assert(p,h)==((5,1),1)
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
ST=[dict(a=(0,0),b=(0,0),h=1,R=(1,-4),part=61),dict(a=(2,2),b=(-1,0),h=0,R=(2,-5),part=71),dict(a=(-2,6),b=(0,-4),h=3,R=(4,-6),part=61),dict(a=(-10,-2),b=(5,0),h=2,R=(2,-7),part=71),dict(a=(-6,-6),b=(0,8),h=1,R=(3,-4),part=14)]
def rot(x,r):
 x,y=x
 for _ in range(r%4):x,y=y,-x
 return(x,y)
def add_affine(s,z):return((s['a'][0],s['b'][0]+z[0]),(s['a'][1],s['b'][1]+z[1]))
def projected(q,n):return tuple(sum(q[j][u]*n[j]for j in range(2))for u in range(2))
out20=[]
for si,s in enumerate(ST):
 QA,pa,ha=geometry((0,0),s['h'],A);QH,ph,hh=geometry(pa,ha,H);dd=(ph[0]-pa[0],ph[1]-pa[1]);forward=[n for n in NORM if sum(n[j]*dd[j]for j in range(2))>0];assert len(forward)==3
 for n in forward:
  if si<4:
   nxt=ST[si+1];candidates=[add_affine(nxt,rot(g,nxt['h']-1))for g in G];w=max(candidates,key=lambda q:val(projected(q,n),10));readsets=[(QA,(0,0)),(QH,(s['R'][0],s['R'][1]-4))]
  else:
   w=((0,0),(0,2));readsets=[(QA,(0,0)),(QH,(s['R'][0],s['R'][1]-4))] # omit last3 complete periods plus14 partial moves
  margins=[]
  for positions,j in readsets:
   for z in positions:
    q=((s['a'][0]+j[0]*dd[0],s['b'][0]+z[0]+j[1]*dd[0]),(s['a'][1]+j[0]*dd[1],s['b'][1]+z[1]+j[1]*dd[1]));m=sub(projected(w,n),projected(q,n));assert nonnegative(m,10),(si,n,w,q,m);margins.append(m)
  out20.append(dict(stage=si,normal=n,persistent_black_witness=w,source='unread next initial port'if si<4 else'R60 target (0,2), unread until e',minimum_margin_at_k10=min(val(m,10)for m in margins),all_affine_margins=margins))
result=dict(status='AUTHOR all-parameter prepared-record scope check; independent audit pending',wave184=out184,twenty_cell_forward_blockers=out20,twenty_cell_uniform_marked_record_bound=dict(stage_initial_windows=5*286,all_stage_final_windows=5*312+278,recovery_to_canonical_phase0=775,first_canonical_period=104,total_time_cuts=4147,at_most_eight_directions_per_cut=33176),dependencies=dict(manifest184='causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json',execution20='sources/kehao95-core/memory_feedback/proof/scalable-feedback-circuit.md Sections3-4',frozen_target='active_w_archive_itinerary_2026-10-23/twenty_cell_frozen_dormancy_certificate.json'))
(P/'PREPARED_PRISTINE_RECORD_SCOPE_CHECKED.json').write_text(json.dumps(result,indent=2)+'\n')
print('184 margins',[(x['normal'],x['strict_margin'])for x in out184]);print('20 blockers',[(x['stage'],x['normal'],x['minimum_margin_at_k10'])for x in out20]);print('bound4147timecuts33176marked')
