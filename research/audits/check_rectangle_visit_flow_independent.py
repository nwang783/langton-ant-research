from pathlib import Path
from collections import Counter
from itertools import product
from math import comb
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'RECTANGLE_VISIT_FLOW_MANIFEST.json')=='ae95dcdef257f2fff6768449011ed58d3bc127cc10602907652d7bfc6be9db8f';m=json.loads((D/'RECTANGLE_VISIT_FLOW_MANIFEST.json').read_text())
for kind in('files','dependencies'):
 for f,h in m[kind].items():assert sha(D/f)==h
J=json.loads((D/'RECTANGLE_VISIT_FLOW_CHECKED.json').read_text());V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)]
def kernel(i,j):return 0 if i<0 or j<0 else 2**(i+j)*comb(i+j,i)
def area(i,j):return 0 if i<0 or j<0 else sum(kernel(a,b)for a in range(i+1)for b in range(j+1))
def local(M,s,e):
 for p,n in M.items():assert n<=2*(M[p-1]+M[p-1j])+1+2*(p==s)+(p==e)
def dynamic_bound(M,s,e,box):
 x0,x1,y0,y1=box;w=x1-x0+1;h=y1-y0+1;rows=[0]*h;const=[0]*h;total=base=0;wanted={(x1-int(s.real),y1-int(s.imag)),(x1-int(e.real),y1-int(e.imag)),(w-1,h-1)};vals={}
 for i in range(w):
  for j in range(h):
   p=complex(x0+i,y0+j);rows[j]=1+2*rows[j]+(2*rows[j-1]if j else 0)+2*(p==s)+(p==e);const[j]=1+2*const[j]+(2*const[j-1]if j else 0);total+=rows[j];base+=const[j]
   assert M[p]<=rows[j]
   if(i,j)in wanted:vals[i,j]=const[j]
 exact=base+2*vals[x1-int(s.real),y1-int(s.imag)]+vals[x1-int(e.real),y1-int(e.imag)];assert total==exact and sum(M.values())<=exact
 assert exact<=base+3*vals[w-1,h-1]<=(w*h+3)*(4**(w+h-1)-1)//3
 return exact
# Complete small-field cover and every actual confined prefix. Tables are direct binomial sums.
small=[];incidence_checks=0
for w,h in((1,6),(2,4),(3,3)):
 cells=[complex(x,y)for x in range(w)for y in range(h)];A={(x,y):area(x,y)for x in range(w)for y in range(h)};SB=sum(A.values());assert SB==sum((w-x)*(h-y)*kernel(x,y)for x in range(w)for y in range(h));pref=states=maxexit=0;digest=hashlib.sha256()
 for mask in range(1<<len(cells)):
  initial={p for j,p in enumerate(cells)if mask>>j&1}
  for start,hs in product(cells,range(4)):
   B=set(initial);p=start;hd=hs;pts=[];heads=[];turns=[];M=Counter();t=0
   while 0<=p.real<w and 0<=p.imag<h:
    pts.append(p);heads.append(hd);M[p]+=1;local(M,start,p);pref+=1
    for q,n in M.items():
     x,y=xy(q);assert n<=A[x,y]+2*kernel(x-int(start.real),y-int(start.imag))+kernel(x-int(p.real),y-int(p.imag))
    b=SB+2*A[w-1-int(start.real),h-1-int(start.imag)]+A[w-1-int(p.real),h-1-int(p.imag)];assert sum(M.values())<=b
    c='L'if p in B else'R';B.symmetric_difference_update({p});turns.append(c);hd=(hd+(1 if c=='R'else-1))%4;p+=V[hd];t+=1;assert t<1000
   # Full confined interval ends at the last inside CUT, before the exit update.
   for q in set(pts):
    good=[];bad=[];charges=[]
    for i in range(len(pts)-1):
     if pts[i]!=q:continue
     inc=pts[i-1]if i else q-V[heads[0]];out=pts[i+1];isbad=inc in(q-1,q-1j)or out in(q-1,q-1j)
     if not isbad:good.append(turns[i]);continue
     bad.append(i)
     if inc in(q-1,q-1j):charges.append(('phantom',)if i==0 else(inc,i-1))
     if out in(q-1,q-1j):charges.append((out,i+1))
    assert len(set(good))<=1 and len(good)<=len(bad)+1 and len(set(charges))==len(charges)
    assert len(bad)<=M[q-1]+M[q-1j]+(q==start);incidence_checks+=1
   states+=1;maxexit=max(maxexit,t);digest.update(f'{mask},{tuple(xy(start))},{hs},{t};'.encode())
   # Different corner choices: exact local inequalities on reflected coordinate counters.
   for ex,ey in((1,-1),(-1,1),(-1,-1)):
    conv=lambda z:complex(ex*z.real,ey*z.imag);MM=Counter({conv(q):n for q,n in M.items()});local(MM,conv(start),conv(pts[-1]))
 row=dict(width=w,height=h,complete_states=states,confined_prefixes=pref,max_exit_updates=maxexit,results_sha256=digest.hexdigest());assert row==next(z for z in J['small_exhaustions']if z['width']==w and z['height']==h);small.append(row)
