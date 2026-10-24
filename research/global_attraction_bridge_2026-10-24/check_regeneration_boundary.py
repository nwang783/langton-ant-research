"""Exact current-field and literal next-interface checks, not recurrence claims."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
from check_three_positive_passes import ends,D,Graph
OUT=Path(__file__).parent

def uv(v):X,Y=v;assert(X+Y-2)%4==0 and(X-Y)%4==0;return((X+Y-2)//4,(X-Y)//4)
def cell(a,b):return((a[0]+a[1]+b[0]+b[1]+1)//2,(a[0]-a[1]+b[0]-b[1]+1)//2)
def joins(A):
 degree=defaultdict(int)
 for e in A:
  for v in ends(e,0):degree[v]+=1
 tips=[uv(v)for v,d in degree.items()if d==1];J=set()
 for u in tips:
  for v in tips:
   if abs(u[0]-v[0])+abs(u[1]-v[1])==1:
    e=cell(u,v)
    if e not in A:J.add(e)
 return J

def rot(p,r):
 x,y=p
 for _ in range(r):x,y=y,-x
 return x,y

cert=json.loads((OUT/'THREE_POSITIVE_PASSES_CERTIFICATE.json').read_text());verified=json.loads((OUT/'THREE_POSITIVE_PASSES_CHECKED.json').read_text());out=[]
for c,v in zip(cert['cases'],verified['cases']):
 q=c['q'];B=set(map(tuple,c['initial_black']));p,h=tuple(c['initial_pose'][0]),c['initial_pose'][1];history=defaultdict(list);t=0
 for s in c['stages']:
  for ch in s['word']:
   assert ch==('L'if p in B else'R');history[p].append((t,ch));t+=1
   if ch=='L':B.remove(p);h=(h-1)%4
   else:B.add(p);h=(h+1)%4
   p=(p[0]+D[h][0],p[1]+D[h][1])
 assert B==set(map(tuple,v['full_final_field']))and[p,h]==[tuple(v['final_pose'][0]),v['final_pose'][1]]
 A3={tuple(x)for x,s,b in v['full_final_lifetime_labels']if s=='third_positive_ordinary'};J3=joins(A3)
 assert len(J3)==q-1 and not(J3&B)and not(J3&set(history))
 A2={tuple(x)for x,b in v['remaining_second_lifetimes']};assert len(A2)==5 and not(J3&A2)
 oldentry=v['stages'][3]['entry_pose'];oldB=set(map(tuple,v['stages'][2]['full_field']));rp=rot(tuple(oldentry[0]),(h-oldentry[1])%4);shift=(p[0]-rp[0],p[1]-rp[1]);r=(h-oldentry[1])%4
 model={tuple(a+b for a,b in zip(rot(x,r),shift))for x in oldB}
 w=c['stages'][3]['word']+c['stages'][4]['word'];pp=p;hh=h;first={};bad=[]
 for i,ch in enumerate(w):
  if pp not in first:
   first[pp]=(i,ch)
   if (pp in B)!=(ch=='L'):bad.append(dict(offset=i,cell=pp,required=ch,current='L'if pp in B else'R'))
  hh=(hh+(1 if ch=='R'else-1))%4;pp=(pp[0]+D[hh][0],pp[1]+D[hh][1])
 assert min(x['offset']for x in bad)==1
 # Each actual output component, not just the marked rods, remains in the final field.
 G=Graph(B,0);remain=set(B);components=[]
 while remain:
  e=min(remain);C=G.component(ends(e,0)[0]);remain-=C;components.append(dict(edges=sorted(C),third_R_edges=sorted(C&A3),retained_second_edges=sorted(C&A2)))
 out.append(dict(q=q,final_pose=[p,h],next_direct_stitches=sorted(J3),next_stitches_currently_white=True,next_stitches_never_read_in_entire_certified_history=True,five_second_R_boundary_lifetimes=v['remaining_second_lifetimes'],surviving_original_added_lifetimes=v['surviving_original_added_lifetimes'],pose_compatible_repetition=dict(rotation_clockwise_quarter_turns=r,translation=shift,full_template_missing_black=sorted(model-B),full_template_extra_black=sorted(B-model),minimal_first_read_guard_violations=bad,first_literal_guard_failure=min(bad,key=lambda z:z['offset'])),complete_final_w_components=components,scope='The exact old return-plus-third word cannot immediately repeat, even allowing irrelevant extra archive. A later repair, different port, different word, or longer detour is not excluded. Missing q−1 direct stitches do not exclude alternative connecting paths.'))
(OUT/'REGENERATION_BOUNDARY_CHECKED.json').write_text(json.dumps(dict(status='AUTHOR exact finite boundary checks, independent review requested',cases=out),indent=2)+'\n')
print([(x['q'],len(x['next_direct_stitches']),x['pose_compatible_repetition']['first_literal_guard_failure'],len(x['pose_compatible_repetition']['minimal_first_read_guard_violations']))for x in out])
