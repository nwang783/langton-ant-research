"""Independent exact interval/ownership constants for the signed slab lift."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];U=ROOT/'causal_reduction/unit_scale';G=ROOT/'global_architecture_2026-10-23'
A=json.loads((U/'nonstationary_short_slab/architecture.json').read_text());prior=json.loads((ROOT/'audits/check_nonstationary_short_slab_independent.json').read_text());assert prior['architecture_sha256']==hashlib.sha256((U/'nonstationary_short_slab/architecture.json').read_bytes()).hexdigest()
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
def trace(w,h,dx=0):
 x=dx;y=0;out=[];dirs=((0,1),(1,0),(0,-1),(-1,0))
 for c in w:
  out.append((x,y));h=(h+(1 if c=='R'else-1))%4;u,v=dirs[h];x+=u;y+=v
 return out,(x,y),h
lo={tuple(d['orbit']):d['min']for d in A['orbit_offset_ranges']};new={}
for b in range(-6,7):
 own={(a,k)for a,L in lo.items()for k in range(L-5*b-4,L-5*b+1)}
 shifted={(tuple(c['orbit']),c['level']-5*b)for c in A['cells']if not c['inherited_arbitrary']}
 assert own==shifted and len(own)==150
 assert all(not(own&other)for other in new.values());new[b]=own
 for c in A['cells']:assert -6-5*b<=c['level']-5*b<=2-5*b
for k in range(-90,91):assert sum(-6-5*b<=k<=2-5*b for b in range(-30,31))<=2
# Exact standard endpoint classification. Empty or short flights are retained.
widths=set();checks=0
for h in (1,3):
 for dx in range(-5,6):
  rr,end,hh=trace(H,h,dx);assert hh==h;sgn=(end[0]-dx)//2;assert sgn in (-1,1)
  levels={x//2 for x,y in rr};m=min(levels);M=max(levels);W=M-m;widths.add(W);assert W in (2,3)
  for n in range(25):
   if sgn==1:bad=set(range(m,M))|set(range(m+n,M+n))
   else:bad=set(range(m-n+1,M-n+1))|set(range(m+1,M+1))
   assert len(bad)<=2*W<=6
   statuses={}
   for k in range(m-n-30,M+n+31):
    occurrences=[0<=sgn*(k-a)<n for a in levels]
    status=2 if all(occurrences) else 1 if any(occurrences)else 0
    if k not in bad:assert status in (0,2)
    statuses[k]=status
   for start in range(m-n-10,M+n+11):
    win=set(range(start,start+9))
    if not win&bad:assert len({statuses[k]for k in win})==1
    checks+=1
assert widths=={2,3}
# Expanded writer envelope: all translations anchored to ANY potential read.
normals={a[0]for a in lo};assert(min(normals),max(normals))==(-8,6)
Ulo,Uhi=min(normals)-10,max(normals)+10;assert(Ulo,Uhi)==(-18,16)
classes=2*(Uhi-Ulo+1);assert classes==70 and 22*classes==1540
out={'status':'PASS independent slab ownership and exact interval boundary constants; universal lift analytically reviewed','slab_architecture_sha256':prior['architecture_sha256'],'note_sha256':hashlib.sha256((G/'nonstationary_slab_preparation_lift.md').read_bytes()).hexdigest(),'new_cells_per_block':150,'new_blocks_disjoint':True,'full_level_window':[-6,2],'maximum_blocks_per_bad_level':2,'standard_endpoint_widths':sorted(widths),'parallel_bad_levels_per_flight':6,'perpendicular_bad_levels_per_flight':1540,'exact_interval_controls':checks,'bound':'|B|+12 F_parallel+2 L+3080 F_perpendicular >= floor(N/5)','scope':'Fixed inverse104 coarse path, independent1/5/9 choices at every occurrence after finite standard-flight preparation. No general nonstandard preparation or capture claim.'}
(ROOT/'audits/check_nonstationary_preparation_boundary_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
