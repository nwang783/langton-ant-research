from pathlib import Path
from itertools import combinations,product
from collections import Counter,defaultdict,deque
import json,hashlib,ast
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'even_portal_uncapped_outer_readers_retain_deep_stock_shields.md':'ab849f2a1dcd377612bfb2f56a100b3619b37b95a5afa81b068b0a3149300110','check_even_portal_uncapped_outer_shields.py':'4208bf2da150a6c80029e6bc52290d273ba2871e43b7ab2b1bc2872860ee9223','check_even_portal_uncapped_outer_shields.json':'f522e2e2b2165b258099cad75f8d3cd3a35f5924fafee48a9c1a374c70f69762'}
for f,h in files.items():assert sha(D/f)==h
ref=json.loads((D/'check_even_portal_uncapped_outer_shields.json').read_text());lib=S.with_name('check_terminal_LL_upper_completion_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('ct1=Counter()')[0],ns);cv,string,V,out,test,physical,ev=[ns[k]for k in('cv','string','V','out','test','physical','ev')]
def dom(a,b,n,k):
 for pos in combinations(range(n),k):
  pos=set(pos);yield tuple(a if i in pos else b for i in range(n))
Ls=[w for n in range(2,9)for w in dom(3,1,n,2)if sum(out(w,j)==2 for j in range(n))==2]
assert set(map(string,Ls))==set(ref['L_domain'])and len(Ls)==18
Ks={m:[w for n in range(2,2*(2+m)+2)for w in dom(0,2,n,2)if sum(out(w,j)==1 for j in range(n))==m]for m in{w.count(1)for w in Ls}}
assert {m:len(w)for m,w in Ks.items()}=={1:9,2:22,5:106,6:150}
assert all(set(map(string,w))==set(ref['K_domains'][str(m)])for m,w in Ks.items())
# Verify count identities on the entire derived domains, not a selected sample.
for w in Ls:
 rw=sum(w[j]==3 for j in range(0,len(w),2));lw=sum(w[j]==3 for j in range(1,len(w),2));re=sum(w[j]==1 for j in range(0,len(w),2));assert rw==re==2-lw and len(w)<=8
for m,ws in Ks.items():
 for w in ws:
  a=sum(w[j]==0 for j in range(0,len(w),2));b=sum(w[j]==0 for j in range(1,len(w),2));c=sum(w[j]==2 for j in range(0,len(w),2));d=sum(w[j]==2 for j in range(1,len(w),2));ep=len(w)%2
  assert a+b==2 and a+d==m and c==2+m-3*a+ep and len(w)==2*(2+m-2*a)+ep
prior=json.loads((D/'check_terminal_LL_upper_side_collision.json').read_text());tops=[tuple(map(cv,z))for z in prior['Q_square_modes']]
opened={(z['R'],z['U'],z['W'],z['L'],z['K']):z for z in ref['open']};ct=Counter();per=Counter();matched=set();sizes=[];ranks=Counter();clocks=Counter();higher=[]
for (rr,uu,ww),ll in product(tops,Ls):
 for kk in Ks[ll.count(1)]:
  hs={-2-1j:cv('EEWW'),-1-1j:cv('SNNS'),-1j:cv('WWEE'),1-1j:rr,0j:uu,1+0j:ww,-1+0j:ll,-2+0j:kk};ans,wit=test(hs);typ={'skipped':'rank','global_max':'higher_C'}.get(ans,ans);ct[typ]+=1;key=tuple(map(string,(rr,uu,ww,ll,kk)));per[str((key[:3],typ))]+=1
  su,edges=physical(hs)
  if typ=='rank':
   assert all(su[a]==b for a,b in zip(wit,wit[1:]));assert wit[-1][0]==wit[0][0]and wit[-1][1]!=wit[0][1]+1;ranks[len(wit)-1]+=1
  elif typ=='clock':
   assert sum(z[2]for z in wit)>0;assert all(any(e[:3]==z for e in edges)for z in wit);clocks[sum(z[2]for z in wit)]+=1
  elif typ=='higher_C':assert wit[1]>0;higher.append([key,wit])
  elif typ=='open':
   assert key in opened;z=opened[key];matched.add(key);assert {complex(*ast.literal_eval(p)):cv(w)for p,w in z['histories'].items()}==hs
   certsu={ev(a):ev(b)for a,b in z['certificate']['successor_edges']};assert su==certsu
   cal=z['finite_event_calendar'];times={ev(e):t for e,t in cal['times']};events={(p,j)for p,w in hs.items()for j in range(len(w))};assert set(times)==events and len(set(times.values()))==len(events)
   assert all(times[b]==times[a]+1 for a,b in su.items());assert all(times[p,j+1]>=times[p,j]+4 for p,w in hs.items()for j in range(len(w)-1))
   phase=lambda p:2*(int(p.real)%2)if int(p.real+p.imag)%2==0 else 3-2*(int(p.real)%2)
   assert all(t%4==phase(p)for(p,j),t in times.items())
   comps=[[ev(e)for e in c]for c in cal['components']];assert set(sum(comps,[]))==events and sum(map(len,comps))==len(events);assert sorted(cal['order'])==list(range(len(comps)))
   for c in comps:
    assert c[0]not in set(su.values())and c[-1]not in su and all(su[a]==b for a,b in zip(c,c[1:]))
   for a,b in zip(cal['order'],cal['order'][1:]):assert max(times[e]for e in comps[a])<min(times[e]for e in comps[b])
   # Independently integrate the complete radial stream, including zero ports.
   adj=defaultdict(list)
   for p,w in hs.items():
    for h,v in enumerate(V):
     rt=p+v/2-1j*v/2;lt=p+v/2+1j*v/2;delta=sum(out(w,j)==h for j in range(len(w)))-w.count((h+2)%4);adj[lt].append((rt,delta));adj[rt].append((lt,-delta))
   vals={.5-.5j:0};queue=deque(vals)
   while queue:
    p=queue.popleft()
    for q,d in adj[p]:
     if q in vals:assert vals[q]==vals[p]+d
     else:vals[q]=vals[p]+d;queue.append(q)
   assert vals=={complex(p[0]+.5,p[1]+.5):v for p,v in z['certificate']['face_values']};assert vals[-1.5+.5j]==-(len(ll)-2)
   sizes.append([key,len(events),len(comps),len(ll),len(kk),vals[-1.5+.5j]])
  else:raise AssertionError(typ)
assert dict(ct)==ref['counts']and ct==dict(rank=7998,clock=108,higher_C=86,open=18);assert set(opened)==matched
assert dict(per)==ref['profile_counts'];assert len({z[-2:]for z in matched})==9
outreport=dict(status='PASS uncapped L/K necessary local shields only; signed complete-cap4 obstruction unchanged',script=sha(S),bindings=files,derived_domains=dict(L=len(Ls),K={m:len(w)for m,w in Ks.items()}),counts=dict(ct),independent_rank_path_lengths=dict(ranks),independent_positive_clock_weights=dict(clocks),higher_C_count=len(higher),all18_calendars=sizes,analytic_review=[
'Only outer L and K are uncapped. The other six complete WHITE histories and GLOBAL maximum Q premise remain exactly the signed five Q-square modes. This does not relax the whole core or prove an all-cap portal classification.',
'L has exactly two W arrivals and two S departures. WHITE alternating counts give R_W=R_E=2-L_W, total R<=4, hence total reads<=8. K has N_in2 and E_out=m with m in1,2,5,6; exact integer count identities give n<=2(2+m)+1. Enumerating all placements of the two fixed-axis arrivals through those derived bounds is complete, not a guessed visit cutoff.',
'Every8210 count-compatible product is rebuilt independently. Physical ordinal successors, wrong-next-rank paths and positive actual-time cycles are reconstructed; global C heights use the actual Q anchor and all radial equations. Counts agree7998 rank,108 positive clocks,86 higherC,18 necessary opens.',
'All18 author calendars independently satisfy every actual successor equality, every complete same-cell next rank gap>=4, phase residues, unique event times and whole-component disjointness. These are calendars of known event components, not completed exterior routes or physical finite-board factors.',
'Exactly nine outer pairs remain in two fixed core modes. L has7/8 reads, K6..8 and the named low C face is M-5/M-6. Its large read count cannot be excluded by pretending its first-R sector is globally maximal.',
'Original complete-cap4 upper completion remains signed and is not invalidated. The present argument cannot be promoted reader-independent: these necessary higher-read shields survive it. No actual front, full-drift equality, autonomous controller, renewable stock, input fuel charge or global attainment is supplied.'
],dependencies={'signed_upper_completion':sha(S.with_name('check_terminal_LL_upper_completion_independent.json'))})
S.with_suffix('.json').write_text(json.dumps(outreport,indent=2)+'\n');print(outreport['status']);print(sha(S.with_suffix('.json')));print(ct)
