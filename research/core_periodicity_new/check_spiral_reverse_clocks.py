from fractions import Fraction as Q
import importlib.util,json
from pathlib import Path
p=Path(__file__).with_name('probe_spiral_reverse_charges.py');sp=importlib.util.spec_from_file_location('p',p);mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
def clocks(B,p,h):
 chi=lambda p:1 if sum(p)%2==0 else-1
 sig=chi(p)*(1 if h%2==0 else-1);e=1 if h in(0,1) else-1
 a=lambda e:Q(1,2) if e==1 else Q(-3,2)
 return tuple(-sig*sum(chi(q)*Q(3)**(s*sum(q)) for q in B)+a(s*e)*Q(3)**(s*sum(p)) for s in(1,-1))
out=[]
for n in[1,2,3,5,10,20,50,100]:
 B=mod.E(n);A,C=clocks(B,(0,0),0)
 A0=Q(253,54)+sum((Q(2,3)*(Q(9)**j+Q(9)**(-j))-Q(11,9) for j in range(2,n+1)),Q(0))
 assert A==A0 and C==9*A-8*n+2 and A>=Q(1,2)*9**n and C>=4*9**n
 for tx,ty in[(-n-4,n-1),(3,4),(0,1),(-101,42)]:
  assert(tx+ty)%2
  Y={(tx-x,ty-y) for x,y in B};a,c=clocks(Y,(tx,ty+1),0);s=tx+ty
  assert a==-Q(3)**s*C and c==-Q(3)**(-s)*A
 out.append({'n':n,'A':str(A),'C':str(C),'four_translations_passed':True})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print('All exact seven-arm clock and reversal checks passed:',len(out))
