from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'LAST_M_REGISTER_SCATTERING_MANIFEST.json';assert sha(MF)=='f78459ea17f25c93fa4d2cd69fbf94c95372738f990dc10a979e78609d59acae';mf=json.loads(MF.read_text())
for kind in ('files','dependencies'):
 for f,h in mf[kind].items():assert sha(D/f)==h
J=json.loads((D/'LAST_M_REGISTER_SCATTERING_CHECKED.json').read_text())
ns={'__file__':str(S.with_name('check_southwest_archive_import_independent.py'))};exec(Path(ns['__file__']).read_text().split('B100=expand')[0],ns)
K,W,Q,H,V,xy,rot,geometry,sim,cert,key,M,T,TQ,TH,post,qm,TM,base,base_seed,source,local,MJ,SWJ=[ns[k]for k in('K','W','Q','H','V','xy','rot','geometry','sim','cert','key','M','T','TQ','TH','post','qm','TM','base','base_seed','source','local','MJ','J')] if 'rot'in ns else [ns.get(k)for k in('K','W','Q','H','V','xy','rot','geometry','sim','cert','key','M','T','TQ','TH','post','qm','TM','base','base_seed','source','local','MJ','J')]
# rot is unused: all packet coordinates share the original physical frame.
enc=lambda q:sorted(map(xy,q));dec=lambda q:{complex(*p)for p in q};d=2+2j;quad=lambda p:p.real<=38 and p.imag>=-43;normal=lambda p:p.real-p.imag
remote={q-qm for q in dec(SWJ['exact_entry_pruning']['remote'])};baseQ={q-qm for q in dec(SWJ['controls'][0]['whole_post_event_black'])if quad(q-qm)};assert enc(baseQ)==J['registered_quadrant']and enc(remote)==J['remote_last_M_pruning']and enc(local)==J['local_T_pruning']
assert len(remote)==786 and all(quad(q)for q in remote)
modes={}
for label in'SM':
 r=MJ['modes'][label];z=cert(sim(dec(r['kernel']),len(r['recovery_word']),0j,0,r['recovery_word']),r['tail_word']);assert enc(z['B'])==r['complete_output_black']and max(q.imag for q in z['B'])<=31
 if label=='S':assert(min(map(normal,z['B'])),max(map(normal,z['B'])))==(-8,4)
 tq,_,_,_=geometry(z['p'],z['h'],z['tail']);assert min(q.real for q in z['pts']+tq)>=r['west_guard_x'] if 'west_guard_x'in r else min(q.real for q in z['pts']+tq)>=-23
 modes[label]=z
