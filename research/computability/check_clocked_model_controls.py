#!/usr/bin/env python3
"""Finite marker/cutoff boundary controls for the logical toy separation model.
Known halting times in these controls do not implement or solve universal HALT.
"""
import json,itertools
from pathlib import Path

def marker(t,H=None,c=None):
 return int(t>0 and not(t&(t-1)) and(H is None or t<H)and(c is None or t<c))
def next_power(t):return 1<<max(0,(max(t,1)-1).bit_length())
def bad(t,H,c):return any(marker(j,H,c)for j in range(t-9,t+1))
def event(t,H,c):return bad(t-1,H,c)and bad(t,H,c)
def renewal(t,H,c):
 p=next_power(t)
 for u in range(t,p+11):
  if event(u,H,c):return u+1
 return None

def zero_tail(t,H,c):
 p=next_power(t);return (H is not None and H<=p)or(c is not None and c<=p)

def check():
 count=0;tails=0;overlaps=0
 vals=[None,0,1,2,3,4,7,8,9,15,16,17,31,32,33,64,65]
 for H,c,t in itertools.product(vals,vals,range(-12,90)):
  expected=next((u+1 for u in range(t,300)if event(u,H,c)),None)
  ans=renewal(t,H,c);assert ans==expected,(H,c,t,ans,expected);count+=1
  exact=not any(marker(u,H,c)for u in range(t,300))
  assert zero_tail(t,H,c)==exact;tails+=1
 for H,c in itertools.product(vals,vals):
  expected=[u+1 for u in range(0,150)if event(u,H,c)]
  t=0
  for target in expected:
   t=renewal(t,H,c);assert t==target;overlaps+=1
 return dict(status='PASS finite boundary controls; universal logical construction is analytic',first_event_controls=count,zero_tail_controls=tails,overlapping_renewal_controls=overlaps)
if __name__=='__main__':
 out=check();Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
