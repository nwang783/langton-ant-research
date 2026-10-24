"""Finite local ingredient search for opposed U/V run-spine interlacing."""
from itertools import product
from pathlib import Path
import json
from verify_macro_word import D,rot

def trace3(w,h,p=(0,0)):
 d=rot(D[w[0]]['end_pose'][:2],h);p=(p[0]-d[0],p[1]-d[1]);first={};last={};middle=set()
 for i,a in enumerate(w):
  for z in D[a]['trace']:
   d=rot(z['p'],h);q=p[0]+d[0],p[1]+d[1];first.setdefault(q,z['c']);last[q]=z['c']
   if i==1:middle.add(q)
  d=rot(D[a]['end_pose'][:2],h);p=p[0]+d[0],p[1]+d[1]
 return first,last,middle

def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def transverse(a,b,c,d):return cross(a,b,c)*cross(a,b,d)<0 and cross(c,d,a)*cross(c,d,b)<0
rows=[];miss=[]
for aa in map(''.join,product('UV',repeat=3)):
 af,al,am=trace3(aa,0);a=(-1,1);d=D[aa[1]]['end_pose'];a2=a[0]+2*d[0],a[1]+2*d[1]
 for bb in map(''.join,product('UV',repeat=3)):
  d=D[bb[1]]['end_pose'];
  for x in range(-8,9):
   for y in range(-8,9):
    b=(2*x+1,2*y-1);b2=b[0]-2*d[0],b[1]-2*d[1]
    if a!=b or aa[:2]not in("UU","VV") or bb[:2]not in("UU","VV") or aa[1]==bb[1]:continue
    bf,bl,bm=trace3(bb,2,(x,y));shared={q for q in set(al)&set(bf) if -D[aa[0]]["end_pose"][1]<q[1]<D[aa[1]]["end_pose"][1]+D[aa[2]]["end_pose"][1]-1 and y-D[bb[1]]["end_pose"][1]-D[bb[2]]["end_pose"][1]+1<q[1]<y+D[bb[0]]["end_pose"][1]};bad=[q for q in shared if al[q]==bf[q]]
    row={'north':aa,'south':bb,'south_pose':[x,y,2],'conflicts':sorted(bad),'letters':[al[q]for q in sorted(bad)]}
    rows.append(row)
    if not bad:miss.append(row)
print('cases',len(rows),'without central-cell conflict',len(miss))
print(miss[:5])
Path(__file__).with_name('uv_vertex_crossing.json').write_text(json.dumps({'cases':rows,'misses':miss},indent=2))
