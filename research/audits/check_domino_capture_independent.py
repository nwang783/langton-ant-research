"""Independent parameter/index Presburger check. No author family code or pruning.
Every ordered pair of literal read slots is tested directly with both repeat
indices; no spatial compatibility signature or inverse-time formula is used.
"""
from pathlib import Path
import json,sys,time,hashlib
B=Path('/workspace/shared/langton'); src=B/'causal_reduction/unit_scale/domino_growth_capture_certificate.json'
sys.path.insert(0,str(B/'sources/kehao95-core/defect_synthesis/verification/presburger_defects'))
from isl_exact import Context

def xy(z): return (round(z.real),round(z.imag))
def lin(c,vars):
 return '('+'+'.join(f'{v}*{name}' for v,name in zip(c,vars))+')'
def main():
 start=time.monotonic(); data=json.loads(src.read_text()); ctx=Context(max_operations=100000000)
 assert data['minimum_r']==20
 fam=[]; pos=[0j,0j]; clock=[0,0]; heading=1+0j
 stages=data['stages']+[dict(word=data['infinite_tail_word'],count_r=None,count_constant=None)]
 for s,stage in enumerate(stages):
  word=stage['word']; a,b=stage['count_r'],stage['count_constant']; h=heading; d=0j; slots=[]
  assert word and set(word)<=set('RL')
  for j,c in enumerate(word):
   slots.append((d,c,j)); h*=(-1j if c=='R' else 1j); d+=h
  if a is None:
   assert xy(pos[0])==(2,0) and xy(pos[1])==(2,7) and clock==[60,777] and heading==1j
   assert len(word)==104 and d==-2+2j and h==heading
  elif a:
   assert a*20+b>0 and a>=0 and h==heading and d!=0
  else: assert b==1
  for off,c,j in slots:
   xr,yr=xy(pos[0]); xc,yc=xy(pos[1]+off); dx,dy=xy(d)
   fam.append(dict(x=(xr,dx,xc),y=(yr,dy,yc),t=(clock[0],len(word),clock[1]+j),a=a,b=b,c=c,s=s,j=j))
  if a is None:break
  pos=[pos[0]+a*d,pos[1]+b*d]; clock=[clock[0]+a*len(word),clock[1]+b*len(word)]; heading=h
 assert len(fam)==973
 def bound(f,v):
  return f'{v}>=0' if f['a'] is None else f'0<={v}<{f["a"]}*r+{f["b"]}'
 empty=ctx.set('{[r,k]:false}'); pairs=hits=0; records=[]
 for i,f in enumerate(fam):
  ctx.reset_operations(); base=f'r>=20 and {bound(f,"k")}'
  dom=ctx.set('{[r,k]:'+base+'}')
  x,y,t=[lin(f[key],['r','k','1']) for key in ('x','y','t')]
  color=ctx.set('{[r,k]:'+base+f' and (({y}=0 and 0<={x}<=2*r) or ({x}=-1 and {y}=1))'+'}')
  for g in fam:
   X,Y,T=[lin(g[key],['r','l','1']) for key in ('x','y','t')]
   prior=ctx.set('{[r,k]:'+base+' and exists(l:'+bound(g,'l')+f' and {X}={x} and {Y}={y} and {T}<{t})'+'}')
   pairs+=1
   if not prior.is_empty():
    hits+=1; color=color.subtract(prior).union(prior.subtract(color)).coalesce()
  bad=dom.subtract(color) if f['c']=='L' else color
  assert bad.is_empty(),(i,str(bad))
  records.append(dict(family=i,stage=f['s'],slot=f['j'],turn=f['c'],bad_empty=True))
  if i%100==0: print('checked',i,'pairs',pairs,'seconds',round(time.monotonic()-start,2),flush=True)
 # Direct finite-board controls, independently following actual turns.
 controls=[]
 for r in (20,21,40,100,1000):
  board={(x,0) for x in range(2*r+1)}|{(-1,1)}; p=0j;h=1+0j;n=0
  for s,st in enumerate(stages):
   count=100 if st['count_r'] is None else st['count_r']*r+st['count_constant']
   if st['count_r'] is None: assert (n,xy(p),h)==(60*r+777,(2*r+2,7),1j)
   for _ in range(count):
    for c in st['word']:
     q=xy(p); assert (q in board)==(c=='L'),(r,n,c)
     if q in board:board.remove(q)
     else:board.add(q)
     h*=(-1j if c=='R' else 1j);p+=h;n+=1
  controls.append(dict(r=r,reads=n,tail_periods=100))
 out=dict(status='PASS',scope='Specified J_r seed, every integer r>=20 and every future read; no compatibility filtering.',candidate_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),families=len(fam),all_ordered_pairs=pairs,nonempty_prior_relations=hits,tail_time=[60,777],tail_pose=[[2,2],[0,7],'N'],tail_period=104,tail_drift=[-2,2],controls=controls,records=records,seconds=time.monotonic()-start)
 outpath=Path(__file__).with_suffix('.json');outpath.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
