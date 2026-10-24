"""Independent exact complete-board reflector audit, including unbounded tail.
Complex literal geometry; explicit two-index time order, no inverse-time filter.
"""
from pathlib import Path
import json,sys,hashlib,time
B=Path('/workspace/shared/langton');HERE=B/'causal_reduction/unit_scale';P=HERE/'highway_wake_reflector_certificate.json';cert=json.loads(P.read_text());data=json.loads((HERE/'highway_wake_reflector_collision.json').read_text());mirror=json.loads((HERE/'highway_wake_mirror_minimal.json').read_text());standard=json.loads((B/'recovered_bundle/ant_global/root/standard.json').read_text());H=standard['word'];W=data['collision_word'];assert cert['tail_word']==H and standard['heading']==3 and len(H)==104
sys.path.insert(0,str(B/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'));from isl_exact import Context
C=Context(max_operations=100000000);start=time.monotonic();domain='n>=30 and m>=30'
def xy(z):return int(z.real),int(z.imag)
def trace(word,p,h):
 reads=[]
 for j,c in enumerate(word):reads.append((p,c,j));h*=(-1j if c=='R' else 1j);p+=h
 return reads,p,h
def S(condition):return C.set('[n,m]->{[x,y]:'+domain+' and ('+condition+')}')
def T(condition):return C.set('[n,m]->{[t]:'+domain+' and ('+condition+')}')
def points(ps):return S(' or '.join(f'(x={x} and y={y})'for x,y in sorted(set(map(xy,ps))))or'false')
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
seed={complex(x,y)for x,y in standard['seed']};assert len(seed)==13
oldseed=S(' or '.join(f'(x=-2*n+{xy(-z)[0]} and y=-2*n+{xy(-z)[1]})'for z in seed))
incoming=S(' or '.join(f'(x=-2*m+1+{xy(1j*z)[0]} and y=2*m+{xy(1j*z)[1]})'for z in seed))
def striped(heading,ox,oy,count):
 slots,drift,end=trace(H,0j,heading);assert end==heading;dx,dy=xy(drift);odd=S('false');support=S('false')
 for q,c,j in slots:
  x,y=xy(q);ss=S(f'exists(j:0<=j<{count} and x=({ox})+{x}+{dx}*j and y=({oy})+{y}+{dy}*j)');odd=xor(odd,ss);support=support.union(ss)
 return odd,support.coalesce(),drift
oldpar,_,d=striped(1,'-2*n','-2*n','2*n');assert d==2+2j;old=xor(oldseed,oldpar)
prepar,presupport,d=striped(-1j,'-2*m+1','2*m','m-10');assert d==2-2j
assert old.intersect(incoming).is_empty() and old.intersect(presupport).is_empty()
initial=old.union(incoming);entry=xor(initial,prepar);assert initial.is_equal(C.set(cert['initial_relation'])) and entry.is_equal(C.set(cert['entry_relation']))
assert len(W)==19872;reads,end,heading=trace(W,-19+20j,-1j);assert end==-31-10j and heading==1j
need={};odd=set();seen_turn={}
for q,c,j in reads:
 if q not in need:need[q]=c
 else:assert seen_turn[q]!=c
 seen_turn[q]=c;odd.symmetric_difference_update([q])
assert len(need)==2416 and len(odd)==1260
assert points(q for q,c in need.items()if c=='L').subtract(entry).is_empty();assert points(q for q,c in need.items()if c=='R').intersect(entry).is_empty()
assert sorted(map(xy,odd))==list(map(tuple,cert['complete_collision_xor']))==list(map(tuple,data['complete_xor']))
after=xor(entry,points(odd));assert after.is_equal(C.set(cert['postcollision_relation']))
print('complete parametric seeds, approach, collision guards and XOR PASS',time.monotonic()-start,flush=True)
# Check EVERY earlier same-cell tail relation with separate period indices.
slots,finish,h=trace(H,end,heading);drift=finish-end;assert drift==-2+2j and h==heading
pairs=nonempty=0;tailread=S('false')
for q,c,j in slots:
 C.reset_operations();qx,qy=xy(q);dom=T('t>=0')
 selector=C.map(f'[n,m]->{{[x,y]->[t]:{domain} and t>=0 and x={qx}-2*t and y={qy}+2*t}}')
 color=selector.binary('intersect_domain',after).range()
 tailread=tailread.union(S(f'exists(t:t>=0 and x={qx}-2*t and y={qy}+2*t)'))
 for v,cv,l in slots:
  vx,vy=xy(v);prior=T(f't>=0 and exists(u:u>=0 and {qx}-2*t={vx}-2*u and {qy}+2*t={vy}+2*u and 104*u+{l}<104*t+{j})');pairs+=1
  if not prior.is_empty():nonempty+=1;color=xor(color,prior)
 failure=dom.subtract(color)if c=='L'else color;assert failure.is_empty(),(j,str(failure))
assert pairs==10816
# Exact whole-field damage, not a box-restricted board postcondition.
removed=old.intersect(entry).intersect(points(odd));assert removed.is_equal(points(complex(*p)for p in cert['erased_old_black_cells'])) and len(cert['erased_old_black_cells'])==152
strip=points(odd).intersect(S('-7<=x-y<=3'));assert strip.is_equal(points(complex(*p)for p in cert['changed_old_wake_strip_cells'])) and len(cert['changed_old_wake_strip_cells'])==298
assert need[-1+5j]=='L' and (-1+5j)in odd and points([-1+5j]).intersect(after).is_empty()
# The finite scatterer is proved by exact all-parameter read-set ownership.
needed=old.intersect(points(need).union(tailread)).coalesce();kept={complex(x,y)for x,y in mirror['mirror_black_cells']};assert len(kept)==322 and needed.is_equal(points(kept))
assert old.subtract(needed).intersect(presupport.union(points(need)).union(tailread)).is_empty()
assert points(kept).union(incoming).is_equal(C.set(mirror['initial_relation']))
controls=[]
def execute(board,p,h,word):
 for j,c in enumerate(word):
  assert(p in board)==(c=='L'),(j,p,c);board.symmetric_difference_update([p]);h*=(-1j if c=='R' else 1j);p+=h
 return p,h
for n,m in((30,30),(30,80),(80,30)):
 board={-z+complex(-2*n,-2*n)for z in seed};p,h=execute(board,complex(-2*n,-2*n),1,H*(2*n));assert(p,h)==(complex(2*n,2*n),1)and len(board)==24*n+13
 approach={1j*z+complex(-2*m+1,2*m)for z in seed};assert not board&approach;board|=approach;assert len(board)==24*n+26
 p,h=execute(board,complex(-2*m+1,2*m),-1j,H*(m-10));assert(p,h)==(-19+20j,-1j)
 p,h=execute(board,p,h,W);assert(p,h)==(-31-10j,1j) and len(board)==24*n+12*m+844
 execute(board,p,h,H*100)
 reduced=kept|approach;assert len(reduced)==335;p,h=execute(reduced,complex(-2*m+1,2*m),-1j,H*(m-10)+W);assert(p,h)==(-31-10j,1j);execute(reduced,p,h,H*100)
 controls.append(dict(n=n,m=m,tail_periods=100,complete_initial_mass=24*n+26,reduced_initial_mass=335))
result=dict(status='PASS independent whole-board all n,m>=30 and all future tail reads; exact322-cell scatterer pruning',candidate_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),collision_word_sha256=hashlib.sha256(W.encode()).hexdigest(),collision_read_cells=len(need),collision_xor_cells=len(odd),all_tail_ordered_pairs_including_self=pairs,nonempty_prior_relations=nonempty,erased_old_black=152,changed_old_strip_cells=298,mirror_cells=len(kept),mirror_total_initial_mass=335,tail_start_time='104*m+18832',tail_pose=[-31,-10,'N'],tail_drift=[-2,2],same_pose_sector=1,controls=controls,seconds=time.monotonic()-start,scope='One-shot finite prepared-wake/scatterer family only. Old guard is damaged; no renewable mirror, compound preparation path or noncapture model.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
