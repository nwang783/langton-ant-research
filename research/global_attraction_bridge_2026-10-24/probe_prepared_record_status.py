import json
from pathlib import Path
P=Path(__file__).parent;M=Path('/workspace/shared/langton/causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json');a=json.loads(M.read_text());D=((0,1),(1,0),(0,-1),(-1,0));normals=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
outs=[]
for N in (1,2,3):
 B={tuple(v[0]*N+v[1]for v in z)for z in a['seed_families']};p=tuple(v[0]*N+v[1]for v in [a['stages'][0]['start_x_N_constant'],a['stages'][0]['start_y_N_constant']]);h=a['stages'][0]['heading']
 for s in a['stages'][:-1]:
  assert p==tuple(s[k][0]*N+s[k][1]for k in ['start_x_N_constant','start_y_N_constant'])and h==s['heading']
  for c in s['word']*(s['count_N_constant'][0]*N+s['count_N_constant'][1]):
   assert(p in B)==(c=='L');B^={p};h=(h+(1 if c=='R'else-1))%4;p=tuple(p[j]+D[h][j]for j in range(2))
 w=a['stages'][-1]['word']*N;read=set();headmax={n:-10**9 for n in normals}
 for c in w:
  read.add(p)
  for n in normals:headmax[n]=max(headmax[n],sum(n[j]*p[j]for j in range(2)))
  h=(h+(1 if c=='R'else-1))%4;p=tuple(p[j]+D[h][j]for j in range(2))
 untouched=B-read;zs={n:max(untouched,key=lambda z:(sum(n[j]*z[j]for j in range(2)),z))for n in normals}
 print(N,[(n,zs[n],sum(n[j]*zs[n][j]for j in range(2))-headmax[n])for n in normals],flush=True)
 outs.append(dict(N=N,witnesses=[[n,zs[n]]for n in normals]))
(P/'PREPARED_RECORD_STATUS_PROBE.json').write_text(json.dumps(outs,indent=2)+'\n')
