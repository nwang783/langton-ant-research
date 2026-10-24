"""Targeted full-state lifetime placement measurement; no word/seed search."""
import sys
sys.path.insert(0,"/workspace/shared/langton/global_renewal_archive_2026-10-23")
from check_renewal_archive import *
OUT=Path(__file__).parent
from collections import deque

class FullGraph:
 def __init__(self,B,k):
  self.k=k;self.g={}
  for q in B:self.add(q)
 def add(self,q):
  u,v=endpoints(q,self.k);self.g.setdefault(u,{})[v]=q;self.g.setdefault(v,{})[u]=q
 def delete(self,q):
  u,v=endpoints(q,self.k);del self.g[u][v];del self.g[v][u]
 def nonbridge(self,q):
  s,t=endpoints(q,self.k);fs={s};ft={t};ss={s};st={t}
  # Exact two-front connectivity in the complete current graph minus q.
  while fs and ft:
   if len(fs)<=len(ft):
    nx=set()
    for v in fs:
     for u,e in self.g.get(v,{}).items():
      if e==q:continue
      if u in st:return True
      if u not in ss:ss.add(u);nx.add(u)
    fs=nx
   else:
    nx=set()
    for v in ft:
     for u,e in self.g.get(v,{}).items():
      if e==q:continue
      if u in ss:return True
      if u not in st:st.add(u);nx.add(u)
    ft=nx
  return False

def produce(which,N):
 U=ROOT/'causal_reduction/unit_scale';sys.path.insert(0,str(U))
 if which==1564:
  import check1564_noncrossing_producer as mod
  R=100+28*N;p,B,segs,_=mod.setup(R,N);h=3
 else:
  import check4352_noncrossing_producer as mod
  R=200+52*N;p,B,segs,_=mod.setup(R,N);h=3
 seedmass=len(B);prep=0
 for s in segs:
  assert[p,h]==s['start']
  if s['kind']=='wave':return B,p,h,mod.W,R,seedmass,prep
  word=mod.H*s['count']if s['kind']=='H'else s['word']
  for c in word:
   assert ('L'if p in B else'R')==c
   p,h=step(B,p,h);prep+=1
 raise AssertionError

def measure(name,B0,p,h,W,N,context=None):
 B=set(B0);k=wwhich(p,h);G=FullGraph(B,k);Gz=FullGraph(B,1-k);birth={q:None for q in B};r=0;events=[];per=[]
 oldall=oldE=oldD=0
 for t in range(len(W)*N):
  c=W[t%len(W)];assert ('L'if p in B else'R')==c,(name,t,p,h,c)
  q=p
  if c=='R':
   r+=1;birth[q]=t;G.add(q);Gz.add(q)
  else:
   wn=G.nonbridge(q);zn=Gz.nonbridge(q);ex=r>=3 or wn
   age=None if birth[q]is None else t-birth[q]
   oldall+=age is None;oldE+=ex and age is None;oldD+=(wn or zn)and age is None
   events.append({'t':t,'period':t//len(W),'slot':t%len(W),'r':r,'wn':wn,'zn':zn,'E':ex,'birth':birth[q],'age':age,'cell':q})
   G.delete(q);Gz.delete(q);del birth[q];r=0
  p,h=step(B,p,h)
  if (t+1)%len(W)==0:
   es=[e for e in events if e['period']==t//len(W)]
   E=[e for e in es if e['E']];D=[e for e in es if e['wn']or e['zn']]
   per.append({'period':t//len(W),'mass':len(B),'L':len(es),'E':len(E),'D':len(D),'input_L':sum(e['birth']is None for e in es),'input_E':sum(e['birth']is None for e in E),'input_D':sum(e['birth']is None for e in D),'E_max_newborn_age':max([e['age']for e in E if e['age']is not None]or[0]),'input_E_slots':[e['slot']for e in E if e['birth']is None],'input_wn_slots':[e['slot']for e in E if e['wn']and e['birth']is None],'input_E_r_counts':{str(x):sum(e['r']==x and e['birth']is None for e in E)for x in(0,1,2,3,4)}})
 return {'name':name,'context':context,'initial_mass':len(B0),'N':N,'period':len(W),'per_period':per,'events':events,'final_pose':[p,h],'final_mass':len(B),'input_L':oldall,'input_E':oldE,'input_D':oldD}

if __name__=='__main__':
 out=[]
 S=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())
 out.append(measure('standard104_seed13',{tuple(q)for q in S['seed']},(0,0),S['heading'],S['word'],6))
 for which in(1564,4352):
  N=3;B,p,h,W,R,sm,prep=produce(which,N)
  out.append(measure('actual_prepared_wave_'+str(which),B,p,h,W,N,{'R':R,'original_seed_mass':sm,'preparation_steps':prep}))
 result={'scope':__doc__,'runs':out}
 (OUT/'renewal_input_age_probe.json').write_text(json.dumps(result,indent=2)+'\n')
 for run in out:print(json.dumps({k:v for k,v in run.items()if k!='events'},indent=2),flush=True)
