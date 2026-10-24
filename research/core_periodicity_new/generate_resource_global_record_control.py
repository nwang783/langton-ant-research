"""Entire marked-prefix record abstraction with retained initial activations.
CLI PROFILE POTENTIAL TARGET TARGET_GLOBAL_PHASE PREFIX 'inputs|context|file:JSON' [all|inputs]
No source anchor or unproved clauses. Initial entry pose is arbitrary, core tags unknown.
Code0 white,1 black unknown/core,2 black initial residual,3 black produced residual.
"""
from pathlib import Path
import json,sys,hashlib,itertools
from resource_profile import load_profile
profile,potential=map(Path,sys.argv[1:3]);target,phase=map(int,sys.argv[3:5]);out=Path(sys.argv[5]);mode=sys.argv[6];watchmode=sys.argv[7]if len(sys.argv)>7 else'all';P,D,M=load_profile(profile);W=json.loads(potential.read_text());assert W['profile_sha256']==M['resource_profile_sha256'];G=D['geometry']['geometry'];keep=P['keep'];core=D['geometry']['core'];v=W['values'];direction=(v['ax'],v['ay'])
def rot(q,h):x,y=q;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(q):return sum(a*b for a,b in zip(direction,q))
def A(h):return L(rot((-1,1),h))+v[f'c{h%4}']
def T(a,h):
 h%=4;g=G[a];e=g['endpoint'];return max([2*L(rot(e[:2],h))+A(h+e[2])]+[2*L(rot(q,h))+v[f'w_{a}_{i}_{h}']for i,q in enumerate(g['outputs'])])
S=T(target,phase);assert S>A(phase);I=max(T(a,h)-2*L(rot(q,h))for a in keep for h in range(4)for q in G[a]['inputs'])
points=set(map(tuple,G[target]['inputs']))
if mode=='context':points|={tuple(r[:2])for r in G[target]['requirements']}
elif mode.startswith('file:'):points|=set(map(tuple,json.loads(Path(mode.split(':',1)[1]).read_text())))
else:assert mode=='inputs'
points=sorted(points);watch=set(points)if watchmode=='all'else set(map(tuple,G[target]['inputs']));ix={p:i for i,p in enumerate(points)};cells=[];n=0
for i,q in enumerate(points):
 bits=2 if q in watch else 1;cells.append({'cell':q,'offset':n,'bits':bits,'watched':bits==2});n+=bits
assert n<=50,('engine variable cap',n)
heads=set()
for a in keep:
 for h in range(4):
  for rr in G[a]['requirements']:
   z=rot(rr[:2],h)
   for q in points:
    p=(q[0]-z[0],q[1]-z[1])
    if (sum(p)+h)%2==0:heads.add((*p,h))
heads=sorted(heads);si={p:i for i,p in enumerate(heads)};init=len(heads);OUT=init+1;re=set();trans=[];initial_edges=[];near_edges=[]
# Initial arbitrary patch colors: watched cells0/2, unwatched0/1.
sk=sum(1<<c['offset']for c in cells if c['watched']);start=[init,sk,0]
for sid,(x,y,h)in enumerate(heads):
 if 2*L(rot((x,y),phase))+A(h+phase)<S:
  clear=reset=0
  initialcore={(x+z[0],y+z[1])for p in core for z in [rot(p,h)]}
  for c in cells:
   if tuple(c['cell'])in initialcore:
    mask=((1<<c['bits'])-1)<<c['offset'];clear|=mask;reset|=1<<c['offset']
  initial_edges.append(len(trans));trans.append([init,sid,0,0,0,clear,reset,0,-1])
 for a in keep:
  g=G[a];e=g['endpoint'];z=rot(e[:2],h);dest=(x+z[0],y+z[1],(h+e[2])%4);to=si.get(dest,OUT);goal=(a==target and(x,y,h)==(0,0,0));peak=2*L(rot((x,y),phase))+max(A(h+phase),T(a,h+phase))
  hh=(h-e[2])%4;zz=rot(e[:2],hh);pred=(x-zz[0],y-zz[1],hh)
  if pred not in si:re.add(sid)
  if not goal and peak>=S:continue
  req={tuple(r[:2]):bool(r[2])for r in g['requirements']};odd=set(map(tuple,g['raw_odd']));inputs=set(map(tuple,g['inputs']));outputs=set(map(tuple,g['outputs']));branches=[(0,0)];flip=clear=reset=0
  for c in cells:
   q=c['cell'];off=c['offset'];bits=c['bits'];zz=rot((q[0]-x,q[1]-y),-h)
   if zz not in req:assert zz not in odd;continue
   black=req[zz]
   if bits==1:
    branches=[(kk|(1<<off),vv|(int(black)<<off))for kk,vv in branches]
    if zz in odd:flip|=1<<off
    continue
   if not black:allowed=[(3,0)]
   elif goal and zz in inputs:allowed=[(3,3)]
   elif False and zz in inputs and 2*L(rot(q,phase))+I>=S:allowed=[(1,1)] # unknown1 or produced3, never initial2
   else:allowed=[(1,1),(3,2)]
   branches=[(kk|(mk<<off),vv|(mv<<off))for kk,vv in branches for mk,mv in allowed]
   final=3 if zz in outputs else int(black^(zz in odd));clear|=3<<off;reset|=final<<off
  if goal:assert inputs<=watch
  for kk,vv in branches:near_edges.append(len(trans));trans.append([sid,to,kk,vv,flip,clear,reset,int(goal),a])
# Arbitrarily far initial entry has no core/patch intersection; hidden intervals omit cuts.
initial_edges.append(len(trans));trans.append([init,OUT,0,0,0,0,0,0,-1])
J={**M,'format':'CONTROL_ONLY_funding_allowed_global_record_prefix','n':n,'points':points,'poses':heads,'initial_control_pose':init,'out':OUT,'start':start,'transitions':trans,'reentry':sorted(re),'keep':keep,'target':target,'target_global_phase':phase,'target_pose':[0,0,0],'potential_file':str(potential.resolve()),'potential_sha256':hashlib.sha256(potential.read_bytes()).hexdigest(),'record_threshold':S,'initial_token_weight':I,'core_offsets':[A(h)for h in range(4)],'created_peaks':[[a,h,T(a,h)]for a in keep for h in range(4)],'origin_cells':cells,'origin_encoding':{'white':0,'black_unknown_or_core':1,'black_initial':2,'black_produced':3},'initial_transition_indices':initial_edges,'packet_transition_indices':near_edges,'scope':'Entire marked prefix, arbitrary finite entry board/pose overapproximated; strict record includes earlier initial activations. No source, protected anchor, or unproved relation. OUT omits peak and activation cuts conservatively.'}
out.with_suffix('.json').write_text(json.dumps(J,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {OUT+1} {len(trans)} {len(re)}\n");f.write(' '.join(map(str,start))+'\n')
 for r in trans:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,sorted(re)))+'\n')
print(json.dumps({'variables':n,'poses':OUT+1,'transitions':len(trans),'threshold':S,'I':I,'initial_poses':len(initial_edges),'target':target,'phase':phase,'points':len(points)}))
