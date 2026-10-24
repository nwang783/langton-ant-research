"""Discovery only: the sole cap output directed back toward old finite debris."""
import sys,json,gzip
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan,step,PHASES,certify_period
Q,_,_,_=plan(W,(0,0),2)
C=json.loads((ROOT/'scattering/ordinary_reverse_interface/certificate_r28.json').read_text());MODEL=json.loads((HERE/'discovery.json').read_text())[1]
def run(m,k,limit=1000000):
 O=(-15-2*m,10-2*m);rot=lambda p:(p[1],-p[0]);add=lambda p,q:(p[0]+q[0],p[1]+q[1]);q2=tuple(a*k+b for a,b in C['second_marker_affine'])
 initial={add(O,rot(Q[28])),add(O,rot(q2))};B=set(initial);p=(0,0);h=0;word=[];hits={};failure=None
 entry=208*(m+k)+65457;compare=entry+MODEL['capture'];tail=W[MODEL['tail']['phase']:]+W[:MODEL['tail']['phase']]
 for t in range(limit):
  if p in initial and p not in hits:hits[p]=t
  before=p;p,h,ch=step(B,p,h);word.append(ch)
  if t>=compare and ch!=tail[(t-compare)%104] and failure is None:failure=dict(time=t,point=before,expected=tail[(t-compare)%104],actual=ch)
  if t>compare+20000 and (t+1)%104==0:
   tw=''.join(word[-104:])
   if tw in PHASES and ''.join(word[-312:])==tw*3:
    cert=certify_period(B,p,h,tw)
    if cert:
     filename=f'r28_complete_m{m}_k{k}.txt.gz'
     with gzip.open(HERE/filename,'wt') as f:f.write(''.join(word))
     return dict(m=m,k=k,initial=sorted(initial),capture=t+1,pose=[p,h],tail=cert,cap_entry=entry,first_cap_tail_failure=failure,hits=[(p,t) for p,t in hits.items()],word_file=filename)
 return dict(m=m,k=k,status='cap',failure=failure)
if __name__=='__main__':
 rows=[]
 for m,k in [(100,100),(101,100),(100,101),(101,101)]:
  x=run(m,k);rows.append(x);print(json.dumps(x),flush=True);(HERE/'r28_complete_discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
