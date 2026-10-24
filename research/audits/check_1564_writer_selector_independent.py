"""Fresh literal standard/wave reconstruction, exhaustive profiles and cap matchings."""
from pathlib import Path
from collections import defaultdict,Counter
from itertools import combinations,permutations
import json,hashlib
P=Path(__file__).resolve();ROOT=P.parents[1];R=ROOT/'nonlinear_global_budget_2026-10-23'
std=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());H=std['word'];dirs=(1j,1,-1j,-1)
p=-15+10j;h=std['heading'];hr=[];hh=[]
for c in H:
 hr.append(p);hh.append(h);h=(h+(1 if c=='R' else -1))%4;p+=dirs[h]
assert(p,h)==(-17+8j,3)
def xy(q):return(int(q.real),int(q.imag))
def old(q):
 x,y=xy(q);a=x%2;return(x-y,a),(a-x)//2
profile=set()
for q in hr:profile.symmetric_difference_update({old(q)[0]})
assert len(profile)==12 and {old(q)[0]for q in hr}=={(t,a)for t in range(-28,-17)for a in(0,1)}
J=json.loads((R/'prepared_travelling_wave_certificate.json').read_text());w=J['word'];p=complex(*J['wave_pose'][0]);h=J['wave_pose'][1];p0=p;h0=h;groups=defaultdict(list)
for i,c in enumerate(w):
 x,y=xy(p);a=x%14;k=(x-a)//14;groups[x-y,a].append((k,i,c));h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
assert(p,h)==(p0+14+14j,h0)and len(groups)==557
req={}
for(t,a),ls in groups.items():
 ls.sort(key=lambda r:r[1]-len(w)*r[0]);assert all(x[2]!=y[2]for x,y in zip(ls,ls[1:]))
 cl=t,a%2;col=ls[0][2]=='L';assert cl not in req or req[cl]==col;req[cl]=col
black={cl for cl,b in req.items()if b};white=set(req)-black;assert(len(req),len(black),len(white))==(167,60,107)
lo=min(t for t,a in req);hi=max(t for t,a in req);candidates=[];examined=0
for ori,base in [('SW',profile),('NE',{(-t,a)for t,a in profile})]:
 for shift in range(lo-max(t for t,a in base),hi-min(t for t,a in base)+1):
  if shift%2:continue
  for pa in(0,1):
   examined+=1;mask={(t+shift,(a+pa)%2)for t,a in base}
   if mask&white:continue
   candidates.append(dict(orientation=ori,delta=shift,a=pa,strip=[min(t for t,a in mask),max(t for t,a in mask)],black_profiles=sorted(map(list,mask)),required_black_hit=sorted(map(list,mask&black)),kind='USEFUL'if mask&black else'NEUTRAL'))
assert len(candidates)==5 and all(x['kind']=='USEFUL'and len(x['required_black_hit'])==12 for x in candidates)
author=json.loads((R/'select_1564_standard_writers.json').read_text());assert sorted(black)==list(map(tuple,author['required_black_classes']))and sorted(white)==list(map(tuple,author['required_white_classes']))
for a,b in zip(candidates,author['candidates']):assert a=={k:v for k,v in b.items()if k!='id'}
covers=[]
for flags in range(1<<len(candidates)):
 chosen=[candidates[i]for i in range(len(candidates))if flags>>i&1]
 if any(max(a['strip'][0],b['strip'][0])<=min(a['strip'][1],b['strip'][1])for a,b in combinations(chosen,2)):continue
 if set().union(*(set(map(tuple,c['required_black_hit']))for c in chosen))==black:covers.append([i for i in range(len(candidates))if flags>>i&1])
assert covers==author['useful_solution_ids']==[[0,1,2,3,4]]
# Enumerate every orientation-compatible matching by permutations, then reject crossings.
def matchings(signs,free):
 left=[i for i,s in enumerate(signs)if i!=free and s==1];right=[i for i,s in enumerate(signs)if i!=free and s==-1];assert len(left)==len(right)
 out=[]
 for perm in permutations(right):
  es=sorted(tuple(sorted(e))for e in zip(left,perm))
  if not any(a<c<b<d or c<a<d<b for(a,b),(c,d)in combinations(es,2)):out.append(es)
 return sorted(out)
