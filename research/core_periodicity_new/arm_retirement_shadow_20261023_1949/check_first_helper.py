"""Finite first-touch gate inventory and protected-tree exact clocks. No path search."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter,deque
import math,json,hashlib
ROOT=Path('/workspace/shared/langton/core_periodicity_new');HERE=Path(__file__).resolve().parent
GP=ROOT/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];IDS=(0,1,4,5,6,7,8,9);K=set(map(tuple,J['core']));MARK=G[0]['marker'];W=(-1,3)
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def place(q,p,h):return add(p,rot(q,h))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def on(p,a,b):return cross(sub(p,a),sub(b,a))==0 and dot(sub(p,a),sub(p,b))<=0
def contact(a,b,c,d):
 u=sub(b,a);v=sub(d,c);r=sub(c,a);z=cross(u,v)
 if z:
  s=F(cross(r,v),z);t=F(cross(r,u),z)
  return [[str(F(a[k])+s*u[k])for k in range(2)]]if 0<=s<=1 and 0<=t<=1 else[]
 return[list(p)for p in sorted({a,b,c,d})if on(p,a,b)and on(p,c,d)]
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def edge(q):
 x,y=q;d=(1,1)if(x+y)%2==0 else(1,-1)
 return((2*x-d[0],2*y-d[1]),(2*x+d[0],2*y+d[1]))
def reconstruct(word):
 p=(0,0);h=0;par=set();req={}
 for ch in word:
  b=(ch=='L')^(p in par);assert p not in req or req[p]==b
  req[p]=b;par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=place((0,1),p,h)
 return req,par,p,h
for a in IDS:
 req,par,p,h=reconstruct(G[a]['word']+MARK);assert req=={(x,y):bool(b)for x,y,b,*_ in G[a]['requirements']}
 req,par,p,h=reconstruct(G[a]['word']);assert[*p,h]==G[a]['endpoint'];board=(K|set(map(tuple,G[a]['inputs'])))^par;assert board-{place(q,p,h)for q in K}==set(map(tuple,G[a]['outputs']))
def chords(a,p=(0,0),h=0):
 out=[];base=0 if a in(0,1)else 4 if a in(4,5,6)else 7
 start=center(p,h);end=add(start,rot((2,2)if base==0 else(2,6)if base==4 else(0,8),h));out.append((start,end))
 ep=G[base]['endpoint'];p=place(ep[:2],p,h);h=(h+ep[2])%4
 for _ in range(G[a]['name'].count('C')):
  start=center(p,h);p=place((0,1),p,h);h=(h+3)%4;out.append((start,center(p,h)))
 return out

def unique_tree_bridge(cells,E):
 adj={}
 for q in cells:
  a,b=edge(q);adj.setdefault(a,[]).append((b,q));adj.setdefault(b,[]).append((a,q))
 # All six gates sit on one attached tree. The source west-top route is the
 # unique shortest path to W, no traversal of the source cycle is needed.
 todo=deque([(E,[E],[])]);seen={E};paths=[]
 while todo:
  v,p,qs=todo.popleft()
  if v==W:return p,qs
  for z,q in adj.get(v,[]):
   if z not in seen:seen.add(z);todo.append((z,p+[z],qs+[q]))
 raise AssertionError('no bridge')
allrows=[];cases=[];expected={7:{(0,(2,3),3),(1,(2,3),3)},8:{(0,(1,7),2),(4,(2,8),2)},9:{(0,(-3,6),1),(4,(-4,7),1)}}
for s in(7,8,9):
 R=set(map(tuple,G[s]['outputs']));src=chords(s);got=set()
 for a in IDS:
  for h in range(4):
   for q in sorted(R):
    p=sub(q,rot(G[a]['inputs'][0],h));ins={place(z,p,h)for z in G[a]['inputs']};ctx={place(z[:2],p,h)for z in G[a]['requirements']};cc=chords(a,p,h)
    row=dict(source=s,consumer=a,head=[*p,h],inputs=sorted(ins))
    if(sum(p)+h)%2:row['reason']='wrong_sector'
    elif not ins<=R:row['reason']='needs_outside_identity'
    elif ctx&(R-ins):row.update(reason='other_current_source_output_in_context',hits=sorted(ctx&(R-ins)))
    elif any(contact(*x,*y)for x in cc for y in src):row['reason']='past_source_chord_contact'
    else:
     row['reason']='first_helper_gate';got.add((a,p,h));E=cc[0][1];bridge,qs=unique_tree_bridge(R,E)
     assert bridge[-1]==W and len(bridge)==len(set(bridge));assert len(qs)==len(set(qs))
     for i,(u,v)in enumerate(zip(bridge,bridge[1:])):
      assert set(edge(qs[i]))=={u,v}
      for j,(x,y)in enumerate(zip(bridge,bridge[1:])):
       if j<=i+1:continue
       assert not contact(u,v,x,y)
      assert contact(*cc[0],u,v)==([[str(E[0]),str(E[1])]]if i==0 else[])
      # Source portion beginning W, including all source C tails, avoids bridge.
      for z,(x,y)in enumerate(src):
       if z==0:x=W
       hit=contact(x,y,u,v)
       assert hit==([[str(W[0]),str(W[1])]]if i==len(bridge)-2 and z==0 else[])
     # Each bridge identity is installed by source end and held current until
     # this first touch. Before full source end, exact source interface above
     # replaces the current-residual barrier.
     vectors=[sub(cc[0][1],cc[0][0])]+[sub(v,u)for u,v in zip(bridge,bridge[1:])]+[(0,1)]
     turns=[math.atan2(cross(u,v),dot(u,v))for u,v in zip(vectors,vectors[1:])]
     c=G[s]['name'].count('C');alpha=math.pi/4 if a in(0,1)else math.atan(3)
     closing=sum(turns);target=math.pi/2-alpha-(c+1)*math.pi/2
     assert abs(closing-target)<1e-12
     case=dict(source=s,consumer=a,head=[*p,h],inputs=sorted(ins),base_chord=cc[0],bridge=bridge,bridge_identities=qs,closing_turns_radians=turns,closing_turn_identity=f'pi/2-alpha_base-{c+1}*pi/2',atomic_turn_identity='n*pi/2+alpha_base-pi/2',total_closed_turn=f'(n-{c+1})*pi/2',forced_nonnegative_C_age=c+5)
     cases.append(case)
    allrows.append(row)
 assert got==expected[s],(s,got)
assert len(cases)==6
D=[GP,Path(__file__).resolve()]+[ROOT/x/'manifest.json'for x in('U_entry_simplicity_frozen_20261023_1616','current_residual_barrier_frozen_20261023_1822','U_renewal_exact_clock_frozen_20261023_1902')]
out=dict(status='AUTHOR_FIRST_HELPER_PORT_CLOCK_THEOREM_PENDING_INDEPENDENT_AUDIT',scope='Reset component at a genuine U-family entry, containing exactly source fresh outputs at source full exit. At first later touch of any source output, either the packet imports an outside component or it is one of exactly six all-source gates. The latter have source-entry C age5+c. No bound on subsequent helpers, global U total, or component merger claimed.',counts=dict(Counter(r['reason']for r in allrows)),cases=cases,rows=allrows,dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(HERE/'first_helper.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['counts'],indent=2));print('cases',[(x['source'],x['consumer'],x['head'],x['forced_nonnegative_C_age'])for x in cases])
