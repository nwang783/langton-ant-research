"""Discovery only: ordinary SW output plus two opposite remote72 markers."""
import json,sys,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];SRC=HERE.parent/'ordinary_reverse_interface'
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import P,D,W,plan,PHASES
sys.path.insert(0,str(HERE.parent/'transverse'));from crossing import Field,tail
RAYS=[29,32,38,55,56,62,71];Q=plan(W,(0,0),2)[0]
def run(r,n,p,limit=500000):
 cert=json.loads((SRC/f'certificate_r{r}.json').read_text());q2=tuple(a*n+b for a,b in cert['second_marker_affine']);cp,ch=cert['capture_pose'];assert ch==1 and cert['tail_phase']==0 and cert['tail']['drift']==[2,2]
 assert [a for a,b in cp]==[-2,-2];base=tuple(b for a,b in cp);q3=plan(W[:72],base,1)[2];q3=(q3[0]+2*p,q3[1]+2*p)
 f=Field([((x-2,y+2),(-2,2),0,None) for x,y in D],P^{Q[r],q2,q3});pos=(0,0);h=2;w=[];hits={};lo=hi=0
 for t in range(limit):
  if pos==q2 and 'q2' not in hits:hits['q2']=t
  if pos==q3 and 'q3' not in hits:hits['q3']=t
  lo=min(lo,pos[0]-pos[1]);hi=max(hi,pos[0]-pos[1]);pos,h,ch=f.step(pos,h);w.append(ch)
  if 'q3' in hits and t>hits['q3']+2000 and (t+1)%104==0:
   tw=''.join(w[-104:])
   if tw in PHASES and ''.join(w[-312:])==tw*3:
    proof=tail(f,pos,h,tw)
    if proof:
     name=f'r{r}_n{n}_p{p}.txt.gz'
     with gzip.open(HERE/name,'wt') as out:out.write(''.join(w))
     return dict(status='exact infinite-input witness only; no all-parameter theorem',r=r,n=n,p=p,markers=[Q[r],q2,q3],capture=t+1,pose=[pos,h],tail=proof,hits=hits,prefix_u_bounds=[lo,hi],word_file=name)
 return dict(status='discovery limit',r=r,n=n,p=p,hits=hits,pose=[pos,h],prefix_u_bounds=[lo,hi])
if __name__=='__main__':
 rows=[]
 for r in RAYS:
  for n,p in [(100,100),(101,100),(100,101)]:
   row=run(r,n,p);rows.append(row);print(json.dumps(row),flush=True);(HERE/'discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
