#!/usr/bin/env python3
"""Positive model construction for one supplied interval order, not exhaustion."""
import json,re,math
from pathlib import Path
R=Path(__file__).resolve().parent
q=json.load(open(R/'return_debt_interval_calendar_result.json'));v={k:(-int(s[3:-1])if s.startswith('(-')else int(s))for k,s in re.findall(r'([xsz]\d+) -> (\(- \d+\)|-?\d+)',q['model'])};P=q['period_parameter'];chs=q['chains'];lev=q['levels'];H={int(t):h for t,h in q['histories'].items()};D=((0,1),(1,0),(0,-1),(-1,0));n=len(chs);where={}
for c,ch in enumerate(chs):
 for a,((i,j),k)in enumerate(ch):where[lev[i],j]=(c,a,k)
rank=[]
for t,hs in H.items():
 for j in range(len(hs)-1):
  u,a,ka=where[t,j];w,b,kb=where[t,j+1];rank.append((u,w,4+a-b,kb-ka))
def ceildiv(a,b):return -((-a)//b)
def BF(E,N):
 dist=[0]*N
 for it in range(N):
  changed=False
  for u,w,b in E:
   if dist[w]<dist[u]+b:dist[w]=dist[u]+b;changed=True
  if not changed:return dist
 return None
# Preserve first model phases, minimize the integer lifts by exact difference constraints.
s=[v['s'+str(c)]for c in range(n)];rz=[v['z'+str(c)]%2 for c in range(n)];E=[]
for u,w,C,K in rank:
 b=K+ceildiv(C+s[u]-s[w],P);E.append((u,w,ceildiv(b-rz[w]+rz[u],2)))
y=BF(E,n);assert y is not None;z=[2*(yy-y[0])+rr for yy,rr in zip(y,rz)];assert z[0]==0
assert all((s[w]+z[w]*P)-(s[u]+z[u]*P)>=C+K*P for u,w,C,K in rank)
order=sorted(range(n),key=lambda c:s[c]);rs=[(lev[chs[c][0][0][0]]%2-2*z[c])%4 for c in range(n)];E=[]
def edge(u,w,b):E.append((u,w,ceildiv(b-rs[w]+rs[u],4)))
for u,w,C,K in rank:edge(u,w,C+(K-z[w]+z[u])*P)
travel=[]
from collections import deque
def padded_path(ps,h0,pe,h1):
 def safe_loop(p,h):
  for sg in(-1,1):
   qq=p;hh=h;ok=True
   for _ in range(4):
    hh=(hh+sg)%4;qq=(qq[0]+D[hh][0],qq[1]+D[hh][1]);ok &= 3*qq[1]-qq[0]>=13
   if ok:return sg
  return None
 root=(ps,h0,safe_loop(ps,h0)is not None);prev={root:None};Q=deque([root]);depth={root:0}
 while Q:
  at=Q.popleft();p,h,flag=at
  if p==pe and(h-h1)%2==1 and flag:
   path=[]
   while at is not None:path.append(at);at=prev[at]
   return path[::-1]
  assert depth[at]<120, 'positive connector search limit reached; no exclusion'
  for hh in((h-1)%4,(h+1)%4):
   pp=(p[0]+D[hh][0],p[1]+D[hh][1])
   if 3*pp[1]-pp[0]<13:continue
   nxt=(pp,hh,flag or safe_loop(pp,hh)is not None)
   if nxt not in prev:prev[nxt]=at;depth[nxt]=depth[at]+1;Q.append(nxt)
for c,b in zip(order,order[1:]+order[:1]):
 wrap=int(b==order[0]);ch=chs[c];nxt=chs[b];(i,j),k=ch[-1];t=lev[i];h0=(H[t][j]+(1 if j%2==0 else-1))%4;(ii,jj),kk=nxt[0];tt=lev[ii];h1=H[tt][jj]
 pc=(-t+3*k-3*z[c],k-z[c]);pb=(-tt-3*z[b]+3*wrap,-z[b]+wrap);delta=tuple(pb[a]-pc[a]for a in range(2));r=tuple(delta[a]-D[h0][a]-D[h1][a]for a in range(2));first_remaining_axis=(h0+1)%2
 need=max(2,*[2+2*abs(r[a])-int(first_remaining_axis==(1 if a==0 else 0))for a in range(2)])
 ps=(pc[0]+D[h0][0],pc[1]+D[h0][1]);pe=(pb[0]-D[h1][0],pb[1]-D[h1][1]);path=padded_path(ps,h0,pe,h1);need=max(need,len(path)+1)
 edge(c,b,len(ch)-1+need-wrap*P);travel.append({'source_chain':c,'target_chain':b,'wrap':wrap,'delta':delta,'required_minimum':need,'geometric_unknown_region_path':path})
# Bounds with a zero-reference node.
E0=[]
for u,w,b in E:E0.append((u,w,b))
for c,ch in enumerate(chs):
 E0.append((n,c,ceildiv(-rs[c],4)));E0.append((c,n,ceildiv(rs[c]-(P-len(ch)),4)))
E0 += [(n,0,0),(0,n,0)]
y=BF(E0,n+1)
result={'scope':__doc__,'period':P,'fixed_order':order,'reduced_lifts':z,'phase_residues':rs,'status':'NO_MODEL_FOR_THIS_FIXED_LIFT_AND_ORDER'if y is None else'EXPLICIT_NAMED_CLOCK_AND_TRAVEL_MODEL'}
if y is not None:
 s=[4*(y[c]-y[n])+rs[c]for c in range(n)];x=[s[c]+z[c]*P for c in range(n)];result.update({'phases':s,'canonical_chain_starts':x,'travel_obligations':travel,'source_histories':H,'chains':chs,'levels':lev})
 for u,w,C,K in rank:assert x[w]-x[u]>=C+K*P
 for o in travel:o['actual_distance']=s[o['target_chain']]+o['wrap']*P-s[o['source_chain']]-(len(chs[o['source_chain']])-1);assert o['actual_distance']>=o['required_minimum']
 print('SAT explicit',z,s)
else:print('fixed-lift-and-order fails',z)
(R/'return_debt_halfplane_clock_result.json').write_text(json.dumps(result))
