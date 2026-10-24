from pathlib import Path
import json,hashlib,importlib.util
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';m=D/'ordered_W_marker_ownership_erratum_manifest.json';sha=hashlib.sha256(m.read_bytes()).hexdigest();assert sha=='506cb0d1771c0f0ce7317bbdab2a23d6463da8a3437f1995d18148838c6e9295'
j=json.loads(m.read_text())
for f,h in j['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in j['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
p=R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py';sp=importlib.util.spec_from_file_location('ownership',p);u=importlib.util.module_from_spec(sp);sp.loader.exec_module(u);rows=u.input_rows();assert len(rows)==23
chosen=[r for r in rows if r['ordered_W_choice']];assert len(chosen)==8
for r in chosen:
 if r['packet'] in ('V','VC'):assert r['context_tick0']==13 and r['owner_read_number1']==14
 else:assert r['owner_tick0']==1 and r['owner_read_number1']==2
for n,t in [('D',11),('U',29),('V',19)]:
 r=u.describe(n,t);assert r['owner']=='next actual word RAW' and r['next_word_tick0']==1 and r['next_word_read_number1']==2
out={'status':'PASS mandatory W marker physical-owner correction','manifest_sha256':sha,'canonical_ownership_utility_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'all_eight_chosen_inputs':chosen,'analytic':'The full before-color inputs and exact context ticks are unchanged. RAW length L owns ticks0..L-1; context tick L+1 is next actual word tick1, the SECOND read. D11, U29 and V19 therefore are not first physical reads. DC/UC/UCC/VCC own their corresponding first-C-tail tick1/read2. Residual remove/core absorption may precede the physical next-word read. This erratum changes owner prose, not literal chronology, C clock or the established matching/transport claims. Companion U-role erratum remains separately mandatory.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
