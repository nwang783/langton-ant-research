#!/usr/bin/env python3
"""Exact stream/voltage telescoping and an ACTUAL standard local sign control."""
from pathlib import Path
import json,hashlib,random
from collections import Counter
from check_extremal_read_coupling import event_word,quotient,front
R=Path(__file__).resolve().parent

def main():
 rng=random.Random(310124);controls=[]
 for t in range(-4,9,2):
  for _ in range(10):
   lo=-20;c=rng.randrange(-4,5);H={j:c for j in range(lo-4,lo+4)}
   for j in range(lo+4,t+5):H[j]=rng.randrange(-10,11)
   n=lambda j:H[j]-H[j+1]
   s=lambda j:H[j-2]-H[j-3]
   K=sum(n(j)for j in range(lo+1,t-2,2))-sum(s(j)for j in range(lo+1,t,2))
   assert K==c-H[t-2]
   w=H[t+1]-H[t-2];nn=H[t-1]-H[t];ss=H[t-1]-H[t-2];u=H[t+1]-H[t]
   assert w+nn==ss+u
   assert c-H[t]==K+nn-ss
   controls.append({'cut':t,'lower_exterior_height':c,'K':K,'L_face_height':H[t-2],'cut_counts_signed_algebra':[w,nn,ss,u]})
 p=R.parent/'recovered_bundle/ant_global/root/standard.json';s=json.loads(p.read_text());F=front(s['word'],s['heading']);assert F['complete_white'];E,d,_=event_word(s['word'],s['heading']);G={}
 for e in E:
  r,k=quotient(e['p'],d);G.setdefault(r,[]).append((e['t']-k*104,e))
 G={r:sorted(v)for r,v in G.items()};hp=(1,-1);vp=(0,-1);HH=G[hp];VV=G[vp]
 lam=sum(i%2==1 and e['hi']==3 for i,(time,e)in enumerate(HH));eta=sum(i%2==1 and e['hi']==0 for i,(time,e)in enumerate(VV));assert(lam,eta)==(3,2)
 assert ''.join('NESW'[e['hi']]for time,e in HH)=='WWEWWEEW';assert ''.join('NESW'[e['hi']]for time,e in VV)=='NSSSSNSN'
 out={'scope':__doc__,'stream_formulas':{'N_t':'h_t-h_(t+1)','S_t':'h_(t-2)-h_(t-3)','W_t':'h_(t+1)-h_(t-2)','E_t':'h_(t-3)-h_t','K_internal_even_cut':'c_right-h_(t-2)','K_next':'K+n-s','potential':'B=2K+w; B_next-B=4(eta-lambda)'},'algebra_controls':controls,'actual_standard_control':{'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'word':s['word'],'heading':s['heading'],'full_drift':d,'H_position':hp,'V_position':vp,'H_stable_complete_events':HH,'V_stable_complete_events':VV,'lambda_W_at_L':lam,'eta_N_at_L':eta,'warning':'Actual complete WHITE standard104, but NOT drift(3,1) or growth8. It refutes a universal LOCAL eta>=lambda inference only.'},'limits':'No global bound on K, monotonicity in the particular middle-short reachable family, or controller is established.'}
 (R/'drift31_voltage_stream_counter_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS70 telescoping controls; actual local eta-lambda=-1')
if __name__=='__main__':main()
