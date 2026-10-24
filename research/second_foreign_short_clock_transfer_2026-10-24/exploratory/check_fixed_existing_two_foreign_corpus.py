from pathlib import Path
import importlib.util,json
R=Path('/workspace/shared/langton');P=R/'word_stabilization/probe_existing_foreign_contacts.py';s=importlib.util.spec_from_file_location('p',P);p=importlib.util.module_from_spec(s);s.loader.exec_module(p);l=p.lit;W=p.words;M=p.M

def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def after(w,pose=(0,0,0)):
 q,h=pose[:2],pose[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h
STAR={(0,0),(0,1),(1,0),(1,1)};HOOK={4:{(-3,-1),(-2,-1)},5:{(-3,-3),(-2,-3),(-1,-3),(-1,-2)},6:{(-2,-4),(-1,-4),(0,-4),(0,-3)}}
seqs={};histseen=set();sections=0
for he,(u,a,v)in enumerate(p.H['history_edges']):
 ids=tuple(p.H['history_states'][u]+[p.H['source_return_ids'][a]])
 if ids in histseen:continue
 histseen.add(ids);raw=''.join(p.R[i][2]for i in ids);full=raw+p.R[ids[-1]][1]
 for start in range(len(raw)):
  if not full.startswith(W[3]+M,start):continue
  labels=[];pos=start
  while pos<len(raw):
   opts=[(a,len(w))for a,w in enumerate(W)if pos+len(w)<=len(raw)and full.startswith(w+M,pos)]
   if not opts:break
   assert len(opts)==1
   a,n=opts[0];labels.append(a);pos+=n
   if sum(a>=4 for a in labels)==2:
    sections+=1;seqs.setdefault(tuple(labels),dict(history_edge=he,return_ids=ids,start=start,end=pos));break
print('fixed_histories',len(histseen),'two_foreign_U_sections',sections,'distinct',len(seqs),flush=True)
for seq,meta in sorted(seqs.items(),key=lambda q:(sum(map(lambda a:len(W[a]),q[0])),q[0])):
 raw=''.join(W[a]for a in seq);tt=l.trace(raw+M);assert tt['feasible'];B={q:('initial',q)for q,(c,k)in tt['first'].items()if c=='L'};pose=(0,0,0);tick=0;targets={};firstA=False;secondidx=len(seq)-1;pre2={};loss=[]
 for i,a in enumerate(seq):
  if i==0:
   tr=l.trace(W[3]);targets.update({('oldU',q):(q,tr['last'][q][1])for q in STAR})
  if a>=4 and not firstA:
   firstA=True;fr=l.trace(W[a]);ep=after(W[a],pose);normep=after(W[a])
   for q in HOOK[a]:
    cell=add(ep[:2],l.rot(q,ep[2]));loc=l.rot(sub(cell,pose[:2]),-pose[2]);targets['hook',q]=(cell,tick+fr['last'][loc][1])
  if i==secondidx:pre2={name:(B.get(g)==birth,g,birth)for name,(g,birth)in targets.items()};start2=tick
  for k,c in enumerate(W[a]):
   g=pose[:2]
   if i==secondidx and c=='L':
    for name,(alive,cell,birth)in pre2.items():
     if alive and g==cell and B.get(g)==birth:loss.append((name,k,'ownRAW',g,birth))
   if c=='L':del B[g]
   else:B[g]=tick
   pose=after(c,pose);tick+=1
 for k,c in enumerate(M):
  g=pose[:2]
  if c=='L':
   for name,(alive,cell,birth)in pre2.items():
    if alive and g==cell and B.get(g)==birth:loss.append((name,k,'actualM11',g,birth))
  if c=='L':del B[g]
  else:B[g]=tick
  pose=after(c,pose);tick+=1
 print('CONTROL',''.join('DCVUFQB'[a]for a in seq),'raw',len(raw),'loss',loss,flush=True)
 if loss:
  out=dict(seq=seq,word=''.join('DCVUFQB'[a]for a in seq),raw=raw,loss=loss,seed=[q for q,(c,k)in tt['first'].items()if c=='L'],meta=meta,source_corpus='fixed13516sixreturnhistoryedges');Path('/tmp/attained_existing_twoFORE_loss.json').write_text(json.dumps(out,indent=2));print('ATTAINED',out['word'],flush=True);break
