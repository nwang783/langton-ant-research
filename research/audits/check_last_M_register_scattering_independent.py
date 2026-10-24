from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'LAST_M_REGISTER_SCATTERING_MANIFEST.json';assert sha(MF)=='f78459ea17f25c93fa4d2cd69fbf94c95372738f990dc10a979e78609d59acae';mf=json.loads(MF.read_text())
for kind in('files','dependencies'):
 for f,h in mf[kind].items():assert sha(D/f)==h
J=json.loads((D/'LAST_M_REGISTER_SCATTERING_CHECKED.json').read_text());PJ=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());AJ=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text())
for fn,prefix in[('check_recursive_phase13_packet_independent.json','b5866d4e'),('check_southwest_archive_import_independent.json','600f91c4')]:
 f=R/'audits'/fn;assert sha(f).startswith(prefix)and json.loads(f.read_text())['status'].startswith('PASS')
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);K,V,xy,future,phases,geometry,sim,cert,key=[ns[k]for k in('K','V','xy','future','phases','geometry','sim','cert','key')]
enc=lambda q:sorted(map(xy,q));dec=lambda q:{complex(*v)for v in q};d=2+2j;W=sim(K,104)['word'];Q,H,_,_=geometry(0j,1,W);quad=lambda p:p.real<=38 and p.imag>=-43;shift=lambda B,q:{p+q for p in B}
def odd(P):
 B=set()
 for p in P:B.symmetric_difference_update({p})
 return B
modes={}
for lab in'SM':
 row=PJ['modes'][lab];z=cert(sim(dec(row['kernel']),len(row['recovery_word']),0j,0,row['recovery_word']),row['tail_word']);assert enc(z['B'])==row['complete_output_black']and max(p.imag for p in z['B'])<=31;fq,fh,_,_=geometry(z['p'],z['h'],z['tail']);assert min(p.real for p in fq)>=-23
 if lab=='S':assert all(-8<=p.real-p.imag<=4 for p in z['B'])
 modes[lab]=z
