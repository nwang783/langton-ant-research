"""Independent literal-image inventory, exact CNF reconstruction, and occurrence-RUP."""
from pathlib import Path
from collections import defaultdict,Counter
import itertools,json,gzip,hashlib,subprocess,time
R=Path(__file__).resolve().parents[1];S=R/'causal_reduction/morphic_candidates';A=R/'audits';D=((0,1),(1,0),(0,-1),(-1,0))
def walk(w,p=(0,0),h=0):
 out=[]
 for c in w:out.append((p,h,c));h=(h+(1 if c=='R' else -1))%4;p=p[0]+D[h][0],p[1]+D[h][1]
 return out,p,h
def valid(w):
 last={}
 for p,h,c in walk(w)[0]:
  if last.get(p)==c:return False
  last[p]=c
 return True
opt={'R':[],'L':[]}
for z in itertools.product('RL',repeat=9):
 w=''.join(z);_,p,h=walk(w)
 if valid(w):
  if (p,h)==((3,0),1):opt['R'].append(w)
  if (p,h)==((-3,0),3):opt['L'].append(w)
assert len(opt['R'])==len(opt['L'])==9
# Rebuild the entire finite prefix tree; no sampling and no node cap.
prefixes=set()
def dfs(ws,text,p,h,last):
 if len(ws)==9:prefixes.add(tuple(ws));return
 n=len(ws)
 for w in (opt[text[n]] if n else opt['R']+opt['L']):
  if n==0 and w not in opt[w[0]]:continue
  rr,q,g=walk(w,p,h);seen=last.copy()
  for v,_,c in rr:
   if seen.get(v)==c:break
   seen[v]=c
  else:dfs(ws+[w],text+w,q,g,seen)
dfs([],'',(0,0),0,{})
assert len(prefixes)==1280
source=next(z['images'] for z in json.loads((S/'free_inflations_k9.json').read_text())['results'] if z['scale']==[3,0]);assert all(set(opt[c])==set(source[c]) for c in opt);opt=source;allwords=opt['R']+opt['L']
ids=[list(map(int,s.split(','))) for s in (S/'free_nine_coarse81_prefixes.csv').read_text().splitlines()];assert len(ids)==1280 and {tuple(allwords[j] for j in row) for row in ids}==prefixes
canon=lambda c:tuple(sorted(set(c)))
def cnf(fixed):
 coarse=''.join(fixed);assert len(coarse)==81;cells=defaultdict(lambda:defaultdict(dict));clauses=[];var=lambda i,j:9*i+j+1
 for i,(p,h,c) in enumerate(walk(coarse)[0]):
  clauses.append([var(i,j) for j in range(9)])
  for j in range(9):
   for k in range(j):clauses.append([-var(i,j),-var(i,k)])
  if i<9:clauses.append([var(i,opt[c].index(fixed[i]))])
  for j,w in enumerate(opt[c]):
   rr,_,_=walk(w,(3*p[0],3*p[1]),h);local=defaultdict(list)
   for q,_,turn in rr:local[q].append(turn)
   for q,seq in local.items():
    assert all(a!=b for a,b in zip(seq,seq[1:]));cells[q][i][j]=(seq[0]=='L',len(seq)%2)
 nvar=729
 for q,events in sorted(cells.items()):
  times=sorted(events);chain=list(range(nvar+1,nvar+len(times)+2));nvar+=len(times)+1
  for t,i in enumerate(times):
   x,y=chain[t:t+2]
   for j in range(9):
    v=var(i,j)
    if j in events[i]:first,flip=events[i][j];last=first^flip;clauses.extend([[-v,x if first else-x],[-v,y if last else-y]])
    else:clauses.extend([[-v,-x,y],[-v,x,-y]])
 return nvar,Counter(map(canon,clauses))
def parse(text):
 lines=text.splitlines();header=lines[0].split();assert header[:2]==['p','cnf'];n,m=map(int,header[2:]);cs=[]
 for line in lines[1:]:
  v=list(map(int,line.split()));assert v[-1]==0 and all(0<abs(x)<=n for x in v[:-1]);cs.append(canon(v[:-1]))
 assert len(cs)==m;return n,Counter(cs)
manifest=json.loads((S/'k9_rup/manifest.json').read_text());assert manifest['status']=='ALL_1280_MONOTONE_RUP_CERTIFICATES_VERIFIED' and manifest['cases']==1280
results=[];start=time.time();exe=A/'check_rup_occurrence_independent';tmp=A/'k9_rup_independent_working';tmp.mkdir(exist_ok=True)
for i,row in enumerate(manifest['results']):
 assert row['index']==i and row['initial_choices']==ids[i];fixed=[allwords[j] for j in ids[i]];expected=cnf(fixed)
 ct=gzip.decompress((S/f'k9_rup/case{i:04d}.cnf.gz').read_bytes()).decode();pt=gzip.decompress((S/f'k9_rup/case{i:04d}.rup.gz').read_bytes()).decode()
 assert hashlib.sha256(ct.encode()).hexdigest()==row['cnf_sha256'];assert hashlib.sha256(pt.encode()).hexdigest()==row['rup_sha256'];assert parse(ct)==expected
 (tmp/'input.cnf').write_text(ct);(tmp/'proof.rup').write_text(pt);q=subprocess.run([str(exe),str(tmp/'input.cnf'),str(tmp/'proof.rup')],capture_output=True,text=True);assert q.returncode==0,(i,q.stdout,q.stderr);result=json.loads(q.stdout);assert result['valid'];results.append(result)
 if i%100==0:print(i,'independent CNF + occurrence-RUP PASS',round(time.time()-start,3),flush=True)
assert len(results)==1280
out={'status':'ALL1280 exact independently reconstructed CNFs have independently verified monotone-RUP refutations','prefix_count':1280,'additions':sum(r['rup_additions'] for r in results),'max_additions':max(r['rup_additions'] for r in results),'source_manifest_sha256':hashlib.sha256((S/'k9_rup/manifest.json').read_bytes()).hexdigest(),'checker_source_sha256':hashlib.sha256((A/'check_rup_occurrence_independent.cpp').read_bytes()).hexdigest(),'seconds':time.time()-start,'scope':'No729-turn prefix on ANY initial coloring can have p(9n)=3p(n), h(9n)=h(n) through81 coarse steps. No SAT solver trusted; literal enumeration, CNF semantics, and unit-propagation checker remain the proof base.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
