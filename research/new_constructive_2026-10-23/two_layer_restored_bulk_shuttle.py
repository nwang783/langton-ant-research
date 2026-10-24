#!/usr/bin/env python3
"""One actual full-row out-and-back shuttle on the exact carried endpoint output.
All-parameter local endcap change; no renewable-controller claim.
"""
from pathlib import Path
import sys,json,time,hashlib
P=Path('/workspace/shared/langton');O=Path(__file__).parent
sys.path.insert(0,str(P/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
ctx=Context(max_operations=100000000);D=((0,1),(1,0),(0,-1),(-1,0));DOMAIN='r>=10 and k>=10'
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,n):return tuple(x*n for x in a)
def exp(v):return '('+'+'.join(f'{a}*{z}'for a,z in zip(v,('r','k','1')))+')'
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
source=O/'two_layer_carried_endpoint.json';J=json.loads(source.read_text());initial=ctx.set(J['returned_relation']);sample=(O/'two_layer_gap_frame_r10_k10.word.txt').read_text();E=sample[868:914];assert len(E)==46
stages=[('LRRL',(1,0,0),'east'),(E,(0,0,1),'remote_cap'),('LRRL',(1,0,0),'west'),('RRRRLL',(0,0,1),'local_cap')]
assert ''.join(w*(10*a+10*b+c)for w,(a,b,c),_ in stages)==sample[828:960]
p=((0,0,0),(0,0,2));h=1;tm=(0,0,0);F=[];manifest=[];mass=(0,0,0)
for w,count,label in stages:
 start=p;hs=h;local=(0,0);rr=[]
 for i,ch in enumerate(w):
  rr.append((local,ch));h=(h+(1 if ch=='R'else-1))%4;v=D[h];local=local[0]+v[0],local[1]+v[1]
 repeated=count!=(0,0,1)
 if repeated:assert h==hs and local!=(0,0)
 manifest.append(dict(label=label,word=w,count=count,start=start,heading=hs,time=tm,drift=local))
 for i,(off,ch) in enumerate(rr):
  v=tuple(plus(start[a],(0,0,off[a]))for a in(0,1))
  if repeated:
   bound=f'0<=i<{exp(count)}';dom=DOMAIN+' and exists(i:'+bound+f' and x={exp(v[0])}+{local[0]}*i and y={exp(v[1])}+{local[1]}*i)'
   axis=0 if local[0]else 1;assert len(w)%local[axis]==0;sc=len(w)//local[axis]
   tf=(tm[0]-sc*v[axis][0],tm[1]-sc*v[axis][1],sc if axis==0 else 0,sc if axis==1 else 0,tm[2]+i-sc*v[axis][2])
  else:dom=DOMAIN+f' and x={exp(v[0])} and y={exp(v[1])}';tf=(tm[0],tm[1],0,0,tm[2]+i)
  F.append(dict(stage=label,slot=i,turn=ch,domain=ctx.set('[r,k]->{[x,y]:'+dom+'}'),time=tf))
 p=tuple(plus(start[a],mul(count,local[a]))for a in(0,1));tm=plus(tm,mul(count,len(w)));mass=plus(mass,mul(count,w.count('R')-w.count('L')))
assert p==((0,0,0),(0,0,2)) and h==1 and tm==(8,0,52) and mass==(0,0,12)
fail=[];pairs=nonempty=0
for i,f in enumerate(F):
 ctx.reset_operations();current=initial.intersect(f['domain'])
 for j,g in enumerate(F):
  if i==j:continue
  pairs+=1;z=f['domain'].intersect(g['domain'])
  if z.is_empty():continue
  dt=tuple(g['time'][a]-f['time'][a]for a in range(5));ineq='+'.join(f'{a}*{b}'for a,b in zip(dt,('r','k','x','y','1')))+'<0';prior=z.intersect(ctx.set('[r,k]->{[x,y]:'+ineq+'}'))
  if not prior.is_empty():current=xor(current,prior);nonempty+=1
 bad=f['domain'].subtract(current)if f['turn']=='L'else current
 if not bad.is_empty():fail.append(dict(family=i,stage=f['stage'],slot=f['slot'],bad=str(bad.coalesce())));break
returned=initial;change=ctx.set('[r,k]->{[x,y]:false}')
if not fail:
 for f in F:change=xor(change,f['domain'])
 returned=xor(initial,change)
# Two fixed-size affine endcap boxes, not an omitted region.
capbox=ctx.set('[r,k]->{[x,y]:'+DOMAIN+' and ((-3<=x<=3 and 0<=y<=6) or (2r-3<=x<=2r+5 and 0<=y<=6))}')
assert not fail and change.subtract(capbox).is_empty()
left={(0,3),(0,4),(-1,4),(-1,2)}
right={(-1,1),(0,1),(1,1),(2,1),(3,2),(3,3),(0,3),(1,3),(-1,4),(0,4),(1,4),(2,4),(0,5),(1,5)}
cleared_left={(-1,2)};cleared_right={(0,1),(1,1)}
def finite_caps(L,R):
 clauses=[f'(x={x} and y={y})'for x,y in L]+[f'(x=2r+{x} and y={y})'for x,y in R]
 return ctx.set('[r,k]->{[x,y]:'+DOMAIN+' and ('+' or '.join(clauses)+')}')
assert change.is_equal(finite_caps(left,right))
assert initial.intersect(change).is_equal(finite_caps(cleared_left,cleared_right))
# Same shuttle cannot be repeated immediately: its second read wants R at
# (0,3), but this first shuttle has just added that black cell.
assert returned.intersect(finite_caps({(0,3)},set())).is_equal(finite_caps({(0,3)},set()))
report=dict(status='AUTHOR EXACT ALL-r,k RESTORED-BULK SHUTTLE',domain=DOMAIN,source_manifest_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),initial='COMPLETE returned_relation of two_layer_carried_endpoint.json',endpoint=[[0,2],1],duration_coefficients=tm,mass_delta_coefficients=mass,families=len(F),ordered_pairs=pairs,nonempty_prior_relations=nonempty,failures=fail,stages=manifest,complete_change_relation=str(change),complete_returned_relation=str(returned),all_changes_within_two_fixed_size_affine_endcap_boxes=True,cleared_left=sorted(cleared_left),cleared_right_relative_2r=sorted(cleared_right),added_left=sorted(left-cleared_left),added_right_relative_2r=sorted(right-cleared_right),immediate_same_shuttle_failure='second read (0,3), R required, current black from this shuttle',endcap_box_relation=str(capbox),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope=__doc__)
(O/'two_layer_restored_bulk_shuttle.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k not in('stages','complete_returned_relation')},indent=2))
