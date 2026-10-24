#!/usr/bin/env python3
from pathlib import Path
from itertools import product
from collections import defaultdict
import json
from frontier_drift_geometry import Geometry
from probe_diagonal_n_window import histories
from heavy_cycle_frontier import transition

def blankrow():return [histories((c+p)%2,0)[0] for c in range(4)]
def cell(p,inc,out):
 return next(h for h in histories(p,4) if h['ins'][inc]==3 and h['outs'][out]==3)
g=Geometry(4,0);empty=histories(0,0)[0]
# Fill both rows with one finite clockwise high-flow unit-face cycle.
r0=[cell(0,3,0),cell(1,2,3),empty,empty];r1=[cell(1,0,1),cell(0,1,2),empty,empty]
# Low ports outside this toy cycle need not match; the independent safe
# filter itself is called via a wrapper retaining only high-flow arcs.
class HighGeometry:
 def __init__(self,g,rows,p):self.g=g;self.rows=rows;self.p=p
 def splice_arcs(self,p):
  return [e for e in self.g.splice_arcs(p) if self.rows[e[0]][e[1]]['outs'][e[4]]==3 or self.rows[e[2]][e[3]]['ins'][e[4]]==3]
E=[empty]*4
s=transition((),E,r0,1,HighGeometry(g,(E,r0),1));assert s is not None
assert transition(s,r0,r1,0,HighGeometry(g,(r0,r1),0)) is None
# Essential zigzag high-flow cycle N,E,S,E repeated, full drift(+4,0).
points=[(0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(3,1),(3,0)];directions=[0,1,2,1,0,1,2,1];rr=[[None]*4 for _ in range(2)]
for i,(x,y) in enumerate(points):rr[y][x]=cell((x+y)%2,directions[i-1],directions[i])
s=transition((),E,rr[0],1,HighGeometry(g,(E,rr[0]),1));assert s is not None
s=transition(s,rr[0],rr[1],0,HighGeometry(g,rr,0));assert s is not None
r=dict(status='AUTHOR_HEAVY_CYCLE_FRONTIER_CONTROLS_PASS',contractible_unit_face_rejected=True,essential_full_drift_zigzag_retained=True,essential_state=s);Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
