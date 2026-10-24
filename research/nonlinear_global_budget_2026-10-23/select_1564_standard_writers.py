#!/usr/bin/env python3
"""Finite complete-profile selector for supplied1564 word; no physical preparation inference."""
from pathlib import Path
from collections import defaultdict,Counter
import json,runpy
ROOT=Path(__file__).parent;E=runpy.run_path(str(ROOT/'endpoint_catalog.py'));J=json.loads((ROOT/'prepared_travelling_wave_certificate.json').read_text());p=tuple(J['wave_pose'][0]);h=J['wave_pose'][1];G=defaultdict(list)
for i,ch in enumerate(J['word']):
 x,y=p;t=x-y;a=x%14;k=(x-a)//14;G[t,a].append((k,i,ch));h=(h+(-1 if ch=='L'else 1))%4;v=E['V'][h];p=(p[0]+v[0],p[1]+v[1])
req={}
for(t,a),g in G.items():
 g.sort(key=lambda z:(-z[0],z[1]));j=(t,a%2);c=g[0][2]=='L'
 if j in req:assert req[j]==c
 req[j]=c
black={j for j,c in req.items()if c};white={j for j,c in req.items()if not c};read=set(req)
# Forward settled profiles from the signed endpoint's P24 low band.
F={j for j in E['PORB']if -28<=j[0]<=-18};assert len(F)==12
B={(-t,a)for t,a in F}
candidates=[]
for orientation,profile in[('SW',F),('NE',B)]:
 for delta in range(min(t for t,a in read)-max(t for t,a in profile),max(t for t,a in read)-min(t for t,a in profile)+1):
  if delta%2:continue
  for a in[0,1]:
   mask={(t+delta,(b+a)%2)for t,b in profile}
   if mask&white:continue
   hit=mask&black
   if not mask&read:kind='NEUTRAL'
   elif hit:kind='USEFUL'
   else:raise AssertionError
   lo,hi=min(t for t,b in mask),max(t for t,b in mask);candidates.append({'id':len(candidates),'orientation':orientation,'delta':delta,'a':a,'strip':[lo,hi],'black_profiles':sorted(mask),'required_black_hit':sorted(hit),'kind':kind})
# Exact covers using useful writers only, with disjoint eleven-level strips.
useful=[c for c in candidates if c['kind']=='USEFUL'];bycell={j:[c for c in useful if j in map(tuple,c['required_black_hit'])]for j in black};solutions=set()
def compatible(a,b):return a['strip'][1]<b['strip'][0]or b['strip'][1]<a['strip'][0]
def search(left,chosen):
 if not left:solutions.add(tuple(sorted(c['id']for c in chosen)));return
 j=min(left,key=lambda j:sum(all(compatible(c,x)for x in chosen)for c in bycell[j]))
 for c in bycell[j]:
  if all(compatible(c,x)for x in chosen):search(left-set(map(tuple,c['required_black_hit'])),chosen+[c])
search(set(black),[])
report={'scope':'Finite complete-profile compatibility and disjoint-strip selector only; no connected preparation, causal guards or finite seed theorem.','required_black_classes':sorted(black),'required_white_classes':sorted(white),'read2_class_count':len(read),'candidates':candidates,'useful_solution_ids':[list(s)for s in sorted(solutions)]}
(ROOT/'select_1564_standard_writers.json').write_text(json.dumps(report,indent=2)+'\n');print('READ2',len(read),'BLACK',len(black),'WHITE',len(white),'CAND',Counter(c['kind']for c in candidates),'SOLUTIONS',len(solutions))
for c in candidates:print(c['id'],c['orientation'],c['strip'],c['a'],c['kind'],'HITS',len(c['required_black_hit']))
for s in sorted(solutions):print('SOLUTION',[(candidates[i]['orientation'],candidates[i]['strip'],candidates[i]['a'])for i in s])

# Minimal exterior-return combinatorics. An all-strand snake fromSWtoSW needs
# four SW and three NE writers. With the fixed five usefulwriters this means
# exactlytwo additionalNEs, necessarilyoutside the active normal range.
def nc_matchings(signs,ids):
 if not ids:return[[]]
 out=[];i=ids[0]
 for k,j in enumerate(ids[1:],1):
  if signs[i]==signs[j]or k%2==0:continue
  for a in nc_matchings(signs,ids[1:k]):
   for b in nc_matchings(signs,ids[k+1:]):out.append([(i,j)]+a+b)
 return out

def snakes(signs,oldfree,newfree):
 n=len(signs);left=nc_matchings(signs,[i for i in range(n)if i!=oldfree]);right=nc_matchings(signs,[i for i in range(n)if i!=newfree]);good=[]
 for x in left:
  for y in right:
   adj=[[]for _ in range(n)]
   for i,j in x+y:adj[i].append(j);adj[j].append(i)
   seen={oldfree};todo=[oldfree]
   while todo:
    for q in adj[todo.pop()]:
     if q not in seen:seen.add(q);todo.append(q)
   if len(seen)==n:good.append({'oldside_matching':x,'remoteside_matching':y})
 return{'oldside_matching_count':len(left),'remoteside_matching_count':len(right),'connected_snakes':good}
minimal=[]
for lower_helpers in range(3):
 signs=[-1]*lower_helpers+[1,1,1,1,-1]+[-1]*(2-lower_helpers)
 minimal.append({'lower_helper_count':lower_helpers,'signs':signs,'fixed_original_SW_start':lower_helpers+1,'fixed_final_SW_end':lower_helpers+2,**snakes(signs,lower_helpers+1,lower_helpers+2)})
signs=[-1,1,1,1,1,-1,-1];alternate=snakes(signs,1,4);assert len(alternate['connected_snakes'])==1
report['minimal_two_exterior_return_fixed_endpoint_test']=minimal;report['alternative_endpoint_non_crossing_witness']={'signs':signs,'oldside_start_index':1,'remoteside_end_index':4,'strips':[[-72,-62],[-40,-30],[-28,-18],[-16,-6],[-2,8],[14,24],[42,52]],**alternate};(ROOT/'select_1564_standard_writers.json').write_text(json.dumps(report,indent=2)+'\n')
