"""Exact bounded rejection controls for geometrically self-similar turn substitutions.
A surviving prefix is NOT an infinite trajectory certificate. Finite first-L
is a separate obligation even after full alternating-read legality.
"""
import itertools,collections,json,pathlib,sys,time,math
HERE=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))

def geometry(w):
 x=y=h=0
 for c in w:
  h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return h,x,y

def words(u,v,s,depth):
 stack=[(s,depth)]
 while stack:
  c,d=stack.pop()
  if d==0:yield c
  else:stack.extend((a,d-1)for a in (u if c=='R'else v)[::-1])

def roots(u,v):
 # Include each fixed initial letter, or the two phases of a first-letter 2-cycle.
 first={'R':u[0],'L':v[0]}
 return [(s,1)for s in 'RL'if first[s]==s]or[(s,2)for s in 'RL']

def check(u,v,s,period,cap):
 n=len(u);depth=period
 while n**depth<cap:depth+=period
 x=y=h=0;last={};freshL=0;marks=[];nextmark=n
 for t,c in enumerate(words(u,v,s,depth)):
  if t>=cap:break
  p=x,y
  if p in last and last[p][0]==c:
   return {'kind':'chronology_conflict','time':t,'earlier':last[p][1],'cell':p,'turn':c,'first_L':freshL}
  if p not in last and c=='L':freshL+=1
  last[p]=c,t;h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
  if t+1==nextmark:marks.append([t+1,freshL,len(last),x,y]);nextmark*=n
 return {'kind':'prefix_survivor','steps':cap,'first_L':freshL,'cells':len(last),'pose':[x,y,h],'marks':marks}

def mass_filter(u,v,a2):
 """Only valid for an R-prolongable root; square first for a 2-cycle."""
 # Primitive incidence matrix since every expanding image contains both letters.
 n=len(u);r=u.count('R');s=v.count('R');bias=r+s-n
 if bias<0:return 'negative_asymptotic_mass'
 if bias>0 and n>a2:return 'mass_exceeds_geometric_area'
 if bias==0:
  lam=r-s
  if lam<0 and abs(lam)>1:return 'alternating_negative_mass'
  if lam*lam<a2:return 'mass_below_midpoint_bound'
  if lam>a2:return 'mass_exceeds_geometric_area'
 return None

if __name__=='__main__':
 maximum=int(sys.argv[1])if len(sys.argv)>1 else 11
 cap=int(sys.argv[2])if len(sys.argv)>2 else 100000
 rows=[];tot=collections.Counter();start=time.time();lengths={}
 for n in range(3,maximum+1,2):
  groups=collections.defaultdict(list)
  for tup in itertools.product('RL',repeat=n):
   w=''.join(tup);groups[geometry(w)].append(w)
  pairs=0;nt=collections.Counter()
  for (h,x,y),us in groups.items():
   a2=x*x+y*y
   if h!=1 or a2<=1:continue
   for u in us:
    for v in groups.get((3,-x,-y),[]):
     if u[0]!='L' or v[0]!='R':continue
     pairs+=1;mf=mass_filter(u,v,a2)
     for s,k in [('R',2)]:
      r=check(u,v,s,k,cap)
      r.update(n=n,u=u,v=v,root=s,first_cycle=k,scale=[x,y],mass_filter=mf)
      rows.append(r);tot[r['kind']]+=1;nt[r['kind']]+=1
      if r['kind']=='prefix_survivor':print('SURVIVOR',json.dumps(r),flush=True)
  lengths[n]={'pairs':pairs,'outcomes':dict(nt)}
  print('LENGTH',n,lengths[n],'total_seconds',time.time()-start,flush=True)
 out={'maximum_length':maximum,'prefix_cap':cap,'lengths':lengths,'totals':dict(tot),'seconds':time.time()-start,'records':rows}
 p=HERE/f'two_cycle_turns_l{maximum}.json';p.write_text(json.dumps(out));print('DONE',str(p),dict(tot),time.time()-start,flush=True)
