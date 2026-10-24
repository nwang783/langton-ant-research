"""Complete two-ended certificate for a reversible G orbit; no search exhaustion is acceptance."""
from pathlib import Path
import hashlib,json
from check_return_permanent_output_debt import DXY,future
from blank_collision_operator import H
P=Path(__file__).parent
G={(0,-1),(1,1),(1,3),(2,2)}
PHASES={H[i:]+H[:i]for i in range(104)}
def R(p,h):return(p[0]-DXY[h][0],p[1]-DXY[h][1]),(h+2)%4

def run(B0,p0,h0,N):
 B={q:-i-1 for i,q in enumerate(sorted(B0))};p=p0;h=h0;word=[];mass=[len(B)];poses=[[p,h]];deaths={};events=[];first={};states=[]
 for t in range(N):
  states.append(set(B));first.setdefault(p,t);old=B.pop(p,None);events.append(old)
  if old is None:B[p]=t;h=(h+1)%4;word.append('R')
  else:deaths[old]=t;h=(h-1)%4;word.append('L')
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1]);poses.append([p,h]);mass.append(len(B))
 states.append(set(B));w,dr,tail,tests=future(B,p,h);assert w in PHASES
 deaths.update({i:N+t for i,t in tail.items()})
 # Finite exact mass range of one all-future certified period.
 delta=[0]
 for ch in w:delta.append(delta[-1]+(1 if ch=='R'else-1))
 assert delta[-1]==12
 return dict(B=B,p=p,h=h,word=''.join(word),mass=mass,poses=poses,deaths=deaths,events=events,first=first,states=states,tail_word=w,drift=dr,tests=tests,tail_relative_mass_min=min(delta),tail_relative_mass_max=max(delta))

forward=run(G,(0,0),1,390)
rp,rh=R((0,0),1);assert(rp,rh)==((-1,0),3)
reverse=run(G,rp,rh,1040)
assert min(forward['mass'])==min(reverse['mass'])==4
assert [i for i,x in enumerate(forward['mass'])if x==4]==[0,2]
assert [i for i,x in enumerate(reverse['mass'])if x==4]==[0]
assert len(forward['B'])+forward['tail_relative_mass_min']>4
assert len(reverse['B'])+reverse['tail_relative_mass_min']>4
assert sorted(forward['first'][q]for q in G)==[1,22,32,58]
# Literal full-field forward replay from the certified negative endpoint.
B=set(reverse['B']);p,h=R(reverse['p'],reverse['h']);negp,negh=p,h;backword=[]
for i in range(1040):
 n=1040-i;assert B==reverse['states'][n]and(p,h)==R(*reverse['poses'][n])
 if p in B:B.remove(p);h=(h-1)%4;backword.append('L')
 else:B.add(p);h=(h+1)%4;backword.append('R')
 p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
assert(B,p,h)==(G,(0,0),1)
assert ''.join(backword)==''.join('L'if c=='R'else'R'for c in reverse['word'][::-1])
# ENTIRE forward-relevant current population on the positive half orbit.
relevant=4;profile=[4]
for t,old in enumerate(forward['events']):
 relevant+=int(t in forward['deaths'])if old is None else -1;profile.append(relevant)
assert min(profile)==4 and [i for i,x in enumerate(profile)if x==4]==[0,2]
# Exact104 phase relevance and translated pruning closure, with all full fields retained.
B=dict(forward['B']);p=forward['p'];h=forward['h'];C0=None;tail_profile=[];root_tests=[]
for i in range(105):
 w,dr,dead,tests=future(B,p,h);C={q for q,j in B.items()if j in dead};tail_profile.append(len(C));root_tests.append(tests)
 if i==0:C0=C
 if i==104:
  assert C=={(q[0]+dr[0],q[1]+dr[1])for q in C0};break
 old=B.pop(p,None)
 if old is None:B[p]=390+i;h=(h+1)%4
 else:h=(h-1)%4
 p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
assert min(tail_profile)==11 and max(tail_profile)==22

def serialize(z):
 return dict(prefix_length=len(z['word']),prefix_word=z['word'],prefix_masses=z['mass'],prefix_poses=z['poses'],complete_terminal_field=[dict(cell=q,identity=i,future_consumption=z['deaths'].get(i))for q,i in sorted(z['B'].items())],tail_pose=[z['p'],z['h']],tail_word=z['tail_word'],tail_drift=z['drift'],tail_parity_tests=z['tests'],tail_relative_mass_min=z['tail_relative_mass_min'],tail_relative_mass_max=z['tail_relative_mass_max'],tail_mass_gain=12)
out=dict(status='AUTHOR complete two-ended certificate; independent audit requested',scope='Literal G orbit only. Refutes reducing every two-sided orbit to <=2 black cells, even after deleting cells never read in either direction. Does not refute capture or general well-founded potentials.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in ['check_return_permanent_output_debt.py','blank_collision_operator.py']},seed=sorted(G),original_pose=[[0,0],1],reverse_conjugate_pose=[rp,rh],forward=serialize(forward),reverse_conjugate=serialize(reverse),original_negative_endpoint=dict(time=-1040,black=sorted(reverse['B']),pose=[negp,negh],full_forward_recovery_word=''.join(backword),full_fields_matched=1040),global_full_black_minimum=4,global_full_minimum_times=[0,2],forward_relevant_profile=profile,forward_tail_relevant_profile=tail_profile,forward_tail_phase_parity_tests=root_tests,global_forward_relevant_minimum=4,global_forward_relevant_minimum_times=[0,2],initial_black_consumptions=[dict(cell=q,time=forward['first'][q])for q in sorted(G)],negative_relevance_reason='Every current black cell at a negative time is either consumed before cut0 or survives to one of the four cut0 black cells, all of which are consumed forward. Thus C*(t)=B_t for every t<=0.',bidirectional_unread_black_cells='none at every integer cut')
(P/'TWO_SIDED_G_MINIMUM_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print('full two-sided minimum4 at0,2; whole relevant minimum4 at0,2')
print('forward terminal mass/min',len(forward['B']),forward['tail_relative_mass_min'],'reverse',len(reverse['B']),reverse['tail_relative_mass_min'])
print('reverse original endpoint',negp,negh,'reverse drift',reverse['drift'],'prefix1040; all current input accounted')
