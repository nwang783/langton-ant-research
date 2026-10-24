"""Exact all-(r,k), all-future capture check for one explicit chamfered seed family.
Candidate selection is finite discovery. The chronology check is unbounded.
"""
from pathlib import Path
import sys,json,hashlib,time
HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
D=((0,1),(1,0),(0,-1),(-1,0))
def expr(v):return f'({v[0]}*r+{v[1]})'
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def trace(w,h):
 p=(0,0);out=[]
 for c in w:
  out.append((p,c));h=(h+(1 if c=='R'else -1))%4;p=tuple(p[i]+D[h][i]for i in(0,1))
 return out,p,h

def main():
 st=time.monotonic();ctx=Context(max_operations=100000000)
 sample=next(z for z in json.loads(HERE.joinpath('probe_chamfered_continuation.json').read_text())if z['r']==20 and z['k']==20);w=sample['word'];end=20*20+287
 P=w[:50];V=w[50:70];C=w[50+20*19:end];H=w[end:end+104]
 assert len(C)==257 and len(H)==104 and w[:end+104]==P+V*19+C+H
 stages=[(P,0,1),(V,1,-1),(C,0,1),(H,None,None)];F=[];p=((0,0),(0,0));tm=(0,0);h=1;tail_pose=None;tail_drift=None
 for stage,(word,ca,cb)in enumerate(stages):
  rr,delta,hh=trace(word,h);L=len(word)
  if ca!=0:assert hh==h and delta!=(0,0)
  if ca is None:tail_pose=[list(p[0]),list(p[1]),h];tail_drift=delta;assert tm==(20,287)
  for j,(off,turn)in enumerate(rr):
   start=tuple((p[i][0],p[i][1]+off[i])for i in(0,1))
   if ca!=0:
    bound='i>=0'if ca is None else f'0<=i<{ca}*r+{cb}'
    dom=f'r>=10 and k>=10 and exists(i:{bound} and x={expr(start[0])}+{delta[0]}*i and y={expr(start[1])}+{delta[1]}*i)'
    axis=0 if delta[0] else 1;assert L%delta[axis]==0;scale=L//delta[axis]
    tf=(tm[0]-scale*start[axis][0],scale if axis==0 else 0,scale if axis==1 else 0,tm[1]+j-scale*start[axis][1])
   else:dom=f'r>=10 and k>=10 and x={expr(start[0])} and y={expr(start[1])}';tf=(tm[0],0,0,tm[1]+j)
   F.append(dict(stage=stage,slot=j,turn=turn,domain=ctx.set('[r,k]->{[x,y]:'+dom+'}'),time=tf))
  if ca is None:break
  p=tuple((p[i][0]+ca*delta[i],p[i][1]+cb*delta[i])for i in(0,1));tm=(tm[0]+ca*L,tm[1]+cb*L);h=hh
 initial=ctx.set(json.loads(HERE.joinpath('chamfered_frames_certificate.json').read_text())['output_relation'])
 failures=[];pairs=0;nonempty=0
 for i,f in enumerate(F):
  ctx.reset_operations();current=initial.intersect(f['domain'])
  for j,g in enumerate(F):
   if i==j:continue
   pairs+=1;z=f['domain'].intersect(g['domain'])
   if z.is_empty():continue
   dt=tuple(g['time'][a]-f['time'][a]for a in range(4));prior=z.intersect(ctx.set(f'[r,k]->{{[x,y]:{dt[0]}*r+{dt[1]}*x+{dt[2]}*y+{dt[3]}<0}}'))
   if not prior.is_empty():current=xor(current,prior);nonempty+=1
  bad=f['domain'].subtract(current)if f['turn']=='L'else current
  if not bad.is_empty():failures.append(dict(family=i,stage=f['stage'],slot=f['slot'],bad=str(bad.coalesce())));break
 result=dict(status='EXACT_ALL_PARAMETER_ALL_FUTURE_LEGAL'if not failures else'FAILED',domain='integers r>=10,k>=10',initial='complete O_(r,k) after the self-avoiding frame, head(0,0,E)',families=len(F),ordered_distinct_pairs=pairs,nonempty_prior_relations=nonempty,failures=failures,words=dict(P=P,V=V,C=C,H=H),continuation='P V^(r-1) C H^infinity',tail_time_after_frame='20r+287',tail_time_from_original_seed='36r+8k+291',tail_pose_coefficients=tail_pose,tail_period=104,tail_drift=tail_drift,seconds=time.monotonic()-st,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),isl_version=ctx.version)
 HERE.joinpath('chamfered_capture_certificate.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='words'},indent=2))
if __name__=='__main__':main()
