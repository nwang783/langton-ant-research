"""Exact all-integer-parameter checker, no author geometry or simulator imports.
R=100+28N, N>=1. Each physical orbit is split modulo14. Read and seed
eligibility become integer affine intervals; every parameter interval and
spatial slab is checked by exact ordering of all affine boundary lines.
"""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction
import json,hashlib,time
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale';R=ROOT/'nonlinear_global_budget_2026-10-23';D=(1j,1,-1j,-1)
H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];W=json.loads((R/'prepared_travelling_wave_certificate.json').read_text())['word'];plan=json.loads((U/'prepared1564_noncrossing_router_plan.json').read_text());launch=json.loads((U/'prepared1564_fresh_launch_cap.json').read_text())
def xy(z):return(int(z.real),int(z.imag))
def lit(w,p=0j,h=3):
 out=[]
 for i,c in enumerate(w):out.append((i,p,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return out,p,h
# Independent minimal thirteen-cell phase-zero H seed.
tr,_,_=lit(H*30);hist={};last={}
for i,z,c in tr:
 if z not in hist:hist[z]=c=='L'
 else:assert last[z]!=c
 last[z]=c
Hseed={z for z,c in hist.items()if c};assert len(Hseed)==13
G=defaultdict(list);seeds=[];blocks=[];block=0;pA=14+14j;pB=33+70j;h=3

def scalar(A,B):
 assert A.real==A.imag and int(A.real)%14==0
 a=int(B.real)%2;t=int(B.real-B.imag);alpha=int(A.real)//2;beta=(int(B.real)-a)//2
 return t,a,alpha,beta

def addseed(A,B,tag):
 t,a,alpha,beta=scalar(A,B);r=beta%7;v=(alpha//7,beta//7)
 G[t,a,r].append({'lo':v,'hi':v,'seed':tag});seeds.append((xy(A),xy(B),tag))
for j,z in enumerate(sorted(Hseed,key=xy)):addseed(pA,pB+z,('initial',j))

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

# Exact affine target router positions, derived from the stated six u values.
for router,(uA,uB)in zip(plan['routers'],[(-56,-197),(56,201),(-112,-397),(112,403),(-56,-199),(56,203)]):
 t,parity,hh=router['source_lane'];assert hh==h
 qA=complex(uA//2,uA//2);qB=complex((uB+t)//2,(uB-t)//2);assert int(qB.real)%2==parity
 da=qA-pA;db=qB-pB;assert da.real==da.imag and db.real==db.imag;step=2 if h==1 else -2
 assert int(da.real)%step==int(db.real)%step==0
 addblock(H,(int(da.real)//step,int(db.real)//step),'H')
 assert(pA,pB)==(qA,qB)
 for j,z in enumerate(router['extra_black_relative_input']):addseed(pA,pB+complex(*z),('router',router['index'],j))
 addblock(router['word'],(0,1),'router')
qA=0j;qB=7+6j;da=qA-pA;db=qB-pB;assert h==3 and da.real==da.imag and db.real==db.imag
addblock(H,(-int(da.real)//2,-int(db.real)//2),'H');assert(pA,pB,h)==(0j,7+6j,3)
addblock(H[:55],(0,1),'H-prefix');assert(pA,pB,h)==(0j,4+0j,2)
for j,z in enumerate(launch['fresh_cap']):addseed(0j,complex(*z),('launch',j))
addblock(launch['forward_prelude'],(0,1),'launch');assert(pA,pB,h)==(0j,-6-6j,0)
wave_block=block;addblock(W,(1,0),'wave');assert(pA,pB,h)==(14+14j,-6-6j,0)and len(seeds)==184
# Bind the entire frozen supplied contract, not merely its finite sample.
manifest_path=U/'prepared1564_uniform_support_manifest.json';manifest=json.loads(manifest_path.read_text())
assert hashlib.sha256(manifest_path.read_bytes()).hexdigest()=='90fcf1a66046418c38d07f7e935ea80cf873751aefae69a4b07af89ba3bd8399'
assert len(manifest['seed_families'])==184
assert sorted((a[0],b[0],a[1],b[1])for a,b,tag in seeds)==sorted(tuple(x+y)for x,y in manifest['seed_families'])
assert len(blocks)==len(manifest['stages'])==16
timeA=timeB=0
for own,given in zip(blocks,manifest['stages']):
 assert own['kind']==given['kind']and own['count']==given['count_N_constant']
 assert own['word_sha256']==hashlib.sha256(given['word'].encode()).hexdigest()
 aa,bb,hh=own['start'];assert [aa[0],bb[0]]==given['start_x_N_constant']and[aa[1],bb[1]]==given['start_y_N_constant']and hh==given['heading']
 assert [timeA,timeB]==given['start_time_N_constant']
 timeA+=own['period']*own['count'][0];timeB+=own['period']*own['count'][1]
assert(timeA,timeB)==(25588,91747)
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
# Exact defect count from last-ten memory, using one H copy for each nonempty
# standard power. Its interior is standard and its boundary words are fixed.
allowed={(H*2)[i:i+10]for i in range(104)};assert len(allowed)==84
# Exact true-history stabilization, using all184 affine seed families.
back=set(Hseed);bp=0j;bh=3;rev=[];backreads=[]
for _ in range(10):
 bp-=D[bh];backreads.append(bp);post=bp in back;rev.append('R'if post else'L');bh=(bh+(-1 if post else 1))%4;back.symmetric_difference_update({bp})
hist=''.join(rev[::-1]);assert hist=='LRLRRRRLLL'
for aa,bb,tag in seeds:
 if tag[0]=='initial':continue
 A=complex(*aa)-(14+14j);B=complex(*bb)-(33+70j)
 for q in backreads:
  if A==0:assert B!=q
  else:
   if A.real:
    val=Fraction(int((q-B).real),int(A.real))
    matches=Fraction(int(A.imag))*val==int((q-B).imag)
   else:
    val=Fraction(int((q-B).imag),int(A.imag));matches=int((q-B).real)==0
   assert not(matches and val.denominator==1 and val>=1),(tag,q,val)

def kc(w):
 s=hist+w;return sum(s[i:i+10]not in allowed and s[i+1:i+11]not in allowed for i in range(len(w)))
compressed=''
for b in blocks[:-1]:
 if b['kind']=='H':compressed+=H
 elif b['kind']=='router':compressed+=plan['routers'][sum(x['kind']=='router'for x in blocks[:blocks.index(b)])]['word']
 elif b['kind']=='H-prefix':compressed+=H[:55]
 elif b['kind']=='launch':compressed+=launch['forward_prelude']
k1=kc(compressed+W);k2=kc(compressed+W*2);k3=kc(compressed+W*3);assert(k1,k2,k3)==(706,1320,1934)
# The cycle automaton returns to the same10-bit state after every W;
# therefore the exact additional cost614 holds for every further period.
assert W[-10:]==(W*2)[-10:];assert sum((W*2)[i:i+10]not in allowed and(W*2)[i+1:i+11]not in allowed for i in range(len(W)))==614
# A fresh whole-board implementation checks three finite specializations;
# these are controls only, not the parameter-completeness argument.
controls=[]
for nn in (1,2,5):
 seed={complex(*a)*nn+complex(*b)for a,b,tag in seeds};assert len(seed)==184
 p=(14+14j)*nn+(33+70j);hh=3;field=set(seed);first={};ticks=0;router_index=0
 for b in blocks:
  assert [xy(p),hh]==[xy(complex(*b['start'][0])*nn+complex(*b['start'][1])),b['start'][2]]
  if b['kind']=='H':word=H
  elif b['kind']=='router':word=plan['routers'][router_index]['word'];router_index+=1
  elif b['kind']=='H-prefix':word=H[:55]
  elif b['kind']=='launch':word=launch['forward_prelude']
  else:word=W
  for c in word*(b['count'][0]*nn+b['count'][1]):
   first.setdefault(p,c);assert(p in field)==(c=='L');field.symmetric_difference_update({p});hh=(hh+(1 if c=='R'else-1))%4;p+=D[hh];ticks+=1
 assert {z for z,c in first.items()if c=='L'}==seed
 assert (p,hh)==((14+14j)*nn-6-6j,0)and ticks==91747+25588*nn and len(field)==10805+2876*nn
 controls.append({'N':nn,'R':100+28*nn,'reads':ticks,'final_mass':len(field)})
out={'status':'PASS ALL N>=1 exact affine chronology and constant184-cell first-L input for R=100+28N','supplied_manifest_sha256':hashlib.sha256(manifest_path.read_bytes()).hexdigest(),'router_plan_sha256':hashlib.sha256((U/'prepared1564_noncrossing_router_plan.json').read_bytes()).hexdigest(),'domain':'integer N>=1, R=100+28N','seed_count':184,'seed_families':[{'coefficient':a,'constant':b,'tag':tag}for a,b,tag in seeds],'blocks':blocks,'physical_classes':len(G),'parameter_regions_total':total_regions,'spatial_slabs_total':total_slabs,'chronological_read_obligations':total_obligations,'global_parameter_partition_starts':sorted(globalcuts),'all_first_L_counts':[0,184],'obligation_digest':digest.hexdigest(),'K_word_count_affine':[614,92],'actual_true_inverse_history':hist,'read_count_affine':[25588,91747],'wave_entry_time_affine':[24024,91747],'final_mass_affine':[2876,10805],'literal_controls':controls,'groups':reports,'scope':'Every supplied finite word is physically legal on its184-cell finite seed for ALL N>=1. Exact finite N-wave episodes only, not an infinite wave from a fixed finite board or eventual capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('groups','seed_families','blocks')},indent=2))
