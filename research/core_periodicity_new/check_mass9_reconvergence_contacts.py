"""All-length complete mass-nine prefix tree plus literal core contacts.
Independent audit requested; no depth or node cutoff in this certificate.
"""
from pathlib import Path
from collections import deque,Counter
import json,hashlib
R=Path(__file__).resolve().parent;gp=R/'chronology_dcuv/literal_residual_geometry.json';JJ=json.loads(gp.read_text());G=JJ['geometry'];IDS=(0,1,4,5,6,7,8,9);K={tuple(q)for q in JJ['core']};DIR=((0,1),(1,0),(0,-1),(-1,0));MARK=G[0]['marker']
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return(p[0]+q[0],p[1]+q[1])
def trace(w):
 program=''.join(G[a]['word']for a in w)+MARK;col={};seed=set();p=(0,0);h=0
 for t,c in enumerate(program):
  b=c=='L'
  if p in col and col[p]!=b:return {'consistent':False,'conflict':[t,*p,c]}
  if p not in col and b:seed.add(p)
  col[p]=not b;h=(h+(-1 if b else 1))%4;p=add(p,DIR[h])
 return {'consistent':True,'initial_black_cells':sorted(seed),'raw_length':sum(len(G[a]['word'])for a in w)}
def incidence(w,seed):
 roots=sorted(set(map(tuple,seed))-K);P=list(range(len(roots)));T={q:('root',i,i)for i,q in enumerate(roots)};p=(0,0);h=0;hist=[];beta=0;t=0;B=set(map(tuple,seed))
 def find(i):
  while P[i]!=i:i=P[i]
  return i
 for j,a in enumerate(w):
  I=[add(p,rot(q,h))for q in G[a]['inputs']];ins=[T.pop(q)for q in I];comps={find(v[-1])for v in ins};input_rootsets=[[roots[i]for i in range(len(roots))if find(i)==c]for c in sorted(comps)];inc=len(I)-len(comps);beta+=inc;z=min(comps)
  for c in comps:P[c]=z
  O=[]
  for si,q in enumerate(G[a]['outputs']):
   qq=add(p,rot(q,h));assert qq not in T;T[qq]=(j,si,z);O.append(qq)
  base=0 if a in(0,1)else 4 if a in(4,5,6)else 7;baseword=G[base]['word'];anchor=(0,1)if base==0 else(1,2)if base==4 else(0,3);anchorworld=add(p,rot(anchor,h));basepoint=add(p,rot(G[base]['endpoint'][:2],h));basecore={add(basepoint,rot(q,h))for q in K};assert anchorworld in basecore
  pp=p;hh=h
  for k,c in enumerate(G[a]['word']):
   assert(c=='L')==(pp in B)
   if pp in B:B.remove(pp)
   else:B.add(pp)
   hh=(hh+(-1 if c=='L'else 1))%4;pp=add(pp,DIR[hh])
   if k+1==len(baseword):assert basecore<=B
  hist.append({'packet':a,'pose':[*p,h],'inputs':I,'input_identities':ins,'input_rootsets_before':input_rootsets,'beta_increment':inc,'base_core_time':t+len(baseword),'base_core_pose':[*basepoint,h],'selected_input_cell_in_core':anchorworld,'all_input_cells_in_base_core':[q for q in I if q in basecore]})
  p=add(p,rot(G[a]['endpoint'][:2],h));h=(h+G[a]['endpoint'][2])%4;assert pp==p and hh==h;t+=len(G[a]['word'])
 return {'beta':beta,'components':[[roots[i]for i in range(len(roots))if find(i)==c]for c in sorted({find(i)for i in P})],'history':hist,'final_residual_count':len(T)}
Q=deque([()]);accepted=[()];reject=[];rs={():None}
while Q:
 w=Q.popleft()
 for a in IDS:
  ww=w+(a,);r=trace(ww)
  if r['consistent']and len(r['initial_black_cells'])<=9:Q.append(ww);accepted.append(ww);rs[ww]=r
  else:reject.append({'word':ww,**r,'reason':'needs_at_least_ten_black'if r['consistent']else'literal_conflict'})
assert len(accepted)==87 and max(map(len,accepted))==5;reports=[];cycles=[]
for w in accepted[1:]:
 r=rs[w];inc=incidence(w,r['initial_black_cells']);report={'word':w,'initial_black_cells':r['initial_black_cells'],'beta':inc['beta'],'component_count':len(inc['components'])};reports.append(report)
 if inc['beta']:cycles.append({**report,**inc})
assert [z['word']for z in cycles]==[(1,6,4,4),(1,6,4,5)]
for z in cycles:
 assert z['beta']==1 and z['component_count']==2;H=z['history'];assert H[-1]['input_identities']==[(0,2,3),(0,0,3)]
 assert H[1]['base_core_time']==43 and H[2]['base_core_time']==91 and H[3]['base_core_time']==109
 assert H[1]['selected_input_cell_in_core']==(-1,3)and H[2]['selected_input_cell_in_core']==(-1,1)
 assert H[3]['input_rootsets_before']==[[(0,1)]]
# Virgin D/DC cohort is disjoint from ALL inputs of EVERY immediate successor.
immediate=[]
for b in(0,1):
 O={tuple(q)for q in G[b]['outputs']};p=G[b]['endpoint'][:2];h=G[b]['endpoint'][2]
 for a in IDS:
  I={add(p,rot(q,h))for q in G[a]['inputs']};assert not I&O;immediate.append({'producer':b,'successor':a,'successor_pose':[*p,h],'successor_inputs':sorted(I),'source_outputs':sorted(O),'intersection':[]})
J={'status':'AUTHOR_COMPLETE_MASS9_CLOSURE_AND_CORE_CONTACT_PASS','scope':'Reset incidence components at a complete recurrent-eight factor entry, total boundary mass<=9; no global inherited-component theorem or per-cycle fresh-root budget.','accepted_words':accepted,'accepted_count':len(accepted),'depth_distribution':dict(Counter(map(len,accepted))),'max_packet_length':5,'rejected_extensions':reject,'all_nonempty_incidence_summaries':reports,'all_cycle_histories':cycles,'virgin_D_DC_immediate_successor_disjointness':immediate,'input_sha256':hashlib.sha256(gp.read_bytes()).hexdigest()}
(R/'chronology_dcuv/mass9_reconvergence_contacts.json').write_text(json.dumps(J,indent=2)+'\n');print({'accepted':len(accepted),'all_extensions':8*len(accepted),'depth_distribution':J['depth_distribution'],'cycles':[z['word']for z in cycles],'contact_times':[43,91,109],'all_count_first_successor_controls':len(immediate)})
