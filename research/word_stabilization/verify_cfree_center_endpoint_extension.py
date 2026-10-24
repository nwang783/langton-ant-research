import json
from pathlib import Path
from verify_macro_word import D,rot
M={a:set(map(tuple,ps))for a,ps in json.load(open(Path(__file__).with_name('cfree_kernel_current_marks.json'))).items()}
for a in'UVQB':
 d=D[a]['end_pose'];dx,dy=rot((0,-1),d[2]);tip=(d[0]+dx,d[1]+dy)
 assert tip in M[a]
 F={tuple(z['p'])for z in D[a]['trace']};assert(0,-1)in F
 if a!='V':assert(-1,2)in F
 print(a,'endpoint-relative marked terminal input',tip)
print('Endpoint strengthening ingredients passed.')
