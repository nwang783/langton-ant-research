from pathlib import Path
import hashlib,json
S=Path(__file__);D=S.parents[1]/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'PRISTINE_RECORD_AFTER_RETIREMENT_MANIFEST.json';assert sha(MF)=='802c8898531f196550a4b708c9cd00c34793b5aa67b53229ed8a227ea281ec29';mf=json.loads(MF.read_text())
for kind in('files','dependencies'):
 for f,h in mf[kind].items():assert sha(D/f)==h
J=json.loads((D/'PRISTINE_RECORD_AFTER_RETIREMENT_CHECKED.json').read_text());A=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());Rj=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);K,xy,geometry,sim,cert,key=[ns[k]for k in('K','xy','geometry','sim','cert','key')];enc=lambda q:sorted(map(xy,q));dec=lambda q:{complex(*p)for p in q};d=2+2j;W=sim(K,104)['word'];Q,H,_,_=geometry(0j,1,W);qm=202+201j;tm=10413
kernel=dec(A['T_kernel']);word=A['T_recovery'];z=cert(sim(kernel,len(word),0j,0,word,cuts={6009,6942}),A['T_tail_word']);assert z['tail']==W[65:]+W[:65];local={}
for cut,wantp,wanth,wantmass in[(6009,13+10j,1,335),(6942,3+21j,0,345)]:
 B,p,h=z['snap'][cut];assert(p,h)==(wantp,wanth);C={q for q,i in B.items()if i in z['dead']};assert len(C)==wantmass;local[cut]=C
 if cut==6009:assert enc(C)==J['local_record_pruning']and max(max(abs((q-p).real),abs((q-p).imag))for q in C)==41 and all(q.real<p.real for q in B)
 else:assert enc(C)==J['north_record_local']['pruning']and all(q.imag<p.imag for q in B)
 assert max(z['dead'][i]for q,i in B.items()if q in C)<104*100+10604
 assert min(q.real for q in B)>=-38 and qm.real+228-38>qm.real+38
remote=dec(A['exact_entry_pruning']['remote']);assert len(remote)==786 and enc(remote)==J['remote_pruning'];assert(min(q.real for q in remote),max(q.real for q in remote),min(q.imag for q in remote),max(q.imag for q in remote))==(158,225,162,229)
# Affine all-n flight extrema. Only n-dependent coordinates are +2n; every slope is nonnegative.
fixed=W*100+W[:13]+Rj['modes']['M']['recovery_word'];fp,fh,end,eh=geometry(0j,1,fixed);assert end==qm+complex(*Rj['modes']['M']['output_pose'][0]);flight=W[41:]+W[:41];fq,_,fd,hh=geometry(end,eh,flight);assert fd-end==d and hh==eh;partial,_,pe,ph=geometry(end,eh,flight[:76]);assert pe==qm+28+28j and ph==0
# At n>=100, exact preT extrema are the extremal affine terms from fixed, first/last period and partial.
pre_bounds={}
for coord,name in[(lambda q:q.real,'x'),(lambda q:q.imag,'y')]:
 fixed_min=min(map(coord,fp));fixed_max=max(map(coord,fp));fmin=min(map(coord,fq));fmax=max(map(coord,fq));pmin=min(map(coord,partial));pmax=max(map(coord,partial));assert fixed_min<=fmin and fixed_min<=pmin+200
 max_intercept=max(fmax-2,pmax);assert fixed_max<=max_intercept+200
 pre_bounds[name]=dict(min=int(fixed_min),max_intercept=int(max_intercept),max_slope=2)
 assert max_intercept-coord(pe)<= (12 if name=='x' else 20)
