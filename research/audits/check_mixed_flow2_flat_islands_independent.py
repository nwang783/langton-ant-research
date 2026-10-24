from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();PF=D/'global_max_mixed_flow2_roots_have_only_flat_local_islands.md';assert sha(PF)=='c9574fb8a1a2d8d592cbd06d601a49ef241eec6d18c6c50cfa3497ee83e8259d';C=D/'mixed_O_triple_helper_uncapped_count_control.json';J=json.loads(C.read_text());H='NESW';V={'N':1j,'E':1,'S':-1j,'W':-1};out=lambda w:[H[(H.index(c)+(1 if r%2==0 else-1))%4]for r,c in enumerate(w)];rank=lambda w,d,output=False:[r for r,c in enumerate(out(w)if output else w)if c==d]
profiles={'u':'WEE','s':'NSN','w':'WEEE'};positions={'u':1j,'s':2j,'w':1+2j};edges=[]
for a,b,d in [('u','s','N'),('s','w','E')]:
 src=rank(profiles[a],d,True);dst=rank(profiles[b],d);assert len(src)==len(dst);edges += [(a,r,b,s)for r,s in zip(src,dst)]
assert('u',0,'s',0)in edges and('s',0,'w',1)in edges
assert rank(profiles['u'],'W')==[0]and rank(profiles['w'],'S',True)==[2]
# Exact soleS/Wout1 count algebra derives n1 or n4/5, not a truncation.
rows=[]
for n in(1,4,5):
 for j in range(n):
  if n//2!=(0 if j%2==0 else 2):continue
  w='N'*j+'S'+'N'*(n-j-1);dep=rank(w,'W',True);assert len(dep)==1
  rows.append(dict(history=w,S_rank=j,W_rank=dep[0],W_before_S=dep[0]<j,height_raise=n-2))
canon=lambda x:json.dumps(x,sort_keys=True);assert set(map(canon,rows))==set(map(canon,J['all_count_profiles']))
surv=[r['history']for r in rows if r['W_before_S']];assert surv==J['strict_survivors']==['NNNS','NNNSN']
heights={}
for helper in surv:
 raw={positions[k]:v for k,v in profiles.items()};raw[1+1j]=helper;eq={};adj=defaultdict(list)
 for p,w in raw.items():
  ia='NS'if(int(p.real)+int(p.imag))%2==0 else'EW';oa='EW'if ia=='NS'else'NS'
  for d in oa:
   key=p,d;f=out(w).count(d)
   if key in eq:assert eq[key]==f
   eq[key]=f
  for d in ia:
   key=p-V[d],d;f=w.count(d)
   if key in eq:assert eq[key]==f
   eq[key]=f
 for(p,d),f in eq.items():
  c,l={'E':(p-1j,p),'W':(p-1,p-1-1j),'N':(p,p-1),'S':(p-1-1j,p-1j)}[d];adj[l].append((c,f));adj[c].append((l,-f))
 vals={1j:0};todo=[1j]
 while todo:
  p=todo.pop()
  for q,f in adj[p]:
   if q in vals:assert vals[q]==vals[p]+f
   else:vals[q]=vals[p]+f;todo.append(q)
 assert vals[0]==-1 and vals[1]==len(helper)-2;heights[helper]={'shared_C':0,'L_SW':vals[0],'other_C':vals[1]}
