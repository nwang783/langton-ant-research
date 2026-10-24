from pathlib import Path
from collections import Counter,defaultdict
from itertools import combinations,product
import hashlib,json,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for line in(D/'FIXED_INVENTORY_SHA256SUMS').read_text().splitlines():h,p=line.split(None,1);assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_all_cap_extremal_read_coupling_independent.py'))};exec(Path(ns['__file__']).read_text().split('std=json.loads')[0],ns);trace,key,loops,V=[ns[k]for k in['trace','key','loops','V']];W=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];P=len(W);ev,dr,hh=trace(W);assert(P,dr,hh)==(104,-2+2j,0);xy=lambda q:(int(q.real),int(q.imag));cx=lambda q:complex(*q)
H=defaultdict(list)
for t,p,hi,ho,c in ev:
 q,k=key(p,dr);H[q].append((t-P*k,hi,c))
for q in H:H[q].sort();assert all(z[2]==('R'if j%2==0 else'L')for j,z in enumerate(H[q]))
points=sorted(H,key=xy);index={q:i for i,q in enumerate(points)};options=[];known=[]
for p in points:
 es=H[p];n=len(es);axis=es[0][1]%2;assert all(h%2==axis for t,h,c in es);counts=Counter((c,h)for t,h,c in es);rr=list(range(0,n,2));ll=list(range(1,n,2));oo=[]
 for ra,la in product(combinations(rr,counts['R',axis]),combinations(ll,counts['L',axis])):
  positive=set(ra)|set(la);oo.append(tuple(axis if j in positive else axis+2 for j in range(n)))
 options.append(oo);known.append(oo.index(tuple(h for t,h,c in es)))
sizes=list(map(len,options));assert sizes==[1,2,1,1,100,18,6,1,9,2,1,1,2,9,3,12,24,24,3,1,2,1]and math.prod(sizes)==870712934400
# Fresh outgoing physical-edge ordinal variables, in the declared order.
var={};meta=[];standard_times={}
for i,p in enumerate(points):
 for ho in range(4):
  counts=[sum((hi+(1 if j%2==0 else-1))%4==ho for j,hi in enumerate(hs))for hs in options[i]];assert len(set(counts))==1
  ranks=[j for j,(t,hi,c)in enumerate(H[p])if(hi+(1 if c=='R'else-1))%4==ho]
  for k in range(counts[0]):v=len(meta);var[i,ho,k]=v;meta.append([i,ho,k]);standard_times[v]=H[p][ranks[k]][0]
assert len(meta)==104
ALL=[];routing=[]
for i,p in enumerate(points):
 oo=[];routes=[]
 for hs in options[i]:
  ni=Counter();no=Counter();ins=[];outs=[];const=[];ee={}
  for rank,hi in enumerate(hs):
   ho=(hi+(1 if rank%2==0 else-1))%4;pred,shift=key(p-V[hi],dr);j=index[pred];iv=var[j,hi,ni[hi]];ni[hi]+=1;ov=var[i,ho,no[ho]];no[ho]+=1;ins.append(iv);outs.append(ov);const.append(1+shift*P)
  def add(u,v,w):ee[u,v]=max(ee.get((u,v),-10**9),w)
  for iv,ov,c in zip(ins,outs,const):add(iv,ov,c);add(ov,iv,-c)
  for j in range(1,len(hs)):add(ins[j-1],ins[j],4+const[j-1]-const[j])
  oo.append(ee);routes.append((ins,outs,const))
 ALL.append(oo);routing.append(routes)
for i,o in enumerate(known):assert all(standard_times[v]-standard_times[u]>=w for(u,v),w in ALL[i][o].items())
cert=json.loads((D/'standard_inventory_clock_tree.json').read_text());assert cert['complete']and cert['variables']==meta and cert['standard_options']==known
nodes={n['id']:n for n in cert['nodes']};assert len(nodes)==len(cert['nodes'])==9
# Independent verifier only reads explicit positive cycles; NO Bellman-Ford,
# SMT query, search timeout, or generator status is used to reject an option.
def common(dom):
 result={}
 for i,ds in enumerate(dom):
  assert ds;kk=set(ALL[i][ds[0]])
  for o in ds[1:]:kk&=set(ALL[i][o])
  for e in kk:result[e]=max(result.get(e,-10**9),min(ALL[i][o][e]for o in ds))
 return result
def verify_cycle(cc,available):
 assert cc and sum(w for u,v,w in cc)>0
 for z,(u,v,w)in enumerate(cc):assert v==cc[(z+1)%len(cc)][0]and(u,v)in available and available[u,v]>=w
seen=set();removed=0;leafs=[];badleaves=0

def verify_node(ident,initial):
 global removed,badleaves
 assert ident not in seen;seen.add(ident);node=nodes[ident];assert node['input_domains']==initial;dom=[list(d)for d in initial]
 for rnd in node['propagation']:
  base=common(dom);rr=set()
  for r in rnd['removed']:
   i,o=r['cell'],r['option'];assert o in dom[i]and len(dom[i])>1 and(i,o)not in rr;rr.add((i,o));combined=dict(base)
   for e,w in ALL[i][o].items():combined[e]=max(combined.get(e,-10**9),w)
   verify_cycle(r['cycle'],combined);removed+=1
  assert rr;dom=[[o for o in ds if(i,o)not in rr]for i,ds in enumerate(dom)]
 assert dom==node['after_domains']
 if node.get('leaf')=='infeasible':
  badleaves+=1
  if node['reason']=='empty_domain':assert any(not d for d in dom)
  else:verify_cycle(node['reason'],common(dom))
 elif node.get('leaf')=='feasible_complete':
  assert all(len(d)==1 for d in dom);v=[d[0]for d in dom];assert v==node['options']==known;leafs.append(v)
 else:
  i=node['branch_cell'];assert len(dom[i])>1;children=node['children'];assert sorted(z['option']for z in children)==sorted(dom[i])and len({z['option']for z in children})==len(dom[i])
  for ch in children:child=[list(d)for d in dom];child[i]=[ch['option']];verify_node(ch['node'],child)
