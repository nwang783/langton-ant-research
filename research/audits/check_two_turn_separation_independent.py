from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'ordinary_two_turn_noninterpenetration_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF).startswith('238543f4')
mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'two_turn_separation.json').read_text());lib=S.with_name('check_old_V_second_age1_independent.py');n={'__file__':str(lib)};exec(lib.read_text().split('# Universal')[0],n)
W,M,K,tr,rot,center,cross,xy=[n[k]for k in('W','M','K','tr','rot','center','cross','xy')];raw={a:tr(W[a])for a in'DCVU'};ctx={a:tr(W[a]+M)for a in raw};vec={a:center(raw[a]['p'],raw[a]['h'])-center(0j,0)for a in raw};assert vec==dict(D=2+2j,C=2+2j,V=2+6j,U=8j)
alpha={'D':(1,0),'C':(1,0),'V':(1,1),'U':(2,0)};order={'D':0,'C':0,'V':1,'U':2}
for a in raw:
 for b in raw:
  x=2*(a=='C')+alpha[b][0]-alpha[a][0];y=alpha[b][1]-alpha[a][1];assert -4<min(x,x+y)<=max(x,x+y)<4
  z=next(z for z in J['all16_exact_principal_ordinary_joins']if(z['old'],z['new'])==(a,b));assert(z['principal_join_coeff_pi_over4'],z['principal_join_coeff_gamma'])==(x,y)
  t=(4+alpha[b][0]-alpha[a][0],alpha[b][1]-alpha[a][1]);assert 3<=min(t[0],sum(t))<=max(t[0],sum(t))<=5
  z=next(z for z in J['all16_source_relative_two_C_turn_forms']if(z['source'],z['actor'])==(a,b));assert(z['T_coeff_pi_over4'],z['T_coeff_gamma'])==t and z['possible_T_strictly_above_pi']==(order[b]>order[a])
for a in raw:
 for h in(2,1,0):
  z=tr(W[a],0j,h);dv=center(z['p'],z['h'])-center(0j,h);assert dv==rot(h)*vec[a]
  if h==2:assert dv.real<=0 and dv.imag<0
  elif h==1:assert dv.real>0 and dv.imag<=0
  else:assert dv.real>=0 and dv.imag>0
# Actual C1 reset and both E cases, independent of any fresh-output reserve.
for q,t in[(-1,1),(-1-1j,2),(-1j,3)]:assert raw['C']['last'][q]==('L',t)
assert tr(W['C']+W['U']+M)['bad']
for a in'DV':assert min(q.real for q,h,c in raw[a]['reads']if c=='R')>=0 and(rot(1)*raw[a]['p']).imag==-1
assert min(q.real for q,h,c in raw['C']['reads']if c=='R')>=0

def contact(a,b,c,d):
 u=b-a;v=d-c;q=c-a;den=cross(u,v)
 if den:
  s,t=F(cross(q,v),den),F(cross(q,u),den)
  return(s,t,False,None)if 0<=s<=1 and 0<=t<=1 else None
 if cross(q,u):return None
 coord=lambda p:int(p.real)if v.real else int(p.imag)
 ends=[F(coord(a-c),coord(v)),F(coord(b-c),coord(v))];lo=max(F(0),min(ends));hi=min(F(1),max(ends))
 if lo>hi:return None
 # v and u are axis/diagonal integer multiples, use exact component arithmetic.
 ax=0 if u.real else 1;val=lambda p:int(p.real)if ax==0 else int(p.imag);ss=(F(val(c-a))+lo*val(v))/val(u)
 return ss,lo,True,(lo,hi)
rows={};witnesses=[];a=1+1j
for source in raw:
 u=-vec[source];b=a+u
 for actor in raw:
  v=vec[actor];corners=[1+1j+s*u/2-t*v/2 for s in(0,1)for t in(0,1)];xr=range(math.floor(min(p.real for p in corners)),math.ceil(max(p.real for p in corners))+1);yr=range(math.floor(min(p.imag for p in corners)),math.ceil(max(p.imag for p in corners))+1)
  for x in xr:
   for y in yr:
    if(x+y)%2:continue
    p=complex(x,y);c=center(p,0);z=contact(a,b,c,c+v)
    if z is None:continue
    s,t,parallel,interval=z;key=(source,actor,x,y)
    if t==0:route='earlier_executed_new_endpoint'
    elif s==1:route='old_terminal_has_outgoing_owner'
    else:
     assert not parallel
     if order[actor]<=order[source]:route='relative_two_C_Jordan_angle'
     else:
      I={q for q,black in ctx[actor]['req'].items()if black and q not in K};ws=[g for g in(1,1+1j,1j)if g-p in I];assert ws
      firsts=[next(i for i,(q,h,c)in enumerate(ctx[actor]['reads'])if q==g-p)for g in ws];assert any(i<len(W[actor])for i in firsts);witnesses.append([source,actor,[x,y],list(map(xy,ws)),firsts]);route='unavailable_deleted_true_input'
    rows[key]=(str(s),str(t),parallel,route)