# Full original MT histories: no cropping, and shifted actual interval counters.
Mdata=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());pin=json.loads((D/'DROUGHT_BOUNDARY_PINNING_CHECKED.json').read_text());controls=[]
for au in J['full_controls']:
 n=au['n'];seed={complex(*q)for q in Mdata['canonical_source']};qm=202+201j;qt=2*n+230+(2*n+229)*1j;seed|={qm+a*(2+2j)for a in(0,1,6,8)}|{qt+a*(2+2j)for a in(0,1,3,5,6)};assert len(seed)==22 and sorted(map(xy,seed))==au['seed'];B=set(seed);p=0j;hd=1;M=Counter([p]);MD=Counter();end=80270+208*n;start=32433+104*n;box=[0,0,0,0];records=0;ds=None
 for t in range(end):
  if t==start:ds=p;MD[p]+=1
  c=p in B;B.symmetric_difference_update({p});hd=(hd+(-1 if c else 1))%4;p+=V[hd];M[p]+=1
  if t>=start:MD[p]+=1
  x,y=xy(p);new=[min(box[0],x),max(box[1],x),min(box[2],y),max(box[3],y)];records+=new!=box;box=new
 c=next(z for z in pin['controls']if z['n']==n);assert B=={complex(*q)for q,i in c['whole_end_black']}and[xy(p),hd]==[list(c['pose_end'][0]),c['pose_end'][1]]
 local(M,0j,p);bound=dynamic_bound(M,0j,p,box);dbox=[int(min(z.real for z in MD)),int(max(z.real for z in MD)),int(min(z.imag for z in MD)),int(max(z.imag for z in MD))];local(MD,ds,p);db=dynamic_bound(MD,ds,p,dbox)
 assert str(bound)==au['exact_whole_bound_decimal']and str(db)==au['exact_drought_bound_decimal']and max(M.values())==au['max_site_head_cuts']and box==au['head_box']and records==au['head_records']
 enc=sorted((tuple(xy(q)),v)for q,v in M.items());assert hashlib.sha256(json.dumps(enc).encode()).hexdigest()==au['local_counter_sha256']and hashlib.sha256(json.dumps(sorted(tuple(xy(q))for q in B)).encode()).hexdigest()==au['whole_field_sha256']
 assert box[1]-box[0]+box[3]-box[2]+2==records+2
 controls.append(dict(n=n,full_reads=end,head_records=records,max_cut_visits=max(M.values()),exact_bound=str(bound),drought_exact_bound=str(db)))
review=['At a fixed physical cell the checkerboard sector fixes the incoming axis and hence the one direction of each incident edge. A visit avoiding the two selected perpendicular predecessor edges has one fixed turn. Actual color alternation gives reads<=2 exceptional+1. Charge exceptional edge incidences to neighbor HEAD CUTS: directed-edge uniqueness makes each neighbor occurrence usable at most once for this edge. A read touching both predecessors may be charged twice, safely overestimating.','Only the initial incoming edge can lack a neighboring in-window cut, contributing at most one exceptional read and hence +2 at p_s. Every outgoing arrival cut, including the final update, is retained. Converting reads to cuts adds exactly +1 at p_t. Thus M(v)<=2M(west)+2M(south)+1+2start+end for any actual interval, including arbitrary endpoint headings and both sectors. No no-bounded-orbit theorem is imported.','With all head cuts confined, outside counts are zero. Coordinate induction solves the linear inequality by Green kernel2^(i+j)binomial(i+j,i), a constant-source cumulative sum, and two endpoint point sources. Summing yields exactly the endpoint-sensitive formula, then S+3A and the conservative (WH+3)(4^(W+H-1)-1)/3. Thin strips are included without a separate induction base.','From an arbitrary cut, the historical HEAD rectangle starts1x1 and each strict record adds exactly one to W+H, so W+H=N+2. The explicit inequality gives a logarithmic lower bound on head-record count. These records need not be pristine or outside the prepared BLACK seed hull; neither record gap density nor a finite capture window is forced.','The local recurrence is an actual visit-count hierarchy in one continuous interval, not a lifetime nesting, fuel, BLACK-hull descent, or no-return-after-exit statement. Its universal proof is analytic; complete small fields and full MT histories test endpoints and bookkeeping only. No canonical104 uniqueness or global attraction conclusion follows.']
out=dict(status='PASS universal directed visit-flow and perimeter-exponential confined-interval bound',manifest=sha(D/'RECTANGLE_VISIT_FLOW_MANIFEST.json'),dependencies=m['dependencies'],small_exhaustions=small,edge_incidence_and_alternation_checks=incidence_checks,all_corner_choices_checked=True,full_original_field_controls=controls,analytic_review=review,scope=m['scope'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
