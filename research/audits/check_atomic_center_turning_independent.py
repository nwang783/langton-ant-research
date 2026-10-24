from pathlib import Path
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
P=Path(__file__).resolve();B=ROOT/'core_periodicity_new/atomic_center_turning_frozen_20261023_1400';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_atomic_center_turning.json').read_text());C=raws[1][len(raws[0]):];words=dict(D=raws[0],V=raws[4],U=raws[7],C=C);corr=(-1-1j)/2
steps={};ends={}
for name,word in words.items():
 e,h,*_=walk(word);steps[name]=e+rotation(corr,h)-corr;ends[name]=(e,h)
 assert steps[name]=={'D':1+1j,'V':1+3j,'U':4j,'C':1+1j}[name]
 assert h==(3 if name=='C'else 0)
 a=J['atoms'][name];assert a['raw_word']==word and a['raw_endpoint']==[*xy(e),h]and a['center_step']==list(xy(steps[name]))
rows=[]
for a,u in steps.items():
 for b,v in steps.items():
  v=rotation(v,ends[a][1]);cross=int(u.real*v.imag-u.imag*v.real);dot=int(u.real*v.real+u.imag*v.imag)
  if a=='C':assert cross>0 and dot<=0 and cross>=-dot
  else:assert dot>0 and abs(cross)<=dot
  rows.append((a,b,xy(u),xy(v),cross,dot))
assert set(rows)=={(r['before'],r['after'],tuple(r['before_vector']),tuple(r['after_vector_in_before_frame']),r['cross_product'],r['dot_product'])for r in J['all_16_adjacent_atom_transitions']}
out=dict(status='PASS independent literal center correction and exact principal-turn branches',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),center_steps={a:xy(z)for a,z in steps.items()},adjacent_cases=rows,scope='Actual retained-factor atomic cuts. Principal turns telescope cyclically to pi*C/2 at full-pose closure; noC closure impossible by fixed forward cone. Simple closed polygon would force C4, already excluded. Thus any actual closed full-pose center polygon self-contacts. Auxiliary chord contact is NOT a microscopic collision or an exclusion of larger-C returns.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='adjacent_cases'})