ref={(z['old_source'],z['new_actor'],*z['N_ENTRY'][:2]):(z['closed_intersection']['old_s'],z['closed_intersection']['new_t'],z['closed_intersection']['parallel'],z['route'])for z in J['all_closed_oldS_newN_pair_rows']}
assert rows==ref and len(rows)==72 and dict(Counter(v[3]for v in rows.values()))==J['closed_pair_counts']
assert Counter(v[3]for v in rows.values())=={'earlier_executed_new_endpoint':36,'old_terminal_has_outgoing_owner':20,'relative_two_C_Jordan_angle':8,'unavailable_deleted_true_input':8}
# Entire prepared controls, without assuming a preceding RAW or old V-cohort seal.
controls=[]
for labels in('DCCC','VCCVC'):
 word=''.join(W[a]for a in labels)+M;z=tr(word,0j,2);assert not z['bad'];seed={q for q,b in z['req'].items()if b};B=set(seed)
 for q,h,c in z['reads']:assert(q in B)==(c=='L');B.symmetric_difference_update({q})
 p=0j;h=2;segments=[]
 for A in labels:
  zz=tr(W[A],p,h);segments.append((center(p,h),center(zz['p'],zz['h'])));p,h=zz['p'],zz['h']
 for j,(c,d)in enumerate(segments):
  for i,(a,b)in enumerate(segments[:j]):
   hit=contact(a,b,c,d)
   if hit is None:continue
   assert j==i+1 and hit[0]==1 and hit[1]==0 and(not hit[2]or hit[3][0]==hit[3][1])
 controls.append(dict(labels=labels,seed=list(map(xy,sorted(seed,key=lambda q:(q.real,q.imag)))),reads=len(word),final_mass=len(B),simple_relative_proxy=True))
 assert labels!='DCCC'or set(map(tuple,J['prepared_DCCC_positive_regression']['complete_final_BLACK']))=={tuple(xy(q))for q in B}
q=tr(W['Q']);assert(q['p'],q['h'])==(-4-4j,2);c=tr(W['C'],-6-2j,0);assert(c['p'],c['h'])==(-6-1j,3)and center(q['p'],2)==-7-7j and center(c['p'],3)==-11-3j
probe='UQDDDDVCDCVUUC';bad=tr(''.join(W[a]for a in probe)+M)['bad'];assert bad==(221,133,-7-4j,'L')
out=dict(status='PASS relative ordinary two-turn separation and exact completed Q-C3 gate',manifest=sha(MF),dependencies=mf['dependencies'],closed_counts=J['closed_pair_counts'],all72_rows=[dict(key=k,result=v)for k,v in sorted(rows.items())],eight_deleted_external_inputs=witnesses,complete_positive_controls=controls,analytic=[
'All S chords strictly decrease corrected y, all E chords strictly increase corrected x, and all N chords including terminal C3 strictly increase corrected y. C1 drops below the S terminal; E stays there and C2 drops again. N begins two corrected-x units beyond the E end and cannot revisit E/C2 except its legitimate initial adjacency. Thus any first nonadjacent contact of the selected factor is between N and S/C1.',
'Relative earliest contact licenses a simple source-to-contact subarc, independently of any geometry before this selected factor. A new ENTRY repeat is assigned to the preceding actually executed END; C2 cannot be that first repeat by separation. An old S terminal is owned by its outgoing S piece or C1. C1 END belongs to the separated E/C2 part. Opposite-collinear approach either is already touching at new ENTRY or first hits an old terminal; after outgoing reassignment, an opposite continuation would intersect immediately BEFORE that point, contradicting earliest onset. Thus no parallel strict-onset case is missing.',
'Each of16 actual principal joins is pi/2 times preceding-C plus alpha_next-alpha_previous. Along the simple loop there are exactly C1/C2, including sourceC1 own outgoing join but excluding actorC3 own outgoing join. T=pi+alpha_actor-alpha_source lies in[3pi/4,5pi/4]. Principal closing delta is strictly between-pi andpi for nonparallel tangents; Jordan winding therefore must be positive and requires T>pi. All eight remaining positive poses have a genuine deleted external input, with at least one decisive read in the actor RAW.',
'Signed cb606 supplies the S BASE deleted-port obstruction. For sourceC1, zero-E C2 writes below the holes; nonempty E cannot begin U by actual CU, and firstD/V R support is at/below its head before its y drop. Later U and C2 also remain below. The same genuine N external-export argument applies; no N physical-WHITE, V-cohort or U-star invariant is imported.',
'Q target uses actual corrected centers start(-7,-7), final(-11,-3). If S is empty the COMPOUND final x is startx+E_delta_x+N_delta_x+2, not a claim that intermediate C1 never goes left. If S is nonempty, N starts below its terminal and at x=terminalx+E_delta_x. At terminal y it is at/right of S; at initial y it is left because N x is nondecreasing up to the northwest final point. The exact graph intermediate-value argument forces contact, with bottom equality assigned to outgoingC1. Thus the completed targetC3 cannot occur.',
'Prepared DCCC and VCCVC with their actual M are independently legal and have simple selected proxies. In particular the argument does not assume the first V entire output cohort survives. Nominal target path fails actual external U input at221 versus sourceL133. No partial C3-R8 repair, arbitrary-tail G7 simplicity, FOREIGN crossing, ancestry, age or capture conclusion follows.'
])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
