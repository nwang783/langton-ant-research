from pathlib import Path
from itertools import product
from collections import Counter,deque
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'high_macro_junctions_force_a_triangular_run_normal_form.md';J=json.loads((D/'check_high_macro_junctions.json').read_text());ns={'__file__':str(S.with_name('check_two_flat_pair_gate_independent.py'))};exec(Path(ns['__file__']).read_text().split('summary=Counter();row_results=')[0],ns);audit,words,ports,xy,H,dv=[ns[k]for k in('audit','words','ports','xy','H','dv')]
rot=lambda w,n:''.join(H[(H.index(c)+n)%4]for c in w);specs={'RR3':[('R','EWE'),('R','EEE')],'RLR3':[('R','EWE'),('L','WEEE'),('R','EEE')],'RR4':[('R','EWEW'),('R','EEEE')]}
def build(a,b,s):
 p=1j;ci=1;nodes=[]
 for t,w in specs[a]+[('L','WWEE')]*s+specs[b]:
  w=rot(w,ci-1);co=(ci+(1 if t=='R'else-1))%4;nodes.append(dict(cell=xy(p),turn=t,history=w,ci=H[ci],co=H[co]));p+=dv[co];ci=co
 return nodes

def enumerate_patch(nodes):
 fixed={complex(*n['cell']):n['history']for n in nodes}
 if len(fixed)<len(nodes):return None,None,None
 pts=set(fixed)
 while True:
  add={q for p in pts for v in dv if(q:=p+v)not in pts and sum(q+vv in pts for vv in dv)>=2}
  if not add:break
  pts|=add
 pts=sorted(pts,key=lambda p:(p.real,p.imag));adj={p:[(p+v,k)for k,v in enumerate(dv)if p+v in pts]for p in pts};ds={p:[fixed[p]]if p in fixed else words[int(p.real+p.imag)%2][:]for p in pts};counts=Counter();good=[]
 def search(ds):
  queue=deque(ds)
  while queue:
   p=queue.popleft()
   for q,k in adj[p]:
    allowed={ports(w,p,k)for w in ds[p]};keep=[w for w in ds[q]if ports(w,q,(k+2)%4)in allowed]
    if not keep:return
    if len(keep)<len(ds[q]):ds[q]=keep;queue.append(q)
  undec=[p for p in pts if len(ds[p])>1]
  if undec:
   p=min(undec,key=lambda p:len(ds[p]))
   for w in ds[p]:search(ds|{p:[w]})
  else:
   hs={p:w[0]for p,w in ds.items()};ans=audit(hs);counts[ans]+=1
   if ans=='open':good.append({str((int(p.real),int(p.imag))):w for p,w in hs.items()})
 search(ds);return pts,counts,good
refs={(r['A'],r['B'],r['separator']):r for r in J['rows']};summary=Counter();report=[]
for a,b,s in product(specs,specs,(1,2)):
 ref=refs[a,b,s];nodes=build(a,b,s);assert nodes==ref['nodes'];pts,counts,good=enumerate_patch(nodes);assert pts is not None and list(map(xy,pts))==ref['corner_closure'];assert counts==ref['counts'];assert {json.dumps(z,sort_keys=True)for z in good}=={json.dumps(z,sort_keys=True)for z in ref['open']};summary.update(counts);report.append(dict(A=a,B=b,separator=s,counts=dict(counts)))
assert summary==J['summary']=={'skipped_rank':3556,'clock_cycle':232,'open':28};assert len(refs)==18
# Zero-LEFT separators: adjacent high endpoints are also independently checked.
zero=[]
for a,b in product(specs,repeat=2):
 nodes=build(a,b,0);pts,counts,good=enumerate_patch(nodes);assert not good;zero.append(dict(A=a,B=b,coincident_primary=pts is None,counts=None if counts is None else dict(counts)))
# Exact RR,VV geometry has net zero heading and advances two first-outgoing units.
for macro in('RR3','RR4'):
 nodes=build(macro,'RR3',2);start=complex(*nodes[0]['cell']);nxt=complex(*nodes[len(specs[macro])+2]['cell']);assert nodes[0]['ci']==nodes[len(specs[macro])+2]['ci']and nxt-start==2*dv[H.index(nodes[0]['co'])]
out=dict(status='PASS local high-junction cover and qualified critical global-M run normal form',proof=sha(P),certificate=sha(D/'check_high_macro_junctions.json'),script=sha(S),summary=dict(summary),rows=report,zero_separator_control=zero,analytic_review=['All18 physical source/macro/V-or-VV/macro stencils and finite count-closures are independently regenerated. Empty and every WHITE1..4 history on each true incoming axis are retained; exact port counts, literal ordinal return constraints and max-plus clocks alone reproduce all3816 complete patches. No height or critical-side filter is used.','All one-V and all joins targeting RLR3 fail. Exactly28 open VV joins target RR3 orRR4; these remain necessary exterior-port patches, not attained factors or assigned full clocks.','The separate global corollary retains complete WHITE cap4, actual essential b-circle at critical GLOBALM, no one-use edges, and the signed exhaustive high macro inventory. Three consecutive LEFT turns close a physical unit square. Zero-LEFT joins are ruled out by the general RR neighborhood restriction; allnine such adjacent macro controls are also rebuilt and have no open completion.','O/U cannot be the first separator contact because a flow2 crossing needs an immediately preceding flatRIGHT, not a high sink; it cannot be second by the signed critical last-LEFT gate. Thus every interior separator isV orVV, and the local cover makes itVV. At most the first macro of each flat-ended run isRLR3, with arbitrary RR3/RR4 rails thereafter.','The physical RR,VV step restores incoming heading and advances two units in the first outgoing direction. Neither this spatial monotonicity nor the finite triangular run language bounds rail length, full drift voltage, actual clock span, old stock or number of flats; no global exclusion or fuel follows.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
