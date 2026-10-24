from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
hashes={'PHYSICAL_EXIT_COMPONENT_COLOR_TURN_AND_BOUNDARY_FLUX.md':'cdff2e608b072490d58bd8eb9d83d16bdc5df3dc26330cc1524ceaebff4bc1fc','certify_exit_component_turn_flux.py':'e34b8ce4890e6f0b50394c9b3a09c687c9c0cbb54ab80c3fb3d4f1e64f45b67b','exit_component_turn_flux_certificate.json':'61a1dd93fb93e79055dffe80aacb8de85febdc9e9ed85f3aba16badb38592ba9','PHYSICAL_EXIT_SPINES_ORDER_COMPONENTS_AND_FLUX_CUTS.md':'82b34f15074a73f857bea4ce0012330f0503be14c6a9b6d187a8701e37dbfdbd','certify_exit_component_ordered_cuts.py':'05474b2a362dc3e4badd3447234f60758a98657f1f0349669857f375ab91229c','exit_component_ordered_cuts_certificate.json':'a44721b20a978013466e7b542edf6fdc986cf94db658f40c74fd898570e654d8'}
for f,h in hashes.items():assert sha(D/f)==h,(f,sha(D/f))
ref=json.loads((D/'exit_component_turn_flux_certificate.json').read_text());ordered=json.loads((D/'exit_component_ordered_cuts_certificate.json').read_text())
for f,h in ref['dependencies'].items():assert sha(Path(f))==h
for f,h in ordered['dependencies'].items():assert sha(D/f)==h
lib=S.with_name('check_phase13_double_scatter_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('# Canonical source')[0],ns);future,phases=ns['future'],ns['phases']
V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];tup=lambda p:(int(p.real),int(p.imag))
def analyze(w,h0=0):
 P=len(w);p=0j;h=h0;E=[]
 for i,c in enumerate(w):
  ho=(h+(1 if c=='R'else-1))%4;E.append((p,h,ho,c));p+=V[ho];h=ho
 d=p;assert h==h0 and d
 def qu(q):
  j=0 if d.real else 1;v=int(q.real if j==0 else q.imag);dd=int(d.real if j==0 else d.imag);k=(v//abs(dd))*(1 if dd>0 else-1);return q-k*d,k
 H=defaultdict(list);rep={};lift={};rank={}
 for i,(p,hi,ho,c)in enumerate(E):
  q,k=qu(p);rep[i]=q;lift[i]=k;H[q].append((i-k*P,i))
 for q,ls in H.items():
  ls.sort()
  for j,(t,i)in enumerate(ls):rank[i]=j
  assert all(E[i][3]!=E[j][3]for (_,i),(_,j)in zip(ls,ls[1:]))
 G={};edges={}
 for q,ls in H.items():
  lam,i=ls[-1];p,k=qu(q+V[E[i][2]]);gap=H[p][-1][0]+k*P-lam;assert gap>=1 and rep[(i+1)%P]==p;G[q]=(p,k);edges[q]=(p,k,lam,i,gap)
 seen=set();cycles=[]
 for q in H:
  at={};path=[];x=q
  while x not in seen:
   seen.add(x);at[x]=len(path);path.append(x);x=G[x][0]
  if x in at:
   cy=path[at[x]:];assert sum(G[x][1]for x in cy)==1
   hh=[E[edges[x][3]][2]for x in cy];turns=[(hh[(j+1)%len(hh)]-v)%4 for j,v in enumerate(hh)];assert all(x in[1,3]for x in turns)and sum(1 if x==1 else-1 for x in turns)==0;cycles.append(cy)
 color={q:i for i,cy in enumerate(cycles)for q in cy}
 for q in H:
  x=q
  while x not in color:x=G[x][0]
  color[q]=color[x]
 labels=[color[rep[i]]for i in range(P)];comps=[]
 for cid,cy in enumerate(cycles):
  qs={q for q in H if color[q]==cid};ii=[i for i in range(P)if labels[i]==cid];I=sum(E[H[q][0][1]][3]=='L'for q in qs);O=sum(E[H[q][-1][1]][3]=='R'for q in qs);g=sum(1 if E[i][3]=='R'else-1 for i in ii);assert g==O-I
  Q=sum((1 if E[i][3]=='R'and E[i][1]==3 else-1 if E[i][3]=='L'and E[i][1]==0 else 0)for i in ii)
  b=[0]*4;out=[0]*4;inc=[0]*4
  for i in range(P):
   a,c=labels[i],labels[(i+1)%P];hh=E[i][2]
   if a!=c:
    if a==cid:b[hh]+=1;out[hh]+=1
    if c==cid:b[hh]-=1;inc[hh]+=1
  assert sum(b)==0;phi=sum(i*x for i,x in enumerate(b));assert g==4*Q+phi
  starts=[i for i in range(P)if labels[i]==cid and labels[i-1]!=cid]or[0];blocks=[]
  for start in starts:
   stop=start
   while stop<start+P-1 and labels[(stop+1)%P]==cid:stop+=1
   inds=[j%P for j in range(start,stop+1)];hin=E[inds[0]][1];hout=E[inds[-1]][2];T=sum(1 if E[j][3]=='R'else-1 for j in inds);delta=(hout-hin+1)%4-1;assert (T-delta)%4==0
   blocks.append(dict(start_phase=start,end_unwrapped_phase=stop,length=stop-start+1,word=''.join(E[j][3]for j in inds),incoming_heading=hin,outgoing_heading=hout,actual_signed_turn_sum=T,principal_endpoint_turn=delta,residual_full_turns=(T-delta)//4))
  psi=sum(z['principal_endpoint_turn']for z in blocks);WW=sum(z['residual_full_turns']for z in blocks);assert g==4*WW+psi
  comps.append(dict(cid=cid,cells=qs,cycle=cy,I=I,O=O,g=g,Q=Q,b=b,phi=phi,psi=psi,W=WW,blocks=blocks,out=out,inc=inc))
 cross=[];owners=[]
 for i in range(P):
  j=(i+1)%P;a,b=labels[i],labels[j]
  if a==b:continue
  q=rep[i];r=rank[i];ls=H[q];assert r<len(ls)-1;tt,k=ls[r+1];age=tt-ls[r][0];nu=lift[i]-lift[k];assert age>=4 and age%4==0 and E[k][0]+nu*d==E[i][0]and k+nu*P-i==age
  cross.append(dict(source_phase=i,target_phase=j,actual_step_period_voltage=int(j==0),direction=E[i][2],source_component=a,target_component=b,source_position=xy(E[i][0]),target_position=xy(E[i][0]+V[E[i][2]]),source_complete_rank=r,source_complete_count=len(ls),source_first_read=r==0,source_turn=E[i][3],target_complete_rank=rank[j],target_turn=E[j][3],required_next_same_cell_read=dict(phase=k,period_voltage=nu,turn=E[k][3],incoming_heading=E[k][1],gap=age,same_component=a)))
 for q,ls in H.items():
  for (ta,a),(tb,b)in zip(ls,ls[1:]):
   if E[a][3]=='R':owners.append(dict(class_=xy(q),component=color[q],R_phase=a,L_phase=b,age=tb-ta,owner_period_relative_to_L=lift[b]-lift[a]))
 return dict(P=P,d=d,E=E,H=H,edges=edges,comp=comps,labels=labels,cross=cross,owners=owners)
def signature(a):return sorted((c['O'],c['I'],len(c['cells']),c['g'],c['psi'],c['W'],len(c['blocks'])if len(a['comp'])>1 else 0)for c in a['comp'])
def cutcheck(a):
 d=a['d'];cs=a['comp'];ranges=[]
 for c in cs:
  vals=[int(d.real*q.imag-d.imag*q.real)for q in c['cycle']];ranges.append(dict(component_id=c['cid'],minimum=min(vals),maximum=max(vals),outputs=c['O']))
 ranges.sort(key=lambda z:z['minimum']);assert all(x['maximum']<y['minimum']for x,y in zip(ranges,ranges[1:]));ix={z['component_id']:i for i,z in enumerate(ranges)};J=[[0]*4 for _ in ranges[:-1]];cnt=[[0,0]for _ in J]
 for z in a['cross']:
  i,j=ix[z['source_component']],ix[z['target_component']];assert abs(i-j)==1;k=min(i,j);s=1 if i<j else-1;J[k][z['direction']]+=s;cnt[k][int(s<0)]+=1
 assert all(x==y and x>0 for x,y in cnt);rows=[];prev=[0]*4;sg=sq=0
 for i,z in enumerate(ranges):
  c=cs[z['component_id']];aft=J[i]if i<len(J)else[0]*4;assert c['b']==[a-b for a,b in zip(aft,prev)];phi=sum(h*v for h,v in enumerate(aft));before=sum(h*v for h,v in enumerate(prev));sg+=c['g'];sq+=c['Q'];assert sg==4*sq+phi
  rows.append(dict(component_id=c['cid'],outputs=c['O'],inputs=c['I'],Q=c['Q'],lower_cut_flux=before,upper_cut_flux=phi,prefix_charge=sg,prefix_Q=sq));prev=aft
 return dict(transverse_spine_ranges_in_order=ranges,adjacent_cut_direction_vectors=J,each_cut_out_in_counts=cnt,component_and_prefix_identities=rows)
base={};summaries={}
for name,z in ref['base_controls'].items():
 a=analyze(z['word']);base[name]=a;assert a['cross']==z['all_actual_cross_component_steps'];assert xy(a['d'])==z['drift']
 for c,r in zip(a['comp'],z['components']):
  assert sorted(map(xy,c['cells']))==r['read_classes']and list(map(xy,c['cycle']))==r['last_spine']['cells']
  for x,y in [('I','I'),('O','O'),('g','color_charge'),('Q','branch_cut_wrap_count'),('b','out_minus_in_direction_counts'),('phi','heading_branch_flux'),('psi','principal_boundary_flux'),('W','block_residual_full_turn_sum'),('blocks','blocks'),('out','outgoing_cross_counts'),('inc','incoming_cross_counts')]:assert c[x]==r[y],(name,x)
 for hr in z['all_complete_read_histories']:
  q=complex(*hr['class']);ls=a['H'][q]
  assert len(ls)==len(hr['events'])
  for (tt,i),e in zip(ls,hr['events']):
   p,hi,ho,cc=a['E'][i];assert e==dict(canonical_time=tt,t=i,p=xy(p),hi=hi,ho=ho,c=cc)
 ours=[{('class'if k=='class_'else k):v for k,v in z.items()}for z in a['owners']];assert ours==z['all_same_component_R_to_L_owners']
 for e in z['all_last_departure_edges']:
  q=complex(*e['source']);p,k,lam,i,gap=a['edges'][q];assert e['target']==xy(p)and e['voltage']==k and e['last_source_phase']==i and e['selected_edge_last_clock_gap']==gap
 assert cutcheck(a)==ordered['base_controls'][name];summaries[name]=signature(a)
controls=[]
for rr in ref['all100_rotation_power_phase_controls']:
 z=ref['base_controls'][rr['name']];w=z['word']
 if 'phase'in rr:k=rr['phase'];h=base[rr['name']]['E'][k][1];a=analyze(w[k:]+w[:k],h)
 else:a=analyze(w*rr['power'],rr['heading'])
 assert list(map(list,signature(a)))==rr['component_signature']
 if 'branch_cut_data'in rr:assert [[c['O'],c['Q'],c['phi']]for c in a['comp']]==rr['branch_cut_data']
 controls.append(dict(name=rr['name'],phase=rr.get('phase'),heading=rr.get('heading'),power=rr.get('power'),signature=signature(a)))
for rr in ordered['all16_standard_representation_controls']:assert cutcheck(analyze(ref['base_controls']['S104']['word']*rr['power'],rr['heading']))==rr['result']
# Entire blank realization with actual BLACK birth IDs, no cropped board.
lit=ref['literal_standard_positive'];cuts={z['time']:z for z in lit['full_states']};frame=lit['period_frame'];B={};p=0j;h=0;events=[];hist=defaultdict(list);fchecks=[]
for t in range(frame+3*104):
 if t in cuts:
  z=cuts[t];assert sorted(map(xy,B))==z['full_black_field']and xy(p)==z['head']and h==z['heading']
  if t in[9977,frame]:tw,dr,dead,tests=future(B,p,h);assert tw==ref['base_controls']['S104']['word']and tw in phases;fchecks.append((t,len(B),tests))
 c='L'if p in B else'R';e=dict(time=t,position=xy(p),incoming_heading=h,turn=c)
 if c=='L':e['actual_R_owner']=B.pop(p)
 else:B[p]=t
 events.append(e);hist[p].append(t);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
assert events[frame:frame+104]==lit['all104_reads_and_actual_owners']
for z in lit['all_eight_crossings_and_required_next_reads']:
 e=z['literal_source'];i=e['time'];j=z['literal_next_same_cell_read']['time'];assert events[i]==e and events[i+1]==z['literal_target']and events[j]==z['literal_next_same_cell_read'];q=complex(*e['position']);assert [t for t in hist[q]if i<t<=j]==[j]
assert hist[complex(*events[frame+38]['position'])][0]==frame+38
# All six complete lower interfaces, actual arrows and FULL-voltage merger.
low=[]
for z in ref['middle_short_lower_merge']:
 H={int(k):v for k,v in z['complete_T0_through_T10'].items()};ed={}
 for t,hs in H.items():
  h=(hs[-1]+(1 if len(hs)%2 else-1))%4;v=V[h];ed[t]=(t+int(3*v.imag-v.real),int(v.imag))
 paths=[]
 for t in range(11):
  v=t;k=0;pa=[]
  while v in ed:
   assert v not in[x['source']for x in pa];u,dk=ed[v];pa.append(dict(source=v,target=u,voltage=dk));v=u;k+=dk
  paths.append(dict(start=t,path=pa,unknown_endpoint_class=v,total_voltage=k))
 assert paths==z['all11_last_departure_paths']and len({x['unknown_endpoint_class']for x in paths})==1
 assert all(len(H[t])%2==1 for t in[0,1,2,6,7]);low.append(paths)
# Whole prepared backgrounds remain exact bound signed profiles, not graph deletion.
life=json.loads((D/'lifetime_boundary_graph_certificate.json').read_text())['controls']
for n in['P1564','Q4352']:assert ref['full_prepared_backgrounds'][n]==life[n]['complete_background']
review=[
'Physical read CELL components use the actual FULL Zd quotient and selected last departure, not C faces, first-entry basins, BLACK graph or lifetime circuit. Canonical last times give lambda(target)+nuP-lambda(source)>=1; target last read need not be the selected arrival. Signed primitive unit spine makes each quotient basin one physical component.',
'Complete alternating cell histories yield R-L=O-I. Summing actual heading increments cancels INTERNAL actual movements only, leaving outgoing-minus-incoming SAME-heading flux and wrap term. Every crossing is strictly before its source last read and has a retained next same-cell opposite read of positive age divisible by4. No interval-disjointness follows.',
'Principal endpoint differences use {-1,0,1,+2}; maximal cyclic component blocks, including seams, give O-I=4W+Psi. Proper rotation and phase preserve this decomposition; power multiplies charges and counts without changing physical component number. W is not a nonnegative geometric winding theorem.',
'WHITE standard really has component8 Psi=-4,W3 and component4 Psi+4,W0. R38 is an actual first departure crossing components. All eight steps, source next-ranks, full blank fields/owners and exact infinite tail are independently replayed. Prepared controls retain all BLACK-first and passive backgrounds.',
'For the topology companion, finitely many disjoint embedded essential unit spines are transversely ordered by cylinder separation, not by globally disjoint normal ranges. A connected basin stays on the same side of every other spine as its own spine. A used UNIT edge between nonadjacent basins must cross an intermediate spine at a grid vertex, which would identify components. Connected full bi-infinite read graph then forces every adjacent edge, hence exactly a path.',
'Each adjacent cut has equal positive opposite-direction component crossing counts. Its physical heading vector J gives b_i=J_i-J_(i-1), with the stated prefix identity. Actual reverse crossing heading is not negated artificially. Principal Psi is nonadditive and is NOT substituted for linear Phi without carries.',
'Normal-range separation is verified only for supplied standard representation controls. The sole standard low-to-high cut has Phi+4, so negative component flux is not a negative ordered-cut control. No ordered-cut sign, four-output lower bound, two-component WHITE theorem or controller exclusion is proved.',
'All six middle lower physical last-arrow paths merge to one unknown class with full voltages. Signed primitive spines, not primitive coordinate erasure, justify one physical exit component; higher completion remains open.'
]
out=dict(status='PASS exact physical exit-component flux and scoped ordered-spine path/cut identities',sources=hashes,base_signatures=summaries,representation_controls=controls,literal_standard_future_checks=fchecks,middle_six_full_voltage_paths=low,analytic_review=review,dependencies=ref['dependencies'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
