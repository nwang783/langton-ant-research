"""Two named complete-field controls for a conditional spatial archive ledger.

This is not a seed scan or a long-range interleaving construction. The blank
control completes an actual fresh interleaving; the signed20-cell control
tests a nontrivial long-distance ledger during its known returning lifetime.
"""
from pathlib import Path
from collections import defaultdict
import json,sys,hashlib
ROOT=Path('/workspace/shared/langton'); OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import rot,cursor,ends,sector,step

class Graph:
 def __init__(self,B,k):
  self.k=k;self.g=defaultdict(dict)
  for q in B:self.toggle(q,True)
 def toggle(self,q,add):
  a,b=ends(q,self.k)
  if add:self.g[a][b]=q;self.g[b][a]=q
  else:del self.g[a][b];del self.g[b][a]
 def comp(self,v):
  todo=[v];seen={v};C=set()
  for a in todo:
   for b,q in self.g[a].items():
    C.add(q)
    if b not in seen:seen.add(b);todo.append(b)
  return C
 def allcomps(self,B):
  remain=set(B);ans=[]
  while remain:
   q=min(remain);C=self.comp(ends(q,self.k)[0]);ans.append(C);remain-=C
  return ans

def named(name,B0,p0,h0,b,d,stop,helper,episodes=None):
 B=set(B0);p=p0;h=h0;k=sector(p,h);G=Graph(B,k)
 born={q:None for q in B};cohort=None;old=set();retired=[];M=0;snap={};special={}
 for t in range(stop+1):
  C=G.comp(cursor(p,h))
  if b<=t<=d:M=max(M,len(C))
  if t==b:
   assert p==helper and p not in B
   base=set(B);baseborn=dict(born);origin=p;cohort=dict(born);old=set(B)
  if episodes and t in [episodes['s']-1,episodes['s'],episodes['d']-1,episodes['d'],episodes['j'],episodes['c']]:
   special[str(t)]=dict(pose=[p,h],black=sorted(B),births=[[q,born[q]]for q in sorted(B)],active=sorted(C))
  if t==d:
   axis=max(range(2),key=lambda i:abs(p[i]-origin[i]));L=abs(p[axis]-origin[axis])
   strict=list(range(min(p[axis],origin[axis])+1,max(p[axis],origin[axis])))
   fresh={q for q in B if born[q]is not None and born[q]>=b}
   comps=G.allcomps(B);dorm=[A for A in comps if A!=C and A&fresh]
   assert all(len(A)<=M-1 for A in dorm)
   per=[]
   for r in strict:
    df={q for q in B^base if q[axis]==r}
    fr={q for q in fresh if q[axis]==r};rr=[z for z in retired if z['cell'][axis]==r]
    assert len(df)>=2 and len(fr)+len(rr)>=2
    per.append(dict(line=r,discrepancy=sorted(df),fresh=sorted(fr),retired=rr))
   K=sum(z['cell'][axis]in strict for z in retired)
   bound=max(0,2*len(strict)-K-M)
   nbound=(bound+M-2)//(M-1)if M>1 else 0
   assert len(fresh)>=2*len(strict)-K and len(dorm)>=nbound
   snap=dict(name=name,initial_black=sorted(B0),initial_pose=[p0,h0],b=b,d=d,
    helper=helper,axis=axis,distance=L,M=M,strict_lines=len(strict),old_retirements_on_lines=K,
    fresh_mass=len(fresh),active_fresh_mass=len(C&fresh),dormant_fresh_components=len(dorm),
    lower_bound_dormant_fresh_components=nbound,base_black=sorted(base),base_births=[[q,baseborn[q]]for q in sorted(base)],
    cut_pose=[p,h],cut_full_black=sorted(B),cut_births=[[q,born[q]]for q in sorted(B)],
    cut_active=sorted(C),dormant_fresh_component_fields=[dict(edges=sorted(A),fresh=sorted(A&fresh))for A in dorm],
    per_line=per,old_retirements=retired.copy(),helper_frozen_complete_component=sorted(G.comp(ends(helper,k)[0])))
  if t==stop:break
  q=p;c='L'if q in B else'R'
  if c=='L':
   if old and q in old:retired.append(dict(update=t,cell=q,birth_at_b=cohort[q]));old.remove(q)
   born.pop(q);G.toggle(q,False)
  else:born[q]=t;G.toggle(q,True)
  p,h=step(B,p,h)
 if episodes:
  es=episodes;s,j,c=es['s'],es['j'],es['c'];d0=es['d'];f=tuple(es['helper']);e=tuple(es['parent'])
  assert s<d0<=j<c
  for z in [s,d0]:assert f in {tuple(q)for q in special[str(z)]['black']}and f not in {tuple(q)for q in special[str(z)]['active']}
  assert f in {tuple(q)for q in special[str(s-1)]['active']}
  assert e in {tuple(q)for q in special[str(d0-1)]['active']}
  assert e not in {tuple(q)for q in special[str(d0)]['active']}
  assert tuple(special[str(j)]['pose'][0])==f and tuple(special[str(c)]['pose'][0])==e
  assert dict((tuple(q),a)for q,a in special[str(j)]['births'])[f]==es['helper_birth']
  assert dict((tuple(q),a)for q,a in special[str(c)]['births'])[e]==es['parent_birth']
  snap['completed_interleaving']=dict(**episodes,full_special_cuts=special,
   no_initial_black_cells=True,no_older_than_helper_consumption_during_s_through_c=True)
  # The only lifetime older than helper b1 is born0 and dies at4<s17.
  assert b==1 and all(z['birth_at_b']==0 and z['update']==4 for z in retired)
 return snap

blank=named('blank fresh interleaving regression',set(),(0,0),0,1,18,59,(1,0),
 dict(s=17,d=18,j=53,c=59,helper=(1,0),parent=(0,1),helper_birth=1,parent_birth=7))
n=400;G0={(0,-1),(1,1),(2,2),(1,3)}
poses=[((0,0),1),((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)]
B=set()
for p,h in poses:B|={(p[0]+v[0],p[1]+v[1])for q in G0 for v in[rot(q,(h-1)%4)]}
feedback=named('signed20-cell returning R60 lifetime, long excursion checkpoint',B,(0,0),1,60,52*n-173,52*n-173,(0,2))
feedback['next_actual_helper_consumption_from_retained_full_history']=624*n-1516
feedback['scope']='Checkpoint is NOT asserted to be a second completed parent episode; it tests the spatial lemma on a known actually returning lifetime. Initial old remote turns remain paid.'
out=dict(status='AUTHOR exact full-field spatial archive-ledger controls',controls=[blank,feedback],
 scope='Two named controls only. Blank interleaving is short-range;20-cell long-range checkpoint is not claimed to close a second parent episode. No arbitrary long fresh interleaving or global monotonicity is established.')
(OUT/'interleaving_spatial_archive_ledger_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([dict((k,z[k])for k in['name','b','d','distance','M','old_retirements_on_lines','fresh_mass','dormant_fresh_components','lower_bound_dormant_fresh_components'])for z in out['controls']],indent=2))
