from pathlib import Path
from collections import defaultdict,Counter
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';G=R/'nonlinear_global_budget_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'CHRONOLOGICAL_LIFETIME_BOUNDARY_GRAPH.md':'d2161fb988c98377726bbacccb561a6856bb89e8d4323b6746ba807e72181e5d','lifetime_boundary_graph.py':'b15a34eb8e94dc2c1aa87fcbc29dc7d79b6645ed7e28a94505d04769b5e225df','certify_lifetime_boundary_graph.py':'0dc234345a2c9b10f1353d296dfa68b7fef96f2a1d143cc9a7131327ce8695f1','lifetime_boundary_graph_certificate.json':'ef020ae604b07dbdb20f442ab5a874f6f3141f5d1a05a488e7900e81297233bb'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'lifetime_boundary_graph_certificate.json').read_text())
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
V=[1j,1,-1j,-1];xy=lambda q:[int(q.real),int(q.imag)]
def quo(q,d):
 k=int(q.real)//abs(int(d.real));k*=1 if d.real>0 else -1
 return q-k*d,k

def analyze(w):
 P=len(w);p=0j;h=0;E=[]
 for i,c in enumerate(w):
  hi=h;h=(h+(1 if c=='R'else-1))%4;E.append(dict(t=i,p=xy(p),hi=hi,ho=h,c=c));p+=V[h]
 d=p;assert h==0 and d.real and d.imag
 H=defaultdict(list);ks={}
 for e in E:
  q,k=quo(complex(*e['p']),d);H[q].append((e['t']-k*P,e['t']));ks[e['t']]=k
 A={};I=set();O=set()
 for q,rows in H.items():
  rows.sort();ids=[i for _,i in rows];cs=[w[i]for i in ids]
  assert all(a!=b for a,b in zip(cs,cs[1:]));assert len({E[i]['hi']%2 for i in ids})==1
  if cs[0]=='L':I.add(ids[0])
  if cs[-1]=='R':O.add(ids[-1])
  for i,j in zip(ids,ids[1:]):
   if w[i]=='R':A[i]=(j,ks[i]-ks[j]);A[j]=(i,ks[j]-ks[i])
 B={}
 for i,(j,v)in A.items():B[(i+1)%P]=((j+1)%P,v+(j==P-1)-(i==P-1))
 maps=[A,B];remaining=set(range(P));paths=[];cycles=[]
 while remaining:
  start=min(remaining);stack=[start];lifts={start:0};vertices=set()
  while stack:
   i=stack.pop();vertices.add(i);remaining.discard(i)
   for M in maps:
    if i in M:
     j,v=M[i];assert E[i]['hi']%2==E[j]['hi']%2
     if j in lifts:assert lifts[j]==lifts[i]+v
     else:lifts[j]=lifts[i]+v;stack.append(j)
  ends=[]
  for i in sorted(vertices):
   if i not in A:assert i in I|O;ends.append((i,lifts[i],'I'if i in I else'O'))
   if i not in B:
    j=(i-1)%P;assert j in I|O;ends.append((j,lifts[i]-(i==0),'I'if j in I else'O'))
  if not ends:cycles.append(tuple(sorted(vertices)));continue
  assert len(ends)==2
  (a,ka,ta),(b,kb,tb)=ends;v=kb-ka;axis='H'if E[start]['hi']%2 else'V'
  pa=complex(*E[a]['p']);pb=complex(*E[b]['p'])+v*d
  assert (pa.imag==pb.imag if axis=='H'else pa.real==pb.real)
  if (a,ta)>(b,tb):a,b,ta,tb,v=b,a,tb,ta,-v
  paths.append((a,b,v,axis,tuple(sorted(vertices))))
 adj=defaultdict(list)
 for k,(a,b,v,axis,_)in enumerate(paths):adj[a].append((b,v,k,axis));adj[b].append((a,-v,k,axis))
 assert set(adj)==I|O and all(len(es)==2 and{e[3]for e in es}=={'H','V'}for es in adj.values())
 remain=set(adj);rc=[]
 while remain:
  st=min(remain);at=st;prev=-1;vol=0;nodes=[]
  while True:
   remain.discard(at);nodes.append(at);b,v,k,ax=next(e for e in adj[at]if e[2]!=prev);at=b;prev=k;vol+=v
   if at==st:break
  rc.append((tuple(sorted(nodes)),abs(vol),len(set(nodes)&I),len(set(nodes)&O)))
 assert sum(v for _,v,_,_ in rc)%2==1
 return E,d,I,O,paths,cycles,rc,H

