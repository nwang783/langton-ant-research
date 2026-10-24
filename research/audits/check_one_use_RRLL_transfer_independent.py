from pathlib import Path
from itertools import product
from collections import Counter,defaultdict,deque
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'one_use_RRLL_circles_force_a_single_even_reader_row.md';A=D/'check_one_use_RRLL_symbolic_transfer.json'
assert sha(P)=='124f7a9b41d1d77b10358e0a7ad3d757c21f80e28532b708c733b6bfd448f87e';assert sha(A).startswith('00327469')and sha(D/'check_one_use_RRLL_symbolic_transfer.py').startswith('ca1cc4de');J=json.loads(A.read_text())
lib=S.parent/'check_global_max_flow2_staircase_independent.py';N={'__file__':str(lib)};exec(lib.read_text().split('rows=[];stats=Counter()')[0],N);test,cv,out,V=[N[x]for x in('test','cv','out','V')];xy=lambda p:[int(p.real),int(p.imag)];words=lambda a:[''.join(w)for n in range(5)for w in product(a,repeat=n)];mapping={'port':'port','skipped':'skipped_rank','clock':'clock_cycle','global_max':'global_C_max','open':'open'}
def patch(z,j=0):
 s,t,d,e=z;p=2*j
 return{p+0j:cv('NNS'+('N'if s else'')),p+1+0j:cv('WWE'+('W'if t else'')),p+1j:cv('E'),p+1+1j:cv('N'),p-1j:cv(d),p+1-1j:cv(e)}
def encode(w):
 if isinstance(w,complex):return xy(w)
 if isinstance(w,(list,tuple)):return[encode(x)for x in w]
 return w
states=[];counts=Counter();rows=[]
for z in product([0,1],[0,1],words('EW'),words('NS')):
 kind,wit=test(patch(z));assert kind in mapping;result=mapping[kind];counts[result]+=1;rows.append(dict(state=z,result=result,witness=encode(wit)))
 if result=='open':states.append(z)
assert len(rows)==3844 and dict(counts)==J['node_counts']and[list(z)for z in states]==J['states']
assert[(r['state'],r['result'])for r in rows if r['result']!='port']==[(tuple(r['state']),r['result'])for r in J['node_nonport_rows']]
height=[z for z in rows if z['result']=='global_C_max'];assert len(height)==1 and height[0]['state']==(0,0,'EEEE','NSNS')and height[0]['witness']==[[-1,-3],2]
def net(hs):
 su={}
 for p,w in hs.items():
  for h,v in enumerate(V):
   q=p+v
   if q not in hs:continue
   a=[r for r in range(len(w))if out(w,r)==h];b=[r for r,c in enumerate(hs[q])if c==h]
   assert len(a)==len(b)
   su.update({(p,r):(q,s)for r,s in zip(a,b)})
 return su
pairs=[];edges=[];co=Counter()
for i,z in enumerate(states):
 for j,w in enumerate(states):
  if z[1]!=w[0]:continue
  hs=patch(z)|patch(w,1);kind,wit=test(hs);result=mapping[kind];assert result in['port','skipped_rank','open'];co[result]+=1;ar=next(r for r in J['edge_rows']if(r['source'],r['target'])==(i,j));assert ar['result']==result;cert=ar['certificate']
  if result=='port':
   p=complex(*cert['source']);q=complex(*cert['target']);h='NESW'.index(cert['direction']);assert q==p+V[h];aa=[r for r in range(len(hs[p]))if out(hs[p],r)==h];bb=[r for r,c in enumerate(hs[q])if c==h];assert aa==cert['source_ranks']and bb==cert['target_ranks']and len(aa)!=len(bb)
  else:
   su=net(hs)
   if result=='skipped_rank':
    path=[(complex(*p),r)for p,r in cert['path']];assert all(su[a]==b for a,b in zip(path,path[1:]));assert path[-1][0]==path[0][0]and path[-1][1]!=path[0][1]+1;assert all(p!=path[0][0]for p,r in path[1:-1]);assert(cert['start_rank'],cert['returned_rank'])==(path[0][1],path[-1][1])
   else:
    assert sorted([[xy(p),r,xy(q),s]for(p,r),(q,s)in su.items()])==sorted([[p,r,q,s]for(p,r),(q,s)in cert['successor_edges']]);edges.append((i,j))
  pairs.append(dict(source=i,target=j,result=result,independent_witness=encode(wit)))
assert len(pairs)==294 and dict(co)==J['edge_counts']and[list(e)for e in edges]==J['open_edges'];rank={i:int(i in[2,5,12,14,16])for i in range(24)};assert rank=={int(i):r for i,r in J['strict_rank'].items()};assert all(i==j==23 or rank[i]>rank[j]for i,j in edges);assert states[23]==(1,1,'WWWE','SSSN')and[(i,j)for i,j in edges if rank[i]==rank[j]]==[(23,23)]
# Independent whole-lift band successor trace.
def band(p):
 x,y=int(p.real),int(p.imag);return cv({1:('E','N'),0:('NNSN','WWEW'),-1:('WWWE','SSSN')}[y][x%2])
