import sys,json,gzip
from pathlib import Path
from discover import initial,HERE,step,certify_period,W,PHASES

def run(m,k):
 B,A=initial(72,m,k);n=m+k;C=(2*n-4*m-112,-2*n-14);D=(C[0],A[1]);B|={C,D};initialB=sorted(B);p=(0,0);h=0;word=[];firstC=firstD=None
 for t in range(3000000):
  if p==C and firstC is None:firstC=t
  if p==D and firstD is None:firstD=t
  p,h,c=step(B,p,h);word.append(c)
  if firstC is not None and t>firstC+20000 and (t+1)%104==0:
   tw=''.join(word[-104:])
   if tw in PHASES and ''.join(word[-312:])==tw*3:
    proof=certify_period(B,p,h,tw)
    if proof:
     fn=f'cycle72_m{m}_k{k}.txt.gz'
     with gzip.open(HERE/fn,'wt') as o:o.write(''.join(word))
     out=dict(status='complete finite five-cell discovery only',phase=72,m=m,k=k,n=n,initial=initialB,C=C,D=D,first_C=firstC,first_D=firstD,capture=t+1,pose=[p,h],tail=proof,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),word_file=fn);(HERE/f'cycle72_m{m}_k{k}.json').write_text(json.dumps(out,indent=2)+'\n');return out
 return dict(status='limit without certified tail',m=m,k=k,first_C=firstC,first_D=firstD)
if __name__=='__main__':
 for m,k in [(100,100),(101,100),(100,101),(101,101)]:print(json.dumps(run(m,k)),flush=True)
