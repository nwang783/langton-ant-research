from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'F_same_target_C_cohort_lock_2026-10-24';p=SELF.with_name('check_returned_V_source_reduction_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('mins=')[0],ns)
W,M,walk,xy,raw,I,O,K,ctx=[ns[k]for k in('W','M','walk','xy','raw','I','outputs','K','ctx')];raw={**raw,'C':walk(W['C'])};names=['D','DC','V','VC','VCC','U','UC','UCC'];ids=[0,1,4,5,6,7,8,9];MIN=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text())['slots'];mins={}
for n,i in zip(names,ids):
 for v in I[n]:
  z=MIN[f'{i}:{xy(v)}']['certified_minimum_C_age'];assert z>=2
  if z==2:assert n in['V','VC']and v==3j
  mins[n,v]=z
assert len(mins)==23
suffixcuts=[]
for n in['DC','VC','VCC','UC','UCC']:
 tr=walk(''.join(W[c]for c in n)+W['F']+M);assert not tr['feasible'];suffixcuts.append((n,tr['i'],xy(tr['q'])))
cu=walk(W['C']+W['U']+M);assert not cu['feasible'];cf=walk(W['C']+W['F']+M);assert cf['feasible']
# Positive source-free regression: actually execute rawC+F+actualM11 on the complete minimum board.
cfseed={q for q,c in cf['req'].items()if c};B=set(cfseed);p=0j;h=0;cftrace=[]
for t,c in enumerate(W['C']+W['F']+M):
 assert('L'if p in B else'R')==c;cftrace.append((t,xy(p),h,c));B^={p};h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
births=[];earlyW=[];south=[];east=[];last=[];counts=Counter();foreign=3-4j
for k in(1,2):
 cp=-k-1-k*1j;tags={'T':-k-1-(k+2)*1j,'Q':-k-(k+2)*1j,'R':1-k-(k+1)*1j};slots={'T':2,'Q':2+1j,'R':1+2j}
 for label,q in tags.items():
  assert cp+slots[label]*(-1j)==q
  occ=[(i,c)for i,(p,h,c)in enumerate(raw['C']['reads'])if p==slots[label]];assert occ[-1]==({'T':8,'Q':7,'R':13}[label],'R')
 for n in['DC','VC']:
  src=-k-k*1j-raw[n]['p']*(-1j);assert(src+raw[n[0]]['p']*(-1j),1)==(cp,1)
  for label,q in tags.items():
   slot=(q-src)*1j;assert slot in O[n]
   actual=[(i,c)for i,(p,h,c)in enumerate(raw[n]['reads'])if p==slot];assert actual[-1]==(len(W[n[0]])+{'T':8,'Q':7,'R':13}[label],'R')
   births.append((k,n,xy(src),label,xy(slot),actual[-1],-1,-1,0))
 for n in['V','VC']:
  entry=tags['Q']-3j*1j;assert entry.imag==tags['Q'].imag<2;earlyW.append((k,n,xy(entry),2,1))
 for label in['T','Q']:
  tag=tags[label]
  for n in['D','V','U']:
   for v in I[n]:
    entry=tag+v;end=entry-raw[n]['p'];assert end.imag<=tag.imag and end.imag-2<foreign.imag
    south.append((k,label,n,xy(v),xy(entry),xy(end),int(end.imag-2)))
 held=set()
 for label in(['T','Q']if k==1 else['T','Q','R']):
  tag=tags[label]
  for n in['D','V','U']:
   for v in I[n]:
    entry=tag-v*(-1j);end=entry+raw[n]['p']*(-1j);hits=held&{entry+q*(-1j)for q in ctx[n]['req']};minimum=mins[n,v];solutions=[]
    if(int(entry.real+entry.imag)+1)%2:kind='sector'
    elif minimum>4:assert minimum==5;kind='upper_min5'
    elif hits:kind='earlier_current_tag'
    else:
     dx=int((foreign-end).real);down=int((end-foreign).imag)
     if down>=0:
      for nv in range(down+1):
       nd=down-nv;rest=dx-nd-3*nv
       if rest>=0 and rest%4==0:
        nu=rest//4;last_allowed=([n]if end==foreign and n in['V','U']else[])if nd+nv+nu==0 else(['V']if nv else[])+(['U']if nu else[])
        solutions.append((nd,nv,nu,last_allowed))
     assert all(not z[-1]for z in solutions);kind='endpoint'
    hitrows=[]
    for q in hits:
     local=(q-entry)*1j;first=next((i,c)for i,(z,h,c)in enumerate(ctx[n]['reads'])if z==local);hitrows.append((xy(q),xy(local),ctx[n]['req'][local],local in K,first))
    counts[kind]+=1;east.append((k,label,n,xy(v),minimum,xy(entry),xy(end),kind,hitrows,solutions))
  held.add(tag)
 for n,label in[('V','Q'if k==1 else'R'),('U','T'if k==1 else'Q')]:
  entry=foreign-raw[n]['p']*(-1j);tag=tags[label];local=(tag-entry)*1j;assert tag in held and local in K and ctx[n]['req'][local]
  first=next((i,c)for i,(q,h,c)in enumerate(raw[n]['reads'])if q==local);assert first[1]=='L';last.append((k,n,xy(entry),label,xy(tag),xy(local),first))
