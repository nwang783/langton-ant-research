"""Self-contained literal verifier. Does not import any discovery geometry."""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib,gzip
OUT=Path(__file__).parent
D=((0,1),(1,0),(0,-1),(-1,0))
def ends(e,k):
 x,y=e;s=1 if (x+y)%2==k else -1
 return((2*x-1,2*y-s),(2*x+1,2*y+s))
class Graph:
 def __init__(self,B,k):
  self.k=k;self.g=defaultdict(dict)
  for e in B:self.insert(e)
 def insert(self,e):
  u,v=ends(e,self.k);self.g[u][v]=e;self.g[v][u]=e
 def erase(self,e):
  u,v=ends(e,self.k);del self.g[u][v];del self.g[v][u]
 def connected(self,e,skip=False):
  u,v=ends(e,self.k);seen={u};todo=[u]
  for x in todo:
   for y,f in self.g[x].items():
    if skip and f==e:continue
    if y==v:return True
    if y not in seen:seen.add(y);todo.append(y)
  return False
 def component(self,v):
  seen={v};todo=[v];edges=set()
  for x in todo:
   for y,e in self.g[x].items():
    edges.add(e)
    if y not in seen:seen.add(y);todo.append(y)
  return edges
 def rank(self):
  vertices={u for u in self.g if self.g[u]};E=sum(len(self.g[u])for u in vertices)//2;seen=set();C=0
  for u in vertices:
   if u in seen:continue
   C+=1;seen.add(u);todo=[u]
   for x in todo:
    for y in self.g[x]:
     if y not in seen:seen.add(y);todo.append(y)
  return E-len(vertices)+C

