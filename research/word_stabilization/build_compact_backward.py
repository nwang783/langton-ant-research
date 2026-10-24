from pathlib import Path
p=Path('/workspace/shared/langton/word_stabilization/bdd_macro_backward_ports.py');s=p.read_text();a=s.index('heads=[(*c,h)');b=s.index('F={};initial={}',a)
prefix=s[:a]
template=s[s.index('# For each exact port,',a):b].replace("if head[0]=='OUT':return 1","if isfar(head):return 1")
body='''# Rectangular compactification. Each extreme coordinate denotes an entire
# unbounded half-line, not one lattice point. Every far region misses P.
amin=min(a for a,b in centers);amax=max(a for a,b in centers)
bmin=min(b for a,b in centers);bmax=max(b for a,b in centers)
def isfar(head):
 a,b,h=head;return not(amin<=a<=amax and bmin<=b<=bmax)
def clip(a,b,h):return (max(amin-1,min(amax+1,a)),max(bmin-1,min(bmax+1,b)),h)
def dim_image(c,lo,hi,d):
 if lo<=c<=hi:return [max(lo-1,min(hi+1,c+d))]
 if c==lo-1:
  end=lo-1+d;return [lo-1]+list(range(lo,min(hi,end)+1))+([hi+1] if end>hi else [])
 assert c==hi+1
 start=hi+1+d;return ([lo-1] if start<lo else [])+list(range(max(lo,start),hi+1))+[hi+1]
heads=[(a,b,h) for a in range(amin-1,amax+2) for b in range(bmin-1,bmax+2) for h in range(4)]
print('COMPACT BOX',amin,amax,bmin,bmax,'heads',len(heads),flush=True)
'''
body+=template
body+='''T={};NEXT={};SOURCE={}
INCOMING={c:[] for c in contexts}
for (c,k),nc in CT.items():INCOMING[nc].append((c,k))
for head in heads:
 a,b,h=head
 for k in ALPHA:
  _,(da,db,eh)=zero[h,k]
  if isfar(head):
   T[head,k]=(1,0,False)
   NEXT[head,k]=[(aa,bb,eh) for aa in dim_image(a,amin,amax,da) for bb in dim_image(b,bmin,bmax,db)]
   continue
  tr,to=trace(head,k);NEXT[head,k]=[clip(*to)]
  seq=[(1<<ix[p],c) for p,c in tr if p in ix]
  known=black=odd=0
  for bit,c in seq:
   if not known&bit:known|=bit;black|=bit if c else 0
   else:assert bool((black^odd)&bit)==c
   odd^=bit
  guard=bb.cube(known,black);T[head,k]=(guard,odd,any(bit==qb for bit,c in seq))
  nr=[c for p,c in tr if p==q]
  if nr and not nr[-1]:
   to=NEXT[head,k][0]
   for (pc,letter),nc in CT.items():
    if letter!=k:continue
    pre=bb.intersect(guard,color_guard(head,pc))
    root=bb.intersect(bb.flip(pre,odd),color_guard(to,nc))
    key=(to,nc);SOURCE[key]=bb.union(SOURCE.get(key,0),root)
REV={(head,k):[] for head in heads for k in ALPHA}
for head in heads:
 for k in ALPHA:
  guard,odd,touch=T[head,k]
  if touch:continue
  for to in NEXT[head,k]:REV[to,k].append((head,guard,odd))
F={};target=(0,0,0);tg,to,tt=T[target,TARGET]
for c in contexts:
 if (c,TARGET) in CT:
  nc=CT[c,TARGET];dest=NEXT[target,TARGET][0]
  root=bb.intersect(tg,color_guard(target,c))
  root=bb.intersect(root,bb.flip(color_guard(dest,nc),to))
  if root:F[target,c]=root
queue=deque(F);queued=set(queue);iters=0;t0=time.time()
while queue:
 key=queue.popleft();queued.remove(key);head,ctx=key;iters+=1
 if bb.intersect(F[key],SOURCE.get(key,0)):
  print('ABSTRACT WITNESS COMPACT',ALPHA,TARGET,R,q,'iterations',iters,'bddnodes',len(bb.nodes),'time',time.time()-t0,flush=True);break
 if len(bb.nodes)>100000 and iters%500==0:
  before=len(bb.nodes);roots=list(F.values())+list(SOURCE.values())+list(G.values())+[x[0] for x in T.values()]
  mp=bb.collect(roots)
  F={h:mp[v] for h,v in F.items()};SOURCE={h:mp[v] for h,v in SOURCE.items()};G={h:mp[v] for h,v in G.items()}
  T={hk:(mp[g],odd,t) for hk,(g,odd,t) in T.items()}
  REV={hk:[(ph,mp[g],odd) for ph,g,odd in prev] for hk,prev in REV.items()}
  print('GC',iters,before,'->',len(bb.nodes),'elapsed',round(time.time()-t0,1),flush=True)
  if len(bb.nodes)>LIMIT:print('LIVE NODE CAP',len(bb.nodes),'iterations',iters,flush=True);break
 for pc,k in INCOMING[ctx]:
  for ph,guard,odd in REV[head,k]:
   root=bb.intersect(bb.flip(F[key],odd),guard)
   root=bb.intersect(root,color_guard(ph,pc))
   if not root:continue
   pkey=(ph,pc);old=F.get(pkey,0);new=bb.union(old,root)
   if new!=old:
    F[pkey]=new
    if pkey not in queued:queued.add(pkey);queue.append(pkey)
else:print('EXCLUDED COMPACT',ALPHA,TARGET,R,q,'cells',len(P),'heads',len(heads),'contexts',len(contexts),'iterations',iters,'bddnodes',len(bb.nodes),'fullcolorstates',sum(bb.count(v) for v in F.values()),'time',time.time()-t0,flush=True)
'''
p.with_name('bdd_macro_compact_backward.py').write_text(prefix+body)
