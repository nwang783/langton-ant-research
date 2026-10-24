from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=D/'JOINT_C_FIRST_LAST_TEMPORAL_FORESTS.md';JF=D/'joint_C_temporal_forests_certificate.json'
assert sha(P)=='9a1c37168565f05c9d69c0383e570792e1c2399105b6d81beee25537c618825c' and sha(JF)=='7e910e59f2fb8450ce6294994b0e870e27545f79cda6c3cc204e15062582c0bf'
assert sha(D/'certify_joint_C_temporal_forests.py')=='339e25609b2ba38cc1007e9dc400f2a4847a520c5f9f6f20f991a4d50f404ede'
J=json.loads(JF.read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_active_C_entry_exit_independent.py'))};src=Path(ns['__file__']).read_text().split('base={};summary={}')[0];src=src.replace(' return sig',' return dict(E=E,d=d,n=n,ev=ev,rep=rep,face=face,H=H,F=F,starts=starts,ends=ends,graphs=graphs,fw=fw,cycles=cycs[1])');exec(src,ns)
analyze=ns['analyze'];base=ns['J']['base_controls'];xy=ns['xy'];V=ns['V'];complexify=lambda q:complex(*q)
def graph(w,h=0):
 z=analyze(w,h);n=z['n'];A=z['starts'];B=z['ends'];ee=[];sp=[]
 def edge(kind,sl,u,tl,v,nu,g,**extra):
  s=(A if sl=='A'else B)[u];t=(A if tl=='A'else B)[v]+nu*n
  assert t-s==g>=0 and z['face'](s)==u and z['face'](t)==v+nu*z['d']
  ee.append(dict(kind=kind,source_layer=sl,source=xy(u),target_layer=tl,target=xy(v),voltage=nu,gap=g,source_time=s,target_time=t,**extra))
 for v,f in z['graphs'][0].items():
  u=complexify(f['target']);nu=-f['voltage'];lt=A[v]+nu*n-1;lp,lh,lc,li=z['ev'](lt);assert lc=='L'and li==f['L_phase']
  extra=dict(WHITE_owned=f['WHITE_first'],first_entry_L_time=lt,first_entry_L_phase=li)
  if f['WHITE_first']:
   rt=lt-f['R_to_L_age'];rp,rh,rc,ri=z['ev'](rt);assert(rp,rh,rc)==(lp,lh,'R')and ri==f['R_owner_phase'];extra.update(R_owner_time=rt,R_owner_phase=ri,R_to_L_age=lt-rt)
  edge('first','A',u,'A',v,nu,f['clock_gap'],**extra)
 for u,f in z['graphs'][1].items():
  v=complexify(f['target']);nu=f['voltage'];lt=B[u];lp,lh,lc,li=z['ev'](lt);assert lc=='L'and li==f['L_phase'];extra=dict(last_exit_L_time=lt,last_exit_L_phase=li,selected_cell_ends_R=f['ends_R'])
  if f['ends_R']:
   rt=lt+f['L_to_R_gap'];rp,rh,rc,ri=z['ev'](rt);assert rp==lp and(rh-lh)%4==2 and rc=='R'and ri==f['final_R_phase'];extra.update(final_R_time=rt,final_R_phase=ri,L_to_R_gap=rt-lt)
  edge('last','B',u,'B',v,nu,f['clock_gap'],**extra)
  if A[v]+nu*n==B[u]+1:edge('literal_handoff','B',u,'A',v,nu,1)
 for v in sorted(A,key=lambda p:(p.real,p.imag)):
  span=B[v]-A[v];k=(span+n-1)//n;assert span>=0 and(not span or span%n)
  edge('span','A',v,'B',v,0,span);edge('canonical_carry','B',v,'A',v,k,k*n-span)
  sp.append(dict(face=xy(v),A=A[v],B=B[v],span=span,minimal_carry=k,carry_gap=k*n-span))
 return z,ee,sp
canonical=lambda rows:sorted(json.dumps(a,sort_keys=True)for a in rows)
zs={};summary={}
for name,g in J['base_graphs'].items():
 z,edges,sp=graph(base[name]['word']);zs[name]=z
 assert canonical(edges)==canonical(g['edges'])and sp==g['face_spans'];assert max(a['span']for a in sp)==g['maximum_span']and max(a['minimal_carry']for a in sp)==g['maximum_carry']
 summary[name]=dict(faces=len(sp),edges=len(edges),maximum_span=g['maximum_span'],maximum_carry=g['maximum_carry'],zero_spans=sum(a['span']==0 for a in sp))
 cc=J['literal_collapsed_cycle_countercontrols'][name];u=complexify(cc['u']);v=complexify(cc['v']);aa=z['starts'];bb=z['ends'];n=z['n']
 assert cc['collapsed_winding']*n==cc['first_last_gap_sum']+bb[v]-aa[v]-bb[u]+aa[u]
 previous=aa[u]
 for a in cc['full_actual_contiguous_arcs']:
  assert a['from']==previous and a['to']-a['from']==a['duration'];previous=a['to'];rows=[]
  for t in range(a['from'],a['to']):
   p,h,c,i=z['ev'](t);rows.append(dict(t=t,p=xy(p),hi=h,ho=(h+(1 if c=='R'else-1))%4,c=c))
  assert rows==a['all_events']
 assert previous-aa[u]==cc['repaired_duration']==n*cc['repaired_winding']
for r in J['representation_checks']:
 w=base[r['name']]['word'];w=w[r['phase']:]+w[:r['phase']]if 'phase'in r else w*r['power'];z,e,s=graph(w,r.get('heading',0));assert(len(s),len(e),max(a['span']for a in s),max(a['minimal_carry']for a in s))==(r['face_count'],r['edge_count'],r['maximum_span'],r['maximum_carry'])
 if 'input_count'in r:assert r['input_count']==sum(v[0][1]['c']=='L'for v in z['H'].values())and r['output_count']==sum(v[-1][1]['c']=='R'for v in z['H'].values())
assert len(J['representation_checks'])==60
ns2={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns2['__file__']).read_text().split('# Canonical source')[0],ns2);sim=ns2['sim'];future=ns2['future']
blank=sim(set(),10359,0j,0);w,d,dead,tests=future(blank['B'],blank['p'],blank['h']);W=base['S104']['word'];assert w==W[70:]+W[:70]
for name,row in J['complete_finite_field_replays'].items():
 if name=='S104':seed=set(blank['B']);p=blank['p'];h=blank['h'];word=w
 else:seed={-1-1j,-1+0j,1j}|({3+2j}if name=='F80'else set());p=0j;h=0;word=base[name]['word']*(2 if name=='M10'else 1)
 assert row['states'][0]['full_BLACK']==sorted(map(xy,seed));B=set(seed);ref=[e for a in J['literal_collapsed_cycle_countercontrols'][name]['full_actual_contiguous_arcs']for e in a['all_events']];rot=(-1j)**row['normalized_graph_to_replay']['clockwise_quarter_turns'];offset=complexify(row['normalized_graph_to_replay']['translation']);stateby={a['time']:a for a in row['states']}
 for t in range(len(word)+1):
  if t in stateby:assert dict(time=t,head=xy(p),heading=h,full_BLACK=sorted(map(xy,B)))==stateby[t]
  if t==len(word):break
  c='L'if p in B else'R';assert c==word[t];assert row['all_events'][t]==dict(time=t,position=xy(p),incoming_heading=h,turn=c);rr=ref[t];assert complexify(rr['p'])*rot+offset==p and(rr['hi']+row['normalized_graph_to_replay']['clockwise_quarter_turns'])%4==h and rr['c']==c
  B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
