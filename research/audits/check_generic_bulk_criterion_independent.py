"""Independent joint-period literal profiles and complete finite selector oracle."""
from pathlib import Path
from collections import defaultdict,Counter
from itertools import combinations,product
import sys,json,hashlib,math,random,subprocess
ROOT=Path(__file__).resolve().parents[1];G=ROOT/'global_architecture_2026-10-23';sys.path.insert(0,str(G));import bulk_standard_compatibility as candidate
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];V=''.join('L'if c=='R'else'R'for c in H[::-1]);P108=V[:31]+'LRRRR'+V[32:]
def trace(word,h):
 x=y=0;rows=[];D=((0,1),(1,0),(0,-1),(-1,0))
 for c in word:
  rows.append((x,y,c));h=(h+(1 if c=='R'else-1))%4;u,v=D[h];x+=u;y+=v
 return rows,(x,y),h
def profile(word,h,l):
 rows,d,hh=trace(word,h);assert d[0]==d[1]and abs(d[0])==l and hh==h
 # Translate actual complete copies on BOTH sides and collect the literal x-strip.
 radius=2+max(abs(x)//l for x,y,c in rows);out=defaultdict(list)
 for j in range(-radius,radius+1):
  for i,(x,y,c)in enumerate(rows):
   u,v=x+j*d[0],y+j*d[1]
   if 0<=u<l:out[u-v,u].append((j*len(word)+i,c))
 assert sum(map(len,out.values()))==len(word)
 return {s:sorted(v)for s,v in out.items()}
# Literal standard complete profiles, not candidate orbit tables.
writer={}
for orient,h in [('NE',1),('SW',3)]:
 p=profile(H,h,2);assert all(v[0][1]=='R'for v in p.values());writer[orient]=(set(p),{s for s,v in p.items()if v[-1][1]=='R'})

def bundle_oracle(rows,need):
 # Enumerate ALL geometrically disjoint nonpolluting bundles by increasing band.
 available=sorted([c for c in rows if not c['polluted_white']],key=lambda c:(c['band'],c['orientation'],c['normal'],c['x_parity']))
 states=0
 def rec(j,right,covered):
  nonlocal states;states+=1
  if covered>=need:return True
  for k in range(j,len(available)):
   c=available[k]
   if c['band'][0]>right and rec(k+1,c['band'][1],covered|set(map(tuple,c['covered_black']))):return True
  return False
 return rec(0,-10**9,set()),states
records=[];profile_classes=0
cases=[('H',H),('H3',H*3),('reverse',V),('P108',P108),('P108x3',P108*3),('LR','LR'),('LR3','LR'*3),('LR5','LR'*5),('axis','RLLR'),('singleR','R'),('zero','RRRR'),('refinedH',H.replace('R','RLLLL',1))]
for name,P in cases:
 for h in range(4):
  got=json.loads(json.dumps(candidate.criterion(P,h)));rr,d,dh=trace(P,h)
  if got['status']=='FINITE_POWER_CONFLICT':
   copies=got['copies_tested'];seen={};bad=False
   for i,(x,y,c)in enumerate(trace(P*copies,h)[0]):
    if (x,y)in seen and seen[x,y][1]==c:bad=True;break
    seen[x,y]=(i,c)
   assert bad
  elif abs(d[0])==abs(d[1])and d[0]!=0:
   hn=next(k for k in range(4)if trace(P,k)[1][0]==trace(P,k)[1][1]<0)
   a=-trace(P,hn)[1][0];l=math.lcm(a,2);q=l//a;r=l//2;qp=profile(P*q,hn,l);profile_classes+=len(qp)
   alternating=all(all(x[1]!=y[1]for x,y in zip(v,v[1:]))for v in qp.values())
   if not alternating:assert got['status']=='INTERNAL_BULK_CONFLICT';records.append({'name':name,'heading':h,'status':got['status']});continue
   reads=set(qp);black={s for s,v in qp.items()if v[0][1]=='L'};white=reads-black
   assert sorted(map(list,reads))==got['read_classes']and sorted(map(list,black))==got['required_black_classes']
   kw=[x//l for x,y,c in trace(P*q,hn)[0]];wq=max(kw)-min(kw)
   wh=max(max((x+off)//l for x,y,c in trace(H*r,hh)[0])-min((x+off)//l for x,y,c in trace(H*r,hh)[0])for hh in(1,3)for off in range(l))
   constants=got['constants'];assert constants['superperiod_copies']==q and constants['standard_superperiods']==r and constants['consumer_endpoint_loss']==wq and constants['parallel_flight_loss']==2*wh+104*(r-1)
   assert constants['nonparallel_flight_loss']==22*l*(max(t for t,e in reads)-min(t for t,e in reads)+21)
   if not black:assert got['status']=='MATCH_EMPTY_WHITE_PROFILE';records.append({'name':name,'heading':h,'status':got['status']});continue
   own=[];bindex={s:i for i,s in enumerate(sorted(black))}
   for orient in('NE','SW'):
    R,B=writer[orient];tlo=min(t for t,e in R);thi=max(t for t,e in R)
    shifts={(tb-tw,(eb-ew)%2)for tb,eb in black for tw,ew in B if(tb-tw)%2==(hn-1)%2}
    for t,e in sorted(shifts):
     painted={s for s in reads if(s[0]-t,(s[1]-e)%2)in B};cover=painted&black
     own.append(dict(orientation=orient,normal=t,x_parity=e,band=[tlo+t,thi+t],covered_black=sorted(map(list,cover)),polluted_white=sorted(map(list,painted&white)),cover_mask=sum(1<<bindex[s]for s in cover)))
   assert own==got['candidates']
   clauses=[[-i-1]for i,c in enumerate(own)if c['polluted_white']]
   clauses += [[i+1 for i,c in enumerate(own)if s in set(map(tuple,c['covered_black']))]for s in sorted(black)]
   for i,j in combinations(range(len(own)),2):
    if max(own[i]['band'][0],own[j]['band'][0])<=min(own[i]['band'][1],own[j]['band'][1]):clauses.append([-i-1,-j-1])
   canon=lambda cs:Counter(tuple(sorted(c))for c in cs)
   assert canon(clauses)==canon(got['_clauses'])
   match,states=bundle_oracle(own,black);assert match==(got['status']=='MATCH_STANDARD_RAIL_BUNDLE')
  else:
   assert dh==h and d!=(0,0)
   if got['status']=='INCOMPATIBLE':
    p=tuple(got['required_black_representative']);width=got['complete_history_loss'];w=P*(width+3);seen={}
    for x,y,c in trace(w,h)[0]:seen.setdefault((x,y),c)
    # Every complete cell on the designated orbit must first require black.
    on=[c for (x,y),c in seen.items()if (x-p[0])*d[1]==(y-p[1])*d[0]];assert 'L'in on
   else:assert got['status']in('MATCH_EMPTY_WHITE_PROFILE','INTERNAL_BULK_CONFLICT')
  records.append({'name':name,'heading':h,'status':got['status']})
# Exhaustive subset oracle versus recursive search on independent synthetic instances.
rng=random.Random(232612);synthetic=0
for z in range(160):
 b=1+rng.randrange(4);n=rng.randrange(10);cs=[]
 for i in range(n):
  lo=rng.randrange(16);hi=lo+rng.randrange(1,6);cs.append(dict(band=[lo,hi],cover_mask=rng.randrange(1,1<<b),polluted_white=[]if rng.randrange(4)else[0]))
 target=(1<<b)-1;possible=False
 for bits in range(1<<n):
  chosen=[i for i in range(n)if bits>>i&1]
  if any(cs[i]['polluted_white']for i in chosen):continue
  if any(max(cs[i]['band'][0],cs[j]['band'][0])<=min(cs[i]['band'][1],cs[j]['band'][1])for i,j in combinations(chosen,2)):continue
  cover=0
  for i in chosen:cover|=cs[i]['cover_mask']
  if cover==target:possible=True;break
 model,_=candidate.solve_cover(cs,b);assert(model is not None)==possible;synthetic+=1
proofs=[]
for path in sorted(G.glob('generic_bulk_*.rup')):
 cnf=path.with_suffix('.cnf');r=subprocess.run([str(ROOT/'causal_reduction/morphic_candidates/check_drat'),str(cnf),str(path)],capture_output=True,text=True,check=True);j=json.loads(r.stdout);assert j['valid']and j['RAT']==0 and j['deletions']==0;proofs.append({'case':path.stem,'RUP':j['RUP']})
out={'status':'PASS independent literal joint profiles, anchor selectors/CNF, exhaustive cover oracle and retained RUP proofs','source_sha256':hashlib.sha256((G/'bulk_standard_compatibility.py').read_bytes()).hexdigest(),'note_sha256':hashlib.sha256((G/'generic_bulk_preparation_criterion.md').read_bytes()).hexdigest(),'cases':records,'joint_profile_classes':profile_classes,'synthetic_exhaustive_selector_controls':synthetic,'proofs':proofs,'scope':'Decision for one supplied periodic consumer bulk interface and its stated finite-preparation necessity. No arbitrary consumer search, launch realization, common finite-seed construction or capture theorem.'}
(ROOT/'audits/check_generic_bulk_criterion_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
