"""Finite exact sources/masks and sharp literal controls for a conditional V1 history."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
GP=R/'chronology_dcuv/literal_residual_geometry.json'; CP=R/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
G=json.loads(GP.read_text())['geometry']; M={0:0,1:1,4:2,5:3,6:4,7:5,8:6,9:7}
F={tuple(map(int,s.split()[:8]))for s in CP.read_text().splitlines()}
K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};DIR=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def ht(p):return sum(p)
def geom_reads(word,p=(0,0),h=0):
 out=[]
 for t,ch in enumerate(word):
  out.append((t,p,ch));h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h])
 return out,(p,h)
assert G[1]['endpoint']==[1,2,3] and (2,0)in map(tuple,G[1]['outputs']) and (3,1)in map(tuple,G[1]['outputs'])
source_output_heights=[ht(p)-1 for p in G[1]['outputs']];assert source_output_heights==[1,4,3,4]
masks=[]
for a,offset,mins in [(4,-2,[2,3]),(7,-4,[3,3,5,5,5])]:
 rows=[]
 for p,age in zip(G[a]['inputs'],mins):
  lev=offset+ht(rot(p,1));forbidden28=28+2*lev>=26;forbidden30=30+2*lev>=26
  rows.append(dict(slot=p,height_minus_H=lev,minimum_produced_age=age,entry_forbidden_I28=forbidden28,entry_forbidden_I30=forbidden30,pre_DC_I28=forbidden28 and age>=3,pre_DC_I30=forbidden30 and age>=3))
 masks.append(dict(helper=a,inputs=rows))
assert sum(r['pre_DC_I28']for r in masks[0]['inputs'])==1
assert sum(r['pre_DC_I28']for r in masks[1]['inputs'])==3
assert all(r['pre_DC_I30']for r in masks[1]['inputs'])
queries=[];survive=[]
for a in M:
 for oi,o in enumerate(G[a]['outputs']):
  w=o[0]-o[1];pre=1+w
  if pre<0 or pre%2:continue
  query=(M[a],M[4],o[0],o[1]+3,2,*o,2)
  cut=query in F
  row=dict(source=a,output_index=oi,output=o,cone_rhs=pre,count5_query=query,count5_excluded=cut)
  queries.append(row)
  if not cut:survive.append(row)
assert[(r['source'],r['output'])for r in survive]==[(4,[0,1]),(6,[0,1])]
assert all(r['cone_rhs']==0 for r in survive)
# All g>=1 conflict proof: the infinite prefix is reduced analytically to raw
# read membership in a single packet or two exceptional DC coordinates.
draw,_=geom_reads(G[0]['word']);drawset={p for _,p,_ in draw}
assert all((k-1,k)not in drawset for k in range(1,4))
assert max(p[1]for p in drawset)<3 # k>=3 is outside, and k=3 already tested
DCraw,_=geom_reads(G[1]['word']);dcset={p for _,p,_ in DCraw}
assert (0,2)not in dcset and (-1,3)not in dcset and min(p[0]for p in dcset)>=-1
fixed=G[6]['word']+G[4]['word']+G[0]['word']+G[0]['marker'][:2]
read,_=geom_reads(fixed);hits=[(t,ch)for t,p,ch in read if p==(-1,0)]
assert hits==[(1,'L'),(77,'L')]
# Exact minimal initial field and full ordered residual replay, no invented head resets.
def replay(ids):
 word=''.join(G[a]['word']for a in ids)+G[ids[-1]]['marker'];reads,_=geom_reads(word);need={};par={}
 for t,p,ch in reads:
  b=(ch=='L')^par.get(p,False)
  assert p not in need or need[p]==b,(ids,t,p)
  need[p]=b;par[p]=not par.get(p,False)
 seed={p for p,b in need.items()if b};assert K<=seed
 B=set(seed);T={p:('entry',None)for p in seed-K};p=(0,0);h=0;clock=0;t=0;records=[]
 for j,a in enumerate(ids):
  assert B=={add(p,rot(k,h))for k in K}|set(T)
  I=[add(p,rot(q,h))for q in G[a]['inputs']];ages=[None if T[q][1]is None else clock-T[q][1]for q in I]
  births=[T[q][0]for q in I]
  if j==len(ids)-2:
   assert a==4 and p==(-3,2)and h==1 and clock==3
   assert births[0]in(1,) and ages[0]==2
  if j==len(ids)-1:assert births==[0,0]and ages==[3,3]
  for q in I:del T[q]
  for q in G[a]['outputs']:
   v=add(p,rot(q,h));assert v not in T;T[v]=(j,clock)
  records.append(dict(index=j,packet=a,pose=[*p,h],C=clock,input_cells=I,input_birth_packets=births,input_ages=ages))
  for ch in G[a]['word']:
   assert(ch=='L')==(p in B)
   if p in B:B.remove(p)
   else:B.add(p)
   h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h]);t+=1
  clock+=G[a]['name'].count('C')
 for ch in G[ids[-1]]['marker']:
  assert(ch=='L')==(p in B)
  if p in B:B.remove(p)
  else:B.add(p)
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h]);t+=1
 return dict(word=ids,seed=sorted(seed),mass=len(seed),reads_including_marker=t,records=records)
controls=[replay([1,6,4,4]),replay([1,4,6,4,4,4])]
assert [c['mass']for c in controls]==[9,12]
J=dict(status='AUTHOR_CONDITIONAL_V1_COHORT_OLDER_SUPPORT_AND_YOUNG_HELPER_BRANCH_PASS',scope='Only DC(3,1) to V lower slot at relative(0,1,E), exactage3. No V1/global closure. Older-support deductions independently analytically checked; finite source/word refinement submitted.',source_output_heights_minus_H=source_output_heights,helper_input_masks=masks,young_critical_origin_queries=queries,young_critical_survivors=survive,all_g_conflict=dict(cell='(1-g,1+g)',times=['26+10g','102+10g'],fixed_block_hits=hits),literal_controls=controls,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in [GP,CP,Path(__file__).resolve()]})
(R/'chronology_dcuv/v1_dc_age3_joint_history.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(survivors=survive,pre_DC_counts_I28=[sum(q['pre_DC_I28']for q in r['inputs'])for r in masks],controls=[(c['word'],c['mass'])for c in controls]))
