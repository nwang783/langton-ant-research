#!/usr/bin/env python3
"""Author local controls for a COMPLETE-read extreme proof, not independent audit."""
import sys,json,hashlib
from pathlib import Path
from itertools import product
ROOT=Path(__file__).resolve().parent
SRC=ROOT.parent/'sources/kehao95-core/wake_synthesis/verification/general_wake_parity'
sys.path.insert(0,str(SRC));import screen
D=((0,1),(1,0),(0,-1),(-1,0));change=lambda h:3*D[h][1]-D[h][0]
mn=[h for h in range(4)if change(h)<=0 and change((h+1)%4)>=0];mx=[h for h in range(4)if change(h)>=0 and change((h+1)%4)<=0];assert mn==[2]and mx==[0];assert change((2-1)%4)<0 and change((0-1)%4)>0
h13=[];v12=[];v8=[]
for n in range(1,5):
 for hs in product((1,3),repeat=n):
  out=[(h+(1 if j%2==0 else-1))%4 for j,h in enumerate(hs)]
  if hs.count(1)==1 and all(h==2 for h in out):h13.append(hs)
for n in range(3):
 hs=(0,)*n;out=[(h+(1 if j%2==0 else-1))%4 for j,h in enumerate(hs)]
 if 3 not in out:v12.append(hs)
for n in range(1,6):
 for hs in product((0,2),repeat=n):
  out=[(h+(1 if j%2==0 else-1))%4 for j,h in enumerate(hs)]
  if hs.count(0)==2 and all(h==1 for h in out):v8.append(hs)
assert h13==[(1,),(1,3)]and v12==[(),(0,)]and v8==[(0,2,0),(0,2,0,2)]
points=[(-8,0),(-7,0),(-7,-1),(-8,-1),(-8,0)];assert all((b[0]-a[0],b[1]-a[1])==D[h]for a,b,h in zip(points,points[1:],(1,2,3,0)))
for hs in v8:assert[ j for j,h in enumerate(hs)if h==0][1]==2 and[ j for j,h in enumerate(hs)if(h+(1 if j%2==0 else-1))%4==1][0]==0
examples=[]
for c in(2,3):
 T=[0,1,2,5,6,8,13,6*c+2];s=screen.screen([(-t,0)for t in T],(3,1));assert s['status']=='NOT_EXCLUDED';examples.append({'a':2,'b':1,'c':c,'complete_candidate_odd_levels':T,'retained_screen':s,'current_scope':'Cannot extend specified prefix by top-zero-port proof'if c==2 else'Not excluded by this particular top-zero-port proof; no completion supplied'})
result={'scope':__doc__,'minimum_first_R_heading':mn,'maximum_first_R_heading':mx,'top13_complete_choices':h13,'top12_complete_choices':v12,'all_E_T8_choices':v8,'physical_four_return':points,'exact_rank_skip':[0,2],'parity_passing_candidates':examples,'screen_source_sha256':hashlib.sha256((SRC/'screen.py').read_bytes()).hexdigest()}
(ROOT/'drift31_extreme_read_controls.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS author controls, not independent')
