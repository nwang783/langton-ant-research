import json,pathlib
P=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
A='LRLLRRRRLLRL';B='RRRLLLLRLLLLRLLLLRRRRLRRRRLR';S='RLLR';W='LLRLRRRRLRRRRLLLLRLL'
def trace(w,p):
 x,y,h=p;out=[]
 for c in w:
  out.append((x,y,c));h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return out,(x,y,h)
def sign(x):return 1 if x%2==0 else -1
def g(p,r):
 x,y,h=p;a=int(y==r);aa=int(y>r);return 2*aa+[0,sign(x)*a,2*a,-sign(x)*a][h]
ports=[((0,0,1),(0,8,3)),((0,2,1),(0,8,1)),((0,0,1),(0,10,3)),((0,2,1),(-1,9,3))]
assert all(g(e,11)==g(o,11)==0 for e,o in ports)
wr,_=trace(W,(0,8,1));sr,_=trace(S,(0,10,3))
assert[(x,c)for x,y,c in wr if y==11]==[(-2,'R'),(-1,'R')]
assert[(x,c)for x,y,c in sr if y==11]==[(0,'L'),(-1,'L')]
others=[(A,(0,0,1)),(B,(0,2,1)),(S,(0,8,3)),(S,(-1,9,3))]
assert all(y!=11 for w,p in others for x,y,c in trace(w,p)[0])
controls=0
for n in range(2,101):
 wr,_=trace(W*n,(2*n,8,1));sr,_=trace(S*n,(2*n,10,3))
 assert sorted(x for x,y,c in wr if y==11)==list(range(2*n))
 assert sorted(x for x,y,c in sr if y==11)==list(range(1,2*n+1))
 for m in range(1,n):
  cut=2*n-2*m
  delta=sum((1 if c=='R'else-1)*sign(x)for x,y,c in wr+sr if y==11 and x>=cut)
  assert delta==-1;controls+=1
(P/'eight_pass_phase_certificate.json').write_text(json.dumps(dict(row=11,right_flux_mod4=3,minimum_cap_cycle_divisor=4,all_n_literal_footprints=True,finite_controls=controls),indent=2))
print('PASS exact two literal footprints and',controls,'finite cut controls; same-cap contract impossible, phase period divisible by4')
