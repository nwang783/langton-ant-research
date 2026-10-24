from pathlib import Path
from collections import Counter
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'kernel_cycle_lift_2026-10-24';p=SELF.with_name('check_cycle_birth_finite_fuel_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
ends,component,step,wvertex=[ns[k]for k in('ends','component','step','wvertex')]
def xy(z):return(int(z.real),int(z.imag))
def verts(B):return{v for q in B for v in ends(q,0)}
A=json.loads((D/'cap7_word_pairs_certificate.json').read_text());words=A['words'];assert len(words)==23;prev=json.loads(SELF.with_name('check_cap7_word_mandatory_filters_independent.json').read_text());assert set(words)=={z['word']for z in prev['23_finite_positive_controls']}
refs={tuple(z['words']):z for z in A['all_529_pairs']};rows=[];ct=Counter();edges=[];tail=[];paid=None
for aa,bb in product(words,repeat=2):
 word=aa+bb;seams={0,len(aa),len(word)};p=0j;h=0;last={};seed=set();failure=None
 for t,c in enumerate(word):
  if p in last and last[p][1]==c:failure={'status':'NO_WORD_COLOR','cell':xy(p),'first':last[p],'next':(t,c)};break
  if p not in last and c=='L':seed.add(p)
  last[p]=(t,c);h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
 if failure is None:
  B=set(seed);p=0j;h=0;birth={q:None for q in B};trace=[];ev=[];maximum=0
  for t in range(len(word)+1):
   C=component(B,0,wvertex(p,h))[1];maximum=max(maximum,len(C));trace.append((t,xy(p),h,sorted(map(xy,B)),sorted(map(xy,C))))
   if len(C)>7:failure={'status':'NO_CAP7','cut':t,'component':sorted(map(xy,C))};break
   if t in seams and C:failure={'status':'NO_EMPTY_SEAM','cut':t,'component':sorted(map(xy,C))};break
   if t not in seams:assert C
   if t==len(word):break
   if word[t]=='R':
    u,v=ends(p,0);w=wvertex(p,h);other=v if u==w else u;imp=component(B,0,other)[1]if other not in verts(C)|{w}else set()
    if imp:ev.append(('import',t,sorted((xy(q),birth[q])for q in imp)))
    birth[p]=t
   else:ev.append(('consume',t,xy(p),birth.pop(p)))
   p,h,ch=step(B,p,h);assert ch==word[t]
  if failure is None:
   w=wvertex(p,h);U=set()
   for dx,dy in product([-2,2],repeat=2):U|=component(B,0,w+dx+dy*1j)[1]
   u,v=ends(p,0);other=v if u==w else u;trapped=len(U)>3 or(len(U)==3 and other not in verts(U))
   i,j=words.index(aa),words.index(bb);edges.append((i,j))
   if not trapped:tail.append((i,j))
   row={'words':[aa,bb],'status':'ACTUAL_WORD_SEQUENCE','seed':sorted(map(xy,seed)),'final':sorted(map(xy,B)),'pose':[xy(p),h],'maximum':maximum,'future_trapped':trapped,'neighbor_union':sorted(map(xy,U)),'trace':trace,'lifetimes':ev}
   ref=refs[aa,bb];assert len(trace)==len(ref['trace'])
   for z,a in zip(trace,ref['trace']):assert(z[0],z[1],z[2],z[3],z[4])==(a['cut'],tuple(a['pose'][0]),a['pose'][1],list(map(tuple,a['full_black'])),list(map(tuple,a['active_w'])))
   assert trapped==ref['future_budget_trap']['trapped']
   if(aa,bb)==('RRRRLRLRL','RRRRLLLLRLRL'):paid=row
 if failure is not None:row={'words':[aa,bb],**failure}
 assert row['status']==refs[aa,bb]['status'];ct[row['status']]+=1;rows.append(row)
assert ct=={'ACTUAL_WORD_SEQUENCE':78,'NO_WORD_COLOR':220,'NO_EMPTY_SEAM':20,'NO_CAP7':211};assert set(edges)==set(map(tuple,A['existence_edges']))and set(tail)==set(map(tuple,A['future_untrapped_edges']))and len(tail)==51
# Small exact reachability closure computes SCCs independently of author DFS.
def cyclic(E):
 reach=[{i}for i in range(23)]
 for a,b in E:reach[a].add(b)
 for k in range(23):
  for a in range(23):
   if k in reach[a]:reach[a]|=reach[k]
 seen=set();out=[]
 for a in range(23):
  if a in seen:continue
  C={b for b in range(23)if b in reach[a]and a in reach[b]};seen|=C
  if len(C)>1 or(a,a)in E:out.append(sorted(C))
 return sorted(out)
assert cyclic(edges)==sorted(A['existence_recurrent_sccs'])and cyclic(tail)==sorted(A['future_untrapped_recurrent_sccs'])
tails=[{words[i]for i in C}for C in cyclic(tail)];assert{frozenset(x)for x in tails}=={frozenset(['RRRRLRLRL','RRRRLLLLRLRL']),frozenset(['RRRRLLLLRL'])}
assert paid['seed']==[(-4,4),(-3,1),(-2,2),(-1,1)]
assert('import',9,[((-3,1),None),((-2,1),7)])in paid['lifetimes']
assert('consume',14,(-3,1),None)in paid['lifetimes']and('consume',15,(-2,1),7)in paid['lifetimes']and('consume',20,(-4,4),None)in paid['lifetimes']
# All-copy freshness of the singleton recurrent U word is a finite invariant-direction check.
p=0j;h=0;U='RRRRLLLLRL';ph=[]
for i,c in enumerate(U):ph.append((i,xy(p),c));h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
assert(p,h)==(1+1j,0)and[z for z in ph if z[1][0]-z[1][1]==-1]==[(5,(-1,0),'L')]
files=['CAP7_EXACT_WORD_PAIR_GRAPH.md','check_cap7_word_pairs.py','cap7_word_pairs_certificate.json'];hashes={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files};assert hashes[files[0]]=='836e984698760903c260e6495a9492806656f6d7a5b299e52f5124c1f5504fcc'
out={'status':'PASS exact529 cap7 word pairs and finite-support eventual binary S/T necessity; NOT cap7 exit','source_hashes':hashes,'counts':dict(ct),'all529_pairs':rows,'existence_edges':edges,'future_untrapped_edges':tail,'existence_sccs':[[words[i]for i in C]for C in cyclic(edges)],'tail_sccs':[[words[i]for i in C]for C in cyclic(tail)],'singleton_U_all_phase_geometry':ph,'analytic_review':[
'The fixed-word minimum-board theorem is exact for color, cap and empty seams. At any cut every other realizing complete board adds only cells unread by the WHOLE pair, and thus cannot shrink an active component or repair a nonempty endpoint. Individual23 minimal first returns separately guarantee every interior nonempty cut, even in the second word via its local minimum-field inclusion. Consequently the criterion is sufficient AND necessary for WORD pair existence, not prescribed-profile composition.',
'All529 pairs are independently integrated at their actual continued poses and fixed w lattice. All78 complete finite-field positive traces match cut-by-cut, with initial seeds at most5 cells. The220/20/211 negative partition is exact. No initial bits are reset at the seam.',
'The27 future-trapped positives remain actual finite executions. Their mandatory final subsets trigger only the separately signed subsequent import-budget exit within9 updates. Removing them gives51 necessary edges for a sustained tail, not51 positive infinite transitions. Exact SCCs leave the complete binary S/T graph and the singleton U self-loop.',
'U restores heading and translates(1,1). Its unique read phase on x-y=-1 is phase5L at(-1,0). All translates of this cell are distinct and no other U read phase can reach them, so each U copy spends a different black cell already present at the START OF THAT RUN. This excludes an infinite U-only tail from finite support, without claiming those are original time-zero seed identities.',
'Finite-support cap7 nonempty excursions reach empty by the signed rank and bounded core. A hypothetical sustained cap7 orbit therefore has infinitely many first returns. Finite-graph condensation eventually confines its words to one recurrent SCC; U-only is impossible, so the eventual words must belong to S/T. Arbitrary nonperiodic binary mixtures and their full-field resources are NOT resolved.',
'The S-to-T paid transport is genuinely replayed on its complete4-cell board: output toothR7 is imported with prefunded connector at9 and consumed15; connector consumed14 and another prefunded input20. This is not full-input regeneration and does not contradict fixed-profile noncomposition.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(dict(ct))
