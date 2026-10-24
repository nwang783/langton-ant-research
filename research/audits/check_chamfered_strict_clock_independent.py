from pathlib import Path
import sympy as s,json,hashlib
from fractions import Fraction as Q
B=Path('/workspace/shared/langton');r,k=s.symbols('r k',integer=True,nonnegative=True);a=s.symbols('a',positive=True);i=s.symbols('i',integer=True,nonnegative=True)
P=0;pos=[0j,0j,0j];h=1
for side in range(4):
 for word,which,length in [('LRRL',0,r),('RL',1,k),('R',None,1)]:
  z=0j;hh=h;slots=[]
  for c in word:slots.append((z,c));hh*=(-1j if c=='R' else 1j);z+=hh
  for off,c in slots:
   if c!='L':continue
   e=[int(t.real+t.imag)for t in(pos[0],pos[1],z,pos[2]+off)];er,ek,ei,ec=e
   assert er%2==ek%2==ei%2==0
   factor=length if ei==0 else (a**(ei*length)-1)/(a**ei-1)
   P+=(-1)**ec*a**(er*r+ek*k+ec)*factor
  if which is None:pos[2]+=z
  else:pos[which]+=z
  h=hh
assert pos==[0j,0j,0j] and h==1
# Use the finite geometric sum instead of leaving a symbolic summation.
Fr=(1-a**(2*r))/(a+1);rhs=2*Fr*(1-a**(-2*r-2*k-1))-k*a**(2*r-1)-k*a**(-2*r-2*k-1)+2*(1-a**(-2*k))/(a*a-1)
assert s.simplify(s.expand_power_base(P-rhs,force=True))==0
# Verify the eight one-step strict increments in the actual sector1.
dirs=(1j,1,-1j,-1);gamma=(Q(2,5),Q(2,5),Q(-8,5),Q(-8,5));increments=[]
for heading in range(4):
 p=complex((1-heading)%2,0);assert int(p.real+p.imag+heading)%2==1
 for black in(0,1):
  nh=(heading+(1 if black==0 else -1))%4;np=p+dirs[nh];w=Q(4)**int(p.real+p.imag);nw=Q(4)**int(np.real+np.imag)
  boardchange=(1-2*black)*(Q(-4)**int(p.real+p.imag));inc=gamma[nh]*nw-gamma[heading]*w+boardchange
  assert inc>0;increments.append(str(inc/w))
# Exact remainder bounds use 0<=1-16^-r<=1, 0<=sum16^-i<=1/15,
# and k/16^k<=1/16 for integer k>=1 (ratio(k+1)/(16*k)<=1/8).
assert Q(2,5)+Q(2,5)*Q(1,4)+Q(2,15)==Q(19,30)
assert Q(2,5)-Q(1,64)>0
F={(1,0),(1,1),(-3,1),(-3,2)};fv=sum((Q(-4)**(x+y)for x,y in F),Q(0));assert fv==Q(189,16)
assert -14*16+Q(152,15)+6+fv<0
out=dict(status='PASS independently summed twelve literal L families and exact strict-clock inequalities',symbolic_sum_identity=True,one_step_normalized_increments=increments,remainder_interval=['0','19/30'],four_cell_clock_correction=str(fv),scope='Fixed even clean layer shifts cannot be repaired by any changes in one fixed finite central support as r grows; specific four-cell control impossible for r,k>=3. No remote-work or general construction exclusion.',subject_sha256=hashlib.sha256((B/'causal_reduction/unit_scale/chamfered_multilayer_charge_obstruction.md').read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
