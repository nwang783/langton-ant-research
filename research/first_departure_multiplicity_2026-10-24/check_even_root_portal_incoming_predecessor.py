"""Even-root fixed LL portal: complete incoming first-R predecessor bridge.
The selected maximum is F=(1,0), NOT the possibly lower opposite C face.
All four predecessor cases retain every complete WHITE cap-four reader.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
b=Path(__file__).parent
S={'__file__':str(b/'check_terminal_LL_upper_side_collision.py')};exec((b/'check_terminal_LL_upper_side_collision.py').read_text().split('# Shift the physical Q')[0],S)
analyze=S['analyze'];out=S['out'];words=S['words'];V=S['V'];H=S['H']
def at_F(hs):return analyze({(p[0]-1,p[1]-1):h for p,h in hs.items()})
def dom(p):return words('NS' if sum(p)%2==0 else 'EW')
def edge(h,p,dr):
 if (dr in 'EW')==(sum(p)%2==0):return sum(out(h,r)==dr for r in range(len(h)))
 return h.count(H[(H.index(dr)+2)%4])
def propagate(ds):
 ds={p:list(h) for p,h in ds.items()};queue=list(ds)
 while queue:
  p=queue.pop()
  for dr,v in V.items():
   q=p[0]+v[0],p[1]+v[1]
   if q not in ds:continue
   vals={edge(h,p,dr) for h in ds[p]};opp=H[(H.index(dr)+2)%4]
   new=[h for h in ds[q] if edge(h,q,opp) in vals]
   if not new:return None
   if len(new)<len(ds[q]):ds[q]=new;queue.append(q)
 return ds
# Derive every possible complete v whose first R departs N and whose total
# N output is one, because q=SSN has exactly one incoming N.
predecessors=[h for h in words('EW') if h and out(h,0)=='N' and sum(out(h,r)=='N' for r in range(len(h)))==1]
assert predecessors==['W','WW','WWE','WWEW']
local_counts={};local_modes=[];local_nonport=[]
for v in predecessors:
 ct=Counter()
 for x,h in product(dom((2,0)),dom((2,1))):
  hs={(1,0):v,(1,1):'SSN',(2,0):x,(2,1):h}
  res,cert=at_F(hs);ct[res]+=1
  if res!='port':local_nonport.append(dict(v=v,X=x,H=h,result=res,certificate=cert))
  if res=='open':local_modes.append((v,x,h))
 local_counts[v]=dict(ct)
assert local_counts=={'W':{'port':936,'open':6,'rank':13,'higher_C':4,'clock':2},'WW':{'port':933,'open':9,'rank':13,'clock':5,'higher_C':1},'WWE':{'port':933,'open':9,'rank':13,'clock':5,'higher_C':1},'WWEW':{'port':949,'open':4,'rank':6,'clock':2}}
closure_counts=Counter();rows=[];profiles=Counter()
for v,x,h in local_modes:
 fixed={(1,0):v,(1,1):'SSN',(2,0):x,(2,1):h,(0,1):'WE',(0,2):'SNNS',(-1,2):'EEWW',(-1,1):'SS',(1,2):'WWEE'}
 pts=set(fixed)|{(-1,0),(0,0),(2,2)}
 ds=propagate({p:[fixed[p]] if p in fixed else dom(p) for p in pts})
 if ds is None:closure_counts['empty_closure']+=1;continue
 def visit(ds):
  if all(len(h)==1 for h in ds.values()):
   hs={p:h[0] for p,h in ds.items()};res,cert=at_F(hs);closure_counts[res]+=1
   row=dict(v=v,X=x,H=h,histories={str(p):z for p,z in sorted(hs.items())},result=res,certificate=cert)
   if res=='open':
    assert x[0]=='N' and out(x,0)=='E'
    profiles[v,x,h]+=1
    if v in ['W','WW']:
     row['b_incidence_failure']=dict(required_predecessor=[2,0],required_departure='W',actual_first_R_departure='E')
    else:
     assert hs[(2,2)] in ['SNN','SNNS']
     row['upper_completion_obstruction']='65df766a: Z=EEWW,Y=SNNS,C=WWEE,R=SNN/SNNS, maximal Q'
   rows.append(row);return
  p=min((p for p,h in ds.items() if len(h)>1),key=lambda p:len(ds[p]))
  for candidate in ds[p]:
   nd=propagate(ds|{p:[candidate]})
   if nd is not None:visit(nd)
 visit(ds)
assert closure_counts=={'rank':358,'higher_C':6,'open':30}
assert profiles=={('W','NSSS','EWE'):4,('WW','NNS','WEE'):4,('WW','NNSS','WEEW'):4,('WWE','NNS','WEE'):6,('WWE','NNSS','WEEW'):6,('WWEW','NNSN','WEE'):6}
obj=dict(scope=__doc__,predecessor_complete_domain=predecessors,physical_translation=[-1,-1],selected_max_face=[1,0],opposite_face_not_assumed_max=[0,-1],local_counts=local_counts,local_modes=local_modes,local_nonport_rows=local_nonport,closure_counts=dict(closure_counts),open_profiles={str(k):v for k,v in profiles.items()},closure_rows=rows,
 dependencies={'WWE_WWEW':'Signed terminal supplier cover7d52e9b3 WITH be3d76da plus upper completion65df766a/auditb80c7a38'},
 warning='This excludes only the exact even-root portal on an actual GLOBAL-M essential b-circle with complete WHITE cap-four histories. No arbitrary mixed circle, all-cap interior maximum, fuel or translating-front exclusion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n')
print('PASS four incoming words; first-square3844 ->28 modes;394 full closures ->358rank+6higherC+30 open, then12 incidence failures+18 signed upper collisions')
