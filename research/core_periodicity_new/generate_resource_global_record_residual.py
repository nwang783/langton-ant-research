"""Whitened entire-prefix record model storing only residual BLACK membership.
CLI PROFILE POTENTIAL TARGET PHASE PREFIX 'context|file:JSON'.
Core is implicit in head pose. High initial residual cells are white; low cells arbitrary.
All goal inputs are high, hence any later black residual there is necessarily produced.
"""
from pathlib import Path
import sys,json,hashlib
from resource_profile import load_profile
profile,potential=map(Path,sys.argv[1:3]);target,phase=map(int,sys.argv[3:5]);out=Path(sys.argv[5]);mode=sys.argv[6];P,D,M=load_profile(profile);W=json.loads(potential.read_text());assert W['profile_sha256']==M['resource_profile_sha256'];G=D['geometry']['geometry'];K=set(map(tuple,D['geometry']['core']));keep=P['keep'];v=W['values'];direction=v['ax'],v['ay']
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def add(q,z):return q[0]+z[0],q[1]+z[1]
def L(q):return sum(a*b for a,b in zip(direction,q))
def A(h):return L(rot((-1,1),h))+v[f'c{h%4}']
def T(a,h):
 h%=4;g=G[a];e=g['endpoint'];return max([2*L(rot(e[:2],h))+A(h+e[2])]+[2*L(rot(q,h))+v[f'w_{a}_{i}_{h}']for i,q in enumerate(g['outputs'])])
S=T(target,phase);assert S>A(phase);I=max(T(a,h)-2*L(rot(q,h))for a in keep for h in range(4)for q in G[a]['inputs']);points=set(map(tuple,G[target]['inputs']))
if mode=='context':points|={tuple(r[:2])for r in G[target]['requirements']}
elif mode.startswith('file:'):points|=set(map(tuple,json.loads(Path(mode.split(':',1)[1]).read_text())))
else:assert mode=='inputs'
points=sorted(points);ix={q:i for i,q in enumerate(points)};n=len(points);assert n<=50
high={q for q in points if I+2*L(rot(q,phase))>=S};assert set(map(tuple,G[target]['inputs']))<=high
for a in keep:
 g=G[a];e=g['endpoint'];newK={add(e[:2],rot(q,e[2]))for q in K};assert not(set(map(tuple,g['outputs']))&newK);assert not(set(map(tuple,g['inputs']))&K)
heads=set()
for a in keep:
 for h in range(4):
  for rr in G[a]['requirements']:
   z=rot(rr[:2],h)
   for q in points:
    x,y=q[0]-z[0],q[1]-z[1]
    if(x+y+h)%2==0:heads.add((x,y,h))
heads=sorted(heads);si={p:i for i,p in enumerate(heads)};init=len(heads);OUT=init+1;re=set();trans=[];initial=[];packet=[];start=[init,sum(1<<ix[q]for q in high),0]
for sid,(x,y,h)in enumerate(heads):
 oldK={add((x,y),rot(q,h))for q in K};km=sum(1<<ix[q]for q in oldK if q in ix)
 if 2*L(rot((x,y),phase))+A(h+phase)<S:initial.append(len(trans));trans.append([init,sid,0,0,0,km,0,0,-1])
 for a in keep:
  g=G[a];e=g['endpoint'];ep=add((x,y),rot(e[:2],h));eh=(h+e[2])%4;dest=(*ep,eh);to=si.get(dest,OUT);goal=(a==target and(x,y,h)==(0,0,0));hh=(h-e[2])%4;zz=rot(e[:2],hh)
  if(x-zz[0],y-zz[1],hh)not in si:re.add(sid)
  if not goal and 2*L(rot((x,y),phase))+max(A(h+phase),T(a,h+phase))>=S:continue
  guard=km;value=0;valid=True
  for rr in g['requirements']:
   q=add((x,y),rot(rr[:2],h));black=bool(rr[2])
   if q in oldK:
    assert black,'literal core conflict'
   elif q in ix:
    bit=1<<ix[q];guard|=bit
    if black:value|=bit
  inputs={add((x,y),rot(q,h))for q in g['inputs']};outputs={add((x,y),rot(q,h))for q in g['outputs']};newK={add(ep,rot(q,eh))for q in K};assert not(outputs&newK)
  clear=sum(1<<ix[q]for q in (inputs|outputs|newK)if q in ix);reset=sum(1<<ix[q]for q in outputs if q in ix)
  packet.append(len(trans));trans.append([sid,to,guard,value,0,clear,reset,int(goal),a])
initial.append(len(trans));trans.append([init,OUT,0,0,0,0,0,0,-1]);J={**M,'format':'guarded_reset_global_record_residual_v1','n':n,'points':points,'poses':heads,'initial_control_pose':init,'out':OUT,'start':start,'transitions':trans,'reentry':sorted(re),'keep':keep,'target':target,'target_global_phase':phase,'target_pose':[0,0,0],'potential_file':str(potential.resolve()),'potential_sha256':hashlib.sha256(potential.read_bytes()).hexdigest(),'record_threshold':S,'initial_token_weight':I,'core_offsets':[A(h)for h in range(4)],'created_peaks':[[a,h,T(a,h)]for a in keep for h in range(4)],'high_initial_white_cells':sorted(high),'initial_transition_indices':initial,'packet_transition_indices':packet,'scope':'Entire prefix, implicit five-cell core, exact ordered residual remove/install; high initial identities existentially whitened; all goal inputs high. No unproved family, source anchor, or forgotten activation. OUT drops all cuts but preserves retained residual bits.'};out.with_suffix('.json').write_text(json.dumps(J,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{n} {OUT+1} {len(trans)} {len(re)}\n');f.write(' '.join(map(str,start))+'\n')
 for r in trans:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,sorted(re)))+'\n')
print(json.dumps({'variables':n,'positions':OUT+1,'transitions':len(trans),'initial_free_bits':n-start[1].bit_count(),'target':target,'phase':phase,'threshold':S}))
