from pathlib import Path
import json,hashlib,heapq
from check_return_permanent_output_debt import DXY,rot,future
P=Path(__file__).parent;G={(0,-1),(1,1),(1,3),(2,2)};source=json.loads((P/'TRANSVERSE_FAR_MODULE_SOURCE.json').read_text());B=set(G);p=(0,0);h=1;word='';firstG={};posesG=[]
for t in range(286):
 posesG.append((p,h))
 if p in G and p not in firstG:firstG[p]=t
 old=p in B
 if old:B.remove(p);h=(h-1)%4
 else:B.add(p);h=(h+1)%4
 word+='L'if old else'R';p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
A,U=word[:182],word[182:];assert posesG[59]==((1,2),2)and sorted(firstG.values())==[1,22,32,58];records=[]
for n in (20,40,80):
 k=n//2;poses=[((0,0),1),((7*n-1,7*n),0),((5*n,9*n-4),3),((n+5,5*n),2)];seed={ (o[0]+rot(g,h-1)[0],o[1]+rot(g,h-1)[1])for o,h in poses for g in G};R=[7*k-4,2*k-5,4*k-6,2*k-6];part=[61,71,61,56];entries=[0]
 for i in range(3):entries.append(entries[-1]+182+104*R[i]+part[i])
 T=676*n-762;c=780*n-1207;b=156*n-59;q=(3*n,3*n+3);assert entries[3]+59==T
 seq=''.join(A+U*R[i]+U[:part[i]]for i in range(4))+source['post_contact_word']+U*2;B={v:-i-1 for i,v in enumerate(sorted(seed))};p=(0,0);h=1;births={};deaths={};reads=[];events=[];first={};snap={};allpos=[]
 for t,ch in enumerate(seq):
  allpos.append(p)
  if t in(T-1,T,T+1):snap[t]=(dict(B),p,h)
  if p in seed and p not in first:first[p]=t
  old=B.pop(p,None);assert (old is None)==(ch=='R');events.append(old);reads.append(p)
  if old is None:B[p]=t;births[t]=p;h=(h+1)%4
  else:deaths[old]=t;h=(h-1)%4
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 allpos.append(p);w,dr,tail,tests=future(B,p,h);assert w==U and dr==(2,-2);deaths.update({i:len(seq)+t for i,t in tail.items()})
 for i,(o,hh)in enumerate(poses):
  for g in G:
   z=rot(g,hh-1);v=(o[0]+z[0],o[1]+z[1]);assert first[v]==entries[i]+firstG[g]
 assert max(first.values())==T-1 and all(deaths[-i-1]==first[v]for i,v in enumerate(sorted(seed)))
 BT,pt,ht=snap[T];assert pt==(n+7,5*n-1)and ht==3 and BT[q]==b and deaths[b]==c
 # Exact whole-future relevance, with lazy extrema heaps; no local cropping.
 live={-i-1:v for i,v in enumerate(sorted(seed))};heaps=[[],[],[],[]]
 def addlife(i,v):
  live[i]=v
  for heap,val in zip(heaps,[v[0],-v[0],v[1],-v[1]]):heapq.heappush(heap,(val,i))
 for i,v in list(live.items()):addlife(i,v)
 def radius(head):
  if not live:return 0
  vals=[]
  for heap in heaps:
   while heap[0][1]not in live:heapq.heappop(heap)
   vals.append(heap[0][0])
  return max(abs(vals[0]-head[0]),abs(-vals[1]-head[0]),abs(vals[2]-head[1]),abs(-vals[3]-head[1]))
 profile=[];prev=None;maxpop=0
 for t,head in enumerate(allpos):
  rho=radius(head);maxpop=max(maxpop,len(live))
  if prev is not None:assert abs(rho-prev)<=1
  prev=rho
  if t in(T-1,T,T+1):profile.append(dict(cut=t,rho=rho,whole_relevant_mass=len(live),whole_relevant=sorted(live.values())))
  if t==len(seq):break
  old=events[t]
  if old is None:
   if t in deaths:addlife(t,reads[t])
  else:assert old in live;del live[old]
 assert maxpop==432 and profile[1]['rho']>=2*n-4
 assert set(profile[1]['whole_relevant'])=={v for v,i in BT.items()if i in deaths}
 records.append(dict(n=n,seed=sorted(seed),port_entries=entries,original_first_reads=[dict(cell=v,time=first[v])for v in sorted(seed)],cohort_complete_cut=T,complete_cut_pose=[pt,ht],marker=dict(cell=q,birth=b,death=c,distance=2*n-4,remaining_wait=c-T),complete_cut_full_field=[dict(cell=v,lifetime=i,death=deaths.get(i))for v,i in sorted(BT.items())],near_renewal_radius=profile,physical_reads=len(seq),all_finite_radius_updates_checked=len(seq),full_tail_parity_tests=tests,max_relevant_mass=maxpop))
 print(n,'renewal',T,pt,ht,'rho',[a['rho']for a in profile],'population',profile[1]['whole_relevant_mass'],'marker',2*n-4,flush=True)
# The NON-ANT temporal cover countermodel, for exact formula regression only.
interval_tests=[]
for m in(2,3,10,100):
 vals=[]
 for t in range(m*m,(m+1)*(m+1)):
  liveidx=[j for j in(m-1,m)if j*j+1<=t<=(j+2)*(j+2)-1]
  depth=max(min(t-j*j,(j+2)*(j+2)-1-t)for j in liveidx);assert depth>=m and len(liveidx)<=2;vals.append(depth)
 interval_tests.append(dict(m=m,min_two_sided_depth=min(vals),max_population=2))
out=dict(status='AUTHOR exact radius evolution and cohort-renewal countercontrol; independent audit requested',scope='One-step rho lemma and all-n retirement formula use exact C* and signed source. Named controls verify full futures. No universal orbit-dependent recurrence failure. Interval system is explicitly NON-ANT and only refutes a temporal nesting inference.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in ['TRANSVERSE_FAR_MODULE_MANIFEST.json','TRANSVERSE_FAR_MODULE_SOURCE.json','TRANSVERSE_PERMANENT_BUDGET_MANIFEST.json']},source59_pose=posesG[59],source_initial_first_reads=[dict(cell=v,time=t)for v,t in sorted(firstG.items())],all_n_retirement=dict(cut='676n-762',head='(n+7,5n-1),W',marker_distance='2n-4',marker_remaining_wait='104n-445',population_cap=432),controls=records,non_ant_interval_regressions=interval_tests)
(P/'RELEVANT_RADIUS_RENEWAL_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
