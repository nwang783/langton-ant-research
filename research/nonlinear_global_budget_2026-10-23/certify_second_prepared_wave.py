#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict,Counter
import runpy,json,hashlib,time
ROOT=Path(__file__).parent;C=runpy.run_path(str(ROOT/'certify_prepared_travelling_wave.py'));E=C['E'];A=json.loads((ROOT/'second_prepared_wave_input.json').read_text());J=json.loads((ROOT/'second_prepared_wave_probe.json').read_text());rows={tuple(j):[0]for j in A['profiles']};cap={tuple(q)for q in A['cap']};rows,F,p,h,tau,phi=E['incoming'](rows,cap,(20,1));first=[list(p),h];p,h,Q=E['advance'](rows,F,p,h,6820);assert[list(p),h]==J['pose'];word=J['word'];cert=C['cert_parallel'](rows,F,p,h,word);assert cert;V=E['V'];slots=[];pp=p;hh=h;reps={};start=time.time()
for i,ch in enumerate(word):
 assert ('L'if E['initial_color'](pp,rows,F)else'R')==ch
 E['toggle'](F,pp);slots.append((pp,i,ch));reps.setdefault((pp[0]-pp[1],pp[0]%26),pp);hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
# Recover exact boundary F for independent far-flip controls.
rows,F,p,h,tau,phi=E['incoming']({tuple(j):[0]for j in A['profiles']},cap,(20,1));p,h,Q=E['advance'](rows,F,p,h,6820);rejected=0
for q in reps.values():
 far=(q[0]+26000000,q[1]+26000000);bad=set(F);E['toggle'](bad,far);assert C['cert_parallel'](rows,bad,p,h,word)is None;rejected+=1
report={'scope':'Complete inherited infinite prepared72-profile4352-wave, not finite-original reachability.','source_hash':A['state_sha256'],'channel':[20,1],'first_contact_pose':first,'first_contact_H_index':tau,'wave_entry':6820,'wave_pose':[list(p),h],'finite_XOR_mass':len(F),'finite_XOR_sha256':hashlib.sha256(json.dumps(sorted(F),separators=(',',':')).encode()).hexdigest(),'word_sha256':J['word_sha256'],'word':word,'certificate':cert,'bad10_per_period':J['bad10_per_period'],'K_per_period':J['K_per_period'],'far_flip_rejections':rejected,'elapsed_seconds':time.time()-start};(ROOT/'second_prepared_wave_certificate.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k!='word'},indent=2))