O=dict(status='PASS exact joint first/last C temporal graph and literal countercontrols, with zero-duration identity arcs discarded after contraction',proof=sha(P),certificate=sha(JF),script=sha(S),base=summary,representation_checks=60,blank_absolute_start=10359,complete_tail_parity_tests=tests,analytic_review=[
'Each edge is checked against actual physical first/last occurrence times with full supplied drift; FIRST reverses the child-parent arrow and its voltage. Actual same-cell R/L owners and final-R opposite headings remain. Arbitrary interior events are retained, not declared separate channels.',
'Canonical carry ceil((B-A)/P) targets a translated face, never a free rewind. A nonzero span cannot be a multiple of P since one phase has only one position under nonzero full drift. Zero-span A/B identification also discards its zero-duration identity arcs; every remaining closed positive-duration walk has wP=sum gaps>0.',
'The collapsed FIRST/LAST identity retains signed span switches at each occurrence. It allows nonpositive projected winding. Restoring each backward switch adds the actual carry voltage, not an assumed unit. Graph-simple two-node span/carry cycles need not be spatially embedded and can wind three times.',
'All graphs, event owners, three complete finite fields, every countercontrol event and rigid map were independently reconstructed. Blank standard control includes full all-future parity and every archived bit. Prepared10/80 controls cover only the specified paid finite periods, not complete finite-seed translation.',
'No span/carry bound, event-disjointness across graph walks, controller module forcing, WHITE lifetime S1 or universal capture follows. Powers split full quotient classes and change numerical carry; these are not invariant input charges.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(summary);print(sha(S.with_suffix('.json')))
