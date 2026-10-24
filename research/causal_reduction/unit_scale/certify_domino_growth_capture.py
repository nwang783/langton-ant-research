"""Exact all-r and all-future read/color check for one frozen counted-word candidate.
No bounded-repeat observation is treated as proof. Every read-family domain is
Presburger, and all prior reads at that same cell are XORed before its turn.
"""
from pathlib import Path
import sys,json,time,hashlib
HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from probe_domino_growth_capture import trajectory
D=((0,1),(1,0),(0,-1),(-1,0))
def af(v):return f'({v[0]}*r+{v[1]})'
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def trace(w,h):
 p=(0,0);rows=[]
 for j,c in enumerate(w):
  rows.append((p,h,c));h=(h+(1 if c=='R' else -1))%4;p=tuple(p[i]+D[h][i] for i in (0,1))
 return rows,p,h

def compile_candidate(ctx,R=20):
 template=json.loads(HERE.joinpath('probe_domino_growth_capture.json').read_text())['cases'][0]
 rs=template['r'];sample,_,_=trajectory(rs,60*rs+777+104);tail=sample[-104:]
 stages=[]
 for s in template['segments']:
  if s['cap']:stages.append((s['cap'],0,1))
  stages.append((s['word'],1,s['count_offset']))
 stages.append((template['tail'],0,1))
 families=[];p=((0,0),(0,0));tm=(0,0);h=1
 for stage,(w,ca,cb) in enumerate(stages+[(tail,None,None)]):
  rows,dr,hh=trace(w,h);L=len(w)
  repeated=ca!=0
  if repeated:assert hh==h and dr!=(0,0)
  if ca is None:
   assert p==((2,2),(0,7)) and tm==(60,777) and h==0
   assert dr==(-2,2) and hh==0
  for j,(off,head,turn) in enumerate(rows):
   start=tuple((p[i][0],p[i][1]+off[i]) for i in (0,1))
   if repeated:
    bound='k>=0' if ca is None else f'0<=k<{ca}*r+{cb}'
    dom=f'r>={R} and exists(k: {bound} and x={af(start[0])}+{dr[0]}*k and y={af(start[1])}+{dr[1]}*k)'
    axis=0 if dr[0] else 1;assert L%dr[axis]==0
    scale=L//dr[axis];coord='xy'[axis]
    coeff=(tm[0]-scale*start[axis][0],scale if axis==0 else 0,scale if axis==1 else 0,tm[1]+j-scale*start[axis][1])
   else:
    dom=f'r>={R} and x={af(start[0])} and y={af(start[1])}'
    coeff=(tm[0],0,0,tm[1]+j)
   ty='tail' if ca is None else 'horizontal'
   sig=(start[0][0]%2,start[0][1]%2,start[1][1]) if ty=='horizontal' else (sum(z[0] for z in start),sum(z[1] for z in start),start[1][1]%2)
   families.append(dict(stage=stage,slot=j,turn=turn,domain=ctx.set('[r]->{[x,y]:'+dom+'}'),formula=dom,time=coeff,type=ty,sig=sig))
  if ca is None:break
  p=tuple((p[i][0]+ca*dr[i],p[i][1]+cb*dr[i]) for i in (0,1));tm=(tm[0]+ca*L,tm[1]+cb*L);h=hh
 return families,stages,tail

def compatible(a,b):
 if a['type']==b['type']:return a['sig']==b['sig']
 return True

def main():
 start=time.monotonic();ctx=Context(max_operations=50000000);R=20
 F,stages,tail=compile_candidate(ctx,R)
 initial=ctx.set(f'[r]->{{[x,y]:r>={R} and ((y=0 and 0<=x<=2r) or (x=-1 and y=1))}}')
 failures=[];pairs=0;nonempty=0
 for i,f in enumerate(F):
  ctx.reset_operations();current=initial.intersect(f['domain'])
  for j,g in enumerate(F):
   if i==j or not compatible(f,g):continue
   pairs+=1;d=f['domain'].intersect(g['domain'])
   if d.is_empty():continue
   diff=tuple(g['time'][a]-f['time'][a] for a in range(4))
   cond=f'{diff[0]}*r+{diff[1]}*x+{diff[2]}*y+{diff[3]}<0'
   prior=d.intersect(ctx.set('[r]->{[x,y]:'+cond+'}'))
   if not prior.is_empty():current=xor(current,prior);nonempty+=1
  bad=f['domain'].subtract(current) if f['turn']=='L' else current
  if not bad.is_empty():
   failures.append(dict(family=i,stage=f['stage'],slot=f['slot'],bad=str(bad.coalesce())))
   print('FAIL',failures[-1],flush=True);break
  if i%100==0:print('checked',i,'/',len(F),'pairs',pairs,'seconds',round(time.monotonic()-start,2),flush=True)
 out=dict(status='EXACT_ALL_PARAMETER_ALL_FUTURE_LEGAL' if not failures else 'FAILED',
  scope='One specified seed family J_r for every integer r>=20, seven finite counted arms followed by the stated infinite104 word.',
  minimum_r=R,families=len(F),candidate_pairs=pairs,nonempty_prior_relations=nonempty,failures=failures,
  stages=[dict(word=w,count_r=a,count_constant=b) for w,a,b in stages],infinite_tail_word=tail,
  tail_start_time='60*r+777',tail_start_pose=['2*r+2',7,'N'],tail_period=104,tail_drift=[-2,2],
  seconds=time.monotonic()-start,isl_version=ctx.version,
  checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 HERE.joinpath('domino_growth_capture_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('stages','infinite_tail_word')},indent=2))
if __name__=='__main__':main()
