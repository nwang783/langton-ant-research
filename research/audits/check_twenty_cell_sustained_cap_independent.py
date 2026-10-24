from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'active_w_archive_itinerary_2026-10-23'
ns={'__file__':str(SELF.parent/'check_cycle_birth_finite_fuel_independent.py')};exec(Path(ns['__file__']).read_text().split('cells=')[0],ns)
ends,graph,component,rank,connected,step,wvertex=[ns[x]for x in('ends','graph','component','rank','connected','step','wvertex')]
xy=lambda p:(int(p.real),int(p.imag));cross=lambda x,y:x.real*y.imag-x.imag*y.real
std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());H=std['word'];I={complex(*q)for q in std['seed']};assert std['heading']==3
cert=json.loads((R/'standard_unread_cap_2026-10-23/standard_w_frontier_certificate.json').read_text());T={complex(*q)for q in cert['emitted_w_tree_T']};assert len(T)==12
G0={-1j,1+1j,2+2j,1+3j};B=set(G0);p=0j;h=1;A='';states={};readsA=[]
for t in range(182):
 states[t]=(set(B),p,h);readsA.append((p,h,'L'if p in B else'R'));p,h,ch=step(B,p,h);A+=ch
states[182]=(set(B),p,h);assert(p,h,len(B))==(5+1j,1,36)
def trace(word,p=0j,h=0):
 rd=[]
 for ch in word:rd.append((p,h,ch));h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 return rd,p,h
def infinite_H_guard(B,p,h):
 seed={p+x*(-1j)**((h-3)%4)for x in I};assert seed<=B;extra=B-seed
 rd,end,eh=trace(H,p,h);dr=end-p;assert eh==h
 for x in extra:
  for q,hh,ch in rd:
   z=x-q
   if cross(z,dr)==0:
    n=F(int(z.real),int(dr.real));assert n.denominator!=1 or n<0
 return extra,dr
extra0,dr0=infinite_H_guard(B,p,h);assert dr0==2+2j
assert [i for i,(q,hh,ch)in enumerate(readsA)if q==2j]==[60] and readsA[60][2]=='R'
# Inclusive integer domains for exact affine equalities and inequalities.
def ge(dom,a,b):
 if dom is None:return None
 lo,hi=dom;a=F(a);b=F(b)
 if a==0:return dom if b>=0 else None
 if a>0:lo=max(lo,math.ceil(-b/a))
 else:
  u=math.floor(-b/a);hi=u if hi is None else min(hi,u)
 return None if hi is not None and lo>hi else(lo,hi)
def eq(dom,a,b):return ge(ge(dom,a,b),-a,-b)
def nonneg(a,b,dom):return ge(dom,a,b)==dom
# n=2k. All positions and times use exact affine k coefficients.
ST=[(0j,0j,1,(0,0),(1,-4),61),(2+2j,-1+0j,0,(104,-173),(2,-5),71),(-2+6j,-4j,3,(312,-440),(4,-6),61),(-10-2j,5+0j,2,(728,-821),(2,-7),71),(-6-6j,8j,1,(936,-1296),(3,-4),14)]
DATA=[]
for pa,pb,h,tm,rep,partial in ST:
 ar,ep,eh=trace(A,0j,h);hr,end,hh=trace(H,ep,h);dr=end-ep;assert hh==h==eh
 DATA.append(dict(pa=pa,pb=pb,h=h,time=tm,rep=rep,partial=partial,A=ar,H=hr,dr=dr,ep=ep))
 # Exact stage endpoint/time identity to next start or target consumption.
for i,s in enumerate(DATA):
 _,partial_end,ph=trace(H[:s['partial']],s['ep'],s['h']);a=s['pa']+s['rep'][0]*s['dr'];b=s['pb']+s['rep'][1]*s['dr']+partial_end
 ta=s['time'][0]+104*s['rep'][0];tb=s['time'][1]+182+104*s['rep'][1]+s['partial']
 if i<4:assert(a,b,ph,(ta,tb))==(ST[i+1][0],ST[i+1][1],ST[i+1][2],ST[i+1][3])
 else:assert(a,b,ph,ta,tb)==(0j,2j,1,1248,-1516)
def extrema(s,l,maximize):
 out=[]
 for q,hh,ch in s['A']:out.append((l(s['pa']),l(s['pb']+q)))
 ld=l(s['dr']);use_last=(ld>0)==maximize and ld!=0
 for q,hh,ch in s['H']:
  a,b=l(s['pa']),l(s['pb']+q)
  if use_last:a+=ld*s['rep'][0];b+=ld*(s['rep'][1]-1)
  out.append((a,b))
 for q,hh,ch in s['H'][:s['partial']]:out.append((l(s['pa'])+ld*s['rep'][0],l(s['pb']+q)+ld*s['rep'][1]))
 return out
