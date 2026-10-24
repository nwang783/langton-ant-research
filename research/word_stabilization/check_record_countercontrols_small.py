from pathlib import Path
import json,subprocess
R=Path(__file__).resolve().parents[1];D=R/'core_periodicity_new/chronology_dcuv';G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];keep=[0,1,4,5,6,7,8,9];A=[0,22,20,10];depth=5;counts=[1]+[0]*depth;best=-999;attempts=0;events=[]
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def rk(z,h):x,y=rot(z,h);return 2*(x+y)
def at(p,z):x,y=rot(z,p[2]);return p[0]+x,p[1]+y
def trace(board,p,word):
 b=board.copy();x,y,h=p
 for turn in word:
  need=turn=='L';q=x,y
  if q in b and b[q]!=need:return None
  b[q]=not need;h=(h+(-1 if need else 1))%4;dx,dy=[(0,1),(1,0),(0,-1),(-1,0)][h];x+=dx;y+=dy
 return b,(x,y,h)
def go(board,p,prod,C,Q,path,pending):
 global best,attempts
 if len(path)==depth:return
 for a in keep:
  attempts+=1;t=trace(board,p,G[a]['word'])
  if t is None:continue
  b,pe=t
  if trace(b,pe,'LLLLRLRRRRL')is None:continue
  counts[len(path)+1]+=1
  for e in pending:
   if e>best:best=e;events.append({'required_I':e,'path':path+[a]})
  inp={at(p,q)for q in G[a]['inputs']};out={at(p,q)for q in G[a]['outputs']};qq=[max([Q[h]]+[rk(q,h)for q in inp-prod])for h in range(4)];peak=[rk(pe[:2],h)+A[(pe[2]+h)%4]for h in range(4)];pending2=[peak[h]-qq[h]for h in range(4)if peak[h]>C[h]];cc=[max(C[h],peak[h])for h in range(4)];go(b,pe,(prod-inp)|out,cc,qq,path+[a],pending2)
go({},(0,0,0),set(),A,[-1000000]*4,[],[])
z=subprocess.run([str(D/'search_record_countercontrols'),str(depth),'100000','10000000'],text=True,capture_output=True,check=True);summary=json.loads([x[8:]for x in z.stdout.splitlines()if x.startswith('SUMMARY ')][0]);assert summary['counts']==counts,(summary,counts);assert summary['attempts']==attempts;assert summary['max_required_I']==best
J={'status':'PASS','depth':depth,'counts':counts,'attempts':attempts,'maximum_required_I':best,'events':events,'scope':'Fresh current-color tracing and ordered residual remove/install, compared to last-turn alternating trace/full-context label engine.'};(R/'word_stabilization/record_countercontrols_small_independent.json').write_text(json.dumps(J,indent=2)+'\n');print(json.dumps(J))
