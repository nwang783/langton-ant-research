from pathlib import Path
from collections import defaultdict
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];N=ROOT/'new_constructive_2026-10-23';MP=ROOT/'causal_reduction/unit_scale/prepared4352_capture_manifest.json'
assert hashlib.sha256(MP.read_bytes()).hexdigest()=='52d80fe06d739254a9d71615de67bfb6639d1f4d1301455b4f332d7110874f9b'
m=json.loads(MP.read_text());st={s['kind']:s for s in m['stages']};W=st['wave']['word'];T=st['source-transition']['word'];P=st['return-wave']['word'];Z=st['launch-end-response']['word'][:17395]
C=(N/'minimal_two_port_fixed_continuation.word.txt').read_text();assert hashlib.sha256(C.encode()).hexdigest()=='213e036d20414d5c4a3b943b1296d0594f649c7fd82ee028f80760255bae36dc'
H=json.loads((N/'minimal_two_port_M1_exact_tail.json').read_text())['tail_word'];std=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];assert H in{std[i:]+std[:i]for i in range(104)}
V=((0,1),(1,0),(0,-1),(-1,0))
def trace(w,p,h):
 reads=[]
 for c in w:
  reads.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1]
 return reads,p,h
def desc(w,p,h):
 r,q,g=trace(w,p,h);us=[sum(x)for x,h,c in r];return min(us),max(us),q,g
stages={name:desc(word,p,h)for name,word,p,h in [('W',W,(-2,3),3),('T1',T,(180,185),3),('nearestP',P,(195,189),0),('Z',Z,(117,111),0),('C',C,(9,-10),3),('H',H,(-2,26),0)]}
assert stages['W'][0]==1 and stages['W'][2:]==((24,29),3)
assert stages['T1'][0]==338 and stages['T1'][2:]==((195,189),0)
assert stages['nearestP'][0]==182 and stages['nearestP'][2:]==((117,111),0)
assert stages['Z'][2:]==((9,-10),3)and stages['C']==(-21,208,(-2,26),0)
assert stages['H']==(17,27,(-4,28),0)
# All extra W start at index>=7, hence u>=365. All T reads u>=156M+182.
# Reindex P from the common end: nearest copy fixed, every extra copy u>=338.
# Common stages preserve their order on u<=337, so minimal first-read colors
# and complete returned colors agree pointwise, including unread white cells.
assert 1+52*7==365 and 182+156==338
body='RLL'+W*7+T+P+Z;rr,p,h=trace(body,(-2,2),0);assert(p,h)==((9,-10),3)
first={};last={};seed=set();odd=set()
for q,hd,c in rr:
 if q in last:assert last[q]!=c
 else:
  first[q]=c
  if c=='L':seed.add(q)
 last[q]=c;odd.symmetric_difference_update({q})
assert len(seed)==5925 and all(sum(q)>0 for q in seed)
board=seed^odd;assert{q for q in board if sum(q)<=0}=={(-2,2),(10,-10)}
for q,hd,c in trace(C,p,h)[0]:assert(q in board)==(c=='L');board.symmetric_difference_update({q})
_,p,h=trace(C,p,h);assert(p,h)==((-2,26),0)and len(board)==14289
# Our existing independent whole-finite-board tail oracle, no author checker.
src=SELF.with_name('check_prepared1564_connected_capture_independent.py').read_text();func=src[src.index('def periodic('):src.index('reports=[]')];ns={'V':V,'defaultdict':defaultdict};exec(compile(func,str(SELF),'exec'),ns);periodic=ns['periodic']
bad,d,groups,tests=periodic(board,p,h,H);assert bad is None and d==(-2,2)
for a in groups:
 remote=(a[0]+1000000*d[0],a[1]+1000000*d[1]);assert periodic(board^{remote},p,h,H)[0] is not None
# Actual inverse ten from the whole minimal seed.
b=set(seed);q=(-2,2);g=0;back=[];backus=[]
for _ in range(10):
 v=V[g];q=q[0]-v[0],q[1]-v[1];c='R'if q in b else'L';backus.append(sum(q));b.symmetric_difference_update({q});g=(g-(1 if c=='R'else-1))%4;back.append(c)
history=''.join(reversed(back));assert history=='RLLLLRLLLL'and(min(backus),max(backus))==(-2,0)
F={''.join(std[(i+j)%104]for j in range(10))for i in range(104)};assert len(F)==84
def cost(w,hist):
 lastbad=hist not in F;k=0
 for c in w:
  hist=(hist+c)[-10:];bad=hist not in F;k+=bad and lastbad;lastbad=bad
 return hist,k
hist,k=cost('RLL',history);constant=k;coefficient=0;ledger=[('RLL',k)]
for name,w,a,b in [('W',W,3,4),('T',T,0,1),('P',P,1,0),('Z',Z,0,1),('C',C,0,1)]:
 if a:
  hist,k1=cost(w,hist);same,k2=cost(w,hist);assert same==hist;coefficient+=a*k2;constant+=k1+(b-1)*k2;ledger.append((name,k1,k2,a,b))
 else:hist,k=cost(w,hist);constant+=k;ledger.append((name,k))
_,seam=cost(H,hist);constant+=seam;ledger.append(('tail_full_period',seam))
assert(coefficient,constant)==(13269,118240)
_,direct=cost(body+C+H,history);assert direct==coefficient+constant
assert len(body)+len(C)==248488+28380
note=N/'minimal_two_port_allM_capture.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='cadf6e5dac56305e20888a6dbca75e88e3d9bc40944b47bc3b4856fdcf39ee66'
out=dict(status='PASS independent all-M minimal two-port capture by complete halfplane identity',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),stage_extrema=stages,M1_seed_mass=len(seed),M1_capture_mass=len(board),M1_literal_steps=len(body)+len(C),complete_tail_checks=tests,far_flip_controls=len(groups),true_inverse_ten=history,K_ledger=ledger,total_K_M_constant=[coefficient,constant],capture_time_M_constant=[28380,248488],capture_pose=[p,h],scope='Canonical first-L minimum seed of supplied Q_M for allM>=1, growing input mass. Whole low-halfplaneu<=337 agreement transfers fixedC and NW104 forever; not original394 seed, changedcaps or renewable module.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('M1',len(seed),len(body)+len(C),len(board),'K',coefficient,constant,'tail',tests)
