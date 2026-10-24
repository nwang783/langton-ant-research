"""Shortest odd-root nonsquare return and its complete necessary RR interface.
A fixed local cover with arbitrary prior WHITE stock, not a front/period scan.
The literal three-black transfer is a separate genuine finite prepared factor.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict,Counter
import json
base=Path(__file__).parent;H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def add(p,dr,sgn=1):return(p[0]+sgn*V[dr][0],p[1]+sgn*V[dr][1])
def rr(h,dr,kind):return[r for r in range(len(h))if(h[r]if kind=='in'else out(h,r))==dr]
# All eight-step full-pose first returns from incoming E, first turn L.
raw=[];legal=[]
for tail in product('RL',repeat=7):
 w='L'+''.join(tail);p=(0,0);h=1;hh=defaultdict(str);trace=[];early=False
 for i,l in enumerate(w):
  trace.append(dict(time=i,cell=p,incoming=H[h],turn=l));hh[p]+=l
  h=(h+(1 if l=='R'else-1))%4;p=add(p,H[h])
  if p==(0,0)and i<7:early=True
 if p!=(0,0)or h!=1 or early:continue
 raw.append(w)
 if any(any(a==b for a,b in zip(v,v[1:]))for v in hh.values()):continue
 legal.append(dict(word=w,trace=trace,cell_letters=[dict(cell=p,letters=v)for p,v in hh.items()]))
assert len(raw)==5 and [r['word']for r in legal]==['LLRRRRLL','LLLRRRRL']
# Genuine prepared stock transfer; NOT a full WHITE history or controller.
seed={(0,0),(0,1),(-1,0)};board=set(seed);p=(0,0);h=1;trace=[]
for i,w in enumerate('LLRRRRLL'):
 turn='L'if p in board else'R';assert turn==w
 trace.append(dict(time=i,cell=p,incoming=H[h],turn=turn,board_before=sorted(board)))
 board.symmetric_difference_update({p});h=(h+(1 if turn=='R'else-1))%4;p=add(p,H[h])
assert p==(0,0)and h==1 and board=={(0,1),(-1,2),(0,2)}and len(board)==len(seed)==3
literal=dict(seed_black=sorted(seed),initial_pose=[0,0,'E'],word='LLRRRRLL',trace=trace,final_pose=[0,0,'E'],final_black=sorted(board),black_mass_change=0,repeat_failure='The same word cannot repeat immediately: the root is WHITE after8, so its next read is R, not the required initial L.')
# Reuse the signed generic physical port/next-rank/clock/dual-height checker only.
ss=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0]
ss=ss.replace("val={(0,-1):0};q=deque([(0,-1)])","val={(0,1):0};q=deque([(0,1)])")
ns={};exec(ss,ns);check=ns['check']
def words(axis):return[''.join(x)for n in range(1,5)for x in product(axis,repeat=n)]
def exposure(hs):
 succ={};starts=[];ends={};ext=set();internal=[]
 for p,h in hs.items():
  for dr in H:
   q=add(p,dr);sr=rr(h,dr,'out')
   if q in hs:
    tr=rr(hs[q],dr,'in');assert len(sr)==len(tr)
    for j,(a,b)in enumerate(zip(sr,tr)):
     succ[p,a]=(q,b);internal.append(dict(source=p,source_rank=a,target=q,target_rank=b,heading=dr,ordinal=j+1))
   else:
    ext.add(q)
    for j,a in enumerate(sr):ends[p,a]=(q,dr,j)
   q0=add(p,dr,-1)
   if q0 not in hs:
    ext.add(q0)
    for j,a in enumerate(rr(h,dr,'in')):starts.append((q0,dr,j,(p,a)))
 loops=[];channels=[]
 for x,dr,j,cur in starts:
  route=[]
  while True:
   assert cur not in route;route.append(cur)
   if cur not in succ:break
   cur=succ[cur]
  y,di,k=ends[cur];rec=dict(source_external=x,departure_heading=dr,departure_ordinal=j+1,target_external=y,arrival_heading=di,arrival_ordinal=k+1,steps=len(route)+1,named_route=route)
  channels.append(rec)
  if x==y:loops.append(rec)
 candidates=[]
 for x in sorted(ext):
  req=[]
  for dr in H:
   y=add(x,dr)
   if y in hs:req.append(('out',dr,len(rr(hs[y],dr,'in'))))
   y=add(x,dr,-1)
   if y in hs:req.append(('in',dr,len(rr(hs[y],dr,'out'))))
  axis='NS'if sum(x)%2==0 else'EW';good=[]
  for h in words(axis):
   if any(len(rr(h,d,k))!=m for k,d,m in req):continue
   if any(rr(h,l['arrival_heading'],'in')[l['arrival_ordinal']-1]!=rr(h,l['departure_heading'],'out')[l['departure_ordinal']-1]+1 for l in loops if l['source_external']==x):continue
   good.append(h)
  assert good
  candidates.append(dict(cell=x,required_port_counts=req,complete_WHITE_histories=good))
 return dict(all_internal_ordinal_edges=internal,all_named_channels=channels,same_external_first_return_obligations=loops,all_unfilled_external_helpers=candidates)
counts=Counter();rows=[]
for b,d,e,p,q in product(['WWE','WWEE'],words('NS'),words('EW'),['NNSS','NSSN'],['EEWW','EWWE']):
 hs={(0,1):'WEE',(0,2):'NNSS',(-1,1):'NSSN',(-1,2):b,(-1,3):d,(0,3):e,(1,2):'WWEE',(1,3):p,(2,3):q,(2,2):'NNSS'}
 ans=check(hs);counts[ans]+=1
 if ans!='open':continue
 ex=exposure(hs);succ={(tuple(x['source']),x['source_rank']):(tuple(x['target']),x['target_rank'])for x in ex['all_internal_ordinal_edges']}
 route=[((0,1),1)];cur=route[0]
 for _ in range(8):cur=succ[cur];route.append(cur)
 assert route[-1]==((0,1),2)
 got=''.join('R'if r%2==0 else'L'for _,r in route[:-1]);assert got=='LLRRRRLL'
 assert route[3]==((-1,3),0)and route[4]==((0,3),0)
 loops=ex['same_external_first_return_obligations'];assert len(loops)==1
 lp=loops[0];assert lp['source_external']==(1,1)and lp['departure_heading']=='W'and lp['departure_ordinal']==1 and lp['arrival_heading']=='S'and lp['arrival_ordinal']==2 and lp['steps']==4
 k=next(r for r in ex['all_unfilled_external_helpers']if r['cell']==(1,1));assert set(k['complete_WHITE_histories'])=={'SS','SSN'}
 assert p=='NSSN'
 kh=[]
 for kk in k['complete_WHITE_histories']:
  assert check(hs|{(1,1):kk})=='open';kh.append(kk)
 rows.append(dict(variable_profiles=dict(B=b,D=d,E=e,P=p,Q=q),complete_named_histories=[dict(cell=z,history=h)for z,h in sorted(hs.items())],eight_step_actual_route=route,K_extensions=kh,**ex))
assert sum(counts.values())==7200 and len(rows)==14
assert dict(counts)=={'port':7040,'skipped_rank':138,'open':14,'clock_cycle':6,'global_C_max':2}
obj=dict(scope=__doc__,eight_step_raw_full_pose_words=raw,eight_step_letter_legal_words=legal,literal_prepared_transfer=literal,complete_neighbor_cover_counts=dict(counts),necessary_open_rows=rows,warning='The14 rows and their exposed-helper choices are necessary OPEN networks, not physical board factors, assigned period phases, a single event orbit or complete WHITE translating fronts. Only the separate explicit8-word seed replay is a genuine prepared finite factor. Old D/E histories were allowed in the7200 cover; all14 survivors force their displayed R0 reads.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS two legal8 returns; prepared3-black transfer;7200 full-stock neighborhoods ->14 open; K=SS/SSN survives')
