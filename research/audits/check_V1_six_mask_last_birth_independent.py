from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ns={'__file__':str(SELF.parent/'check_U_first_helper_ports_independent.py')};exec((SELF.parent/'check_U_first_helper_ports_independent.py').read_text().split('rows=[];gates=[];adjacent_rejects=[]')[0],ns)
globals().update({k:ns[k]for k in('ROOT','G','IDS','xy','rotation','chords','meet','pt','walk','raws','mark','K')})
D=ROOT/'core_periodicity_new';B=D/'V1_six_mask_last_birth_frozen_20261023_2044';man=json.loads((B/'manifest.json').read_text())
for x in man['files']:assert hashlib.sha256((B/x['file']).read_bytes()).hexdigest()==x['sha256']
for f,h in man['dependencies'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
M=json.loads((D/'atomic_core_record_interface_frozen_20261023_1359/04_root_out.json').read_text());p=Path(M['potential_file']);assert hashlib.sha256(p.read_bytes()).hexdigest()==M['potential_sha256'];weights=json.loads(p.read_text())['values']
HH=lambda z:int(z.real+z.imag);A=[HH(rotation(-1+1j,h))+weights[f'c{h}']for h in range(4)];assert A==[0,22,20,10];peaks={}
for a in IDS:
 for phase in range(4):
  peaks[a,phase]=max(2*HH(rotation(G[a]['end'],phase))+A[(phase+G[a]['h'])%4],*(2*HH(rotation(o,phase))+weights[f'w_{a}_{j}_{phase}']for j,o in enumerate(sorted(G[a]['O'],key=xy))))
assert peaks=={(a,h):v for a,h,v in M['created_peaks']}
F={-1+1j,-1+2j,-1+4j,2j,3j,-2+3j};creatorI=G[7]['I'];e=-2+3j;HELP=-1+5j;star={0j,1j,1,1+1j};globalH=lambda z:6-int(z.imag-z.real);mp={s:i for i,s in enumerate(IDS)};cc=lambda a,p,h:{p+rotation(q,h)for q in G[a]['ctx']};tails=lambda a:0 if a in(0,4,7)else 2 if a in(6,9)else 1
assert F==creatorI|{e}and len(F)==6 and all(28+2*globalH(z)>26 for z in F)
placements={(a,z-rotation(o,h),h)for a in IDS for h in range(4)for o in G[a]['O']for z in F};assert len(placements)==927
rows=[];needed=set();adj=[]
for helper in(4,):
 futurectx=cc(9,0j,0)|cc(helper,HELP,2)
 future=[('creator',j,ch)for j,ch in enumerate(chords(9))]+[('mandatory_helper',j,ch)for j,ch in enumerate(chords(helper,HELP,2))]
 for a,p,h in sorted(placements,key=lambda x:(x[0],*xy(x[1]),x[2])):
  outs={p+rotation(o,h):o for o in G[a]['O']};new=F&outs.keys();old=F-outs.keys();r=dict(creator=9,helper=helper,producer=a,pose=[*xy(p),h],new_final_cells=sorted(map(xy,new)),older_final_cells=sorted(map(xy,old)))
  if(sum(xy(p))+h)%2:why='wrong_sector'
  else:
   phase=(h+3)%4;en=2*globalH(p)+A[phase];cr=2*globalH(p)+peaks[a,phase];r.update(original_entry=en,original_created=cr)
   if max(en,cr)>=26:why='original_record_funding'
   elif old&cc(a,p,h):why='complete_context_hits_older_final_identity'
   elif len(new&creatorI)>=4:why='signed_max_three_same_producer_U_inputs'
   elif a>=7 and {p+rotation(q,h)for q in star}&futurectx:why='permanent_U_left_star_hits_actual_future_context'
   else:
    bad=[]
    if a>=7:
     sc=chords(a,p,h);ep=p+rotation(G[a]['end'],h);eh=(h+G[a]['h'])%4
     for j,arc in enumerate(sc):
      for name,k,farc in future:
       hit=meet(*arc,*farc)
       if not hit:continue
       if name=='creator'and k==0 and j==len(sc)-1 and(ep,eh)==(0j,0)and hit=={pt(-1-1j)}:adj.append([helper,a,*xy(p),h]);continue
       bad.append([j,name,k])
    if bad:why='U_producer_suffix_nonadjacent_center_contact';r['contact_atoms']=bad
    else:
     why='pending';r['age_cases']=[]
     ages=[k for k in range(5)if k%4==h]+[5+(h-5)%4]
     for age in ages:
      if tails(a)>age:continue
      keys=[]
      for z in sorted(new,key=xy):
       target,tp,th,ta=(helper,HELP,2,age+2)if z==e else(9,0j,0,age)
       rel=rotation(tp-p,-h);key=(mp[a],mp[target],*xy(rel),(th-h)%4,*xy(outs[z]),min(ta,5));needed.add(key);keys.append(key)
      r['age_cases'].append(dict(representative_age=age,age_class=min(age,5),queries=keys))
  r['reason']=why;rows.append(r)
found=set();cp=D/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
for line in cp.open():
 k=tuple(map(int,line.split()[:8]))
 if k in needed:found.add(k)
def zeroN(q):
 x,y=xy(q)
 return x>=0 and any(y-x-2*v>=0 and(y-x-2*v)%4==0 for v in range(x+1))
def endpoint(a,p,h,k):
 ep=p+rotation(G[a]['end'],h);eh=(h+G[a]['h'])%4;left=k-tails(a)
 if k>=5 or left not in(0,1):return True
 q=-ep
 if left==0:assert eh==0;return zeroN(q)
 assert eh==1
 for turn in(1,5,8):
  target=q-rotation(G[turn]['end'],1);X=int(target.real)
  if X<0:continue
  reachable={0j}
  for cost in range(X+1):
   for z in list(reachable):
    if z.real!=cost:continue
    for v in(1-1j,3-1j,4+0j):
     if(z+v).real<=X:reachable.add(z+v)
  if any(zeroN(target-z)for z in reachable):return True
 return False
for r in rows:
 if r['reason']!='pending':continue
 alive=[]
 for c in r['age_cases']:
  if any(k in found for k in c['queries']):c['reason']='signed_count5_query_excluded'
  elif not endpoint(r['producer'],complex(*r['pose'][:2]),r['pose'][2],c['representative_age']):c['reason']='exact_zero_or_one_C_endpoint_cone'
  else:c['reason']='necessary_last_birth_obligation_not_attainment';alive.append(c)
 r['surviving_age_cases']=alive;r['reason']='surviving_last_birth_obligation'if alive else'no_common_legal_age_and_timely_endpoint'
ref=json.loads((B/'02_V1_six_mask_last_birth.json').read_text());key=lambda r:(r['helper'],r['producer'],tuple(r['pose']));refs={key(r):r for r in ref['all_cases']}
for r in rows:
 z=refs[key(r)];assert r['reason']==z['reason'],(r,z)
 for f in('new_final_cells','older_final_cells'):assert r[f]==list(map(tuple,z[f]))
 for f in('original_entry','original_created'):
  if f in r:assert r[f]==z[f]
 if'age_cases'in r:
  assert len(r['age_cases'])==len(z['age_cases'])
  for c,d in zip(r['age_cases'],z['age_cases']):assert c['reason']==d['reason']and set(c['queries'])==set(map(tuple,d['queries']))
counts=Counter(r['reason']for r in rows);assert counts==ref['counts'];surv=[r for r in rows if r['reason']=='surviving_last_birth_obligation'];assert len(surv)==39
r=next(r for r in surv if r['producer']==5 and r['pose']==[-4,7,1]);assert r['new_final_cells']==[(-1,4)]and(r['original_entry'],r['original_created'])==(-10,10)
assert [age['representative_age']for age in r['surviving_age_cases']]==[5]
assert {28+2*globalH(-1+7j),28+2*globalH(-2+6j)}=={24}
out=dict(status='PASS original cap26 V1 fixed-six-mask necessary origins only',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),raw_placements=927,counts=dict(counts),survivors=39,common_age_classes=sum(len(r['surviving_age_cases'])for r in surv),needed_queries=len(needed),excluded_queries=len(found),all_rows=rows,scope='Specific UCC recycled-q to immediate V branch only; no outerU1 context. Necessary origins and overflow classes are not actual histories. Exact age5 VC representative separately blocked by signed4C bud guard; ages9+ not excluded here. Original funding11/13 unchanged.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)
