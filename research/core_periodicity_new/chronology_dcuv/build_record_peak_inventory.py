"""Exact finite inventory for the historical-record event route; no no-hit claim."""
from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from resource_profile import load_profile
profile,potential,out=map(Path,sys.argv[1:4]);P,D,M=load_profile(profile);J=json.loads(potential.read_text());assert J['profile_sha256']==M['resource_profile_sha256'];v=J['values'];G=D['geometry']['geometry'];keep=P['keep'];F=D['ordinary'];FP=D['protected'];direction=(v['ax'],v['ay'])
def rot(q,h):x,y=q;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(q):return sum(a*b for a,b in zip(direction,q))
def A(h):return L(rot((-1,1),h))+v[f'c{h%4}']
def T(a,h):
 g=G[a];e=g['endpoint'];return max([2*L(rot(e[:2],h))+A(h+e[2])]+[2*L(rot(q,h))+v[f'w_{a}_{i}_{h%4}']for i,q in enumerate(g['outputs'])])
peaks={(a,h):T(a,h)for a in keep for h in range(4)};events=[];rows=[];counts={'sector_alignments':0,'ordinary_excluded':0,'protected_excluded':0,'nonrecord_target':0,'source_peak_blocks':0}
for b in keep:
 for bh in range(4):
  if T(b,bh)>A(bh):events.append([b,bh,T(b,bh),A(bh)])
for a in keep:
 for q in G[a]['outputs']:
  for b in keep:
   for z in G[b]['inputs']:
    for rh in range(4):
     rz=rot(z,rh);p=(q[0]-rz[0],q[1]-rz[1]);r=(a,b,*p,rh,*q)
     if (sum(p)+rh)%2:continue
     for phase in range(4):
      counts['sector_alignments']+=1
      if r[:5]in F:counts['ordinary_excluded']+=1;continue
      if r in FP:counts['protected_excluded']+=1;continue
      bh=(rh+phase)%4
      if T(b,bh)<=A(bh):counts['nonrecord_target']+=1;continue
      threshold=2*L(rot(p,phase))+T(b,bh)
      if max(A(phase),T(a,phase))>=threshold:counts['source_peak_blocks']+=1;continue
      rows.append([*r,phase,threshold])
rows=sorted(set(map(tuple,rows)));I=max(T(b,h)-2*L(rot(q,h))for b in keep for h in range(4)for q in G[b]['inputs']);obj={**M,'potential_file':str(potential.resolve()),'potential_sha256':hashlib.sha256(potential.read_bytes()).hexdigest(),'direction':direction,'core_offsets':[A(h)for h in range(4)],'created_peaks':[[a,h,t]for (a,h),t in peaks.items()],'event_types_phases':events,'initial_token_weight':I,'counts':counts,'remaining_count':len(rows),'rows':rows,'row_format':['source','target','x','y','relative_heading','qx','qy','source_global_phase','record_threshold'],'status':'Exact algebraic inventory, not no-hit exclusions'}
out.with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');out.with_suffix('.tsv').write_text(''.join(' '.join(map(str,r))+'\n'for r in rows));print(json.dumps({k:obj[k]for k in ['core_offsets','event_types_phases','initial_token_weight','counts','remaining_count']}))
