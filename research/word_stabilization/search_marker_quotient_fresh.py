import json,sys,time,random
from pathlib import Path
from collections import defaultdict,Counter
prefix=sys.argv[1];depthlim=int(sys.argv[2]);cap=int(sys.argv[3]);Q=json.load(open(prefix+'_port_quotient.json'));M=Q['macro_words'];A=defaultdict(list)
for u,a,v in Q['quotient_edges']:A[u].append((a,v))
D=(1j,1,-1j,-1);T=[];S={};witness=[];seen_counts=Counter();start=time.time()
def trace(w):
 p=0j;h=0;f={};l={}
 for t,c in enumerate(w):
  assert l.get(p)!=c;f.setdefault(p,(c,t));l[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return f,l,p,h
for a,z in enumerate(M):
 f,l,p,h=trace(z['word']);ff,_,_,_=trace(z['word']+z['end_marker']);S[a]={q for q,(c,t)in f.items()if c=='L'};T.append([(tuple((q*(-1j)**r,c)for q,(c,t)in ff.items()),tuple((q*(-1j)**r,c)for q,c in l.items()),p*(-1j)**r,h)for r in range(4)])
N=0;stop=False;word=[];field={}
def dfs(state,p,h):
 global N,stop
 N+=1
 if N>cap:stop=True;return
 if len(word)>=depthlim:return
 for a,dest in A[state]:
  f,l,dp,dh=T[a][h]
  if any(field.get(p+q)==c for q,c in f):continue
  seen_counts[a]+=1;lost={q for q in S[a]if p+q*(-1j)**h in field}
  if lost:
   witness.append({'macro':a,'sites':sorted((int(q.real),int(q.imag))for q in lost),'word':word+[a]});S[a]-=lost;print('LOST',a,len(lost),'left',len(S[a]),'word',word+[a],flush=True)
  undo=[]
  for q,c in l:q+=p;undo.append((q,field.get(q)));field[q]=c
  word.append(a);dfs(dest,p+dp,(h+dh)%4);word.pop()
  for q,c in undo:
   if c is None:del field[q]
   else:field[q]=c
  if stop:return
for state in sorted(A):
 dfs(state,0j,0)
 if stop:break
out={'depth':depthlim,'cap':cap,'nodes':N,'complete':not stop,'seconds':time.time()-start,'survivors':{str(a):sorted((int(q.real),int(q.imag))for q in ss)for a,ss in S.items()},'observed':dict(seen_counts),'witnesses':witness};Path(prefix+'_fresh_search.json').write_text(json.dumps(out,indent=2));print('DONE',N,not stop,'survivors',out['survivors'],flush=True)
