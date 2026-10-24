from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'PRUNE_TWO_ORIGINAL_INPUTS_V2_MANIFEST.json';assert sha(MF)=='5908e37dde521eb5b10ccf942196ae837e2db4b51c364aaeaa5e8183ddc98f93';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
J=json.loads((D/'PRUNE_TWO_ORIGINAL_INPUTS_V2_CHECKED.json').read_text())
for f,h in J['source_hashes'].items():assert sha(D/f)==h
ns={};exec(S.with_name('check_return_permanent_debt_independent.py').read_text().split('def check_case')[0],ns);verify,vec,xy,ray=[ns[k]for k in('verify_future','vec','pair','ray_k')];cache={}
def comp(seed,N):
 key=(tuple(sorted(seed,key=lambda q:(q.real,q.imag))),N)
 if key in cache:return cache[key]
 assert len(seed)<=2 and 0<N<=200000;B={q:-i-1 for i,q in enumerate(key[0])};p=0j;h=0;first={};turns='';deaths={}
 for t in range(N):
  first.setdefault(p,t);old=B.pop(p,None)
  if old is None:B[p]=t;turns+='R';h=(h+1)%4
  else:deaths[old]=t;turns+='L';h=(h-1)%4
  p+=vec[h]
 w,dr,ff,tests=verify(B,p,h);assert len(w)==104 and dr.real in(-2,2)and dr.imag in(-2,2);rr=[];q=p;hh=h
 for c in w:rr.append(q);hh=(hh+(1 if c=='R'else-1))%4;q+=vec[hh]
 assert q-p==dr and hh==h;deaths.update({tag:N+t for tag,t in ff.items()});ans=dict(seed=set(seed),N=N,B=B,p=p,h=h,first=first,word=w,dr=dr,reads=rr,tests=tests,prefix=turns,deaths=deaths);cache[key]=ans;return ans

def omitted(c,points):
 hits=[]
 for q in points:
  times=[]
  if q in c['first']:times.append(c['first'][q])
  for i,p in enumerate(c['reads']):
   k=ray(q-p,c['dr'])
   if k is not None and k>=0:times.append(c['N']+104*k+i)
  if times:hits.append((min(times),q))
 return min(hits,key=lambda z:z[0])if hits else None

def serial(hit):return None if hit is None else[hit[0],xy(hit[1])]
controls=[]
for r in J['controls']:
 original=set(map(lambda p:complex(*p),r['initial_black']));selected=set();hits=[];assert r['initial_pose']==[[0,0],0]
 for i,a in enumerate(r['comparisons']):
  assert selected==set(complex(*q)for q in a['selected'])and len(selected)<=2;c=comp(selected,a['certified_prefix']);assert c['word']==a['tail_word']and[xy(c['p']),c['h']]==a['tail_pose']and xy(c['dr'])==a['tail_drift']and c['tests']==a['ray_tests'];hit=omitted(c,original-selected);assert serial(hit)==a['first_omitted_hit']
  if hit is None:
   assert i==len(r['comparisons'])-1 and r['kind']=='EXACT whole original pruning <=2'and selected==set(complex(*q)for q in r['relevant'])
   # Replay the ORIGINAL full board and certify its whole archive, without deleting unread extras.
   B={q:-i-1 for i,q in enumerate(sorted(original,key=lambda z:(z.real,z.imag)))};p=0j;h=0
   for t,ch in enumerate(c['prefix']):
    old=B.pop(p,None);assert(ch=='R')==(old is None)
    if old is None:B[p]=t;h=(h+1)%4
    else:h=(h-1)%4
    p+=vec[h]
   w,dr,ff,tests=verify(B,p,h);b=r['full_board_tail'];assert w==b['word']==c['word']and dr==c['dr']and sorted(map(xy,B))==b['black']and[xy(p),h]==b['pose']and tests==b['ray_tests']
   assert all(omitted(c,{q})is not None for q in selected)
  else:
   t,q=hit;assert not hits or t>hits[-1]['time'];hits.append(dict(time=t,cell=xy(q)));selected.add(q)
 assert hits==r['contacts']
 if len(selected)==3:assert r['kind']=='AT LEAST THREE original inputs'and len(r['comparisons'])==3
 # Independently read full input through its claimed third or last original contact.
 B=set(original);p=0j;h=0;seen=set();actual=[];end=hits[-1]['time']+1 if hits else 0
 for t in range(end):
  if p in original and p not in seen:assert p in B;seen.add(p);actual.append(dict(time=t,cell=xy(p)))
  black=p in B;B.symmetric_difference_update({p});h=(h+(-1 if black else 1))%4;p+=vec[h]
 assert actual==hits;controls.append(dict(name=r['name'],kind=r['kind'],contacts=hits,comparisons=len(r['comparisons'])))
