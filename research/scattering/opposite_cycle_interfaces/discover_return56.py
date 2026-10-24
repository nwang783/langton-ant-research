"""Discovery only: secondary SE return through the complete phase56 local packet."""
import sys,json,gzip
from pathlib import Path
from certify_caps import HERE,ROOT
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,P,D,plan,PHASES
sys.path.insert(0,str(HERE.parent/'transverse'));from crossing import Field,tail,plus,rotate

def model(n,p):
 C=json.loads((HERE/'backward_certificate_r56.json').read_text());T=json.loads((HERE/'template_r56.json').read_text());ev=lambda v:v[0]*(n-100)+v[1]*(p-100)+v[2]
 initial=[tuple(ev(v) for v in q) for q in C['initial']];F=Field([(plus(q,(-2,2)),(-2,2),0,None) for q in D],set(P)^set(initial));pos=(0,0);h=2
 for seg in T['segments']:
  count=1 if seg['type']=='finite' else seg['count_np'][0]*n+seg['count_np'][1]*p+seg['count_np'][2]
  for expected in seg['word']*count:
   pos,h,ch=F.step(pos,h);assert ch==expected
 assert pos==(2,24) and h==0 and C['tail_phase']==0
 F.changes.symmetric_difference_update({plus(pos,rotate(q,2)) for q in P});F.rays.extend([(plus(pos,rotate(q,2)),(-2,2),0,None) for q in D])
 entry=(-70,130);F.changes.symmetric_difference_update({plus(entry,q) for q in P});F.rays.extend([(plus(plus(entry,q),(-2,2)),(-2,2),0,None) for q in D])
 return F,entry,2

def main(n=100,p=100):
 F,pos,h=model(n,p);w=[];umin=umax=pos[0]-pos[1];zmin=zmax=sum(pos)
 for t in range(500000):
  umin=min(umin,pos[0]-pos[1]);umax=max(umax,pos[0]-pos[1]);zmin=min(zmin,sum(pos));zmax=max(zmax,sum(pos));pos,h,ch=F.step(pos,h);w.append(ch)
  if t>=312 and (t+1)%104==0:
   tw=''.join(w[-104:])
   if tw in PHASES and ''.join(w[-312:])==tw*3:
    cert=tail(F,pos,h,tw)
    if cert:
     file=f'return56_n{n}_p{p}.txt.gz'
     with gzip.open(HERE/file,'wt') as f:f.write(''.join(w))
     out=dict(status='infinite completed-rail model discovery only',n=n,p=p,capture=t+1,pose=[pos,h],tail=cert,u_bounds=[umin,umax],z_bounds=[zmin,zmax],word_file=file);break
 else:out=dict(status='limit',n=n,p=p,time=len(w),pose=[pos,h],u_bounds=[umin,umax],z_bounds=[zmin,zmax])
 (HERE/f'return56_n{n}_p{p}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main(*map(int,sys.argv[1:]))
