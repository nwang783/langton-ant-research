"""Discovery only: complete three-cell finite seed, independent m,k."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,PHASES,step,certify_period

def main(m,k):
 s=(-2*m-19,-2*m+8);Q=(-2*m-2*k-26,-2*m-2*k-5);C=(-2*m+2*k+27,-2*m-2*k-5);B={s,Q,C};p=(0,0);h=0;w=[];reads=[];hits={}
 for t in range(1500000):
  reads.append(p)
  for key,q in [('Q',Q),('C',C)]:
   if p==q and key not in hits:hits[key]=t
  p,h,c=step(B,p,h);w.append(c)
  if 'C' in hits and t>hits['C']+65000 and (t+1)%104==0:
   tw=''.join(w[-104:])
   if tw in PHASES and ''.join(w[-312:])==tw*3:
    cert=certify_period(B,p,h,tw)
    if cert:
     name=f'actual_m{m}_k{k}.txt.gz'
     with gzip.open(HERE/name,'wt') as f:f.write(''.join(w))
     out=dict(status='complete finite-seed discovery',m=m,k=k,initial=[s,Q,C],first_contacts=hits,capture=t+1,pose=[p,h],tail=cert,phase=next(j for j in range(104) if tw==W[j:]+W[:j]),bounds_u_z=[min(x-y for x,y in reads),max(x-y for x,y in reads),min(map(sum,reads)),max(map(sum,reads))],word_file=name);break
 else:out=dict(status='limit',m=m,k=k,time=len(w),pose=[p,h],first_contacts=hits)
 (HERE/f'actual_m{m}_k{k}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main(int(sys.argv[1]),int(sys.argv[2]))
