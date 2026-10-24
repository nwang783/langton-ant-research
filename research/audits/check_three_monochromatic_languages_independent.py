"""Three additional eventual single-K-label languages, exact current-color audit."""
from pathlib import Path
from collections import deque
import json,hashlib,time,gc
R=Path(__file__).resolve().parents[1];P=R/'word_stabilization';OLD=R/'continuation_2026-10-22/ant_continuation/factor_language'
bits=lambda w:int(w.replace('L','0').replace('R','1'),2)
assert hashlib.sha256((OLD/'no_pair_words150.txt').read_bytes()).hexdigest()=='28c950002dd8c7bcaddee65da9fcb2291f7166196aea80f4fab6b3db7374ba27'
W=json.loads((R/'computability/singleton_first_block_input.json').read_text())['word'];T='RRRLLRLLRRRRLLRRRRLLRLLR';F={bits((W+W)[i:i+10]) for i in range(104)};assert len(F)==84
H={bits(s.split()[0]) for s in (OLD/'no_pair_large_scc.txt').read_text().splitlines()};mask=(1<<149)-1
cyc=lambda w:{bits((w*20)[i:i+149]) for i in range(len(w))}
CW,CT=cyc(W),cyc(T);groups=[H,CW,CT];assert list(map(len,groups))==[34712,104,24] and not (H&CW or H&CT or CW&CT)
old_inner=[set(),set(),set()]
for s in (OLD/'no_pair_words150.txt').read_text().splitlines():
 w=bits(s)
 for i,G in enumerate(groups):
  if w>>1 in G and w&mask in G:old_inner[i].add(w)
assert list(map(len,old_inner))==[36277,104,24]
def check(pat,expected):
 start=time.time();target=bits(pat);colors=bytearray([2])*(301*301);step=(301,1,-301,-1);words=[];levels=[0]*151;digest=hashlib.sha256()
 def dfs(t,p,h,b,prev):
  levels[t]+=1
  if t==150:
   words.append(b);digest.update((format(b,'0150b').replace('0','L').replace('1','R')+'\n').encode());return
  old=colors[p]
  for black in(1,0):
   if old!=2 and old!=black:continue
   nb=(b<<1)+1-black;bad=t>=9 and (nb&1023) not in F
   if bad and prev and (nb&2047)!=target:continue
   colors[p]=1-black;nh=(h+(3 if black else 1))%4;dfs(t+1,p+step[nh],nh,nb,bad)
  colors[p]=old
 dfs(0,150*301+150,0,0,False)
 assert len(words)==expected
 source=P/('mono_'+pat.lower()+'_words150.txt');assert digest.hexdigest()==hashlib.sha256(source.read_bytes()).hexdigest()
 V={w>>1 for w in words}|{w&mask for w in words};assert all(g<=V for g in groups)
 index={v:i for i,g in enumerate(groups) for v in g};nextid=3
 for v in V-index.keys():index[v]=nextid;nextid+=1
 adj=[[]for _ in range(nextid)];degree=[0]*nextid;internal=[set(),set(),set()]
 for w in words:
  i,j=index[w>>1],index[w&mask]
  if i==j and i<3:internal[i].add(w)
  else:adj[i].append(j);degree[j]+=1
 assert internal==old_inner
 q=deque(i for i,n in enumerate(degree) if not n);processed=0
 while q:
  i=q.popleft();processed+=1
  for j in adj[i]:
   degree[j]-=1
   if not degree[j]:q.append(j)
 assert processed==nextid
 z=dict(pattern=pat,nodes=sum(levels),words=len(words),vertices=len(V),contracted_DAG_vertices=nextid,internal_groups_equal_previously_audited=True,source_sha256=digest.hexdigest(),seconds=time.time()-start);print(json.dumps(z),flush=True);return z
rows=[]
for p,n in [('LLRLRLLRRLL',309366),('RRRRLRLLRLL',321673),('RRRLRRRRLRL',372039)]:rows.append(check(p,n));gc.collect()
out={'status':'Independent complete-language audit passed','rows':rows,'scope':'Each specified eventual sole adjacent-defect label implies capture for finite seeds; no spacing premise and no assertion for other labels.'};Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
