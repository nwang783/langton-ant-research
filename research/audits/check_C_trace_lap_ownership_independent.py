from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'C_TRACE_LAP_OWNERSHIP_AND_FIXED_GEOMETRY_RIGIDITY.md';JF=D/'C_trace_lap_ownership_certificate.json';assert sha(P).startswith('53933f0c')and sha(JF).startswith('bf93aa87')and sha(D/'certify_C_trace_lap_ownership.py').startswith('5f03f890');J=json.loads(JF.read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
base=json.loads((D/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls'];V=(1j,1,-1j,-1);off=(-1j,-1-1j,-1,0j);xy=lambda p:[int(p.real),int(p.imag)]
def events(w,h=0,p=0j):
 start=p;E=[]
 for t,c in enumerate(w):
  hi=h;h=(h+(1 if c=='R'else-1))%4;E.append(dict(t=t,p=p,hi=hi,ho=h,c=c));p+=V[h]
 return E,p-start,h

def build(w,h0=0):
 E,d,hh=events(w,h0);assert hh==h0 and d
 cut=(max(e['t']for e in E if e['c']=='L')+1)%len(w);ww=w[cut:]+w[:cut];p=E[cut]['p'];h=E[cut]['hi'];start=p;hstart=h;ks=list(map(len,ww.split('L')[:-1]));assert ww.endswith('L')and all(k in(0,1,2,4)for k in ks);N=len(ks);opts=[i for i,k in enumerate(ks)if k in(0,4)];hist={};cursors=[]
 def rep(p):
  v=d.real if d.real else d.imag;a=p.real if d.real else p.imag;k=int(a//abs(v))*(1 if v>0 else-1);return p-k*d,k
 def add(i,j,p,c,v):
  q,k=rep(p);e=dict(block=i,slot=j,p=xy(p),**{'class':xy(q)},lift=k,order=[i-N*k,j],kind=c,var=v);hist.setdefault(q,[]).append(e)
 for i,k in enumerate(ks):
  cursors.append([xy(p),h,xy(p+off[h])]);a=p+off[h]
  if i in opts:
   pp,hh=p,h
   for j in range(4):add(i,j,pp,'R',i);hh=(hh+1)%4;pp+=V[hh];assert pp+off[hh]==a
   assert(pp,hh)==(p,h)
  else:
   for j in range(k):add(i,j,p,'R',None);h=(h+1)%4;p+=V[h];assert p+off[h]==a
  add(i,4,p,'L',None);h=(h-1)%4;p+=V[h];assert p+off[h]!=a
 assert p-start==d and h==hstart
 for es in hist.values():es.sort(key=lambda e:e['order'])
 return dict(word=ww,cut=cut,drift=xy(d),heading=hstart,position=xy(start),ks=ks,optional=opts,chosen={str(i):int(ks[i]==4)for i in opts},cursors=cursors,maximal_candidate_histories=[{'class':xy(q),'events':es}for q,es in sorted(hist.items(),key=lambda kv:(kv[0].real,kv[0].imag))]),hist

def constraints(hist,white=True):
 C=[];bad=[]
 def emit(q,typ,es,target):
  C.append(dict(**{'class':xy(q)},type=typ,vars=[e['var']for e in es],target=target,occurrences=[dict(phase=e['var'],voltage=-e['lift'],block=e['block'],slot=e['slot'],position=e['p'],order=e['order'])for e in es]))
 for q,es in hist.items():
  ind=[i for i,e in enumerate(es)if e['var']is None]
  if not ind:emit(q,'all_optional',es,'<=1');continue
  emit(q,'prefix_'+es[ind[0]]['kind'],es[:ind[0]],0 if es[ind[0]]['kind']=='R'else(1 if white else'<=1'))
  for a,b in zip(ind,ind[1:]):
   typ=es[a]['kind']+es[b]['kind']
   if typ=='RR':bad.append(dict(**{'class':xy(q)},type='mandatory_RR',events=[es[a],es[b]]))
   emit(q,typ,es[a+1:b],1 if typ=='LL' else 0)
  emit(q,'suffix_'+es[ind[-1]]['kind'],es[ind[-1]+1:],0 if es[ind[-1]]['kind']=='R'else'<=1')
 return C,bad

def force(C,bad):
 vals={};thr={};steps=[]
 if bad:return False,vals,thr,steps
 while True:
  old=len(vals)
  for j,c in enumerate(C):
   cap=1 if c['target']=='<=1'else c['target'];known=sum(vals.get(v,0)for v in c['vars']);unknown=[v for v in c['vars']if v not in vals];cut=max([0]+[thr[e['phase']]-e['voltage']for e in c['occurrences']if e['phase']in vals])
   if known>cap or(c['target']!='<=1'and known+len(unknown)<cap):return False,vals,thr,steps
   if known==cap:value=0
   elif c['target']!='<=1'and known+len(unknown)==cap:value=1
   else:continue
   for v in sorted(set(unknown)):
    assert value==0 or unknown==[v]
    vals[v]=value;thr[v]=cut+min(e['voltage']for e in c['occurrences']if e['phase']==v);steps.append((j,v,value,thr[v]))
  if old==len(vals):return True,vals,thr,steps

def replay_proof(C,bad,p):
 assert C==p['constraints']and bad==p['mandatory_RR'];vals={};th={}
 for s in p['proof']:
  c=C[s['constraint']];v=s['phase'];value=s['value'];assert v not in vals and v in c['vars'];cap=1 if c['target']=='<=1'else c['target'];known=sum(vals.get(x,0)for x in c['vars']);un=[x for x in c['vars']if x not in vals];cut=max([0]+[th[e['phase']]-e['voltage']for e in c['occurrences']if e['phase']in vals]);assert cut==s['relative_anchor_threshold']
  if value==0:assert known==cap
  else:assert c['target']!='<=1'and un==[v]and known+1==cap
  threshold=cut+min(e['voltage']for e in c['occurrences']if e['phase']==v);assert threshold==s['relative_phase_threshold'];vals[v]=value;th[v]=threshold
 assert{str(k):v for k,v in vals.items()}==p['values']and{str(k):v for k,v in th.items()}==p['thresholds']
 if not p['possible']:
  if bad:assert p['contradiction']==bad[0]
  else:
   c=C[p['contradiction']['constraint']];cap=1 if c['target']=='<=1'else c['target'];known=sum(vals.get(v,0)for v in c['vars']);un=[v for v in c['vars']if v not in vals];assert known>cap or(c['target']!='<=1'and known+len(un)<cap)
 return vals,th

def stable(z,hist,vals,white):
 w=''.join('R'*(4*vals[i]if i in z['optional']else k)+'L'for i,k in enumerate(z['ks']));E,d,h=events(w,z['heading'],complex(*z['position']));assert xy(d)==z['drift']and h==z['heading'];hs=defaultdict(list)
 for e in E:
  v=d.real if d.real else d.imag;a=e['p'].real if d.real else e['p'].imag;k=int(a//abs(v))*(1 if v>0 else-1);hs[e['p']-k*d].append((e['t']-len(w)*k,e['c']))
 for es in hs.values():
  es.sort();assert all(a[1]!=b[1]for a,b in zip(es,es[1:]))and(not white or es[0][1]=='R')
 C,bad=constraints(hist,white);assert not bad
 for c in C:
  count=sum(vals[i]for i in c['vars']);assert count<=1 if c['target']=='<=1'else count==c['target']
 return dict(period=len(w),read_classes=len(hs),inputs=sum(v[0][1]=='L'for v in hs.values()),outputs=sum(v[-1][1]=='R'for v in hs.values()),word=w)
summary={}
for name,b in J['base_controls'].items():
 z,hs=build(base[name]['word']);assert z==b['geometry'];C,bad=constraints(hs);vals,thr=replay_proof(C,bad,b['WHITE_uniform_propagation']);yes,v,t,steps=force(C,bad);assert yes==b['WHITE_uniform_propagation']['possible'];chosen={int(i):v for i,v in z['chosen'].items()};assert stable(z,hs,chosen,False)==b['literal_supplied_assignment']
 if name=='S104':assert yes and vals==chosen and v==chosen;stable(z,hs,vals,True)
 else:assert not yes
 prep=force(*constraints(hs,False));assert prep[0]and all(chosen[i]==v for i,v in prep[1].items());summary[name]=dict(C_blocks=len(z['ks']),optional=len(chosen),constraints=len(C),WHITE_possible=yes,forced=len(vals),threshold_min=min(thr.values()),threshold_max=max(thr.values()))
for r in J['representation_controls']:
 w=base[r['name']]['word'];k=r['phase_cut'];w=(w[k:]+w[:k])*r['power'];z,hs=build(w,r['heading']);yes,v,t,steps=force(*constraints(hs));chosen={int(i):v for i,v in z['chosen'].items()};pos=stable(z,hs,chosen,False);assert yes==r['WHITE_possible']==(r['name']=='S104')and(len(z['ks']),len(chosen),len(v),pos['period'],pos['inputs'])==(r['C_transitions'],r['optional_laps'],r['forced_count'],r['positive_period'],r['positive_inputs'])
 if yes:assert v==chosen
assert len(J['representation_controls'])==100
# The supplied nonbacktracking geometric ladder has an immutable mandatoryR/R defect.
L=J['ladder_forced_RR_obstruction'];lw=''.join('R'*k+'L'for k in json.loads((D/'disconnected_C_ladder_attempt_certificate.json').read_text())['minimal_R_exponents']);z,hs=build(lw,1);assert z==L['geometry'];cc,bb=constraints(hs,False);assert bb;replay_proof(cc,bb,L['proof'])
# Entire symbolic prepared backgrounds, including never-read bulk and finite XOR caps.
full=[]
for a in J['complete_P_Q_background_replays']:
 p=R/'nonlinear_global_budget_2026-10-23'/a['normal_form'];assert sha(p)==a['normal_form_sha256'];nf=json.loads(p.read_text());name='P1564'if'five_band'in p.name else'Q4352';key='full_black_orbit_profiles'if name=='P1564'else'full_black_profiles';bulk=set(map(tuple,nf[key]));cap={complex(*v)for v in nf['finite_XOR_cap']};X=set(cap);pos=complex(*nf['pose'][0]);h=nf['pose'][1];start=pos;h0=h;w=base[name]['word'];stride=nf['drift'][0];hist=defaultdict(list)
 for t,c in enumerate(w*3):
  x,y=int(pos.real),int(pos.imag);bit=((x-y,x%2)in bulk)^(pos in X);assert bit==(c=='L')
  if t<len(w):hist[x-y,x%stride].append((t-len(w)*((x-x%stride)//stride),c))
  X.symmetric_difference_update({pos});h=(h+(1 if c=='R'else-1))%4;pos+=V[h]
 assert pos==start+3*stride*(1+1j)and h==h0
 B={(t,a)for t,b in bulk for a in range(b,stride,2)}
 for es in hist.values():es.sort();assert all(a[1]!=b[1]for a,b in zip(es,es[1:]))
 assert{r for r,es in hist.items()if es[0][1]=='L'}==B&hist.keys();O=B^{r for r,es in hist.items()if len(es)%2};U=B-hist.keys();assert(len(B),len(O),len(U),len(cap),len(X))==(a['full_bulk_black_classes'],a['full_output_black_classes'],a['untouched_black_classes'],a['retained_finite_XOR_cap_count'],a['final_full_XOR_count']);assert hashlib.sha256(json.dumps(sorted(map(xy,X)),separators=(',',':')).encode()).hexdigest()==a['final_full_XOR_sha256'];full.append(dict(name=name,bulk=len(B),outputs=len(O),untouched=len(U),cap=len(cap),final_XOR=len(X)))
# Complete blank board and exact infinite tail, independent parity checker.
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);blank=ns['sim'](set(),10392,0j,0);w,d,dead,tests=ns['future'](blank['B'],blank['p'],blank['h']);a=J['complete_finite_standard_positive'];assert sorted(map(xy,blank['B']))==a['complete_BLACK']and xy(blank['p'])==a['head']and blank['h']==a['heading']and w==a['word']==J['base_controls']['S104']['geometry']['word'];W=base['S104']['word'];assert w in{W[k:]+W[:k]for k in range(104)}
O=dict(status='PASS exact occurrence-indexed C-trace constraints and five fixed-spatial-geometry conclusions, including eventual standard104 from a finite whole entry field',proof=sha(P),certificate=sha(JF),script=sha(S),base=summary,representations=100,full_prepared_backgrounds=full,blank_cut=10392,blank_full_mass=len(blank['B']),infinite_parity_tests=tests,analytic_review=[
'An actual C crossing fixes the next block cursor; R stays on its C face and fourR returns the pose. FiveR would repeat a stillBLACK firstcell. Minimal3R beforeL returns over the previous L edge, stillWHITE, so no actual Cbacktracking. Only minimal0 admits optional4R; minimal1/2 are fixed. Initial partialblock changes only a finite prefix.',
'Candidate reads at q+kd in blocki translate to physicalq in blocki-kN, with N counting Cblocks, not antupdates. At q+ell d the variable is the independently indexedX_i(ell-k). Slots0..3optional/forcedR and4mandatoryL give true chronology for every nonperiodic assignment. All maximal candidate classes and occurrences were independently reconstructed at the FULL supplied drift, retaining repeated phase names with distinct offsets.',
'Exact zero/one/at-mostone constraints are necessary and sufficient for complete cell alternation with the stated firstcolors. Optionalreads are onlyR, so mandatoryRR cannot be repaired; mandatoryLL needs exactlyone actualowner. PreparedfirstL permitszero/one and may need infiniteBLACK input. No finite-support construction is asserted by that sufficiency direction.',
'Every recorded inference was replayed with separate occurrence multiplicity and exact translated thresholds. Uniformphase values are conclusions from the same constraint at EVERYtranslate, never assumed equalities between variables. Unknown duplicate phase copies still count separately. Forcing1 needs exactlyone remaining occurrence; forcing0 uses an already saturated bound. The minimum targetoffset is valid because the same inference translates over all sufficiently late anchors.',
'For a forward infinite tail on a FINITE WHOLE entryboard, nonzero fixedspatialdrift and finitelymany candidate templates give a commonlate anchor beyond every initialBLACK and beyond the entrytime of every candidate. Thus WHITE constraints hold eventually. Finite inference chains propagate only finite threshold changes, forcing standard laps eventually or an actual late contradiction for the four prepared traces. No temporal period was supplied for this argument.',
'Standard46Cblocks/32optionalphases/86constraints force exactlytenlaps and canonical104. Prepared10/80/1564/4352 exactgeometries are WHITE-inconsistent even with nonperiodic laps, while their genuine infinitepreparedfields satisfy their chosen assignments. All100 rotation/phase/fullpower controls checked. Full P/Q untouchedstrands and XORcaps freshly replayed; blank10392 entirefield and infinite canonicalphase103 tail independently certified.',
'The fixed17C ladder mandatoryRR obstruction is retained. None of these conclusions proves generalCtrace entry, forestunionconnectivity, a finite globalmodulealphabet, unrestrictedWHITE lifetimeS1, canonicaluniqueness or universal attraction.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(summary);print(sha(S.with_suffix('.json')))
