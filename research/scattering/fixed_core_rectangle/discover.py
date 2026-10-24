"""Discovery only: exceptional rectangle plus one fixed NW phase72 core bit."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import step,plan,certify_period,PHASES,W
S=(-223,231)

def seed(n):return {S,(-33-2*n,-14-2*n),(-33-2*n,41+2*n),(8+2*n,-14-2*n),(8+2*n,41+2*n)}

def run(n,cap=3000000):
 B=seed(n);p=(0,0);h=0;letters=[];contacts={};last='';lastreads={}
 for t in range(cap):
  if p in seed(n) and p not in contacts:contacts[p]=t
  p,h,ch=step(B,p,h);letters.append(ch);last=(last+ch)[-312:]
  if t>1000 and t%104==103 and len(last)==312 and last[-104:] in PHASES and last==last[-104:]*3:
   cert=certify_period(B,p,h,last[-104:])
   if cert:
    out=dict(n=n,capture=t+1,pose=[p,h],certificate=cert,contacts=[(q,t) for q,t in contacts.items()],final_mass=len(B))
    with gzip.open(HERE/f'word_{n}.txt.gz','wt') as f:f.write(''.join(letters))
    return out
 return dict(n=n,status='cutoff',pose=[p,h],contacts=[(q,t) for q,t in contacts.items()],final_mass=len(B))

def blank_guard():
 B=set();p=(0,0);h=0;reads=[];word=[]
 for t in range(9977):
  reads.append(p);p,h,ch=step(B,p,h);word.append(ch)
 assert certify_period(B,p,h,W)
 tail=plan(W,p,h)[0]
 bounds=[min(x-y for x,y in reads+tail),max(x-y for x,y in reads+tail)]
 assert S[0]-S[1]<bounds[0]
 out=dict(status='all-future blank read guard certified',u_bounds=bounds,fixed_core=S,fixed_core_u=S[0]-S[1],tail_pose=[p,h])
 (HERE/'blank_guard.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)

if __name__=='__main__':
 blank_guard();out=[]
 for n in [200,201,202,500]:
  row=run(n);out.append(row);print(json.dumps(row),flush=True)
  (HERE/'discovery.json').write_text(json.dumps(out,indent=2)+'\n')
