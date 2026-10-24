from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'RECURSIVE_PHASE13_PACKET_MANIFEST.json';assert sha(MF)=='6ddc626c03632dbaa1d11a4cdfc487b112d4c15bb8d9638d79dfc2fade266220'
m=json.loads(MF.read_text())
for kind in ['files','source_dependencies','source_data']:
 for f,h in m[kind].items():assert sha(D/f)==h
J=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text())
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);K,V,xy,future,phases,geometry,sim,cert,key=[ns[k]for k in('K','V','xy','future','phases','geometry','sim','cert','key')]
enc=lambda pts:sorted(map(xy,pts));dec=lambda pts:{complex(*q)for q in pts};z=cert(sim(K,104));W=z['word'];assert W==J['W']and enc(K)==J['canonical_source']and z['tail']==W and z['d']==2+2j
Q,HH,_,_=geometry(0j,1,W);assert Q[13]==2+1j and HH[13]==0 and min(q.real for q in Q)==-1
fresh=[]
for i,p in enumerate(Q):
 d=Q[13]-p
 if d.real==d.imag and int(d.real)%2==0:
  a=int(d.real)//2;fresh.append([i,a,104*a+i]);assert 104*a+i>=13
assert fresh==J['phase13_freshness']and [r[2]for r in fresh]==[13,17,25]
def mature(g):
 B=set()
 for i,p in enumerate(Q):
  a=p-Q[13];lo=-((int(a.real)-g)//2);hi=0 if i<13 else-1
  for k in range(lo,hi+1):B.symmetric_difference_update({a+k*(2+2j)})
 return B
modes={};summary={}
for label,g,indices,N,phase,ep,eh,nC,radius in [('S',-3,[0],312,97,2+6j,2,14,5),('M',-23,[0,1,6,8],10712,41,26+28j,0,126,22)]:
 row=J['modes'][label];A={2*a*(1+1j)for a in indices};B0=mature(g);assert not A&B0;seed=A|B0;assert enc(seed)==row['kernel']
 z=cert(sim(seed,N,0j,0,row['recovery_word']),W[phase:]+W[:phase]);assert(z['p'],z['h'],z['d'])==(ep,eh,2+2j)and enc(z['B'])==row['complete_output_black']and z['tests']==row['full_tail_tests']
 tq,th,_,_=geometry(ep,eh,z['tail']);assert min(p.real for p in z['pts']+tq)==g
 bbox=[int(min(p.real for p in z['pts'])),int(max(p.real for p in z['pts'])),int(min(p.imag for p in z['pts'])),int(max(p.imag for p in z['pts']))];assert bbox==row['full_read_bbox']
 C={p for i,p in enumerate(sorted(seed,key=key))if -i-1 in z['dead']};fates=[dict(cell=xy(p),first_read=z['dead'].get(-i-1))for i,p in enumerate(sorted(seed,key=key))];assert fates==row['initial_input_fates']and enc(C)==row['entire_comparison_pruning']and len(C)==nC and max(max(abs(p.real),abs(p.imag))for p in C)==radius
 assert enc(C-A)==row['old_input_cells']and [z['first'][2*a*(1+1j)]for a in indices]==row['first_packet_reads'];assert max(r['first_read']for r in fates if r['first_read']is not None)==row['last_initial_consumption']<N
 origin=ep-Q[phase];assert origin.real-origin.imag==-1 and int(origin.real)%2==0 and xy(origin)==row['output_virtual_origin']
 modes[label]=dict(seed=seed,z=z,g=g,indices=indices,N=N,phase=phase,C=C,r=radius)
 summary[label]=dict(seed=len(seed),relevant=len(C),radius=radius,old_inputs=len(C-A),recovery=N,tail_tests=z['tests'],full_output=len(z['B']))
# Entire source-field difference is left of x2 for every n>=100.
omitted=max(max(p.real for p in K),max(p.real-2 for p in Q));assert omitted==2
for row in J['initial_interfaces']:
 mode=modes[row['mode']];q=202+201j;bits={q+2*a*(1+1j)for a in mode['indices']};flight=W*100+W[:13];z=sim(K|bits,len(flight),expected=flight);assert(z['p'],z['h'])==(q,0)and not bits&set(z['pts']);inside={p for p in z['B']if p.real>=q.real+mode['g']};assert inside=={q+p for p in mode['seed']}and enc(inside)==row['inside']and q.real+mode['g']>omitted and row['old_source_max_x']==omitted
# Four complete-field transitions, with n-affine guard movement derived from actual endpoint poses.
for row in J['pair_interfaces']:
 r=modes[row['previous']];s=modes[row['next']];phase=r['phase'];q=r['z']['p']+202*(1+1j)+Q[13]-Q[phase];assert q.real==q.imag and q.real==(206 if row['previous']=='S'else 228)
 tail=W[phase:]+W[:phase];flight=tail*100+tail[:(13-phase)%104];seq=r['z']['word']+flight;bits={q+2*a*(1+1j)for a in s['indices']};z=sim(r['seed']|bits,len(seq),0j,0,seq);assert(z['p'],z['h'])==(q,0)and not bits&set(z['pts']);inside={p for p in z['B']if p.real>=q.real+s['g']};assert inside=={q+p for p in s['seed']}and enc(inside)==row['complete_inside']
 synthetic=r['z']['p'].real+max(Q[i].real-Q[phase].real+(0 if i<phase else-2)for i in range(104));oldmax=max(r['g'],max(p.real for p in r['z']['pts']),max(p.real for p in r['z']['B']),synthetic);boundary=q.real+s['g'];assert oldmax==row['previous_generated_max_x']and synthetic==row['synthetic_past_max_x']and boundary==row['next_guard_boundary']and boundary-oldmax==row['guard_slack']and boundary-r['g']==row['frontier_increase']>=186
 assert row['flight_reads']==len(flight)and row['all_reads']==len(seq)
 # For arbitrary n, endpoint and boundary shift by2(n-100), old support bounds unchanged.
 assert q.real==(6 if row['previous']=='S'else 28)+200 and len(flight)==10400+(20 if row['previous']=='S'else 76)
 assert max(p.real for p in r['z']['pts'])<=28<206 and max(d['N']for d in modes.values())<min(10400+20+r['N'],10400+76+r['N'])
controls=[];reads=0
for row in J['controls']:
 labels=row['modes'];gaps=row['gaps'];archive=dec(row['retained_western_archive']);assert all(p.real<-1 for p in archive);seed=K|archive;seq='';p=0j;phase=0;starts=[];packets=[]
 for label,n in zip(labels,gaps):
  assert n>=100;mode=modes[label];q=p+2*(n+int(13<phase))*(1+1j)+Q[13]-Q[phase];tail=W[phase:]+W[:phase];seq+=tail*n+tail[:(13-phase)%104];starts.append(len(seq));bits={q+2*a*(1+1j)for a in mode['indices']};assert not bits&seed;seed|=bits;packets.append((q,label,bits));seq+=mode['z']['word'];p=q+mode['z']['p'];phase=mode['phase']
 assert seq==row['complete_prefix_word']and enc(seed)==row['seed'];z=cert(sim(seed,len(seq),expected=seq,cuts=set(starts)),W[phase:]+W[:phase]);reads+=len(seq);assert enc(z['B'])==row['terminal_full_black']and [xy(z['p']),z['h']]==row['terminal_pose']and xy(z['d'])==row['tail_drift']and z['tests']==row['full_future_parity_tests']
 F=max(p.real for q,label,bits in packets for p in bits);potentials=[];radii=[];pop=[]
 for j,(t,(q,label,bits),ref)in enumerate(zip(starts,packets,row['mode_contacts'])):
  mode=modes[label];B,p,h=z['snap'][t];assert(p,h)==(q,0)and ref['time']==t and enc(B)==ref['complete_current_black'];pending={v for qq,ll,bb in packets for v in bb if z['first'][v]>=t};assert enc(pending)==ref['unread_original_markers'];assert all(z['first'][q+2*a*(1+1j)]==t+u for a,u in zip(mode['indices'],J['modes'][label]['first_packet_reads']))
  inside={v for v in B if v.real>=q.real+mode['g']};assert inside=={q+v for v in mode['seed']}|(pending-bits)
  C={v for v,i in B.items()if i in z['dead']};assert C=={q+v for v in mode['C']}|pending and enc(C)==ref['entire_pruning'];rho=max(max(abs((v-q).real),abs((v-q).imag))for v in C);potential=max(rho-22,0);assert rho==max(mode['r'],F-q.real)==ref['entire_relevant_radius']and potential==max(F-q.real-22,0)==ref['clipped_radius_potential']
  if j:step=q.real-packets[j-1][0].real;assert step>=206 and potential==max(potentials[-1]-step,0)
  potentials.append(int(potential));radii.append(int(rho));pop.append(len(C))
 assert potentials[-1]==0 and archive.isdisjoint(z['first']);assert all(z['B'].get(q)==-i-1 for i,q in enumerate(sorted(seed,key=key))if q in archive)
 controls.append(dict(modes=labels,gaps=gaps,reads=len(seq),initial_black=len(seed),full_terminal=len(z['B']),relevant_counts=pop,radii=radii,potentials=potentials,tail_checks=z['tests']))
out=dict(status='PASS all finite two-mode phase13 packet words and all gaps>=100 with entire-field advancing guards',manifest=sha(MF),script=sha(S),modes=summary,source_interfaces=2,pair_interfaces=4,complete_control_reads=reads,controls=controls,analytic_review=[
'Both actual full mature kernels are reconstructed from all prior104 phase-ray XORs, not from supplied local masks. The literal S312/M10712 words, exact phase97/41 endpoints, full62/719 outputs and every infinite parity condition pass. Every local initial relevant bit dies within its own recovery; whole comparisonC* is14/r5 or126/r22, with all122 old imports retained inM.',
'Phase13 freshness is an exact104-phase ray equality whose only offsets are13,17,25. Complete initialK and omitted synthetic prestart writes have x<=2. Thus all firstn>=100 guard transfers are exact full-half-plane XOR identities, not interpolation fromn100.',
'Each of four actual pair interfaces is replayed with the COMPLETE current kernel/output and later packet. Endpoint poses derive head increments2n+6/2n+28 and flight lengths104n+20/104n+76. Actual finite output, recovery footprint and complete omitted formal past are bounded by oldmax6/28. The next guard lies strictly east by at least177, advances>=186, and moves2(n-100) farther east for everylargern. Current recovery ends before any next input; canonical first-visit ordering handles the entire flight and all later packets.',
'Induction retains every old field bit, original packet and arbitrary initial archive x<-1. Older actual/synthetic discrepancies stay behind an advancing western guard; each future remains within its applicable guard. No normal-changingNW transition is imported. Original packet indices not in{0} or{0,1,6,8} are WHITE except later explicitly paid packets.',
'Exact C* entry equality is comparison pruning UNION all unread original packet bits, with current packet overlap counted once. Each reference-unread kernel bit remains unread before nextcontact and lies forever behind nextguard afterward; this is the necessary future-transfer proof, not template-based irrelevance. Fixed farthest original coordinateF gives rho=max(localradius,F-headx), so max(rho-22,0) decreases by the exact head increment at sampled contacts whilepositive. Relevant cardinality need not decrease and no fine-time potential is claimed.',
'Six full finite controls, all contact fields/lifetime fates, final complete fields and infinite tails independently replay. The all-word/all-gap theorem is the guard induction, not the incomplete32-node exploratory tree or these samples. Paid finite sufficient class only: no arbitrary-ray coverage, autonomous input regeneration, general bounded-state encoding, universal compact recurrence or global attraction.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')));print(controls)
