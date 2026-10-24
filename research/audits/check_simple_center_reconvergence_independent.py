"""Fresh fine-step simulation and explicit all-parent incidence graph, not producer DSU."""
from pathlib import Path
SELF=Path(__file__).resolve();S=SELF.with_name('check_D_first_W5_gate_independent.py');exec(compile(S.read_text().split('rows=[];late=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/simple_center_reconvergence_frozen_20261023_1618';M=json.loads((B/'manifest.json').read_text())
for x in M['files']:assert hashlib.sha256((B/x['frozen']).read_bytes()).hexdigest()==x['sha256']
J=json.loads((B/'02_simple_center_reconvergence_control.json').read_text());word=[9,4,1,0,5,0,7];assert J['word']==word
raw=''.join(raws[a]for a in word);seed={q for q,c in walk(raw+mark)[2].items()if c};assert len(seed)==19 and set(map(xy,seed))==set(map(tuple,J['initial_actual_board']))
field=set(seed);p=0j;h=0;clock=0;tick=0;roots=sorted(seed-K,key=xy);tags={q:('root',i)for i,q in enumerate(roots)};adj={z:set()for z in tags.values()};birth={};producer={};history=[];arcs=[];clauses=[]
def edge(a,b):adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
def components():
 out=[];unseen=set(adj)
 while unseen:
  first=next(iter(unseen));seen={first};stack=[first]
  while stack:
   for j in adj[stack.pop()]:
    if j not in seen:seen.add(j);stack.append(j)
  unseen-=seen;out.append(seen)
 return out
for pi,src in enumerate(word):
 core={p+rotation(q,h)for q in K};assert field==core|set(tags)and not core&set(tags)
 assert all((p+rotation(q,h)in field)==c for q,c in G[src][2].items())
 cs=components();ins=[]
 for q in G[src][3]:
  cell=p+rotation(q,h);tag=tags.pop(cell);ins.append((cell,tag));edge(tag,('packet',pi))
  if tag[0]=='out':
   sj,si=tag[1:];sp,sh,ss=producer[sj];rel=rotation(p-sp,-sh);dh=(h-sh)%4;slot=G[ss][4];oq=rotation(cell-sp,-sh);age=clock-birth[tag];hb=(ss,src,*xy(rel),dh,*xy(oq));cq=(mp[ss],mp[src],*xy(rel),dh,*xy(oq),min(age,5));assert hb not in HB and cq not in C5;clauses.append((sj,pi,xy(cell),age,hb,cq))
 groups={next(i for i,c in enumerate(cs)if tag in c)for cell,tag in ins};inc=len(ins)-len(groups)
 producer[pi]=(p,h,src)
 for oi,q in enumerate(sorted(G[src][4],key=xy)):
  cell=p+rotation(q,h);assert cell not in tags;tag=('out',pi,oi);tags[cell]=tag;birth[tag]=clock;edge(('packet',pi),tag)
 for at,w in [('D'if base[src]==0 else'V'if base[src]==4 else'U',raws[base[src]])]+[('C',C)]*counts[src]:
  a=2*p+rotation(-1-1j,h)
  for c in w:assert(p in field)==(c=='L');field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h];tick+=1
  arcs.append((a,2*p+rotation(-1-1j,h)));clock+=at=='C'
 assert field==set(tags)|{p+rotation(q,h)for q in K}and not set(tags)&{p+rotation(q,h)for q in K}
 countc=len(components());edges=sum(map(len,adj.values()))//2;beta=edges-len(adj)+countc
 history.append(dict(packet=src,beta_increment=inc,beta=beta,components=countc,input_components=len(groups),inputs=[(xy(q),tag)for q,tag in ins]))
assert tick==182 and(p,h,clock)==(3+3j,0,4)and len(field)==47 and len(tags)==42 and len(roots)==14
assert history[-1]['beta']==1 and history[-1]['components']==5 and history[-1]['beta_increment']==1 and history[-1]['input_components']==4 and all(x['beta_increment']==0 for x in history[:-1])
assert {q for q,tag in ins if tag[0]=='out'and tag[1]==0}=={2+0j,2+1j}
assert len(clauses)==3 and sorted(x[3]for x in clauses)==[2,4,4]
nonadj=0
for j,(b0,b1)in enumerate(arcs):
 for i,(a0,a1)in enumerate(arcs[:j]):
  if j==i+1:
   assert a1==b0
   u=a1-a0;v=b1-b0
   assert det(u,v)!=0 or u.real*v.real+u.imag*v.imag>0
  else:assert not meet(a0,a1,b0,b1);nonadj+=1
assert len(arcs)==11 and nonadj==45
for c in mark:assert(p in field)==(c=='L');field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
out=dict(status='PASS actual19-cell simple-center beta-one control, independent physical and explicit graph replay',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),initial_black=19,entry_roots=14,word=word,raw_turns=182,raw_exit=[3,3,0],raw_final_black=47,residual_identities=42,C_count=4,incidence_vertices=len(adj),incidence_edges=sum(map(len,adj.values()))//2,incidence_components=5,beta=1,history=history,produced_queries=clauses,atomic_chords=11,exact_nonadjacent_disjoint_pairs=45,scope='Refutes center simplicity implying beta0. Final rank-producing U also merges four components; no claim against every mass-dependent or merge-paid rank bound, no renewal or infinite trajectory.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('history','produced_queries')})