M=modes['M'];T=cert(sim(dec(AJ['T_kernel']),11232,0j,0,AJ['T_recovery']),AJ['T_tail_word']);TQ,TH,_,_=geometry(T['p'],T['h'],T['tail']);post=AJ['postcollision_word'];postQ,postH,ep,eh=geometry(5+28j,1,post);NW=AJ['controls'][0]['complete_future_certificate']['tail_word'];nwQ,_,nd,nh=geometry(ep,eh,NW)
assert(ep,eh,nd-ep,nh)==(-47+14j,1,-2+2j,1)and max(p.real for p in postQ+nwQ)==38 and min(p.imag for p in postQ+nwQ)==-43
assert all(quad(p)for p in M['pts'])and min(p.real for p in T['pts'])==-38
# Exact incoming mature field on the WHOLE infinite quadrant, derived from
# all prior canonical phase rays. Both inequalities give finite integer ranges.
qin=set()
for i,p in enumerate(Q):
 r=p-Q[13];lo=-((43+int(r.imag))//2);hi=min((38-int(r.real))//2,0 if i<13 else-1)
 for k in range(lo,hi+1):qin.symmetric_difference_update({r+k*d})
qin|={a*d for a in(0,1,6,8)}
qm=202+201j;qt=430+429j;seed=K|{qm+a*d for a in(0,1,6,8)}|{qt+a*d for a in(0,1,3,5,6)};z=sim(seed,10413,expected=W*100+W[:13]);assert{p-qm for p in z['B']if quad(p-qm)}==qin
# Earlier outputs/formal prestart are below quadrant, while later paid inputs
# lie east. These inequalities are uniform under every allowed head gap.
assert 31-206<-43 and max(p.imag for p in K)-201<-43
assert 206-23>38 and 228-38>38
# Exactly all NE tail reads in quadrant, with solved integer bounds (no k cap).
fq,_,_,_=geometry(M['p'],M['h'],M['tail']);ne=[]
for i,p in enumerate(fq):
 lo=max(0,-((43+int(p.imag))//2));hi=(38-int(p.real))//2
 for k in range(lo,hi+1):ne.append((104*k+i,p+k*d))
ne.sort();assert [[t,xy(p)]for t,p in ne]==sorted(J['all_NE_quadrant_reads'])and max(t for t,p in ne)==J['last_NE_quadrant_read']==788<10420
# Return SW reads use r=D-k. All full periods have r>=22, final partial r21.
# Every quadrant solution has r<=rmax<114. Therefore everyD>=114 has
# IDENTICAL ordered quadrant prefix before the marked L.
sw=[];rmax=-10**9
for i,p in enumerate(TQ):
 lo=max(22,-((43+int(p.imag))//2));hi=(38-int(p.real))//2;rmax=max(rmax,hi)
 for r in range(lo,hi+1):sw.append((-104*r+i,p+r*d))
for i,p in enumerate(TQ[:100]):
 if quad(p+21*d):sw.append((-104*21+i,p+21*d))
sw.sort();assert rmax<114 and TH[100]==2 and TQ[100]+21*d==4+28j
qb=qin^odd(M['pts'])^odd(p for t,p in ne)^odd(p for t,p in sw)^{4+28j};assert enc(qb)==J['registered_quadrant']
basepost=dec(AJ['controls'][0]['whole_post_event_black']);assert qb=={p-qm for p in basepost if quad(p-qm)}
remote=dec(AJ['exact_entry_pruning']['remote']);remote={p-qm for p in remote};local=dec(AJ['exact_entry_pruning']['local']);assert enc(remote)==J['remote_last_M_pruning']and enc(local)==J['local_T_pruning']and all(quad(p)for p in remote)
# All384 per-M return hits translate to104D+constant; earliest9148, and a
# strictly older diagonal origin has a strictly later earliest event.
hits=AJ['all_affine_old_output_hits'];assert len(hits)==384 and min(r['time_offset']-104*14 for r in hits)==9148 and all(114+r['period_offset']-14>=0 for r in hits)
controls=[];total=0
for row in J['controls']:
 labels=row['prior_modes'];gaps=row['gaps'];seed=set(K);prefix='';p=0j;phase=0;packets=[]
 for lab,n in zip(labels+'T',gaps):
  assert n>=100;word=W[phase:]+W[:phase];q=p+(n+int(phase>13))*d+Q[13]-Q[phase];prefix+=word*n+word[:(13-phase)%104];indices=[0,1,3,5,6]if lab=='T'else PJ['modes'][lab]['packet_black_indices'];bits={q+a*d for a in indices};assert not bits&seed;seed|=bits;packets.append((lab,q,len(prefix),indices))
  if lab=='T':break
  prefix+=modes[lab]['word'];p=q+modes[lab]['p'];phase=PJ['modes'][lab]['output_phase']
 tT=len(prefix);qT=q;prefix+=T['word'];mm=next((x for x in reversed(packets)if x[0]=='M'),None);ev=None
 if mm:
  _,qM,tM,_=mm;dist=qT-qM;assert dist.real==dist.imag and int(dist.real)%2==0;dd=int(dist.real)//2;assert dd>=114;prefix+=T['tail']*(dd-21)+T['tail'][:100];ev=len(prefix);assert ev-tT==104*dd+9148;prefix+='L'+post
 assert prefix==row['complete_word']and enc(seed)==row['seed'];cuts={tT}|({ev,ev+1}if mm else set());z=cert(sim(seed,len(prefix),expected=prefix,cuts=cuts),row['tail_word']);total+=len(prefix)
 B,p,h=z['snap'][tT];assert(p,h)==(qT,0)and{p-qT for p in B if p.imag>=qT.imag-15}==dec(AJ['T_kernel']);assert sorted([[xy(p),i]for p,i in B.items()])==row['T_full_black']
 Cstar={p for p,i in B.items()if i in z['dead']};want=shift(local,qT)
 for(lab,org,t,indices),given in zip(packets,row['packets']):
  assert given==dict(mode=lab,origin=xy(org),time=t,indices=indices)
  assert all(z['first'][org+a*d]>=t for a in indices)
 if mm:
  want|=shift(remote,qM);before,pp,hh=z['snap'][ev];after,_,_=z['snap'][ev+1];assert(pp,hh)==(qM+4+28j,2)and before[pp]==tM+9752 and z['dead'][tM+9752]==ev
  assert{p-qM for p in after if quad(p-qM)}==qb and enc(before)==row['event_full_black']and enc(qb)==row['post_event_quadrant']
  assert(z['p'],z['h'],z['d'])==(qM-47+14j,1,-2+2j)and z['tail']==NW;rho=2*dd+44;assert len(Cstar)==885
 else:assert len(Cstar)==99 and z['tail']==T['tail']and z['d']==-d;rho=18
 assert Cstar==want and enc(Cstar)==row['T_entire_pruning']and max(max(abs((p-qT).real),abs((p-qT).imag))for p in Cstar)==rho==row['T_entire_radius']
 assert enc(z['B'])==row['terminal_full_black']and[xy(z['p']),z['h']]==row['terminal_pose']and xy(z['d'])==row['tail_drift']and z['tests']==row['parity_tests'];controls.append(dict(modes=labels+'T',gaps=gaps,reads=len(prefix),relevant=len(Cstar),rho=rho,parity_checks=z['tests']))
assert total==644310
out=dict(status='PASS all finite protected S/M prefixes thenT, exact latest-M register and whole-quadrant future',manifest=sha(MF),script=sha(S),whole_quadrant_input_cells=len(qin),whole_quadrant_postcollision_cells=len(qb),last_NE_quadrant_read=788,largest_SW_quadrant_r=rmax,control_reads=total,controls=controls,analytic_review=['The fixed13 source and paid S/M/T origins inherit exact full-field forward interfaces. Every S output misses the SW return strip; every M has the complete82-cell surviving strip inventory. All384 exact ray hits for a particularM have earliest104D+9148. Older origins have largerD, so the LATESTM is genuinely first, not an assumed global stack rule. Source/standard/S cells are excluded by full transverse support.','An independent all-past ray XOR reconstructs the ENTIRE incoming quadrant x<=38,y>=-43 at latestM, including standard old cells outside the147-cell M comparison kernel. Earlier outputs and formal prestart are below it by31-206<-43; later paid inputs are east. This is the essential complete-field correction, not a cropped-kernel argument.','M recovery stays wholly in that quadrant. Exact integer ray bounds enumerate every outgoing NE quadrant visit, last788 before any allowed nextpacket. Every intervening S recovery/flight is east, and T minimumx-38 with distance>=228 is east as well. The returning train is reindexed r=D-k; all quadrant solutions have boundedr<114, so every permittedD has identical ordered quadrant reads up to the same physicalL. Direct XOR reconstructs the full postL quadrant exactly.','The entire48464 recovery and NW rays stay x<=38,y>=-43, hence first-difference induction transfers the actual infinite future with all outside archive retained. EarlierM debris is below and interveningS/T debris east. No arbitrary western archive is allowed, unlike the earlier forward-only S/M theorem.','AtT entry the actual local99 and latestM remote786 are exact future-consumed cohorts. Every other current cell is either outside the read strips/quadrant or a reference-unread local bit; the quadrant full field and future are identical. Thus C*=99 or99+786 for any finite prefix, andrho=18 or2D+44. No other historicalM is silently pruned without the all-future exclusion.','Six complete finite histories total644310 actual reads, full entry/event/terminal fields, originalfirstread ownership and infinite parity pass independently. The universal finite-word conclusion is the support induction, not the six examples. This is a paid restricted source class with an unbounded coordinate register, not finite-state full dynamics, arbitrary packet/oldarchive closure, autonomous regeneration, or universal attraction.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')));print(controls)
