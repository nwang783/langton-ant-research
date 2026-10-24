"""Named actual helper-return legs, with complete fields and old lifetimes.
No candidate-word, pose, seed or ratio scan.
"""
from pathlib import Path
from collections import defaultdict
import sys,json
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import rot,cursor,ends,sector,step

class Graph:
 def __init__(self,B,k):
  self.k=k;self.g=defaultdict(dict)
  for q in B:self.change(q,True)
 def change(self,q,on):
  a,b=ends(q,self.k)
  if on:self.g[a][b]=q;self.g[b][a]=q
  else:del self.g[a][b];del self.g[b][a]
 def comp(self,v):
  E=set();seen={v};todo=[v]
  for a in todo:
   for b,q in self.g[a].items():
    E.add(q)
    if b not in seen:seen.add(b);todo.append(b)
  return E
 def components(self,B):
  left=set(B);ans=[]
  while left:
   q=min(left);C=self.comp(ends(q,self.k)[0]);ans.append(C);left-=C
  return ans

def run(name,B0,p0,h0,d,j,helper,helper_birth,target,target_birth,parent_death,verify_to=None):
 B=set(B0);p=p0;h=h0;born={q:None for q in B};k=sector(p,h);G=Graph(B,k)
 stop=verify_to if verify_to is not None else j;K=[];M=0;res=None
 for t in range(stop+1):
  C=G.comp(cursor(p,h))
  if d-1<=t<=j:M=max(M,len(C))
  if t==d:
   start=set(B);startborn=dict(born);old=set(B);origin=p;originh=h;startC=set(C)
   assert helper in B and target in B and born[helper]==helper_birth and born[target]==target_birth
   assert target not in C
  if t==j:
   assert p==helper and born[p]==helper_birth and p in B
   assert target in B and born[target]==target_birth
   L=max(abs(p[i]-origin[i])for i in(0,1));axis=max((0,1),key=lambda i:abs(p[i]-origin[i]));lines=list(range(min(p[axis],origin[axis])+1,max(p[axis],origin[axis])))
   fresh={q for q in B if born[q]is not None and born[q]>=d};A=B-start;O=start-B
   assert O<={tuple(z['cell'])for z in K}
   per=[]
   for a in lines:
    delta={q for q in B^start if q[axis]==a};fr={q for q in fresh if q[axis]==a};kr=[z for z in K if z['cell'][axis]==a]
    assert len(delta)>=2 and len(fr)+len(kr)>=2
    per.append(dict(line=a,discrepancy=sorted(delta),fresh=sorted(fr),old_retirements=kr))
   delta=len(B)-len(start);passivedelta=(len(B)-len(C))-(len(start)-len(startC))
   assert delta+2*len(K)>=2*len(lines)
   assert passivedelta>=2*len(lines)-2*len(K)-M
   comps=G.components(B);newdorm=[a for a in comps if a!=C and a&fresh]
   assert all(len(a)<=M-1 for a in newdorm)
   bound=max(0,2*len(lines)-len(K)-M);countbound=(bound+M-2)//(M-1)
   assert len(newdorm)>=countbound
   res=dict(name=name,initial_black=sorted(B0),initial_pose=[p0,h0],departure=d,helper_consumption=j,parent_consumption=parent_death,
    helper=helper,helper_birth=helper_birth,parent=target,parent_birth=target_birth,
    departure_pose=[origin,originh],helper_read_pose=[p,h],distance=L,axis=axis,M=M,older_cut_d_consumptions_before_helper=K,
    old_consumption_count=len(K),global_mass_change=delta,passive_mass_change=passivedelta,
    connector_or_growth_rhs=2*len(lines),connector_or_growth_lhs=delta+2*len(K),
    new_fresh_mass=len(fresh),new_dormant_component_count=len(newdorm),new_dormant_component_lower_bound=countbound,
    departure_full_black=sorted(start),departure_births=[[q,startborn[q]]for q in sorted(start)],departure_active=sorted(startC),
    helper_pre_read_full_black=sorted(B),helper_pre_read_births=[[q,born[q]]for q in sorted(B)],helper_pre_read_active=sorted(C),
    per_line=per,new_complete_dormant_components=[dict(edges=sorted(a),fresh=sorted(a&fresh))for a in newdorm],
    helper_and_target_excluded_from_K=True)
   assert all(tuple(z['cell'])not in(helper,target)for z in K)
  if verify_to is not None and t==parent_death:
   assert p==target and born[p]==target_birth and p in B
   res['parent_actual_consumption_independently_replayed']=True
  if t==stop:break
  q=p;on=q not in B
  if on:born[q]=t
  else:
   if d<=t<j and q in old:
    K.append(dict(update=t,cell=q,cut_d_birth=startborn[q]));old.remove(q)
   born.pop(q)
  G.change(q,on);p,h=step(B,p,h)
 return res

blank=run('blank completed fresh interleaving',set(),(0,0),0,18,53,(1,0),1,(0,1),7,59,59)
n=400;G0={(0,-1),(1,1),(2,2),(1,3)};B=set()
for p,h in [((0,0),1),((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)]:
 B|={(p[0]+v[0],p[1]+v[1])for q in G0 for v in[rot(q,(h-1)%4)]}
feedback=run('signed20-cell old-root helper, n400',B,(0,0),1,173,52*n-172,(n,n),None,(0,2),60,624*n-1516)
feedback['parent_consumption_scope']='Retained signed all-n trajectory and earlier full-history n400 replay, not rerun past this helper in this checker.'
out=dict(status='AUTHOR complete helper-return connector-or-growth controls',controls=[blank,feedback],scope='Blank pair is short-range and all R-born.20-cell helper is a genuine old INITIAL root, not a R-born episode with an earlier departure. No arbitrary fresh long-range interleaving construction.')
(OUT/'helper_return_connector_or_growth_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:a[k]for k in['name','distance','M','old_consumption_count','global_mass_change','passive_mass_change','connector_or_growth_rhs','connector_or_growth_lhs','new_dormant_component_count','new_dormant_component_lower_bound']}for a in out['controls']],indent=2))