p=1-1j;r=3;path=[(p,r)];directions=[]
while True:
 w=band(p);h=out(w,r);q=p+V[h];aa=[i for i in range(len(w))if out(w,i)==h];ord=aa.index(r);directions.append(h)
 if q.imag not in[-1,0,1]:assert q==-2-2j and h==2 and ord==0;break
 bb=[i for i,c in enumerate(band(q))if c==h];assert len(aa)==len(bb);p,r=q,bb[ord];assert(p,r)not in path;path.append((p,r))
assert len(path)==18 and [[xy(p),r]for p,r in path]==J['band_actual18_read_path'];assert band(1-1j).count(0)==1 and band(1-1j)[3]==0;assert sum(out(band(-2-1j),i)==2 for i in range(4))==1
roles=[]
for p,r in path:
 x,y=int(p.real),int(p.imag);family={1:('T','R'),0:('C','A'),-1:('D','E')}[y][x%2];roles.append((family,x//2,r))
assert[list(v)for v in roles]==J['all_index_disjoint_roles'];assert len({(f,r)for f,j,r in roles})==18
expected={(f,r)for f,n in [('T',1),('R',1),('C',4),('A',4),('D',4),('E',4)]for r in range(n)};assert{(f,r)for f,j,r in roles}==expected
# Exact stream potentials in the surviving single unit, with both directions
# and all zero radial edges. Anchor is the incident selected C=M at(.5,-.5).
hs=patch(states[23]);adj=defaultdict(list)
for p,w in hs.items():
 for h,v in enumerate(V):
  right=p+v/2-1j*v/2;left=p+v/2+1j*v/2;k=sum(out(w,r)==h for r in range(len(w)))-w.count((h+2)%4);adj[left].append((right,k));adj[right].append((left,-k))
vals={.5-.5j:0};queue=deque(vals)
while queue:
 p=queue.popleft()
 for q,k in adj[p]:
  if q in vals:assert vals[q]==vals[p]+k
  else:vals[q]=vals[p]+k;queue.append(q)
assert vals[-.5+.5j]==vals[.5-.5j]==vals[1.5+.5j]==0;assert vals[-.5-1.5j]==vals[1.5-1.5j]==-2
bits=S.parent/'check_one_use_L3_transport_independent.json';assert sha(bits)=='ad205d481891b627c1fa783be2f185a112ae784eca5768149867cf68f004069e'
O=dict(status='PASS all-period pure one-use RRLL transfer reduction, surviving even lower row and exact19-edge open-port channel',proof=sha(P),certificate=sha(A),script=sha(S),signed_bit_transport=sha(bits),all3844_node_results=rows,node_counts=dict(counts),all294_pair_results=pairs,edge_counts=dict(co),states=states,open_edges=edges,strict_rank=rank,only_cyclic_state=23,higher_C_rejection=height[0],band_path=[[xy(p),r]for p,r in path],all_index_roles=roles,stream_values=[[float(p.real),float(p.imag),z]for p,z in vals.items()],analytic_review=[
'The scope supplies complete WHITE cap4 and a whole one-use GLOBAL-M b-circle of pure RRLL shape. The signed cap-free one-use alphabet gives singleton RIGHT and NNS[N]/WWE[W] LEFT cells. The actual geometry normalizes to the stated two-row units; signed LRRL bit equality across each top RR cap gives precisely the inter-unit bit match. No other one-use shape is imported.',
'Independent full3844 product reconstruction retains every exterior0..4 WHITE history and every internal zero port. Literal same-cell returns and explicit positive-clock cycles reject the stated36 nonport cases. The only height failure is(0,0,EEEE,NSNS), with lower C at(-.5,-1.5)=M+2. This is genuinely a GLOBAL maximum rejection, not an imposed local side convention.',
'All294 compatible ordered pairs retain twelve physical cells and both upper/lower connecting edges. The exact126 port failures and150 rank failures have independently replayed certificates; exactly18 edges remain. No hidden clock, height, period or age filtering is used at this stage.',
'The integer potential on the24 states strictly decreases on every surviving edge except23->23. Summing around ANY finite cyclic state word therefore forces all states23, without a bounded cycle-length or period scan. For short full-drift quotients, distinct physical translated cells still satisfy these local patches; additional alias constraints cannot restore a rejected physical return.',
'The surviving lower readers WWWE/SSSN have lower C sectors M-2. The unique north port of still-UNKNOWN F_j enters E_j.L3; the full literal band trace has18 known events and exits by the unique south port into G_(j-1), giving19 actual steps. Neither endpoint port is assumed first or last in its complete reader.',
'Across the whole band, each family/rank role appears exactly once with one integer index shift. Translation of the unit index is a bijection modulo ANY n, proving disjointness for every full quotient, including n=1, rather than only the sampled n<=8. The pure geometry has full d=(-2n,0); distinct row/parity families cannot alias, and no actual cursor or field completion is supplied.',
'This is only the exact pure RRLL necessary row. Unknown F/G multiplicities, old stock, full period, nonminimal lower closures and all mixed non-RRLL curves remain open. No controller, fuel charge, support bound or universal attraction follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(counts,co);print(sha(S.with_suffix('.json')))
