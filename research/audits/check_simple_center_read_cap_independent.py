from pathlib import Path
from collections import Counter,defaultdict
import json,hashlib
P=Path(__file__).resolve();ROOT=P.parents[1];B=ROOT/'core_periodicity_new/simple_center_read_cap_frozen_20261023_1612';M=json.loads((B/'manifest.json').read_text())
for x in M['files']:assert hashlib.sha256((B/x['frozen']).read_bytes()).hexdigest()==x['sha256']
G=json.loads((B/'03_literal_residual_geometry.json').read_text())['geometry'];words={a:G[i]['word']for a,i in [('D',0),('V',4),('U',7)]};words['C']=G[1]['word'][len(words['D']):];V=(1j,1,-1j,-1)
def reads(w):
 p=0j;h=0;out=[]
 for c in w:out.append(p);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 return Counter(out),(p,h)
centers=defaultdict(list)
for a,w in words.items():
 count,end=reads(w)
 for z,m in count.items():
  for h in range(4):
   c=(-1j)**h*(-1-1j-2*z);centers[(int(c.real),int(c.imag))].append((a,h,(int(z.real),int(z.imag)),m))
weights={c:max(z[3]for z in v)for c,v in centers.items()};spectrum=Counter(weights.values());assert len(weights)==60 and spectrum=={1:28,2:20,3:12}and sum(weights.values())==104
marker=G[0]['marker'];mc,_=reads(marker);assert len(marker)==11 and max(mc.values())==2
A=json.loads((B/'02_simple_center_physical_read_cap.json').read_text())
out=dict(status='PASS independent literal footprint cap conditional on distinct atomic entry centers',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),raw_lengths={k:len(v)for k,v in words.items()},possible_entry_centers=60,multiplicity_spectrum=dict(spectrum),raw_read_cap=104,terminal_marker_extra=2,weights=[[*c,w]for c,w in sorted(weights.items())],scope='Pure footprint consequence of corrected-center injectivity; no assertion that arbitrary ant paths have this property, no optimality, beta, lifetime, duration or capture claim.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='weights'})
