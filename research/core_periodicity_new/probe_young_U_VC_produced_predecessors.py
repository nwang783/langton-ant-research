"""One targeted exact partial-board predecessor probe, full initial-origin funding.
No no-hit from a node budget. Output positives require whole literal replay.
"""
from pathlib import Path
import json,hashlib,heapq,time,sys
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';RP=R/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json';G=json.loads(GP.read_text())['geometry'];RJ=json.loads(RP.read_text());A=RJ['core_offsets'];T={(a,h):t for a,h,t in RJ['created_peaks']};ids=(0,1,4,5,6,7,8,9);DIR=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};suffix=[5,5,5,4,0,7];S=28;Iweight=28;CAP=int(sys.argv[1])if len(sys.argv)>1 else 100000
watch=[(0,3),(1,2),(4,0),(2,-1),(3,-1)];minimum=[2,3,2,2,2]
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def plus(p,q):return p[0]+q[0],p[1]+q[1]
def trace(word,p=(0,0),h=0):
 B=set();W=set()
 for ch in word:
  if ch=='L':
   if p in W:return None
   B.add(p)
  else:
   if p in B:return None
   W.add(p)
  # Move this required board backwards through all earlier flips by maintaining
  # initial parity separately; the direct initializer below is clearer.
  h=(h+(-1 if ch=='L'else 1))%4;p=plus(p,DIR[h])
 return B,W
word=''.join(G[a]['word']for a in suffix)+G[7]['marker'];p=(0,0);h=0;B=set();W=set();par=set()
for ch in word:
 need=(ch=='L')^(p in par)
 assert p not in(W if need else B)
 (B if need else W).add(p)
 if p in par:par.remove(p)
 else:par.add(p)
 h=(h+(-1 if ch=='L'else 1))%4;p=plus(p,DIR[h])
B=frozenset(B);W=frozenset(W);assert len(B)==16 and all(q in B for q in watch)
# Oriented packet masks, independent of head translation.
ops={}
for a in ids:
 for h in range(4):
  ctxB={rot(q[:2],h)for q in G[a]['requirements']if q[2]};ctxW={rot(q[:2],h)for q in G[a]['requirements']if not q[2]};X={rot(q,h)for q in G[a]['raw_odd']};O={rot(q,h)for q in G[a]['outputs']}
  ops[a,h]=(ctxB,ctxW,X,O,rot(G[a]['endpoint'][:2],h),G[a]['name'].count('C'))
def core(p,h):return{plus(p,rot(q,h))for q in K}
def badblack(B,p,h):return{q for q in B-core(p,h)if Iweight+2*sum(q)>=S}
def replay(prefix,start):
 pp,hh=start;full=prefix+suffix;initial=set(nodes[current]['B']);C0=core(pp,hh);assert C0<=initial
 Board=set(initial);ledger={q:('entry',None)for q in initial-C0};clock=0;records=[];vcindex=len(prefix);target_births=None
 for j,a in enumerate(full):
  C=core(pp,hh);assert C.isdisjoint(ledger)and Board==C|set(ledger)
  inp=[plus(pp,rot(q,hh))for q in G[a]['inputs']];births=[ledger[q]for q in inp]
  for q,v in zip(inp,births):
   if v[0]=='entry':assert Iweight+2*sum(q)<S,(j,q,'initial funding')
  ev=2*sum(pp)+A[hh];cr=2*sum(pp)+T[a,hh]
  assert max(ev,cr)<S if j<len(full)-1 else cr==S
  if j==vcindex:
   assert(pp,hh)==((0,0),0)
   ages=[clock-ledger[q][1]if ledger[q][1]is not None else None for q in watch]
   assert all(x is not None and x>=r for x,r in zip(ages,minimum)),ages
  if j==len(full)-1:
   target_births=births;assert[clock-b[1]for b in births[:2]]==[3,3]and all(b[0]<vcindex and clock-b[1]>=5 for b in births[2:])
  records.append(dict(index=j,packet=a,pose=[*pp,hh],C_clock=clock,entry_core=ev,created_peak=cr,input_cells=inp,input_births=births))
  for q in inp:del ledger[q]
  for q in G[a]['outputs']:
   z=plus(pp,rot(q,hh));assert z not in ledger;ledger[z]=(j,clock)
  for ch in G[a]['word']:
   assert(ch=='L')==(pp in Board)
   if pp in Board:Board.remove(pp)
   else:Board.add(pp)
   hh=(hh+(-1 if ch=='L'else 1))%4;pp=plus(pp,DIR[hh])
  clock+=G[a]['name'].count('C')
 for ch in G[7]['marker']:
  assert(ch=='L')==(pp in Board)
  if pp in Board:Board.remove(pp)
  else:Board.add(pp)
  hh=(hh+(-1 if ch=='L'else 1))%4;pp=plus(pp,DIR[hh])
 return dict(prefix=prefix,fullword=full,initial_pose=[*start[0],start[1]],seed=sorted(initial),mass=len(initial),records=records)
