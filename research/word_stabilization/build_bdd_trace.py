from pathlib import Path
p=Path('/workspace/shared/langton/word_stabilization/bdd_macro_colored_ports_trap.py');s=p.read_text()
s=s.replace("F={};initial={};T={};BOUND=", "SOURCES={}\nF={};initial={};T={};BOUND=")
s=s.replace('def put_initial(head,ctx,root):','def put_initial(head,ctx,root,origin):')
s=s.replace('key=(head,ctx);initial[key]=bb.union(initial.get(key,0),root)','key=(head,ctx);initial[key]=bb.union(initial.get(key,0),root);SOURCES.setdefault(key,[]).append((root,origin))')
s=s.replace('put_initial(to,ctx,root)','put_initial(to,ctx,root,(head,k))')
a=s.index('F=dict(initial);queue=');s=s[:a]+'''# Version DAG retains a constructive abstract path for every added color.
F=dict(initial);versions=[];VID={}
for key,root in F.items():
 VID[key]=len(versions);versions.append((key,root,None))
def pick(root):
 color=0
 while root>=2:
  v,l,h=bb.nodes[root]
  if l:root=l
  else:color|=1<<v;root=h
 assert root==1
 return color

def witness(key,color):
 ver=VID[key];back=[]
 while True:
  key,root,event=versions[ver]
  assert bb.evaluate(root,color)
  if event is None:
   source=next(origin for r,origin in SOURCES[key] if bb.evaluate(r,color))
   sh,sk=source
   back.append({'from':sh,'to':key[0],'macro':sk,'color_after':color,'source':True})
   break
  old,src,k=event
  if old is not None and bb.evaluate(versions[old][1],color):ver=old;continue
  skey,sroot,_=versions[src]
  back.append({'from':skey[0],'to':key[0],'macro':k,'color_after':color,'source':False})
  if skey[0][0]!='OUT':color^=T[skey[0],k][2]
  assert bb.evaluate(sroot,color)
  ver=src
 steps=list(reversed(back));word=''.join(x['macro'] for x in steps)+TARGET
 actual=tuple(steps[0]['from']);mismatches=[]
 for i,step in enumerate(steps):
  tr,actual=trace(actual,step['macro'])
  expected=tuple(step['to'])
  if expected[0]!='OUT' and actual!=expected:mismatches.append([i,actual,expected])
 print('ABSTRACT WORD',word,'steps',len(steps),'POSE MISMATCHES',mismatches,flush=True)
 out={'alphabet':ALPHA,'target':TARGET,'q':q,'patch':P,'word':word,'steps':steps,'mismatches':mismatches}
 path='/workspace/shared/langton/word_stabilization/abstract_witness_'+TARGET+'_'+str(len(P))+'.json'
 json.dump(out,open(path,'w'),indent=2)
 print('SAVED',path,flush=True)

queue=deque(F);queued=set(queue);iters=0;t0=time.time()
while queue:
 key=queue.popleft();queued.remove(key);head,ctx=key;iters+=1;svid=VID[key];source_root=F[key]
 if len(bb.nodes)>LIMIT:
  print('NODE CAP',len(bb.nodes),'iterations',iters,flush=True);break
 images=[]
 for k in ALPHA:
  nc=CT.get((ctx,k))
  if nc is None:continue
  if head[0]=='OUT':
   oldh=head[1];_,(_,_,newh)=zero[oldh,k]
   images.append(((('OUT',newh),nc),source_root,k))
   images.extend(((to,nc),source_root,k) for to in BOUND[oldh,k])
  else:
   to,guard,odd,touches=T[head,k];target=head==(0,0,0) and k==TARGET
   if touches and not target:continue
   pre=bb.intersect(source_root,guard)
   if target and pre:
    print('ABSTRACT WITNESS',ALPHA,TARGET,R,q,'iterations',iters,'bddnodes',len(bb.nodes),'time',time.time()-t0,flush=True)
    witness(key,pick(pre));break
   if pre:images.append(((to,nc),bb.flip(pre,odd),k))
 else:
  for to,img,k in images:
   img=bb.intersect(img,color_guard(*to))
   if not img:continue
   old=F.get(to,0);new=bb.union(old,img)
   if new!=old:
    oldvid=VID.get(to);VID[to]=len(versions);versions.append((to,new,(oldvid,svid,k)));F[to]=new
    if to not in queued:queued.add(to);queue.append(to)
  continue
 break
else:print('EXCLUDED',ALPHA,TARGET,R,q,'cells',len(P),'heads',len(heads),'contexts',len(contexts),'iterations',iters,'bddnodes',len(bb.nodes),'fullcolorstates',sum(bb.count(v) for v in F.values()),'time',time.time()-t0,flush=True)
'''
p.with_name('bdd_macro_trace_ports.py').write_text(s)
