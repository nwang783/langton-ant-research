from synthesize_third_return import *
from return_guide_geometry import fine_of,axis_join,vertices,D

def parallel(q,d=-4):
 C=vertices(q,12);runs=[D[j%4]for j in range(q)];ends=[];idx=0
 for j in range(q):idx+=12*((j+2)//2);ends.append(C[idx])
 corners=[(0,d)]
 for j,V in enumerate(ends[:-1]):
  a=runs[j];b=runs[j+1];corners.append((V[0]-d*(a[1]+b[1]),V[1]+d*(a[0]+b[0])))
 V=ends[-1];a=runs[-1];corners.append((V[0]-d*a[1],V[1]+d*a[0]));return list(reversed(fine_of(axis_join(corners))))

def test(q,d=-4):
 B,p,h,z=final(q);k=wwhich(p,h);A={tuple(x)for x,s in z['labels']if s=='second'};J=joins(A,k);hist=get_history(z);base=B|J
 root=uv(cursors(p,h)[1]);sg=1 if q%4==1 else -1
 cycvs=[add(root,(sg*x,sg*y))for x,y in[(0,0),(0,-1),(1,-1),(1,0),(0,0)]];cycle=set(cell(u,v)for u,v in zip(cycvs,cycvs[1:]));start=cycvs[1]
 K=parallel(q,d);a=K[0]
 # From the outer cyclic renewal, pass one step out then across to the parallel lane.
 patch=axis_join([start,(start[0],a[1]),a]);K=patch+K[1:]
 tail=axis_join([K[-1],(K[-1][0],-2),(2,-2)]);K+=tail[1:]
 change=True
 while change:
  change=False
  for i in range(len(K)-3):
   if abs(K[i][0]-K[i+3][0])+abs(K[i][1]-K[i+3][1])==1:K=K[:i+1]+K[i+3:];change=True;break
 guide=set(cell(u,v)for u,v in zip(K,K[1:]));badseed=guide&(set(hist)|base|cycle)
 print(q,'d',d,'K',len(K)-1,'simple',len(K)==len(set(K)),'badseed',len(badseed),sorted(badseed)[:4],flush=True)
 if badseed:return
 extras=guide|J|cycle;bb=set(map(tuple,z['initial']))|extras;pp,hh=tuple(z['entry'][0]),z['entry'][1]
 for w in z['words']:
  for c in w:assert c==('L'if pp in bb else'R');pp,hh=step(bb,pp,hh)
 prev=(start[0]-root[0],start[1]-root[1]);b=(K[1][0]-K[0][0],K[1][1]-K[0][1]);r=1+prev[0]*b[1]-prev[1]*b[0]
 ret='RL'+path_word(K,r)+'RRRRL'
 for t,c in enumerate(ret):
  if c!=('L'if pp in bb else'R'):print('returnbad',q,t,pp,c,'L'if pp in bb else'R');return
  pp,hh=step(bb,pp,hh)
 print('entry',pp,hh)
 P3=list(map(uv,ordered_path(A|J,k,xy((1,-2)))))[2:-1];third=path_word(P3,1)
 for t,c in enumerate(third):
  if c!=('L'if pp in bb else'R'):print('thirdbad',q,t,pp,c,'L'if pp in bb else'R');return
  pp,hh=step(bb,pp,hh)
 print('SUCCESS',q,'extra',len(extras))
 (OUT/f'parallel_third_q{q}.json').write_text(json.dumps(dict(q=q,d=d,K=K,extra=sorted(extras),return_word=ret,third_word=third),indent=2)+'\n')
if __name__=='__main__':
 for q in(3,5,7,9):test(q)
