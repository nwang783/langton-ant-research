from pathlib import Path
from fractions import Fraction
from itertools import product
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'TEN_MODULE_HEADING_KERNEL_AND_NEUTRAL_COUNTERCHECK.md';assert sha(P).startswith('6a144e15');assert sha(D/'certify_prepared80_neutral_four_heading_obstruction.py')=='cb7b05d9f2ce36d89a8f32585897b439f7e798adf85973e7ccdb5359e2b5d823';F=D/'prepared80_neutral_four_heading_obstruction_certificate.json';assert sha(F)=='9f427efe09e882dbbf0de8166f69081975ff531e2e549585e0cf155ff46263f6';J=json.loads(F.read_text());M='RRRRLLLLRL';A,B,C,Dw=['RLRRRRL','RRRRL','RRRRLRLRLRRRRL','LRRL'];V=[1j,1,-1j,-1];xy=lambda z:[int(z.real),int(z.imag)]
def geo(w,h):
 p=0j;out=[]
 for i,c in enumerate(w):out.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 return out,p,h
columns=[]
for h in range(4):
 E,p,e=geo(M,h);assert e==h;q=sum(1 if c=='R'else-1 for t,(_,_,c)in enumerate(E)if(t+h)%2==1);columns.append(xy(p)+[q])
assert columns==[[1,1,-1],[1,-1,1],[-1,-1,-1],[-1,1,1]]
# Exact rational rank and kernel, not a finite exponent sample.
mat=[[Fraction(columns[c][r])for c in range(4)]for r in range(3)];rr=0;piv=[]
for c in range(4):
 k=next((i for i in range(rr,3)if mat[i][c]),None)
 if k is None:continue
 mat[rr],mat[k]=mat[k],mat[rr];v=mat[rr][c];mat[rr]=[x/v for x in mat[rr]]
 for i in range(3):
  if i!=rr:v=mat[i][c];mat[i]=[x-v*y for x,y in zip(mat[i],mat[rr])]
 piv.append(c);rr+=1
 if rr==3:break
assert piv==[0,1,2]and mat==[[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]]
ce,_,_=geo(C,2);assert[i for i,(_,h,c)in enumerate(ce)if h==1]==[3,5,7,9,13]
def templates(k):
 pn=pc=0j;tn=tc=0;h=0;out=[]
 for name,w,an,ac in [('M0',M,1,2),('A',A,0,1),('M1',M,1,1),('B',B,0,1),('M2',M,1,1),('Cpre',C[:k],0,1),('ME',M,1,0),('Cpost',C[k:],0,1),('M3',M,0,1),('D',Dw,0,1)]:
  E,v,hh=geo(w,h)
  if name=='ME':assert h==1
  for i,(p,hi,ch)in enumerate(E):out.append(dict(name=name,phase=i,count=[an,ac],x=[int(pn.real),int((pc+p).real)],y=[int(pn.imag),int((pc+p).imag)],step=xy(v),time=[tn,tc+i],time_step=len(w),turn=ch,heading=hi))
  pn+=an*v;pc+=ac*v;tn+=len(w)*an;tc+=len(w)*ac;h=hh
 assert(pn,pc,tn,tc,h)==(0j,4+4j,40,80,0);return out