assert len(east)==40 and len(south)==32 and len(earlyW)==4 and len(last)==4
A=json.loads((D/'F_C_cohort_lock.json').read_text());mapping={'sector':'wrong_active_sector','upper_min5':'true_input_full_age4_below_minimum5','earlier_current_tag':'would_touch_or_retire_previously_proved_CURRENT_cohort_tag','endpoint':'no_exact_E_zero_run_endpoint_with_actual_last_V_U'};assert{mapping[k]:v for k,v in counts.items()}==A['E_role_counts']
mp=D/'manifest.json';mf=json.loads(mp.read_text());mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='ed14673e746c7277b18f5c9235f5f7c9b2576e01242bc77e37b3eaf163da5a7e'
for f in mf['files']:assert hashlib.sha256((D/f['file']).read_bytes()).hexdigest()==f['sha256']
for f,h in A['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS reader-independent first-C DC/VC cohort lock at F3,-4 for k1/k2','manifest_sha256':mh,'fresh_twelve_source_birth_roles':births,'fresh_all23_true_full_input_minima':[(n,xy(v),z)for(n,v),z in mins.items()],'fresh_five_real_full_Ctail_F_conflicts':suffixcuts,'C_U_conflict':[cu['i'],xy(cu['q'])],'genuine_raw_C_F_positive_scope_control':{'seed':sorted(map(xy,cfseed)),'trace':cftrace},'fresh_four_Q_W_cones':earlyW,'fresh32_S_endpoint_budgets':south,'fresh40_E_hierarchical_roles':east,'E_counts':dict(counts),'four_actual_last_core_clashes':last,'analytic_review':[
'The actual last positive-C parent is FIRST-tail DC or VC, at selectedDclock-1; its C entry is also-1 and exit0. Fresh literal reconstruction givesT C8R,Q C7R,Rexit C13R in each true FULL output. k1/k2 interveningN D steps preserve the packet ordering. This is not a C2 source: its full age at foreign would differ and the Uupper5 comparison would fail.',
'T common first consumer is no earlier than selectedclock2 by signed atomic ENTRY minimum3. Q has trueFULL produced-input minimum2 and its sole age2 possibilities are V/VC UPPER0,3, not selected1,2. Their W1 heads have negative y below every actual postselectedD W-head y>=2. Rexit uses signed atomic EXIT minimum3, hence no consumer before selectedclock3. These distinct clocks are not interchanged.',
'Any firstT/Q S2 consumer base exits no higher than the tag. One remainingS-to-E C lowersy1. Its actual containing completed old packet cannot directly precedeF, by five genuine fullpacket literal conflicts; rawC-to-U also conflicts, so a mandatory subsequent plainE D/V lowersy another1. Thus F_y<=tag_y-2<-4. This includes a retiring consumer whose ownC is that last turn; two-tail consumers cannot complete. Standalone rawC+F is physically feasible and independently replayed, so a source-free atomic C/F ban is expressly NOT used.',
'At E3 all originals have true FULL sourceage4. Fresh40 real plainD/V/U input roles include marker-only inputs. T is first locked by sector, Uupper5, or exact zero-C endpoint equations. Then every permittedQ role either needs upper5 or meets already-currentT in its complete context; nextk2R similarly meetsT/Q. This is sequential proof, not simultaneous assumed permanence. All leftover endpoint cases fail, including a possible immediate last consumer.',
'A same original residual cannot first become entryCORE without having been a true full-context input of the preceding old packet: choose its first such cut, where it was outside priorK and BLACK. RAW plus actual right marker must require it BLACK at first L; that is exactly I=beforeBLACK-minus-priorK. If it had been in priorK, first cut was earlier. This covers deferred physical reads/core absorption and prevents a hidden core-only escape; C itself has no residualI.',
'The required last plainV/U beforeF has one of these SAME originals in its genuine entryK, which contradicts the proved absence of first retirement/core capture. No foreign toggle or returned reader is invoked. Therefore bothD30 andC75 k1/k2 DC/VC parent interfaces are excluded, butF2,-5 D15 and other hypothetical source histories are not addressed.'
],'dependencies':A['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(dict(counts))
