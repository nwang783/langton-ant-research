from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib,random
S=Path(__file__).resolve();R=S.parents[1];D=R/'K1_pipeline_detours_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'all_matched_rank12_ports_have_erasable_exchange_pairs.md';assert sha(note)=='79dcbbd4f25b23ab629b203993fe09fc4ee8f4bc141ec6abfccf76739a754076'
H='NESW';out=lambda a,k:(a[k]+(1 if k%2==0 else-1))%4;head=lambda a:''.join(H[v]for v in a);rows=[];flats=[];rotated=[]
for direction in range(4):
 ss=[a for n in range(1,5)for a in product(((direction-1)%4,(direction+1)%4),repeat=n)]
 tt=[a for n in range(1,5)for a in product((direction,(direction+2)%4),repeat=n)]
 local=[]
 for a in ss:
  pa=[k for k in range(len(a))if out(a,k)==direction]
  if not {1,2}<=set(pa):continue
  assert (a[1]-a[2])%4==2
  for b in tt:
   pb=[k for k in range(len(b))if b[k]==direction]
   if len(pa)!=len(pb):continue
   images=[pb[pa.index(k)]for k in (1,2)]
   if images!=[1,2]:continue
   assert b[1]==b[2]
   local.append((head(a),head(b),len(pa),pa,pb))
   if direction==2:rows.append(dict(source=head(a),target=head(b),flow=len(pa),source_ranks=pa,target_ranks=pb,target_of_source_rank12=images))
 assert len(local)==10 and Counter(z[2]for z in local)=={2:4,3:5,4:1};rotated.append(local)
 for b in tt:
  pb=[k for k in range(len(b))if b[k]==direction]
  if len(pb)!=2:continue
  repaired=[out(b,3-k if len(b)>=3 and k in (1,2)else k)for k in pb]
  if repaired==[(direction+1)%4,(direction-1)%4]and direction==2:flats.append(head(b))
a=json.loads((D/'matched_rank12_port_inventory.json').read_text());key=lambda x:(x['source'],x['target'])
assert sorted(rows,key=key)==sorted(a['matched'],key=key);assert sorted(flats)==sorted(x['headings']for x in a['unit_loop_target_profiles'])==sorted(['SS','NSS','SSN','NNSS','NSSN','SNNS','SSNN'])
# Exact unmatched two-unit-turn countercontrol, not an attained front.
a0=[H.index(c)for c in'WWEE'];b0=[H.index(c)for c in'SSNN'];pa=[k for k in range(4)if out(a0,k)==2];pb=[k for k in range(4)if b0[k]==2];assert pa==[1,2]and pb==[0,1]
# Simultaneous algebra controls with many pairs and arbitrary other repairs.
compose=lambda p,q:[p[q[i]]for i in range(len(p))]
def trans(n,ps):
 p=list(range(n));used=set()
 for x,y in ps:assert x not in used and y not in used;used|={x,y};p[x],p[y]=y,x
 return p
def cycles(p):
 seen=set();cs=[]
 for v in range(len(p)):
  if v in seen:continue
  c=[]
  while v not in seen:seen.add(v);c.append(v);v=p[v]
  cs.append(c)
 return cs
rng=random.Random(612);controls=0
for n in range(8,51):
 for rep in range(20):
  sigma=list(range(1,n))+[0];free=set(range(n));src=[]
  for _ in range(n):
   if len(free)<4:break
   x,y=rng.sample(sorted(free),2);four={x,y,sigma[x],sigma[y]}
   if len(four)==4 and four<=free:src.append((x,y));free-=four
  if not src:continue
  tgt=[(sigma[x],sigma[y])for x,y in src];rest=list(free);rng.shuffle(rest);extra=list(zip(rest[::2],rest[1::2]));sp,tp,up=trans(n,src),trans(n,tgt),trans(n,extra);partial=compose(compose(sp,tp),sigma);assert partial==compose(compose(sp,sigma),sp)and len(cycles(partial))==1
  full=compose(up,partial);cs=cycles(full);idx={v:i for i,c in enumerate(cs)for v in c};G=[set()for c in cs]
  for x,y in extra:G[idx[x]].add(idx[y]);G[idx[y]].add(idx[x])
  reached={0};todo=[0]
  for i in todo:
   for z in G[i]-reached:reached.add(z);todo.append(z)
  assert len(reached)==len(cs);beta=len(extra)-len(cs)+1;assert beta>=0 and beta%2==0;controls+=1
outp={'status':'PASS complete matched L1/R2 port inventory and simultaneous exchange-pair erasure','author_note':sha(note),'author_inventory':sha(D/'matched_rank12_port_inventory.json'),'prior_four_use_audit':sha(S.with_name('check_four_use_pair_erasure_independent.json')),'matched':rows,'rotations_checked':4,'unit_loop_targets':sorted(flats),'abstract_multi_pair_controls':controls,'analytic_review':[
'Every 1..4-read WHITE heading history on both physical axes is reconstructed without height or front realizability assumptions. Exact chronological port ordinals give10 matches, 4 flow2/5 flow3/1 flow4. Source rank1/2 headings opposite, target equal; a cell cannot be both roles or use multiple common ports. Full-drift checker parity forbids adjacent endpoint alias; distinct samephysicalcell ranks cannot alias with nonzero drift.',
'Actual physical successor sigma sends BOTH source L1/R2 to target L1/R2. Thus target swap is sigma source swap sigma^-1, all source/target supports disjoint. Simultaneous product ST sigma=S sigma S remains a singlePcycle. Remaining repair swaps are disjoint. Any proper component union in the graph after pair deletion would be invariant under fullcanonical routing and remaining swaps, hence under that singlecycle. Contradiction. Nodes unchanged, beta-2Q>=0 and permutation parity makes it even.',
'Full repair sends sourceL1 to targetR2 and sourceR2 to targetL1, showing two parallel exchange edges. Their nodes lie on distinct adjacent sheets; short quotient does not merge sheet heights. Exact source/target Delta equal, opposite clock contributions cancel on each node as well as across cuts.',
'For proper length0<ell<P, residual signed clock Pw=ell+positiveR2- negativeL1 requires at leastone negative incidence whenw<=0, at leastone positiveR2 whenw>=1. TOP C loop negativeL1 has opposite incomingrank1/2 headings, hence common outgoing source port. BOTTOM L loop negativeL1 has equal incomingrank1/2 headings, hence common incoming target port. At leastone must remain unmatched. This is not a unique defect or fuel payment.',
'An unmatched common source cannot map both ranks to target1/2 because ordinal order would make it matched; at leastone image is0/3. Dual target statement likewise. This conditional commonport statement does not identify arbitrary face patch geometry with a matched pair.',
'WWEE sourceS ranks1/2 to SSNN targetS ranks0/1 retains both repairedunitturns but is unmatched; all7 permitted two-S unit-turn targethistories checked. No local profile or abstractpermutation control is promoted to a physical completefront. No beta upperbound, highercap extension or legalantsplice.' ]}
S.with_suffix('.json').write_text(json.dumps(outp,indent=2)+'\n');print(outp['status'],controls)
