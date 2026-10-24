"""Exact-height finite-box discovery for a global residual-height upper bound.
A hit is a countercontrol; a no-hit here is not a certificate (low truncation).
"""
import json,collections
G=json.load(open('chronology_dcuv/literal_residual_geometry.json'))['geometry'];keep=[0,1,4,5,6,7,8,9];A=[0,22,20,10];D=json.load(open('chronology_dcuv/literal_factor_dfa_k5.json'))
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for target,I in [(4,44),(7,48)]:
 phase=1; ht=lambda q:sum(rot(q,phase));peak=lambda a,h:2*ht(rot(G[a]['endpoint'][:2],h))+A[(h+G[a]['endpoint'][2]+phase)%4]
 S=peak(target,0);F=(S-I-1)//2;need=max(ht(q)for q in G[target]['inputs']);cut=-50
 ins={(a,h):max(ht(rot(q,h))for q in G[a]['inputs'])for a in keep for h in range(4)};outs={(a,h):max(ht(rot(q,h))for q in G[a]['outputs'])for a in keep for h in range(4)}
 starts=[(q,h,F,D['initial_class'])for h in range(4)for q in range(cut,(S-1-A[(h+phase)%4])//2+1)if(q+h)%2==0];pred={z:None for z in starts};queue=collections.deque(starts);hit=None
 while queue:
  q,h,Q,c=queue.popleft()
  if q==0 and h==0 and Q>=need and D['transitions'][c][keep.index(target)]>=0:hit=(q,h,Q,c);break
  for a in keep:
   cc=D['transitions'][c][keep.index(a)]
   if cc<0:continue
   if 2*q+max(A[(h+phase)%4],peak(a,h))>=S or q+ins[a,h]>Q:continue
   qq=q+ht(rot(G[a]['endpoint'][:2],h));hh=(h+G[a]['endpoint'][2])%4;QQ=max(Q,q+outs[a,h]);z=(qq,hh,QQ,cc)
   if qq<cut:continue
   if z not in pred:pred[z]=((q,h,Q,c),a);queue.append(z)
 path=[];z=hit
 while z is not None and pred[z]is not None:
  old,a=pred[z];path.append([old,a,z]);z=old
 path.reverse();print(json.dumps({'target':target,'S':S,'I':I,'F':F,'goal_max_input_height':need,'states':len(pred),'hit':hit,'path':path}))
