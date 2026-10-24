from pathlib import Path
from itertools import product
from collections import Counter,defaultdict,deque
import json,hashlib
S=Path(__file__);R=S.parent.parent;P=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();bind={f:sha(P/f)for f in('global_max_flow2_staircase_segments_have_one_core_and_cannot_close.md','flat_flow2_symbolic_row_with_odd_left.py','flat_flow2_symbolic_row_with_odd_left.json')};assert bind['global_max_flow2_staircase_segments_have_one_core_and_cannot_close.md']=='e597889e756ec21b6f4c6db01de2ea8e56d2e85fdb6851439673db39c7eb1b21';ref=json.loads((P/'flat_flow2_symbolic_row_with_odd_left.json').read_text())
H='NESW';V=(1j,1,-1j,-1);out=lambda w,j:(w[j]+(1 if j%2==0 else-1))%4;string=lambda w:''.join(H[h]for h in w);cv=lambda w:tuple(H.index(c)for c in w);A={'X':cv('NNSS'),'Y':cv('NSSN')};B={'O':cv('WEE'),'U':cv('WEEW'),'V':cv('WWEE')};allw=lambda a:[w for n in range(5)for w in product(a,repeat=n)];NS=allw((0,2));EW=allw((1,3));cin=lambda w,h:w.count(h);cout=lambda w,h:sum(out(w,j)==h for j in range(len(w)))
def test(hs):
 ev=[(p,j)for p,w in hs.items()for j in range(len(w))];su={};edges=[]
 for p,w in hs.items():
  for j in range(len(w)-1):edges.append(((p,j),(p,j+1),4))
  for h,v in enumerate(V):
   q=p+v
   if q not in hs:continue
   sr=[j for j in range(len(w))if out(w,j)==h];tr=[j for j,x in enumerate(hs[q])if x==h]
   if len(sr)!=len(tr):return'port',None
   for i,j in zip(sr,tr):su[p,i]=(q,j);edges.extend([((p,i),(q,j),1),((q,j),(p,i),-1)])
 # Literal continuous paths, not elapsed-time lower bounds.
 for e in ev:
  u=e;seen={e};seq=[e]
  while u in su:
   u=su[u];seq.append(u)
   if u[0]==e[0]:
    if u[1]!=e[1]+1:return'skipped',seq
    break
   if u in seen:return'event_cycle',seq
   seen.add(u)
 # Max-plus necessary clocks with explicit positive-cycle extraction.
 dist={u:0 for u in ev};prev={};changed=None
 for _ in ev:
  changed=None
  for u,v,k in edges:
   if dist[v]<dist[u]+k:dist[v]=dist[u]+k;prev[v]=(u,v,k);changed=v
  if changed is None:break
 if changed is not None:
  at=changed
  for _ in ev:at=prev[at][0]
  start=at;cy=[]
  while True:
   e=prev[at];cy.append(e);at=e[0]
   if at==start:break
  assert sum(e[2]for e in cy)>0 and all(e in edges for e in cy);return'clock',cy
 # Independent local stream equations with BOTH directions on every radial edge, even zero ports.
 adj=defaultdict(list)
 for p,w in hs.items():
  for h,v in enumerate(V):
   right=p+v/2-1j*v/2;left=p+v/2+1j*v/2;net=cout(w,h)-cin(w,(h+2)%4);adj[left].append((right,net));adj[right].append((left,-net))
 vals={.5-.5j:0};q=deque(vals)
 while q:
  p=q.popleft()
  for r,k in adj[p]:
   if r in vals:
    if vals[r]!=vals[p]+k:return'height_cycle',None
   else:vals[r]=vals[p]+k;q.append(r)
 assert set(vals)==set(adj)
 for p,z in vals.items():
  faceindex=int(p.real-.5)+int(p.imag-.5)
  if faceindex%2 and z>0:return'global_max',[(int(2*p.real),int(2*p.imag)),z]
 return'open',None
