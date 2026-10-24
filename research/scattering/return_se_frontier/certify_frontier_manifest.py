"""Regression bindings for the stated 22-class scope; not a replacement replay."""
import json,sys,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import W,plan

def main():
 I=json.loads((HERE/'strip_interface.json').read_text());phases=I['fresh_phases']
 immediate=json.loads((HERE/'mass5_interfaces.json').read_text())['excluded_phases'];scars=[r['phase'] for r in json.loads((HERE/'localized_scars_certificate.json').read_text())['rows']]
 opposite=[15,45,72];displaced=[28,60,61,70,75]
 assert len(immediate+scars+opposite+displaced)==22 and sorted(immediate+scars+opposite+displaced)==phases
 files=['strip_interface.json','parallel_model_certificate.json','mass5_interfaces.json','localized_scars_certificate.json']
 for r in opposite:
  f=f'full_opposite_certificate_r{r}.json';x=json.loads((HERE/f).read_text());assert x['phase']==r and x['remote_c_never_read'] and x['tail_phase']==0
  assert x['total_capture_time']=={15:[312,728,412568],45:[312,728,412512],72:[312,624,399373]}[r]
  assert x['total_capture_pose']=={15:[[[-2,-2,-636],[2,2,696]],0],45:[[[-2,-2,-642],[2,2,702]],0],72:[[[-2,0,-321],[2,0,238]],3]}[r]
  b=f'full_opposite_bindings_r{r}.json';y=json.loads((HERE/b).read_text());assert y['phase']==r and y['first_d_phase']==72 and y['first_d_read_source_time']==[0,104,{15:34827,45:33523,72:72247}[r]];files.extend([f,b])
 for r in displaced:
  f=f'displaced_se_certificate_r{r}.json';x=json.loads((HERE/f).read_text());assert x['phase']==r
  assert x['full_prefix_read_upper']=={'u':{28:78,60:78,61:106,70:58,75:58}[r],'z':71}
  if r in (28,60):assert x['archive_u_upper']==78 and x['forced_c_x_offset']=={28:-40,60:-52}[r]
  else:assert x['all_future_read_upper']==x['full_prefix_read_upper']
  files.append(f)
 for r in (28,60):
  f=f'displaced_se_cycle_certificate_r{r}.json';x=json.loads((HERE/f).read_text());assert x['phase']==r and x['remote_d_never_read'] and x['first_c_phase']==72 and x['tail_phase']==0
  assert x['total_capture_time']=={28:[624,624,376449],60:[728,728,356785]}[r]
  assert x['total_capture_pose']=={28:[[[0,0,23],[0,0,38]],1],60:[[[-2,-2,-465],[2,2,404]],3]}[r]
  files.append(f)
 reads,_,_,_=plan(W,(0,0),2);bases=[(-62+reads[r][0],2+reads[r][1]) for r in phases]
 assert {(x+y,x%2) for x,y in bases}=={(z,p) for z in range(-63,-52) for p in (0,1)}
 assert min(x-y for x,y in bases)==-61
 out=dict(status='all 22 exact certificate families independently audited',domain='each fixed m>=100, all sufficiently large n; family-specific uniform cones as certified',band_z=[-63,-53],sufficient_global_u_upper=-461,classes=dict(immediate=immediate,localized_scars=scars,opposite_NE=opposite,displaced_SE=displaced),certificate_sha256={f:hashlib.sha256((HERE/f).read_bytes()).hexdigest() for f in files},scope='Excluded under the established recurrent mass-five incidence hypotheses. Not an arbitrary finite-seed theorem.')
 (HERE/'frontier_manifest.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
