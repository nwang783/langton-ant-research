from pathlib import Path
from itertools import combinations
import hashlib,json
Sfile=Path(__file__).resolve();R=Sfile.parents[1];D=R/'K1_pipeline_detours_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'four_use_pair_erasure_preserves_cycle_connectivity.md';assert sha(note)=='7d357e694664155236e6aabc53328c46cfea7ab605dde27f1ca66351cfc7bd9e'
compose=lambda p,q:[p[q[i]]for i in range(len(p))]
def trans(n,pairs):
 a=list(range(n))
 for x,y in pairs:assert a[x]==x and a[y]==y;a[x],a[y]=y,x
 return a
def cycles(p):
 seen=set();out=[]
 for v in range(len(p)):
  if v in seen:continue
  c=[];u=v
  while u not in seen:seen.add(u);c.append(u);u=p[u]
  out.append(c)
 return out
# Literal four-use port law and its prohibition of both types at one cell.
ports=[]
for dr in range(4):
 source=[(dr-(1 if c=='R'else-1))%4 for c in'RLRL'];target=[dr]*4
 outs=[(h+(1 if c=='R'else-1))%4 for h,c in zip(source,'RLRL')];tout=[(h+(1 if c=='R'else-1))%4 for h,c in zip(target,'RLRL')]
 assert outs==target and len(set(source))==2 and len(set(tout))==2;ports.append((source,target,tout))
# Many small ABSTRACT occurrence permutations sanity-check graph reconstruction.
# The theorem itself is the all-size conjugacy proof, not this finite family.
controls=0
for n in range(4,13):
 sigma=[(i+1)%n for i in range(n)]
 for a,b in combinations(range(n),2):
  targets=(sigma[a],sigma[b]);used={a,b,*targets}
  if len(used)!=4:continue
  rest=[i for i in range(n)if i not in used]
  for extra in [[],list(zip(rest[::2],rest[1::2]))]:
   ss=trans(n,[(a,b)]);tt=trans(n,[targets]);U=trans(n,extra);sigF=compose(compose(ss,tt),sigma);assert sigF==compose(compose(ss,sigma),ss)and len(cycles(sigF))==1
   sig0=compose(U,sigF);cs=cycles(sig0);index={v:i for i,c in enumerate(cs)for v in c};G=[set()for _ in cs]
   for x,y in extra:G[index[x]].add(index[y]);G[index[y]].add(index[x])
   reachable={0};todo=[0]
   while todo:
    i=todo.pop()
    for j in G[i]-reachable:reachable.add(j);todo.append(j)
   assert len(reachable)==len(cs);beta=len(extra)-len(cs)+1;assert beta>=0 and beta%2==0;controls+=1
# Reconstruct author two-interleaved-pair control, no physical interpretation.
a=json.loads((D/'four_use_pair_erasure_preserves_cycle_connectivity.json').read_text());n=len(a['sigma']);sig=a['sigma'];src=[tuple(x)for x in a['source_pairs']];tgt=[(sig[x],sig[y])for x,y in src];ss=trans(n,src);tt=trans(n,tgt);assert compose(compose(ss,tt),sig)==compose(compose(ss,sig),ss)==a['partially_repaired'];assert len(cycles(a['partially_repaired']))==1
bindings={p:sha(Sfile.with_name(p+'.json'))for p in ['check_nonleaf_max_RIGHT_tradeoff_independent','check_deep_rootfree_valley_ladder_independent','check_simultaneous_scalar_canonical_embedding_independent']}
out={'status':'PASS all-four-use-pair erasure preserves canonical graph connectivity and beta>=2F4','author_note':sha(note),'dependency_reports':bindings,'literal_rotated_ports':ports,'small_abstract_graph_controls':controls,'analytic_review':[
'Cap4 and a physical port used FOUR times force all source departures and all target arrivals on that port. Complete WHITE histories are RLRL. Source has alternating opposite incoming headings, target one fixed incoming heading; neither cell can simultaneously have a four-use incoming AND outgoing port. Each source/target thus belongs to only one F4 edge class.',
'Actual ordinal matching gives targetrankr exactly one physical update after sourcerankr. In outgoing occurrence labels, target L1/R2 is the exact sigma-image of source L1/R2, so t=sigma*s*sigma^-1. The four occurrence classes are distinct: actual full drift preserves checker parity so opposite-neighbor cells cannot alias; same-cell different ranks cannot differ by a full period with zero displacement and nonzero drift.',
'Different F4 edges have disjoint source/target cell classes and hence disjoint transposition supports, including in short full-drift quotients. Their source productS is an involution, target productT=sigma*S*sigma^-1, and allF4 repairs ST*sigma=S*sigma*S, a one-cycle conjugate. Temporal interval interleaving is irrelevant.',
'All other local repair transpositionsU are disjoint from those supports. Fullcanonical sigma0=U*sigmaF4. A union of components of G_minus is invariant under sigma0 and eachU transposition because every remaining edge has both endpoints there; thus invariant under sigmaF4=U*sigma0. One-cycle transitivity forbids a nonempty proper union. This proof also allows graph loops and multiple edges.',
'With unchanged canonical nodesV and remaining edgesE-2F4, connectivity gives beta_minus=beta-2F4>=0. Permutation sign (-1)^(P-V)=(-1)^(E-2F4)*(-1)^(P-1) makes beta_minus even. This is a stronger lower bound, not an upper bound.',
'The alternative clock proof uses exact equal Delta at the source and target with opposite exchange signs. These cancel across every node-union cut, leaving a putative proper component length=P*integer winding, impossible strictly between0 andP. No Delta reduction moduloP and no extra additive charge.',
'Any two essential nodes still have a path using NON-F4 exchanges after all such pairs are removed. The direct deep ladder needs such an alternate assembly route, but its possible face patches, ordinary essential contacts or odd-root exceptional nodes are not excluded. This is graph/permutation manipulation only, not a legal ant splice or controller.']}
Sfile.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],controls)