assert max(q.real for q in M['pts'])<=38 and min(q.imag for q in M['pts'])>=-43
pr,_,pe,ph=geometry(5+28j,1,post);tail=SWJ['controls'][0]['complete_future_certificate']['tail_word'];pq,_,_,_=geometry(pe,ph,tail);assert(pe,ph)==(-47+14j,1)and(max(q.real for q in pr+pq),min(q.imag for q in pr+pq))==(38,-43)
# Reconstruct the whole infinite-quadrant incoming board, not the M west crop.
incoming=set()
for i,p in enumerate(Q):
 r=p-Q[13];lo=-((int(r.imag)+43)//2);hi=min(0 if i<13 else-1,(38-int(r.real))//2)
 for a in range(lo,hi+1):incoming.symmetric_difference_update({r+a*d})
Mbits={a*d for a in(0,1,6,8)};assert all(quad(q)for q in Mbits)and not incoming&Mbits;incoming|=Mbits
mb=sim(base_seed,TM,expected=source);assert {q-qm for q in mb['B']if quad(q-qm)}==incoming
# Previous outputs and omitted synthetic past are below the quadrant after
# every permitted206/228 shift, while every later paid input is to its east.
assert 31-206<-43 and 206>38 and max(p.imag for p in K)-201<-43
for label in'SM':
 z=modes[label];phase=MJ['modes'][label]['output_phase'];pastmax=z['p'].imag+max(Q[i].imag-Q[phase].imag+(0 if i<phase else-2)for i in range(104));assert pastmax<=31
# ALL outgoing NE phase rays inside Q, using derived exact integer bounds.
fq,fh,_,_=geometry(M['p'],M['h'],M['tail']);ne=[]
for i,p in enumerate(fq):
 lo=max(0,-((int(p.imag)+43)//2));hi=(38-int(p.real))//2
 for k in range(lo,hi+1):ne.append((104*k+i,p+k*d))
ne.sort();assert max(t for t,q in ne)==788<10400 and sorted((t,tuple(xy(q)))for t,q in ne)==sorted((t,tuple(q))for t,q in J['all_NE_quadrant_reads'])and J['last_NE_quadrant_read']==788
before=set(incoming)
for q in M['pts']+[q for t,q in ne]:
 if quad(q):before.symmetric_difference_update({q})
# Every T finite prefix is east ofQ, and extra SW periods added by increasingD
# are also east. ReindexSW by r=D-k; all full periods have r>=22; finalpartialr21.
assert min(q.real for q in T['pts'])==-38 and 228-38>38
assert min(q.real for q in TQ)+228>38
sw=[]
Dbase=114
for r in range(Dbase,21,-1):
 for i,q in enumerate(TQ):
  p=q+r*d
  if quad(p):sw.append((r,i,p))
for i,q in enumerate(TQ[:100]):
 p=q+21*d
 if quad(p):sw.append((21,i,p))
after=set(before)
for r,i,q in sw:after.symmetric_difference_update({q})
after.symmetric_difference_update({4+28j});assert after==baseQ
# All384 latest-M encounter constants shift uniformly by104D; older M has
# strictly larger D. Standard/S inventories miss the return strip entirely.
assert len(SWJ['all_affine_old_output_hits'])==384 and min(r['time_offset']-104*14 for r in SWJ['all_affine_old_output_hits'])==9148
controls=[];reads=0
for row in J['controls']:
 labels=row['prior_modes']+'T';gaps=row['gaps'];seed=set(K);word='';p=0j;phase=0;packets=[]
 for lab,n in zip(labels,gaps):
  assert n>=100;q=p+(n+int(13<phase))*d+Q[13]-Q[phase];fw=W[phase:]+W[:phase];word+=fw*n+fw[:(13-phase)%104];t=len(word);indices=[0,1,3,5,6]if lab=='T'else MJ['modes'][lab]['packet_black_indices'];bits={q+a*d for a in indices};assert not bits&seed;seed|=bits;packets.append(dict(mode=lab,origin=xy(q),time=t,indices=indices))
  if lab=='T':break
  word+=modes[lab]['word'];p=q+modes[lab]['p'];phase=MJ['modes'][lab]['output_phase']
 assert packets==row['packets']and enc(seed)==row['seed'];tT=len(word);qt=q;word+=T['word'];last=next((z for z in reversed(packets)if z['mode']=='M'),None);event=None
 if last:
  qM=complex(*last['origin']);dist=qt-qM;DD=int(dist.real)//2;assert dist==DD*d and DD>=114;word+=T['tail']*(DD-21)+T['tail'][:100];event=len(word);assert event-tT==104*DD+9148;word+='L'+post
 assert word==row['complete_word']and tT==row['T_contact']and event==row['marked_event'];cuts={tT}
 if event is not None:cuts|={event,event+1}
 z=cert(sim(seed,len(word),expected=word,cuts=cuts),row['tail_word']);reads+=len(word);B,p,h=z['snap'][tT];assert(p,h)==(qt,0)and sorted([[xy(q),i]for q,i in B.items()])==row['T_full_black']
 assert{q-qt for q in B if q.imag>=qt.imag-15}==dec(SWJ['T_kernel'])
 for pkt in packets:
  oq=complex(*pkt['origin']);assert all(z['first'][oq+a*d]>=pkt['time']for a in pkt['indices'])
 C={q for q,i in B.items()if i in z['dead']};expected={qt+q for q in local}
 if last:
  expected|={qM+q for q in remote};pre,ep,eh=z['snap'][event];bb,ap,ah=z['snap'][event+1];hit=qM+4+28j;birth=last['time']+9752
  assert(ep,eh)==(hit,2)and pre[hit]==birth and z['events'][event]==birth and z['dead'][birth]==event and(ap,ah)==(qM+5+28j,1)
  assert{q-qM for q in bb if quad(q-qM)}==baseQ and {q-qM for q in B if quad(q-qM)}==before
  assert enc(pre)==row['event_full_black']and enc(baseQ)==row['post_event_quadrant']and(z['p'],z['h'],z['d'])==(qM-47+14j,1,-2+2j)
  rho=2*DD+44
 else:assert z['d']==-d;rho=18
 assert C==expected and enc(C)==row['T_entire_pruning']and max(max(abs((q-qt).real),abs((q-qt).imag))for q in C)==rho==row['T_entire_radius']
 assert enc(z['B'])==row['terminal_full_black']and[xy(z['p']),z['h']]==row['terminal_pose']and z['tests']==row['parity_tests']
 controls.append(dict(modes=labels,reads=len(word),relevant=len(C),radius=rho,event=event,tail_checks=z['tests']))
assert reads==644310
out=dict(status='PASS all finite protected S/M prefixes followed by T, latest-M register and whole-quadrant capture',manifest=sha(MF),script=sha(S),NE_quadrant_last_read=788,quadrant_input_mass=len(incoming),quadrant_postevent_mass=len(baseQ),controls=controls,total_reads=reads,analytic_review=['The original S/M guard induction supplies every finite prefix with gaps>=100. Relative to the latestM, all earlier actual outputs and omitted synthetic past have y<=31-206<-43; originalK lies still lower. The actual final canonical flight produces the exact whole mature phase13 field in x<=38,y>=-43, reconstructed independently from all past phase rays. Later original inputs are east. This is NOT just the M147 western crop.','The M recovery lies wholly inside that quadrant. Exact integer bounds on every NE phase ray give its last quadrant read788, strictly before any next packet. All later S recoveries and flights stay east, and T prefix minx=-38 still stays east with head separation>=228. Reindexing the backwardSW train by r=D-k gives fixed in-quadrant events with r>=22 plus partialr21; extra earlier periods are northeast. Thus the ENTIRE post-L quadrant equals the reference for arbitrary prefix length and all gaps, not merely six samples.','AllS output lies in transverse strip[-8,4], standard/source in[-8,2]; neither meets SW[-32,-22]. EachM retains its exact82 strip outputs and384 phase encounters. Earliest encounter is104D+9148; olderM has strictly largerD, so the latestM is first. This ordered register fact is specific to these protected diagonal placements, not general LIFO.','The actual post-L48464 word and infiniteNW rays stay in the certified quadrant. Earlier packet debris is below and later S/T debris east, so first-difference induction transfers the full future with every archive bit retained. WithoutM the SW tail misses the whole source/S field. Arbitrary western archive is expressly excluded.','Entire T-entry C* is99 local plus786 at latestM when present, otherwise99. PriorM fields cannot add inputs because the full future misses them; after the first import the current quadrant and its future are fixed. This yields rho=2D+44, an unbounded position register, not a bounded-radius state or finite-state full-board encoding.','Six whole finite histories total644310 reads with complete source/entry/event/terminal fields, exact lifetime births and deaths, and infinite-tail certificates. Paid finite sufficient language only, no autonomous regeneration, arbitrary packet coverage or global attraction.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')));print(controls)
