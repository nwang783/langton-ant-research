"""Bounded exact search, not a no-highway theorem."""
import json,time,sys
from pathlib import Path
W={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'}
N=int(sys.argv[1]);CAP=int(sys.argv[2]);start=time.time();dirs=(1j,1,-1j,-1)
def tr(w):
 p=0j;h=0;f={};l={};reads=[]
 for t,c in enumerate(w):
  if l.get(p)==c:return None
  f.setdefault(p,c);l[p]=c;reads.append((p,c,t));h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
 return f,l,p,h,reads
M={a:tr(w)for a,w in W.items()};last={};nodes=0;tested=0;hits=[];stopped=False;levels=[0]*(N+1)
def stable(word,d):
 reads=tr(word)[4];groups=[]
 for p,c,t in reads:
  for r,items in groups:
   z=(p-r)/d
   if abs(z.imag)<1e-8 and abs(z.real-round(z.real))<1e-8:
    items.append((int(round(z.real)),t,c));break
  else:groups.append((p,[(0,t,c)]))
 seed=[]
 for r,g in groups:
  g.sort(key=lambda z:(-z[0],z[1]));letters=[c for k,t,c in g]
  if letters[0]!='R' or any(a==b for a,b in zip(letters,letters[1:])):return None
  for j in range(min(z[0]for z in g),max(z[0]for z in g)):
   s=next(c for k,t,c in g if k<=j)
   if s=='L':
    p=r+j*d;seed.append((int(p.real),int(p.imag)))
 return sorted(set(seed))
def dfs(s,p,h):
 global nodes,tested,stopped
 nodes+=1;levels[len(s)]+=1
 if nodes>=CAP:stopped=True;return
 if s and h==0 and p and 'C'in s and s.count('C')%4==0:
  rots=[s[i:]+s[:i]for i in range(len(s))if s[i]=='D']
  if s==min(rots):
   tested+=1;w=''.join(W[a]for a in s);seed=stable(w,p)
   if seed is not None:
    hit={'macros':s,'turns':len(w),'drift':[int(p.real),int(p.imag)],'seed':seed};hits.append(hit);print('HIT',hit,flush=True)
 if len(s)==N:return
 for a in 'DCV':
  if not s and a!='D':continue
  f,l,d,dh,reads=M[a];r=(-1j)**h;up={p+x*r:c for x,c in f.items()}
  if any(q in last and last[q]==c for q,c in up.items()):continue
  old={p+x*r:last.get(p+x*r)for x in l}
  for x,c in l.items():last[p+x*r]=c
  dfs(s+a,p+d*r,(h+dh)%4)
  for q,c in old.items():
   if c is None:del last[q]
   else:last[q]=c
  if stopped:return
dfs('',0j,0)
out={'max_macros':N,'node_cap':CAP,'nodes':nodes,'levels':levels,'tested_cycles':tested,'stopped':stopped,'hits':hits,'seconds':time.time()-start,'scope':'Bounded exact physical periodic-word search; no all-period conclusion.'}
Path('dcv_periods_'+str(N)+'.json').write_text(json.dumps(out,indent=2));print(out)
