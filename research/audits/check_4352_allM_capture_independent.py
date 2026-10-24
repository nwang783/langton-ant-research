"""Exact all-M original394-cell full capture, including every infinite tail read.
Independent physical affine arrangement, no author simulator/guard imports.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale';D=(1j,1,-1j,-1);MOD=39
original=json.loads((U/'prepared4352_uniform_support_manifest.json').read_text());supply=json.loads((U/'prepared4352_finite_return_supply.json').read_text());wave=json.loads((U/'prepared4352_output_return_wave.json').read_text());H=json.loads((ROOT/'deliverables/constant_184_capturing_family/family_data.json').read_text())['standard_word']
xy=lambda z:(int(z.real),int(z.imag))
def lit(w,p=0j,h=3):
 out=[]
 for i,c in enumerate(w):out.append((i,p,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return out,p,h
stages=[]
for st in original['stages']:
 q=dict(st)
 for key in ['start_x_N_constant','start_y_N_constant','count_N_constant','start_time_N_constant']:
  a,b=st[key];q[key]=[3*a,4*a+b]
 stages.append(q)
W=stages[-1]['word'];transition=W*3+W[:2331]+wave['prefix_word'];assert transition==supply['transition_after_N_waves']and len(transition)==158151
stages.extend([dict(kind='finite source-end response',word=transition,count_N_constant=[0,1],start_x_N_constant=[78,102],start_y_N_constant=[78,107],heading=3,start_time_N_constant=[114456,297010]),dict(kind='opposite15324 return',word=wave['word'],count_N_constant=[1,0],start_x_N_constant=[78,117],start_y_N_constant=[78,111],heading=0,start_time_N_constant=[114456,455161])])
CAP=json.loads((U/'prepared4352_capture_manifest.json').read_text());assert hashlib.sha256((U/'prepared4352_capture_manifest.json').read_bytes()).hexdigest()=='52d80fe06d739254a9d71615de67bfb6639d1f4d1301455b4f332d7110874f9b'
for x,y in zip(stages,CAP['stages']):
 for key in ['word','heading','count_N_constant','start_x_N_constant','start_y_N_constant','start_time_N_constant']:assert x[key]==y[key]
stages.extend(CAP['stages'][14:])
G=defaultdict(list);seeds=[];blocks=[];pA=78+78j;pB=217+192j;h=3;timeA=timeB=0;massA=0;massB=394

def scalar(A,B):
 assert A.real==A.imag and int(A.real)%78==0
 a=int(B.real)%2;return int(B.real-B.imag),a,int(A.real)//2,(int(B.real)-a)//2
for idx,(x,y)in enumerate(original['seed_families']):
 A=complex(3*x[0],3*y[0]);B=complex(4*x[0]+x[1],4*y[0]+y[1]);t,a,alpha,beta=scalar(A,B);res=beta%MOD;v=alpha//MOD,beta//MOD
 G[t,a,res].append(dict(lo=v,hi=v,seed=idx));seeds.append((A,B))
assert len(seeds)==394
for block,given in enumerate(stages):
 ca,cb=given['count_N_constant'];word=given['word'];assert ca>=0 and ca+cb>=1
 assert [int(pA.real),int(pB.real)]==given['start_x_N_constant']and[int(pA.imag),int(pB.imag)]==given['start_y_N_constant']and h==given['heading']
 assert [timeA,timeB]==given['start_time_N_constant']
 tr,d,eh=lit(word,h=h);L=len(word);repeat=(ca,cb)!=(0,1)
 if repeat:assert eh==h and d.real==d.imag and d.real in(-78,-2,2,26)
 s=int(d.real)//2 if repeat else 0
 for i,z,c in tr:
  t,a,alpha,beta=scalar(pA,pB+z)
  if not repeat:
   res=beta%MOD;lo=hi=(alpha//MOD,beta//MOD);G[t,a,res].append(dict(lo=lo,hi=hi,order=(block,i),turn=c))
  else:
   if s>0:lA,lB,uA,uB=alpha,beta,alpha+ca*s,beta+(cb-1)*s
   else:lA,lB,uA,uB=alpha+ca*s,beta+(cb-1)*s,alpha,beta
   assert lA%MOD==uA%MOD==0 and MOD%abs(s)==0
   for res in range(MOD):
    if (res-beta)%abs(s):continue
    lo=lA//MOD,-((res-lB)//MOD);hi=uA//MOD,(uB-res)//MOD
    order=(block,abs(s)*i-L*beta*(1 if s>0 else-1))
    G[t,a,res].append(dict(lo=lo,hi=hi,order=order,turn=c))
 blocks.append(dict(kind=given['kind'],count=[ca,cb],word=word,start=[xy(pA),xy(pB),h],period=L))
 pA+=ca*d;pB+=cb*d;h=eh;timeA+=ca*L;timeB+=cb*L;massA+=ca*(word.count('R')-word.count('L'));massB+=cb*(word.count('R')-word.count('L'))
assert len(blocks)==18 and(pA,pB,h)==(-156-156j,-399-429j,0)and(timeA,timeB)==(137892,514609)and(massA,massB)==(13596,41167)
# Append infinitely many literal SW104 copies as negative-infinite physical
# intervals. No final-field truncation or sampled tail is used.
tail=CAP['tail_word'];assert tail in{H[i:]+H[:i]for i in range(104)}
tr,d,eh=lit(tail,h=h);assert d==-2-2j and eh==h
for i,z,c in tr:
 t,a,alpha,beta=scalar(pA,pB+z)
 for res in range(MOD):
  hi=alpha//MOD,(beta-res)//MOD;G[t,a,res].append(dict(lo=None,hi=hi,order=(18,i+104*beta),turn=c))

reports=[];total_regions=total_slabs=total_obligations=0;digest=hashlib.sha256();globalcuts={1}
for key,rs in sorted(G.items()):
 lines=sorted(set([tuple(x['lo'])for x in rs if x['lo']is not None]+[(x['hi'][0],x['hi'][1]+1)for x in rs]));cuts={1}
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
  for v,nextv in [(None,vals[0])]+list(zip(vals,vals[1:]))+[(vals[-1],None)]:
   probe=nextv-1 if v is None else v
   act=[x for x in rs if(x['lo']is None or x['lo'][0]*n+x['lo'][1]<=probe)and probe<=x['hi'][0]*n+x['hi'][1]]
   rd=sorted([x for x in act if 'turn'in x],key=lambda x:x['order']);sd=[x for x in act if 'seed'in x]
   assert len(sd)<=1,(key,n,v,'duplicate seed')
   assert len({tuple(x['order'])for x in rd})==len(rd)
   assert all(a['turn']!=b['turn']for a,b in zip(rd,rd[1:])),(key,n,v,'nonalternation',rd)
   if sd:assert rd,(key,n,v,'unused seed')
   if rd:assert (rd[0]['turn']=='L')==bool(sd),(key,n,v,'initial color',rd[0],sd)
   if sd:
    assert v is not None and nextv is not None
    left=values[v][0];right=values[nextv][0];blackA+=right[0]-left[0];blackB+=right[1]-left[1]
   record=[key,n,end,None if v is None else values[v][0],None if nextv is None else values[nextv][0],[x.get('order')for x in rd],[x.get('seed')for x in sd]];digest.update(json.dumps(record,separators=(',',':')).encode());slabrows+=1;obligations+=len(rd)
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

# Exact true-history premise inherited from independently reconstructed original
# family, specialized N=3M+4. All remote cells were excluded for EVERY N>=1.
prior=json.loads((SELF.with_name('check_4352_constant_mass_family_independent.json')).read_text());assert prior['true_previous_ten']=='LRLRRRRLLL'and prior['affine_inverse_seed_exclusions']==3810
hist=prior['true_previous_ten'];allowed={(H*2)[i:i+10]for i in range(104)}
def kc(w):
 z=hist+w;return sum(z[i:i+10]not in allowed and z[i+1:i+11]not in allowed for i in range(len(w)))
# Every repeated prefix block has identical ten-read suffix and zero standard
# interior K. Keeping one H per occurrence preserves seams. W and return loops
# have exact additive cyclic K after their first full period.
for m in(1,2,3):
 candidate=''.join(b['word']*(1 if b['word']in{H[i:]+H[:i]for i in range(104)}else b['count'][0]*m+b['count'][1])for b in blocks)
 assert kc(candidate+tail[:10])==13269*m+104594,(m,kc(candidate+tail[:10]))
controls=[]
for m in(1,2):
 field={A*m+B for A,B in seeds};assert len(field)==394;p=(78+78j)*m+217+192j;h=3;ticks=0;rolling=hist;K=0;first={}
 for b in blocks:
  assert(p,h)==(complex(*b['start'][0])*m+complex(*b['start'][1]),b['start'][2])
  for c in b['word']*(b['count'][0]*m+b['count'][1]):
   assert(p in field)==(c=='L'),(m,ticks,xy(p),h,c)
   first.setdefault(p,c);field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h];ticks+=1;bad=rolling not in allowed;rolling=(rolling+c)[-10:];K+=bad and rolling not in allowed
 assert {q for q,c in first.items()if c=='L'}=={A*m+B for A,B in seeds}
 assert(ticks,p,h,len(field))==(514609+137892*m,(-156-156j)*m-399-429j,0,41167+13596*m)
 # Account for all ten-window seam events beyond this supplied tail section.
 for c in tail[:10]:bad=rolling not in allowed;rolling=(rolling+c)[-10:];K+=bad and rolling not in allowed
 assert K==104594+13269*m

 controls.append(dict(M=m,producer_N=3*m+4,reads=ticks,final_mass=len(field),K=K,final_field_sha256=hashlib.sha256(json.dumps(sorted(map(xy,field)),separators=(',',':')).encode()).hexdigest()))
out=dict(status='PASS ALL M>=1 original394-cell complete capture including infinite SW104 tail',domain='M>=1, original producer N=3M+4',original_mass=394,stage_count=len(blocks),read_count_affine=[137892,514609],end_pose_affine=[[-156,-399],[-156,-429],0],end_mass_affine=[13596,41167],K_count_affine=[13269,104594],tail_drift=[-2,-2],infinite_tail_orbit_intervals=104*39,physical_classes=len(G),parameter_regions=total_regions,spatial_slabs=total_slabs,read_obligations=total_obligations,global_partition_starts=sorted(globalcuts),exact_first_L_count=[0,394],obligation_digest=digest.hexdigest(),literal_controls=controls,source_hashes={n:hashlib.sha256((U/n).read_bytes()).hexdigest()for n in ['prepared4352_uniform_support_manifest.json','prepared4352_finite_return_supply.json','prepared4352_output_return_wave.json','prepared4352_capture_manifest.json']},groups=reports,scope='Every original394-cell member N=3M+4, M>=1, executes both growing nonstandard phases and eventually captures SW104. All future tail reads are included as exact negative-infinite physical intervals. No claim for other original N or universal capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='groups'},indent=2))
