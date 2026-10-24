from pathlib import Path
p=Path('/workspace/shared/langton/word_stabilization/bdd_macro_compact_backward.py');s='from pathlib import Path\n'+p.read_text();s=s.replace('T={};NEXT={};SOURCE={}', 'T={};NEXT={};SOURCE={};SOURCEREC=[]')
s=s.replace('key=(to,nc);SOURCE[key]=bb.union(SOURCE.get(key,0),root)', 'key=(to,nc);SOURCE[key]=bb.union(SOURCE.get(key,0),root);SOURCEREC.append((key,head,k,pc,root))')
s=s.replace('F={};target=', 'F={};VERS=[];FV={};target=')
s=s.replace('if root:F[target,c]=root', "if root:\n   key=(target,c);F[key]=root;FV[key]=len(VERS);VERS.append((root,key,None,None,None))")
a=s.index('while queue:');s=s[:a]+'''def member(root,color):
 while root>1:
  var,lo,hi=bb.nodes[root];root=hi if (color>>var)&1 else lo
 return bool(root)
def sample(root):
 color=0
 while root>1:
  var,lo,hi=bb.nodes[root]
  if lo:root=lo
  else:color|=1<<var;root=hi
 return color
def witness(key):
 color=sample(bb.intersect(F[key],SOURCE.get(key,0)));v=FV[key];steps=[]
 start=[key,color]
 src=next((h,k,pc) for skey,h,k,pc,root in SOURCEREC if skey==key and member(root,color))
 while True:
  root,node,old,child,act=VERS[v];assert member(root,color)
  if act is None:break
  if old is not None and member(VERS[old][0],color):v=old;continue
  k,odd=act;nextkey=VERS[child][1];steps.append([node,nextkey,k,color,color^odd]);color^=odd;v=child
 word=src[1]+''.join(x[2] for x in steps)+TARGET
 actual=src[0];geometry=[]
 allsteps=[(src[0],key[0],src[1])]+[(a[0],b[0],k) for a,b,k,c,d in steps]
 for ph,to,k in allsteps:
  _,(da,db,eh)=zero[actual[2],k];actual=(actual[0]+da,actual[1]+db,eh)
  if clip(*actual)!=to:geometry.append({'macro':k,'actual_after':actual,'abstract_after':to})
 out={'status':'Abstract compactification witness, not a physical counterexample','source':src,'start':start,'steps':steps,'final':VERS[v][1],'word':word,'geometry_mismatches':geometry,'target':TARGET,'patch':P}
 path=Path(__file__).with_name('compact_witness_'+TARGET+'_'+str(len(P))+'_'+Path(PORT_FILE).stem+'.json');path.write_text(json.dumps(out,indent=2));print('WITNESS',word,'geometry_mismatches',len(geometry),'file',path,flush=True)
''' +s[a:]
s=s.replace("print('ABSTRACT WITNESS COMPACT'","witness(key);print('ABSTRACT WITNESS COMPACT'")
a=s.index(' if len(bb.nodes)>100000');b=s.index(' for pc,k in INCOMING[ctx]:',a);s=s[:a]+" if len(bb.nodes)>LIMIT:print('CREATED NODE CAP',len(bb.nodes),'iterations',iters,flush=True);break\n"+s[b:]
s=s.replace('F[pkey]=new', "oldver=FV.get(pkey);childver=FV[key];FV[pkey]=len(VERS);VERS.append((new,pkey,oldver,childver,(k,odd)));F[pkey]=new")
p.with_name('bdd_macro_compact_trace.py').write_text(s)
