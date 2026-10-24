import json
from pathlib import Path
from blank_collision_operator import D,multiple,cross
from check_fresh_record_trap_bridge import geometry
P=Path(__file__).parent
src=json.loads((P/'REVERSE_INTERFACE_DISCOVERY.json').read_text());pert=json.loads((P/'REVERSE_RETURN_PERTURB_DISCOVERY.json').read_text())[0]
B0=set(map(tuple,src['cuts']['64200']['black']))
B={(-49,-30)};p=(0,0);h=0
for t in range(64408):
 a=p in B;B^={p};h=(h+(-1 if a else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
assert p==(20,-22) and h==0
L=B^B0;print('layer',len(L),'massB1',len(B),'bbox',min(x for x,y in L),max(x for x,y in L),min(y for x,y in L),max(y for x,y in L))
F=src['post_hit_word'][:12]+pert['post_extra_word'];V=pert['capture']['word'];Q,end,hh=geometry((20,-22),0,F);T,te,th=geometry(end,hh,V);v=(te[0]-end[0],te[1]-end[1]);d=(-2,-2);bad=[]
for b in L:
 for i,q in enumerate(Q):
  k=multiple((q[0]-b[0],q[1]-b[1]),d)
  if k is not None and k>=0:bad.append([b,'F',i,k])
 for i,q in enumerate(T):
  z=(q[0]-b[0],q[1]-b[1]);det=cross(d,v);kn=cross(z,v);jn=cross(z,d)
  if kn%det==0 and jn%det==0 and kn//det>=0 and jn//det>=0:bad.append([b,'tail',i,kn//det,jn//det])
print('futurelen',len(F),'tail',v,'raybad',len(bad),bad[:10])
(P/'REVERSE_LAYER_GUARD_DISCOVERY.json').write_text(json.dumps(dict(layer=sorted(L),B1=sorted(B),pose1=[p,h],layer_size=len(L),prefix_word=F,tail_word=V,ray_hits=bad),indent=2)+'\n')
