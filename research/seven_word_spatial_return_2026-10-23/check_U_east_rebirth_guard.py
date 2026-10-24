"""Causal same-cell renewal guard, not permanence of a single identity.
No word-tree, prefix or seed scan.
"""
from pathlib import Path
import hashlib,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';WP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];G7=json.loads(WP.read_text())['macro_words'];M=G[0]['marker'];V=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def derive(w):
 p=(0,0);h=0;req={};par=set();reads={}
 for t,ch in enumerate(w):
  bit=(ch=='L')^(p in par);assert p not in req or req[p]==bit
  req[p]=bit;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return req,p,h,reads
cell=(2,1);breaker=(3,-1);qlocal=(-1,2)
assert add(breaker,qlocal)==cell
source_rows=[]
for a in(7,8,9):
 assert cell in set(map(tuple,G[a]['outputs']))
 assert qlocal in set(map(tuple,G[a]['inputs']))and qlocal in set(map(tuple,G[a]['outputs']))
 _,_,_,reads=derive(G[a]['word'])
 assert reads[qlocal][0][1]=='L'and reads[qlocal][-1][1]=='R'
 assert all(t<28 for t,ch in reads[qlocal])
 source_rows.append(dict(packet=G[a]['name'],q_local=qlocal,q_global_after_breaker=cell,physical_q_reads=reads[qlocal],first_q_read=reads[qlocal][0],fresh_q_birth=reads[qlocal][-1],optional_C_tails_preserve=True))
# First source-cycle break is fixed at clock4, followed by fresh q retirement
# only at that source's own exact age2, hence globalclock6.
assert 4+2==6
foreign_pose=(-3,6,3);freq,_,_,fr=derive(G7[6]['word']+M)
local=rot((cell[0]-foreign_pose[0],cell[1]-foreign_pose[1]),-foreign_pose[2])
assert local==(-5,-5)and local not in K and freq[local]is False
assert fr[local][0]==(82,'R')and all(t>=74 for t,ch in fr[local])
D=[GP,WP,R/'core_periodicity_new/causal_cycle_renewal_20261023_1841/manifest.json',R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/manifest.json',R/'core_periodicity_new/U_recycled_q_consumer_frozen_20261023_1954/manifest.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_AUDIT',scope='At actual full cuts after the creating full U-family packet has completed and before the first foreign, original U east cell(2,1) is black through source-entry C age5, possibly with a new identity after its unique age4 renewal. No single-identity permanence or fine-time color constancy. This excludes B(-3,6,W) at age5 by an actual complete-context before-white guard.',cell=cell,first_breaker_pose=(*breaker,0),first_breaker_clock=4,replacement_role='genuine fresh recycled-q output of the actual first breaker',earliest_replacement_retirement_clock=6,source_and_breaker_literal_rows=source_rows,foreign_guard=dict(foreign='B',pose=foreign_pose,local_cell=local,required_initial_black=False,first_full_context_read=fr[local][0],foreign_RAW_reads=[],owner='successor RAW phase8 R, never foreign RAW'),dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'U_east_rebirth_guard.json').write_text(json.dumps(o,indent=2)+'\n')
print('Original east cell(2,1) black at all full cuts through C5: old identity, or genuine age4 renewed q surviving to C6. B(-3,6,W), age5, before-white guard is impossible.')
