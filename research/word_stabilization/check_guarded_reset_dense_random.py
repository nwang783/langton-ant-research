import random,subprocess,tempfile,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];B=R/'core_periodicity_new';rng=random.Random(634020);results=[]
with tempfile.TemporaryDirectory()as td:
 for case in range(250):
  n=rng.randrange(1,9);np=rng.randrange(2,8);mask=(1<<n)-1;start=(rng.randrange(np-1),rng.randrange(mask+1),0);start=(start[0],start[1],rng.randrange(mask+1)&start[1]);edges=[]
  for _ in range(rng.randrange(2,30)):
   p=rng.randrange(np-1);q=rng.randrange(np);k=rng.randrange(mask+1);v=rng.randrange(mask+1)&k;f=rng.randrange(mask+1);c=rng.randrange(mask+1);reset=rng.randrange(mask+1)&c;goal=int(rng.random()<.08);edges.append((p,q,k,v,f,c,reset,goal,len(edges)))
  re=sorted(rng.sample(range(np-1),rng.randrange(np)));fn=Path(td)/'model.dat';fn.write_text(f'{n} {np} {len(edges)} {len(re)}\n'+ ' '.join(map(str,start))+'\n'+'\n'.join(' '.join(map(str,e))for e in edges)+'\n'+' '.join(map(str,re))+'\n')
  seen={(start[0],c)for c in range(mask+1)if(c&start[1])==start[2]};fr=set(seen);hit=False
  while fr and not hit:
   nx=set()
   for p,c in fr:
    if p==np-1:nx|={(q,c)for q in re}
    else:
     for e in edges:
      a,b,k,v,f,cl,r,g,_=e
      if a!=p or(c&k)!=v:continue
      if g:hit=True;break
      nx.add((b,((c^f)&~cl)|(r&cl)))
    if hit:break
   fr=nx-seen;seen|=fr
  z=subprocess.run([str(B/'guarded_reset_dense'),str(fn)],capture_output=True,text=True,check=True);lines=z.stdout.splitlines();assert('ABSTRACT_WITNESS'in lines[0])==hit,(case,z.stdout)
  if not hit:assert int(lines[0].split()[3])==len(seen),(case,len(seen),z.stdout)
  else:
   rows=[tuple(map(int,l.split()[1:]))for l in lines[1:]];assert rows;assert rows[0][0]==start[0]and(rows[0][1]&start[1])==start[2]
   for (p,c,a),(q,cc,_)in zip(rows,rows[1:]):
    if a==99:assert p==np-1 and q in re and c==cc
    else:assert any(e[0]==p and e[1]==q and e[8]==a and not e[7]and(c&e[2])==e[3]and(((c^e[4])&~e[5])|(e[6]&e[5]))==cc for e in edges),(case,p,c,a,q,cc)
   p,c,a=rows[-1];assert any(e[0]==p and e[8]==a and e[7]and(c&e[2])==e[3]for e in edges)
  results.append({'case':case,'n':n,'poses':np,'hit':hit})
O={'status':'PASS','controls':len(results),'seed':634020,'cases':results};(R/'word_stabilization/guarded_reset_dense_random_controls.json').write_text(json.dumps(O,indent=2)+'\n');print('PASS',len(results))
