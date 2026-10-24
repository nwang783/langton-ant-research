from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'STANDARD_LIFETIME_PROJECTED_CROSSING_COUNTERCONTROL.md':'66e9e6fd958c9fd44736d1608687ee896f4deabff3f59943c56635835f8e1bc7','certify_lifetime_projection_crossing.py':'6f8bed1cf66a0859cffc1f7fe985de1480863832002f03096a708606995d452f','lifetime_projection_crossing_certificate.json':'2d960c3f7f15cbbb96232dcc938a64eeef501de678079384ca348c7fbcdc5494'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'lifetime_projection_crossing_certificate.json').read_text());signed=R/'audits/check_lifetime_boundary_graph_independent.json';assert sha(signed)=='2146e0898133417c220dbd595812f59308252169dbdeaa0d4c812fd9e5d933dc'
for f,h in J['dependencies'].items():assert sha(D/f)==h
w=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];assert w==J['word'];P=len(w);V=[1j,1,-1j,-1];xy=lambda q:[int(q.real),int(q.imag)];p=0j;h=0;pos=[]
for c in w:pos.append(p);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
d=p;assert d==-2+2j and P==104;H=defaultdict(list);lift={}
for i,p in enumerate(pos):k=-(int(p.real)//2);q=p-k*d;lift[i]=k;H[q].append((i-P*k,i))
A={}
for q,es in H.items():
 es.sort();assert w[es[0][1]]=='R'
 for(_,i),(_,j)in zip(es,es[1:]):
  assert w[i]!=w[j]
  if w[i]=='R':A[i]=(j,lift[i]-lift[j]);A[j]=(i,lift[j]-lift[i])
B={(i+1)%P:((j+1)%P,v+(j==P-1)-(i==P-1))for i,(j,v)in A.items()};graph=json.loads((D/'lifetime_boundary_graph_certificate.json').read_text())['controls']['S104']['graph'];results=[]
for key in('horizontal_path','vertical_path'):
 row=J[key];ref=graph['root_pairing_edges'][row['component_index']];start=min(ref['interior_events']);stack=[start];L={start:0}
 while stack:
  i=stack.pop()
  for M in(A,B):
   if i not in M:continue
   j,v=M[i]
   if j in L:assert L[j]==L[i]+v
   else:L[j]=L[i]+v;stack.append(j)
 first=ref['ends'][0];i=first['event'];g=L[i]if first['side']=='A'else L[(i+1)%P]-(i==P-1);assert sorted((i,z-g)for i,z in L.items())==list(map(tuple,row['complete_event_lifts']))
 ends=[xy(pos[e['event']]+(e['lift']-first['lift'])*d)for e in ref['ends']];assert ends==row['endpoints'];lives={}
 for i,z in L.items():
  if i in A and w[i]=='R':lives[i,z-g]='A'
  if i in B:
   j=(i-1)%P
   if w[j]=='R':lives[j,z-(j==P-1)-g]='B'
 exact=[]
 for(i,z),color in sorted(lives.items()):
  j,v=A[i];p=pos[i]+z*d;birth=i+z*P;death=j+(z+v)*P;assert birth<death and p==pos[j]+(z+v)*d;exact.append(dict(birth_phase=i,birth_lift=z,position=xy(p),birth_time=birth,consumption_time=death,matching_color=color))
 assert exact==row['complete_black_lifetimes'];at=[(r['birth_time'],r['consumption_time'])for r in exact if r['position']==[-1,0]];results.append(at)
assert results[0]==[(21,101)]and sorted(results[1])==[(-151,-71),(-67,-63),(1,9)]
assert J['horizontal_path']['endpoints']==[[-2,0],[0,0]]and J['vertical_path']['endpoints']==[[-1,2],[-1,-2]]
for a,b in results[0]:
 for c,e in results[1]:assert b<c or e<a
out=dict(status='PASS genuine standard proper projected H/V crossing uses distinct lifetime epochs',files=files,script=sha(S),signed_graph=sha(signed),horizontal_crossing_lifetimes=results[0],vertical_crossing_lifetimes=sorted(results[1]),analytic_review=['Both compressed spatial segments cross strictly in their interiors at-1,0, which is not either output endpoint. Their complete actual alpha/beta components, full event lifts and all underlying R-to-next-L intervals were independently reconstructed from the literal standard word.','The horizontal path lifetime21..101 is different from and temporally disjoint from all three vertical lifetimes at the crossing. Fibre space-time embedding is not contradicted. Combined projected H/V planarity and a shared-lifetime-at-every-crossing shortcut are false even for the genuine complete WHITE standard front. No stronger shared-lifetime invariant or controller classification is excluded.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
