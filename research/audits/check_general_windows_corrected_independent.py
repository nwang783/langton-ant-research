"""Nonvacuous sector-correct literal positive controls for both diagonal signs."""
from pathlib import Path
from collections import defaultdict
import json,sys,hashlib
R=Path(__file__).resolve().parents[1];P=R/'periodic_classification_new';sys.path.insert(0,str(P))
from frontier_drift_geometry import Geometry
from general_literal_window import bad_window as old
from general_first_return_window import bad_window as new
D=(1j,1,-1j,-1);word=(R/'word_stabilization/standard_word.txt').read_text().strip();out=[]
for copies in(1,2,3):
 a=2*copies;period=104*copies
 for sign in(1,-1):
  b=sign*a;g=Geometry(a,b);start=-1+0j if sign==1 else 0j;h=1j if sign==1 else 1+0j;q=start;hist=defaultdict(list)
  for t,c in enumerate(word*copies):
   assert (int(q.real+q.imag)+D.index(h))%2==1
   k=int(q.real)//a;rep=q-k*complex(a,b);hist[rep].append((t-k*period,h,c));h*=(-1j if c=='R'else 1j);q+=h
  assert q==start+complex(a,b)
  low=min(int(z.imag)-b*int(z.real)//a for z in hist);high=max(int(z.imag)-b*int(z.real)//a for z in hist)
  rs=[];ts=[]
  for r in range(low,high+1):
   rows=[];times=[]
   for x in range(a):
    es=sorted(hist[complex(x,r+b*x//a)]);assert all(c==('R'if j%2==0 else'L')for j,(_,h,c)in enumerate(es));rows.append(tuple(D.index(h)for _,h,c in es));times.append(tuple(t for t,h,c in es))
   rs.append(rows);ts.append(times)
  windows=nonempty=arc_count=event_count=first_returns=0
  for width in(2,3,4):
   for off in range(len(rs)-width+1):
    hs=rs[off:off+width];times=ts[off:off+width];r0=low+off;succ={};used_arcs=set()
    for y,row in enumerate(hs):
     for x,hsx in enumerate(row):
      actual=complex(x,r0+y+b*x//a)
      for j,hh in enumerate(hsx):
       d=D[hh]*(-1j if j%2==0 else 1j);nq=actual+d;k=int(nq.real)//a;nx=int(nq.real)-k*a;ny=int(nq.imag)-k*b-b*nx//a-r0
       if not 0<=ny<width:continue
       rank=sum(D[v]*(-1j if z%2==0 else 1j)==d for z,v in enumerate(hsx[:j]));arr=[z for z,v in enumerate(hs[ny][nx])if D[v]==d];assert rank<len(arr);jj=arr[rank]
       assert times[ny][nx][jj]+k*period==times[y][x][j]+1
       arc=(x,nx,D.index(d),k,ny-y);assert arc in g.arcs[(r0+y)%2]
       succ[y,x,j]=((ny,nx,jj),k);used_arcs.add((y,*arc))
    # Check exact geometric arc set, not only a possibly empty filtered monitor.
    for y in range(width):
     for x,nx,dd,k,dr in g.arcs[(r0+y)%2]:
      ny=y+dr
      if not 0<=ny<width:continue
      src=[j for j,v in enumerate(hs[y][x])if(v+(1 if j%2==0 else-1))%4==dd]
      dst=[j for j,v in enumerate(hs[ny][nx])if v==dd];assert len(src)==len(dst)
      for j,jj in zip(src,dst):assert succ[y,x,j]==((ny,nx,jj),k)
    assert succ
    for begin in succ:
     cur=begin;wind=0;seen={cur};seen_first=False
     while cur in succ:
      cur,k=succ[cur];wind+=k
      if cur in seen:break
      seen.add(cur)
      if not seen_first and cur[:2]==begin[:2]and wind==0:
       assert cur[2]==begin[2]+1;seen_first=True;first_returns+=1
    assert old(hs,r0%2,g)is None and new(hs,r0%2,g)is None
    windows+=1;nonempty+=1;arc_count+=len(used_arcs);event_count+=len(succ)
  out.append(dict(period=period,full_drift=[a,b],start=[int(start.real),int(start.imag)],incoming=0 if sign==1 else 1,windows=windows,nonempty_windows=nonempty,matched_nonempty_arcs=arc_count,matched_event_successors=event_count,first_physical_returns=first_returns))
author=json.loads((P/'general_windows_positive_corrected.json').read_text())['controls']
for x,y in zip(out,author):
 for k,v in x.items():
  if k!='first_physical_returns':assert v==y[k],(k,v,y[k])
result=dict(status='PASS independent physical successor and chronology reconstruction, explicitly nonvacuous in both sectors',controls=out,corrects='Earlier negative-slope author and audit implementation positives used incompatible geometry sector; physical ref was nonvacuous but tested geometry path could be empty. No exclusion graph depended on those positives.',hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in('check_general_windows_positive_corrected.py','general_windows_positive_corrected.json','general_first_return_window.py')})
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
