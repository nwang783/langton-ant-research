#!/usr/bin/env python3
"""The signed V20 exit physically reuses its old rod, then enters standard104.
One forced first-return adapter and one fixed standard-word tail query.
No cap, phase, seed, period or growing-horizon scan.
"""
from pathlib import Path
import sys,json,hashlib
from collections import deque
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).parent
sys.path.insert(0,str(ROOT/'stateful_growth_quadratic_2026-10-23'))
from quadratic_lap_validator import Context,D
ctx=Context(max_operations=100000000)
source=HERE/'guard_exchange_exit.json';old=json.loads(source.read_text());DOMAIN=old['domain']
B=ctx.set(old['complete_returned_relation'])
std=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
C63='RRRLRRRRLLLLRLLRRRRLLRLRRRRLRRRRLLLLRLRRRRLRLLLLRRRRLRRRRLRRLRR'
# Derive the one adapter by stopping at the FIRST actual untouched rod cell.
L={(-1,-1),(0,-2),(0,2),(-2,3),(-1,3),(-2,1),(-3,2),(-3,0)}
local=set(L);p=(-4,0);h=3;derived='';reads=[]
while not(p[1]==0 and p[0]>=1):
 assert p[0]<19 # No possible far cap on the whole r>=10 cone.
 t='L'if p in local else'R';reads.append((p,h,t));derived+=t
 if p in local:local.remove(p)
 else:local.add(p)
 h=(h+(1 if t=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
assert derived==C63 and p==(1,0)and h==2
# Derive the fixed remote continuation until the first observed canonical
# 104-word block. The full infinite tail is verified below, not inferred.
remote={(-1,-1),(2,-1),(3,0),(3,1),(0,1),(1,1),(-1,2),(0,2),(1,2),(2,2),(0,3),(1,3)}
ledger=set();p=(0,0);h=1;word='';last=deque(maxlen=104)
cyclic={(std+std)[i:i+104]for i in range(104)}
while True:
 t='L'if ((p in remote or(p[1]==1 and p[0]<=-1))!=(p in ledger))else'R'
 word+=t;last.append(t)
 if p in ledger:ledger.remove(p)
 else:ledger.add(p)
 h=(h+(1 if t=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 if len(last)==104 and ''.join(last)in cyclic:break
 # The fixed finite derivation is reproducibly bounded by the supplied252
 # letters; failure is an error, never interpreted as no tail.
 assert len(word)<=252
assert len(word)==252
C148=word[:-104];H=word[-104:];assert len(C148)==148 and H in cyclic
# Exact all-parameter literal continuation on the COMPLETE signed board.
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def point(q):
 return ctx.set('[M,r]->{[x=-2M+'+str(q[0])+',y='+str(q[1])+']:'+DOMAIN+'}')
def affinepoint(q):
 return ctx.set('[M,r]->{[x=-2M+2r+'+str(q[0])+',y='+str(q[1])+']:'+DOMAIN+'}')
def do_constant(word,start,heading,remote_origin=False):
 global B
 p=start;h=heading;rr=[]
 for i,t in enumerate(word):
  z=affinepoint(p)if remote_origin else point(p)
  current=B.intersect(z)
  assert(current.is_equal(z)if t=='L'else current.is_empty()),(i,p,h,t,str(current))
  B=xor(B,z);rr.append(dict(phase=i,relative=p,heading=h,turn=t))
  h=(h+(1 if t=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return p,h,rr
p,h,rr63=do_constant(C63,(-4,0),3);assert(p,h)==((1,0),2)
p,h,one=do_constant('L',p,h);assert(p,h)==((2,0),1)
# Every read in T^(r-1) is distinct. The inherited black rod, not new input,
# supplies exactly its two L phases; its row1 output has current identity.
rail=[]
for phase,(y,parity,t)in enumerate(((0,0,'L'),(1,0,'R'),(1,1,'R'),(0,1,'L'))):
 z=ctx.set('[M,r]->{[x,y]:'+DOMAIN+f' and y={y} and exists(j:0<=j<r-1 and x=-2M+2+2j+{parity})'+'}')
 rail.append(z);current=B.intersect(z)
 assert(current.is_equal(z)if t=='L'else current.is_empty())
for i,z in enumerate(rail):
 for zz in rail[:i]:assert z.intersect(zz).is_empty()
for z in rail:B=xor(B,z)
# Actual head is now (-2M+2r,0,E).
p,h,rr148=do_constant(C148,(0,0),1,True)
assert p==(2,-2)and h==1
before_tail=B
# Exact all-future104 front query. In a fixed phase, the translated cells
# are injective. All possible earlier physical reads arise from one fixed
# integer period difference per other phase.
P=[];pos=p;hh=h
for i,t in enumerate(H):
 P.append((pos,hh,t));hh=(hh+(1 if t=='R'else-1))%4;pos=(pos[0]+D[hh][0],pos[1]+D[hh][1])
drift=(pos[0]-p[0],pos[1]-p[1]);assert drift==(2,2)and hh==h
alln=ctx.set('[M,r]->{[n]:'+DOMAIN+' and n>=0}')
tail_bad=[];prior_pairs=0
for i,(q,heading,t)in enumerate(P):
 ctx.reset_operations()
 tocell=ctx.map('[M,r]->{[n]->[x,y]:'+DOMAIN+f' and n>=0 and x=-2M+2r+{q[0]}+2n and y={q[1]}+2n'+'}')
 current=tocell.reverse().binary('intersect_domain',before_tail).range()
 for j,(v,hj,tj)in enumerate(P):
  dx,dy=v[0]-q[0],v[1]-q[1]
  if dx!=dy or dx%2:continue
  delta=dx//2 # earlier period m=n-delta
  if 104*delta+i-j<=0:continue
  prior=ctx.set('[M,r]->{[n]:'+DOMAIN+f' and n>=0 and n>={delta}'+'}')
  current=xor(current,prior);prior_pairs+=1
 bad=alln.subtract(current)if t=='L'else current
 if not bad.is_empty():tail_bad.append(dict(phase=i,turn=t,bad=str(bad.coalesce())))
assert not tail_bad,tail_bad
# One full uninterrupted finite-board replay to tail entry plus two whole
# 104 blocks. No field mutation outside actual turns.
c=json.loads((HERE/'guard_exchange_exit_M50_r51.json').read_text());seed={tuple(q)for q in c['seed']}
full=c['word']+C63+'L'+'LRRL'*50+C148
actual=set(seed);pos=(0,0);hh=1
for i,t in enumerate(full+H*2):
 assert('L'if pos in actual else'R')==t,(i,pos,hh,t)
 if pos in actual:actual.remove(pos)
 else:actual.add(pos)
 hh=(hh+(1 if t=='R'else-1))%4;pos=(pos[0]+D[hh][0],pos[1]+D[hh][1])
assert len(full)==1892 and pos==(8,2)and hh==1
report=dict(status='EXACT ALL-PARAMETER SELF-OWNED ROD REUSE AND STANDARD104 CAPTURE',domain=DOMAIN,
 continuation='C63 L T^(r-1) C148 H104^infinity',C63=C63,C148=C148,H104=H,
 C63_first_rod_entry=dict(relative_to_old_p=[1,0],heading=2,length=63),
 rod_owner='same J-restored black row0, x=1..2r-1 relative to p; L consumes x1 and T^(r-1) consumes x2..2r-1',
 remote_entry=[['-2M+2r',0],1],capture_time='20M+12r+280',capture_pose=[['-2M+2r+2',-2],1],
 tail_drift=drift,tail_period=104,tail_prior_phase_pairs=prior_pairs,tail_bad_sets=tail_bad,
 complete_capture_board=str(before_tail),C63_reads=rr63,C148_reads=rr148,
 same_minimal_seed='2r+5 cells, no later supply',
 sample=dict(M=50,r=51,minimal_seed_mass=len(seed),capture_reads=len(full),capture_pose=[[4,-2],1],replayed_tail_periods=2,final_pose=[pos,hh]),
 source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 input_certificate_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 scope=__doc__)
(HERE/'exit_owned_rail_capture.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items()if k not in('complete_capture_board','C63_reads','C148_reads')},indent=2))
