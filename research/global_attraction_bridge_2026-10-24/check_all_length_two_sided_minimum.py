"""One exact guarded-scattering rule, all-length induction data, and two-ended minimum.
No broad controller or seed scan. Complete fields and actual cursor retained.
"""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
from blank_collision_operator import H as CANON
P=Path(__file__).parent
K={(-1,2),(-1,3),(0,0),(0,4),(0,5),(0,6),(1,0),(1,1),(1,2),(1,5),(2,0),(2,3),(2,4)}
W='LRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR'
assert len(W)==104 and W in {CANON[i:]+CANON[:i]for i in range(104)}
D=(2,2)
def geom(p,h,w):
 Q=[];heads=[]
 for ch in w:
  Q.append(p);heads.append(h);h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return Q,heads,p,h
Q,H,end,eh=geom((0,0),1,W);assert end==D and eh==1

def run(seed,p,h,N,expected=None,snapcuts=()):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};first={};deaths={};word=[];mass=[len(B)];positions=[];snap={}
 for t in range(N):
  if t in snapcuts:snap[t]=(dict(B),p,h)
  positions.append(p);first.setdefault(p,t);old=B.pop(p,None)
  if old is None:B[p]=t;h=(h+1)%4;ch='R'
  else:deaths[old]=t;h=(h-1)%4;ch='L'
  if expected is not None:assert ch==expected[t]
  word.append(ch);p=(p[0]+DXY[h][0],p[1]+DXY[h][1]);mass.append(len(B))
 return dict(B=B,p=p,h=h,first=first,deaths=deaths,word=''.join(word),mass=mass,positions=positions,snap=snap)

def certify(z):
 w,dr,dead,tests=future(z['B'],z['p'],z['h']);assert w in {CANON[i:]+CANON[:i]for i in range(104)}
 z['tail_word']=w;z['tail_drift']=dr;z['tail_tests']=tests;z['deaths'].update({i:len(z['word'])+t for i,t in dead.items()});return z

def balance(w):
 a=[0]
 for ch in w:a.append(a[-1]+(1 if ch=='R'else-1))
 return dict(length=len(w),gain=a[-1],minimum=min(a),maximum=max(a),minimum_cuts=[i for i,v in enumerate(a)if v==min(a)])

