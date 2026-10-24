from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'MIRROR_WINDING_RENEWAL_MANIFEST.json';assert sha(MF)=='266ea46614a7c088065ea82276f82991958175d64fc95e1274bd1808ab120dde';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
ref=json.loads((D/'MIRROR_WINDING_RENEWAL_CHECKED.json').read_text())
for f,h in ref['dependencies'].items():assert sha(D/f)==h
lib=S.with_name('check_phase13_double_scatter_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('# Canonical source')[0],ns);future,phases=ns['future'],ns['phases'];V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];key=lambda z:(int(z[0].real),int(z[0].imag),z[1]);norm=lambda z:json.loads(json.dumps(z))
def step(z,B):
 p,h=z;hh=(h+(-1 if p in B else 1))%4;return(p+V[hh],hh)
def cycle(z,B):
 ans=[];seen=set();q=z
 while q not in seen:
  seen.add(q);ans.append(q);q=step(q,B);assert len(ans)<=8*len(B)+4
 assert q==z;return ans
def wind(c):
 # Independently sum crossings of the ray from each face center to +infinity.
 byrow=defaultdict(list);area2=0
 for a,b in zip(c,c[1:]+c[:1]):
  p,q=a[0],b[0];assert abs(p-q)==1;area2+=int(p.real*q.imag-q.real*p.imag)
  if q.imag!=p.imag:byrow[int(min(p.imag,q.imag))].append((int(p.real),1 if q.imag>p.imag else-1))
 ans={}
 for y,edges in byrow.items():
  left=min(x for x,s in edges);right=max(x for x,s in edges)
  for x in range(left,right):
   z=sum(s for xx,s in edges if xx>x)
   if z:ans[(x,y)]=z
 assert area2%2==0 and area2 and sum(ans.values())==area2//2
 assert set(ans.values())==({1}if area2>0 else{-1});return ans,area2//2
def whole(B,pose):
 U=set()
 for p in B:
  for h in([1,3]if int(p.real+p.imag)%2==0 else[0,2]):U.update(cycle((p,h),set()))
 if pose not in U:U.update(cycle(pose,set()))
 # Every changed map is closed on this explicitly finite baseline universe.
 assert {step(z,B)for z in U}==U
 def partition(board):
  unseen=set(U);ans=[]
  while unseen:
   c=cycle(min(unseen,key=key),board);assert set(c)<=unseen;unseen.difference_update(c);ans.append(c)
  return ans
 baseline=Counter()
 for c in partition(set()):
  w,a=wind(c);assert len(c)==4 and a==-1;baseline.update(w)
 assert all((x+y)%2==0 and v==-1 for(x,y),v in baseline.items())
 total=Counter();positive=Counter();rows=[];active=None
 for c in partition(B):
  w,a=wind(c);total.update(w)
  if a>0:positive.update(w)
  row=dict(representative=[xy(c[0][0]),c[0][1]],length=len(c),area=a);rows.append(row)
  if pose in c:active=row
 assert total==baseline;P=sum(max(r['area'],0)for r in rows);assert P==sum(positive.values())and sum(abs(r['area'])for r in rows)-len(U)//4==2*P
 return dict(black_mass=len(B),baseline_loops=len(U)//4,affected_states=len(U),circuits=rows,active=active,positive_winding_area=P,positive_winding=[[list(q),n]for q,n in sorted(positive.items())],positive_loop_count=sum(r['area']>0 for r in rows),max_loop_length=max(r['length']for r in rows),max_absolute_area=max(abs(r['area'])for r in rows))
def surgery(B,pose):
 other=(pose[0],(pose[1]+2)%4);old=[cycle(pose,B)]
 if other not in old[0]:old.append(cycle(other,B))
 bb=set(B);bb.symmetric_difference_update({pose[0]});new=[cycle(pose,bb)]
 if other not in new[0]:new.append(cycle(other,bb))
 assert set(sum(old,[]))==set(sum(new,[]))and sorted([len(old),len(new)])==[1,2]
 def data(cc):
  ww=Counter();aa=[];dd=[]
  for c in cc:w,a=wind(c);ww.update(w);aa.append(a);dd.append(set(w))
  return ww,aa,dd
 ow,oa,od=data(old);nw,na,nd=data(new);assert ow==nw;pair=oa if len(old)==2 else na;dom=od if len(old)==2 else nd;same=pair[0]*pair[1]>0
 if same:assert dom[0].isdisjoint(dom[1])
 else:assert dom[0]<dom[1]or dom[1]<dom[0]
 delta=sum(max(a,0)for a in na)-sum(max(a,0)for a in oa);assert delta==(0 if same else min(map(abs,pair))*(1 if len(new)==2 else-1))
 return dict(kind='split'if len(new)==2 else'merge',old_areas=oa,new_areas=na,same_orientation=same,positive_area_change=delta,pair_domain_sizes=list(map(len,dom)),old_lengths=list(map(len,old)),new_lengths=list(map(len,new)))
small=Counter();cells=[complex(x,y)for x in range(3)for y in range(3)]
for mask in range(512):
 B={q for i,q in enumerate(cells)if mask>>i&1};whole(B,(0j,1))
 for q in cells:
  z=surgery(B,(q,1 if int(q.real+q.imag)%2==0 else 0));small[z['kind'],z['same_orientation']]+=1
assert [dict(kind=k[0],same_orientation=k[1],count=v)for k,v in sorted(small.items())]==ref['small_surgery_class_counts']
print('Independent512 boards/4608 surgeries passed.',flush=True)
controls=[]
for z in ref['controls']:
 seed={complex(*q)for q in z['initial_black']};B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda p:(p.real,p.imag)))};p=0j;h=1;N=z['fine_reads'];events=[];word=[];hull=[max([0]+[int(q.imag)for q in seed]),max([0]+[int(q.real)for q in seed]),max([0]+[-int(q.imag)for q in seed]),max([0]+[-int(q.real)for q in seed])];cuts={r['cut']:r for r in z['complete_cuts']};geoms={};ledger=[]
 for t in range(N+1):
  vv=[int(p.imag),int(p.real),-int(p.imag),-int(p.real)]
  for k in range(4):
   if vv[k]>hull[k]:assert p not in B;events.append([t,k]);hull[k]=vv[k]
  if t in cuts:
   rr=cuts[t];assert [xy(p),h]==rr['pose'];assert [dict(cell=xy(q),lifetime=B[q])for q in sorted(B,key=lambda p:(p.real,p.imag))]==rr['complete_black'];gg=whole(set(B),(p,h));assert gg==rr['geometry'];geoms[t]=gg
  if t==N:break
  c='L'if p in B else'R'
  if z['local_packet']and z['local_packet'][0]<=t<z['local_packet'][1]:
   ll=surgery(set(B),(p,h));ll.update(tick=t,cell=xy(p),turn=c);assert ll==z['local_surgery_ledger'][len(ledger)];ledger.append(ll)
  word.append(c)
  if c=='L':del B[p]
  else:B[p]=t
  h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 word=''.join(word);assert word==z['whole_word']and events==z['union_records'];tw,dr,deaths,tests=future(B,p,h);assert tw in phases and tw==z['infinite_tail_word']and xy(dr)==z['tail_drift']and tests==z['tail_parity_tests']
 positive=sum(max(r['positive_area_change'],0)for r in ledger);negative=sum(max(-r['positive_area_change'],0)for r in ledger);assert positive==z['gross_positive_area_created']and negative==z['gross_positive_area_cancelled']
 if ledger:
  s,t=z['local_packet'];assert next((a[0],b[0])for a,b in zip(events,events[1:])if b[0]-a[0]>104)==(33345,33639);assert t-s==294 and len(ledger)==294
  delta=Counter({tuple(q):n for q,n in geoms[t]['positive_winding']});delta.subtract({tuple(q):n for q,n in geoms[s]['positive_winding']});changes=[dict(plaquette=list(q),change=n)for q,n in sorted(delta.items())if n];assert changes==z['packet_positive_winding_change'];assert Counter(v['change']for v in changes)=={1:8,-1:6}
  phasebad=[]
  for k in range(104):
   expected=(tw[k:]+tw[:k])*2;phasebad.append(next(j for j in range(208)if word[t+j]!=expected[j]))
  assert phasebad==z['canonical_phase_rejection']and max(phasebad)==21
  assert(positive,negative)==(99,97);types=Counter((r['kind'],r['same_orientation'])for r in ledger);assert types=={('merge',True):117,('split',True):92,('split',False):45,('merge',False):40}
 else:
  assert next((a[0],b[0])for a,b in zip(events,events[1:])if b[0]-a[0]>104)==(355,509)
 controls.append(dict(name=z['name'],whole_reads=N,cut_mass_area=[(t,len(cuts[t]['complete_black']),g['positive_winding_area'])for t,g in sorted(geoms.items())],tail_drift=xy(dr),tail_tests=tests,created=positive,cancelled=negative))
 print(z['name'],'whole field and geometry passed',flush=True)
