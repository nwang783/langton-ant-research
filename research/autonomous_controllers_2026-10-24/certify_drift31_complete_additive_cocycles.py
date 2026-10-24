#!/usr/bin/env python3
"""All universal Z/4 position/signed-turn cocycles on the full drift(3,1) quotient.
Analytic recurrence proves completeness without imposing any spatial period.
The finite parameter table is a proof control, not a trajectory search.
"""
from pathlib import Path
from itertools import product
import json,hashlib
R=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))

def build(x,y0,rho):
 y={0:y0}
 for j in range(1,6):y[j]=(y[j-1]+2*(x[j%3]+x[(j-1)%3]+rho))%4
 assert (y[5]+2*(x[0]+x[2]+rho))%4==y0
 A={};W={};psi={}
 for j in range(6):A[2*j]=x[j%3];A[2*j+1]=y[j]
 for t in range(12):
  w=((A[(t-1)%12]-A[t])if t%2==0 else(A[t]-A[(t+3)%12]-rho))%4
  W[t]=w;psi[t,t%2]=A[t];psi[t,t%2+2]=(A[t]+2*w)%4
 for(t,h),p in psi.items():
  for s in(-1,1):
   hh=(h+s)%4;dx,dy=D[hh];tt=(t+3*dy-dx)%12
   assert(psi[tt,hh]-p-W[t]*s+rho*dy)%4==0
 for t in range(12):assert W[(t+6)%12]==(W[t]+2*rho)%4
 return W,psi

def main():
 rows=[];distinct=set();failed={(c,a):0 for c,a in product(range(2),repeat=2)}
 for x in product(range(4),repeat=3):
  for y0,rho in product(range(4),repeat=2):
   W,psi=build(x,y0,rho);distinct.add((rho,tuple(W.values())))
   checks=[]
   for c,a in product(range(2),repeat=2):
    O=(0,1,2,6,7,6*c+1,6*a+2,6*a+4)
    residual=(sum(W[t%12]for t in O)-rho)%4
    assert residual==2*rho*(c+1)%4
    failed[c,a]+=int(residual!=0)
    checks.append({'c_parity':c,'a_parity':a,'residual':residual})
   rows.append({'x':x,'y0':y0,'rho':rho,'weights_T_mod12':list(W.values()),'potential24':[[t,h,v]for(t,h),v in sorted(psi.items())],'family_parity_controls':checks})
 assert len(rows)==1024 and len(distinct)==256
 assert failed=={(0,0):512,(0,1):512,(1,0):0,(1,1):0}
 # Exhaustively check each modular elimination used in the analytic recurrence.
 # This is local algebra only, with no imposed period and no dynamics premise.
 eliminations=0
 for xm1,x0,xp2,ym2,ym1,y0,rho in product(range(4),repeat=7):
  e1=(xp2-xm1-2*y0+2*ym2)%4==0
  e2=(3*y0-2*xp2-2*rho-2*x0+ym1)%4==0
  if e1 and e2:
   assert(y0-ym1-2*(x0+xm1+rho))%4==0;eliminations+=1
 result={'scope':__doc__,'analytic_parameters':'x0,x1,x2,y0,rho in Z/4; global additive potential gauge acts freely','parameter_models':1024,'distinct_weight_and_winding_pairs':256,'checked_local_transitions':1024*48,'recurrence_elimination_controls':eliminations,'arbitrary_j_recurrence':['x_(j+2)=x_(j-1)','y_j-y_(j-1)=2*(x_j+x_(j-1)+rho)','y_(j+3)=y_j+2*rho'],'complete_family_residual':'sum_(T in full O) w(T)-rho = 2*rho*(c+1) modulo4','parity_failure_counts':[{'c_parity':c,'a_parity':a,'failed_models':n}for(c,a),n in failed.items()],'models':rows,'dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['DRIFT31_MOD4_WINDING_ODD_INVENTORY.md','TURN_POSITION_COCYCLE_MODULUS_LIMIT.md','DRIFT31_MIDDLE_SHORT_FULL_ODD_REDUCTION.md']},'limits':'No complete front is constructed. No chronological, rank-dependent, board-nonlinear or multiplicity-weighted invariant is exhausted.'}
 (R/'drift31_complete_additive_cocycles_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
 print('PASS',len(rows),'parameter cocycles,',len(distinct),'weight/winding pairs;',1024*48,'transitions; odd c passes all')
if __name__=='__main__':main()
