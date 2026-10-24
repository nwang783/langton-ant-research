#!/usr/bin/env python3
"""Author check of a local all-cap four-step skipped-rank contradiction."""
import json
from pathlib import Path
from itertools import combinations,product
D=((0,1),(1,0),(0,-1),(-1,0))
def qwords(I,J):
 out=[]
 for n in range(2*(I+J)+1):
  z=I+(n+1)//2-J
  if z%2:continue
  X=z//2;Y=I-X
  if not 0<=X<=(n+1)//2 or not 0<=Y<=n//2:continue
  for rr,ll in product(combinations(range(0,n,2),X),combinations(range(1,n,2),Y)):
   N=set(rr)|set(ll);h=tuple(0 if k in N else 2 for k in range(n));nn=sorted(N);ww=[k for k,x in enumerate(h)if(x+(1 if k%2==0 else-1))%4==3]
   if nn[1]==ww[2]+1:out.append(h)
 return out

def edge(H,p,j,q,k):
 hs=H[p];h=(hs[j]+(1 if j%2==0 else-1))%4
 assert q==(p[0]+D[h][0],p[1]+D[h][1]) and H[q][k]==h
 src=[z for z,x in enumerate(hs)if(x+(1 if z%2==0 else-1))%4==h]
 dst=[z for z,x in enumerate(H[q])if x==h]
 assert len(src)==len(dst)and src.index(j)==dst.index(k)
 return {'source':[p,j],'target':[q,k],'heading':h,'physical_ordinal':src.index(j)}

def main():
 A0=(0,1);A1=(1,0);B0=(0,0);Q1=(1,1);out=[]
 for ah in((3,3,1,1),(3,3,1,1,3)):
  I=len(ah)-2;qs=qwords(I,3);assert len(qs)==2 and all(q[:5]==(2,2,2,0,0)for q in qs)
  for qh in qs:
   H={A0:(3,1,3,3),A1:ah,B0:(0,2),Q1:qh}
   skip=[(A1,0),(Q1,3),(A0,3),(B0,1),(A1,3)]
   firstret=[(Q1,3),(A0,3),(B0,1),(A1,3),(Q1,4)]
   se=[edge(H,*a,*b)for a,b in zip(skip,skip[1:])];re=[edge(H,*a,*b)for a,b in zip(firstret,firstret[1:])]
   assert len({p for p,j in skip[1:-1]})==3 and A1 not in{p for p,j in skip[1:-1]}
   out.append({'A1_headings':ah,'Q1_headings':qh,'complete_named_histories':{str(p):h for p,h in H.items()},'skipped_chain':se,'first_return':re,'forced_A1_rank0_to_rank3_gap':4,'minimum_from_three_consecutive_return_gaps':12})
 result={'scope':__doc__,'models_checked':len(out),'records':out,'all_period_contradiction':'The fixed physical four-step chain goes directly from A1 rank0 to rank3. Complete ranks1 and2 cannot occur in between. Equivalently12<=4.','limitations':'Only the two supplied one-singleton minimum interfaces are excluded. Higher fields remain open, no general g8 exclusion.'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='records'},indent=2))
if __name__=='__main__':main()
