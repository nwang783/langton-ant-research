from pathlib import Path
import sys
src,out=map(Path,sys.argv[1:3]);ix=list(map(int,sys.argv[3].split(',')))
with src.open()as f,out.open('w')as o:
 m,np,ne,ni,ng=map(int,next(f).split());o.write(f'{len(ix)} {np} {ne} {ni} {ng}\n');o.write(next(f));
 for _ in range(ng):
  v=list(map(int,next(f).split()));o.write(' '.join(map(str,[v[0]]+[v[1+5*k+j]for k in ix for j in range(5)]))+'\n')
 for _ in range(ne):
  v=list(map(int,next(f).split()));o.write(' '.join(map(str,v[:4]+[v[4+5*k+j]for k in ix for j in range(5)]+[v[4+5*m+k]for k in ix]))+'\n')