def H(B):return hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest()
def check(c,component_stream=None):
 q=c['q'];E=c['expected'];B=set(map(tuple,c['initial_black']));base=set(map(tuple,c['baseline_black']));extra=set(map(tuple,c['additional_initial_black']));assert B==base|extra and not(base&extra)
 assert len(B)==E['initial_mass']and len(extra)==E['extra_mass']
 p,h=tuple(c['initial_pose'][0]),c['initial_pose'][1];assert p==(1,1)and h==1
 graph=[Graph(B,k)for k in(0,1)];initial_ranks=[g.rank()for g in graph];birth={x:('baseline'if x in base else'added',-1)for x in B}
 r=0;t=0;stages=[];A1=set();A2=set();readprefix=set();allA2afterreturn=False;first_extra={x:None for x in extra};component_hash=hashlib.sha256();component_samples=0;last_recorded=-1
 def record_components():
  nonlocal component_samples,last_recorded
  if t==last_recorded:return
  last_recorded=t
  def cursor(v):
   a,b=v
   for _ in range(h):a,b=b,-a
   return(2*p[0]+a,2*p[1]+b)
  W=graph[0].component(cursor((1,-1)));Z=graph[1].component(cursor((-1,-1)))
  row=dict(q=q,cut=t,pose=[p,h],full_active_w=sorted(W),full_active_z=sorted(Z))
  raw=(json.dumps(row,separators=(',',':'))+'\n').encode();component_hash.update(raw);component_samples+=1
  if component_stream is not None:component_stream.write(raw)
 for stage in c['stages']:
  name=stage['name'];w=stage['word'];start=len(B);count=Counter();deaths=Counter();ex=[];be=[0,0];de=[0,0];entry=[p,h];A2cons=[];ranksin=[g.rank()for g in graph]
  for j,ch in enumerate(w):
   record_components()
   if p in extra and first_extra[p]is None:first_extra[p]=t
   assert ch==('L'if p in B else'R'),(q,name,j,p,ch)
   assert (p[0]+p[1]+h)%2==1
   if name in('first_positive_ordinary','first_charged_return','second_positive_ordinary'):readprefix.add(p);assert p not in extra
   count[ch]+=1
   if ch=='L':
    cyc=[g.connected(p,True)for g in graph];exw=r>=3 or cyc[0]
    if exw:ex.append(dict(offset=j,r=r,cell=p,w_nonbridge=cyc[0]))
    if 'positive_ordinary'in name:assert r<=2 and not cyc[0],(q,name,j,'not ordinary')
    origin,b=birth.pop(p);deaths[origin]+=1
    if name=='first_positive_ordinary':assert origin=='baseline'
    if name=='third_positive_ordinary'and origin=='second_positive_ordinary':A2cons.append((p,b))
    B.remove(p)
    for k,g in enumerate(graph):de[k]+=cyc[k];g.erase(p)
    h=(h-1)%4;r=0
   else:
    cyc=[g.connected(p)for g in graph];B.add(p);birth[p]=(name,t)
    if name=='first_positive_ordinary':A1.add((p,t))
    if name=='second_positive_ordinary':A2.add((p,t))
    for k,g in enumerate(graph):be[k]+=cyc[k];g.insert(p)
    h=(h+1)%4;r+=1
   p=(p[0]+D[h][0],p[1]+D[h][1]);t+=1
  assert r==0 and w[-1]=='L';assert len(B)-start==stage['gain']
  if name=='first_charged_return':assert A1<={(x,b)for x,(origin,b)in birth.items()};assert len(ex)==2
  if name=='second_positive_ordinary':assert not(A1&{(x,b)for x,(origin,b)in birth.items()});assert len(A2)==E['second_R_lifetimes']
  if name=='second_charged_return':assert A2<={(x,b)for x,(origin,b)in birth.items()};assert len(ex)==2;allA2afterreturn=True
  if name=='third_positive_ordinary':assert len(A2cons)==E['second_R_consumed_in_third'];assert deaths=={'second_positive_ordinary':len(A2cons),'added':q-1};assert count['L']==E['third_ordinary_L']and count['R']==E['third_ordinary_R']
  stages.append(dict(name=name,duration=len(w),entry_pose=entry,exit_pose=[p,h],R=count['R'],L=count['L'],gain=len(B)-start,deaths_by_origin=dict(deaths),w_exceptions=ex,cycle_births_w_z=be,cycle_erasures_w_z=de,ranks_in=ranksin,ranks_out=[g.rank()for g in graph],full_field_sha256=H(B),full_field=sorted(B)))
 record_components()
 assert allA2afterreturn and not(extra&readprefix)
 assert t==E['total_duration']and len(B)-len(base|extra)==E['net_gain']
 remaining=A2&{(x,b)for x,(origin,b)in birth.items()};assert len(remaining)==5
 oldextras={x for x,(origin,b)in birth.items()if origin=='added'};assert len(oldextras)==3
 oldbase={x for x,(origin,b)in birth.items()if origin=='baseline'};assert len(oldbase)==3
 final_pose=[p,h];final=sorted(B);final_labels=[[x,origin,b]for x,(origin,b)in sorted(birth.items())]
 # The third interval really stops immediately before a nonordinary full RRL block.
 for i,ch in enumerate(c['following_exception_word']):
  assert ch==('L'if p in B else'R')
  if ch=='R':B.add(p);[g.insert(p)for g in graph];h=(h+1)%4
  else:assert i==2 and graph[0].connected(p,True);B.remove(p);[g.erase(p)for g in graph];h=(h-1)%4
  p=(p[0]+D[h][0],p[1]+D[h][1])
 return dict(q=q,additional_initial_cell_first_reads=[[x,first_extra[x]]for x in sorted(extra)],full_component_stream_sha256=component_hash.hexdigest(),full_component_cut_count=component_samples,status='AUTHOR literal verified',initial_mass=len(base|extra),additional_seed=len(extra),additional_seed_unread_through_original_prefix=True,initial_ranks_w_z=initial_ranks,stages=stages,remaining_second_lifetimes=sorted(remaining),surviving_original_added_lifetimes=sorted(oldextras),surviving_original_baseline_lifetimes=sorted(oldbase),final_pose=final_pose,full_final_field=final,full_final_lifetime_labels=final_labels,total_duration=t,net_gain=len(final)-len(base|extra),following_RRL_is_w_nonbridge=True,scope='One finite fully charged construction, not self-regeneration.')
if __name__=='__main__':
 src=OUT/'THREE_POSITIVE_PASSES_CERTIFICATE.json';cert=json.loads(src.read_text());ans=[]
 with gzip.open(OUT/'THREE_POSITIVE_PASSES_FULL_COMPONENTS.jsonl.gz','wb')as component_stream:
  for c in cert['cases']:
   a=check(c,component_stream);ans.append(a);print({k:a[k]for k in['q','initial_mass','additional_seed','total_duration','net_gain','initial_ranks_w_z']},flush=True)
 (OUT/'THREE_POSITIVE_PASSES_CHECKED.json').write_text(json.dumps(dict(status='AUTHOR verified, independent audit requested',certificate_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),cases=ans),indent=2)+'\n')
