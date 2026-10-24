"""Independent complex ant, orbit-chronology infinite tails, and paired ports."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,itertools,random
R=Path(__file__).resolve().parents[1];P=R/'global_architecture_2026-10-23';W=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];G={-1j,1+1j,1+3j,2+2j}
def xy(z):return int(z.real),int(z.imag)
def dot(a,b):return int((a*b.conjugate()).real)
def step(B,p,h):
 h*=1j if p in B else -1j;B.symmetric_difference_update({p});return p+h,h
def rev(B,p,h):
 q=p-h;B.symmetric_difference_update({q});old=h*(-1j if q in B else 1j);return q,old
def involution(B,p,h):return set(B),p-h,-h
def trace(B,p,h,n):
 B=set(B);reads=[];w=''
 for _ in range(n):reads.append(p);w+='L'if p in B else'R';p,h=step(B,p,h)
 return B,p,h,w,reads
def exact_tail(B,p,h,w):
 slots=[];q=p;hh=h
 for i,c in enumerate(w):slots.append((q,i,c));hh*=1j if c=='L'else -1j;q+=hh
 d=q-p;assert hh==h and d and d.real
 classes=defaultdict(list);width=abs(int(d.real));needed=set();visited_seed=set();histories=0
 for q,i,c in slots:
  k=(int(q.real)-int(q.real)%width)//int(d.real);rep=q-k*d;classes[rep].append((k,i,c))
 for rep,es in classes.items():
  lo=min(k for k,i,c in es);hi=max(k for k,i,c in es)
  # Exact chronological subsets for every finite change-point cell, and stable suffix.
  for n in range(lo,hi+1):
   seq=sorted(((i-len(w)*k,c)for k,i,c in es if k<=n));assert seq
   assert all(a[1]!=b[1]for a,b in zip(seq,seq[1:])),(rep,n,seq)
   if n==hi:assert seq[0][1]=='R',('nonwhite stabilized history',rep)
   elif seq[0][1]=='L':needed.add(rep+n*d)
   histories+=1
  for b in B:
   diff=b-rep
   if diff.real%int(d.real)==0:
    n=int(diff.real)//int(d.real)
    if diff==n*d and n>=lo:visited_seed.add(b)
 assert visited_seed==needed,(needed-B,visited_seed-needed)
 return {'classes':len(classes),'finite_history_checks':histories,'required_black':len(needed),'ignored_black':len(B-visited_seed)},d
B,p,h,trans,reads=trace(G,0j,1,182);assert(p,h,len(B))==(5+1j,1,36)
T,pp,hh,w,tailreads=trace(B,p,h,104);assert w==W
oracle,drift=exact_tail(B,p,h,W);assert drift==2+2j
assert min(z.real for z in reads+tailreads)==0 and min(z.imag for z in reads+tailreads)==-2
assert all(z.real>=0 and z.imag>=-2 for z in G)
def port(e,g,k):
 assert k in(1j*g,-1j*g);w='LRLR'if k==1j*g else'RLRLR';p=e;h=g;black=set();seen=[]
 for c in w:
  assert p not in seen;seen.append(p)
  if c=='L':black.add(p)
  h*=1j if c=='L'else -1j;p+=h
 gate={p+h*z for z in G};assert not gate.intersection(seen)and len(black|gate)==6
 return black|gate,w

def inside(z,e,g,k):return dot(z-e,g)>=0 and dot(z-e,k)>=0
def choose(e,g,f,h):
 if g==-h:return 1j*g,1j*h
 if g==h:
  k=1j*g
  return(-k,k)if dot(f-e,k)>0 else(k,-k)
 return-h,-g

def separate(e,g,k,f,h,l):
 for axis in(1,1j):
  va=dot(g+k,axis);vb=dot(h+l,axis);a=dot(e,axis);b=dot(f,axis)
  if va>0 and vb<0 and b<a:return True
  if va<0 and vb>0 and a<b:return True
 return False
ports=0
for g in(1,1j,-1,-1j):
 for k in(1j*g,-1j*g):
  e=13-7j;seed,w=port(e,g,k);C,p,h,ww,rr=trace(seed,e,g,len(w)+182);assert ww.startswith(w);_,d=exact_tail(C,p,h,W)
  assert d==2*(g+k);_,_,_,wt,tr=trace(C,p,h,104);assert wt==W
  assert all(inside(z,e,g,k)for z in seed|set(rr)|set(tr));ports+=1
pairs=tight=0
for radius in range(7):
 exits=[]
 for n in range(-radius,radius+1):exits += [(radius+1+n*1j,1),(-radius-1+n*1j,-1),(n+(radius+1)*1j,1j),(n-(radius+1)*1j,-1j)]
 for (e,g),(f,h)in itertools.combinations(exits,2):
  assert e!=f;k,l=choose(e,g,f,h);assert separate(e,g,k,f,h,l);pairs+=1
  if radius<=1:
   E,w=port(e,g,k);F,v=port(f,h,l);assert len(E|F)==12
   for q,hh,kk,ww in((e,g,k,w),(f,h,l,v)):
    C,p,h2,actual,rr=trace(E|F,q,hh,len(ww)+182);assert actual.startswith(ww)and all(inside(z,q,hh,kk)for z in rr);exact_tail(C,p,h2,W)
   tight+=1
rng=random.Random(101823);full=0;maxexit=0;inverse=0
for i in range(100):
 cells=[complex(x,y)for x in range(-3,4)for y in range(-3,4)];B=set(rng.sample(cells,rng.randrange(24)));p=0j;h=(1,1j,-1,-1j)[i%4];radius=4+i%3
 # Independent algebraic and literal reverse-step control.
 U=set(B);fp,fh=step(U,p,h);V=set(U);rp,rh=rev(V,fp,fh);assert(V,rp,rh)==(B,p,h)
 V,ip,ih=involution(B,p,h);ip,ih=step(V,ip,ih);V,ip,ih=involution(V,ip,ih);Z=set(B);zp,zh=rev(Z,p,h);assert(V,ip,ih)==(Z,zp,zh);inverse+=1
 origins=[(p,h),(p-h,-h)];ex=[]
 for pp,hh in origins:
  BB=set(B);t=0
  while max(abs(pp.real),abs(pp.imag))<=radius:
   pp,hh=step(BB,pp,hh);t+=1;assert t<1000000,'Control cap only, not theorem'
  ex.append((pp,hh,t));maxexit=max(maxexit,t)
 (e,g,t1),(f,hh,t2)=ex;assert e!=f;k,l=choose(e,g,f,hh);assert separate(e,g,k,f,hh,l)
 E,w=port(e,g,k);F,v=port(f,hh,l);hardware=E|F;assert len(hardware)==12 and not hardware&B and all(max(abs(z.real),abs(z.imag))>radius for z in hardware)
 for (pp,hh),(ee,gg,t),ww in zip(origins,ex,(w,v)):
  C,q,d,words,rr=trace(B,pp,hh,t);C2,q2,d2,words2,rr2=trace(B|hardware,pp,hh,t);assert(q,d,words,rr)==(q2,d2,words2,rr2)and C^C2==hardware
  BB,q,d,words,rr=trace(C2,q2,d2,len(ww)+182);assert words.startswith(ww);exact_tail(BB,q,d,W)
 full+=1
out={'status':'PASS independent exact gate, both quadrant ports, reverse involution, disjoint routing and complete infinite-tail controls','proof_sha256':hashlib.sha256((P/'two_sided_quadrant_completion.md').read_bytes()).hexdigest(),'gate_orbit_chronology':oracle,'quadrant_orientations':ports,'boundary_pairs':pairs,'literal_tight_pairs':tight,'full_finite_seed_controls':full,'direct_inverse_controls':inverse,'max_control_first_exit':maxexit,'scope':'Analytic all-square twelve-addition two-sided completion. Controls do not replace the all-time geometry proof or assert capture of an unmodified input.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
