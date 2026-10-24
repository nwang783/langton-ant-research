"""Independent full-phase reverse-wake and finite-rail constants audit."""
import json
from pathlib import Path
from collections import Counter,defaultdict
R=Path(__file__).resolve().parents[1];P=R/'core_periodicity_new';D=((0,1),(1,0),(0,-1),(-1,0))
src=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());W=src['word'];h0=src['heading']
Wbound=json.loads((R/'computability/singleton_first_block_input.json').read_text())['word'];assert W in Wbound*2

def tr(w,h):
 p=(0,0);out=[];heads=[]
 for c in w:
  out.append(p);heads.append(h);h=(h+(1 if c=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return out,heads,p,h

def key(p):return p[0]-p[1],p[0]%2
ps,hs,d,hh=tr(W,h0);assert d==(-2,-2) and hh==h0
wake={k for k,n in Counter(map(key,ps)).items() if n%2}
V=''.join('L' if c=='R' else 'R' for c in reversed(W));rv,rh,rd,eh=tr(V,(h0+2)%4)
assert rd==(2,2);q0=(d[0]-D[h0][0],d[1]-D[h0][1]);assert q0==ps[-1]
black0=white0=None;maxreadwidth=0
for j in range(104):
 w=V[j:]+V[:j];qs,heads,dd,hend=tr(w,rh[j]);assert dd==(2,2) and hend==rh[j]
 qj=(q0[0]+rv[j][0],q0[1]+rv[j][1]);groups=defaultdict(list)
 for i,q in enumerate(qs):groups[key(q)].append((i,q))
 B=set();F=set()
 for seq in groups.values():
  # Larger x wins by a whole period; ties are decided by earlier phase.
  order=sorted(seq,key=lambda v:(-v[1][0],v[0]))
  assert all(w[a[0]]!=w[b[0]] for a,b in zip(order,order[1:]))
  i,q=order[0];kk=key((qj[0]+q[0],qj[1]+q[1]))
  (B if w[i]=='L' else F).add(kk)
 assert B==wake and len(F)==10 and not(B&F)
 if white0 is None:black0=B;white0=F
 assert F==white0
 assert (sum(qj)+rh[j]-h0)%2==1
 maxreadwidth=max(maxreadwidth,max(x for x,y in qs)-min(x for x,y in qs),max(y for x,y in qs)-min(y for x,y in qs))
assert len(wake)==12 and maxreadwidth<=9
width=max(t for t,a in wake)-min(t for t,a in wake)
single=[]
for delta in range(-width-1,width+2):
 if delta%2==0:continue
 for parity in (0,1):single.append(len({(t+delta,(a+parity)%2) for t,a in wake}-wake))
assert min(single)==7
# Normalize reverse start by s=(0,-1), which changes transverse class by+1.
L=sorted((t+1,a) for t,a in black0);F=sorted((t+1,a) for t,a in white0)
profiles=[]
for sign in (1,-1):
 base={(sign*t,a) for t,a in wake}
 for delta in range(min(t for t,a in L)-max(t for t,a in base),max(t for t,a in L)-min(t for t,a in base)+1):
  if delta%2:continue
  for parity in (0,1):
   rail={(t+delta,(a+parity)%2) for t,a in base}
   b=frozenset(i for i,q in enumerate(L) if q in rail);f=frozenset(i for i,q in enumerate(F) if q in rail)
   if b:assert f;profiles.append((b,f))
best=22
for bits in range(1<<len(F)):
 allowed={i for i in range(len(F)) if bits>>i&1};b=set();f=set()
 for bb,ff in profiles:
  if ff<=allowed:b.update(bb);f.update(ff)
 best=min(best,len(L)-len(b)+len(f))
assert best==4
# Verify, rather than trust, the supplied odd-mask coboundary identities.
phase_data=json.loads((P/'standard_block_union_data.json').read_text())['rows'];maxP=maxL=maxQwidth=0
assert len(phase_data)==104
for j,row in enumerate(phase_data):
 w=W[j:]+W[:j];qs,heads,dd,hh=tr(w,hs[j]);assert dd==(-2,-2) and hh==hs[j]
 assert row['phase']==j and row['heading']==hs[j]
 odd={q for q,n in Counter(qs).items() if n%2};Q=set(map(tuple,row['tile']));C=set(map(tuple,row['coboundary']))
 assert odd==Q^C^{(x-2,y-2) for x,y in C}
 assert len(Q)==len(set(map(key,Q)))==12
 groups=defaultdict(list)
 for i,(x,y) in enumerate(qs):groups[key((x,y))].append((i,-x))
 span=max((max(v for i,v in g)-min(v for i,v in g))//2 for g in groups.values());assert span<=3
 for g in groups.values():assert w[min(g,key=lambda v:(-v[1],v[0]))[0]]=='R'
 first={}
 for k in range(4):
  for i,(x,y) in enumerate(qs):first.setdefault((x-2*k,y-2*k),w[i])
 firstL=sum(c=='L' for c in first.values());assert firstL==row['first_L_count']
 maxP=max(maxP,len(C));maxL=max(maxL,firstL)
 maxQwidth=max(maxQwidth,max(x for x,y in Q)-min(x for x,y in Q),max(y for x,y in Q)-min(y for x,y in Q))
 maxreadwidth=max(maxreadwidth,max(x for x,y in qs)-min(x for x,y in qs),max(y for x,y in qs)-min(y for x,y in qs))
assert (maxP,maxL,maxQwidth,maxreadwidth)==(44,22,11,9)
out={'status':'all cyclic phases and finite Boolean/geometry ingredients independently verified','single_rail_missing_black_classes':7,'bilateral_union_minimum_guard_errors':best,'union_profile_count':len(profiles),'white_subset_cases':1<<len(F),'max_endpoint_mask':maxP,'max_first_L_inputs':maxL,'max_tile_coordinate_width':maxQwidth,'max_period_read_coordinate_width':maxreadwidth,'history_error_per_standard_block':maxL+2*maxP,'parallel_transition_period_bound':20,'perpendicular_intersection_period_bound':11,'safe_discard_per_history_block':32,'analytic_consequence':'For a complete history partitioned into r legal standard powers and D other updates from m black cells, any subsequent N full reverse104 periods satisfy 4N <= m+D+238r. This counts entry-field errors, not an unconditional initial-mass fuel theorem.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