# nodes are exact suffix predecessor requirements; cap3 C age is exact for all
# five >=threshold birth tests. Resolved targets need no protection farther back.
nodes=[];seen=set();todo=[];stats=dict(pops=0,attempts=0,record_cuts=0,origin_cuts=0,age_cuts=0,color_cuts=0,duplicates=0)
def add(B,W,p,h,unresolved,c,par,a):
 key=(B,W,p,h,unresolved,c)
 if key in seen:stats['duplicates']+=1;return
 seen.add(key);dep=0 if par<0 else nodes[par]['depth']+1;bad=badblack(B,p,h);n=dict(B=B,W=W,p=p,h=h,mask=unresolved,c=c,par=par,a=a,depth=dep,bad=bad);idx=len(nodes);nodes.append(n)
 score=dep+30*len(bad)+15*unresolved.bit_count();heapq.heappush(todo,(score,dep,idx))
add(B,W,(0,0),0,31,0,-1,-1);t0=time.time();hit=None;current=-1
while todo and len(nodes)<CAP:
 score,depth,current=heapq.heappop(todo);n=nodes[current];stats['pops']+=1
 if n['mask']==0 and not n['bad']:
  pref=[];q=current
  while nodes[q]['par']>=0:pref.append(nodes[q]['a']);q=nodes[q]['par']
  hit=replay(pref,(n['p'],n['h']));break
 for a in ids:
  stats['attempts']+=1;dh=G[a]['endpoint'][2];h=(n['h']-dh)%4;cb,cw,x,o,e,cc=ops[a,h];p=n['p'][0]-e[0],n['p'][1]-e[1]
  if 2*sum(p)+max(A[h],T[a,h])>=S:stats['record_cuts']+=1;continue
  O={plus(p,q)for q in o};C={plus(p,q)for q in cb|cw};mask=n['mask'];c=min(3,n['c']+cc);bad=False
  for j,q in enumerate(watch):
   if not(mask>>j&1):continue
   if q in O:
    if c<minimum[j]:stats['age_cuts']+=1;bad=True;break
    mask&=~(1<<j)
   elif q in C:stats['origin_cuts']+=1;bad=True;break
  if bad:continue
  X={plus(p,q)for q in x};BB=(n['B']-X)|(n['W']&X);WW=(n['W']-X)|(n['B']&X);QB={plus(p,q)for q in cb};QW={plus(p,q)for q in cw}
  if BB&QW or WW&QB:stats['color_cuts']+=1;continue
  add(frozenset(BB|QB),frozenset(WW|QW),p,h,mask,c,current,a)
  if len(nodes)>=CAP:break
 if stats['pops']%1000==0:print(json.dumps(dict(**stats,labels=len(nodes),queue=len(todo),depth=depth,score=score,best_unresolved=n['mask'].bit_count(),best_forbidden_initial=len(n['bad']),seconds=round(time.time()-t0,2))),flush=True)
status='ACTUAL_FULL_PREFIX_CONTROL'if hit else 'CAP_UNKNOWN'if todo else 'EXACT_STATE_EXHAUSTION_PENDING_AUDIT'
J=dict(status=status,scope='Only fixed VC,VC,VC,V,D,U suffix; full initial activation I28/S28, exact partial-board constraints, genuine production+ages of5pre-VC identities. A cap is UNKNOWN, no general record exclusion.',I=Iweight,S=S,suffix=suffix,watch=watch,minimum_pre_VC_ages=minimum,labels=len(nodes),remaining_queue=len(todo),stats=stats,seconds=time.time()-t0,control=hit,best_queued=[] if not todo else[dict(score=s,depth=d,pose=[*nodes[q]['p'],nodes[q]['h']],unresolved=nodes[q]['mask'],forbidden_initial=sorted(nodes[q]['bad']))for s,d,q in heapq.nsmallest(5,todo)],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,RP,Path(__file__).resolve()]})
OUT=R/'chronology_dcuv/young_U_VC_produced_predecessors.json';OUT.write_text(json.dumps(J,indent=2)+'\n');print(json.dumps({k:v for k,v in J.items()if k not in('control','best_queued')},indent=2))
