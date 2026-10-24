"""Exact relational reversal of a seven-field guarded-XOR patch graph.
CLI FORWARD.json PREFIX. The sole original goal guard is the reverse start cube.
"""
from pathlib import Path
import json,sys,hashlib
p,out=map(Path,sys.argv[1:]);J=json.loads(p.read_text());T=[];goals=[]
for fr,to,k,v,f,g,a in J['transitions']:
 if g:goals.append((fr,k,v));continue
 T.append([to,fr,k,v^(f&k),f,0,0,0,a])
assert len(goals)==1
for r in J['reentry']:T.append([r,J['out'],0,0,0,0,0,0,99])
sid,k,v=J['start'];T.append([sid,sid,k,v,0,0,0,1,100]);new={'format':'exact_reverse_guarded_xor_v1','forward_model_file':str(p),'forward_model_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'n':J['n'],'out':J['out']+1,'poses':J['poses']+[None],'start':list(goals[0]),'transitions':T,'reentry':[]}
out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{new['n']} {new['out']+1} {len(T)} 0\n");f.write(' '.join(map(str,new['start']))+'\n')
 for r in T:f.write(' '.join(map(str,r))+'\n')
 f.write('\n')
print(json.dumps({'variables':new['n'],'positions':new['out']+1,'transitions':len(T),'start':new['start']}))
