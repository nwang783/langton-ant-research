from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
f=D/'incoming_one_use_run_at_even_portal_cannot_end_RIGHT.md';assert sha(f).startswith('3247f7df')
dep=R/'audits/check_short_balanced_portal_joins_independent.json';assert sha(dep)=='3c549e850e12c02366dd28c3f6126a2e0129ad72f5a3591516075918aa4fa83a'
H='NESW';V=[(0,1),(1,0),(0,-1),(-1,0)]
def out(w,r):return(H.index(w[r])+(1 if r%2==0 else-1))%4
def graph(hs):
 g={};bad=[]
 for p,w in hs.items():
  for d,v in enumerate(V):
   q=p[0]+v[0],p[1]+v[1]
   if q not in hs:continue
   ss=[r for r in range(len(w))if out(w,r)==d];tt=[r for r,c in enumerate(hs[q])if H.index(c)==d]
   if len(ss)!=len(tt):bad.append([p,q,H[d],ss,tt])
   else:g.update({(p,r):(q,s)for r,s in zip(ss,tt)})
 return g,bad
rows=[]
for y,l in product(['EWW','EWWE'],['NNS','NNSN']):
 hs={(1,-1):l,(2,-1):'E',(2,-2):'SN',(1,-2):y,(1,-3):'NNSS',(2,-3):'EE'};g,bad=graph(hs)
 if bad:rows.append(dict(root=y,left=l,port_failures=bad));continue
 assert y=='EWWE'and l=='NNS'
 path=[((1,-1),0),((2,-1),0),((2,-2),0),((1,-2),1),((1,-3),3),((2,-3),1),((2,-2),1),((1,-2),2),((1,-1),0)]
 assert all(g[a]==b for a,b in zip(path,path[1:]));rows.append(dict(root=y,left=l,same_physical_event_cycle=path))
assert sum('port_failures'in z for z in rows)==3
# Independent local alternative to the general RRR no-essential-cycle rule:
# If l were RIGHT, its incoming selected edge is Y->l, but b(Y) pointsS.
for y in ['EWW','EWWE']:
 assert out(y,0)==2
outobj=dict(status='PASS localized all-length incoming-run endpoint consequence',proof_sha256=sha(f),dependency_sha256=sha(dep),six_cell_kernel=rows,analytic_review=[
'The statement retains an actual essential complete-WHITE cap-four b-circle and exactly the displayed even portal histories. The internal predecessor r has incoming/outgoing cycle flow1, so the count-derived RIGHT history is singletonE. Its predecessor must exist on the actual b-circle.',
'If predecessor l were RIGHT, l,r,B form three consecutive RIGHT turns and close a physical unit square, impossible for the essential circle. In this exact frame there is an even more local b-incidence check: l would require Y as its selected incoming predecessor, whereas both actual Y histories have first-R departureS, away from l. This is b-edge ownership, not a chronological matching assumption.',
'Thus l is LEFT. A multiplicity-changing start of the flow-one segment is RIGHT in the signed cap-four boundary domain, so l cannot be such a start; it retains flow1. Its complete firstN/selectedSin1/Eout1 domain is exactly NNS/NNSN, as independently derived in signed3c549e85.',
'The contradiction uses only these six physical cells. Three of four root/l products fail internal port counts; the fourth has the literal8-step SAME event cycle. No upper portal or bounded length is used. Therefore every nonempty internal incoming flow1 run at this exact portal ends LEFT.',
'Zero-internal transitions, a changed source/root history, other multiplicity transitions and longer LEFT-ending runs remain open. No odd-output payment, length bound, full-front classification or global capture follows.'
])
S.with_suffix('.json').write_text(json.dumps(outobj,indent=2)+'\n');print(sha(S.with_suffix('.json')))
