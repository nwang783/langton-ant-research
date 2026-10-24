"""Exact guarded-XOR synthesis of a periodic changing-state corner.
The whole proposed rectangular trajectory would be aperiodic (growing lap
lengths). This solves only the infinite-arm local corner, not the seam or
all-field global construction. UNKNOWN caps are explicit.
"""
from periodic_corner_states import *
from loop_decoration_solver import solve

def build(ks,q=4,clean=False,black=None):
 data=[walk(K) for K in ks];ends=[e for ev,e in data];assert len(set(ends))==1 and ends[0][2]==1
 a,b,h=ends[0];span=[0,a+b-1]+[x+y for ev,en in data for (x,y),h,c in ev];lo=min(span);hi=max(span)
 es=defaultdict(list);m=len(ks);N=m*q
 for k in range(q):
  def add(x,y,phase,c,var):es[(x+y,(x-k)%q)].append(((x-k,k)+phase,c,var))
  for j,(ev,en) in enumerate(data):
   var=k*m+j
   for i,((x,y),h,c) in enumerate(ev):add(x,y,(1,j,i),c,var)
  for s in range(lo,hi+1):
   if s<=0:
    y=s-1;add(1,y,(0,0,4*(y//2)+(1 if y%2==0 else 2)),'L',None)
    if s<0:
     y=s;add(0,y,(0,0,4*(y//2)+(0 if y%2==0 else 3)),'R',None)
   if s>=a+b-1:
    x=s-b+1;j=x-a;add(x,b-1,(2,0,4*(j//2)+(1 if j%2==0 else 2)),'L',None)
    if s>=a+b:
     x=s-b;j=x-a;add(x,b,(2,0,4*(j//2)+(0 if j%2==0 else 3)),'R',None)
 eq=[];g=[[] for _ in range(N)]
 for cl,events in es.items():
  events.sort();mask=0;bit=int(black is not None and cl in black)
  for t,c,var in events:
   row=(mask,bit^(c=='L'))
   if var is None:eq.append(row);bit^=1
   else:g[var].append(row);mask^=1<<var
  if clean:eq.append((mask,bit))
 for k in range(q):
  ids=list(range(k*m,(k+1)*m));eq.append((sum(1<<v for v in ids),1))
  for v in ids:
   for z in ids:
    if v!=z:g[v].append((1<<z,0))
 return eq,g

if __name__=='__main__':
 maxlen=int(sys.argv[1]) if len(sys.argv)>1 else 17;q=int(sys.argv[2]) if len(sys.argv)>2 else 4
 clean=bool(int(sys.argv[3])) if len(sys.argv)>3 else True
 e,g=build(['RLR'],1,False,{(1,0)});z,ans=solve(e,g,False,timeout=2);assert z['status']=='SAT' and ans==[1]
 e,g=build(['RLR'],1);z,ans=solve(e,g,False,timeout=2);assert z['status']=='UNSAT'
 byend=defaultdict(list);start=time.time()
 for K,end in words(maxlen,heading=1):
  if feasible(S*(2*maxlen)+K+S*(2*maxlen)):byend[end].append(K)
 out=[]
 for end,ks in sorted(byend.items(),key=lambda z:len(z[1])):
  e,g=build(ks,q,clean);z,ans=solve(e,g,False,limit=100000,timeout=10)
  r=dict(end=end,options_per_phase=len(ks),solver=z)
  if ans is not None:
   selected=[]
   for k in range(q):
    on=[j for j in range(len(ks)) if ans[k*len(ks)+j]];assert len(on)==1;selected.append(ks[on[0]])
   c=check_sequence(selected);assert c['valid'];assert not clean or not c['odd_classes'];r.update(caps=selected,check=c)
  out.append(r);print('PORT',json.dumps(r),flush=True)
  (HERE/f'corner_cycle_{q}_cap{maxlen}_clean{int(clean)}.json').write_text(json.dumps(dict(maxlen=maxlen,q=q,clean=clean,seconds=time.time()-start,ports=out),indent=2))
 print('DONE',len(out),dict(__import__('collections').Counter(r['solver']['status'] for r in out)),time.time()-start,flush=True)
