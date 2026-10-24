"""Discovery CEGAR by exact high-height resources, never excluding a physical path.
CLI FULL_PETRI.json OUTDIR LIMIT. Missing heights are unlimited until selected.
"""
from pathlib import Path
import json,sys,subprocess
src,directory=map(Path,sys.argv[1:3]);limit=int(sys.argv[3]);directory.mkdir(exist_ok=True);J=json.loads(src.read_text());selected={h for _,r in J['goal_requirements'] for h,x in zip(J['places'],r)if x};summ=[]
for rnd in range(len(J['places'])+1):
 p=directory/f'round{rnd:02d}';subprocess.run([sys.executable,'project_record_height_petri.py',str(src),str(p),','.join(map(str,sorted(selected)))],check=True)
 with p.with_suffix('.txt').open('w')as fo,p.with_suffix('.log').open('w')as fe:subprocess.run(['./record_height_petri_backward',str(p.with_suffix('.dat')),str(limit),str(p.with_suffix('.basis'))],stdout=fo,stderr=fe,check=True)
 lines=p.with_suffix('.txt').read_text().splitlines();rec={'round':rnd,'selected_heights':sorted(selected),'status':lines[0],'prefix':str(p)};summ.append(rec)
 if not lines[0].startswith('status PETRI_WITNESS'):break
 C=[0]*len(J['places']);miss=None;path=[]
 for line in lines:
  if not line.startswith('EDGE '):continue
  ei=int(line.split()[1]);fr,to,a,ins,outs=J['transitions'][ei];deficit={h:i-c for h,i,c in zip(J['places'],ins,C)if i>c};path.append({'edge':ei,'packet':a,'deficit':deficit})
  if deficit and miss is None:miss=set(deficit)
  C=[c-i+o for c,i,o in zip(C,ins,outs)]
 rec['first_missing_heights']=sorted(miss or[]);rec['path']=path
 if miss is None:rec['status']='EXACT_PETRI_WITNESS';break
 assert not(miss&selected),(miss,selected)
 selected|=miss
 (directory/'summary.json').write_text(json.dumps(summ,indent=2)+'\n')
(directory/'summary.json').write_text(json.dumps(summ,indent=2)+'\n');print(json.dumps([{k:v for k,v in r.items()if k!='path'}for r in summ],indent=2))
