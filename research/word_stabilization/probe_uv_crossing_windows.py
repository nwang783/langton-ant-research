import itertools,json,sys
from pathlib import Path
from verify_macro_word import D,rot

def tr(w,h,r):
 dx=sum(D[a]['end_pose'][0]for a in w[:r]);dy=sum(D[a]['end_pose'][1]for a in w[:r]);dx,dy=rot((dx,dy),h);p=(-dx,-dy) if h==0 else(-1-dx,1-dy);start=p;first={};last={}
 for a in w:
  for z in D[a]['trace']:
   dx,dy=rot(z['p'],h);q=p[0]+dx,p[1]+dy;first.setdefault(q,z['c']);last[q]=z['c']
  dx,dy=rot(D[a]['end_pose'][:2],h);p=(p[0]+dx,p[1]+dy)
 if h==0:lo,hi=start[1],p[1]-1
 else:lo,hi=p[1]+1,start[1]
 return first,last,lo,hi
r=int(sys.argv[1])if len(sys.argv)>1 else 2
miss=[];cases=[]
for a,b in [('U','V'),('V','U')]:
 aw=[''.join(w)for w in itertools.product('UV',repeat=2*r+1)if w[r-1]==w[r]==a]
 bw=[''.join(w)for w in itertools.product('UV',repeat=2*r+1)if w[r-1]==w[r]==b]
 at={w:tr(w,0,r)for w in aw};bt={w:tr(w,2,r)for w in bw}
 for x in aw:
  af,al,alo,ahi=at[x]
  for y in bw:
   bf,bl,blo,bhi=bt[y];bad=[q for q in al.keys()&bf.keys()if max(alo,blo)<q[1]<min(ahi,bhi) and al[q]==bf[q]]
   row={'north':x,'south':y,'bad':sorted(bad)};cases.append(row)
   if not bad:miss.append(row)
print('radius',r,'cases',len(cases),'misses',len(miss), 'examples',miss[:3])
Path(__file__).with_name(f'uv_crossing_windows_{r}.json').write_text(json.dumps({'radius':r,'cases':cases,'misses':miss},indent=2))
