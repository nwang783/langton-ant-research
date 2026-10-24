"""Exact 22-class scope/output bindings; this is not a replacement proof replay."""
import sys,json,hashlib,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import W,plan
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
lin=lambda n,m,c:[n+m,n,200*n+100*m+c]

def main():
 I=json.loads((HERE/'strip_interface.json').read_text());phases=I['fresh_phases'];striphash=H(HERE/'strip_interface.json')
 assert I['pre_core_read_upper']=={'u_minus_4n':98,'z':71} and I['strip_u']==[-200,200]
 model=json.loads((HERE/'parallel_model_certificate.json').read_text());assert model['strip_interface_sha256']==striphash
 rows={r['phase']:r for r in model['records']};assert len(rows)==len(model['records'])==22 and sorted(rows)==phases
 immediate=[15,29,32,45,47,55,56,57,62,71,72]
 assert [r['phase'] for r in model['records'] if r['finite_history_transfer']=='permanent']==immediate
 for r in immediate:
  x=rows[r];assert x['finite_history_transfer']=='permanent' and x['drift'] in ([-2,-2],[2,2])
  assert -200<=x['tail_source_u_bounds'][0]<=x['tail_source_u_bounds'][1]<=200
 scar=json.loads((HERE/'localized_scars_certificate.json').read_text());assert scar['strip_interface_sha256']==striphash
 scars=[r['phase'] for r in scar['rows']];assert scars==[13,14,27,89]
 for x in scar['rows']:
  assert x['time_delay']=={13:20,14:120,27:132,89:32}[x['phase']]
  assert x['local_checkpoint']==rows[x['phase']]['local_capture'] and x['join_before_segment12']
 returns=[28,38,46,60,61,70,75]
 assert sorted(immediate+scars+returns)==phases and len(immediate+scars+returns)==22
 expected={
 28:((728,0,203308),(( -2,0,-32),(2,0,72)),0,100,77),
 38:((728,0,202712),(( -2,0,-32),(2,0,72)),0,100,71),
 46:((728,208,264506),((2,0,7),(-2,0,-45)),2,100,79),
 60:((728,0,210340),(( -2,0,-32),(2,0,72)),0,100,97),
 61:((624,104,226676),((0,-2,52),(0,2,62)),0,0,123),
 70:((728,0,213872),((-2,0,-66),(2,0,0)),0,99,89),
 75:((728,0,200172),((-2,0,-32),(2,0,72)),0,100,81)}
 files=['strip_interface.json','parallel_model_certificate.json','localized_scars_certificate.json','finite_parent_controls.json']
 for r in returns:
  f=f'full_return_certificate_r{r}.json';x=json.loads((HERE/f).read_text());t,p,h,phase,z=expected[r]
  assert x['phase']==r and x['remote_d_never_read']
  assert x['total_capture_time']==lin(*t) and x['total_capture_pose']==[[lin(*q) for q in p],h]
  assert x['tail_phase']==phase and x['all_future_z_upper']==z
  assert x['template_sha256']==H(HERE/f'full_return_template_r{r}.json')
  template=json.loads((HERE/f'full_return_template_r{r}.json').read_text());word=template['infinite_tail_word']
  modelword=gzip.open(HERE/f'word_r{r}_mature1.txt.gz','rt').read()
  assert word==W[phase:]+W[:phase] and hashlib.sha256(modelword.encode()).hexdigest()==rows[r]['word_sha256']
  assert modelword.startswith(template['segments'][0]['word'])
  files.append(f)
 controls=json.loads((HERE/'finite_parent_controls.json').read_text());assert len(controls)==44
 assert {(x['r'],x['m'],x['n']) for x in controls}=={(r,m,n) for r in phases for m,n in [(100,400),(101,401)]}
 assert all(x['all_local_reads_match'] for x in controls)
 assert all(x['complete_finite_tail'] is not None for x in controls if x['r'] in immediate)
 reads,_,_,_=plan(W,(0,0),0);bases=[(37+reads[r][0],25+reads[r][1]) for r in phases]
 assert {(x+y,x%2) for x,y in bases}=={(z,p) for z in range(55,66) for p in (0,1)}
 assert min(x-y for x,y in bases)==2 and max(x-y for x,y in bases)==9
 out=dict(status='all 22 complete finite-five-cell exact certificate families passed; independent audit pending',domain='m>=100,n-m>=100',band_z=[55,65],sufficient_global_u_upper=-461,classes=dict(permanent_strip=immediate,localized_scars=scars,complete_history_returns=returns),certificate_sha256={f:H(HERE/f) for f in files},scope='Complete five-cell family captures. Its recurrence consequence uses the previously established incidence and fixed-site pristine-band lemmas, not arbitrary finite-core stability.')
 (HERE/'frontier_manifest.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
