from pathlib import Path
import subprocess,json
P=Path(__file__).resolve().parent.parent;D=P/'chronology_dcuv';rows=[tuple(map(int,l.split()))for l in(D/'hypothesis_U_upper3.tsv').read_text().splitlines()];rows=[r for r in rows if r[:2]==(0,7)]
for i,r in enumerate(rows,1):
 if i==1:continue
 cmd=['python','run_resource_producer_refinement.py','--profile',str(D/'profile.json'),'--hypotheses',str(D/'hypothesis_U_upper3.tsv'),'--signed',str(D/'empty.tsv'),'--row',*map(str,r),'--prefix',str(D/'upper3_D_tests'/f'case{i}'),'--rounds','8','--cap','1500000','--expand']
 print(' '.join(cmd),flush=True);subprocess.run(cmd,cwd=P)
