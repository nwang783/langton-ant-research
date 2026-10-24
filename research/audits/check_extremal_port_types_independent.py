from pathlib import Path
from collections import Counter
import hashlib,json,random
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'EXTREMAL_PORT_TYPE_REFINEMENT.md')=='fdde77939e853ddeeba708e300a44b668224f3c80ea0fbbdc7979869801f0eef'
assert sha(D/'check_extremal_port_types.py')=='c1d682528abab01a98db5531986701e15c5dff4cd03d51f823b7780e3db25af3'
assert sha(D/'check_extremal_port_types.json')=='1bf39769ba9945a93a155b09ce64aed88bb92eb5e693c0e2cbd4348a217aa87e'
p=S.with_name('check_all_cap_extremal_read_coupling_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('std=json.loads')[0],ns);trace,key,loops,V=[ns[k]for k in ['trace','key','loops','V']]
std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());controls=[]
for mult in [1,2,3]:
 for h in range(4):
  ev,d,eh=trace(std['word']*mult,h);P=len(ev);H={}
  for t,q,hi,ho,c in ev:r,k=key(q,d);H.setdefault(r,[]).append((t-k*P,hi,ho,c,t))
  for es in H.values():es.sort();assert ''.join(z[3]for z in es)==''.join('R'if i%2==0 else'L'for i in range(len(es)))
  typ={r:('single'if len(es)==1 else('odd'if len(es)%2 else'even')+('_same'if es[0][1]==es[-1][1]else'_opposite'))for r,es in H.items()};E={}
  for r,es in H.items():
   f=es[0];q,k=key(r+V[f[2]],d)
   if f[0]+1==H[q][-1][0]+k*P:E[r]=(q,k);assert typ[r]in ['single','odd_opposite','even_same']and typ[q]in ['single','odd_opposite','even_opposite']
  n=Counter(typ.values());assert len(E)<=n['single']+n['odd_opposite']+min(n['even_same'],n['even_opposite'])
  for cyc,w in loops(E):
   assert w==-1 and sum(typ[r]=='single'for r in cyc)==sum(typ[r]=='odd_opposite'for r in cyc)==len(cyc)//2 and P>=3*len(cyc)
  controls.append(dict(P=P,h=h,types=dict(n),E=len(E)))
rng=random.Random(20261024);checked=exc=0
for i in range(120):
 pts=[complex(x,y)for x in range(-3,4)for y in range(-3,4)];B=set(rng.sample(pts,rng.randrange(15)))if i else set();p=0j;h=i%4;tr=[];H={}
 for t in range(3000):
  c='L'if p in B else'R';ho=(h+(1 if c=='R'else-1))%4;z=(t,p,h,ho,c);tr.append(z);H.setdefault(p,[]).append(z);B.symmetric_difference_update({p});p+=V[ho];h=ho
 for u,es in H.items():
  f,l=es[0],es[-1]
  if f[4]!='R'or f[0]==2999:continue
  v=tr[f[0]+1][1];fv,lv=H[v][0],H[v][-1]
  if lv[0]!=f[0]+1:continue
  checked+=1
  if len(H[v])>1:
   if fv[0]==0:exc+=1
   else:assert fv[2]!=lv[2]
  if len(es)>1:
   if l[0]==2999:exc+=1
   else:assert(f[2]==l[2])==(l[4]=='L')
assert checked==15018 and exc==27
B=set();p=0j;h=0;rd=[]
for t,c in enumerate('RRRRLRRRR'):
 assert('L'if p in B else'R')==c;rd.append((t,p,h,c));B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
origin=[(t,h,c)for t,q,h,c in rd if q==0];assert origin==[(0,0,'R'),(4,0,'L'),(8,2,'R')]
out={'status':'PASS exact all-cap extremal source/sink types and refined capacities','author_note':sha(D/'EXTREMAL_PORT_TYPE_REFINEMENT.md'),'prior_independent_report':sha(S.with_name('check_all_cap_extremal_read_coupling_independent.json')),'standard_controls':controls,'marked_actual_finite_edges':checked,'boundary_exceptions_retained':exc,'blank_origin_age8':origin,'analytic_review':[
'A nonsingleton target cannot have equal first/last incoming heading: its earlier arrival would require the same source neighbor before that source firstR. A nonsingleton source cannot use its first outgoing edge again on its last departure, because the neighbor already had its last read. With the two invariant-axis-compatible headings, lastL therefore forces SAME and lastR OPPOSITE. No cap or WHITE assumption off the two relevant complete histories is used.',
'Only singleton/odd-opposite vertices can be internal. Even-same vertices are source-only, even-opposite sink-only, odd-same isolated. Counting possible outgoing and incoming ends separately yields |E|<=A+min(e_same,e_opposite); it is not an assumption every allowable port is attained.',
'On an E cycle the incoming selected event is the target last read. At singletons it equals first incoming, giving geometricR; at odd-opposite it is opposite, giving geometricL. The signed embedded essential b-cycle has winding-1 and equal R/L counts, so exactly half each. Disjoint cycles give n1,no>=||d||infinity*cE.',
'The age identity P=sum(H-F)-length and at least two positive return gaps of length divisible by4 for each nonsingleton odd give P>=3*cycle length. The exact blank9-turn RRRRLRRRR control has originR0,L4,R8 with incomingN,N,S, so the local age8 lower bound is sharp; two returns do not imply restored heading.',
'Every overlap of a selected b cycle and reversed k cycle has BOTH endpoints even. The port rule places source in even-same and target in even-opposite, so C<=min(e_same,e_opposite). This bounds but does not erase the overlap correction and does not exclude reverse essential cycles or classify controllers.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
