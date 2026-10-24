"""Author finite controls comparing the cube-set engine to explicit BFS."""
from pathlib import Path
from collections import deque
import json,random,subprocess,tempfile
W=Path(__file__).resolve().parent;R=random.Random(202610230811);cases=[]
with tempfile.TemporaryDirectory(prefix='monitor_controls_',dir='/tmp')as tmp:
 D=Path(tmp)
 for seed in range(300):
  cb=2;qs=2;qb=1;ash=3;n=6;np=4;ns=3;high=[R.randrange(2)for _ in range(np)];high[-1]=0
  mt=[[R.randrange(-1,ns)for _ in range(8)]for _ in range(ns)]
  # Every actual packet has a legal fresh-state transition, as for the
  # forbidden length6 monitor used by the pilot.
  mt[0]=[R.randrange(ns)for _ in range(8)]
  sp=0;sv=R.randrange(4)|(R.randrange(2)<<qs)|(R.randrange(5)<<ash);E=[]
  for j in range(R.randrange(3,16)):
   fr=R.randrange(np-1);to=R.randrange(np-1);goal=int(R.randrange(7)==0);a=R.choice([0,1,4,5,6,7,8,9,99,104])if not goal else R.choice([0,1,4,5,6,7,8,9]);k=R.randrange(4);v=R.randrange(4)&k;x=R.randrange(4);clear=R.randrange(4);reset=R.randrange(4)&clear
   if R.randrange(2):k|=1<<qs;v|=R.randrange(2)<<qs
   if R.randrange(2):clear|=1<<qs;reset|=R.randrange(2)<<qs
   if R.randrange(2):k|=7<<ash;v|=R.randrange(5)<<ash
   if R.randrange(2):clear|=7<<ash;reset|=R.randrange(5)<<ash
   E.append([fr,to,k,v,x,clear,reset,goal,a])
  if not any(e[7]for e in E):E[-1][7]=1;E[-1][8]=0
  keep=[0,1,4,5,6,7,8,9];pa={a:i for i,a in enumerate(keep)}
  def advance(e,m):
   fr,to,*_=e;a=e[8]
   if e[7]:return mt[m][pa[a]]
   if a in[99,104]:return 0
   if not high[fr]or not high[to]:return mt[0][pa[a]]if high[to]else 0
   return mt[m][pa[a]]
  seen={(sp,sv,0)};todo=deque(seen);actual=False
  while todo and not actual:
   p,val,m=todo.popleft()
   for e in E:
    if e[0]!=p or(val&e[2])!=e[3]:continue
    mm=advance(e,m)
    if mm<0:continue
    if e[7]:actual=True;break
    vv=((val^e[4])&~e[5])|(e[6]&e[5]);assert((vv>>ash)&7)<=4;z=(e[1],vv,mm)
    if z not in seen:seen.add(z);todo.append(z)
  dat=D/'toy.dat';mon=D/'toy.mon';pre=D/'out'
  with dat.open('w')as f:
   f.write(f'{n} {np} {len(E)} 0\n{sp} {(1<<n)-1} {sv}\n');f.writelines(' '.join(map(str,e))+'\n'for e in E);f.write('\n')
  with mon.open('w')as f:
   f.write(f'{np} {ns} 0\n'+' '.join(map(str,high))+'\n');f.writelines(' '.join(map(str,r))+'\n'for r in mt)
  out=subprocess.check_output([str(W/'record_color_Q_clock_monitor_backward'),str(dat),str(cb),str(qs),str(qb),'1',str(ash),'20000',str(pre),str(mon)],text=True,stderr=subprocess.DEVNULL)
  if 'CUBE_EXHAUSTED_NO_INITIAL'in out:assert not actual,(seed,out)
  if 'CONCRETE_MODEL_WITNESS'in out:assert actual,(seed,out)
  assert 'CAP'not in out,(seed,out)
  cases.append(dict(seed=seed,explicit_hit=actual,cube_status=out.splitlines()[-1],explicit_reached=len(seen)))
O=dict(status='AUTHOR_FINITE_CONTROLS_PASS_NOT_INDEPENDENT',cases=len(cases),explicit_hits=sum(c['explicit_hit']for c in cases),cube_exhaustions=sum('CUBE_EXHAUSTED'in c['cube_status']for c in cases),concrete_hits=sum('CONCRETE_MODEL_WITNESS'in c['cube_status']for c in cases),spurious_unlifted=sum('NOT_CONCRETELY'in c['cube_status']or'GOAL_NOT_LIFTED'in c['cube_status']for c in cases),controls=cases)
(W/'chronology_dcuv/u1_exact_low_color_Q/monitor_engine_controls.json').write_text(json.dumps(O,indent=2)+'\n');print({k:v for k,v in O.items()if k!='controls'})
