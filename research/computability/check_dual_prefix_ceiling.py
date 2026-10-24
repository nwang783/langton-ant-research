#!/usr/bin/env python3
"""Exact slot formula versus all raw geometric words for one mixing matrix."""
from pathlib import Path
import itertools,json,math
D=((0,1),(1,0),(0,-1),(-1,0))
A=((3,2),(2,5));k=9;ell=(-2,3);m=11
records=[]
for coarse,(dx,dy) in enumerate(D):
 tx=A[0][0]*dx+A[0][1]*dy;ty=A[1][0]*dx+A[1][1]*dy
 for startH in [False,True]:
  H=(k+1)//2 if startH else k//2;V=k-H
  if any(v%2 for v in [H+tx,V+ty]) or abs(tx)>H or abs(ty)>V:continue
  E,W,N,S=(H+tx)//2,(H-tx)//2,(V+ty)//2,(V-ty)//2
  ph=E if ell[0]>=0 else W;pv=N if ell[1]>=0 else S
  formula=[]
  for j in range(k):
   hj=(j+1)//2 if startH else j//2;vj=j-hj
   formula.append(abs(ell[0])*(2*min(hj,ph)-hj)+abs(ell[1])*(2*min(vj,pv)-vj))
  actual=[-10**9]*k;count=0
  for es in itertools.combinations(range(H),E):
   for ns in itertools.combinations(range(V),N):
    x=y=0;ih=iv=0;count+=1
    for j in range(k):
     actual[j]=max(actual[j],ell[0]*x+ell[1]*y)
     horizontal=(j%2==0)==startH
     if horizontal:d=1 if ih in es else 3;ih+=1
     else:d=0 if iv in ns else 2;iv+=1
     x+=D[d][0];y+=D[d][1]
    assert (x,y)==(tx,ty)
  assert formula==actual
  records.append(dict(direction=coarse,start_horizontal=startH,count=count,ceiling_by_prefix=formula,maximum=max(formula)))
out=dict(status='ALL RAW PREFIX CEILINGS MATCH',matrix=A,k=k,covector=ell,dual_scale=m,total_words=sum(r['count'] for r in records),global_ceiling=max(r['maximum'] for r in records),records=records)
assert out['total_words']==48 and out['global_ceiling']==10
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
