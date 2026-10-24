"""Independent backward-coordinate audit of port-color templates and all edges.
No import of the symbolic worker's transition/template/BDD code.
"""
import json
from pathlib import Path
ROOT=Path('/workspace/shared/langton')
D=json.load(open(ROOT/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'))
G=json.load(open(ROOT/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_actual_ports.json'))
C=json.load(open(ROOT/'word_stabilization/minimized_actual_ports.json'))
M=G['marker']; DIR=[(0,1),(1,0),(0,-1),(-1,0)]
def rotate(p,h):
 x,y=p
 for _ in range(h%4):x,y=y,-x
 return x,y

def backwards(past):
 # Endpoint (0,0,N). Last chronological read of each cell determines its color.
 p=(0,0);h=0;known={}
 for letter in reversed(past):
  dx,dy=DIR[h];p=p[0]-dx,p[1]-dy
  known.setdefault(p,letter=='R')
  h=(h+(-1 if letter=='R' else 1))%4
 return known

def forward(past):
 x=y=h=0;post={}
 for c in past:
  post[x,y]=c=='R';h=(h+(1 if c=='R' else -1))%4
  dx,dy=DIR[h];x+=dx;y+=dy
 return {rotate((px-x,py-y),-h):b for (px,py),b in post.items()}

def feasible(w):
 last={};p=(0,0);h=0
 for c in w:
  if last.get(p)==c:return False
  last[p]=c;h=(h+(1 if c=='R' else -1))%4;v=DIR[h];p=p[0]+v[0],p[1]+v[1]
 return True

classes=dict(C['port_classes']);templates={};templates_compared=0
for w,cl in C['port_classes']:
 assert len(w)==149 and w.endswith(M) and feasible(w)
 a=backwards(w[:-len(M)]);b=forward(w[:-len(M)])
 assert a==b,w
 templates[w]=a;templates_compared+=1

labels={v['word'][len(M):]+M:k for k,v in D.items()}
ct={(a,k):b for a,k,b in C['transitions']};kept=discarded=overlap_checks=0
for a,b,w in G['edges']:
 if not feasible(a+w):discarded+=1;continue
 kept+=1;k=labels[w];assert ct[classes[a],k]==classes[b]
 # All source template colors must agree with the macro reads, then the
 # destination template must agree with this independently advanced field.
 field=dict(templates[a]);x=y=h=0
 for c in D[k]['word']:
  if (x,y) in field:assert field[x,y]==(c=='L'),(k,'source-read')
  field[x,y]=c=='R';h=(h+(1 if c=='R' else -1))%4
  dx,dy=DIR[h];x+=dx;y+=dy
 for p,value in templates[b].items():
  dx,dy=rotate(p,h);q=x+dx,y+dy
  if q in field:assert field[q]==value,(k,'destination-color');overlap_checks+=1
 # Literal suffix alignment is the reason a post-marker port can be used
 # as a class label at the corresponding before-marker physical pose.
 assert ((a[:-len(M)]+D[k]['word'])[-137:])==b[:-len(M)]

assert kept==C['original_edges'] and discarded==C['discarded_edges']
result={'status':'PASS','ports':templates_compared,'feasible_edges':kept,'discarded_infeasible_edges':discarded,'destination_color_comparisons':overlap_checks,'verified':['backward vs forward rotated templates','before-marker suffix alignment on every edge','class transitions on every edge','source macro read consistency','destination template agreement'],'scope':'Color templates and class/marker alignment; not BDD fixed-point completeness or graph language provenance.'}
print(json.dumps(result,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
