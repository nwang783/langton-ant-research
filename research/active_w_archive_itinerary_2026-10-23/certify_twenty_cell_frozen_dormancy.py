"""All-n actual frozen15-edge archive interval in retained20-cell family."""
from certify_twenty_cell_tree_contacts import *
from certify_all_n_young_token_old_support import equality_domain,intersect,impose_nonnegative,linear_nonnegative
from build_forced_input_cycles import deterministic_trace
OUT=Path(__file__).parent
G0={(0,-1),(1,1),(2,2),(1,3)}
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
B=set(G0);p=(0,0);h=1;A='';B173=None
for t in range(182):
 A+='L'if p in B else'R'
 if p in B:B.remove(p);h=(h-1)%4
 else:B.add(p);h=(h+1)%4
 dd=((0,1),(1,0),(0,-1),(-1,0))[h];p=(p[0]+dd[0],p[1]+dd[1])
 if t+1==173:B173=set(B);pose173=(p,h)
assert p==(5,1)and h==1
D0=edges(FullGraph(B173,0),endpoints((0,2),0)[0]);VV=vertices(D0,0);PORTS=set()
for X,Y in VV:
 for a in(-1,1):
  for b in(-1,1):
   q=((X+a)//2,(Y+b)//2)
   if (X,Y)in endpoints(q,0):PORTS.add(q)
assert len(D0)==15 and len(PORTS)==43 and cursors(*pose173)[1]not in VV
ST=[{'pA':(0,0),'pB':(0,0),'h':1,'time':[0,0],'R':[1,-4],'partial':61},{'pA':(2,2),'pB':(-1,0),'h':0,'time':[104,-173],'R':[2,-5],'partial':71},{'pA':(-2,6),'pB':(0,-4),'h':3,'time':[312,-440],'R':[4,-6],'partial':61},{'pA':(-10,-2),'pB':(5,0),'h':2,'time':[728,-821],'R':[2,-7],'partial':71},{'pA':(-6,-6),'pB':(0,8),'h':1,'time':[936,-1296],'R':[3,-4],'partial':14}]

def av(a,k):return a[0]*k+a[1]
def minus(a,b):return[a[0]-b[0],a[1]-b[1]]
def domains(eqx,eqy):
 d=intersect(equality_domain(eqx),equality_domain(eqy));return intersect(d,(10,None))
def families(q):
 out=[]
 for si,s in enumerate(ST):
  tr,end,eh=deterministic_trace(A,(0,0),s['h']);assert eh==s['h'];a=s['pA'];b=s['pB'];tm=s['time'];r=s['R']
  for i,(z,hh,c)in enumerate(tr):
   dom=domains([a[0],b[0]+z[0]-q[0]],[a[1],b[1]+z[1]-q[1]])
   if dom is not None:out.append({'stage':si,'kind':'A','slot':i,'turn':c,'time':[tm[0],tm[1]+i],'domain':dom})
  tr,fin,hh=deterministic_trace(H,end,s['h']);dr=(fin[0]-end[0],fin[1]-end[1])
  for i,(z,hh,c)in enumerate(tr):
   ja=Fraction(-a[0],dr[0]);jb=Fraction(q[0]-b[0]-z[0],dr[0]);assert ja.denominator==1
   if jb.denominator==1:
    j=[int(ja),int(jb)];dom=intersect(equality_domain([a[1]+dr[1]*j[0],b[1]+z[1]+dr[1]*j[1]-q[1]]),(10,None))
    if dom is not None:dom=impose_nonnegative(dom,j)
    if dom is not None:dom=impose_nonnegative(dom,[r[0]-j[0],r[1]-1-j[1]])
    if dom is not None:out.append({'stage':si,'kind':'H','slot':i,'turn':c,'copy':j,'time':[tm[0]+104*j[0],tm[1]+182+104*j[1]+i],'domain':dom})
   if i<s['partial']:
    dom=domains([a[0]+dr[0]*r[0],b[0]+z[0]+dr[0]*r[1]-q[0]],[a[1]+dr[1]*r[0],b[1]+z[1]+dr[1]*r[1]-q[1]])
    if dom is not None:out.append({'stage':si,'kind':'partial','slot':i,'turn':c,'time':[tm[0]+104*r[0],tm[1]+182+104*r[1]+i],'domain':dom})
 return out

def main():
 exclusions=[]
 for q in sorted(PORTS):
  for si,s in enumerate(ST[1:],1):
   for z in G0:
    zz=rot(z,s['h']-1);dom=domains([s['pA'][0],s['pB'][0]+zz[0]-q[0]],[s['pA'][1],s['pB'][1]+zz[1]-q[1]])
    assert dom is None;exclusions.append({'port':q,'future_port':si,'seed_cell_offset':zz,'domain':None})
 ff=[]
 for q in sorted(PORTS):
  for f in families(q):
   dom=impose_nonnegative(f['domain'],[f['time'][0],f['time'][1]-173])
   if dom is not None:f['after173_domain']=dom;f['cell']=q;ff.append(f)
 choices=[f for f in ff if f['after173_domain'][0]<=10 and(f['after173_domain'][1]is None or f['after173_domain'][1]>=10)]
 first=min(choices,key=lambda f:av(f['time'],10));assert list(first['after173_domain'])==[10,None]
 tau=[1248,-1606];assert first['time']==tau and first['cell']==(-1,1)and first['turn']=='R'
 for f in ff:
  lo,hi=f['after173_domain'];assert linear_nonnegative(minus(f['time'],tau),lo,hi)
 q=(-1,1);ee=endpoints(q,0);assert len(set(ee)&VV)==1
 # Fixed recovery dependency gives phase0 at e+775; verify from its exact90-cell field.
 C=json.loads((ROOT/'causal_reduction/root_reactivation_certificate.json').read_text())['protected_field'];B={tuple(z['cell'])for z in C};p=(0,2);h=1;word='';cap775=None
 for t in range(983):
  if t==775:assert p==(5,-4)and h==2;cap775=set(B)
  c='L'if p in B else'R';word+=c
  assert p[0]>=-16 and-14<=p[0]+p[1]<=12
  if c=='L':B.remove(p);h=(h-1)%4
  else:B.add(p);h=(h+1)%4
  dd=((0,1),(1,0),(0,-1),(-1,0))[h];p=(p[0]+dd[0],p[1]+dd[1])
 assert word[775:]==H*2
 out={'status':'PASS all-k>=10 exact frozen complete15-edge archive and first reimport','parameter':'n=2k, k integer>=10','original_mass':20,'target_R_birth':60,'target_cell':[0,2],'source_consumption_time_n_constant':[624,-1516],'frozen_complete_archive':sorted(D0),'archive_vertices':sorted(VV),'complete_incident_ports':sorted(PORTS),'release_cut':173,'first_future_port_read':first,'first_port_read_time_k_constant':tau,'reactivation_cut_k_constant':[1248,-1605],'completed_dormant_episode_length_n_constant':[624,-1778],'future_initial_seed_port_exclusions':exclusions,'all_port_read_families_after173':ff,'fixed_recovery_check':{'protected_cells':len(C),'updates':983,'phase0_tail_time_offset':775,'phase0_pose':[[5,-4],2],'two_period_tail_word':H*2},'source_execution_dependency':'sources/kehao95-core/memory_feedback/proof/scalable-feedback-circuit.md Sections3-4; root_reactivation_certificate.json protected field'}
 (OUT/'twenty_cell_frozen_dormancy_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k not in('frozen_complete_archive','archive_vertices','complete_incident_ports','future_initial_seed_port_exclusions','all_port_read_families_after173','fixed_recovery_check')},indent=2))
if __name__=='__main__':main()
