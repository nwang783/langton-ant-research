from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'STRAIGHT_C_ENTRY_UNREAD_EXTERIOR_BRIDGE.md';F=D/'straight_outer_C_cycle_bridge_certificate.json';assert sha(P).startswith('dd75780f')and sha(F).startswith('f7b873c6')and sha(D/'certify_straight_outer_C_cycle_bridge.py').startswith('008611ea');J=json.loads(F.read_text())
for f,h in J['dependencies'].items():assert sha(Path(f))==h
V=(1j,1,-1j,-1);off=(-1j,-1-1j,-1,0j);xy=lambda q:[int(q.real),int(q.imag)]
controls=[]
for row in J['all8_controls']:
 w=row['word'];h0=row['heading'];P0=len(w);p=0j;h=h0;E=[]
 for t,c in enumerate(w):E.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 d=p;assert xy(d)==row['full_drift']and d.real<0 and d.imag==-d.real and h==h0;m=int(d.imag)
 def rep(q):k=-int(q.real)//m if int(q.real)%m==0 else -(int(q.real)//m);return q-k*d,k
 # Use canonical x in0..m-1 for negative dx, including negative inputx.
 def rep(q):k=-(int(q.real)//m);return q-k*d,k
 def ev(t):k,i=divmod(t,P0);p,h,c=E[i];return p+k*d,h,c,i
 def face(t):p,h,c,i=ev(t);return p+off[h]
 H=defaultdict(list);FS=defaultdict(list)
 for t,(p,h,c)in enumerate(E):q,k=rep(p);H[q].append((t-k*P0,t,h,c));q,k=rep(p+off[h]);FS[q].append(t-k*P0)
 for z in(H,FS):
  for a in z.values():a.sort()
 G={};active=set(FS)
 for q,ts in FS.items():
  t=ts[0]-1;p,h,c,i=ev(t);assert c=='L'and face(t+1)==q
  parent,k=rep(face(t));rc,lift=rep(p);rs=H[rc]
  if rs[0][3]=='R':assert rs[1][0]+lift*P0==t and rs[0][2]==h;G[q]=(parent,k,rc)
 seen=set();cycles=[]
 for q in G:
  path=[];where={};u=q
  while u in G and u not in seen and u not in where:where[u]=len(path);path.append(u);u=G[u][0]
  if u in where:cycles.append(path[where[u]:])
  seen.update(path)
 assert {frozenset(q for q in cy)for cy in cycles}=={frozenset(complex(*q)for q in c['C_vertices'])for c in row['cycles']}
 outers=0
 for ref in row['cycles']:
  vs=[complex(*q)for q in ref['C_vertices']];level=int((vs[0].real+vs[0].imag));assert len(vs)==m and all(q.real+q.imag==level for q in vs)
  outer=sorted([xy(q)for q in active if q.real+q.imag==level+2]);assert outer==ref['outer_row_active_classes']and(not outer)==ref['outer_row_unvisited']
  if outer:
   for z in ref['selected_read_histories']:
    q=complex(*z['class']);assert ''.join('NESW'[h]for ct,t,h,c in H[q])==z['heading_word']
   continue
  outers+=1;B={}
  assert all(q.real+q.imag<=level for q in active)
  for rr in ref['complete_boundary_rows']:
   q=complex(*rr['cycle_cell']);rs=H[q];word=''.join('NESW'[h]for ct,t,h,c in rs);assert word in('NNS','NNSN')and rs[0][3]=='R'
   v,k=rep(q+1);vr=H[v];assert len(vr)==1 and vr[0][2:]==(1,'R')and xy(v)==rr['outer_corner']and k==rr['first_edge_voltage']
   u,l=rep(v-1j);assert l==rr['second_edge_voltage'];B[q]=(v,k);B[v]=(u,l)
   assert sum(h==0 and c=='R'for ct,t,h,c in rs)==sum(h==2 and c=='R'for ct,t,h,c in rs)==1 and not any(h==2 and c=='L'for ct,t,h,c in rs)
   # Rebuild every complete physical history and final rotation, not just words.
   for pp,ls,title in[(q,rs,'complete_history'),(v,vr,'complete_corner_history')]:
    own=[dict(canonical_time=ct,t=t,p=xy(E[t][0]),hi=h,ho=(h+(1 if c=='R'else-1))%4,c=c)for ct,t,h,c in ls];assert own==rr[title]
  assert len(B)==2*m;start=next(iter(B));u=start;path=[];wind=0
  while u not in path:path.append(u);u,k=B[u];wind+=k
  assert u==start and len(path)==2*m and wind==-1 and set(map(tuple,map(xy,path)))==set(map(tuple,ref['actual_single_used_F_circle']['cells']))
 assert outers==1
 controls.append(dict(name=row['name'],power=row['power'],full_drift=xy(d),input_count=sum(a[0][3]=='L'for a in H.values()),unread_row_cycles=outers))
 assert controls[-1]['input_count']==row['input_count']
assert len(controls)==8
O=dict(status='PASS conditional all-cap straight WHITE C-entry plus truly unread outer-row bridge to a wholly single-used first-R map circle',proof=sha(P),certificate=sha(F),script=sha(S),controls=controls,signed_dependencies={name:sha(S.with_name(name))for name in('check_active_C_entry_exit_independent.json','check_C_cycle_excursion_independent.json','check_C_stream_owned_energy_independent.json')},analytic_review=[
'Normalizeui=(-i,i-1),pi=(-i,i),qi=pi+(1,0). The selectedWHITEfirstentry gives firstRN andfirstLN atpi. Atqi incomingW alreadyactivatestheforbiddenouterCrow; E/L wouldenterthatrow. The onlyreadspossibleareE/R, soactualalternationallows exactlyone, suppliedbytheknownfirstRN atpi. This is a derivedWHITE singleton, not a freshrailassumption.',
'EveryRN orLS atpi wouldreadqi next. Firstreadpi isRN, so thereis exactlyoneRN andnoLS. TheuniqueE/R atq_(i+1) enterspi fromN withheadingS; thismustR, andeverySarrivalhasthissamephysicalpredecessor. ExactlyoneRS follows. CompleteWHITEalternationthereforeforcesNNS orNNSN, withnoexterior/interiorreadcap imposed.',
'ThefirstRmap ispi->qi->p_(i-1), an embedded2m-class FULL-d circleofwinding-1. Eachselectededge is physicallyusedonce. Itsq-to-p arrival isat targetlaterR2, notfirstR0, so thecircleisnot acontiguousactualeventcycle. Nonprimitivefullperiodpowers retainall2mclasses; no primitivecollapse.',
'Atpi theR imbalanceiszero, soCcycleheightconstant; qi singletonmakesboundaryC=unvisitedexteriorC+1. Unreadrowis anactualwholehistoryhypothesis, notinferredfromheight, extremality, WHITE alone orfinitefield. Theproofneedsimmediaterowonly; connectedactiveCwalk cannotjumpit.',
'Independently rebuiltallfullhistories, firstentrycycles, unread/active rows, selectedportsandvoltages ineightstandard/prepared10 powers. Standardouter14/90 qualifies; inner10/94hasactiveouterrow and7/8readselectedcells. Prepared10qualifieswithitsgenuineBLACKinput stillpresent. No finiteexcursionalphabet, all-frontoneuseexistence, WHITE S1 orstandardcapture follows.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
