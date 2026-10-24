"""Read immutable literal Lean tables; extract exact fixed observation windows.
No ant simulation or search. Parsing accepts only the table's literal grammar.
"""
import re,json,hashlib,gzip
from pathlib import Path
P=Path(__file__).parent;R=P.parent/'sources/imfinn-two-black/lean/TwoBlack'
V={'.pp':(2,2),'.pm':(2,-2),'.mp':(-2,2),'.mm':(-2,-2)}
TOKEN=re.compile(r'\s*(⟨|⟩|\[|\]|\(|\)|,|\.[a-z]+|true|false|-?\d+)')
def load_literal(path):
 text=path.read_text();s=text.index(':=')+2; tokens=[]
 while True:
  m=TOKEN.match(text,s)
  if not m:break
  tokens.append(m[1]);s=m.end()
 it=iter(tokens);cur=[next(it)]
 def parse():
  a=cur[0]
  if a in('⟨','[','('):
   end={'⟨':'⟩','[':']','(':')'}[a];out=[];cur[0]=next(it)
   if cur[0]!=end:
    while True:
     out.append(parse())
     if cur[0]!=',':break
     cur[0]=next(it)
     if cur[0]==end:break
   assert cur[0]==end,(path,cur[0],end)
   cur[0]=next(it,None);return out
  cur[0]=next(it,None)
  return int(a)if re.fullmatch(r'-?\d+',a)else a
 ans=parse();return ans
jobs=[];sources={};counts={}
def add(src,kind,index,cells,ms,s,u):
 cells=sorted(set(map(tuple,cells)))
 jobs.append(dict(id=len(jobs),source=src,kind=kind,index=index,cells=cells,
                  windows=[dict(kind='switch',time=t)for t in sorted(ms)]+[dict(kind='terminal',time=s)],
                  terminal_drift=u,updates=s+104))
 assert all(0<=t<=s for t in ms)
 counts[kind]=counts.get(kind,0)+1

def fam1(src,kind,index,F,H):
 dg,near,far=F;n,D,C,ms,s,u,A=H;v=V[dg]
 cells=near+[[q[0]+n*v[0],q[1]+n*v[1]]for q in far]
 add(src,kind,index,cells,ms,s,u)

def cells2(F,a,b):
 vs,blocks=F;ds=[V[z]for z in vs]
 return[[q[0]+sum([a,b][i]*ds[i][0]for i in mask),q[1]+sum([a,b][i]*ds[i][1]for i in mask)]for q,mask in blocks]
files=[R/'Level1Data.lean']+sorted((R/'Parents').glob('Chunk*.lean'))+sorted((R/'Chan').glob('Data*.lean'))+[R/'PerpData.lean',R/'ParData.lean']
for path in files:
 src=str(path.relative_to(R));sources[src]=hashlib.sha256(path.read_bytes()).hexdigest();root=load_literal(path)
 if path.name=='Level1Data.lean':
  for j,(F,H)in enumerate(root):fam1(src,'level1',j,F,H)
 elif path.parent.name=='Parents':
  for j,(point,tau,H0,fs)in enumerate(root):
   s,dg,A,t1,psi,tdiv,periods=H0;add(src,'parent_terminal',j,[point],[],s,V[dg])
   for k,(F,H)in enumerate(fs):fam1(src,'parent_tail',[j,k],F,H)
 elif path.parent.name=='Chan':
  point,kids1,kids2=root
  for j,(F,base,H)in enumerate(kids1):fam1(src,'channel_child',j,F,H)
 else:
  for j,row in enumerate(root):
   if path.name=='PerpData.lean':c,H,slab1=row;slab2=[];kind='perpendicular'
   else:c,side,H,slab1,slab2=row;kind='parallel'
   F,bases=c;aa,bb,D1,C1,ms1,D2,C2,ms2,s,u,A=H
   add(src,kind,j,cells2(F,aa,bb),ms1+ms2,s,u)
   for k,h in enumerate(slab1):add(src,kind+'_slab1',[j,k],cells2(F,bases[0]+k,h[0]),h[3],h[4],h[5])
   for k,h in enumerate(slab2):add(src,kind+'_slab2',[j,k],cells2(F,h[0],bases[1]+k),h[3],h[4],h[5])
assert counts=={'level1':22,'parent_terminal':2432,'parent_tail':53504,'channel_child':45452,'perpendicular':286,'perpendicular_slab1':120,'parallel':220,'parallel_slab1':340,'parallel_slab2':112},counts
meta=dict(source_hashes=sources,counts=counts,total_jobs=len(jobs),total_fixed_updates=sum(j['updates']for j in jobs),
 max_updates=max(j['updates']for j in jobs),max_windows=max(len(j['windows'])for j in jobs),
 note='Does not include dynamically searched direct certB leaves or blank/singleton branches already covered separately.')
with gzip.open(P/'TWO_BLACK_WORD_JOBS.jsonl.gz','wt')as f:
 for j in jobs:f.write(json.dumps(j,separators=(',',':'))+'\n')
(P/'TWO_BLACK_WORD_JOB_INVENTORY.json').write_text(json.dumps(meta,indent=2)+'\n')
# Representative fixed benchmark: all level1, all two-dimensional base families,
# all slabs, plus200 evenly spaced one-dimensional non-level1 anchors.
large=[j for j in jobs if j['kind']in('parent_tail','channel_child')]
sel=[j for j in jobs if j['kind']in('level1','perpendicular','parallel')or'slab'in j['kind']]
sel +=[large[i*(len(large)-1)//199]for i in range(200)]
with open(P/'TWO_BLACK_WORD_BENCHMARK.txt','w')as f:
 for j in sel:
  nums=[j['id'],len(j['cells'])]+[a for q in j['cells']for a in q]+[len(j['windows'])]+[w['time']for w in j['windows']]
  f.write(' '.join(map(str,nums))+'\n')
(P/'TWO_BLACK_WORD_BENCHMARK_JOBS.json').write_text(json.dumps(sel,separators=(',',':'))+'\n')
print(json.dumps({**counts,'total_jobs':len(jobs),'full_fixed_updates':meta['total_fixed_updates'],'benchmark_jobs':len(sel),'benchmark_updates':sum(j['updates']for j in sel)}))
