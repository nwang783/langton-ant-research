"""No-import position-only k8 inventory, prefix tree, CNF and occurrence-RUP audit."""
from pathlib import Path
from collections import Counter,defaultdict
import itertools,json,gzip,hashlib,subprocess,time
B=Path('/workspace/shared/langton');S=B/'causal_reduction/morphic_candidates';A=B/'audits'
DIR=((0,1),(1,0),(0,-1),(-1,0))
def add(p,q):return p[0]+q[0],p[1]+q[1]
def rot(p,h):
 x,y=p
 for _ in range(h%4):x,y=y,-x
 return x,y
def scale(p):return 2*p[0]-2*p[1],2*p[0]+2*p[1]
def walk(w,p=(0,0),h=0):
 rr=[]
 for c in w:
  rr.append((p,h,c));h=(h+(1 if c=='R' else -1))%4;p=add(p,DIR[h])
 return rr,p,h

def extend(rr,old):
 last=old.copy()
 for p,h,c in rr:
  if last.get(p)==c:return None
  last[p]=c
 return last
words=[];traces={}
for letters in itertools.product('RL',repeat=8):
 w=''.join(letters);rr,p,h=walk(w)
 if extend(rr,{}) is not None:words.append(w);traces[w]=(rr,p,h)
prefixes=set();nodes=Counter()
def dfs(chosen,text,p,h,last):
 n=len(chosen);nodes[n]+=1
 if n==8:prefixes.add(tuple(chosen));return
 if n:
  rr,cp,ch=walk(text[:n+1]);q,hc,c=rr[-1];target=scale(DIR[(hc+(1 if c=='R' else -1))%4])
 for w in words:
  _,ep,eh=traces[w]
  if n==0:target=scale(DIR[1 if w[0]=='R' else 3])
  if rot(ep,h)!=target:continue
  rr,np,nh=walk(w,p,h);new=extend(rr,last)
  if new is not None:dfs(chosen+[w],text+w,np,nh,new)
dfs([],'',(0,0),0,{})
assert len(prefixes)==2784 and sum(nodes.values())==5161
source=json.loads((S/'position_only_prefixes_k8_a2_2.json').read_text())
assert source['status']=='COMPLETE' and len(source['prefixes'])==2784
assert {tuple(r['choices']) for r in source['prefixes']}==prefixes
for row in source['prefixes']:assert ''.join(row['choices'])==row['word']
canon=lambda c:tuple(sorted(set(c)))
def cnf(fixed):
 coarse=''.join(fixed);N=len(coarse);assert N==64
 clauses=[];nv=N+1;heads=list(range(1,N+2));clauses.append([-heads[0]])
 cells=defaultdict(lambda:defaultdict(dict));choices=[];counts=[];fixedh=0
 for i,(p,h,c) in enumerate(walk(coarse)[0]):
  target=scale(DIR[(h+(1 if c=='R' else -1))%4]);entries=[]
  for H in (0,2):
   for w in words:
    rr,ep,eh=traces[w]
    if rot(ep,H)==target:entries.append((w,H,(H+eh)%4))
  assert entries
  vs=list(range(nv+1,nv+len(entries)+1));nv+=len(entries);choices.append(vs);counts.append(len(entries));clauses.append(vs)
  for j,(w,H,E) in enumerate(entries):
   v=vs[j]
   for u in vs[:j]:clauses.append([-u,-v])
   clauses.extend([[-v,heads[i] if H==2 else -heads[i]],[-v,heads[i+1] if E==2 else -heads[i+1]]])
   ev,ep,eh=walk(w,scale(p),H);local=defaultdict(list)
   for q,hh,z in ev:local[q].append(z)
   for q,seq in local.items():
    assert all(a!=b for a,b in zip(seq,seq[1:]));cells[q][i][j]=(seq[0]=='L',len(seq)%2)
  if i<8:
   js=[j for j,(w,H,E) in enumerate(entries) if(w,H)==(fixed[i],fixedh)];assert len(js)==1
   clauses.append([vs[js[0]]]);fixedh=entries[js[0]][2]
 for q,events in sorted(cells.items()):
  times=sorted(events);chain=list(range(nv+1,nv+len(times)+2));nv+=len(times)+1
  for t,i in enumerate(times):
   x,y=chain[t:t+2]
   for j,v in enumerate(choices[i]):
    if j in events[i]:
     first,flip=events[i][j];after=first^flip;clauses.extend([[-v,x if first else -x],[-v,y if after else -y]])
    else:clauses.extend([[-v,-x,y],[-v,x,-y]])
 return nv,Counter(map(canon,clauses))
def parse(text):
 lines=text.splitlines();head=lines[0].split();assert head[:2]==['p','cnf'];n,m=map(int,head[2:]);cs=[]
 for line in lines[1:]:
  row=list(map(int,line.split()));assert row[-1]==0 and all(0<abs(x)<=n for x in row[:-1]);cs.append(canon(row[:-1]))
 assert len(cs)==m;return n,Counter(cs)
manifest=json.loads((S/'position_k8_rup/manifest.json').read_text())
assert manifest['status']=='ALL_2784_MONOTONE_RUP_CERTIFICATES_VERIFIED' and manifest['cases']==2784
exe=A/'check_rup_occurrence_independent';tmp=A/'position_k8_rup_independent_working';tmp.mkdir(exist_ok=True)
results=[];start=time.time()
for i,row in enumerate(manifest['results']):
 assert row['index']==i and row['initial_choices']==source['prefixes'][i]['choices']
 fixed=row['initial_choices'];expected=cnf(fixed)
 ct=gzip.decompress((S/f'position_k8_rup/case{i:04d}.cnf.gz').read_bytes()).decode();pt=gzip.decompress((S/f'position_k8_rup/case{i:04d}.rup.gz').read_bytes()).decode()
 assert hashlib.sha256(ct.encode()).hexdigest()==row['cnf_sha256'] and hashlib.sha256(pt.encode()).hexdigest()==row['rup_sha256']
 assert parse(ct)==expected,i
 (tmp/'input.cnf').write_text(ct);(tmp/'proof.rup').write_text(pt)
 q=subprocess.run([str(exe),str(tmp/'input.cnf'),str(tmp/'proof.rup')],capture_output=True,text=True);assert q.returncode==0,(i,q.stdout,q.stderr)
 got=json.loads(q.stdout);assert got['valid'];results.append(got)
 if i%100==0:print(i,'exact CNF and independent occurrence-RUP passed',round(time.time()-start,2),flush=True)
assert len(results)==2784
out={'status':'ALL2784 position-only k8 CNFs independently reconstructed and RUP verified','internally_legal_images':len(words),'prefix_tree_nodes':sum(nodes.values()),'prefix_nodes_by_depth':dict(nodes),'prefixes':len(prefixes),'proof_additions':sum(r['rup_additions'] for r in results),'max_additions':max(r['rup_additions'] for r in results),'source_manifest_sha256':hashlib.sha256((S/'position_k8_rup/manifest.json').read_bytes()).hexdigest(),'seconds':time.time()-start,'scope':'No512-turn prefix on ANY initial coloring satisfies p(8n)=(2+2i)p(n) through64 coarse moves. No heading-preservation premise and no SAT solver trusted.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