sep=[(0,1,lambda z:z.imag,(2,0)),(2,0,lambda z:z.real,(0,0)),(3,0,lambda z:z.imag,(0,-2)),(4,0,lambda z:z.real,(0,0)),(2,1,lambda z:z.real,(-2,1)),(3,1,lambda z:z.imag,(2,0)),(4,1,lambda z:z.imag,(2,0)),(3,2,lambda z:z.imag,(-2,1)),(2,4,lambda z:z.real-z.imag,(0,-11)),(3,4,lambda z:z.real,(-6,0))]
inequalities=0
for i,j,l,(ba,bb)in sep:
 for a,b in extrema(DATA[i],l,True):assert nonneg(ba-a,bb-1-b,(10,None));inequalities+=1
 for a,b in extrema(DATA[j],l,False):assert nonneg(a-ba,b-bb,(10,None));inequalities+=1
assert inequalities==6832
assert {q for q,hh,ch in readsA[:59]if q in G0}==G0
# Six actual T families in ONE fixed w lattice, reconstructed from physical endpoints.
FAM=[]
for i,s in enumerate(DATA+[dict(pa=0j,pb=5-4j,h=2,rep=None)]):
 h=s['h'];origin=s['pb']+(s['ep']if i<5 else 0);cells={origin+q*(-1j)**((h-3)%4)for q in T};vs=set().union(*(set(ends(q,2))for q in cells));dr=(-2-2j)*(-1j)**((h-3)%4)
 assert len(vs)==13 and rank(cells,2)==0
 offsets=set()
 for u in vs:
  for v in vs:
   z=u-v
   if cross(z,2*dr)==0:
    d=F(int(z.real),int((2*dr).real))
    if d.denominator==1:offsets.add(int(d))
 assert offsets=={0}
 FAM.append(dict(name=f'stage{i}'if i<5 else'final_tail',alpha=2*s['pa'],base=vs,drift=2*dr,hi=(s['rep'][0],s['rep'][1]-1)if i<5 else None,cells=cells))
ref=json.loads((D/'twenty_cell_tree_contact_certificate.json').read_text())
for a,b in zip(FAM,ref['families']):assert sorted(map(xy,a['base']))==list(map(tuple,b['base_vertices']))and xy(a['alpha'])==tuple(b['alpha'])and xy(a['drift'])==tuple(b['drift'])and(a['hi']is None and b['hi']is None or list(a['hi'])==b['hi'])
# Independently solve all parallel vertex equalities as affine integer-k domains.
pairs=[];parallelproof=Counter()
for i,Ai in enumerate(FAM):
 for Aj in FAM[i+1:]:
  da,db=Ai['drift'],Aj['drift']
  if cross(da,db):pairs.append((Ai['name'],Aj['name'],169));continue
  s=1 if da==db else-1;assert db==s*da
  for u in Ai['base']:
   for v in Aj['base']:
    delta=Aj['alpha']-Ai['alpha'];z=v-u;dom=eq((10,None),int(cross(delta,da)),int(cross(z,da)))
    if dom is None:parallelproof['perpendicular_impossible']+=1;continue
    qa=F(int(delta.real),int(da.real));qb=F(int(z.real),int(da.real));ui,uj=Ai['hi'],Aj['hi']
    if s==1:
     if uj is not None:dom=ge(dom,qa+uj[0],qb-2+uj[1])
     if ui is not None:dom=ge(dom,ui[0]-qa,ui[1]-2-qb)
    else:
     dom=ge(dom,qa,qb-4)
     if ui is not None and uj is not None:dom=ge(dom,ui[0]+uj[0]-qa,ui[1]+uj[1]-qb)
    assert dom is None,(Ai['name'],Aj['name'],u,v,qa,qb,dom)
    parallelproof['longitudinal_domain_empty']+=1
  pairs.append((Ai['name'],Aj['name'],0))
assert len(pairs)==15 and Counter(v for a,b,v in pairs)=={169:9,0:6};Pbound=sum(v for a,b,v in pairs);S=5*(4+390+42)+983+42;cap=S+12*(12*S+2*Pbound);assert(S,Pbound,cap)==(3205,1521,501229)
# Reconstruct complete dormant archive at173 and its true episode start.
b173,p173,h173=states[173];dv,de=component(b173,2,ends(2j,2)[0]);assert len(de)==15 and len(dv)==15 and wvertex(p173,h173)not in dv
b172,p172,h172=states[172];assert 2j in component(b172,2,wvertex(p172,h172))[1]
ports=set()
for v in dv:
 for delta in(1+1j,1-1j,-1+1j,-1-1j):
  q=(v+delta)/2
  if v in ends(q,2):ports.add(q)
