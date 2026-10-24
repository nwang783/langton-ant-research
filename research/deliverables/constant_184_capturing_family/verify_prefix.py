"""Verify EVERY N>=1 by an exact affine-interval arrangement, not sampling."""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction
import json,hashlib
SELF=Path(__file__).resolve();DATA=json.loads(SELF.with_name('family_data.json').read_text());M=DATA['family'];H=DATA['standard_word'];W=M['stages'][-1]['word'];D=(1j,1,-1j,-1)
def xy(z):return(int(z.real),int(z.imag))
def lit(w,p=0j,h=3):
 out=[]
 for i,c in enumerate(w):out.append((i,p,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return out,p,h
G=defaultdict(list);seeds=[];blocks=[];block=0;pA=14+14j;pB=33+70j;h=3
def scalar(A,B):
 assert A.real==A.imag and int(A.real)%14==0
 a=int(B.real)%2;t=int(B.real-B.imag);alpha=int(A.real)//2;beta=(int(B.real)-a)//2
 return t,a,alpha,beta

def addseed(A,B,tag):
 t,a,alpha,beta=scalar(A,B);r=beta%7;v=(alpha//7,beta//7)
 G[t,a,r].append({'lo':v,'hi':v,'seed':tag});seeds.append((xy(A),xy(B),tag))

def addblock(word,count,kind):
 global pA,pB,h,block
 ca,cb=count;assert ca>=0 and ca+cb>=1
 tr,d,eh=lit(word,0j,h);assert (ca,cb)==(0,1)or eh==h
 s=int(d.real)//2 if ca or cb!=1 else 0
 if ca or cb!=1:assert d.real==d.imag and d.real in(-2,2,14)
 begin=[xy(pA),xy(pB),h];L=len(word)
 for i,z,c in tr:
  t,a,alpha,beta=scalar(pA,pB+z)
  if ca==0 and cb==1:
   r=beta%7;lo=hi=(alpha//7,beta//7);order=(block,i);G[t,a,r].append({'lo':lo,'hi':hi,'order':order,'turn':c})
  elif s in(-1,1):
   if s==1:lA,lB,uA,uB=alpha,beta,alpha+ca,beta+cb-1
   else:lA,lB,uA,uB=alpha-ca,beta-cb+1,alpha,beta
   assert lA%7==uA%7==0
   for r in range(7):
    lo=(lA//7,-((r-lB)//7));hi=(uA//7,(uB-r)//7);order=(block,i-L*beta//s)
    G[t,a,r].append({'lo':lo,'hi':hi,'order':order,'turn':c})
  else:
   assert s==7;r=beta%7;lo=(alpha//7,beta//7);hi=(alpha//7+ca,beta//7+cb-1);order=(block,7*i-L*beta)
   G[t,a,r].append({'lo':lo,'hi':hi,'order':order,'turn':c})
 pA+=ca*d;pB+=cb*d;h=eh;blocks.append({'kind':kind,'count':[ca,cb],'period':L,'word_sha256':hashlib.sha256(word.encode()).hexdigest(),'start':begin,'end':[xy(pA),xy(pB),h]});block+=1


for j,(x,y) in enumerate(M['seed_families']):addseed(complex(x[0],y[0]),complex(x[1],y[1]),j)
timeA=timeB=0
for st in M['stages']:
 assert [int(pA.real),int(pB.real)]==st['start_x_N_constant']
 assert [int(pA.imag),int(pB.imag)]==st['start_y_N_constant'] and h==st['heading']
 assert [timeA,timeB]==st['start_time_N_constant']
 ca,cb=st['count_N_constant'];addblock(st['word'],(ca,cb),st['kind'])
 timeA+=len(st['word'])*ca;timeB+=len(st['word'])*cb
assert len(seeds)==184 and len(blocks)==16 and (timeA,timeB)==(25588,91747)
assert (pA,pB,h)==(14+14j,-6-6j,0)
# Each read template has one occurrence at each eligible (N,w), and its
# chronological rank within the spatial cell is the fixed order key above.
reports=[];total_regions=total_slabs=total_obligations=0;digest=hashlib.sha256();globalcuts={1}
for key,rs in sorted(G.items()):
 lines=sorted(set([tuple(x['lo'])for x in rs]+[(x['hi'][0],x['hi'][1]+1)for x in rs]));cuts={1}
 for i,(a,b)in enumerate(lines):
  for c,d in lines[:i]:
   if a==c:continue
   floor=(d-b)//(a-c)
   for n in(floor,floor+1):
    if n>=1:cuts.add(n)
 cuts=sorted(cuts);globalcuts.update(cuts);regions=[]
 for idx,n in enumerate(cuts):
  end=cuts[idx+1]-1 if idx+1<len(cuts)else None;ordered=sorted(lines,key=lambda z:(z[0]*n+z[1],z));values=defaultdict(list)
  for line in ordered:values[line[0]*n+line[1]].append(line)
  vals=sorted(values)
  # Explicit sign-stability check on the whole integer parameter interval.
  for val,ls in values.items():
   if end is None or end>n:assert len(set(ls))==1
  reprs=[values[val][0]for val in vals]
  for left,right in zip(reprs,reprs[1:]):
   aa=right[0]-left[0];bb=right[1]-left[1];assert aa*n+bb>0
   if end is None:assert aa>=0
   else:assert aa*end+bb>0
  slabrows=0;obligations=0;blackA=blackB=0
  for v,nextv in zip(vals,vals[1:]):
   act=[x for x in rs if x['lo'][0]*n+x['lo'][1]<=v<=x['hi'][0]*n+x['hi'][1]]
   rd=sorted([x for x in act if 'turn'in x],key=lambda x:x['order']);sd=[x for x in act if 'seed'in x]
   assert len(sd)<=1,(key,n,v,'duplicate seed')
   assert len({tuple(x['order'])for x in rd})==len(rd)
   assert all(a['turn']!=b['turn']for a,b in zip(rd,rd[1:])),(key,n,v,'nonalternation',rd)
   if sd:assert rd,(key,n,v,'unused seed')
   if rd:assert (rd[0]['turn']=='L')==bool(sd),(key,n,v,'initial color',rd[0],sd)
   if sd:
    left=values[v][0];right=values[nextv][0];blackA+=right[0]-left[0];blackB+=right[1]-left[1]
   record=[key,n,end,values[v][0],values[nextv][0],[x.get('order')for x in rd],[x.get('seed')for x in sd]];digest.update(json.dumps(record,separators=(',',':')).encode());slabrows+=1;obligations+=len(rd)
  regions.append({'N_min':n,'N_max':end,'boundary_lines':len(lines),'spatial_slabs':slabrows,'read_obligations':obligations,'first_L_count_affine':[blackA,blackB]});total_regions+=1;total_slabs+=slabrows;total_obligations+=obligations
 reports.append({'physical_class':key,'read_templates':sum('turn'in x for x in rs),'seed_templates':sum('seed'in x for x in rs),'regions':regions})
# Independently sum all regional affine first-L cardinalities at every global
# interval. This verifies constant184, not merely a finite sample count.
globalcounts=[]
for n in sorted(globalcuts):
 A=B=0
 for group in reports:
  rr=next(z for z in group['regions']if z['N_min']<=n and(z['N_max']is None or n<=z['N_max']));a,b=rr['first_L_count_affine'];A+=a;B+=b
 assert(A,B)==(0,184),(n,A,B);globalcounts.append(n)

# The exact inverse ten turns follow from the co-moving source and no remote collision.
cofixed={complex(*b)-(33+70j)for a,b,tag in seeds if complex(*a)==14+14j};assert len(cofixed)==13
back=set(cofixed);p=0j;hh=3;rev=[];backreads=[]
for _ in range(10):
 p-=D[hh];backreads.append(p);post=p in back;rev.append('R'if post else'L');hh=(hh+(-1 if post else 1))%4;back.symmetric_difference_update({p})
history=''.join(rev[::-1]);assert history=='LRLRRRRLLL'
for aa,bb,tag in seeds:
 A=complex(*aa)-(14+14j);B=complex(*bb)-(33+70j)
 if A==0:continue
 for q in backreads:
  n=Fraction(int((q-B).real),int(A.real));assert not(n.denominator==1 and n>=1 and int(A.imag)*n==int((q-B).imag))
assert all(len(W)%d or W!=W[:d]*(len(W)//d)for d in range(1,len(W)))
assert all(len(H)%d or H!=H[:d]*(len(H)//d)for d in range(1,len(H)))
allowed={(H*2)[i:i+10]for i in range(104)};assert len(allowed)==84
compressed=''.join(st['word']for st in M['stages'][:-1])
def cost(w):
 s=history+w;return sum(s[i:i+10]not in allowed and s[i+1:i+11]not in allowed for i in range(len(w)))
assert [cost(compressed+W*n)for n in(1,2,3)]==[706,1320,1934]
assert W[-10:]==(W*2)[-10:]
assert sum((W*2)[i:i+10]not in allowed and(W*2)[i+1:i+11]not in allowed for i in range(len(W)))==614
out=dict(status='PASS all integer N>=1',initial_mass=184,physical_classes=len(G),parameter_regions=total_regions,spatial_slabs=total_slabs,read_obligations=total_obligations,parameter_partition=sorted(globalcuts),exact_first_L_count=[0,184],true_inverse_ten=history,prefix_K=[614,92],prefix_time=[25588,91747],obligation_digest=digest.hexdigest())
assert (len(G),total_regions,total_slabs,total_obligations)==(1460,1508,4581,17470)
SELF.with_name('prefix_result.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