def normalized_path(p):
 a,b=[e['event']for e in p['ends']];v=p['edge_voltage']
 if a>b:a,b,v=b,a,-v
 return(a,b,v,p['axis'],tuple(p['interior_events']))

def control(name,w,report=None):
 E,d,I,O,paths,cycles,rc,H=analyze(w)
 if report is not None:
  f=report['graph'];assert E==f['events']and xy(d)==f['d']and I==set(f['input_events'])and O==set(f['output_events']);assert set(paths)==set(map(normalized_path,f['root_pairing_edges']));assert set(cycles)=={tuple(c['events'])for c in f['internal_cycles']}and all(not c['voltages']for c in f['internal_cycles']);assert set(rc)=={(tuple(sorted(c['roots'])),abs(c['winding']),c['input_count'],c['output_count'])for c in f['root_skeleton_cycles']}
  bg=report['complete_background'];U=set()
  if name!='S104':
   fp=G/bg['normal_form'];assert sha(fp)==bg['normal_form_sha256'];N=json.loads(fp.read_text());p0=complex(*N['pose'][0]);rot=(1j)**N['pose'][1];key='full_black_orbit_profiles'if name=='P1564'else'full_black_profiles';mass=set()
   for t,b in N[key]:
    for a in range(b,N['drift'][0],2):mass.add(quo((complex(a,a-t)-p0)*rot,d)[0])
   assert complex(*N['drift'])*rot==d and sorted(map(xy,mass))==bg['full_input_black_classes']and N['finite_XOR_cap']==bg['finite_XOR_cap'];U=mass-set(H);assert sorted(map(xy,U))==bg['untouched_black_classes'];odd={q for q,es in H.items()if len(es)%2};assert sorted(map(xy,mass^odd))==bg['full_output_black_classes'];assert mass&set(H)=={quo(complex(*E[i]['p']),d)[0]for i in I}
  count=0
  for axis in 'HV':
   fixed=(lambda z:z.imag)if axis=='H'else(lambda z:z.real);variable=(lambda z:z.real)if axis=='H'else(lambda z:z.imag)
   for r in range(abs(int(fixed(d)))):
    pairs=[];boundary={}
    for a,b,v,ax,_ in paths:
     if ax!=axis:continue
     pa=complex(*E[a]['p']);q=r-fixed(pa)
     if q%fixed(d):continue
     z=int(q//fixed(d));pb=complex(*E[b]['p'])+(z+v)*d;pa+=z*d;assert fixed(pa)==fixed(pb)==r
     aa=(a,'I'if a in I else'O');bb=(b,'I'if b in I else'O');assert aa not in boundary and bb not in boundary;boundary[aa]=variable(pa);boundary[bb]=variable(pb);pairs.append((aa,bb))
    for i,q in enumerate(sorted(U,key=lambda z:(z.real,z.imag))):
     if(r-fixed(q))%fixed(d):continue
     z=(r-fixed(q))//fixed(d);coord=variable(q+z*d);aa=('passive'+str(i),'I');bb=('passive'+str(i),'O');boundary[aa]=boundary[bb]=coord;pairs.append((aa,bb))
    order=sorted(boundary,key=lambda a:(0,boundary[a])if a[1]=='I'else(1,-boundary[a]));idx={a:i for i,a in enumerate(order)}
    ranges=[sorted((idx[a],idx[b]))for a,b in pairs]
    for i,(a,b)in enumerate(ranges):
     for c,e in ranges[i+1:]:assert not(a<c<b<e or c<a<e<b)
    saved=next(x for x in report['all_fibre_boundary_matchings']if x['axis']==axis and x['fixed_coordinate']==r);string=lambda a:str(a[0])+':'+a[1];assert list(map(string,order))==saved['ordered_boundary'];assert{frozenset(map(string,z))for z in pairs}=={frozenset(z)for z in saved['noncrossing_pairs']};count+=1
  return dict(name=name,P=len(w),drift=xy(d),input_roots=len(I),output_roots=len(O),boundary_paths=len(paths),internal_cycles=len(cycles),internal_lengths=dict(Counter(map(len,cycles))),root_cycles=len(rc),fibres_with_passive_strands=count)
 return(len(I),len(O),len(paths),Counter(map(len,cycles)),[(len(z),v,ni,no)for z,v,ni,no in rc])
W={'S104':json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'],'P1564':json.loads((G/'prepared_travelling_wave_certificate.json').read_text())['word'],'Q4352':json.loads((G/'second_prepared_wave_certificate.json').read_text())['word']};controls=[]
for name,w in W.items():assert hashlib.sha256(w.encode()).hexdigest()==J['controls'][name]['word_sha256'];controls.append(control(name,w,J['controls'][name]))
for p in(14,37,71):assert control('',W['S104'][p:]+W['S104'][:p])==control('',W['S104'])
for k in(2,3):
 a=control('',W['S104']*k);assert a[:3]==(0,12*k,12*k)and a[3]==Counter({14:k,2:4*k})and a[4]==[(12*k,1,0,12*k)]
def perfect(S):
 if not S:return[()]
 a=S[0];ans=[]
 for i,b in enumerate(S[1:],1):
  for m in perfect(S[1:i]+S[i+1:]):ans.append(((a,b),)+m)
 return ans
def nc(m):
 return all(not(a<c<b<d or c<a<d<b)for i,(a,b)in enumerate(m)for c,d in m[i+1:])
hm=[m for m in perfect(tuple(range(8)))if nc(m)];vm=[((0,3),(2,6))+m for m in perfect((1,4,5,7))if nc(m)];assert len(hm)==14 and len(vm)==2
coef=[(0,0,0),(0,0,1),(0,0,2),(0,0,6),(0,0,7),(0,6,1),(6,0,2),(6,0,4)]
expected=set()
for h,v in product(hm,vm):
 edges=[('H',a,b,(0,0,0))for a,b in h]+[('V',a,b,tuple((y-x)//3 for x,y in zip(coef[a],coef[b])))for a,b in v];expected.add(tuple(sorted(edges)))
actual=set()
for row in J['middle_short28_boundary_pairing_types']['all28_types']:
 edges=[(e['axis'],*e['ends'],tuple(e['voltage_coefficients_a_c_constant']))for e in row['edges']];actual.add(tuple(sorted(edges)));adj=defaultdict(list)
 for axis,a,b,v in edges:adj[a].append((b,v,axis));adj[b].append((a,tuple(-z for z in v),axis))
 unseen=set(range(8));polys=[]
 while unseen:
  st=min(unseen);at=st;last=None;vv=[0,0,0]
  while True:
   unseen.discard(at);at,v,last=next(e for e in adj[at]if e[2]!=last);vv=[a+b for a,b in zip(vv,v)]
   if at==st:break
  polys.append(vv)
 assert[sum(v[i]for v in polys)%2 for i in range(3)]==[0,0,1]
assert actual==expected and len(actual)==28
out=dict(status='PASS all-cap chronological lifetime boundary graph, actual controls and28 necessary types only',script=sha(S),files=files,controls=controls,analytic_review=['Alternating physical lifetimes are disjoint time intervals at each cell; every same-cell read has the same arrival axis. Each read has exactly one incident horizontal and one incident vertical actual move across the two fibre constructions. Unit moves cannot cross integer-position lifetimes in their interiors; consecutive moves cannot have the same axis. This proves embedded fibre graphs at all read multiplicities.','Nonzero drift in BOTH coordinates makes each physical row and column contain finitely many complete reads. Paths and Jordan cycles have exactly the stated input/output ray endpoints. BLACK-first even histories retain distinct input and output endpoints at the same physical cell; passive unread BLACK strands are retained in prepared controls.','Compressing vertical-arrival lifetimes through their horizontal outgoing moves gives sigma alpha sigma^-1 on horizontal-arrival reads, with exact seam voltage ki-kj+seam(j)-seam(i). No ant splice or actual deletion occurs. Missing beta endpoints pull back through sigma^-1 with the seam shift.','Each WHITE permanent output has one H and one V endpoint, producing g vertices and g edges. Both drift coordinates nonzero preclude a same-orbit single-fibre loop. Quotient internal cycles have zero voltage because they stay on one physical fibre; standard104 has five genuine internal cycles. Their deletion is NOT licensed.','Every actual ant step occurs once in the projected fibre graphs. Lifetime arcs have zero spatial projection and internal loops have zero voltage, so boundary total winding is1 modulo2. No signed integer total, unit winding, single boundary cycle or global spatial noncrossing follows.','The full middle-short odd levels are strictly ordered for3<=c<=a, including a=c. Row matchings are Catalan4=14; column groups2/4/2 give2 choices. All28 affine edge-voltage types and their parity are independently rebuilt. The complete state is not finite: internal traffic, clocks and lifetime spans remain unbounded.','Prepared1564/4352 complete initial/output class fields, finite XOR caps and223/62 passive classes were reconstructed from signed normal forms. These remain infinite prepared backgrounds with actual input obligations, not finite-seed controllers. No novelty claim or unrestricted classification is signed.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
