#!/usr/bin/env python3
"""Separate nonvacuous sector-correct positive control; old evidence unchanged.
Quarter rotation toggles the pose-sector sign. For SE104 translate the
rotated initial pose by(0,-1), so Geometry's incoming-axis convention holds.
"""
from pathlib import Path
from collections import defaultdict
import json
from frontier_drift_geometry import Geometry
from general_literal_window import bad_window as literal_bad
from general_first_return_window import bad_window as first_bad
D=((0,1),(1,0),(0,-1),(-1,0));root=Path(__file__).parent;word=(root.parent/'word_stabilization/standard_word.txt').read_text().strip();out=[]
for copies in(1,2,3):
 P=104*copies;a=2*copies
 for sign in(1,-1):
  b=sign*a;g=Geometry(a,b);p,h=((-1,0),0) if sign==1 else((0,0),1);start=p;hist=defaultdict(list)
  for t,ch in enumerate(word*copies):
   assert h%2==1-(sum(p)%2),(p,h)
   k=p[0]//a;q=p[0]-k*a,p[1]-k*b;hist[q].append((t-k*P,h,ch));h=(h+(1 if ch=='R' else-1))%4;dx,dy=D[h];p=p[0]+dx,p[1]+dy
  assert p==(start[0]+a,start[1]+b)
  lo=min(y-g.base[x] for x,y in hist);hi=max(y-g.base[x] for x,y in hist);rr=[];ts=[]
  for r in range(lo,hi+1):
   hh=[];tt=[]
   for c in range(a):
    es=sorted(hist[c,g.base[c]+r]);assert all(ch==('R' if j%2==0 else'L') for j,(t,h,ch) in enumerate(es))
    assert all(h%2==1-g.parity(r%2,c) for t,h,ch in es)
    hh.append(tuple(h for t,h,ch in es));tt.append(tuple(t for t,h,ch in es))
   rr.append(hh);ts.append(tt)
  windows=arcs=events=0;nonempty=0
  for k in(2,3,4):
   for z in range(len(rr)-k+1):
    hs=rr[z:z+k];times=ts[z:z+k];p=(lo+z)%2;matched=0
    assert literal_bad(hs,p,g) is None
    assert first_bad(hs,p,g) is None
    for r in range(k):
     for c,cc,d,seam,dr in g.arcs[(p+r)%2]:
      br=r+dr
      if not 0<=br<k:continue
      os=[j for j,h in enumerate(hs[r][c]) if(h+(1 if j%2==0 else-1))%4==d]
      ins=[j for j,h in enumerate(hs[br][cc]) if h==d];assert len(os)==len(ins)
      for j,l in zip(os,ins):assert times[br][cc][l]+seam*P==times[r][c][j]+1
      arcs+=bool(os);matched+=len(os)
    events+=matched;nonempty+=matched>0;windows+=1
  assert arcs>0 and events>0 and nonempty>0
  out.append(dict(period=P,full_drift=[a,b],start=start,incoming=0 if sign==1 else 1,windows=windows,nonempty_windows=nonempty,matched_nonempty_arcs=arcs,matched_event_successors=events,all_read_axes_checked=True,all_internal_successor_ordinals_and_times_checked=True,status='PASS'))
result=dict(status='AUTHOR_CORRECTED_NONVACUOUS_WINDOW_POSITIVES_PASS',scope=__doc__,controls=out);(root/'general_windows_positive_corrected.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
