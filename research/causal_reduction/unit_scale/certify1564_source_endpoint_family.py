"""Exact finite-family stabilization at the original-source fuel endpoint.

Input is the already certified constant-184 affine program through N wave
periods. At its endpoint translate by(-14N,-14N). Every prescribed subsequent
read is compared with the explicit integer-ray limit using exact parameter
eligibility intervals, including ALL old seeds/writes. No geometric cropping.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib,sys
from check1564_noncrossing_producer import H,W,V
from check_prepared1564_router_geometry import trace
from probe1564_source_endpoint_limit import build,first_bad
P=Path(__file__).resolve().parent
M=json.loads((P/'prepared1564_uniform_support_manifest.json').read_text())
A=json.loads((P/'prepared1564_source_endpoint_limit.json').read_text())
# Complete normalized checkpoint field before the next three W periods.
b,p,h=build();extra=W*3+W[:854]
for _,q,hh,c in list(trace(extra,(-6,-6),0))[:-1]:b.toggle(q)
word=extra+A['word'];rows=list(trace(word,(-6,-6),0));Q=sorted({q for _,q,hh,c in rows[:-1]})
assert rows[-1][1:3]==((-104,-24),0)
# Every family is base+a*N+drift*k,0<=k<count_c*N+count_d.
families=defaultdict(list)
for st in M['stages']:
 pp=(st['start_x_N_constant'][1],st['start_y_N_constant'][1]);hh=st['heading']
 aa=(st['start_x_N_constant'][0]-14,st['start_y_N_constant'][0]-14)
 rr=list(trace(st['word'],pp,hh));end=rr[-1][1];d=(end[0]-pp[0],end[1]-pp[1])
 cc=tuple(st['count_N_constant'])
 # Fixed literal blocks have count1 even if their displacement is nonzero;
 # treating their sole occurrence as drift0 avoids divisibility assumptions.
 if cc==(0,1):d=(0,0)
 for i,q,head,c in rr[:-1]:families[q[0]-q[1]].append((q,aa,d,cc,st['kind'],i))
for j,(x,y)in enumerate(M['seed_families']):
 q=(x[1],y[1]);a=(x[0]-14,y[0]-14);families[q[0]-q[1]].append((q,a,(0,0),(0,1),'seed',j))

def eligible(q,f):
 base,a,d,count,kind,i=f;lo=1;hi=None
 assert a[0]==a[1] and d[0]==d[1]
 if d==(0,0):
  n=None
  for j in range(2):
   dif=q[j]-base[j]
   if a[j]==0:
    if dif:return None
   else:
    if dif%a[j]:return None
    nn=dif//a[j]
    if n is not None and n!=nn:return None
    n=nn
  if n is None:return(1,None)
  return(n,n)if n>=1 else None
 if a[0]%d[0]:raise AssertionError(('parameter residue',f))
 if(q[0]-base[0])%d[0]:return None
 alpha=-a[0]//d[0];beta=(q[0]-base[0])//d[0]
 if base[1]+d[1]*beta!=q[1]or a[1]+d[1]*alpha:return None
 for m,c in[(alpha,beta),(count[0]-alpha,count[1]-1-beta)]:
  if m==0:
   if c<0:return None
  elif m>0:lo=max(lo,-(c//m))
  else:
   bound=c//(-m);hi=bound if hi is None else min(hi,bound)
 if hi is not None and lo>hi:return None
 return lo,hi

proof=[];lastbad=0;badpoints=0;eligiblecount=0
for q in Q:
 changes=Counter()
 for f in families.get(q[0]-q[1],()):
  z=eligible(q,f)
  if z:
   eligiblecount+=1;l,u=z;changes[l]^=1
   if u is not None:changes[u+1]^=1
 cuts=sorted({1}|{n for n,v in changes.items()if v});bit=False;want=b.color(q);bad=[]
 for i,n in enumerate(cuts):
  bit^=bool(changes[n]);end=cuts[i+1]-1 if i+1<len(cuts)else None
  if bit!=want:
   assert end is not None,('not a limit',q,n,bit,want)
   lastbad=max(lastbad,end);bad.append([n,end])
 if bad:badpoints+=1
 proof.append([list(q),int(want),bad])
N0=lastbad+1
contact=(31,71)
contact_prior=[eligible(contact,f)for f in families.get(contact[0]-contact[1],())]
assert not any(v is not None for v in contact_prior)
assert all(q!=contact for _,q,hh,c in list(trace(extra,(-6,-6),0))[:-1])
# Verify the entire fixed word on the exact checkpoint ray board.
pp=(-6,-6);hh=0
for i,c in enumerate(word):
 assert b.color(pp)==(c=='L'),('limit chronology',i,pp,hh,c)
 b.toggle(pp);hh=(hh+(1 if c=='R'else-1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
assert(pp,hh)==((-104,-24),0)
tail=A['events'][-1]['word'];assert first_bad(b,pp,hh,tail)[0]is None
# ALL original producer cells have normal>=-72; the outgoing full read strip
# lies strictly outside. Thus the tail sees no unmodelled remote finite edge.
tailrows=list(trace(tail,pp,hh));thull=[min(q[0]-q[1]for _,q,hh,c in tailrows[:-1]),max(q[0]-q[1]for _,q,hh,c in tailrows[:-1])]
producer_min=min(f[0][0]-f[0][1]for ff in families.values()for f in ff)
assert thull[1]<producer_min
# Reuse the independently signed FINITE-board tail oracle: every preexisting
# producer cell misses this strip, so only this finite continuation's XOR remains.
sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
tail_black={q for q in b.F if thull[0]<=q[0]-q[1]<=thull[1]}
assert first_mismatch(State(frozenset(tail_black),pp,hh),tail)is None
# Countercontrols: every standard-tail orbit gets a far actually read flip.
d=(-2,-2);reps={}
for _,q,hh,c in tailrows[:-1]:reps.setdefault((q[0]-q[1],q[0]%2),q)
for q in reps.values():
 far=(q[0]-2000000,q[1]-2000000);b.toggle(far);assert first_bad(b,pp,hh,tail)[0]is not None;b.toggle(far)
charge=word.count('R')-word.count('L')
factors={''.join(H[(i+j)%104]for j in range(10))for i in range(104)}
history=W[-10:];bad=history not in factors;K=0
for c in word:
 history=(history+c)[-10:];nextbad=history not in factors;K+=bad and nextbad;bad=nextbad
assert not bad
assert K==25416
out={'scope':__doc__,'status':'EXACT ALL-N CAPTURE FOR N >= THRESHOLD','threshold_N':N0,'first_extra_wave_failure':{'offset_after_N_periods':len(extra),'pose_normalized':[[31,71],2],'wanted':'L','actual':'R','phase':854},
 'after_checkpoint_word':word,'length':len(word),'fixed_read_cells':len(Q),'nonempty_family_eligibilities':eligiblecount,'exceptional_read_cells':badpoints,
 'parameter_color_proof':proof,'parameter_color_proof_sha256':hashlib.sha256(json.dumps(proof,separators=(',',':')).encode()).hexdigest(),
 'capture_time_N_constant':[25588,91747+len(word)],'capture_pose_N_constant':[[14,-104],[14,-24],0],
 'capture_mass_N_constant':[2876,10805+charge],'continuation_K':K,'complete_K_N_constant':[614,92+K],'capture_word':tail,'capture_drift':[-2,-2],
 'missing_fuel_unread_all_N':True,'outgoing_read_normal_hull':thull,'tail_strip_black':sorted(tail_black),'all_producer_min_normal':producer_min,'far_flip_controls':len(reps),
 'manifest_sha256':hashlib.sha256((P/'prepared1564_uniform_support_manifest.json').read_bytes()).hexdigest(),
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared1564_source_endpoint_family.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in('after_checkpoint_word','parameter_color_proof')},indent=2))
