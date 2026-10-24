#!/usr/bin/env python3
"""Exact masks for the all-cap clean backreflection profile-growth lemma.
No cap search, new channel enumeration, horizon escalation or infinite itinerary.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib,runpy
P=Path('/workspace/shared/langton');G=P/'nonlinear_global_budget_2026-10-23';OUT=Path(__file__).parent
D=((0,1),(1,0),(0,-1),(-1,0));J=json.loads((P/'recovered_bundle/ant_global/root/standard.json').read_text());H=J['word']
def profile(q):return(q[0]-q[1],q[0]%2)
def trace(w,p,h):
 rows=[];p0=p;h0=h
 for i,c in enumerate(w):
  rows.append((p,i,c));h=(h+(-1 if c=='L'else 1))%4;v=D[h];p=(p[0]+v[0],p[1]+v[1])
 return rows,p,h

def signature(w,p,h):
 rows,q,hh=trace(w,p,h);f=(q[0]-p[0],q[1]-p[1]);assert f in[(-2,-2),(2,2)]and hh==h
 groups=defaultdict(list)
 for q,i,c in rows:
  a=q[0]%2;groups[profile(q)].append(((q[0]-a)//f[0],i,c))
 for g in groups.values():g.sort(key=lambda a:(-a[0],a[1]));assert all(a[2]!=b[2]for a,b in zip(g,g[1:]))
 first={j:g[0][2]for j,g in groups.items()};odd={j for j,g in groups.items()if len(g)%2}
 assert len(first)==22 and set(first.values())=={'R'} and len(odd)==12
 return set(first),odd

# Every physical phase, both opposite diagonal orientations. No unexplained
# phase-zero convention is used for the complete read or odd wake profiles.
rows,q,hh=trace(H,(0,0),J['heading']);controls=[]
for halfturn in[0,1]:
 for phase,(p,_,c)in enumerate(rows):
  _,pp,hp=trace(H[:phase],(0,0),J['heading'])
  if halfturn:pp=(-pp[0],-pp[1]);hp=(hp+2)%4
  R,W=signature(H[phase:]+H[:phase],pp,hp)
  controls.append({'halfturn':halfturn,'phase':phase,'read_classes':len(R),'odd_wake_classes':len(W),'first_R_classes':len(R)})

# Replay only TWO already-certified reactions, without enumerating channels.
# The substrate/cap is kept whole through each exact finite oracle replay.
E=runpy.run_path(str(G/'changed_endpoint_catalog.py'))
original=json.loads((G/'endpoint_catalog_results.json').read_text())['results'];changed=json.loads((G/'changed_endpoint_catalog_results.json').read_text())['cap_results']
cycle=[]
final_caps=[]
for source_channel,target_channel in[([-12,0],[26,0]),([26,0],[-12,0])]:
 source=next(r for r in original if r['channel']==source_channel)
 substrate,cap,meta=E['normalized_endcap'](source);P0=set(substrate);assert len(P0)==48
 node=next(r for r in changed if r['normalization']['source_channel']==source_channel)
 result=next(r for r in node['results']if r['channel']==target_channel);assert result['drift']==[2,2]
 rr,F,p,h,tau,phi=E['incoming'](substrate,cap,target_channel)
 after_in={j for j,v in rr.items()if len(v)%2};I=after_in^P0;assert len(I)==12 and I.isdisjoint(P0)
 p,h,read=E['advance'](rr,F,p,h,result['entry']);assert [list(p),h]==result['pose']
 assert E['certify'](rr,F,p,h,result['tail_word'])
 R,O=signature(result['tail_word'],p,h)
 assert R.isdisjoint(after_in)and len(O)==12
 rcopy={j:set(v)for j,v in rr.items()};srows,_,_=trace(result['tail_word'],p,h)
 for q,_,c in srows:
  j,k=E['old_orbit'](q);E['add_threshold'](rcopy,j,k)
 final={j for j,v in rcopy.items()if len(v)%2}
 assert final==P0|I|O and len(final)==72
 canonical_cap=set(F)
 for (tt,aa),thresholds in rcopy.items():
  ts=set(thresholds)
  if len(ts)%2:E['toggle'](ts,0)
  assert len(ts)%2==0
  ts=sorted(ts)
  for lo,hi in zip(ts[::2],ts[1::2]):
   for kk in range(lo+1,hi+1):E['toggle'](canonical_cap,(aa-2*kk,aa-2*kk-tt))
 final_caps.append(canonical_cap)
 # Both former candidate arrivals are now blocked at infinity by their own
 # incoming wake. Finite cap changes cannot restore clean compatibility.
 blocked=[]
 for ch in[[-12,0],[26,0]]:
  delta,a=ch;Rin={(t+delta,(b+a)%2)for t,b in E['RORB']};hits=Rin&final
  assert len(hits)>=12
  blocked.append({'channel':ch,'black_read_classes':sorted(hits),'count':len(hits)})
 cycle.append({'source':source_channel,'second_channel':target_channel,'profile_counts':[len(P0),len(after_in),len(final)],'incoming_new_classes':sorted(I),'outgoing_new_classes':sorted(O),'complete_final_profiles':sorted(final),'both_former_channels_unclean':blocked,'final_normalized_cap_mass':len(canonical_cap),'final_normalized_cap_sha256':hashlib.sha256(json.dumps(sorted(canonical_cap),separators=(',',':')).encode()).hexdigest(),'fixed_second_reaction_length':result['entry'],'fixed_second_reaction_K':result['K_total']})
assert cycle[0]['complete_final_profiles']==cycle[1]['complete_final_profiles']
cap_xor=final_caps[0]^final_caps[1]
report={'status':'PASS exact standard masks and two existing full-field compositions','scope':__doc__,'standard_physical_phase_controls':len(controls),'universal_standard_read_classes':22,'universal_first_R_classes':22,'universal_odd_wake_classes':12,'two_existing_compositions':cycle,'two_order_complete_field_difference':{'mature_profiles_identical':True,'finite_cap_xor_mass':len(cap_xor),'finite_cap_xor':sorted(cap_xor)},'generality':'The all-cap +24 law is analytic in the companion note; controls check the literal104 ingredients, not arbitrary-cap convergence or existence of a finite original sequence.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'clean_backreflection_profile_growth.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k!='two_existing_compositions'},indent=2));print('Both fixed compositions:48 ->60 ->72; same final mature profile; formerchannels both blocked.')
