"""Complete fixed-launch-end limit after the connected15324 return phase.
All past launch modifications and both nonstandard wave fields are retained.
The original moving router/source fields are replaced only in this separately
stated prepared limit, not silently discarded from a finite-seed claim.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,math,time
from check4352_noncrossing_producer import H,W,V,L,J
from check_prepared1564_router_geometry import trace
P=Path(__file__).resolve().parent
A=json.loads((P/'prepared4352_output_return_wave.json').read_text())
def key(q):return q[0]-q[1],q[0]%78
def z(q):return q[0]//78
class RayBoard:
 def __init__(self):self.full=set();self.rays=defaultdict(set);self.F=set()
 def toggle(self,q):self.F.symmetric_difference_update({q})
 def lower(self,q):
  k=key(q);self.full.symmetric_difference_update({k});self.rays[k].symmetric_difference_update({z(q)-1})
 def color(self,q):return(key(q)in self.full)^(sum(z(q)<=a for a in self.rays.get(key(q),()))%2)^(q in self.F)
 def manifest(self):return{'modulus':78,'full':sorted(self.full),'upper_rays':[[list(k),sorted(a)]for k,a in sorted(self.rays.items())if a],'finite_xor':sorted(self.F)}
def build():
 b=RayBoard();groups=defaultdict(list)
 for i,q,h,c in list(trace(L['inverse_tail_word'],tuple(L['inverse_tail_pose'][0]),L['inverse_tail_pose'][1]))[:-1]:
  groups[q[0]-q[1],q[0]%2].append((i-104*(q[0]//2),q[0]//2,c))
 for(t,a),g in groups.items():
  g.sort();mn=min(x[1]for x in g);mx=max(x[1]for x in g)
  for n in range(mn,mx):
   f=next(x for x in g if x[1]<=n)
   if f[2]=='L':b.toggle((a+2*n,a+2*n-t))
  if g[0][2]=='L':
   for r in range(39):b.lower((a+2*(mx+r),a+2*(mx+r)-t))
 other={tuple(q)for q in L['other_full_black_profiles']}
 # Add both retained exterior helper profiles, not only the useful bands.
 for t,a,h in[J['lanes'][i]for i in(1,3)] if 'lanes'in J else []:pass
 for t,a,h in[(89,0,1),(-57,0,1)]:
  pp=(a,a-t);counts=Counter((q[0]-q[1],q[0]%2)for _,q,hh,c in list(trace(H,pp,h))[:-1]);other|={j for j,n in counts.items()if n%2}
 for t,a in other:
  for r in range(a,78,2):b.full.symmetric_difference_update({(t,r)})
 for q in L['fresh_cap']:b.toggle(tuple(q))
 for _,q,h,c in list(trace(L['forward_prelude_word'],tuple(L['forward_entry_pose'][0]),L['forward_entry_pose'][1]))[:-1]:b.toggle(q)
 for _,q,h,c in list(trace(W,(-2,3),3))[:-1]:
  for r in range(3):b.lower((q[0]+26*r,q[1]+26*r))
 for _,q,h,c in list(trace(A['word'],(117,111),0))[:-1]:b.lower((q[0]+78,q[1]+78))
 return b
# Reuse the elementary ray-tail proof with its globals bound to this modulus.
from probe4352_source_endpoint_limit import mult

def first_bad(b,p,h,w):
 rr=list(trace(w,p,h));d=rr[-1][1][0]-p[0],rr[-1][1][1]-p[1];assert rr[-1][2]==h
 slots=[x[1]for x in rr[:-1]];answer=None
 for i,q in enumerate(slots):
  th=[]
  for j,qq in enumerate(slots):
   k=mult((qq[0]-q[0],qq[1]-q[1]),d)
   if k is not None and(k>0 or k==0 and j<i):th.append(k)
  tests={0}
  if d[0]==d[1]:
   per=78//math.gcd(abs(d[0]),78);tests.update(range(per))
   for k in th:tests.update(range(k,k+per))
   for r in range(per):
    qq=q[0]+r*d[0],q[1]+r*d[1];slope=per*d[0]//78
    for cut in b.rays.get(key(qq),()):
     k=(cut-z(qq))//slope
     for kk in(k-1,k,k+1):
      if kk>=0:tests.add(r+per*kk)
  else:
   tests.update(th);dt=d[0]-d[1];qt=q[0]-q[1]
   for t,a in b.full|set(b.rays):
    if(t-qt)%dt==0:
     k=(t-qt)//dt
     if k>=0:tests.update((k,k+1))
  for qq in b.F:
   k=mult((qq[0]-q[0],qq[1]-q[1]),d)
   if k is not None and k>=0:tests.update((k,k+1))
  for k in sorted(tests):
   qq=q[0]+k*d[0],q[1]+k*d[1]
   if(b.color(qq)^(sum(a<=k for a in th)%2))!=(w[i]=='L'):
    v=k*len(w)+i;answer=v if answer is None else min(answer,v);break
 return answer,d

def main():
 b=build();initial=b.manifest();p=(117,111);h=0;word=[];events=[];recent='';rot={H[i:]+H[:i]for i in range(104)};st=time.time()
 def step():
  nonlocal p,h,recent
  c='L'if b.color(p)else'R';b.toggle(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1]);word.append(c);recent=(recent+c)[-208:];return c
 # Check the supplied actual prefix all the way to first launch-bit contact.
 target=A['word']+A['word'][:2029]
 for c in target:assert step()==c
 assert(p,h)==((14,-7),3)and b.color(p);print('same launch-bit contact',len(word),p,h,flush=True)
 while len(word)<1000000:
  if len(recent)==208 and recent[:104]==recent[104:]and recent[104:]in rot:
   w=recent[104:];bad,d=first_bad(b,p,h,w);e={'offset':len(word),'pose':[p,h],'word':w,'first_bad':bad,'drift':d};events.append(e);print(e,flush=True)
   if bad is None:break
   for i in range(bad):assert step()==w[i%104]
   step();recent='';continue
  step()
 out={'scope':__doc__,'initial_board':initial,'word':''.join(word),'events':events,'final_pose':[p,h],'final_finite_xor':sorted(b.F),'status':'EXACT_PREPARED_STANDARD_TAIL'if events and events[-1]['first_bad']is None else'DISCOVERY_LIMIT','seconds':time.time()-st}
 (P/'prepared4352_return_end_limit.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(word),time.time()-st,flush=True)
if __name__=='__main__':main()
