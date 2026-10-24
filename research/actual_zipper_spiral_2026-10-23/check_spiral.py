"""Literal full-board actual ant checks of scaled square-spiral zipper candidates."""
from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton')
sys.path.insert(0,str(ROOT/'global_renewal_archive_2026-10-23'))
from check_renewal_archive import step,cursors,endpoints,wwhich,connected,rank
D=((1,0),(0,1),(-1,0),(0,-1))

def vertices(q,scale=3):
 p=[(0,0)]
 for j in range(1,q+1):
  dx,dy=D[(j-1)%4]
  for _ in range(scale*((j+1)//2)):
   a,b=p[-1];p.append((a+dx,b+dy))
 return p

def xy(v):
 a,b=v;return 2*a+2*b+1,2*a-2*b+1

def setup(q,scale=3):
 vs=list(map(xy,vertices(q,scale)))
 cells=[((u[0]+v[0])//4,(u[1]+v[1])//4)for u,v in zip(vs,vs[1:])]
 assert len(set(vs))==len(vs) and len(set(cells))==len(cells)
 B=set(cells);p=cells[0]
 h=next(h for h in range(4)if cursors(p,h)[1]==vs[0])
 assert wwhich(p,h)==0
 word='L'
 for u,v,w in zip(vs,vs[1:],vs[2:]):
  a=(v[0]-u[0],v[1]-u[1]);b=(w[0]-v[0],w[1]-v[1])
  cross=a[0]*b[1]-a[1]*b[0]
  turn=-1 if cross>0 else 1 if cross<0 else 0
  word+='R'*(1+turn)+'L'
 return B,p,h,vs,cells,word

def check(q,scale=3,graphs=True):
 B,p,h,vs,cells,word=setup(q,scale);B0=set(B);k=wwhich(p,h);n=len(cells)
 # The displayed entry is literally immediately after a bridge L.
 preB=set(B)|{(0,1)};preP=(0,1);preH=2
 assert (0,1) not in B
 assert all(not connected(preB-{preP},kk,*endpoints(preP,kk))for kk in(0,1))
 gotP,gotH=step(preB,preP,preH)
 assert (preB,gotP,gotH)==(B,p,h)
 r=0;L=0;R=0;erasures=[0,0];births=[0,0];maxmass=n
 wpath=[cursors(p,h)[1]]
 for t,c in enumerate(word):
  actual='L'if p in B else'R'
  assert actual==c,('read mismatch',q,scale,t,p,h,c,actual,L,r)
  if c=='R':
   R+=1;r+=1
   if graphs:
    for kk in (0,1):births[kk]+=connected(B,kk,*endpoints(p,kk))
  else:
   assert p==cells[L],('wrong edge',q,scale,t,L,p,cells[L])
   if graphs:
    for kk in (0,1):erasures[kk]+=connected(B-{p},kk,*endpoints(p,kk))
   L+=1;r=0
  p,h=step(B,p,h);maxmass=max(maxmass,len(B))
  if c=='L':wpath.append(cursors(p,h)[1]);assert wpath[-1]==vs[L]
 assert wpath==vs and L==n
 signed=q-1
 # The ordinary epoch is maximal: current w is isolated, forcing RRRRL.
 tailB=set(B);tailP=p;tailH=h
 tailword=''
 for _ in range(5):
  tailword+='L'if tailP in tailB else'R'
  tailP,tailH=step(tailB,tailP,tailH)
 assert tailword=='RRRRL' and len(tailB)==len(B)+3
 assert len(B)-n==signed-1 # first block has gain -1, other gains are path turns
 return {'q_runs':q,'scale':scale,'n_edges':n,'T_updates':len(word),'initial_mass':n,'final_mass':len(B),'mass_gain':len(B)-n,'signed_clockwise_turn':signed,'erasures':erasures if graphs else None,'births':births if graphs else None,'initial_ranks':[rank(B0,kk)for kk in(0,1)],'final_ranks':[rank(B,kk)for kk in(0,1)],'max_mass':maxmass,'proper_post_L_entry':True,'next_word':tailword,'word_sha256':hashlib.sha256(word.encode()).hexdigest()}

if __name__=='__main__':
 cases=[]
 for scale in (1,2,3,4):
  for q in (1,2,3,4,8,16,32):
   try:r=check(q,scale)
   except AssertionError as e:r={'q':q,'scale':scale,'failed':str(e)}
   cases.append(r);print(json.dumps(r),flush=True)
 Path(__file__).with_name('controls.json').write_text(json.dumps(cases,indent=2)+'\n')
