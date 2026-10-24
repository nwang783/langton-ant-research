"""Exact finite proof of arbitrary V/P108 mixture fields, no horizon inference."""
from pathlib import Path
import collections,json,hashlib
import certify_short_refinement_rup as core
P=Path(__file__).resolve().parent
Z=json.loads((P/'short_refinement_scaffold_inputs.json').read_text());V=Z['reverse104'][1:]+Z['reverse104'][:1]
rows,e,h=core.trace(V,(0,0),2);assert(e,h)==((-2,-2),2)
J={q for q,h,c in rows};first={}
for q,h,c in rows:first.setdefault(q,c)
I={q for q,c in first.items() if c=='L'};assert len(I)==25
by=collections.defaultdict(list)
for t,(q,h,c) in enumerate(rows):by[(q[0]-q[1],q[0]%2)].append((q[0]//2,t,q,h,c))
width=max(max(a[0] for a in rr)-min(a[0] for a in rr) for rr in by.values())
# No earlier period farther than this width can touch a local cell.
T=[]
for n in range(1,width+1):
 past={(x+2*k,y+2*k) for k in range(1,n+1) for x,y in J}
 T.append(I-past)
assert all(a==T[0] for a in T) and len(T[0])==12
points=[(1,7),(0,7),(0,8),(1,8)];hist={}
for p in points:
 vv=[]
 for r in range(-width,width+1):
  for t,(q,h,c) in enumerate(rows):
   if(q[0]-2*r,q[1]-2*r)==p:vv.append((r,t,h,c))
 hist[str(p)]=vv
expected={str((1,7)):[(-1,10,0,'R'),(-1,14,2,'L'),(-1,26,0,'R'),(0,30,0,'L')],str((0,7)):[(0,31,3,'L')],str((0,8)):[],str((1,8)):[(-1,13,3,'L')]}
assert hist==expected
# Distinct patch translates: four-cell square with both coordinate spans1
# cannot meet its (2k,2k) translate for a nonzero integer k.
assert max(x for x,y in points)-min(x for x,y in points)==1
assert max(y for x,y in points)-min(y for x,y in points)==1
out=dict(scope=__doc__,coarse_word=V,phase30=rows[30],phase31=rows[31],phase_overlap_width=width,
         initial_first_period=sorted(I),all_later_new_black_template=sorted(T[0]),new_black_templates_equal=True,
         patch_points=points,complete_patch_histories=hist,
         formulas=dict(input_mass='12*n+13-m',output_mass='13+3*m',input_change='remove q+rD for selected r',output_change='add p+rD,u+rD,v+rD for selected r',complete_XOR_change='toggle all four patch cells for selected r'),
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'heading_defect_local_classification/binary_fields.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact patch proof:',width,len(I),len(T[0]))
