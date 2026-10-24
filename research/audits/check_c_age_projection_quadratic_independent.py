from pathlib import Path
import json,hashlib
B=Path('/workspace/shared/langton');F=B/'word_stabilization/dcuv_c_age_projection_quadratic_frozen_20261023_0754';M=json.loads((F/'manifest.json').read_text())
for z in M['files']:assert hashlib.sha256((F/z['file']).read_bytes()).hexdigest()==z['sha256']
G=json.loads((B/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];previous=json.loads((B/'audits/check_c_age_spatial_cubic_independent.json').read_text());rows=[]
for row in previous['rows']:
 g=G[row['packet']];p=0j;h=1j
 for c in g['word']:h*=(-1j if c=='R' else 1j);p+=h
 cc=row['C_count'];assert h==1j*(1j**cc);chosen=complex(*row['selected']);assert chosen.real+chosen.imag in(1,3)
 if cc==0:assert int(p.real+p.imag)=={0:2,4:4,7:4}[row['packet']]
 assert len(g['word'])<=28+15*cc
 rows.append(dict(packet=row['packet'],endpoint=[int(p.real),int(p.imag)],heading_real_imag=[int(h.real),int(h.imag)],chosen_projection=int(chosen.real+chosen.imag),length=len(g['word']),C_count=cc))
for j in range(101):
 low,high=-2*j-11,2*j+7
 assert [sum(v%2==parity for v in range(low,high+1))for parity in(0,1)]==[2*j+9,2*j+10]
# Identity: sum_{j=0}^k(2j+10)=k(k+1)+10(k+1)=(k+1)(k+10).
result=dict(status='PASS literal endpoints, projections and exact parity-interval count; analytic epoch review passed',rows=rows,epoch_packet_bound='(m-5)*(2*j+10)',duration_bound='28*(m-5)*(k+1)*(k+10)+15*k',manifest_sha256=hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),scope='Complete recurrent-eight factors only, necessary square-root C recurrence; no finite-C upper bound or capture.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
