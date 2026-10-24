from pathlib import Path
ns={};s=Path('spatial_packet_kernel.py').read_text();exec(s[:s.index('GOOD2=')],ns)
D,F,LAST,FIRST,WORDS,rot,pair,RAW=[ns[x]for x in('D','F','LAST','FIRST','WORDS','rot','pair','RAW')]
import json
j=json.load(open('spatial_packet_kernel.json'));S={tuple(z[:5])for z in j['kernel']};targets=[tuple(z)for z in j['unexcluded_completed_C_input_pairs']];S.update(targets)
for key in targets:
 a,b,x,y,h=key;first=dict(FIRST[b]);ep=D[b]['end_pose'];
 for z in RAW['V']['trace']:
  dx,dy=rot(z['p'],ep[2]);first.setdefault((ep[0]+dx,ep[1]+dy),z['c'])
 print('TARGET',key)
 for q,c in first.items():
  dx,dy=rot(q,h);q=x+dx,y+dy
  if LAST[a].get(q)!=c:continue
  rem=set()
  for t in WORDS:
   for k in range(4):
    for z in F[t]:
     dx,dy=rot(z,k);p=q[0]-dx,q[1]-dy
     if(sum(p)-k)%2:continue
     if(a,t,*p,k)not in S and pair(t,p,k,b,(x,y),h)not in S:rem.add((t,*p,k))
  print('equal-cell',q,c,'unexcluded readers',len(rem),sorted(rem)[:10])
