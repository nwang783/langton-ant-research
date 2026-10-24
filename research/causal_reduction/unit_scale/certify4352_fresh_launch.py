"""Complete supplied6812-read causal launch of4352 from two mature bands,
one causal SW standard writer and289 fresh black additions. No finite producer
is inferred here. Entire past/future read ownership is checked arithmetically.
"""
from pathlib import Path
from collections import defaultdict
import json,runpy,hashlib
import inverse4352_tail_completion as T
P=Path(__file__).resolve().parent;G=T.G
A=json.loads((P/'4352_supplied_inverse_prelude.json').read_text())['found'];assert A
edits={tuple(q)for q in A['initial_wave_XOR_edits']};assert all(not T.future_read(q)for q in edits)
C=runpy.run_path(str(G/'certify_prepared_travelling_wave.py'))
def color(q,rows,F):return T.bulk(q)^(q in F)
C['cert_parallel'].__globals__['color']=color
p=T.POSE[0]-T.V[T.HEAD][0],T.POSE[1]-T.V[T.HEAD][1];h=(T.HEAD+2)%4;F=T.BASE^edits;inverse_reads=[]
for c in A['inverse_prefix']:
 assert color(p,{},F)==(c=='L');inverse_reads.append(p);F.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=T.V[h];p=(p[0]+v[0],p[1]+v[1])
assert[list(p),h]==A['inverse_tail_pose'];assert F=={tuple(q)for q in A['forward_entry_cap_vs_full_bulk']}
ic=C['cert_parallel']({},F,p,h,A['inverse_tail_word']);assert ic
wc=C['cert_parallel']({},T.BASE^edits,T.POSE,T.HEAD,T.J['word']);assert wc
rr,_,_=T.trace(A['inverse_tail_word'],p,h);groups=defaultdict(list)
for i,(x,y),hh,c in rr:groups[x-y,x%2].append((i-104*(x//2),x//2,c))
groups={j:sorted(g)for j,g in groups.items()}
def required(q):
 x,y=q
 for time,k,c in groups.get((x-y,x%2),()):
  if k<=x//2:return c=='L'
 return None
def other(q):return T.bulk(q)and(q[0]-q[1],q[0]%2)not in groups
K={tuple(q)for q in A['fresh_cap']};assert len(K)==289 and all(required(q)is None for q in K)
assert all(not(6<=x-y<=16 or 22<=x-y<=32)for x,y in K)
def fresh(q,flips=()):
 c=required(q);return other(q)^(bool(c)if c is not None else False)^(q in K)^(q in flips)
def old(q):return T.bulk(q)^(q in F)
checks=0
for(t,a),start in T.FUTURE.items():
 critical={start}
 for _,k,_ in groups.get((t,a%2),()):
  n=(2*k-a)//26;critical.update(n+j for j in(-1,0,1)if n+j>=start)
 for q in F|K:
  if q[0]-q[1]==t and q[0]%26==a:
   n=q[0]//26;critical.update(n+j for j in(-1,0,1)if n+j>=start)
 for n in critical:
  q=(a+26*n,a+26*n-t);assert fresh(q)==old(q),(q,'future field');checks+=1
entry=tuple(A['forward_entry_pose'][0]);eh=A['forward_entry_pose'][1];fr,ep,hh=T.trace(A['forward_word'],entry,eh)
for _,q,hh,c in fr:assert fresh(q)==old(q),(q,'prelude field')
# Direct entire fresh field replay, not just inferred colors of a pruned cap.
p=entry;h=eh;flips=set();literal=0
for c in A['forward_word']+T.J['word']*2:
 assert fresh(p,flips)==(c=='L'),('literal',literal,p,h,c)
 flips.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=T.V[h];p=(p[0]+v[0],p[1]+v[1]);literal+=1
out={'scope':__doc__,'status':'PASS exact prepared causal/future ownership','normalization_translation':[-70,-70],
 'forward_entry_pose':A['forward_entry_pose'],'incoming_H_phase':A['H_phase'],'forward_prelude_word':A['forward_word'],'wave_pose':[T.POSE,T.HEAD],'wave_word_sha256':hashlib.sha256(T.J['word'].encode()).hexdigest(),
 'inverse_tail_pose':A['inverse_tail_pose'],'inverse_tail_word':A['inverse_tail_word'],'inverse_prefix':A['inverse_prefix'],'inverse_certificate':ic,'wave_certificate':wc,
 'other_full_black_profiles':sorted(j for j in T.B if j not in groups),'fresh_cap':sorted(K),'fresh_cap_mass':len(K),'cap_u_hull':[min(x+y for x,y in K),max(x+y for x,y in K)],'cap_t_hull':[min(x-y for x,y in K),max(x-y for x,y in K)],
 'cap_disjoint_entire_incoming_strict_past':True,'cap_disjoint_other_two_writer_read_bands':True,'initial_wave_edits':sorted(edits),'all_initial_wave_edits_future_unread':True,'future_ray_field_equality_tests':checks,'literal_fresh_field_read_control':literal,'literal_final_pose':[p,h],
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_fresh_launch.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('forward_prelude_word','inverse_tail_word','inverse_prefix','fresh_cap','initial_wave_edits','other_full_black_profiles')},indent=2))
