"""Fixed central blank-endcap model. Discovery only until finite guards pass."""
import sys,json,gzip
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import P,D,W,step,PHASES,plan
sys.path.insert(0,str(ROOT/'scattering/transverse'))
from crossing import Field,tail,rotate,plus,times
BAD=[13,28,60,70,75]
def initial(r):
 B=set();p=(0,0);h=0
 for _ in range(9977):p,h,ch=step(B,p,h)
 O0=p;E=B^{plus(O0,rotate(q,1)) for q in P};assert p==(-15,10) and h==3
 R=json.loads((ROOT/f'scattering/ordinary_reverse_interface/certificate_r{r}.json').read_text());p,h=R['capture_pose'];assert h==0 and R['tail_phase']==0
 cap=(-55+p[1][1],-30-p[0][1]);rays=[(plus(O0,rotate(q,1)),(-2,-2),0,None) for q in D]+[(plus(cap,plus(rotate(q,3),(-2,-2))),(-2,-2),0,None) for q in D]
 changes=E^{plus(cap,rotate(q,3)) for q in P}
 return Field(rays,changes),cap,1

def run(r,limit=500000):
 field,p,h=initial(r);start=p;word=[];reads=[]
 for t in range(limit):
  reads.append(p);p,h,ch=field.step(p,h);word.append(ch)
  if (t+1)%104==0 and t>312:
   tw=''.join(word[-104:])
   if tw in PHASES and ''.join(word[-312:])==tw*3:
    cert=tail(field,p,h,tw)
    if cert:
     filename=f'word_r{r}.txt.gz'
     with gzip.open(HERE/filename,'wt') as f:f.write(''.join(word))
     return dict(phase=r,start=[start,1],capture=t+1,pose=[p,h],tail=cert,z_bounds=[min(map(sum,reads)),max(map(sum,reads))],u_bounds=[min(x-y for x,y in reads),max(x-y for x,y in reads)],word_file=filename)
 return dict(phase=r,status='cap',pose=[p,h])
if __name__=='__main__':
 rows=[]
 for r in BAD:
  x=run(r);rows.append(x);print(json.dumps(x),flush=True);(HERE/'discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
