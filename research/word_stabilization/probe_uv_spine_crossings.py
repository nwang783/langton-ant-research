import json
from pathlib import Path
from verify_macro_word import check,D,rot
ROOT=Path(__file__).parent
rows=json.load(open(ROOT.parent/'causal_reduction/five_macro_depth_samples.json'))
words={r['word']for r in rows};words.update('Q'+'U'*n+'Q'+'V'*4+'U'*n+'Q' for n in range(3,12))
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def transverse(a,b,c,d):return cross(a,b,c)*cross(a,b,d)<0 and cross(c,d,a)*cross(c,d,b)<0
witness=[];tested=0
for w in words:
 try:r=check(w)
 except AssertionError:continue
 tested+=1;seg=[]
 for b in r['blocks']:
  if b['macro']not in'UV':continue
  x,y,h=b['pose'];dx,dy=rot((-1,1),h);p=(2*x+dx,2*y+dy);dx,dy=rot(D[b['macro']]['end_pose'][:2],h);q=(p[0]+2*dx,p[1]+2*dy);seg.append((b['index'],h,p,q))
 for z,a in enumerate(seg):
  for b in seg[z+1:]:
   if (a[1]-b[1])%4==2 and transverse(a[2],a[3],b[2],b[3]):witness.append({'word':w,'a':a,'b':b})
print('words',tested,'opposite transverse crossings',len(witness))
(ROOT/'uv_spine_crossings.json').write_text(json.dumps(witness,indent=2))
for w in witness[:3]:print(w)
