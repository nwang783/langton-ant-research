"""Exact inventory and finite inductive pose-set checks, no OUT or search trust."""
from pathlib import Path
import json,hashlib
from check_dcuv_producer_model_independent import geometry,rotation,xy,walk,raws,ordinary,protected,ROOT,digest
from check_dcuv_patch_model_independent import validate_profile
D=ROOT/'core_periodicity_new/chronology_dcuv/record_head_offset_search';gp=D/'geometry_probe.json';G=json.loads(gp.read_text());ip=Path(G['inventory_file']);assert digest(ip)==G['inventory_sha256'];J=json.loads(ip.read_text());keep=validate_profile(J);pp=Path(J['potential_file']);assert digest(pp)==J['potential_sha256'];W=json.loads(pp.read_text());v=W['values'];assert W['profile_sha256']==J['resource_profile_sha256'];L=lambda z:int(z.real*v['ax']+z.imag*v['ay']);A=lambda h:L(rotation(-1+1j,h))+v[f'c{h%4}'];ends=[walk(w)[:2]for w in raws]
def T(a,h):
 h%=4;p,dh=ends[a];return max([2*L(rotation(p,h))+A(h+dh)]+[2*L(rotation(q,h))+v[f'w_{a}_{i}_{h}']for i,q in enumerate(geometry[a]['outputs'])])
assert J['direction']==[v['ax'],v['ay']]and J['core_offsets']==[A(h)for h in range(4)]
assert J['created_peaks']==[[a,h,T(a,h)]for a in keep for h in range(4)]
assert J['event_types_phases']==[[b,h,T(b,h),A(h)]for b in keep for h in range(4)if T(b,h)>A(h)]
assert J['initial_token_weight']==max(T(b,h)-2*L(rotation(z,h))for b in keep for h in range(4)for z in geometry[b]['inputs'])
rows=set();counts=dict(sector_alignments=0,ordinary_excluded=0,protected_excluded=0,nonrecord_target=0,source_peak_blocks=0)
for a in keep:
 for q in geometry[a]['outputs']:
  for b in keep:
   for z in geometry[b]['inputs']:
    for h in range(4):
     p=q-rotation(z,h);r=(a,b,*xy(p),h,*xy(q))
     if(sum(xy(p))+h)%2:continue
     for phase in range(4):
      counts['sector_alignments']+=1
      if r[:5]in ordinary:counts['ordinary_excluded']+=1;continue
      if r in protected:counts['protected_excluded']+=1;continue
      bh=(h+phase)%4
      if T(b,bh)<=A(bh):counts['nonrecord_target']+=1;continue
      threshold=2*L(rotation(p,phase))+T(b,bh)
      if max(A(phase),T(a,phase))>=threshold:counts['source_peak_blocks']+=1;continue
      rows.add((*r,phase,threshold))
assert rows==set(map(tuple,J['rows']))and counts==J['counts']and len(rows)==J['remaining_count']==1651
assert len(G['results'])==len(J['rows']);checked=[];options=0
for rec in G['results']:
 assert rec['row']==J['rows'][rec['index']-1]
 if rec['status']!='EXHAUSTED_NO_HIT':continue
 a0,b,tx,ty,th,qx,qy,phase,threshold=rec['row'];goal=complex(tx,ty);q=complex(qx,qy);S=set(map(tuple,rec['closed_pose_set']));assert len(S)==rec['states'];e,dh=ends[a0];assert(*xy(e),dh)in S and(tx,ty,th)not in S
 for x,y,h in S:
  p=complex(x,y);height=2*L(rotation(p,phase));qq=rotation(q-p,-h)
  if height+A(h+phase)>=threshold:continue
  for a in keep:
   if qq in geometry[a]['context']or height+T(a,h+phase)>=threshold:continue
   left=(a0,a,x,y,h,qx,qy);rel=rotation(goal-p,-h);right=(a,b,*xy(rel),(th-h)%4,*xy(qq))
   if left[:5]in ordinary or left in protected or right[:5]in ordinary or right in protected:continue
   e,dh=ends[a];dest=p+rotation(e,h);assert(*xy(dest),(h+dh)%4)in S,(rec['index'],(x,y,h),a);options+=1
 checked.append(dict(index=rec['index'],row=rec['row'],closed_states=len(S)))
assert len(checked)==181
out=dict(status='PASS exact1651-event inventory and181 conditional finite pose closures',direction=J['direction'],initial_token_weight=J['initial_token_weight'],events=len(rows),closed_events=len(checked),largest_closed_pose_set=max(z['closed_states']for z in checked),checked_transitions=options,closed=checked,scope='Specified canonical fixed-weight strict historical-record events only. No unconditional transfer exclusion and no full record-family closure.',hashes={str(p.relative_to(ROOT)):digest(p)for p in[gp,ip,pp,Path(__file__)]})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('closed','hashes')})
