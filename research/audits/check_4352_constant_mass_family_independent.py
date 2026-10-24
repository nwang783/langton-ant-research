"""Exact ALL-N physical chronology for the supplied394-cell4352 producer.
No author simulator/guard imports. Affine arrangement coverage, not extrapolation.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale';R=ROOT/'nonlinear_global_budget_2026-10-23';D=(1j,1,-1j,-1)
mp=U/'prepared4352_uniform_support_manifest.json';manifest=json.loads(mp.read_text());assert hashlib.sha256(mp.read_bytes()).hexdigest()=='e3f1940d073741ad8bf48a4a8f6b33942569c4a20bc23c2809bf885ae9f0f6d4'
H=json.loads((ROOT/'deliverables/constant_184_capturing_family/family_data.json').read_text())['standard_word'];W=json.loads((R/'second_prepared_wave_certificate.json').read_text())['word'];launch=json.loads((U/'prepared4352_fresh_launch.json').read_text());plan=json.loads((U/'prepared4352_noncrossing_router_plan.json').read_text())
xy=lambda z:(int(z.real),int(z.imag))
def lit(w,p=0j,h=3):
 out=[]
 for i,c in enumerate(w):out.append((i,p,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return out,p,h
# Rebuild every read family directly from the frozen literal contract.
G=defaultdict(list);seeds=[];blocks=[];pA=26+26j;pB=113+88j;h=3;timeA=timeB=0;massA=0;massB=394

def scalar(A,B):
 assert A.real==A.imag and int(A.real)%26==0
 a=int(B.real)%2;return int(B.real-B.imag),a,int(A.real)//2,(int(B.real)-a)//2
for idx,(x,y)in enumerate(manifest['seed_families']):
 A=complex(x[0],y[0]);B=complex(x[1],y[1]);t,a,alpha,beta=scalar(A,B);res=beta%13;v=alpha//13,beta//13
 G[t,a,res].append(dict(lo=v,hi=v,seed=idx));seeds.append((A,B))
assert len(seeds)==394
for block,given in enumerate(manifest['stages']):
 ca,cb=given['count_N_constant'];word=given['word'];assert ca>=0 and ca+cb>=1
 assert [int(pA.real),int(pB.real)]==given['start_x_N_constant']and[int(pA.imag),int(pB.imag)]==given['start_y_N_constant']and h==given['heading']
 assert [timeA,timeB]==given['start_time_N_constant']
 tr,d,eh=lit(word,h=h);L=len(word);repeat=(ca,cb)!=(0,1)
 if repeat:assert eh==h and d.real==d.imag and d.real in(-2,2,26)
 s=int(d.real)//2 if repeat else 0
 for i,z,c in tr:
  t,a,alpha,beta=scalar(pA,pB+z)
  if not repeat:
   res=beta%13;lo=hi=(alpha//13,beta//13);G[t,a,res].append(dict(lo=lo,hi=hi,order=(block,i),turn=c))
  elif s in(-1,1):
   if s==1:lA,lB,uA,uB=alpha,beta,alpha+ca,beta+cb-1
   else:lA,lB,uA,uB=alpha-ca,beta-cb+1,alpha,beta
   assert lA%13==uA%13==0
   for res in range(13):
    lo=lA//13,-((res-lB)//13);hi=uA//13,(uB-res)//13;G[t,a,res].append(dict(lo=lo,hi=hi,order=(block,i-L*beta//s),turn=c))
  else:
   assert s==13;res=beta%13;lo=alpha//13,beta//13;hi=alpha//13+ca,beta//13+cb-1;G[t,a,res].append(dict(lo=lo,hi=hi,order=(block,13*i-L*beta),turn=c))
 blocks.append(dict(kind=given['kind'],count=[ca,cb],word=word,start=[xy(pA),xy(pB),h],period=L))
 pA+=ca*d;pB+=cb*d;h=eh;timeA+=ca*L;timeB+=cb*L;massA+=ca*(word.count('R')-word.count('L'));massB+=cb*(word.count('R')-word.count('L'))
assert len(blocks)==12 and (pA,pB,h)==(26+26j,-2+3j,3)and(timeA,timeB)==(38152,144402)and(massA,massB)==(4084,16654)
assert all(b['word']==H for b in blocks if b['kind']=='H')
assert [b['word']for b in blocks if b['kind']=='router']==[r['word']for r in plan['routers']]
assert blocks[-3]['word']==H[:28]and blocks[-2]['word']==launch['forward_prelude_word']and blocks[-1]['word']==W

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
# interval. This verifies constant394, not merely a finite sample count.
globalcounts=[]
for n in sorted(globalcuts):
 A=B=0
 for group in reports:
  rr=next(z for z in group['regions']if z['N_min']<=n and(z['N_max']is None or n<=z['N_max']));a,b=rr['first_L_count_affine'];A+=a;B+=b
 assert(A,B)==(0,394),(n,A,B);globalcounts.append(n)
# True inverse history: derive the canonical13 source, then exclude EVERY remote
# affine initial point from every inverse read for the entire N>=1 domain.
tr,_,_=lit(H*30);first={};last={}
for i,z,c in tr:
 if z not in first:first[z]=c
 else:assert last[z]!=c
 last[z]=c
Hseed={z for z,c in first.items()if c=='L'};assert len(Hseed)==13
initialA=26+26j;initialB=113+88j;source={(initialA,initialB+z)for z in Hseed};assert source<=set(seeds)
back=set(Hseed);bp=0j;bh=3;rev=[];backreads=[]
for _ in range(10):
 bp-=D[bh];backreads.append(bp);post=bp in back;rev.append('R'if post else'L');bh=(bh+(-1 if post else 1))%4;back.symmetric_difference_update({bp})
hist=''.join(rev[::-1]);assert hist=='LRLRRRRLLL';exclusions=0
for aa,bb in set(seeds)-source:
 A=aa-initialA;B=bb-initialB
 for q in backreads:
  if A==0:assert B!=q
  else:
   if A.real:val=Fraction(int((q-B).real),int(A.real));matches=Fraction(int(A.imag))*val==int((q-B).imag)
   else:val=Fraction(int((q-B).imag),int(A.imag));matches=int((q-B).real)==0
   assert not(matches and val.denominator==1 and val>=1)
  exclusions+=1
assert exclusions==3810
allowed={(H*2)[i:i+10]for i in range(104)};assert len(allowed)==84
compressed=''.join(b['word']for b in blocks[:-1])
def kc(w):
 z=hist+w;return sum(z[i:i+10]not in allowed and z[i+1:i+11]not in allowed for i in range(len(w)))
assert [kc(compressed+W*n)for n in(1,2,3)]==[4975,6947,8919]
assert sum((W*2)[i:i+10]not in allowed and(W*2)[i+1:i+11]not in allowed for i in range(len(W)))==1972
# Finite literal controls supplement, never replace, the all-parameter arrangement.
controls=[]
for n in(1,2,5):
 field={A*n+B for A,B in seeds};assert len(field)==394;p=initialA*n+initialB;h=3;first={};ticks=0;rolling=hist;count=0
 for b in blocks:
  assert(p,h)==(complex(*b['start'][0])*n+complex(*b['start'][1]),b['start'][2])
  for c in b['word']*(b['count'][0]*n+b['count'][1]):
   assert(p in field)==(c=='L');first.setdefault(p,c);field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h];ticks+=1
   bad=rolling not in allowed;rolling=(rolling+c)[-10:];count+=bad and rolling not in allowed
 assert{z for z,c in first.items()if c=='L'}=={A*n+B for A,B in seeds}
 assert(p,h)==((26+26j)*n-2+3j,3)and ticks==144402+38152*n and len(field)==16654+4084*n and count==1972*n+3003
 controls.append(dict(N=n,reads=ticks,final_mass=len(field),K=count,final_field_sha256=hashlib.sha256(json.dumps(sorted(map(xy,field)),separators=(',',':')).encode()).hexdigest()))
out=dict(status='PASS ALL N>=1 exact affine physical chronology of394-cell4352 producer',manifest_sha256=hashlib.sha256(mp.read_bytes()).hexdigest(),domain='N>=1,R=200+52N',initial_mass=394,read_count_affine=[38152,144402],wave_entry_time_affine=[33800,144402],final_pose_affine={'x':[26,-2],'y':[26,3],'heading':3},final_mass_affine=[4084,16654],K_count_affine=[1972,3003],true_previous_ten=hist,affine_inverse_seed_exclusions=exclusions,physical_classes=len(G),parameter_regions=total_regions,spatial_slabs=total_slabs,read_obligations=total_obligations,global_partition_starts=sorted(globalcuts),exact_first_L_count=[0,394],obligation_digest=digest.hexdigest(),literal_controls=controls,seed_families=[[xy(A),xy(B)]for A,B in seeds],blocks=[{k:v for k,v in b.items()if k!='word'}for b in blocks],groups=reports,scope='Every finite supplied prefix on the original394-cell board, ALLN. Five ordinary flights and four routers, causal289-cell launch, N4352 periods. No subsequent capture or one fixed finite infinite-wave orbit inferred.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('groups','seed_families','blocks')},indent=2))
