from pathlib import Path
import json,re
D=json.load(open('spaced_fresh_intersections.json'))['best'];M=json.load(open('spaced_two_marker_macros.json'))['macros'];Q=json.load(open('spaced_two_marker_port_quotient.json'));A={}
for u,a,v in Q['quotient_edges']:A.setdefault(u,[]).append((a,v))
steps=((0,1),(1,0),(0,-1),(-1,0));last={};seed=set();p=(0,0);h=0;trace=[];raw=D['prehistory'];starts=[];state=D['initial_class']
for i,a in enumerate(D['macros']):starts.append(len(raw));raw+=M[a]['word'];state=dict(A[state])[a]
full=raw+M[D['macros'][-1]]['end_marker'];goal=len(D['macros'])-1;goalstart=starts[-1];cut=len(D['prehistory']);goalfirst={};sources={}
for t,c in enumerate(full):
 if t==goalstart:prior=dict(last);goalpose=(*p,h)
 assert last.get(p,(-1,None))[1]!=c,(t,p,c,last.get(p))
 if p not in last and c=='L':seed.add(p)
 if t>=goalstart and p not in goalfirst:
  goalfirst[p]=c
  if c=='L':sources[p]=prior.get(p)
 last[p]=(t,c);trace.append((p,c));h=(h+(1 if c=='R'else-1))%4;p=(p[0]+steps[h][0],p[1]+steps[h][1])
assert all(v is not None and v[0]>=cut for v in sources.values())
B=set(seed);masscut=massgoal=None
for t,(p,c)in enumerate(trace):
 if t==cut:masscut=len(B)
 if t==goalstart:massgoal=len(B)
 assert (p in B)==(c=='L');B.symmetric_difference_update((p,))
W=re.search(r'const string W="([LR]+)"',open('enumerate_adjacent_pair_spacing.cpp').read()).group(1);F={(W+W)[i:i+10]for i in range(104)};J=[False]*9+[full[i-9:i+1]not in F for i in range(9,len(full))];K=[i for i in range(10,len(full))if J[i]and J[i-1]];assert all(b-a>=140 for a,b in zip(K,K[1:]));assert any(i>=goalstart for i in K)
def fits(w):
 last={};p=(0,0);h=0
 for t,c in enumerate(w):
  if last.get(p)==c:return False
  last[p]=c;h=(h+(1 if c=='R'else-1))%4;p=(p[0]+steps[h][0],p[1]+steps[h][1])
 return True
front=[(state,raw,[])];levels=[]
for depth in range(1,9):
 nxt=[]
 for q,w,ext in front:
  for a,r in A[q]:
   ww=w+M[a]['word']
   if fits(ww+M[a]['end_marker']):nxt.append((r,ww,ext+[a]))
 levels.append({'depth':depth,'feasible_continuations':len(nxt),'example':nxt[0][2]if nxt else None});front=nxt
 if not front or len(front)>100000:break
source_records=[]
for q,(t,c)in sources.items():
 j=max(i for i,s in enumerate(starts)if s<=t);source_records.append({'cell':q,'last_turn':t,'last_letter':c,'macro_index':j,'macro_type':D['macros'][j],'phase':t-starts[j]})
out={'status':'literal finite-field zero-fuel event verified','prehistory':D['prehistory'],'macro_ids':D['macros'],'seed':sorted(seed),'turn_word':full,'mass_at_macro_cut':masscut,'mass_at_goal_cut':massgoal,'goal_pose':goalpose,'goal_type':D['macros'][-1],'goal_first_L_sources':source_records,'adjacent_pair_endings':K,'min_pair_gap':min(b-a for a,b in zip(K,K[1:])),'continuations':levels};Path('spaced_zero_fuel_verified.json').write_text(json.dumps(out,indent=2));print({k:v for k,v in out.items()if k not in('seed','turn_word','prehistory','goal_first_L_sources')});print('last-writer macro indices',[x['macro_index']for x in source_records])