# Bind the existing complete mixed gates and independently filter the signed staircase relation.
deps=['check_mixed_U_triple_uncapped_independent.json','check_high_sink_nesting_independent.json','check_mixed_RR_closure_independent.json','check_global_max_flow2_staircase_independent.json','check_mixed_first_track_pipeline_independent.json']
reports={f:json.loads((S.parent/f).read_text())for f in deps};sw=reports['check_global_max_flow2_staircase_independent.json'];windows=[tuple(r['word'])for r in sw['open_words']if r['open']];assert len(windows)==8
urows=[r for r in windows if r[2]=='U'];assert len(urows)==4 and all(r[3]=='X'and r[4]in'OU'for r in urows)
nested=[]
for vv in('WEE','WEEW'):
 hs={0j:'WEEW',1j:'NNSS',1+1j:vv};ee=[]
 for p in hs:
  for d,z in V.items():
   q=p+z
   if q not in hs:continue
   src=rank(hs[p],d,True);dst=rank(hs[q],d);assert len(src)==len(dst);ee +=[(p,r,q,s)for r,s in zip(src,dst)]
 assert all(e in ee for e in[(0j,0,1j,0),(1j,0,1+1j,1),(0j,1,1j,1),(1j,3,1+1j,2)])
 nested.append(dict(next_left=vv,first_clock='T1v=T0u+2<=T1u-2',last_clock='T2v=T3X+1>=T1u+10'))
islands=[r for r in windows if r[2]=='O'and r[0]!='U'];assert islands==[('V','Y','O','X','V'),('V','Y','O','Y','V')]
ll=reports['check_high_sink_nesting_independent.json']['critical_LL_seven_rows'];roots=[h for h in ll if h['Y']!='EEWW'];assert len(roots)==2 and all(h['Z']=='NNSS'and h['A']=='EEWW'and h['B']=='SNNS'and h['Y']in('EWW','EWWE')for h in roots)
outobj=dict(status='PASS global-max critical mixed flow2 roots have only flat local islands, hence require two distinct flat RIGHT classes',proof_sha256=sha(PF),control_sha256=sha(C),dependencies={str((S.parent/f).relative_to(R)):sha(S.parent/f)for f in deps},derived_O_helper_profiles=rows,strict_helper_heights=heights,singleton_U_nested_routes=nested,singleton_O_windows=islands,LL_root_rows=roots,analytic_review=[
'Exact uO,sNSN,wWEEE first strand gives T1w=T0u+2 and helperW=T0u-1<S=T2w+1. Sin1/Wout1 derives n1 or4/5. OnlyNNNS/NNNSN survive; unrestricted all-port curl raises otherC by2/3. With the separately signed U case, GLOBAL selected C maximum excludes both outgoing high-source interfaces without a cap4 maximum shortcut at the helper.',
'Every f2root already has a flat RIGHT predecessor by signed critical incoming nesting. For a singleton root, outgoing source4 forces RR; source3 followedRIGHT also forcesRR; general mixedLRRL forbids both besideO/U. Source3 followedLEFT is exactly the newly excluded higher-C helper. Thus both neighboringRIGHT are flat. LL roots are already exactly the two old flat-end rows; passiveV/V zero-chord notches remain.',
'Outer neighbors of a singleton root cannot beRIGHT by the same generalRR gate; since adjoining edges haveflow2 they areLEFTflow2. Therefore the signed full five-corner constant2 stencil applies even in a globally mixed circle. Every currentU row forces followingX and nextO/U. Literal first/late ordinals put nextrootL1 strictly beforeuL1 and nextrootR2 strictly afteruL1, violating pairwise disjoint actual critical LEFT intervals. No assumed second staircase window or old-age bound is used.',
'With singletonU excluded, the priorU alternatives in a currentO window are impossible too: last-LEFT gate makes that prior crossing itself singleton. Remaining singleton islands are preciselyV,Y,O,X-or-Y,V; LLfirstO/U retainsY,O/U,V,X and its actual four-L cleanup. All outside high3/4 and old stock remain possible.',
'LLflanks have different complete flat types. If singletonO flanks share one full-quotient class, the b permutation cycle has length2; then the displayed outerV cap is a full-drift translate ofO, impossible for their complete histories. Thus at least two distinct flat classes are necessary. This closes the one-flat WITH-f2root branch only, not one-flat with onlyflow3, arbitrary nonmaximal/front cases or the general one-use problem.'
]);S.with_suffix('.json').write_text(json.dumps(outobj,indent=2)+'\n');print(outobj['status']);print(sha(S.with_suffix('.json')))
