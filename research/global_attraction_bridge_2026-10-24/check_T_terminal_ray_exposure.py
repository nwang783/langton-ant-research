"""Whole-future ray exposure of two signed/frozen terminal comparisons; no new kernel search."""
from pathlib import Path
import json,hashlib
from certified_comparison_perturbation import geometry,reference,perturbation_event
from check_return_permanent_output_debt import DXY,future
P=Path(__file__).parent;J=json.loads((P/'T_PORT7_ABSORBER_CHECKED.json').read_text());T=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());W=R['W'];K=set(map(tuple,R['canonical_source']))
def exposure(word,tail):
 reads,_,p,h=geometry((0,0),0,word);Q,_,end,eh=geometry(p,h,tail);d=(end[0]-p[0],end[1]-p[1]);first={};rays=[]
 for i,(x,y)in enumerate(reads):
  if x==y and x>=0 and x%2==0:first.setdefault(x//2,i)
 for i,(x,y)in enumerate(Q):
  solutions=[]
  if d[0]+d[1]==0:
   if(x+y)%4==0:
    a=(x+y)//4
    if a>=0 and(2*a-x)%d[0]==0:
     k=(2*a-x)//d[0]
     if k>=0 and y+k*d[1]==2*a:solutions.append((a,k))
  else:assert x!=y # The parallel SW tail is transversely disjoint from this ray.
  for a,k in solutions:first[a]=min(first.get(a,10**99),len(word)+104*k+i)
  rays.append(dict(phase=i,point=(x,y),solutions=solutions))
 return dict(first_reads=sorted(first.items()),tail_ray_tests=rays,drift=d)
eT=exposure(T['T_recovery'],T['T_tail_word']);e7=exposure(J['word'],J['tail_word']);assert list(a for a,t in eT['first_reads'])==list(range(10));assert list(a for a,t in e7['first_reads'])==list(range(19));q=(202,201)
ref=reference(set(map(tuple,J['kernel'])),(0,0),0,J['word'],J['tail_word']);event=perturbation_event(ref,{(20,20),(22,22)});assert event['time']==18600 and event['cell']==(22,22)and event['remaining_original_extra']==[(20,20)]
seed=K|{(q[0]+2*a,q[1]+2*a)for a in[0,1,3,5,6,7,10,11]};B={r:-i-1 for i,r in enumerate(sorted(seed))};p=(0,0);h=1;first={};death={};prefix=W*100+W[:13]+J['word'][:18600]+'L';near=(q[0]+20,q[1]+20);far=(q[0]+22,q[1]+22);near_id=B[near];far_id=B[far]
for t,c in enumerate(prefix):
 first.setdefault(p,t);old=B.pop(p,None);assert(c=='L')==(old is not None)
 if old is None:B[p]=t;h=(h+1)%4
 else:death[old]=t;h=(h-1)%4
 p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
assert first[far]==10413+18600 and near not in first and B[near]==near_id and death[far_id]==10413+18600
# Exact arbitrary far-input tests; the universal threshold follows the complete exposure table.
far_indices=[19,20,100,10**6,10**9];safe=perturbation_event(ref,{(2*a,2*a)for a in far_indices});assert safe['kind']=='CERTIFIED unchanged complete future'
sourcefiles=['T_PORT7_ABSORBER_MANIFEST.json','LAST_M_REGISTER_SCATTERING_MANIFEST.json','SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','certified_comparison_perturbation.py','check_return_permanent_output_debt.py']
out=dict(status='AUTHOR exact exposure addendum; independent audit pending',scope='Complete reference read-footprints and first extra collision; no universal closure after the skipped-nearer-bit collision.',dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in sourcefiles},T=eT,T7=e7,chronological_T7_extra_ports=sorted((t,a)for a,t in e7['first_reads']if a>=8),safe_far_indices=far_indices,nearer_bit_skipping_control=dict(seed=sorted(seed),physical_reads=len(prefix),far_cell=far,far_consumption=death[far_id],near_cell=near,near_original_id=near_id,near_first_read=None,whole_post_collision_black=[[r,i]for r,i in sorted(B.items())],post_collision_pose=[p,h],exact_reference_event={k:v for k,v in event.items()if k!='new_full_field_terms'}))
(P/'T_TERMINAL_RAY_EXPOSURE_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print('T ray0..9; T7 ray0..18; literal21-cell source skips nearer10 and consumes11 at',10413+18600,flush=True)