# Literal mature incoming kernel for the single retained phase13, guard-3 rule.
g=-3;j=13;a=97;M=set()
for i,q in enumerate(Q):
 r=(q[0]-Q[j][0],q[1]-Q[j][1]);lo=-((r[0]-g)//2);hi=0 if i<j else -1
 for k in range(lo,hi+1):M.symmetric_difference_update({(r[0]+2*k,r[1]+2*k)})
assert(0,0)not in M;M.add((0,0));assert len(M)==24
kernel=certify(run(M,(0,0),H[j],312));V=kernel['word'];assert(kernel['p'],kernel['h'])==((2,6),H[a])and kernel['tail_word']==W[a:]+W[:a]and kernel['tail_drift']==D
assert min(x for x,y in kernel['positions'])>=g
kQ,_,_,_=geom(kernel['p'],kernel['h'],kernel['tail_word']);assert min(x for x,y in kQ)>=g
assert balance(V)==dict(length=312,gain=38,minimum=-2,maximum=39,minimum_cuts=[2])

# First interface, computed on the complete actual field.
q1=(202,201);U=W*100+W[:j];assert len(U)==10413
initial=run(K|{q1},(0,0),1,len(U),U)
assert(initial['p'],initial['h'])==(q1,H[j])and q1 not in initial['first']
assert {q for q in initial['B']if q[0]>=q1[0]+g}=={(q[0]+q1[0],q[1]+q1[1])for q in M}
assert max(x for x,y in initial['positions'])<408

# One exact repeated connector. Its proof translates identically at every stage.
F=W[a:]+W*100+W[:j];assert len(F)==10420
q2=(206,206);pair=run(M|{q2},(0,0),H[j],len(V+F),V+F)
assert(pair['p'],pair['h'])==(q2,H[j])and q2 not in pair['first']
assert {q for q in pair['B']if q[0]>=q2[0]+g}=={(q[0]+q2[0],q[1]+q2[1])for q in M}
assert min(x for x,y in pair['positions'])>=g
assert max(x for x,y in pair['positions'])<412
assert q2[0]+g>g and max(x for x,y in kernel['B'])<q2[0]+g
assert balance(F)==dict(length=10420,gain=1198,minimum=-3,maximum=1201,minimum_cuts=[11])
assert balance(V+F)==dict(length=10732,gain=1236,minimum=-2,maximum=1239,minimum_cuts=[2])

# Reverse-conjugate base certificate; all marker x coordinates exceed its ENTIRE read set.
reverse=certify(run(K,(-1,0),3,2704))
assert(reverse['p'],reverse['h'],len(reverse['B']))==((-11,28),1,299)and reverse['tail_drift']==(-2,2)
rQ,_,_,_=geom(reverse['p'],reverse['h'],reverse['tail_word']);maxX=max(x for x,y in reverse['positions']+rQ)
assert maxX==13 and min(reverse['mass'])==12 and [i for i,v in enumerate(reverse['mass'])if v==12]==[7,9]
assert len(reverse['B'])+balance(reverse['tail_word'])['minimum']>12

# All source inputs really consumed before the first marker; all current minimum-cut bits too.
base=certify(run(K,(0,0),1,208,W*2,snapcuts={4}))
assert max(base['first'][q]for q in K)==99
B4,p4,h4=base['snap'][4];assert len(B4)==11 and all(i in base['deaths']for i in B4.values())
assert min(base['mass'])==11 and [i for i,v in enumerate(base['mass'])if v==11]==[4]

controls=[]
for m in(0,1,2,5):
 markers={(202+206*i,201+206*i)for i in range(m)};seed=K|markers;assert len(seed)==13+m
 if m:
  sequence=U+(V+F)*(m-1)+V;N=10725+10732*(m-1)
 else:sequence=W*2;N=208
 z=certify(run(seed,(0,0),1,N,sequence,snapcuts={4}));assert z['tail_drift']==D
 assert min(z['mass'])==m+11 and [i for i,v in enumerate(z['mass'])if v==m+11]==[4]
 assert len(z['B'])+balance(z['tail_word'])['minimum']>m+11
 for i in range(m):assert z['first'][(202+206*i,201+206*i)]==10413+10732*i
 assert all(q in z['first']for q in seed)
 A4,pp,hh=z['snap'][4];assert len(A4)==m+11 and all(i in z['deaths']for i in A4.values())
 rz=certify(run(seed,(-1,0),3,2704,reverse['word']));assert set(rz['B'])==set(reverse['B'])|markers and min(rz['mass'])==m+12
 assert rz['tail_word']==reverse['tail_word']and rz['tail_drift']==(-2,2)
 # Actual original forward recovery from negative time -2704, with the edge-reversed pose.
 rp=(rz['p'][0]-DXY[rz['h']][0],rz['p'][1]-DXY[rz['h']][1]);rh=(rz['h']+2)%4
 bw=''.join('L'if c=='R'else'R'for c in reverse['word'][::-1]);back=run(set(rz['B']),rp,rh,2704,bw)
 assert(set(back['B']),back['p'],back['h'])==(seed,(0,0),1)
 controls.append(dict(m=m,seed=sorted(seed),initial_mass=13+m,minimum_mass=m+11,only_minimum_time=4,minimum_pose=[pp,hh],minimum_full_black=sorted(A4),minimum_all_black_future_read=True,initial_first_consumptions=[dict(cell=q,time=z['first'][q])for q in sorted(seed)],positive_prefix_length=N,positive_prefix_word=z['word'],positive_terminal_pose=[z['p'],z['h']],positive_terminal_black=sorted(z['B']),positive_tail_word=z['tail_word'],positive_tail_drift=z['tail_drift'],positive_tail_tests=z['tail_tests'],reverse_prefix_length=2704,reverse_terminal_pose=[rz['p'],rz['h']],reverse_terminal_black=sorted(rz['B']),reverse_tail_word=rz['tail_word'],reverse_tail_tests=rz['tail_tests'],reverse_mass_minimum=m+12,negative_endpoint_pose=[rp,rh],negative_forward_recovery_reads=2704))
 print('m',m,'initial',13+m,'unique two-sided minimum',m+11,'at4','capture certificate',N,flush=True)

source_paths=['../sources/kehao95-core/four_cell_port/proof/guarded-scattering-renewal.md','../sources/kehao95-core/four_cell_port/verification/guarded_scattering/check.py','../sources/kehao95-core/four_cell_port/verification/guarded_scattering/check_results.json','../sources/kehao95-core/four_cell_port/evidence/review-2026-10-15.json','TWO_SIDED_G_MINIMUM_MANIFEST.json','check_return_permanent_output_debt.py','blank_collision_operator.py']
out=dict(status='AUTHOR exact all-m construction; independent audit requested',scope='Paid finite m-marker family, unbounded global two-sided FULL mass after deleting only bidirectionally unread black cells. No unbounded minimum of forward-only pruning, no counterexample to capture.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in source_paths},base=sorted(K),base_word=W,base_full_future_tests=base['tail_tests'],base_initial_first_reads=[dict(cell=q,time=base['first'][q])for q in sorted(K)],base_minimum4_black=sorted(B4),base_minimum4_pose=[p4,h4],rule=dict(input_phase=13,guard=-3,recovery=V,recovery_length=312,input_kernel=sorted(M),endpoint_pose=[kernel['p'],kernel['h']],endpoint_black=sorted(kernel['B']),minimum_read_x=min(x for x,y in kernel['positions']),maximum_read_x=max(x for x,y in kernel['positions']),future_minimum_x=min(x for x,y in kQ),full_tail_tests=kernel['tail_tests'],output_phase=97),initial_interface=dict(marker=q1,prefix_length=len(U),minimum_read_x=min(x for x,y in initial['positions']),maximum_read_x=max(x for x,y in initial['positions']),full_inside_field=sorted(q for q in initial['B']if q[0]>=199),cut_pose=[initial['p'],initial['h']]),pair_interface=dict(marker=q2,prefix_length=len(V+F),minimum_read_x=min(x for x,y in pair['positions']),maximum_read_x=max(x for x,y in pair['positions']),full_inside_field=sorted(q for q in pair['B']if q[0]>=203),cut_pose=[pair['p'],pair['h']]),balances={name:balance(w)for name,w in [('W',W),('initial_flight',U),('recovery',V),('connector',F),('repeated_block',V+F),('final_tail',W[97:]+W[:97])]},reverse_base=dict(prefix_word=reverse['word'],prefix_length=2704,prefix_masses=reverse['mass'],full_endpoint=sorted(reverse['B']),endpoint_pose=[reverse['p'],reverse['h']],tail_word=reverse['tail_word'],tail_drift=reverse['tail_drift'],tail_tests=reverse['tail_tests'],full_future_max_x=13,global_mass_minimum=12,minimum_reverse_times=[7,9],tail_mass_balance=balance(reverse['tail_word'])),controls=controls)
(P/'ALL_LENGTH_TWO_SIDED_MINIMUM_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
