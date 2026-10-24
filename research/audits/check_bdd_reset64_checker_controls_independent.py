from pathlib import Path
import random,subprocess,json,tempfile
A=Path(__file__).resolve().parent; rng=random.Random(915);total=0
with tempfile.TemporaryDirectory(dir=A)as tmp:
 p=Path(tmp)
 for case in range(100):
  n=42;np=4;active=[0,7,31,40,41];encode=lambda x:sum(((x>>i)&1)<<b for i,b in enumerate(active));inactive=((1<<n)-1)^encode(31);sk=inactive|encode(rng.randrange(32));sv=encode(rng.randrange(32))&sk;sp=rng.randrange(3)
  ts=[]
  for _ in range(15):
   k=encode(rng.randrange(32));v=encode(rng.randrange(32))&k;reset=encode(rng.randrange(32));rv=encode(rng.randrange(32))&reset;ts.append((rng.randrange(3),rng.randrange(3),k,v,encode(rng.randrange(32)),reset,rv,0,0))
  ts.append((3,3,0,0,0,0,0,1,0));re=[rng.randrange(3)]
  reach=[set()for _ in range(np)];reach[sp]={encode(s) for s in range(32)if encode(s)&sk==sv}
  while True:
   old=sum(map(len,reach))
   for s,d,k,v,f,reset,rv,g,a in ts:
    if not g:reach[d].update(((x^f)&~reset)|rv for x in tuple(reach[s])if x&k==v)
   for d in re:reach[d]|=reach[-1]
   if sum(map(len,reach))==old:break
  data=f'{n} {np} {len(ts)} {len(re)}\n{sp} {sk} {sv}\n'+'\n'.join(' '.join(map(str,t))for t in ts)+'\n'+' '.join(map(str,re))+'\n';(p/'g').write_text(data)
  def cert(sets):
   nodes=[(n,0,0),(n,1,1)];intern={}
   def build(S,v):
    if not S:return 0
    if v==n:return 1
    l=build({x for x in S if not(x>>v)&1},v+1);h=build({x for x in S if(x>>v)&1},v+1)
    if l==h:return l
    key=(v,l,h)
    if key not in intern:intern[key]=len(nodes);nodes.append(key)
    return intern[key]
   roots=[build(S,0)for S in sets]
   (p/'b').write_text(f'{n} {np} {len(nodes)}\n'+'\n'.join(' '.join(map(str,z))for z in nodes)+'\n'+' '.join(map(str,roots))+'\n')
  cert(reach);r=subprocess.run([str(A/'check_guarded_reset_bdd64_invariant_independent'),str(p/'g'),str(p/'b'),str(p/'out')],capture_output=True,text=True);assert r.returncode==0,r.stderr
  out=json.loads((p/'out').read_text());assert out['invariant_states']==sum(map(len,reach));total+=out['checks']
  # Negative control deliberately deletes a permitted initial assignment.
  bad=[S.copy()for S in reach];bad[sp].remove(sv);cert(bad)
  r=subprocess.run([str(A/'check_guarded_reset_bdd64_invariant_independent'),str(p/'g'),str(p/'b'),str(p/'out')],capture_output=True,text=True);assert r.returncode!=0 and 'initial cube missing' in r.stderr
out={'status':'PASS','independent_explicit_graph_controls':100,'rejected_initial_cube_mutations':100,'positive_checks':total}
(A/'bdd_reset64_checker_controls_independent.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
