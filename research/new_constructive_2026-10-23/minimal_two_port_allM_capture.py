#!/usr/bin/env python3
"""Canonical minimal two-port family: fixed55531 response then NW104, all M>=1.
The all-M transfer is the exact low-halfplane history identity, not samples.
"""
from pathlib import Path
import json,hashlib,sys
P=Path('/workspace/shared/langton');O=Path(__file__).parent
J=json.loads((P/'causal_reduction/unit_scale/prepared4352_capture_manifest.json').read_text());C=(O/'minimal_two_port_fixed_continuation.word.txt').read_text();H=json.loads((O/'minimal_two_port_M1_exact_tail.json').read_text())['tail_word'];V=((0,1),(1,0),(0,-1),(-1,0));W=J['stages'][11]['word'];T=J['stages'][12]['word'];R=J['stages'][13]['word'];Z=J['stages'][14]['word'][:17395]
sys.path.insert(0,str(P/'computability'));from periodic_tail_checker import first_mismatch,State,plan

def trace(w,p,h):
 rows=[];p0=p;h0=h
 for c in w:
  rows.append((p,h,c));h=(h+(-1 if c=='L'else 1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1]
 return rows,p,h

def hull(w,p,h):
 rows,q,hh=trace(w,p,h);us=[sum(z[0])for z in rows];return min(us),max(us),q,hh

# These literal one-stage extrema are the only all-M support ingredients.
wlo,whi,q,hh=hull(W,(-2,3),3);assert wlo==1 and(q,hh)==((24,29),3)
tlo,thi,q,hh=hull(T,(180,185),3);assert tlo==338 and(q,hh)==((195,189),0)
rlo,rhi,q,hh=hull(R,(195,189),0);assert rlo==182 and(q,hh)==((117,111),0)
zlo,zhi,q,hh=hull(Z,(117,111),0);assert(q,hh)==((9,-10),3)
assert len(C)==55531
clo,chi,q,hh=hull(C,(9,-10),3);assert(clo,chi,q,hh)==(-21,208,(-2,26),0)
hlo,hhi,q,hh=hull(H,(-2,26),0);assert(hlo,hhi)==(17,27)and(q,hh)==((-4,28),0)

# Reconstruct one minimal seed from the EXPLICIT supplied word; no discovery.
body='RLL'+W*7+T+R+Z;rows,p,h=trace(body,(-2,2),0);seed=set();seen={};odd=set()
for i,(q,hh,c)in enumerate(rows):
 if q in seen:assert seen[q]!=c
 elif c=='L':seed.add(q)
 seen[q]=c;odd.symmetric_difference_update({q})
B=seed^odd;assert(p,h)==((9,-10),3)and{q for q in B if sum(q)<=0}=={(-2,2),(10,-10)}
for i,(q,hh,c)in enumerate(trace(C,p,h)[0]):
 assert(q in B)==(c=='L'),(i,q,c);B.symmetric_difference_update({q})
p,h=trace(C,p,h)[1:];s=State(frozenset(B),p,h);assert first_mismatch(s,H)is None

# True initial inverse-ten, not zero padding. Its reads remain in the common
# low halfplane, hence the same history works for every parameter M.
bb=set(seed);pp=(-2,2);hh=0;back=[];back_us=[]
for _ in range(10):
 v=V[hh];q=pp[0]-v[0],pp[1]-v[1];back_us.append(sum(q));c='R'if q in bb else'L';bb.symmetric_difference_update({q});hh=(hh-(1 if c=='R'else-1))%4;pp=q;back.append(c)
hist=''.join(reversed(back));std=json.loads((P/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];F={''.join(std[(i+j)%104]for j in range(10))for i in range(104)}
def cost(hist,w):
 bad0=hist not in F;n=0
 for c in w:
  hist=(hist+c)[-10:];bad=hist not in F;n+=bad and bad0;bad0=bad
 return hist,n
inverse_hist=hist;coef=0;const=0;hist,k=cost(hist,'RLL');rll_cost=k;const+=k;costs=[]
for name,w,a,b in [('W',W,3,4),('T',T,0,1),('R',R,1,0),('Z',Z,0,1),('C',C,0,1)]:
 if a:
  hist,k1=cost(hist,w);hs,ksteady=cost(hist,w);assert hs==hist
  coef+=a*ksteady;const+=k1+(b-1)*ksteady;costs.append({'name':name,'first':k1,'later':ksteady,'count_M_constant':[a,b]})
 else:
  hist,k=cost(hist,w*b);const+=k;costs.append({'name':name,'cost':k,'count':b})
_,tailcost=cost(hist,H[:10]);const+=tailcost
assert len(seed)==5925 and len(B)==14289
_,directK=cost(inverse_hist,body+C+H[:10]);assert directK==coef+const
out={'status':'AUTHOR all-M exact low-halfplane capture theorem','domain':'M>=1','initial_seed':'Minimal first-L seed of RLL W^(3M+4) T P^M Z; every other cell initially white.','M1_initial_mass':len(seed),'M1_capture_mass':len(B),'common_returned_field_halfplane':'u=x+y<=337','extra_W_min_u':1+52*7,'all_T_min_u_M_constant':[156,182],'extra_P_min_u':182+156,'fixed_Z_read_u_hull':[zlo,zhi],'post_exit_response_length':len(C),'response_read_u_hull':[clo,chi],'capture_time_M_constant':[28380,248488],'capture_pose':[p,h],'tail_period':104,'tail_drift':plan(s,H)[1],'tail_read_u_hull':[hlo,hhi],'initial_inverse_ten':''.join(reversed(back)),'inverse_read_u_hull':[min(back_us),max(back_us)],'total_actual_K_M_constant':[coef,const],'initial_RLL_K':rll_cost,'tail_seam_K':tailcost,'direct_M1_total_K':directK,'tail_word':H,'cost_ledger':costs,'finite_input_fuel_grows_with_M':True,'scope':__doc__,'response_word_sha256':hashlib.sha256(C.encode()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'minimal_two_port_allM_capture.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