rows=[];stats=Counter();n=0;opened={};explicit_clock_cycles=0
for key in product('OUV','XY','OUV','XY','OUV'):
 bp,a,b,an,bn=key;base={-1j:B[bp],0j:A[a],1:B[b],1+1j:A[an],2+1j:B[bn]}
 d0=[w for w in NS if cin(w,2)==cout(B[b],2)and cout(w,3)==cin(B[bp],3)];d1=[w for w in NS if cin(w,2)==cout(B[bn],2)and cout(w,3)==cin(B[b],3)];good=[];local=Counter()
 for u,v in product(d0,d1):
  ee=[w for w in EW if cin(w,1)==cout(u,1)and cout(w,0)==cin(v,0)]
  for e in ee:
   n+=1;ans,wit=test(base|{1-1j:u,2:v,2-1j:e});local[ans]+=1
   if ans=='clock':explicit_clock_cycles+=1
   if ans=='open':good.append({'D0':string(u),'D1':string(v),'E':string(e)})
 z=next(r for r in ref['rows']if tuple(r[k]for k in('Bprev','A','B','Anext','Bnext'))==key);assert good==z['open_completions'];mapped={'port':'port','skipped':'skipped_rank','event_cycle':'event_cycle','clock':'clock_cycle','height_cycle':'height_cycle','global_max':'global_C_max','open':'open'};assert {mapped[k]:v for k,v in local.items()}==z['rejections'];stats.update(local)
 if good:opened[key]=good
 rows.append({'word':key,'counts':dict(local),'open':good})
assert n==5700 and len(opened)==8
expected={('U','X','O','X','V'),('U','X','O','Y','V'),('U','X','U','X','O'),('U','X','U','X','U'),('V','Y','O','X','V'),('V','Y','O','Y','V'),('V','Y','U','X','O'),('V','Y','U','X','U')};assert set(opened)==expected
assert all(k[0]in'UV'and k[2]in'OU'for k in opened)and all(k[1]=='X'for k in opened if k[0]=='U')
# Core opposite-cell full history and physical two-step rank transfer, with no guessed D mode.
candidates=[w for w in NS if cin(w,2)==cout(w,3)==2];assert set(map(string,candidates))=={'NNSS','NSSN','SNNS','SSNN'};prior=[w for w in candidates if min(j for j in range(len(w))if out(w,j)==3)<w.index(2)];assert list(map(string,prior))==['NNSS']
core={0j:A['X'],1:B['U'],-1j:B['U'],1-1j:prior[0]};q=1;rank=2
for want in[(1-1j,2),(-1j,3)]:
 h=out(core[q],rank);dest=q+V[h];outs=[j for j in range(len(core[q]))if out(core[q],j)==h];ins=[j for j,x in enumerate(core[dest])if x==h];rank2=ins[outs.index(rank)];assert(dest,rank2)==want;q,rank=dest,rank2
outreport={'status':'PASS global-max constant-flow2 staircase all-length core and closed-cycle exclusion','bindings':bind,'primary_words':108,'completions':n,'rejections':dict(stats),'independently_extracted_positive_clock_cycles':explicit_clock_cycles,'open_words':rows,'core_D':list(map(string,prior)),'analytic_review':[
'All two RIGHT and three LEFT flow2 modes, including odd WEE, are signed complete alphabets only on constant-selected-C first-R cycle segments. The fixed8-physical-cell stencil independently includes every complete WHITE0..4 exterior history allowed by mandatory ports, all zero uses and all physical outgoing/incoming ordinals. Treating possible short full-quotient aliases as independent physical lifts relaxes conditions, so cannot lose an actual completion.',
'Every5700 completion is reconstructed. Literal forced first returns reject skipped physical ranks; max-plus rejection independently extracts a genuinely positive inequality cycle; all dual-face equations are independently solved from net radial flow including unused ports. The selected SE face of A is M=0, and every C face in the stencil is required<=0. This GLOBAL maximum premise is essential and is not merely local maximum.',
'Exactly eight primary words survive as necessary OPEN rows. In overlapping windows, a B appearing as both current and previous lies in {O,U} intersect {U,V}={U}; with previous U, A=X. Hence closed full-quotient staircase words are entirely NNSS/WEEW, with finite segment caps explicitly retained. No bounded period or length search is used.',
'For that full core, first-W departure at D occurs A.R0-2, while first-S arrival is B.R2+1>A.R0+2. The complete S2/W2 inventory therefore forces D=NNSS. Its literal second ports give B_k.R2 -> D_k.R2 -> B_(k-1).L3. Thus T3(B_(k-1))=T2(B_k)+2<=T3(B_k)-2.',
'Actual first-R b-cycle winding is-1. Geometric NE staircase length2a gives actual full d=(-a,-a), so B_(k-a)=B_k+d has T3 increased byP. Iterating verified core transfer a times instead decreases by>=2a. This closes the true full quotient even for short aliasing; no bare spatial infinite descent.',
'Only closed constant-flow2 DIAGONAL STAIRCASE cycles at GLOBAL M are excluded. Finite core length can be absorbed by endpoint age, nonstaircase turns or multiplicity changes. No general one-use edge/all-one-use, front exclusion or fuel bound follows.'
]};S.with_suffix('.json').write_text(json.dumps(outreport,indent=2)+'\n');print(outreport['status'],stats);print(sha(S),sha(S.with_suffix('.json')))
