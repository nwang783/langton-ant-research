"""Actual finite-board chain splitter and exact inverse-port controls."""
from active_flight import *
import json
from pathlib import Path
OUT=Path(__file__).parent
STAR={(0,-1),(1,-1),(1,0)}
def components(B,k):
 out=[];left=set(B)
 while left:
  q=min(left);C=comp(B,k,ends(q,k)[0]);out.append(sorted(C));left-=C
 return out

def test(n):
 seed={(-i,i)for i in range(1,n+1)};B=set(seed);p=(0,0);h=0;word='';cuts=[]
 for t in range(5+2*n+1):
  C=comp(B,1,cursor(p,h));cuts.append({'t':t,'p':p,'h':h,'active_mass':len(C),'field':sorted(B)})
  assert (p[0]+p[1]+h)%2==0 and sector(p,h)==1
  if t>=5 and(t-5)%2==0:
   j=(t-5)//2;want=STAR|{(-i,i-1)for i in range(1,j+1)}|{(-i,i)for i in range(j+1,n+1)}
   assert B==want and p==(-j-1,j)and h==3 and C=={(-i,i)for i in range(j+1,n+1)}
  if t<5+2*n:word+='L'if p in B else'R';p,h=step(B,p,h)
 assert word=='RRRRL'+'RL'*n and max(c['active_mass']for c in cuts)==n+4
 assert sorted(components(B,1))==sorted([sorted(STAR)]+[[(-i,i-1)]for i in range(1,n+1)])
 output=set(B);exitpose=(p,h);p=(p[0]-DIR[h][0],p[1]-DIR[h][1]);h=(h+2)%4
 assert p==(-n,n)and h==1 and sector(p,h)==0
 assert comp(B,0,cursor(p,h))==B and len(B)==n+3
 inverseword='';inverse_entry=(p,h)
 for t in range(5+2*n):inverseword+='L'if p in B else'R';p,h=step(B,p,h)
 assert B==seed and p==(0,-1)and h==2
 return {'n':n,'seed':sorted(seed),'entry_pose':[[0,0],0],'word':word,'exit_pose':exitpose,'output_field':sorted(output),'forward_output_components_k1':components(output,1),'inverse_entry_pose':inverse_entry,'inverse_word':inverseword,'inverse_exit_pose':[p,h],'inverse_entry_components_k0':components(output,0),'maximum_forward_active_mass':n+4,'cuts':cuts if n<=3 else None}
if __name__=='__main__':
 values=[test(n)for n in range(1,65)];out={'status':'AUTHOR_EXACT_FINITE_BOARD_CONTROLS_PENDING_AUDIT','tested_n':list(range(1,65)),'controls':[v for v in values if v['n']in(1,2,3,8,64)],'scope':'One-shot splitter and known J reversal only; opposite invariant sectors prevent direct replay of the inverse port by the same trajectory.'};(OUT/'chain_splitter_controls.json').write_text(json.dumps(out,indent=2)+'\n');print('passed n=1..64; n2 inverse',values[1]['inverse_word'])
