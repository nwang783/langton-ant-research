#!/usr/bin/env python3
"""Independent exhaustive literal control for the R-first normal form."""
from itertools import product
from pathlib import Path
import json
D=((0,1),(1,0),(0,-1),(-1,0))
def feasible(s):
 p=(0,0);h=0;last={};fuel=set()
 for odd in s:
  for c in ('R',odd):
   if p in last and last[p]==c:return False,None
   if p not in last and c=='L':fuel.add(p)
   last[p]=c;h=(h+(1 if c=='R'else-1))%4;d=D[h];p=p[0]+d[0],p[1]+d[1]
 return True,fuel

def language(s):
 n=len(s)
 return any(('L'*a+'RR').startswith(s)for a in range(n+1))or any(('R'+'L'*b+'RR').startswith(s)for b in range(1,n+1))
if __name__=='__main__':
 totals=[]
 for n in range(17):
  good=0
  for tup in product('RL',repeat=n):
   s=''.join(tup);ok,f=feasible(s);assert ok==language(s),(s,ok)
   if ok:
    good+=1;assert len(f)==s.count('L');assert n<=len(f)+3
  totals.append(dict(pairs=n,words=2**n,feasible=good))
 for m in range(1,21):
  s='R'+'L'*m+'RR';ok,f=feasible(s);assert ok and len(f)==m and len(s)==m+3
 out=dict(status='PASS; independent literal controls, not replacement for the all-length argument',cases=totals,total_words=sum(z['words']for z in totals),sharp_controls=20)
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