assert len(ports)==43
for q in ports:
 for s in DATA[1:]:
  for z in G0:
   zz=s['pb']+z*(-1j)**((s['h']-1)%4)-q;dom=eq(eq((10,None),int(s['pa'].real),int(zz.real)),int(s['pa'].imag),int(zz.imag));assert dom is None
families=[]
for q in sorted(ports,key=xy):
 for si,s in enumerate(DATA):
  pa,pb,tm,rr,dr=s['pa'],s['pb'],s['time'],s['rep'],s['dr']
  for slot,(z,hh,ch)in enumerate(s['A']):
   d=eq(eq((10,None),int(pa.real),int((pb+z-q).real)),int(pa.imag),int((pb+z-q).imag));d=ge(d,tm[0],tm[1]+slot-173)
   if d is not None:families.append(dict(cell=xy(q),stage=si,kind='A',slot=slot,turn=ch,time=(tm[0],tm[1]+slot),domain=d))
  for slot,(z,hh,ch)in enumerate(s['H']):
   ja=F(int(-pa.real),int(dr.real));jb=F(int((q-pb-z).real),int(dr.real));assert ja.denominator==1
   if jb.denominator==1:
    ja,jb=int(ja),int(jb);d=eq((10,None),int(pa.imag+dr.imag*ja),int((pb+z-q).imag+dr.imag*jb));d=ge(d,ja,jb);d=ge(d,rr[0]-ja,rr[1]-1-jb);tt=(tm[0]+104*ja,tm[1]+182+104*jb+slot);d=ge(d,tt[0],tt[1]-173)
    if d is not None:families.append(dict(cell=xy(q),stage=si,kind='H',slot=slot,turn=ch,copy=(ja,jb),time=tt,domain=d))
   if slot<s['partial']:
    z0=pb+z+dr*rr[1]-q;za=pa+dr*rr[0];d=eq(eq((10,None),int(za.real),int(z0.real)),int(za.imag),int(z0.imag));tt=(tm[0]+104*rr[0],tm[1]+182+104*rr[1]+slot);d=ge(d,tt[0],tt[1]-173)
    if d is not None:families.append(dict(cell=xy(q),stage=si,kind='partial',slot=slot,turn=ch,time=tt,domain=d))
win=[f for f in families if f['cell']==(-1,1)and f['stage']==4 and f['kind']=='H'and f['slot']==28];assert len(win)==1;win=win[0];assert(win['time'],win['domain'],win['copy'],win['turn'])==((1248,-1606),(10,None),(3,-5),'R')
for f in families:assert nonneg(f['time'][0]-1248,f['time'][1]+1606,f['domain'])
assert len(set(ends(-1+1j,2))&dv)==1
rr=DATA[4]['H'][28];assert wvertex(-1+1j,rr[1])not in dv
fd=json.loads((D/'twenty_cell_frozen_dormancy_certificate.json').read_text());assert sorted(map(xy,de))==list(map(tuple,fd['frozen_complete_archive']))and sorted(map(xy,ports))==list(map(tuple,fd['complete_incident_ports']))
# Independently reconstruct the exact all-k protected restriction using affine guards.
omega=lambda q:q.real>=-16 and -14<=q.real+q.imag<=12
for i,l,side,bound in [(1,lambda q:q.real+q.imag,'min',12),(3,lambda q:q.real+q.imag,'max',-14),(2,lambda q:q.real-q.imag,'max',-44)]:
 for a,b in extrema(DATA[i],l,side=='max'):
  assert nonneg(a,b-bound-1,(10,None))if side=='min'else nonneg(-a,bound-1-b,(10,None))
H0=DATA[0]['H'];assert all((z+6*dr0).real+(z+6*dr0).imag>12 for z,hh,ch in H0)
assert all((z-8-27*dr0).real+(z-8-27*dr0).imag<-14 for z,hh,ch in H0)
for z,hh,ch in DATA[4]['A']:
 a=DATA[4]['pa'].real+DATA[4]['pa'].imag;b=(DATA[4]['pb']+z).real+(DATA[4]['pb']+z).imag;assert nonneg(-a,-15-b,(10,None))
C=set(G0)
for q,hh,ch in readsA:C.symmetric_difference_update({q})
for j in range(6):
 for q,hh,ch in H0:C.symmetric_difference_update({q+j*dr0})
for j in range(-26,0):
 for q,hh,ch in H0:C.symmetric_difference_update({q-8+j*dr0})
