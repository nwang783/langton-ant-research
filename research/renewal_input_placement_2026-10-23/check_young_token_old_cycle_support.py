"""Actual original184 trajectory: young deleted lifetime, old indispensable cycle support."""
from build_forced_input_cycles import *
import heapq
OUT=Path(__file__).parent

def state_with_births(N=3,slot=126):
 U=ROOT/'causal_reduction/unit_scale';sys.path.insert(0,str(U));import check1564_noncrossing_producer as mod
 p,B,segs,_=mod.setup(100+28*N,N);h=3;seed=sorted(B);birth={q:-1 for q in B};t=0
 for s in segs:
  assert[p,h]==s['start']
  if s['kind']=='wave':break
  word=mod.H*s['count']if s['kind']=='H'else s['word']
  for c in word:
   assert('L'if p in B else'R')==c
   if c=='R':birth[p]=t
   else:del birth[p]
   p,h=step(B,p,h);t+=1
 entry=t
 for c in mod.W[:slot]:
  assert('L'if p in B else'R')==c
  if c=='R':birth[p]=t
  else:del birth[p]
  p,h=step(B,p,h);t+=1
 assert mod.W[slot]=='L'and p in B
 return B,p,h,birth,t,entry,seed

def widest_cycle_path(B,q,k,birth,now):
 G=graph(B-{q},k);s,t=endpoints(q,k);cap={s:now+1};par={};todo=[(-(now+1),s)]
 while todo:
  neg,v=heapq.heappop(todo);a=-neg
  if a!=cap[v]:continue
  if v==t:break
  for u,e in G.get(v,()):
   z=min(a,birth[e])
   if u not in cap or z>cap[u]:cap[u]=z;par[u]=(v,e);heapq.heappush(todo,(-z,u))
 assert t in cap;beta=cap[t];path=[];v=t
 while v!=s:v,e=par[v];path.append(e)
 path=path[::-1];assert min(birth[e]for e in path)==beta
 young={e for e in B-{q}if birth[e]>beta}
 assert not connected(young,k,s,t)
 assert connected({e for e in B-{q}if birth[e]>=beta},k,s,t)
 return beta,path

if __name__=='__main__':
 B,q,h,birth,t,entry,seed=state_with_births();k=wwhich(q,h);beta,path=widest_cycle_path(B,q,k,birth,t)
 out={'status':'full birth trace, maximin cycle witness and strict-threshold nonconnection PASS','original_seed_mass':len(seed),'original_seed':seed,'N':3,'wave_entry_time':entry,'relative_update':126,'global_update':t,'pose':[q,h],'deleted_lifetime_birth':birth[q],'deleted_lifetime_age':t-birth[q],'latest_possible_cycle_bottleneck_birth':min(birth[q],beta),'indispensable_cycle_support_age':t-min(birth[q],beta),'bypass_bottleneck_birth':beta,'bypass_edges':len(path),'cycle_cells':[q]+path,'cycle_lifetime_births':[(e,birth[e])for e in[q]+path],'complete_current_board':sorted(B),'complete_current_lifetime_births':sorted(birth.items()),'minimal_word_read_board_is_bridge':True}
 (OUT/'young_token_old_cycle_support.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('original_seed','cycle_cells','cycle_lifetime_births','complete_current_board','complete_current_lifetime_births')},indent=2))
