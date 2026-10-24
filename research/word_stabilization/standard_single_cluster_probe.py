from pathlib import Path
import json,sys,re
from collections import defaultdict,deque
root=Path('..');W=re.search(r'const string W="([LR]+)"',Path('enumerate_adjacent_pair_spacing.cpp').read_text()).group(1);assert len(W)==104
F={(W+W)[i:i+10]for i in range(104)};long=W*5;CW={long[i:i+149]for i in range(104)}
legal=(root/'continuation_2026-10-22/ant_continuation/factor_language/words150.txt').read_text().splitlines();rev=defaultdict(list);outW=[]
for w in legal:
 rev[w[1:]].append(w[:-1])
 if w[:-1]in CW and w[1:]not in CW:outW.append(w)
reach=set(CW);q=deque(CW)
while q:
 for v in rev[q.popleft()]:
  if v not in reach:reach.add(v);q.append(v)
print('W outgoing legal edges',len(outW),'reachable',len(reach),flush=True)
result=[]
for run in range(1,int(sys.argv[1])if len(sys.argv)>1 else 5):
 L=150+run+149;counts=[0]*(L+1);survivors=[];nodes=0
 for phase in range(104):
  w=long[phase:phase+150];field={};p=0j;h=1j
  for c in w:
   assert field.get(p)!=c;field[p]=c;h*=(-1j if c=='R'else 1j);p+=h
  def dfs(w,p,h):
   global nodes
   nodes+=1;counts[len(w)]+=1
   if len(w)==L:survivors.append({'phase':phase,'word':w,'reaches_standard':w[-149:]in reach});return
   old=field.get(p)
   for c in'LR':
    if c==old:continue
    nw=w+c;bad=nw[-10:]not in F
    if bad!=(150<=len(w)<150+run):continue
    field[p]=c;nh=h*(-1j if c=='R'else 1j);dfs(nw,p+nh,nh)
    if old is None:del field[p]
    else:field[p]=old
  dfs(w,p,h)
 z={'run':run,'nodes':nodes,'max_depth':max(i for i,n in enumerate(counts)if n),'survivors':len(survivors),'standard_reachable':sum(s['reaches_standard']for s in survivors),'counts':counts[150:],'examples':survivors if run==2 else survivors[:10]};result.append(z);print({k:v for k,v in z.items()if k not in('counts','examples')},flush=True)
Path('standard_single_cluster_probe.json').write_text(json.dumps({'W_outgoing_legal_edges':outW,'results':result},indent=2))