verify_node(0,[list(range(n))for n in sizes]);assert seen==set(nodes)and removed==265 and badleaves==4 and leafs==[known]
# Literal one-cycle reconstruction of the sole ordering, including voltage sign.
G={};weights={}
for i,o in enumerate(known):
 ins,outs,cc=routing[i][o]
 for iv,ov,c in zip(ins,outs,cc):assert iv not in G;G[iv]=(ov,0);weights[iv]=c
assert len(G)==104 and len({v[0]for v in G.values()})==104;cycles=loops(G);assert len(cycles)==1 and len(cycles[0][0])==104 and sum(weights[v]for v in cycles[0][0])==0
# Sum(1+aP)=0 => sum a=-1; physical forward winding is+1.
assert sum((weights[v]-1)//P for v in G)==-1
# Replay the explicit feasible model, not its opaque SAT status.
model=json.loads((D/'standard_inventory_positive_model_certificate.json').read_text());events=model['events'];assert len(events)==104;word=''.join(e['turn']for e in events);assert word==model['word']==W[71:]+W[:71];B={cx(q)for q in model['seed']};assert len(B)==19;start=cx(model['position']);h0=model['heading'];assert(start,h0)==(-7j,3)
p=start;h=h0
for i,e in enumerate(events):
 assert e['phase']==i and cx(e['position'])==p and e['incoming_heading']==h;rep,k=key(p,dr);assert xy(rep)==tuple(e['class'])and e['clock']==i-P*k;rank=e['rank'];ii=index[rep];assert h==options[ii][known[ii]][rank]and e['turn']==('R'if rank%2==0 else'L');h=(h+(1 if e['turn']=='R'else-1))%4;p+=V[h]
assert(p,h)==(start+dr,h0)
seed=set(B);p=start;h=h0
for t,c in enumerate(word*3):assert(c=='L')==(p in B);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
# Exact allfuture color at every phase: changes only at affine earlier-read
# thresholds and the finite seed's isolated translated hits.
checks=0
for i,e in enumerate(events):
 q=cx(e['position']);threshold=[];tests={0}
 for j,f in enumerate(events):
  delta=cx(f['position'])-q;k=int(delta.real)//int(dr.real)
  if delta==k*dr and(k>0 or(k==0 and j<i)):threshold.append(k);tests.add(k)
 for b in seed:
  delta=b-q;k=int(delta.real)//int(dr.real)
  if delta==k*dr and k>=0:tests|={k,k+1}
 for n in tests:assert((q+n*dr in seed)^(sum(k<=n for k in threshold)%2))==(word[i]=='L');checks+=1
out={'status':'PASS full fixed-standard-inventory WHITE causal-order rigidity by independently verified finite clock certificate','author_note':sha(D/'STANDARD_FIXED_INVENTORY_RIGIDITY.md'),'tree':sha(D/'standard_inventory_clock_tree.json'),'source_inventory_classes':22,'events':104,'domain_sizes':sizes,'raw_option_product':math.prod(sizes),'verified_tree_nodes':9,'explicit_positive_cycle_option_deletions':265,'infeasible_leaves':4,'unique_complete_leaf_is_standard':True,'all_future_model_threshold_cases':checks,'positive_model':{'phase':71,'seed_mass':19,'position':[0,-7],'heading':3},'analytic_review':[
'WHITE firstness forces alternatingRLRL ranks in each COMPLETE physical-cell history. The preserved incoming-axis follows actual parity invariant; independently redistributing the fixed heading counts acrossR andL ranks exhausts all local orders. No visit cap beyond the supplied standard inventory, no primitive drift substitution, and no first-clock gauge removes a possibility.',
'Each directed physical edge has fixed crossing count. Its kth outgoing and kth incoming occurrences match in COMPLETE chronological order, with no cyclic rank offset. For incoming representative predecessor r+a*d, actual source time isX_in+aP and target read/departure timeX_out=X_in+1+aP. Both equality directions and consecutivephysicalreadgap>=4 are necessary; all seam signs were independently reconstructed.',
'For ANY complete option vector, local read pairing plus edgeordinal matching is a permutation of104 events. Summed exact clock equalities around a cycle giveell=-P*sum(a), so positiveell<=P impliesell=P and forward full-drift winding+1. Thus any feasible model has ONE physical event orbit. The selected history order inequalities prevent reordered visit ranks; the standard feasible option vector explicitly realizes the ordinary ant.',
'The verifier rebuilds every option inequality directly from the retained literal word. A common bound takes intersection of orderedpairs within each remaining cell domain and minimumweight, then strongest acrosscells. Every265 deletion has an explicit positive closedcycle whose edges are available common or tested-option implications. Allbranch options are covered, all9nodes reachable once, fourempty-domain leaves close, and the solecompleteleaf equalsstandard. No solver/timeout/generator UNSAT status is trusted.',
'The positive19-cell model is independently materialized at0,-7,W, phase71, with all104 eventpositions/headings/ranks/clocks checked, full3period replay and exact affine allfuture color-threshold test. Its full successor topology also directly confirms the winding sign and clock gauge interpretation.',
'Only period104, full drift(-2,2), these22 exact quotient classes and perclass(incomingheading,turn) counts are classified. Whole proper rotations/translations transport the theorem. Differentinventory, reflection, simultaneous changes ofcounts, otherperiod/drift and universalfinite-seed capture remain unclassified; unread debris is not removed.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
