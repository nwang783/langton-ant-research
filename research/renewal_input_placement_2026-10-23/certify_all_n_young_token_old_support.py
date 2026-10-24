"""All-N closed-young-component certificate on the retained affine184 program.
No finite sampling supplies the all-N quantifier.
"""
from check_young_token_old_cycle_support import *
from fractions import Fraction
OUT=Path(__file__).parent
MAN=ROOT/'causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json'

def aval(a,n):return a[0]*n+a[1]
def sub(a,b):return[a[0]-b[0],a[1]-b[1]]
def linear_nonnegative(a,lo=1,hi=None):
 if a[0]>=0:return aval(a,lo)>=0
 return hi is not None and aval(a,hi)>=0

def impose_nonnegative(domain,a):
 lo,hi=domain;A,B=a
 if A==0:return None if B<0 else domain
 if A>0:
  x=Fraction(-B,A);lo=max(domain[0],-((-x.numerator)//x.denominator))
 else:
  x=Fraction(-B,A);bound=x.numerator//x.denominator;hi=bound if hi is None else min(hi,bound)
 return None if hi is not None and lo>hi else(lo,hi)

def equality_domain(a):
 A,B=a
 if A==0:return(1,None)if B==0 else None
 x=Fraction(-B,A)
 return(x.numerator,x.numerator)if x.denominator==1 and x>=1 else None

def intersect(x,y):
 if x is None or y is None:return None
 lo=max(x[0],y[0]);hi=y[1]if x[1]is None else x[1]if y[1]is None else min(x[1],y[1])
 return None if hi is not None and lo>hi else(lo,hi)

def read_families(q):
 J=json.loads(MAN.read_text());out=[]
 for si,s in enumerate(J['stages']):
  word=s['word'][:126]if s['kind']=='wave'else s['word']
  tr,end,eh=deterministic_trace(word,(0,0),s['heading'])
  isH=s['kind']=='H';drift=end
  sx=s['start_x_N_constant'];sy=s['start_y_N_constant'];st=s['start_time_N_constant']
  count=s['count_N_constant']if isH else[0,1]
  for i,(p,h,c)in enumerate(tr):
   if isH:
    # q = start(N)+p_i+j*drift. All retained flight drifts have both coordinates nonzero.
    assert drift[0] != 0
    ja=Fraction(-sx[0],drift[0]);jb=Fraction(q[0]-sx[1]-p[0],drift[0])
    # All retained affine slopes are even and drift_x is +/-2.
    # Therefore no ignored rational-slope congruence class can occur.
    assert ja.denominator == 1
    if jb.denominator!=1:continue
    j=[int(ja),int(jb)]
    eq=[sy[0]+j[0]*drift[1],sy[1]+p[1]+j[1]*drift[1]-q[1]]
    dom=equality_domain(eq)
    if dom is None:continue
    dom=impose_nonnegative(dom,j)
    if dom is None:continue
    dom=impose_nonnegative(dom,[count[0]-j[0],count[1]-1-j[1]])
    if dom is None:continue
    tm=[st[0]+len(word)*j[0],st[1]+len(word)*j[1]+i]
   else:
    dom=intersect(equality_domain([sx[0],sx[1]+p[0]-q[0]]),equality_domain([sy[0],sy[1]+p[1]-q[1]]))
    if dom is None:continue
    j=[0,0];tm=[st[0],st[1]+i]
   out.append({'stage':si,'slot':i,'turn':c,'copy_N_constant':j,'time_N_constant':tm,'domain_N':list(dom)})
 return out

def query(q,beta):
 fam=read_families(q);at1=[f for f in fam if f['domain_N'][0]<=1 and(f['domain_N'][1]is None or 1<=f['domain_N'][1])]
 if not at1:
  assert not fam,(q,'no visit at1 but later family',fam)
  return{'cell':q,'families':[],'last_read':None,'young':False}
 c=max(at1,key=lambda f:aval(f['time_N_constant'],1));assert c['domain_N']==[1,None],(q,c)
 for f in fam:
  lo,hi=f['domain_N'];assert linear_nonnegative(sub(c['time_N_constant'],f['time_N_constant']),lo,hi),(q,c,f)
 young=c['turn']=='R'and linear_nonnegative(sub(c['time_N_constant'],[beta[0],beta[1]+1]))
 if c['turn']=='R'and not young:assert linear_nonnegative(sub(beta,c['time_N_constant'])),(q,c,beta)
 return{'cell':q,'families':fam,'last_read':c,'young':young}

if __name__=='__main__':
 B,q,h,b,t,en,seed=state_with_births(3,126);k=wwhich(q,h);beta=[21112,80557]
 J=json.loads(MAN.read_text());wave=J['stages'][-1]
 assert J['seed_mass']==len(seed)==184 and wave['kind']=='wave' and wave['count_N_constant']==[1,0]
 assert wave['start_x_N_constant']==[0,-6] and wave['start_y_N_constant']==[0,-6]
 _,eq,eh=deterministic_trace(wave['word'][:126],(-6,-6),wave['heading'])
 assert eq==q==(3,-17) and eh==h==0 and k==1
 current=[wave['start_time_N_constant'][0],wave['start_time_N_constant'][1]+126]
 assert current==[24024,91873]
 young={e for e in B-{q}if b[e]>aval(beta,3)}
 u,v=endpoints(q,k);C=component(young,k,u);verts=vertices(C,k);ports=set()
 for X,Y in verts:
  for a in(-1,1):
   for z in(-1,1):
    cell=((X+a)//2,(Y+z)//2)
    if (X,Y)in endpoints(cell,k):ports.add(cell)
 assert q in ports and v not in verts and component(C,k,u)==C
 be,path=widest_cycle_path(B,q,k,b,t);assert be==aval(beta,3)
 cycleG=graph(set(path)|{q},k)
 assert len(path)==17 and len(cycleG)==18 and all(len(a)==2 for a in cycleG.values())
 assert component(set(path)|{q},k,u)==set(path)|{q}
 needed=ports|set(path)|{q};queries={z:query(z,beta)for z in needed}
 assert all(queries[z]['young']for z in C)
 assert all(not queries[z]['young']for z in ports-C-{q})
 for z in[q]+path:
  c=queries[z]['last_read'];assert c is not None and c['turn']=='R'
  assert linear_nonnegative(sub(c['time_N_constant'],beta))
 assert any(queries[z]['last_read']['time_N_constant']==beta for z in path)
 assert queries[q]['last_read']['time_N_constant']==[24024,91857]
 out={'status':'exact all-N affine read ownership and closed young component PASS','source_manifest_sha256':hashlib.sha256(MAN.read_bytes()).hexdigest(),'domain':'all integers N>=1','original_seed_mass':184,'current_time_N_constant':current,'target_cell':q,'target_heading':h,'w_lattice':k,'target_R_birth_N_constant':[24024,91857],'deleted_lifetime_age':16,'maximin_cycle_birth_N_constant':beta,'necessary_cycle_support_age_N_constant':[2912,11316],'closed_component_edges':sorted(C),'closed_component_vertices':sorted(verts),'closed_component_ports':sorted(ports),'cycle_cells':[q]+path,'queries':[queries[z]for z in sorted(queries)]}
 (OUT/'all_n_young_token_old_support_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({a:c for a,c in out.items()if a not in('queries','closed_component_edges','closed_component_vertices','closed_component_ports','cycle_cells')},indent=2));print('component edges',len(C),'ports',len(ports),'queries',len(queries))
