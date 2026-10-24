"""Reconstruct each C++ discovery as a full literal finite-seed transfer witness."""
from pathlib import Path
import json,sys,hashlib
P=Path(__file__).resolve().parents[1]/'core_periodicity_new/chronology_dcuv';log=Path(sys.argv[1]);depth=int(sys.argv[2]);G=json.loads((P/'literal_residual_geometry.json').read_text())['geometry'];seen=[];M='LLLLRLRRRRL';core={tuple(z)for z in json.loads((P/'literal_residual_geometry.json').read_text())['core']}
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def world(p,h,z):x,y=rot(z,h);return(p[0]+x,p[1]+y)
for l in log.read_text().splitlines():
 if not l.startswith('EVENT '):continue
 e=json.loads(l[6:]);path=e['packet_ids'];raw=''.join(G[a]['word']for a in path);p=(0,0);h=0;last={};first={};dirs=[(0,1),(1,0),(0,-1),(-1,0)]
 for c in raw+M:
  assert last.get(p)!=c;first.setdefault(p,c);last[p]=c;h=(h+(1 if c=='R'else-1))%4;d=dirs[h];p=(p[0]+d[0],p[1]+d[1])
 seed=sorted([list(q)for q,c in first.items()if c=='L']);tokens={tuple(q):None for q in seed if tuple(q)not in core};p=(0,0);h=0;poses=[];source=e['source_index'];target=e['target_index'];slot=e['target_input_slot'];q=None
 for t,a in enumerate(path):
  g=G[a];poses.append((*p,h))
  if t==source:q=world(p,h,e['tuple'][5:])
  if source<t<target:assert q not in {world(p,h,z[:2])for z in g['requirements']}
  for j,z in enumerate(g['inputs']):
   cell=world(p,h,z);assert cell in tokens
   old=tokens.pop(cell)
   if t==target and j==slot:assert cell==q and old==source
  for z in g['outputs']:
   cell=world(p,h,z);assert cell not in tokens;tokens[cell]=t
  p=world(p,h,g['endpoint'][:2]);h=(h+g['endpoint'][2])%4
 sp=poses[source];tp=poses[target];delta=rot((tp[0]-sp[0],tp[1]-sp[1]),-sp[2]);assert tuple(e['tuple'][:5])==(path[source],path[target],*delta,(tp[2]-sp[2])%4);assert target+1<len(path)
 seen.append(dict(e,packet_names=[G[a]['name']for a in path],source_pose=sp,target_pose=tp,initial_black_seed=seed,raw_word=raw,terminal_marker=M))
summary=[json.loads(l[8:])for l in log.read_text().splitlines()if l.startswith('SUMMARY ')];out={'status':'Literal positive controls, not an absence theorem','packet_depth':depth,'transfer_count':len(seen),'fast_search_summary':summary,'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest(),'profile_sha256':hashlib.sha256((P/'profile.json').read_bytes()).hexdigest(),'witnesses':sorted(seen,key=lambda e:e['tuple'])};pref=P/(sys.argv[3] if len(sys.argv)>3 else f'observed_transfers_fast_depth{depth}');pref.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');pref.with_suffix('.tsv').write_text(''.join(' '.join(map(str,e['tuple']))+'\n'for e in out['witnesses']));print('PASS',len(seen),summary)
