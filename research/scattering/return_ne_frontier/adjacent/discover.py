"""Complete finite three-cell discoveries for matching adjacent corners."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,PHASES,plan,step,certify_period
FRESH=plan(W,(0,0),1)[0];ROWS={r['phase']:r for r in json.loads((HERE.parent/'mass5_interfaces.json').read_text())['rows']}
def initial(r,m,k):
 n=m+k;Q=(-2*n-33,-2*n-14);s=(6-2*m+FRESH[r][0],-43-2*m+FRESH[r][1]);row=ROWS[r];p,h=row['phase_zero_pose_constant'];assert row['pose_translation']=='(-2m,-2m)';b=plan(W[:72],tuple(p),h)[2];d=tuple(row['drift'])
 if d==(-2,2):j=(2*k+33+b[0])//2;assert 2*j==2*k+33+b[0]
 else:assert d==(2,-2);j=(2*k+14+b[1])//2;assert 2*j==2*k+14+b[1]
 t=(b[0]-2*m+j*d[0],b[1]-2*m+j*d[1]);return {Q,s,t},t

def run(r,m,k,limit=2500000):
 B,target=initial(r,m,k);start=sorted(B);p=(0,0);h=0;word=[];reads=[];first=None
 for t in range(limit):
  if p==target and first is None:first=t
  reads.append(p);p,h,c=step(B,p,h);word.append(c)
  if first is not None and t>first+20000 and (t+1)%104==0:
   tw=''.join(word[-104:])
   if tw in PHASES and ''.join(word[-312:])==tw*3:
    proof=certify_period(B,p,h,tw)
    if proof:
     fn=f'r{r}_m{m}_k{k}.txt.gz'
     with gzip.open(HERE/fn,'wt') as o:o.write(''.join(word))
     out=dict(status='complete finite three-cell discovery only',phase=r,m=m,k=k,n=m+k,initial=start,third_marker=target,first_contact=first,capture=t+1,pose=[p,h],tail=proof,tail_phase=next(j for j in range(104) if tw==W[j:]+W[:j]),bounds=[min(x-y for x,y in reads),max(x-y for x,y in reads),min(map(sum,reads)),max(map(sum,reads))],word_file=fn);(HERE/f'r{r}_m{m}_k{k}.json').write_text(json.dumps(out,indent=2)+'\n');return out
 return dict(status='exploration limit, no certified tail',phase=r,m=m,k=k,pose=[p,h])
if __name__=='__main__':
 for r in [15,29,45,56,62,72]:
  for m,k in [(100,100),(101,100),(100,101),(101,101)]:print(json.dumps(run(r,m,k)),flush=True)
