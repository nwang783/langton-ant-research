"""Signed-only all-ten source-patch/source-companion U-tip discovery sweep."""
import json,subprocess,sys,time,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent;rows=json.loads((R/'u_tip_candidates.json').read_text());D=R/'u_tip_baseline';D.mkdir(exist_ok=True);results=[]
def run(cmd,p):
 z=subprocess.run(list(map(str,cmd)),cwd=P,capture_output=True,text=True);Path(str(p)+'.txt').write_text(z.stdout);Path(str(p)+'.log').write_text(z.stderr);return z.stdout.strip()
for i,r in enumerate(rows,1):
 prefix=D/f'case{i:03d}';b=Path(str(prefix)+'_base');f=Path(str(prefix)+'_flags');start=time.time();row=r['tuple']
 run(['python','generate_resource_transfer_patch.py',R/'profile.json',*row,b,'source'],str(b)+'_gen')
 run(['python','add_resource_source_flags.py',str(b)+'.json',f,R/'empty.tsv',R/'empty.tsv'],str(f)+'_gen')
 res=run([P/'protected_patch_bdd_flags',str(f)+'.dat',300000,str(f)+'.bdd'],f);entry={'index':i,'tuple':row,'prefix':str(f),'result':res,'seconds':round(time.time()-start,3)}
 if 'EXHAUSTED_NO_HIT'in res:entry['verification']=run(['python','verify_protected_patch_bdd_flags.py',str(f)+'.dat',str(f)+'.bdd'],str(f)+'_verification')
 results.append(entry);(D/'summary.json').write_text(json.dumps({'scope':'Signed HB premises only; every no-hit still needs independent model/invariant audit','candidate_file_sha256':hashlib.sha256((R/'u_tip_candidates.json').read_bytes()).hexdigest(),'results':results},indent=2));print(i,row,res,flush=True)
