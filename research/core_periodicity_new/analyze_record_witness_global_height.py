"""Discovery: check a band-model witness against a global residual-height bound."""
import json,sys,re
from pathlib import Path
L=json.load(open(sys.argv[1]));J=json.load(open(L['base_model_file']));assert J['format']=='guarded_reset_global_record_far_transverse_bands_v1';H=json.load(open(J['height_model_file']));B=json.load(open(J['base_model_file']));G=json.load(open(Path(B['resource_profile_file']).parent/'literal_residual_geometry.json'))['geometry'];near=len(B['poses']);phase=B['target_global_phase'];cut=H['lower_cutoff'];S=B['record_threshold'];I=B['initial_token_weight'];A=B['core_offsets'];T={(a,h):t for a,h,t in B['created_peaks']};F=(S-I-1)//2

def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(q):return sum(rot(q,phase))
def state(p):
 old=L['retained_old_positions'][p];z,c=J['position_map'][old]
 if z<near:
  x,y,h=B['poses'][z];return {'h':h,'lo':ht((x,y)),'hi':ht((x,y)),'pose':[x,y,h]}
 if z==J['geometric_initial_control']:return None
 k,h,q,b=J['far_controls'][z-near];return {'h':h,'lo':q,'hi':cut if q is None else q,'band':b}
rows=[]
for line in open(sys.argv[2]):
 if line.startswith('WITNESS '):p,col,a=map(int,line.split()[1:]);rows.append((state(p),col,a))
Q=F;report=[]
for i,(s,col,a)in enumerate(rows):
 if s is None:
  dest=rows[i+1][0];h=(dest['h']-G[a]['endpoint'][2])%4;lo=None;hi=(S-I-1)//2-max(ht(rot(q,h))for q in G[a]['inputs'])
 else:h=s['h'];lo=s['lo'];hi=s['hi']
 mi=max(ht(rot(q,h))for q in G[a]['inputs']);mo=max(ht(rot(q,h))for q in G[a]['outputs']);delta=ht(rot(G[a]['endpoint'][:2],h))
 if i+1<len(rows):
  dest=rows[i+1][0];assert dest['h']==(h+G[a]['endpoint'][2])%4
  if dest['lo']is not None:lo=dest['lo']-delta if lo is None else max(lo,dest['lo']-delta)
  hi=min(hi,dest['hi']-delta,(S-1-max(A[(h+phase)%4],T[a,(h+phase)%4]))//2)
 hi=min(hi,Q-mi);hi-=(hi-h)%2
 ok=lo is None or hi>=lo
 report.append(dict(step=i,packet=a,state=s,Q_before=Q,input_offset=mi,output_offset=mo,source_height_max=hi,lower=lo,possible=ok))
 if not ok:break
 Q=max(Q,hi+mo)
print(json.dumps({'initial_bound':F,'residual_max_bound_final':Q,'survives':all(r['possible']for r in report),'steps':report},indent=2))
