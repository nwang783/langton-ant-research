#!/usr/bin/env python3
"""Literal countercontrols for the analytic no-board-only renewal-rank lemma."""
from pathlib import Path
import json,hashlib
P=Path(__file__).parent;V=((0,1),(1,0),(0,-1),(-1,0));H=json.loads((P.parent/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];F={''.join(H[(i+j)%104]for j in range(10))for i in range(104)}
assert all(''.join('RLLR'[(i+j)%4]for j in range(10))not in F for i in range(4))
def inverse(B,p,h):
 B=set(B);rev=[]
 for _ in range(10):
  v=V[h];q=p[0]-v[0],p[1]-v[1];c='R'if q in B else'L';B.symmetric_difference_update({q});h=(h-(1 if c=='R'else-1))%4;p=q;rev.append(c)
 return ''.join(reversed(rev))
def run(B,p,h,n,word='RLLR'):
 B=set(B);hist=inverse(B,p,h);past=hist;bad=hist not in F;events=[]
 for i,c in enumerate(word*n):
  assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1]
  hist=(hist+c)[-10:];b=hist not in F
  if b and bad:events.append(i)
  bad=b
 assert events[-1]==4*n-1 and len(events)>=4*n-10
 return B,p,h,past,events
reports=[]
for n in[3,4,11,50]:
 BR={(1,y)for y in range(2*n)};BL={(0,y)for y in range(2*n)};assert(1+2*n-1)%2==0
 b,p,h,hist,ev=run(BR,(0,0),0,n);assert b==BL and(p,h)==((0,2*n),0)
 b2,p2,h2,hist2,ev2=run(BL,(1,2*n-1),2,n);assert b2==BR and(p2,h2)==((1,-1),2)
 b3,p3,h3,hist3,ev3=run(BL,(0,0),0,n,'LRRL');assert b3=={(-1,y)for y in range(2*n)}and(p3,h3)==((0,2*n),0)
 reports.append({'T_K':len(ev3),'T_true_prior_ten':hist3,'T_maps_left_row_to_xminus1':True,'n':n,'mass':2*n,'right_to_left_pose':[p,h],'left_to_right_pose':[p2,h2],'true_prior_ten_R':hist,'true_prior_ten_L':hist2,'K_R':len(ev),'K_L':len(ev2),'last_read_K_in_both':True})
out={'scope':__doc__,'status':'PASS both exact finite transformations and final-renewal seams','controls':reports,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'board_only_renewal_rank_obstruction.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS board-only nonlinear renewal-rank obstruction; no physical concatenation asserted')