def routes(signs,a,b):
 ma=matchings(signs,a);mb=matchings(signs,b);good=[]
 for x in ma:
  for y in mb:
   adj={i:[]for i in range(len(signs))}
   for i,j in x+y:adj[i].append(j);adj[j].append(i)
   seen={a};q=[a]
   while q:
    for j in adj[q.pop()]:
     if j not in seen:seen.add(j);q.append(j)
   if len(seen)==len(signs):good.append((x,y))
 return ma,mb,good
route_summary=[]
for n in range(3):
 signs=[-1]*n+[1,1,1,1,-1]+[-1]*(2-n);a,b,good=routes(signs,n+1,n+2);assert(len(a),len(b),len(good))==(1,1,0);route_summary.append([n,len(a),len(b),len(good)])
a,b,good=routes([-1,1,1,1,1,-1,-1],1,4);assert len(good)==1
expect=author['alternative_endpoint_non_crossing_witness']['connected_snakes'][0];assert good[0]==(sorted(map(tuple,expect['oldside_matching'])),sorted(map(tuple,expect['remoteside_matching'])))
# Exact causal-front joins. No author profile/clock routines are used.
bulk=set().union(*(set(map(tuple,c['black_profiles']))for c in candidates));last={(t+26,a)for t,a in profile};other=bulk-last;assert len(other)==48
join_author=json.loads((R/'wave_join_from_last_writer.json').read_text());joins=[]
for phase,q in enumerate(hr):
 q-=26j;z=p0-q
 if z.real!=z.imag or int(z.real)%2 or hh[phase]!=h0:continue
 copy=-int(z.real)//2;tau=104*copy+phase;rays=defaultdict(set);past={}
 for i,z in enumerate(hr):
  cl,k=old(z-26j);end=k+(tau-1-i)//104;rays[cl].symmetric_difference_update({end});past[cl]=max(past.get(cl,end),end)
 def col(q):
  cl,k=old(q);return(cl in other)^bool(sum(k<=v for v in rays[cl])%2)
 mismatch=set();critical=0
 for(t,a),ls in groups.items():
  rep=complex(a,a-t);cl,krep=old(rep);start=min(k for k,i,c in ls)
  # These are all changes of eligibility or any XOR ray; beyond max the answer is constant.
  breaks={start}|{k for k,i,c in ls if k>=start}
  for th in rays[cl]:
   change=-((th-krep)//7) # ceil((krep-th)/7)
   if change>=start:breaks.add(change)
  stop=max(breaks);critical+=len(breaks)
  for n in range(start,stop):
   desired=next(c=='L'for k,i,c in ls if k<=n);point=rep+n*(14+14j)
   if col(point)!=desired:mismatch.add(point)
  assert all(k<=stop for k,i,c in ls)
  assert col(rep+stop*(14+14j))==(ls[0][2]=='L')
 erased={q for q in mismatch if col(q)};overlap={q for q in mismatch if old(q)[0]in past and old(q)[1]<=past[old(q)[0]]}
 row=next(r for r in join_author['phase_results']if r['H_phase']==phase)
 assert(copy,tau)==(row['H_copy'],row['tau'])
 assert sorted(map(list,map(xy,mismatch)))==row['mismatch_cells']
 assert sorted(map(list,map(xy,erased)))==row['erasures']and sorted(map(list,map(xy,overlap)))==row['strict_past_overlap']
 joins.append(dict(phase=phase,copy=copy,tau=tau,toggles=len(mismatch),erasures=len(erased),past_overlap=len(overlap),all_change_boundaries=critical))
assert [(r['phase'],r['toggles'],r['erasures'],r['past_overlap'])for r in joins]==[(11,7,5,7),(19,6,4,6),(23,7,6,7),(39,8,3,3)]
out=dict(status='PASS independent literal profiles, exhaustive selector, all cap matchings and exact all-future causal joins',note_sha256=hashlib.sha256((R/'1564_writer_selector_and_routing_scope.md').read_bytes()).hexdigest(),candidate_profiles_tested=examined,required_classes=len(req),black_classes=len(black),white_classes=len(white),useful_writers=candidates,unique_covers=covers,fixed_endpoint_minimal_helper_cases=route_summary,alternative_matching=good,joins=joins,scope='Complete untouched common bulk and minimal two-exterior-helper topology only. Direct fixed-pose joins are not fresh additions; finite scattering prelude and arbitrarily many exterior helper pairs remain open.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
