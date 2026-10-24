exec(open('/workspace/shared/langton/fresh_RAW_U_LEFT_all_length_2026-10-24/check_fresh_U_LEFT_all_length.py').read().split('LEFT={(0,0)')[0])
from functools import lru_cache
from collections import Counter
@lru_cache(None)
def perms(d,v,u):
 if d+v+u==0:return ('',)
 out=[]
 if d:out+=['D'+q for q in perms(d-1,v,u)]
 if v:out+=['V'+q for q in perms(d,v-1,u)]
 if u:out+=['U'+q for q in perms(d,v,u-1)]
 return tuple(out)
STAR={(0,0),(0,1),(1,0),(1,1)};allwords={};meta={}
for A in'FQB':
 p1=after(W[A],(0,4,0));trA=l.trace(W[A]);ep=after(W[A]);S={(-3,-1),(-2,-1)}if A=='F'else{(-3,-3),(-2,-3),(-1,-3),(-1,-2)}if A=='Q'else{(-2,-4),(-1,-4),(0,-4),(0,-3)}
 ids={('oldU',g):g for g in STAR};ids.update({('hook',g):add(p1[:2],l.rot(g,p1[2]))for g in S})
 goals=set()
 for A2 in'FQB':
  tr=l.trace(W[A2]+l.M)
  for tag in ids.values():
   for slot,(c,k)in tr['first'].items():
    if c!='L':continue
    p=(*sub(tag,l.rot(slot,0)),0)
    if(sum(p[:2]))%2==0:goals.add((A2,*p[:2]))
 count=0
 for A2,gx,gy in sorted(goals):
  for final in ['DV','DU','VV','VU']:
   fep=after(''.join(W[q]for q in final))if final else(0,0,0)
   tx,ty=gx-fep[0],gy-fep[1]
   dy=p1[1]-1-ty
   if dy<0:continue
   for vs in range(dy//3+1):
    for us in range(dy//4+1):
     for ds in range(dy-3*vs-4*us+1):
      rr=dy-ds-3*vs-4*us
      for ve in range(rr+1):
       de=rr-ve;dx=tx-p1[0]-1+ds+vs-de-3*ve
       if dx<0 or dx%4:continue
       ue=dx//4
       for pre in perms(ds,vs,us):
        for post in perms(de,ve,ue):
         word='U'+A+pre+'C'+post+'C'+final+A2
         allwords[word]=(A,pre,post,A2,(gx,gy,0));count+=1
 print('A',A,'goals',len(goals),'countrecords',count,'unique total',len(allwords),flush=True)
print('TOTAL',len(allwords),flush=True)
# Necessary read consistency first, then ORIGINAL-ID presence at actual A2
# entry and the actual second RAW/following-M ownership of its loss.
def erosion(word,t):
 A,pre,post,A2,goal=allwords[word];raw=''.join(W[a]for a in word);p=(0,0,0);tick=0;B={q:('initial',q)for q,(c,k)in t['first'].items()if c=='L'};targets={};pre2={};loss=[]
 for i,a in enumerate(word):
  if i==0:
   ut=l.trace(W['U']);targets.update({('oldU',g):(g,ut['last'][g][1])for g in STAR})
  if i==1:
   st=p;fo=l.trace(W[a]);ep=after(W[a]);fexit=add(p[:2],l.rot(ep[:2],p[2]));fh=(p[2]+ep[2])%4;S={(-3,-1),(-2,-1)}if a=='F'else{(-3,-3),(-2,-3),(-1,-3),(-1,-2)}if a=='Q'else{(-2,-4),(-1,-4),(0,-4),(0,-3)}
   for g in S:
    cell=add(fexit,l.rot(g,fh));local=l.rot(sub(cell,st[:2]),-st[2]);targets['hook',g]=(cell,tick+fo['last'][local][1])
  if i==len(word)-1:pre2={name:(B.get(g)==birth,g,birth)for name,(g,birth)in targets.items()};start=tick
  for k,c in enumerate(W[a]):
   cell=p[:2]
   if i==len(word)-1 and c=='L':
    for name,(alive,g,birth)in pre2.items():
     if alive and cell==g and B.get(g)==birth:loss.append((name,k,'own_RAW',cell,birth))
   if c=='L':del B[cell]
   else:B[cell]=tick
   p=after(c,p);tick+=1
 for k,c in enumerate(l.M):
  cell=p[:2]
  if c=='L':
   for name,(alive,g,birth)in pre2.items():
    if alive and cell==g and B.get(g)==birth:loss.append((name,k,'next_M',cell,birth))
  if c=='L':del B[cell]
  else:B[cell]=tick
  p=after(c,p);tick+=1
 return loss,pre2
pos=[];fail=Counter()
for n,word in enumerate(sorted(allwords,key=lambda s:(sum(len(W[a])for a in s),len(s),s))):
 tr=l.trace(''.join(W[a]for a in word)+l.M)
 if not tr['feasible']:fail['literal']+=1;continue
 loss,pre2=erosion(word,tr);pos.append((word,loss))
 if loss:
  print('ATTAINED',word,'wordmeta',allwords[word],'seed',len([q for q,(c,k)in tr['first'].items()if c=='L']),'loss',loss,'tested',n+1,'positivebefore',len(pos),flush=True)
  import json;Path('/tmp/two_C_two_base_attained.json').write_text(json.dumps(dict(word=word,meta=allwords[word],loss=loss,seed=[q for q,(c,k)in tr['first'].items()if c=='L'],tested=n+1,total_candidates=len(allwords),positives_before=pos),indent=2));break
else:print('NO LOSS','feasible',len(pos),'fail',dict(fail),'positives',pos[:20],flush=True)