for q,hh,ch in H0[:14]:C.symmetric_difference_update({q-8})
C={q for q in C if omega(q)};protected=json.loads((R/'causal_reduction/root_reactivation_certificate.json').read_text())['protected_field'];assert len(C)==90 and C=={complex(*r['cell'])for r in protected}
B=set(C);p=2j;h=1;recovery='';tailcap=None
for t in range(983):
 assert omega(p)
 if t==775:
  assert(p,h)==(5-4j,2);tailcap=set(B);extra,dr=infinite_H_guard(B,p,h);assert dr==2-2j
  tr,_,_=trace(H,p,h);assert all(omega(q)for q,hh,ch in tr)
 p,h,ch=step(B,p,h);recovery+=ch
assert recovery[775:]==H*2
note=D/'TWENTY_CELL_SUSTAINED_CAP.md';nh=hashlib.sha256(note.read_bytes()).hexdigest();assert nh=='45e327d689431f873fc791f5e3955edad080b8d7a6ed23a54232c06b9089e6de'
out={'status':'PASS all-even-n>=20 complete w-component cap and unbounded completed dormancy on actual20-cell family','note_sha256':nh,'source_stage_separation_inequalities':inequalities,'six_family_pair_bounds':pairs,'parallel_vertex_pair_exclusions':dict(parallelproof),'finite_cap_edges':S,'cross_tree_copy_pair_bound':Pbound,'all_time_all_component_edge_cap':cap,'exact_dormant_archive_edges':sorted(map(xy,de)),'incident_port_count':len(ports),'active_at_cut172':True,'dormant_at_cut173':True,'all_port_read_families_after173':families,'first_reimport':win,'dormant_integer_cut_count_n':[624,-1778],'protected_recovery_cells':90,'recovery_guarded_updates':983,'phase0_tail_pose':[5,-4,2],'analytic':['I reconstructed the fresh four-cell182 prefix and its actual infiniteH continuation by minimal13-cell plus unread-field ray exclusions, all five affine stage endpoints, and all6832 strict pairwise read-set inequalities for every integerk>=10. All20 input cells are present initially and belong to their respective disjoint stage read sets. Thus stage execution retains the entire previous field, not cleaned masks.','At every time each long reference consists of its at-most394 startup-cell residue, at-most42 current/terminal K-phase cap, and T copies j=2..R_i-1. Future untouched ports are included in those caps. The983 recovery/alignment/warmup reads and final42 cap cover all new cells before the final sixth T family. Total cap cardinality3205 is a valid over-envelope; source histories and complete input debris remain.','All six physical T families were reconstructed in the same fixed w lattice. Each has13 vertices and distinct copies are vertex-disjoint. Nine nonparallel pairs have at most169 contacting copy pairs at eachk by unique2x2 solution. All6parallel pairs and all169vertex pairs each were independently ruled out by exact affine integer-domain feasibility, including the infinite final family.','Any non-isolated T copy in the envelope touches a cap or a different family. Cap endpoints number at most2S, and each meets at most one copy of each of6families, so at most12S copies touch caps. Cross-family contacts involve at most2P copies. Every complete envelope component is therefore bounded by S+12(12S+2P)=501229; actual components are subgraphs, at every fine cut and throughout the infinite captured future.','The target is active at cut172 and dormant in a COMPLETE15-edge archive at173. All43incident ports miss every other affine initial seed cell. I reconstructed every possible stage A/H/partial read family on those ports and its full integer parameter domain. Earliest is exactly stage4Hslot28 copy3k-5 at e-90, R(-1,1), for everyk>=10. No earlier boundary modification occurs. The edge joins an archive endpoint to the actual outside activewcursor, so the whole archive reimports at cut e-89 and the completed dormant cut count is624n-1778.','The90-cell protected restriction was independently reconstructed by the full XOR formula and affine outside-region guards;983actual recovery reads stay inside it, giving phase0H at(5,-4,S),e+775 and two warmup periods. The infinite H read rays stay in the protected region. This independently confirms the recovery/envelope interface without treating remote black output as absent.','The result forbids a UNIFORM archive-wait or consumed-renewal-age bound depending only on original mass20 and sustained component cap501229 across this family. Every member still captures. It does not refute orbit-specific eventual periodicity under boundedcomponents or prove one nonperiodic seed.'],'scope':'All even n>=20. The smaller106 component cap remains named-parameter evidence only. No uniform capture time, single-orbit unbounded dormancy, or global attraction claim.'}
deps=[R/'standard_unread_cap_2026-10-23/W_FRONTIER.md',R/'standard_unread_cap_2026-10-23/standard_w_frontier_certificate.json',R/'recovered_bundle/ant_global/root/standard.json',R/'sources/kehao95-core/memory_feedback/proof/scalable-feedback-circuit.md',R/'causal_reduction/root_reactivation_certificate.json',D/'twenty_cell_tree_contact_certificate.json',D/'twenty_cell_frozen_dormancy_certificate.json']
out['bound_source_sha256']={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('read families',len(families),'cap',cap)