for r in J['sparse_interior_radius_controls']:
 B={complex(*q)for q in r['board']};radius=r['radius'];inside={q for q in B if max(abs(q.real),abs(q.imag))<=radius};a=r['result'];assert len(inside)<=2 and inside==set(complex(*q)for q in a['inside_black']);c=comp(inside,a['comparison_tail_cut']);hit=omitted(c,B-inside);assert serial(hit)==a['first_outside_original_contact']and(hit is None)==a['rho_at_input_le_R']
for r in J['force_black_regressions']:
 B={complex(*q)for q in r['board']};q=complex(*r['target']);c=comp(B,r['comparison_tail_cut']);hit=omitted(c,{q});assert serial(hit)==r['certified_first_hit'];X=set(B);Y=X|{q};px=py=0j;hx=hy=0
 for t in range(r['checked_prefix']):
  assert(px,hx)==(py,hy)and px!=q
  bx=px in X;by=py in Y;assert bx==by;X.symmetric_difference_update({px});Y.symmetric_difference_update({py});hx=(hx+(-1 if bx else 1))%4;hy=(hy+(-1 if by else 1))%4;px+=vec[hx];py+=vec[hy]
 if hit is not None:assert px==py==q
source=R/'audits/two_black_canonical_completion_independent.json';assert sha(source).startswith('892862')
out=dict(status='PASS pruning/reachability oracle equivalence and corrected v2 total Prune2 interface; named budgeted controls checked',manifest=sha(MF),script=sha(S),signed_at_most_two_black_completion=sha(source),comparisons_replayed=len(cache),physical_comparison_reads=sum(v['N']for v in cache.values()),controls=controls,analytic_review=['Only corrected v2 executable867e61d7 is signed. Frozen v1 was never signed: its unjustified assertion equating a past repeated phase with the freshly certified future phase could abort generic search. v2 validates the freshly certified word is canonical, uses it to construct every future read ray, and leaves the past repetition as a filter only. Supplied controls are unchanged; no actual interruption-boundary witness is asserted.','Prune(X) follows from finitely many reachability queries on original BLACK cells. Conversely forcing a target q BLACK changes no read before first q, so Hit(X,q) iff q belongs to Prune(B union{q},pose). This is a uniform oracle reduction, not an undecidability or computability claim.','rho>R is c.e. by first reading any ORIGINAL outside-box black cell; rho<=R is co-c.e. No equivalence between scalar rho and full pruning is asserted. Compact recurrence is c.e. only as a whole-input property equivalent to finite-certificate eventual translation; this does not decide individual-cut pruning.','Prune2 always compares from the ORIGINAL cut. S consists of the first k<=2 distinct actual original consumptions. First omitted-original hit in the certified comparison future is also the next actual one, by first-difference coupling. Repeated visits and R-born replacements never count as additional original inputs.','All three comparison boards have mass<=2, so signed all-position canonical capture gives mathematical termination of simulate-plus-exact-ray-certificate search. Fixed checking times104 do not miss an eventual104 tail. The implementation budget200000 is only an execution limit returning UNKNOWN on exhaustion, not the totality premise. Canonical drifts have nonzero x coordinate, so its integer first-hit division is valid.','On no-hit branch all omitted BLACK cells remain physically present and unread; replay/full-board parity certifies the unchanged complete future. Every selected cell is actually consumed, so S is exact C*. Third-hit branch supplies only three actual inputs, not capture/noncapture or a global renewal budget.','For sparse-radius testing the premise is CURRENT BLACK interior size<=2, not presumed relevant interior size. Certified comparison either never reads any omitted outside bit, proving rho<=R, or its first outside hit is an actual original BLACK consumption, provingrho>R. Six full named controls, three radius tests and force-BLACK/no-hit controls independently checked.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