review=[
'For a finite BLACK set, the union of empty-board four-cycles through both admissible states at each changed cell is closed under every changed pairing; all other baseline cycles remain unchanged. Thus the affected oriented circuit family is finite without cropping the plane or assuming the cursor component contains all relevant cells.',
'The checkerboard sector has exactly one allowed direction on each physical unit edge. Both mirror pairings are noncrossing and preserve the complete oriented edge1-chain. Rounding in disjoint small vertex disks gives embedded Jordan circles and changes no plaquette-center index. Additivity gives pointwise total winding equal to the empty baseline, minus1 on even plaquettes and0 on odd.',
'A nonempty oriented circuit cannot have zero index on every unit face: the difference of neighboring face winding coefficients is its directed edge-chain coefficient, so all-zero faces would imply zero chain. Every physical edge has one allowed orientation, hence no reverse cancellation can annihilate a nonempty circuit. Its Jordan winding therefore has one nonzero sign and nonempty discrete domain.',
'On the two-circuit side of a transposition, equal signs must have disjoint plaquette domains to avoid index2. Opposite signs must be strictly nested, since nonnested domains would yield both signs and equal domains would yield the excluded zero chain. These are discrete plaquette sets, not claims of unchanged microscopic rounded interiors or chronological LIFO.',
'P is finite total positive signed grid area, counting multiplicity, and the exact area identities follow from the same pointwise chain invariant. Equal-sign surgery is neutral; opposite merge/split loses/gains the smaller absolute domain. This is compensated winding bookkeeping, not a monotone fuel or an injective stock charge.',
'Independent geometry implementation checks512 whole finite boards and4608 surgeries, then every complete selected field and all294 actual MT surgeries. Full119249 physical updates begin at the genuine empty or22-cell seeds. Hull records include the entire original seed and all past head positions. The first MT>104 completed pristine gap33345..33639 has masses3101/3125 and P137/139, with99 created and97 cancelled.',
'At cut33639 every canonical cyclic104 turn phase disagrees within22 actual reads; if canonical all-future motion had begun earlier in the gap, that later cut would retain a canonical phase, contradiction. Thus the294-gap increase is genuinely pre-capture. The longer40071..109168 gap and blank9977..10081 area increment are only named finite comparisons, never extrapolated to all parameters or all future periods.',
'Complete terminal BLACK fields independently pass all-ray parity and explicit canonical membership. No unread archive is removed for the geometry. Arbitrary infinite backgrounds, all-n area laws, completed-drought count bounds, renewal control and global attraction remain outside the theorem.'
]
out=dict(status='PASS finite-board pointwise mirror winding/surgery identities and named pre-capture drought-monotonicity falsifier',manifest=sha(MF),script=sha(S),small_boards=512,small_surgeries=4608,small_types=[(k,v)for k,v in sorted(small.items())],complete_controls=controls,analytic_review=review,dependencies=ref['dependencies'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
