"""Candidate discovery after parity-compatible near-core third contacts."""
import json,sys
from pathlib import Path
from discover_parents import extract
from ant_exact import step,certify_period,PHASES,plan,W
HERE=Path(__file__).resolve().parent

def run(m,n,cap=3000000):
 inputs={'q':(-33-2*n,-14-2*n),'s':(-23-2*m,31+2*m)}
 if m==1:inputs['a']=(-33-2*n,2*n-21)
 elif m==6:inputs['c']=(12+2*n,-14-2*n)
 else:raise ValueError(m)
 B=set(inputs.values());p=(0,0);h=0;word=[];last='';contacts={}
 for t in range(cap):
  for k,q in inputs.items():
   if q==p and k not in contacts:contacts[k]=t
  p,h,ch=step(B,p,h);word.append(ch);last=(last+ch)[-312:]
  if t>1000 and t%104==103 and last[-104:] in PHASES and last==last[-104:]*3:
   cert=certify_period(B,p,h,last[-104:])
   if cert:
    w=''.join(word);phase=PHASES[w[-104:]];exc=plan(w[-104:][:(72-phase)%104],p,h)[2]
    return dict(m=m,n=n,capture=t+1,pose=[p,h],tail=cert,phase=phase,contacts=contacts,exc72=exc),w
 return dict(m=m,n=n,status='cutoff',pose=[p,h]),None

if __name__=='__main__':
 out=[]
 for m in (1,6):
  r0,w0=run(m,200);r1,w1=run(m,201);row=dict(m=m,r0=r0,r1=r1)
  if w0 and w1:
   try:
    T=extract(m,r0,w0,r1,w1);(HERE/f'branch_m{m}_template.json').write_text(json.dumps(T,indent=2)+'\n');row['candidate']={k:v for k,v in T.items() if k not in ('segments','infinite_tail_word')}
   except AssertionError as e:row['candidate_failure']=str(e)
  out.append(row);print(json.dumps(row),flush=True)
  (HERE/'branches_discovery.json').write_text(json.dumps(out,indent=2)+'\n')
