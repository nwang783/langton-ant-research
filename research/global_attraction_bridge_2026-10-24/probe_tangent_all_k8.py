import json
from pathlib import Path
from blank_collision_operator import cross,multiple,D
from check_fresh_record_trap_bridge import geometry,replay
P=Path(__file__).parent
rows=json.loads((P/'TANGENTIAL_WAKE_TURN_DISCOVERY.json').read_text());r=next(r for r in rows if r['K']==11)
F=r['post_interrupt_word'];V=r['capture']['word'];a0=(5,-4);d=(2,-2)
data=json.loads((P/'TERMINAL_TRAP_CERTIFICATE.json').read_text());W='RL'+data['fixed_continuation'][46:];H=data['period']
S={(0,1),(0,2),(0,3),(2,4),(3,2),(3,3)}
E,p,h,e=replay(S,(1,1),2,W);Q,pe,he=geometry(p,h,H);assert pe==(p[0]+2,p[1]-2)
M=set()
for q in Q:M^={q}
start_h=geometry(p,h,H[:45])[2]
CF,end,hh=geometry((0,0),start_h,F);TF,ee,eh=geometry(end,hh,V);v=(ee[0]-end[0],ee[1]-end[1])
assert v==(2,2)
# Test a backwards-tangent ray b-k*d, k>=lo against entire future F V^infinity.
def hits(b,lo):
 hits=[];u=(-2,2)
 for t,q in enumerate(CF):
  k=multiple((q[0]-b[0],q[1]-b[1]),u)
  if k is not None and k>=lo:hits.append(('prefix',t,k))
 for i,q in enumerate(TF):
  # b+k*u=q+j*v ; k*u-j*v=q-b
  z=(q[0]-b[0],q[1]-b[1]);det=cross(u,v)
  if cross(z,v)%det or cross(z,u)%det:continue
  k=cross(z,v)//det;j=cross(z,u)//det
  if k>=lo and j>=0:hits.append(('tail',i,k,j))
 return hits
for name,A,lo in [('E',E,8),('M',M,9)]:
 bad=[]
 for q in A:
  b=(q[0]-a0[0],q[1]-a0[1]);hit=hits(b,lo)
  if hit:bad.append([q,hit])
 print(name,len(A),'hits',len(bad),bad[:10])
print('head',start_h,'Flen',len(F),'end',end,hh,'tail',v,'F bbox',min(x for x,y in CF),max(x for x,y in CF),min(y for x,y in CF),max(y for x,y in CF))
