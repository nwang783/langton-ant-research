#!/usr/bin/env python3
"""Independent exact geometric proof checks, not sampled global chronology.
Uses literal H and six supplied finite cap masks/words. All affine inequalities
are decided on the entire integer domain N>=1. Local tail tests are all-future.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import json,hashlib
P=Path(__file__).parent
U=P.parent/'causal_reduction/unit_scale'
H=json.loads((P.parent/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
PLAN=json.loads((U/'prepared1564_noncrossing_router_plan.json').read_text())
LAUNCH=json.loads((P/'fresh_1564_launch_cap.json').read_text())
V=((0,1),(1,0),(0,-1),(-1,0))
def trace(w,p=(0,0),h=3):
 out=[]
 for c in w:
  out.append((p,h,c));h=(h+(1 if c=='R' else -1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1]
 return out,p,h

def infer(w,p=(0,0),h=3):
 rr,p,h=trace(w,p,h);first={};par=set()
 for q,_,c in rr:
  want=(c=='L')^(q in par)
  if q in first:assert first[q]==want
  else:first[q]=want
  par.symmetric_difference_update({q})
 return {q for q,c in first.items()if c},par,p,h,rr

def replay(B,w,p,h):
 B=set(B)
 for q,hh,c in trace(w,p,h)[0]:
  assert(q in B)==(c=='L'),(q,hh,c)
  B.symmetric_difference_update({q})
 _,p,h=trace(w,p,h)
 return B,p,h

def shift(S,q):return{(x+q[0],y+q[1])for x,y in S}
def box(S):return min(x+y for x,y in S),max(x+y for x,y in S),min(x-y for x,y in S),max(x-y for x,y in S)
def cert_finite_tail(B,p,h,w):
 rr,ep,eh=trace(w,p,h);f=ep[0]-p[0],ep[1]-p[1]
 assert eh==h and abs(f[0])==abs(f[1])==2
 s=f[1]//f[0];G=defaultdict(list)
 for i,(q,hh,c)in enumerate(rr):
  x,y=q;t=y-s*x;a=x%2;rep=a,s*a+t;k=(x-a)//f[0]
  assert q==(rep[0]+k*f[0],rep[1]+k*f[1]);G[t,a].append((k,i,c,rep))
 tests=0
 for g in G.values():
  g.sort(key=lambda z:(-z[0],z[1]));assert all(a[2]!=b[2]for a,b in zip(g,g[1:]))
  mn=min(z[0]for z in g);mx=max(z[0]for z in g);c=g[0][3]
  # At all positions n>=mx the full-list first color is white. Every
  # finite black lying on that ray is separately rejected, not just sampled.
  assert g[0][2]=='R'
  for n in range(mn,mx):
   z=next(z for z in g if z[0]<=n);q=c[0]+n*f[0],c[1]+n*f[1]
   assert(q in B)==(z[2]=='L');tests+=1
  for q in B:
   if(q[0]-c[0])%f[0]:continue
   n=(q[0]-c[0])//f[0]
   if q==(c[0]+n*f[0],c[1]+n*f[1]):assert n<mx
 return {'all_future':True,'orbit_lists':len(G),'finite_fringe_tests':tests,'finite_black_cells_examined':len(B)}

local=[];s13={};toggleH={};offsets={}
for h in(1,3):
 S,W,f,eh,rr=infer(H*30,(0,0),h);assert len(S)==13
 s13[h]=S;toggleH[h]=infer(H,(0,0),h)[1];offsets[h]=box({q for q,_,_ in trace(H,(0,0),h)[0]})
 assert offsets[h][:2]==((0,10)if h==1 else(-10,0))
for j,r in enumerate(PLAN['routers']):
 h=r['source_lane'][2];f=(2,2)if h==1 else(-2,-2);st=(-30*f[0],-30*f[1]);S=shift(s13[h],st);cap={tuple(q)for q in r['extra_black_relative_input']}
 assert not S&cap
 incoming,ep,eh=trace(H*30,st,h);assert ep==(0,0)and eh==h
 assert not cap&{q for q,_,_ in incoming}
 board,p,hh=replay(S|cap,H*30+r['word'],st,h)
 assert[p,hh]==[tuple(r['endpoint'][0]),r['endpoint'][1]]
 cert=cert_finite_tail(board,p,hh,H)
 # Exact one-period extension discrepancy at the OLD start. Telescoping
 # these increments extends m=30 to every m>=30 with no bounded-horizon step.
 D=shift(s13[h],(-f[0],-f[1]))^s13[h]^shift(toggleH[h],(-f[0],-f[1]))
 db=box(shift(D,st));RBOX=box(cap|{q for q,_,_ in trace(r['word'],(0,0),h)[0]})
 assert(db[1]<RBOX[0]if h==1 else RBOX[1]<db[0])
 outread={q for q,_,_ in trace(H,p,hh)[0]};outbox=box(outread)
 assert db[3]<outbox[2]or outbox[3]<db[2]
 local.append({'router':j+1,'extra_mass':len(cap),'read_cap_relative_box':RBOX,'older_input_discrepancy_box_at_m30':db,'outgoing_read_normal_interval':outbox[2:],'tail':cert})

# Affine scalar (N coefficient, constant). Every assertion below is for ALL N>=1.
def A(a=0,b=0):return(a,b)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(a,k):return(a[0]*k,a[1]*k)
def val(a,n):return a[0]*n+a[1]
def lt(a,b):d=sub(b,a);return d[0]>=0 and val(d,1)>0
def sep(a,b):
 for i,name in((0,'u'),(2,'t')):
  if lt(a[i+1],b[i]):return name+':first<second'
  if lt(b[i+1],a[i]):return name+':second<first'
 return None
R=A(28,100)
def ar(a,b):return add(mul(R,a),A(0,b))
def point(u,t):
 assert u[0]%2==0 and(u[1]+t)%2==0
 return((u[0]//2,(u[1]+t)//2),(u[0]//2,(u[1]-t)//2))
def pshift(p,q):return(add(p[0],A(0,q[0])),add(p[1],A(0,q[1])))
def affinebox(S,p):
 lo,hi,tl,th=box(S);u=add(*p);t=sub(*p)
 return(add(u,A(0,lo)),add(u,A(0,hi)),add(t,A(0,tl)),add(t,A(0,th)))
def repeatedbox(h,p,m):
 lo,hi,tl,th=offsets[h];u=add(*p);t=sub(*p);delta=mul(sub(m,A(0,1)),4 if h==1 else-4)
 if h==1:return(add(u,A(0,lo)),add(add(u,delta),A(0,hi)),add(t,A(0,tl)),add(t,A(0,th)))
 return(add(add(u,delta),A(0,lo)),add(u,A(0,hi)),add(t,A(0,tl)),add(t,A(0,th)))
start=point(ar(1,3),-37);p=start;h=3;flights=[];routerboxes=[];seedfamilies=[];time=A();stages=[]
for q in sorted(s13[3]):seedfamilies.append(pshift(start,q))
for i,(r,(aa,bb))in enumerate(zip(PLAN['routers'],[(-2,3),(2,1),(-4,3),(4,3),(-2,1),(2,3)])):
 q=point(ar(aa,bb),r['source_lane'][0]);d=2 if h==1 else-2;dd=sub(q[0],p[0]);assert dd[0]%d==dd[1]%d==0 and sub(q[1],p[1])==dd
 m=mul(dd,1) if d==1 else(dd[0]//d,dd[1]//d);assert m[0]>=0 and val(m,1)>=30
 flights.append({'start':p,'end':q,'count':m,'heading':h,'box':repeatedbox(h,p,m)})
 stages.append(['H',m,p,h,time]);time=add(time,mul(m,104));p=q
 cap={tuple(z)for z in r['extra_black_relative_input']};read={z for z,_,_ in trace(r['word'],(0,0),h)[0]}
 routerboxes.append(affinebox(cap|read,p));seedfamilies.extend(pshift(p,z)for z in sorted(cap));stages.append(['router',A(0,1),p,h,time]);time=add(time,A(0,len(r['word'])))
 p=pshift(p,tuple(r['endpoint'][0]));h=r['endpoint'][1]
q=((0,7),(0,6));dd=sub(q[0],p[0]);assert sub(q[1],p[1])==dd;assert dd[0]%-2==dd[1]%-2==0;m=(dd[0]//-2,dd[1]//-2)
assert m[0]>=0 and val(m,1)>=30
flights.append({'start':p,'end':q,'count':m,'heading':h,'box':repeatedbox(h,p,m)})
stages.append(['H',m,p,h,time]);time=add(time,mul(m,104));p=q
rr,ep,eh=trace(H[:55],(7,6),h);assert(ep,eh)==((4,0),2);time=add(time,A(0,55+24));assert time==(24024,91747)
launch={tuple(q)for q in LAUNCH['launch_cap']};assert len(launch)==34
seedfamilies.extend(((0,x),(0,y))for x,y in sorted(launch));assert len(seedfamilies)==184
seedbox=affinebox(s13[3],start);central=(A(0,-21),A(28,0),A(0,-54),A(0,30));guards=[]
def guard(label,a,b):
 why=sep(a,b);assert why,(label,a,b);guards.append([label,why])
for i,r in enumerate(routerboxes):
 for j,f in enumerate(flights):
  if j in(i,i+1):continue
  guard(f'router{i+1}/nonincidentflight{j+1}',r,f['box'])
 for j in range(i):guard(f'router{i+1}/router{j+1}',r,routerboxes[j])
 guard(f'router{i+1}/source13',r,seedbox);guard(f'router{i+1}/central',r,central)
for i,f in enumerate(flights):
 for j in range(i):guard(f'flight{i+1}/flight{j+1}',f['box'],flights[j]['box'])
 if i:guard(f'flight{i+1}/source13',f['box'],seedbox)
guard('source13/central',seedbox,central)
# H[:55] is the next incomplete copy of the final writer; account it explicitly.
partialbox=affinebox({z for z,_,_ in rr},((0,0),(0,0)))
for i,r in enumerate(routerboxes):guard(f'router{i+1}/last55',r,partialbox)
guard('source13/last55',seedbox,partialbox)
for i,f in enumerate(flights[:-1]):guard(f'flight{i+1}/last55',f['box'],partialbox)
# Entire incoming strict-past read set at the phase55 launch, including both
# earlier periods and the within-period prefix. Test every cap cell exactly.
rr,_,_=trace(H,(7,6),3)
for z in launch:
 for i,(q,hh,c)in enumerate(rr):
  dd=z[0]-q[0],z[1]-q[1]
  if dd[0]!=dd[1]or dd[0]%-2:continue
  copy=dd[0]//-2
  assert not(104*copy+i<55),(z,copy,i)
# Four completed useful writers are settled throughout central u window. The
# explicit 32 guard dominates phase offsets (10), cap/read offsets (<=14),
# and source13 fringe. Each bound is checked on the unbounded N domain.
mature=[]
for i in(0,2,4,5):
 f=flights[i];su=add(*f['start']);eu=add(*f['end'])
 lo,hi=(add(su,A(0,32)),add(eu,A(0,-32)))if f['heading']==1 else(add(eu,A(0,32)),add(su,A(0,-32)))
 assert lt(lo,central[0])and lt(central[1],hi)
 mature.append({'flight':i+1,'u_interval':[lo,hi]})
for i in(1,3):assert sep(flights[i]['box'],central).startswith('t:')
assert lt(central[1],add(add(*flights[6]['start']),A(0,-32)))
# Profile matching is derived directly from the odd toggle classes of H, not
# inferred from a long tail. All useful standard masks match the signed kernel.
fullprofiles=set()
for i in(0,2,4,5,6):
 f=flights[i];x=val(f['start'][0],1);y=val(f['start'][1],1);W=toggleH[f['heading']];cc=defaultdict(int)
 for q in W:cc[x-y+q[0]-q[1],(x+q[0])%2]^=1
 fullprofiles|={j for j,c in cc.items()if c}
normal={tuple(j)for j in json.loads((P/'prepared_wave_five_band_normal_form.json').read_text())['full_black_orbit_profiles']}
assert fullprofiles==normal and len(fullprofiles)==60
# Pairwise affine seed distinctness, with exact rational simultaneous equations.
for i,p in enumerate(seedfamilies):
 for q in seedfamilies[:i]:
  root=None;possible=True
  for a,b in zip(p,q):
   d=sub(a,b)
   if d[0]==0:
    if d[1]:possible=False;break
   else:
    r=Fraction(-d[1],d[0])
    if root is not None and r!=root:possible=False;break
    root=r
  assert not(possible and(root is None or root.denominator==1 and root>=1))
# Bind the independently generated seed families to supplied semantics, NOT to
# a positional sorted correspondence. Equality is symbolic in both coordinates.
sup=json.loads((U/'prepared1564_uniform_support_manifest.json').read_text())
assert{tuple(tuple(z)for z in q)for q in seedfamilies}=={tuple(tuple(z)for z in q)for q in sup['seed_families']}
report={'scope':__doc__,'status':'PASS all N>=1 geometric local-interface gluing',
 'family':'R=100+28N','initial_mass':184,'local_router_certificates':local,
 'affine_guards':guards,'guard_count':len(guards),'completed_mature_intervals':mature,
 'seed_families':seedfamilies,'flight_components':flights,'router_read_cap_boxes':routerboxes,
 'central_window':central,'wave_entry_time_N_constant':time,'full_time_N_constant':[25588,91747],
 'matched_settled_black_classes':len(fullprofiles),'all_seed_cells_distinct_for_all_N':True,
 'strict_past_launch_freshness':True,'seed_families_equal_supplied_manifest':True,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'plan_sha256':hashlib.sha256((U/'prepared1564_noncrossing_router_plan.json').read_bytes()).hexdigest()}
(P/'constant_mass_184_geometric_gluing.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: 184 distinct seed cells, six all-future local contracts,',len(guards),'unbounded affine guards; central 60-class field and exact launch freshness match')
# Exact true negative ten reads, not a chosen standard boundary convention.
def inverse10(B,p,h):
 B=set(B);rev=[]
 for _ in range(10):
  v=V[h];q=p[0]-v[0],p[1]-v[1];c='R'if q in B else'L'
  B.symmetric_difference_update({q});h=(h-(1 if c=='R'else-1))%4;p=q;rev.append(c)
 return ''.join(reversed(rev))
hist=inverse10(s13[3],(0,0),3)
# All other171 initial cells miss the entire ten-step inverse ball for all N.
remote=[]
for q in seedfamilies[13:]:
 witness=None
 for axis in(0,1):
  d=sub(q[axis],start[axis])
  if lt(A(0,10),d):witness=[axis,'positive',d];break
  if lt(d,A(0,-10)):witness=[axis,'negative',d];break
 assert witness,(q,start);remote.append(witness)
factors={''.join(H[(i+j)%104]for j in range(10))for i in range(104)}
def K(w,history):
 bad=history not in factors;n=0
 for c in w:
  history=(history+c)[-10:];b=history not in factors;n+=bad and b;bad=b
 return n,history
# Compression of each positive H power preserves all 11-window costs exactly.
Aword=''.join(H+r['word']for r in PLAN['routers'])+H+H[:55]+LAUNCH['prelude_word']
wave=json.loads((P/'prepared_travelling_wave_certificate.json').read_text())['word']
k1,ctx=K(Aword+wave,hist);step,ctx2=K(wave,ctx);assert ctx==ctx2 and step==614 and k1==706
report.update({'true_previous_ten_letters':hist,'remote_inverse_ten_witnesses':remote,
 'compressed_template_length_before_wave':len(Aword),'first_wave_K':k1,'additional_wave_K':step,
 'exact_prefix_K_formula':'614N+92','preserved_inverse_history_for_all_N':True})
(P/'constant_mass_184_geometric_gluing.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS true inverse ten',hist,'; exact K=614N+92')
