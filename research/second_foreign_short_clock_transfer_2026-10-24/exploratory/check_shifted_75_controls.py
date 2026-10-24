exec(open('/workspace/shared/langton/fresh_RAW_U_LEFT_all_length_2026-10-24/check_fresh_U_LEFT_all_length.py').read().split('LEFT={(0,0)')[0])
STAR={(0,0),(0,1),(1,0),(1,1)};HOOK={'F':{(-3,-1),(-2,-1)},'Q':{(-3,-3),(-2,-3),(-1,-3),(-1,-2)},'B':{(-2,-4),(-1,-4),(0,-4),(0,-3)}}
def lossword(word):
 raw=''.join(W[a]for a in word);t=l.trace(raw+l.M)
 if not t['feasible']:return None
 firstidx=next(i for i,a in enumerate(word)if a in'FQB');lastidx=len(word)-1;ut=l.trace(W['U']);targets={('oldU',g):(g,ut['last'][g][1])for g in STAR};B={q:('initial',q)for q,(c,k)in t['first'].items()if c=='L'};p=(0,0,0);tick=0;pre2={};loss=[]
 for i,a in enumerate(word):
  if i==firstidx:
   fr=l.trace(W[a]);ep=after(W[a],p)
   for g in HOOK[a]:
    cell=add(ep[:2],l.rot(g,ep[2]));local=l.rot(sub(cell,p[:2]),-p[2]);targets['hook',g]=(cell,tick+fr['last'][local][1])
  if i==lastidx:pre2={name:(B.get(g)==birth,g,birth)for name,(g,birth)in targets.items()}
  for k,c in enumerate(W[a]):
   g=p[:2]
   if i==lastidx and c=='L':
    for name,(alive,q,birth)in pre2.items():
     if alive and q==g and B.get(g)==birth:loss.append((name,'ownRAW',k,g,birth))
   if c=='L':del B[g]
   else:B[g]=tick
   p=after(c,p);tick+=1
 for k,c in enumerate(l.M):
  g=p[:2]
  if c=='L':
   for name,(alive,q,birth)in pre2.items():
    if alive and q==g and B.get(g)==birth:loss.append((name,'nextM',k,g,birth))
  if c=='L':del B[g]
  else:B[g]=tick
  p=after(c,p);tick+=1
 return dict(word=word,loss=loss,seed=[q for q,(c,k)in t['first'].items()if c=='L'],allreads=tick)
words=[]
for creator in ['U','UC','UCC']:
 for bridge,firstAs in [('V','FQ'),('U','FQB')]:
  for A in firstAs:
   for b,secondAs in [('V','FQ'),('U','FQB')]:
    for A2 in secondAs:words.append(creator+bridge+A+b+A2)
positives=[]
for w in sorted(words,key=lambda w:(len(''.join(W[a]for a in w)),w)):
 r=lossword(w)
 if r:
  positives.append(r);print('YES',w,'mass',len(r['seed']),'loss',r['loss'])
  if r['loss']:
   import json;Path('/tmp/attained_shifted_twoFORE_loss.json').write_text(json.dumps(r,indent=2));break
print('TOTAL',len(words),'positive',len(positives))
