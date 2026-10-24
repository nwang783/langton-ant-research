from pathlib import Path
from collections import Counter
import ast,json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'LL_reset_late_suppliers_keep_both_tail_signs_open_locally.md':'8a0f30700e9043ecc381e3434cb6e01d3bea69618296d6f1115c96eaaac94760','check_fixed_LL_L3_supplier_controls.py':'56eabe0a8eba5d441e30901670817d44dbbbd4a325b0d61ad0742a8571703b01','check_fixed_LL_L3_supplier_controls.json':'0d78caa060dfa639958fa1a6413003ddf4384b4486c2f950a945402bba985a2e'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'check_fixed_LL_L3_supplier_controls.json').read_text());V=[1j,1,-1j,-1];letters='NESW';od=lambda w,r:(letters.index(w[r])+(1 if r%2==0 else-1))%4;phase=lambda z:{(0,0):0,(1,0):1,(0,1):3,(1,1):2}[int(z.real)%2,int(z.imag)%2];base={0j:'NNSS',1j:'EWW',2j:'SSNS',1+0j:'EEWW',1+1j:'SNNS',1+2j:'EEE',2+0j:'NNS'};summ=[]
for row in J['rows']:
 H={complex(*ast.literal_eval(k)):v for k,v in row['histories'].items()};expected=base|({2+1j:'EE',2+2j:'N'}if row['kind']=='positive'else{2+1j:'WEE',2+2j:'NSN'});assert H==expected
 su={};pr={};flows={};events={(p,r)for p,w in H.items()for r in range(len(w))}
 def flow(p,h,n):
  if(p,h)in flows:assert flows[p,h]==n
  flows[p,h]=n
 for p,w in H.items():
  assert len(w)<=4 and all(letters.index(c)%2==int(p.real+p.imag)%2 for c in w)
  for h,d in enumerate(V):
   outs=[r for r in range(len(w))if od(w,r)==h];ins=[r for r,c in enumerate(w)if letters.index(c)==h]
   if h%2!=int(p.real+p.imag)%2:flow(p,h,len(outs))
   else:flow(p-d,h,len(ins))
   q=p+d
   if q in H:
    targets=[r for r,c in enumerate(H[q])if letters.index(c)==h];assert len(outs)==len(targets)
    for r,s in zip(outs,targets):assert(p,r)not in su and(q,s)not in pr;su[p,r]=(q,s);pr[q,s]=(p,r)
 val={complex(*ast.literal_eval(k)):v for k,v in row['stream'].items()};assert val[-1j]==0
 for (p,h),n in flows.items():
  x,y=int(p.real),int(p.imag)
  candidates=([(x,y-1),(x,y)]if h==1 else [(x-1,y-1),(x-1,y)]if h==3 else[(x-1,y),(x,y)]if h==0 else[(x-1,y-1),(x,y-1)])
  c,l=sorted([complex(*z)for z in candidates],key=lambda z:-(int(z.real+z.imag)%2))
  assert int(c.real+c.imag)%2==1 and int(l.real+l.imag)%2==0 and val[c]-val[l]==n
 assert max(v for p,v in val.items()if int(p.real+p.imag)%2)==0 and max(v+1 for p,v in val.items()if not int(p.real+p.imag)%2)<=0
 T={(complex(*z['cell']),z['rank']):z['time']for z in row['times']};assert set(T)==events and len(set(T.values()))==len(events)
 supplied=[]
 for z in row['complete_literal_channels']:
  seq=[(complex(*p),r)for p,r in z['events']];assert seq[0]not in pr and seq[-1]not in su
  assert all(su[a]==b for a,b in zip(seq,seq[1:]));assert[T[e]for e in seq]==list(range(z['start'],z['start']+len(seq)));supplied.extend(seq)
 assert len(supplied)==len(events)and set(supplied)==events
 for a,b in su.items():assert T[b]==T[a]+1
 for p,w in H.items():
  for r in range(len(w)):assert T[p,r]%4==phase(p)
  for r in range(1,len(w)):assert T[p,r]-T[p,r-1]>=4
 x=(1+0j,3);y=(1+1j,3);tail=T[y]-T[x];assert tail==row['tail_Y3_minus_X3']==(45 if row['kind']=='positive'else-3)
 root=(1j,1);cleanup=[root,(0j,3),(1+0j,1),(1+1j,1),(1j,2)];assert all(su[a]==b for a,b in zip(cleanup,cleanup[1:]))
 if row['kind']=='negative':
  late=[y,(2+1j,2),(2+0j,2),x];early=[(1+0j,2),(1+1j,2),(2+1j,1),(2+2j,2)]
  assert all(su[a]==b for a,b in zip(late,late[1:]))and all(su[a]==b for a,b in zip(early,early[1:]));assert sum(od(H[2+0j],r)==1 for r in range(3))==1 and od(H[2+0j],0)==1
  assert H[2+1j].count('W')==1 and od(H[1+1j],0)==3 # incoming-E b alternative would need Y to depart E, false.
 summ.append(dict(kind=row['kind'],events=len(events),channels=len(row['complete_literal_channels']),internal_edges=len(su),directed_flow_equations=len(flows),tail=tail))
out=dict(status='PASS both-sign OPEN supplier inventories and conditional distinct long-return owner only',files=files,script=sha(S),controls=summ,analytic_review=['Every complete WHITE cap4 cell history is retained. Internal physical directional counts include all zero ports; ordinal matching gives exactly the serialized maximal channels. Supplied distinct mod4 clocks satisfy all literal unit steps and same-cell rank gaps>=4, and full stream face equations have C<=M and shiftedL<=M. Exterior connector demands are not fulfilled, so neither inventory is an actual ant factor/front.','The negative late LRR chain goes Y.L3 through D.R2,R.R2 to X.L3, forcing exact signed tail-3. The earlier X.R2,Y.R2,D.L1,T.R2 chain and actual four-L root cleanup remain present; no middle reads are skipped or replaced by a bare prepared subfactor.','Conditional on a critical GLOBAL-M/no-one-use complete cap4 boundary realizing this exact square, R=NNS is off Gamma because its first-R outgoingE has physical use1. D=WEE cannot be a RIGHT boundary contact because its incomingW edge has use1; its LEFT incomingE possibility would require Y first-R outgoingE, while actual Y first-R departsW. Thus both intermediate cells are off Gamma.','The entire late path lies on the LEFT of Gamma and cannot cross a cut at the flat endpoints or off-boundary interiors. Critical same-physical-contact pipeline puts it inside one actual LEFT excursion. It contains R reads and cannot lie in any LL-first four-L return or any four-step same-pose return. Signed root classification leaves a distinct singletonO or WEEE root, with span>=8. This is conditional owner existence, not an injection, per-reset fuel charge, unit voltage or globally attained network.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