ceildiv=lambda a,b:-((-a)//b)
def match(z,Q,L,U):
 if z['count']==[0,1]:jn=jc=0
 else:
  co=next(i for i,v in enumerate(z['step'])if v);step=z['step'][co];assert abs(step)==1;a=z['x']if co==0 else z['y'];jn=(Q[co][0]-a[0])//step;jc=(Q[co][1]-a[1])//step
 for i,a in enumerate([z['x'],z['y']]):
  v=z['step'][i];aa=a[0]+v*jn-Q[i][0];bb=a[1]+v*jc-Q[i][1]
  if aa:
   n=Fraction(-bb,aa)
   if n.denominator!=1:return
   n=int(n);L=max(L,n);U=n if U is None else min(U,n)
  elif bb:return
 for aa,bb in[(jn,jc),(z['count'][0]-jn,z['count'][1]-1-jc)]:
  if aa>0:L=max(L,ceildiv(-bb,aa))
  elif aa<0:hi=bb//(-aa);U=hi if U is None else min(U,hi)
  elif bb<0:return
 if U is not None and L>U:return
 return dict(template=z['name'],phase=z['phase'],j=[jn,jc],n_interval=[L,U],time=[z['time'][0]+z['time_step']*jn,z['time'][1]+z['time_step']*jc],turn=z['turn'])
def positive(a,b,L,U):
 assert a*L+b>0
 if U is None:assert a>=0
 else:assert a*U+b>0
pieces=0;domains={}
for r in J['symbolic_physical_cell_covers']:
 k=r['cut'];ts=templates(k);assert ts==r['all_templates'];L,U=r['range'];Q=r['Q'];matches=[x for z in ts if(x:=match(z,Q,L,U))is not None];assert matches==r['all_matching_templates'];cursor=L
 for part in r['pieces']:
  lo,hi=part['interval'];assert lo==cursor;cursor=None if hi is None else hi+1;hh=part['complete_history'];act=[]
  for m in matches:
   a,b=m['n_interval'];overlap=max(lo,a)<=min(hi if hi is not None else 10**30,b if b is not None else 10**30)
   if overlap:assert a<=lo and(b is None or hi is not None and b>=hi);act.append(m)
  assert {json.dumps(m,sort_keys=True)for m in hh}=={json.dumps(m,sort_keys=True)for m in act}
  for x,y in zip(hh,hh[1:]):positive(y['time'][0]-x['time'][0],y['time'][1]-x['time'][1],lo,hi)
  x,y=part['bad_phases'];i=next(i for i,z in enumerate(hh)if[z['template'],z['phase']]==x);assert[hh[i+1]['template'],hh[i+1]['phase']]==y and hh[i]['turn']==hh[i+1]['turn'];pieces+=1
 assert cursor==(None if U is None else U+1);domains.setdefault(k,[]).append([L,U])
assert pieces==9 and domains=={3:[[1,None]],5:[[1,None]],7:[[1,None]],9:[[1,1],[2,None]],13:[[1,1],[2,None]]}
# Small literal regressions only; the affine complete-history proof above is all-n.
for k,n in product([3,5,7,9,13],[1,2,7]):
 w=M*(n+2)+A+M*(n+1)+B+M*(n+1)+C[:k]+M*n+C[k:]+M+Dw;E,p,h=geo(w,0);assert(p,h,len(w),w.count('R')-w.count('L'))==(4+4j,0,80+40*n,12);last={};bad=False
 for p,h,c in E:
  if p in last and last[p]==c:bad=True
  last[p]=c
 assert bad
out=dict(status='PASS heading-count kernel and five all-n neutral same-cell obstructions',proof=sha(P),certificate=sha(F),script=sha(S),matrix=columns,kernel=[1,1,1,1],complete_affine_history_pieces=pieces,analytic_review=['Every move toggles checker parity and incoming axis, so with initialN at0 all vertical arrivals are checker-even and horizontal arrivals checker-odd. Literal M restores heading and contributes exactly the four displayed columns. Rational elimination has rank3 and kernel span(1,1,1,1).','For a fixed heading-restoring router template, fullWHITE residue bounds |X|,|Y|<=g0/2 and0<=q<=g0 give finitely many integer triples. If one heading is absent, its total0 fixes the common kernel parameter; every individual nonnegative run count is bounded by its fixed heading total. If allfour occur, the common mode is algebraically invisible. No physical realizability is inferred from this nullspace.','All event templates are rebuilt from literal geometry with exact affine starts/times and module-instance indices. Two coordinate equations and both index inequalities independently reproduce EVERY matching physical-cell event and its full integern domain. Nine complete-history pieces cover allfive cuts for alln>=1, with exact affine strict ordering and consecutive identical-turn witnesses. The exceptional earlierL atcut13,n2 is retained, not treated as a fresh cell.','This is a finite-factor impossibility for these five supplied neutral extensions, independent of quotient, firstcolor, exterior field or WHITE premise. It does not exclude general four-heading templates, other insertions, changed routers or WHITE lifetime winding.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
