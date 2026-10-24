from pathlib import Path
import json
from verify_macro_word import D,rot
M={a:set(map(tuple,ps))for a,ps in json.load(open(Path(__file__).with_name('cfree_kernel_current_marks.json'))).items()}
F={a:{tuple(z['p'])for z in d['trace']}for a,d in D.items()}
def transform(s,p,h):return{(p[0]+rot(q,h)[0],p[1]+rot(q,h)[1])for q in s}
def center(p,h):
 x,y=rot((-1,1),h);return 2*p[0]+x,2*p[1]+y
for a in'UVQB':
 assert {(-1,0),(0,1),(1,2)}<=F[a]
 assert center((0,0),0)!=center(D[a]['end_pose'][:2],D[a]['end_pose'][2])
 assert ((1,2)if a=='V'else(-1,0))in M[a]
for a in'QB':assert(-2,-1)in F[a]
assert(-1,2)in F['U']
assert center((0,0),0)==center((-1,1),2)
rows=[]
for a in'UVQB':
 h=(2-D[a]['end_pose'][2])%4;dx,dy=rot(D[a]['end_pose'][:2],h);p=(-1-dx,1-dy)
 ms=transform(M[a],p,h)
 assert(-1,2)in ms
 if a in'UB':assert(0,3)in ms
 if a=='Q':assert(1,4)in ms
 rows.append({'predecessor':a,'pose':[*p,h],'marked_sites':sorted(ms)})
 # Exact two-macro displacement starting V.
 d=D[a]['end_pose'];end=(1+d[0],3+d[1]);c=center(end,d[2]);assert c!=center((0,0),0)
assert center((1,3),0)==center((0,4),2)
Path(__file__).with_name('cfree_center_self_avoidance_ingredients.json').write_text(json.dumps(rows,indent=2))
print('All exact freshness and kinematic ingredients passed.')
