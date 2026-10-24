from pathlib import Path
import json
from check_return_permanent_output_debt import DXY,rot,future
P=Path(__file__).parent;G={(0,-1),(1,1),(1,3),(2,2)}
def ports(n):return [((0,0),1),((7*n-1,7*n),0),((5*n,9*n-4),3),((n+5,5*n),2)]
def seed(n):return {(p[0]+rot(q,h-1)[0],p[1]+rot(q,h-1)[1]) for p,h in ports(n) for q in G}
def step(B,p,h):
 b=p in B
 if b:B.remove(p);h=(h-1)%4
 else:B.add(p);h=(h+1)%4
 return (p[0]+DXY[h][0],p[1]+DXY[h][1]),h,'L' if b else 'R'
B=set(G);p=(0,0);h=1;W='';states=[]
for t in range(286):states.append((p,h));p,h,ch=step(B,p,h);W+=ch
A,U=W[:182],W[182:];gp,gh=states[182]
src=json.loads((P/'TRANSVERSE_FAR_MODULE_SOURCE.json').read_text());F,Z=src['post_contact_word'],src['tail_word']
phase=next(i for i in range(104) if Z[i:]+Z[:i]==U)
print('G182',gp,gh,'phase',phase)
base=seed(20);c1=14393;align=c1+8986+phase
B=set(base);p=(0,0);h=1
for t in range(align):p,h,ch=step(B,p,h)
assert h==(gh+1)%4
for J,n2 in [(100,40),(200,80),(500,160)]:
 T=align+104*J;pT=(p[0]+2*J,p[1]-2*J);rgp=rot(gp,1);v=(pT[0]-rgp[0],pT[1]-rgp[1])
 extra={(v[0]+rot(q,1)[0],v[1]+rot(q,1)[1]) for q in seed(n2)-G};assert len(extra)==12 and not(extra&base)
 BB=set(base)|extra;pp=(0,0);hh=1;first={};turns=[];mismatch=None
 for t in range(T):
  if pp in extra and pp not in first:first[pp]=t
  pp,hh,ch=step(BB,pp,hh);turns.append(ch)
 assert not first and (pp,hh)==(pT,h)
 r=[7*n2//2-4,2*n2//2-5,4*n2//2-6,2*n2//2-6];part=[61,71,61,56]
 second=U*r[0]+U[:61]+''.join(A+U*r[i]+U[:part[i]] for i in range(1,4))
 for j,ch0 in enumerate(second+F+Z*2):
  t=T+j
  if pp in extra and pp not in first:first[pp]=t
  pp,hh,ch=step(BB,pp,hh);turns.append(ch)
  if ch!=ch0:mismatch=(j,ch0,ch,pp,hh);break
 print({'n2':n2,'J':J,'virtual_origin':v,'T':T,'second_contact':T+len(second),'first_extra':min(first.values()) if first else None,'mismatch':mismatch,'read_extra_count':len(first)},flush=True)
 if mismatch is None:
  tail,dr,dd,ct=future({q:i for i,q in enumerate(BB)},pp,hh)
  print('tail',dr,ct,len(BB), 'match',tail==Z)
