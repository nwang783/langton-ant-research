"""Exact literal periodic bulk identities; finite controlled composition probes."""
import json,pathlib,collections
P=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0));A='LRLLRRRRLLRL';B='RRRLLLLRLLLLRLLLLRRRRLRRRRLR'
def reads(w,entry):
 x,y,h=entry;out=[]
 for c in w:
  out.append((x,y,c));h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return out,(x,y,h)
def profile(w,entry,source,target,repeat):
 rr,end=reads(w,entry);assert end==(entry[0]+2,entry[1],entry[2]);g=collections.defaultdict(list)
 for t,(x,y,c)in enumerate(rr):g[x%2,y].append((-(x//2),t,c))
 out=[]
 for(x,y),v in sorted(g.items()):
  s=''.join(c for _,_,c in sorted(v));expected=('L'if source[x]>>y&1 else'R');assert s[0]==expected and all(a!=b for a,b in zip(s,s[1:]));assert(s[-1]=='R')==bool(target[x]>>y&1)
  assert len(s)==(repeat if y in(1,2)else 1);out.append([x,y,s])
 assert len(g)==8;return out
def concat(n,offset):
 last={};seed=set();count=0
 for w,entry in [(A*n,(0,0,1)),(B*n,(offset,2,1))]:
  rr,end=reads(w,entry)
  for x,y,c in rr:
   q=x,y
   if q in last and last[q]==c:return dict(valid=False,conflict_time=count,cell=q,turn=c)
   if q not in last and c=='L':seed.add(q)
   last[q]=c;count+=1
 return dict(valid=True,mass=len(seed),end_mass=sum(c=='R'for c in last.values()),changed=len(set(seed)^set(q for q,c in last.items()if c=='R')))
if __name__=='__main__':
 out=dict(up=profile(A,(0,0,1),(1,7),(8,14),2),down=profile(B,(0,2,1),(8,14),(1,7),6),finite_controls={str(dx):[dict(n=n,**concat(n,dx))for n in(1,2,3,5,10,20,50)]for dx in range(-6,7,2)})
 (P/'12_28_pair_certificate.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