# Exact local record trace gives maxima before6009/6942 and rules out intervening positive-axis records.
assert max(q.real for q in z['pts'][:6009])==12 and max(q.imag for q in z['pts'][:6942])==20
for t in range(6001,6009):assert z['pts'][t].real<=max(q.real for q in z['pts'][:t])and z['pts'][t].imag<=max(q.imag for q in z['pts'][:t])
assert min(q.real for q in z['pts'][6001:6943])+qm.real+228>pre_bounds['x']['min']and min(q.imag for q in z['pts'][6001:6943])+qm.imag+228>pre_bounds['y']['min']
controls=[];total=0
for row in J['controls']:
 n=row['n'];qt=qm+(n+14)*d;seed=K|{qm+a*d for a in(0,1,6,8)}|{qt+a*d for a in(0,1,3,5,6)};assert len(seed)==22 and enc(seed)==row['seed'];pre=fixed+flight*n+flight[:76];entry=len(pre);assert entry==21201+104*n==row['T_contact'];u=entry+6000;cuts={entry+6009,entry+6942};full=pre+word+A['T_tail_word']*(n-7)+A['T_tail_word'][:100]+'L'+A['postcollision_word'];zz=cert(sim(seed,len(full),expected=full,cuts=cuts),row['tail_word']);assert len(full)==80270+208*n==row['terminal_cut'];deaths=sorted([i,t]for i,t in zz['dead'].items()if i<0);assert len(deaths)==22 and deaths==row['all_original_consumptions']and max(t for i,t in deaths)==u==row['original_retirement_update']
 hist=[0,0,0,0];firstpost=None;firstnorth=None;at={}
 for t,q in enumerate(zz['pts']):
  vals=[q.real,q.real,q.imag,q.imag];rec=[i for i in range(4)if(vals[i]<hist[i]if i%2==0 else vals[i]>hist[i])]
  if t in cuts:at[t]=(hist[:],rec)
  if t>=u+1 and rec:
   if firstpost is None:firstpost=t
   if firstnorth is None and 3 in rec:firstnorth=t
  hist=[min(hist[0],vals[0]),max(hist[1],vals[1]),min(hist[2],vals[2]),max(hist[3],vals[3])]
 assert firstpost==entry+6009 and firstnorth==entry+6942
 for cut in(6009,6942):
  t=entry+cut;B,p,h=zz['snap'][t];expectp=qt+(13+10j if cut==6009 else 3+21j);assert p==expectp and all(i>=0 for i in B.values());C={q for q,i in B.items()if i in zz['dead']};assert C=={qt+q for q in local[cut]}|remote
  rho=max(max(abs((q-p).real),abs((q-p).imag))for q in C);assert rho==2*n+(85 if cut==6009 else 88)
  if cut==6009:
   assert at[t][1]==[1]and at[t][0]==row['past_head_extrema']and sorted([[xy(q),i]for q,i in B.items()])==row['whole_current_black']and enc(C)==row['entire_current_pruning'];assert max(q.real for q in seed)==p.real-1 and all(q.real<p.real for q in B)
  else:
   rr=row['north_record'];assert at[t][1]==[3]and at[t][0]==rr['past_extrema']and sorted([[xy(q),i]for q,i in B.items()])==rr['whole_black']and enc(C)==rr['entire_pruning'];assert max(q.imag for q in seed)<p.imag and all(q.imag<p.imag for q in B)
 B,p,h=zz['snap'][entry+6009];mark=qm+4+28j;assert B[mark]==tm+9752 and zz['dead'][tm+9752]==entry+104*n+10604;assert entry+6009-(tm+9752)==104*n+7045 and zz['dead'][tm+9752]-(entry+6009)==104*n+4595
 assert enc(zz['B'])==row['terminal_full_black']and[xy(zz['p']),zz['h']]==row['terminal_pose']and xy(zz['d'])==row['tail_drift']and zz['tests']==row['infinite_parity_tests'];total+=len(full);controls.append(dict(n=n,reads=len(full),last_original=u,first_record=firstpost,first_north=firstnorth,radii=[2*n+85,2*n+88]))
# Exact finite pruned local limit, no external field substituted into a finite family member.
L={q-13-10j for q in local[6009]};lim=J['local_limit'];assert enc(L)==lim['seed']and len(L)==335;ll=cert(sim(L,len(lim['finite_prefix']),0j,1,lim['finite_prefix']),lim['tail_word']);assert len(lim['finite_prefix'])==5223 and ll['d']==-2-2j and all(-i-1 in ll['dead']for i in range(len(L)))and enc(ll['B'])==lim['terminal_full_black']and[xy(ll['p']),ll['h']]==lim['terminal_pose']and ll['tests']==lim['parity_tests']
O={'status':'PASS all-n genuinely pristine post-original-retirement record countercontrol ONLY','manifest':sha(MF),'script':sha(S),'all_n_affine_preT_bounds':pre_bounds,'local_sets':[335,345],'remote_set':786,'entire_record_counts':[1121,1131],'radii':['2n+85','2n+88'],'controls':controls,'full_reads':total,'finite_limit_count':335,'finite_limit_radius':41,'analytic_review':['Signed whole22-cell MT family supplies alln>=100 actual futures. Independent affine fullflight extrema retain both fixedprehistory and every period, not just Tlocal records. LastoriginalupdateT+6000, firstemptycohortcut+6001, firstnextfour-coordinatehistoricalrecord+6009 andfirstnorthrecord+6942 are exact. The first occurs8updates after the emptycut,9afterthelastLupdate.','At easthead(13,10) andnorthhead(3,21), all originalsites andallpastheadsites lie strictlybehind the respectivecoordinate. EverynewBLACK wasborn atapasthead, so ENTIRE currentforwardhalfplanesareWHITE, not merelya boundedobservedguard. All22originals arephysicallydead.','Purelocal fullfuture gives335/345 currentrelevant sets, andeveryfutureconsumptionofthose locallifetimes occurs beforetheminimumpossible oldcollision. Allcurrentlocalcells lieeast ofthelaterwhole postreturnquadrant, so comparisonpermanence isactuallypreserved. Remote786 isnotreadintheearlier southernregion andallits SAMEidentities remainfutureconsumed. OlderidentityoutsideentryC* remainsforeverunread. Thus exact1121/1131 decomposition isall-n,notinterpolation.','Exactremote bbox158..225,162..229 plusaffineheads yieldsrho2n+85/88. Threewholehistories independentlyverify fullfields,alloriginaldeaths,records,entireprunings,markbirth/death andcanonical infinitefutures. NorthispositiveprojectionofactualNWfinaldrift.','Normalizedtruepruned states havefixed335localcells plus786 cellsescapingSW. The finite335 limit is fullypruned andcapturesSW after5223, whilefamilymemberscaptureNW afterremote feedback. The firstomittedinput occurs104n+4595 aftereastrecord, diverging. FixedcellBLACK-and-future-read hasafiniteprefixwitness,so rhoislowersemicontinuous,notnecessarilyupper; noexactone-orbitstate repetition followsfromthisproductlimit.','Onlya uniform across-family next-clear-record compactness rule basedonoriginalmass,currentpopulation andretirementdelayisrefuted. Everymembercapturesandhasorbit-dependenteventualcompactrecurrence. Noone-orbitnoncapture,initialdiameter-independentgeneral theorem,noncomputability orboundedall-timepopulation claim ismade.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
