from pathlib import Path
from collections import deque,Counter
from itertools import product
import json,hashlib,random
P=Path(__file__).resolve().parents[1];dirs=[1j,1,-1j,-1]
# Independently derive undirected port multiplicities from every ordered incoming history.
rows=[];barriers=[]
for parity in [0,1]:
 allowed=[1,3]if parity==0 else[0,2]
 for count in range(4):
  for heads in product(allowed,repeat=count):
   if count==3 and heads[0]==heads[2]:continue
   ports=[0]*4
   for j,h in enumerate(heads):
    ports[(h+2)%4]+=1;ports[(h+(1 if j%2==0 else-1))%4]+=1
   # Rotate odd vertices a quarter turn into the even-vertex convention.
   pp=ports if parity==0 else[ports[(j+1)%4]for j in range(4)]
   N,E,S,W=pp;un=[0,N,N-E,N-E+S];assert un[3]==W
   H=[un[0]+1,un[1],un[2]+1,un[3]];M=max(H)
   assert H.count(M)>=2
   for omitted in range(4):assert max(H[:omitted]+H[omitted+1:])==M
   if count==0:assert H[0]==H[2] and H[1]==H[3] and abs(H[0]-H[1])==1
   if count in [1,3]:assert H.count(M)==3 and min(H)==M-1
   if count==2:assert H.count(M)==2 and min(H)==M-1
   # Check physical horizontal barrier without rotation, using odd-vertex face colors.
   if parity==0:physical=H
   else:physical=[H[3],H[0],H[1],H[2]]
   if (physical[0]==physical[1]>max(physical[2:]))or(physical[2]==physical[3]>max(physical[:2])):
    assert count==2 and ports[0]==ports[2]==1 and sorted([ports[1],ports[3]])==[0,2]
    barriers.append({'parity':parity,'heads':heads,'ports':ports})
   rows.append({'parity':parity,'heads':heads,'ports':ports,'shifted_heights_rotated':H})
assert len(rows)==22
# Both chronological passages of either horizontal domino preserve geometric side.
passages=[]
for heading in [1,3]:
 source=[(heading-1)%4,(heading+1)%4];target=[heading,heading]
 for j in [0,1]:
  turn=1 if j==0 else-1
  assert(source[j]+turn)%4==heading
  exit=(target[j]+turn)%4
  assert dirs[exit]==-dirs[source[j]]
  passages.append((heading,j,source[j],exit))
# Independently integrate periodic physical flow on a large dual square.
# This checks the full-drift winding normalization, including nonprimitive drifts.
rng=random.Random(2718);words=['RLRL','RLRLRLRL','RRLLRRLL',json.loads((P/'recovered_bundle/ant_global/root/standard.json').read_text())['word']]
while len(words)<16:
 w=''.join(rng.choice('RL')for _ in range(16))
 if sum(1 if c=='R'else-1 for c in w)%4==0:words.append(w)
flux=[]
for w in words:
 p=0j;h=1;edges=[]
 for c in w:
  h*=(-1j if c=='R'else 1j);q=p+h;edges.append((p,q));p=q
 d=p
 if d==0:continue
 assert h==1 and(int(d.real+d.imag))%2==0
 def f(u,v):
  result=0
  for a,b in edges:
   if b-a not in (v-u,u-v):continue
   for aa,bb in [(a,b),(b,a)]:
    if bb-aa!=v-u:continue
    z=(u-aa)/d
    if z.imag==0 and z.real==int(z.real):result+=1
  return result
 R=32;heights={(0,0):0};todo=deque([(0,0)])
 while todo:
  x,y=todo.popleft()
  for ex,ey in [(1,0),(-1,0),(0,1),(0,-1)]:
   X,Y=x+ex,y+ey
   if max(abs(X),abs(Y))>R:continue
   if ex:u=complex(max(x,X),y);v=u+1j
   else:u=complex(x,max(y,Y));v=u+1
   value=heights[x,y]+(1 if(X+Y)%2==0 else-1)*f(u,v)
   if(X,Y)in heights:assert heights[X,Y]==value
   else:heights[X,Y]=value;todo.append((X,Y))
 normals=[int(d.real*z.imag-d.imag*z.real)for e in edges for z in e];lo=min(normals)-5;hi=max(normals)+5
 lows={v for(x,y),v in heights.items()if d.real*(y+.5)-d.imag*(x+.5)<lo}
 highs={v for(x,y),v in heights.items()if d.real*(y+.5)-d.imag*(x+.5)>hi}
 assert len(lows)==len(highs)==1 and abs(next(iter(lows))-next(iter(highs)))==1,(w,d,lows,highs)
 flux.append({'period':len(w),'drift':[int(d.real),int(d.imag)],'exterior_jump':next(iter(highs))-next(iter(lows))})
note=P/'periodic_classification_new/cap_three_shifted_stream_height.md'
out={'status':'PASS independent local table, horizontal chronological barrier and full-drift flux controls','local_histories':rows,'horizontal_barriers':barriers,'domino_passages':passages,'periodic_flux_controls':flux,'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'scope':'Finite controls supplement the analytic all-width/all-period proof; random words test only flow topology, not ant legality.'}
(P/'audits/cap_three_stream_height_independent.json').write_text(json.dumps(out,indent=2));print({'status':out['status'],'local_histories':len(rows),'barriers':len(barriers),'flux_controls':len(flux)})
