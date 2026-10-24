"""Exact spatial guard and tangent-record countercontrol; no sampled all-K inference."""
import json,hashlib
from pathlib import Path
P=Path(__file__).parent
D=((0,1),(1,0),(0,-1),(-1,0))
def geometry(p,h,w):
 out=[]
 for a in w:
  out.append(p);h=(h+(1 if a=='R' else -1))%4;p=tuple(p[j]+D[h][j] for j in range(2))
 return out,p,h

def replay(B,p,h,w):
 B=set(B);events=[]
 for t,a in enumerate(w):
  assert (p in B)==(a=='L'),(t,p,a,p in B)
  events.append([t,list(p),h,a]);B^={p};h=(h+(1 if a=='R' else -1))%4;p=tuple(p[j]+D[h][j] for j in range(2))
 return B,p,h,events

def multiple(v,d):
 k=None
 for a,b in zip(v,d):
  if b:
   if a%b:return None
   z=a//b
   if k is not None and z!=k:return None
   k=z
  elif a:return None
 return k

def verify_tail(B,p,h,w):
 Q,pe,he=geometry(p,h,w);d=tuple(pe[j]-p[j]for j in range(2));assert he==h and d!=(0,0)
 tests=0
 for i,q in enumerate(Q):
  intervals=[];checks={0}
  for j,r in enumerate(Q):
   k=multiple(tuple(r[u]-q[u]for u in range(2)),d)
   if k is not None and (k>0 or k==0 and j<i):intervals.append(k);checks.add(k)
  for x in B:
   k=multiple(tuple(x[u]-q[u]for u in range(2)),d)
   if k is not None and k>=0:checks|={k,k+1}
  for k in checks:
   x=tuple(q[u]+k*d[u]for u in range(2));assert ((x in B)^(sum(v<=k for v in intervals)%2))==(w[i]=='L');tests+=1
 return Q,d,tests

def main():
 a=json.loads((P/'TERMINAL_TRAP_CERTIFICATE.json').read_text());C=a['fixed_continuation'][46:];H=a['period'];I={(0,2),(0,3),(1,1),(2,4),(3,2),(3,3)}
 assert len(C)==232
 B,p,h,e=replay(I,(0,0),2,C);Q,d,tests=verify_tail(B,p,h,H)
 assert p==(0,-2) and h==2 and d==(2,-2)
 reads=[tuple(x[1])for x in e];G={x for x in set(reads)|set(Q)if x[1]>=1};assert len(G)==29 and G&I==I and max(y for x,y in Q)==-1
 # Every guard point is genuinely queried in the prefix, so every guard bit is necessary.
 assert G<=set(reads);first={x:reads.index(x)for x in G}
 F='RRRRLR';J='RRRLLLLRLR';assert C[:16]==F+J
 B16,p16,h16,e16=replay(I,(0,0),2,F+J);old16={x for x in reads[:16]if x[1]>=1};assert old16=={(-1,1),(0,1),(1,1)}
 assert p16==(2,-2)and h16==2
 assert all(reads[t][1]>-1 for t in range(6))and reads[6]==(1,-1)
 assert all(reads[t][1]>-2 for t in range(16))and reads[16]==(2,-2)
 variations=[]
 for x in sorted(G-old16):
  V=I^{x};_,pp,hh,_=replay(V,(0,0),2,C[:first[x]]);assert pp==x
  # This is the FIRST disagreement, never a changed earlier turn hidden in the table.
  BB,_,_,_=replay(V,(0,0),2,C[:first[x]]);assert (pp in BB)!=(C[first[x]]=='L')
  _,p2,h2,_=replay(V,(0,0),2,F+J);assert(p2,h2)==(p16,h16)
  variations.append(dict(cell=x,required_black=x in I,first_disagreement=first[x],initial_black=sorted(V)))
 assert len(variations)==26
 # Genuine fresh diagonal first return, not an arbitrary cut.
 q=(1,1);sponsor=(0,1);S=(I|{sponsor})-{q};W='RL'+C
 BB,pp,hh,ev=replay(S,q,2,W);assert(BB,pp,hh)==(B,p,h)
 assert len(S)==6 and min(sum(x)for x in S)==1 and sum(q)==2
 assert ''.join(x[3]for x in ev[1:7])=='LRRRRL'
 assert tuple(ev[12][1])==q and ev[12][2]==0 and all(tuple(x[1])!=q for x in ev[1:12])
 # Lower diagonal cap x+y<1 is initially pristine. The two-top first return has length12.
 assert {sum(tuple(x[1])) for x in ev[:12]}<={-1,0,1,2}
 assert sum(sum(tuple(x[1]))==-1 for x in ev[:12])==2
 # Every remote obstacle a_K is on OLD cap sum=1 and has first read exactly tail epoch K phase45.
 base=(5,-4);assert Q[45]==base and H[45]=='R'
 prefix_hits=[]
 for x in {tuple(z[1])for z in ev}:
  k=multiple(tuple(x[j]-base[j]for j in range(2)),d)
  if k is not None:prefix_hits.append([x,k]);assert k<0
 phase_hits=[]
 for j,r in enumerate(Q):
  delta=multiple(tuple(base[u]-r[u]for u in range(2)),d)
  if delta is not None:phase_hits.append(dict(phase=j,epoch_offset=delta,time_offset=104*delta+j))
 assert min(x['time_offset']for x in phase_hits)==45 and all(x['epoch_offset']>=0 for x in phase_hits)
 # Thus for ALL K>=0 all previous reads miss a_K and the read at234+104K+45 is R in base, L in perturbed.
 controls=[]
 for K in (0,1,2,11):
  x=tuple(base[j]+K*d[j]for j in range(2));V=S|{x};assert len(V)==7 and sum(x)==1 and x not in S
  word=W+H*K+H[:45];b,pp,hh,_=replay(V,q,2,word);assert pp==x and x in b
  controls.append(dict(K=K,obstacle=x,first_difference_time=len(word),required_base_turn='R',actual_turn='L'))
 result=dict(status='AUTHOR exact analytic all-K construction; independent audit pending',six_cell_axis_pristine_criterion=dict(initial_black=sorted(I),old_halfplane='y >= 1',pristine_halfplane='y <= 0',guard=sorted(G),guard_required_black=sorted(I),guard_required_white=sorted(G-I),guard_first_reads=[[x,first[x]]for x in sorted(G)],prefix=C,period=H,tail_pose=[p,h],tail_drift=d,ray_tests=tests),sharp_two_record_prefix=dict(word=F+J,old_input_forced_white=[[-1,1],[0,1]],old_input_forced_black=[[1,1]],unconstrained_guard_bit_count=26,unconstrained_required_black=5,unconstrained_required_white=21,one_bit_controls=variations),diagonal_record_tangent_family=dict(base_initial_black=sorted(S),initial_pose=[q,2],prefix=W,pristine_halfplane='x+y < 1',record_sponsor=sponsor,first_return_word=W[:12],first_return_duration=12,first_return_pose=[q,0],tail_start=234,obstacle_formula='(5+2K,-4-2K), integer K>=0',obstacle_mass=1,total_initial_mass=7,all_K_first_disagreement='279+104K',prefix_ray_intersections=prefix_hits,tail_ray_matches=phase_hits,finite_controls=controls))
 (P/'FRESH_RECORD_TRAP_BRIDGE_CHECKED.json').write_text(json.dumps(result,indent=2)+'\n')
 print({k:result[k] if k=='status' else 'recorded'for k in result})
if __name__=='__main__':main()
