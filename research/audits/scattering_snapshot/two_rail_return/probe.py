"""Discovery only: two clean U-turn crossing rules with full finite history."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'transverse'))
import crossing as c
sys.path.insert(0,str(Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation')))
from ant_exact import step,certify_period,PHASES
rows=json.loads((HERE.parent/'transverse/crossings_discovery.json').read_text())
row=next(r for r in rows if (r['rotation'],r['a'],r['s'])==(3,0,1))
assert row['cert']['phase']==39
REF=(c.WORD*((row['t0']+103)//104))[:row['t0']]+row['word'][:-39]
assert len(REF)==21224
rr,alpha,eh=c.trace(REF);assert alpha==(-44,-2) and eh==(c.H0+2)%4
_,_,_,STATIC=c.first_contact(3,0,1)

def seed(k,M=80):
 one={c.plus(c.plus(b,c.times(k,c.D)),c.times(j,e)) for b,e,_,_ in STATIC for j in range(-M,M+1)}
 two={c.plus(alpha,c.rotate(c.plus(b,c.times(j,e)),2)) for b,e,_,_ in STATIC for j in range(-M,M+1)}
 B=set(map(tuple,c.DATA['seed']))|one|two
 assert len(B)==13+24*(2*M+1)
 return B

def run(k,M=80,cap=1000000):
 B=seed(k,M);initial=set(B);p=(0,0);h=c.H0;last='';firstdiff=None;lastreads={};J10=0
 plan=(c.WORD*k+REF)*2;expectedpose=c.trace(plan)[1:];assert expectedpose==((0,0),c.H0)
 nextcheck=len(plan)
 for t in range(cap):
  prior=lastreads.get(p)
  before=p,h,p in B
  lastreads[p]=(t,'L' if p in B else 'R')
  p,h,ch=step(B,p,h);last=(last+ch)[-312:]
  if len(last)>=10 and last[-10:] not in LEGAL:J10+=1
  if firstdiff is None and t<len(plan) and ch!=plan[t]:
   firstdiff=dict(t=t,expected=plan[t],actual=ch,pose=before,previous_read=prior,
    inputblack=before[0] in initial,stage='first' if t<104*k+len(REF) else 'second',
    second_offset=t-(104*k+len(REF)))
   print('firstdiff',k,firstdiff,flush=True)
  if t>=nextcheck:
   w=last[-104:]
   if w in PHASES and last==w*3:
    cert=certify_period(B,p,h,w)
    if cert:return dict(k=k,M=M,mass=len(initial),firstdiff=firstdiff,capture=t+1,pose=(p,h),tail=cert,J10=J10,final_mass=len(B))
   nextcheck=t+104
 return dict(k=k,M=M,status='cap',firstdiff=firstdiff,p=p,h=h)
LEGAL={(c.WORD+c.WORD)[i:i+10] for i in range(104)}
if __name__=='__main__':
 out=[]
 for k in [0,22,64,128,256]:
  r=run(k);out.append(r);print(json.dumps(r),flush=True)
  (HERE/'results.json').write_text(json.dumps(out,indent=2)+'\n')
