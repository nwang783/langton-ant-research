"""Adds the two forced-next-V equal-read certificates to the packet kernel.
The right-extension hypothesis is essential; these are not terminal-C claims.
"""
from pathlib import Path
import json
ns={};src=Path(__file__).with_name('spatial_packet_kernel.py').read_text();exec(src[:src.index('GOOD2=')],ns)
D,F,LAST,FIRST,WORDS,rot,pair,RAW,feasible=[ns[x]for x in('D','F','LAST','FIRST','WORDS','rot','pair','RAW','feasible')]
j=json.load(open(Path(__file__).with_name('spatial_packet_kernel.json')))
S={tuple(z[:5])for z in j['kernel']}
extra={('a','e',-1,5,2):(0,1),('d','e',0,4,2):(0,0)}
assert set(map(tuple,j['unexcluded_completed_C_input_pairs']))==set(extra)
S.update(extra);counts={}
for key,q in extra.items():
 a,b,x,y,h=key;assert WORDS[b]=='VC';first=dict(FIRST[b]);ep=D[b]['end_pose']
 for z in RAW['V']['trace']:
  dx,dy=rot(z['p'],ep[2]);first.setdefault((ep[0]+dx,ep[1]+dy),z['c'])
 lq=rot((q[0]-x,q[1]-y),-h%4);assert LAST[a][q]==first[lq]=='R'
 # Explicitly recheck all short-gap controls for the two additions.
 p,k=ns['end'](a)
 if (p,k)==((x,y),h):assert not feasible(a+b)
 for c in WORDS:
  p,k=ns['end'](a);p,k=ns['end'](c,p,k)
  if(p,k)==((x,y),h):assert not feasible(a+c+b)
 readers=set()
 for t in WORDS:
  for k in range(4):
   for z in F[t]:
    dx,dy=rot(z,k);p=q[0]-dx,q[1]-dy
    if(sum(p)-k)%2:continue
    readers.add((t,*p,k))
 for t,cx,cy,k in readers:
  assert(a,t,cx,cy,k)in S or pair(t,(cx,cy),k,b,(x,y),h)in S
 counts[str(key)]=len(readers)
 j['kernel'].append(list(key)+[['extended-equal-read',*q]])
j['kernel'].sort(key=lambda z:z[:5]);j['unexcluded_completed_C_input_pairs']=[];j['extension_reader_counts']=counts
Path(__file__).with_name('spatial_packet_kernel_complete.json').write_text(json.dumps(j,indent=2))
print('Complete family',len(j['kernel']),'extra reader counts',counts)
