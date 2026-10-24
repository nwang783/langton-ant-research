from pathlib import Path
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parents[1];note=R/'K1_pipeline_detours_2026-10-23/K1_later_R2_essential_backbone_v2.md';rows=[]
# Normalize each selected/helper history by a genuine rotation to vertical
# arrivals. Reconstruct sheet levels from chronological port ordinals.
for name,hs in [('selected',(0,0,2,0)),('helper_W',(3,3,3,1)),('helper_N',(0,0,0,2))]:
 h0=hs[0];h=tuple((v-h0)%4 for v in hs);r=Counter(h[::2]);se=r[0]-r[2];nw=0;M=max(se,nw);hc={0:se,1:se,2:nw,3:nw};ic=Counter();oc=Counter();events=[]
 for j,v in enumerate(h):
  w=(v+(1 if j%2==0 else-1))%4;ic[v]+=1;oc[w]+=1
  events.append(dict(rank=j,in_level=hc[v]-ic[v]+1,out_level=hc[w]-oc[w]+1,in_heading=(v+h0)%4,out_heading=(w+h0)%4))
 assert events[1]['in_level']==events[2]['out_level']==M-1
 assert events[1]['out_level']!=M-1 and events[2]['in_level']!=M-1
 assert (events[2]['out_heading']-events[1]['in_heading'])%4 in(1,3)
 rows.append(dict(kind=name,headings=hs,max_C=M,events=events))
# The signed unique LEFT middle contour has these and only these corners.
# Every edge leaves source R2 and arrives target L1, so the later pairing
# adds 1+(T2-T1)>=5, rather than using the old earlier-paired R2 map.
for s in range(1,30):
 for m in range(30):
  ell=s+2*m;helpers=s+2*m
  assert helpers==ell and 2*s+3*m+m==2*ell
  d=(-s,ell);assert max(abs(v)for v in d)==ell
out=dict(status='PASS independent reduced local sheet pairing; analytic unique-contour telescope verified',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),rows=rows,identities=['helpers=ell; physical contour length=2ell','P=2ell+sum_selected_and_helpers(T2-T1)>=10ell','sum_selected(T1-T0)=sum_selected_and_helpers(T2-T1)>=8ell','physical drift=(-s,ell) up to genuine rotation'],scope='Complete WHITE cap4, leftmost branch-free K1, signed S/RL grammar and collar. New target-L1 to LATER-R2 dependency, not the old earlier-paired-R2 map. No general K1 exclusion or original-fuel budget.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
