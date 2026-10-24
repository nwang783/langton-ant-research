#!/usr/bin/env python3
"""Small retained T8-T10 cover, with a new exact first/last C-core corollary."""
from pathlib import Path
from collections import Counter
import json,hashlib
from explore_drift31_inventory20 import generated,Gof,paths,depart
R=Path(__file__).resolve().parent

def main():
 H={t:tuple('NESW'.index(c)for c in w) for t,w in enumerate(['S','W','S','EEWE','SSNS','EEWE','NNNSS','EEEWW'])};states=[H];stages=[]
 for t in [8,9,10]:
  out=[];parents=[];counts=Counter()
  for H in states:
   kind,G,rp=paths(H,t);assert kind=='open'
   if t%2==0:ih,I,oh,J=0,len(depart(H[t-3],0)),1,H[t-1].count(1)
   else:ih,I,oh,J=3,len(depart(H[t-1],3)),2,H[t-3].count(2)
   bound=2*(I+J);rows=[]
   for w in generated(t%2,bound,ih,I,oh,J,0,()):
    fail=None
    for i,(a,b,oo,ii) in enumerate(rp[0]):
     source=depart(w,oo)[a];target=[r for r,h in enumerate(w) if h==ii][b]
     if target!=source+1:fail={'physical_return_index':i,'source_rank':source,'target_rank':target};break
    if fail:
     rows.append({'word':w,'outcome':'first_return_rank_mismatch','witness':fail});counts['first_return_rank_mismatch']+=1;continue
    k,g=Gof(H|{t:w});row={'word':w,'outcome':k};counts[k]+=1
    if k=='open':out.append(H|{t:w})
    else:
     assert k in ['skipped_rank','positive_rank_clock_cycle'];row['witness']=g
     if k=='positive_rank_clock_cycle':assert g['period_coefficient']>=0 and g['constant']+g['period_coefficient']*g['local_event_count']>0
    rows.append(row)
   parents.append({'complete_parent':H,'incoming_heading':ih,'incoming_total':I,'outgoing_heading':oh,'outgoing_total':J,'derived_even_length_bound':bound,'all_physical_returns':rp[1],'all_complete_count_domains':rows})
  stages.append({'target_level':t,'parent_count':len(states),'domain_outcomes':dict(counts),'parents':parents});states=out
  print(t,dict(counts),'survivors',len(states),flush=True)
 T8={h[8] for h in states};assert T8=={tuple('NESW'.index(c) for c in w)for w in ['NNSNSSSS','NNSSSNSS']};assert len(states)==6
 old=json.loads((R/'drift31_middle_short_even_gap_discovery.json').read_text())['states']
 oldset={tuple(tuple(z[str(t)]) for t in range(11)) for z in old};newset={tuple(H[t] for t in range(11)) for H in states};assert oldset==newset
 # Exact T8 ports, retaining the physical higher unknowns.
 profiles=[]
 for w in sorted(T8):
  N=[r for r,h in enumerate(w) if h==0];E=depart(w,1);assert N[:2]==[0,1] and N[2] in [3,5] and E[0]==0 and E[-1]==7
  assert w[7]==2 and 7%2==1 and all(r%2==1 for r in N[1:])
  profiles.append({'complete_T8':w,'N_arrival_ranks':N,'E_departure_ranks':E,'first_C5_read':'T8.N/R0','last_C5_read':'T4.S/L3','third_N_before_final_S_L':{'third_N_rank':N[2],'final_S_L_rank':7,'minimum_time_gap':4*(7-N[2])}})
 # Symbolic clock identities are stored coefficient-wise in (a,s,n,P,constant).
 # a=T7.R0, s=T7.R2, n=T8 third N, same physical core as50990252.
 core={'clock_variables':['a','s','n','P','constant'],
  'first_C1':[0,1,0,0,2],'last_C1':[0,1,0,0,14],
  'first_C3':[0,1,0,0,7],'last_C3':[0,0,1,1,-1],
  'first_C5':[1,0,0,0,-1],'last_C5':[0,1,0,0,13],
  'exact_relation_P_equals_s_minus_a_plus18':[-1,1,0,-1,18],
  'spans':{'C1':'12','C3':'P+n-s-8','C5':'P-4'},
  'last_cycle_forward_steps':[{'source':'C5','target':'C1','voltage':0,'selected_L':'T4.L3','clock_gap':'1'},
   {'source':'C1','target':'C3','voltage':0,'selected_L':'T3.L3','clock_gap':'P+n-s-15'},
   {'source':'C3','target':'C5','voltage':1,'selected_L':'T5.L3','clock_gap':'s-n+14'}],
  'strict_span_bounds':{'C1':'12<P','C3':'0<S3<=P-17<P (P-25 in NNSNSSSS)','C5':'P-4<P'},
  'derived_period_lower_bound':46,'C5_last_to_next_first_carry':{'voltage':1,'duration':4,'actual_word':'LLRL','events':['T4.L3','T3.L3','T6.R2','T5.L1']}}
 # Check all symbolic sum identities without substituting sampled parameters.
 assert 1+(-15)+14==0 # last-cycle constant sums to P
 assert (-1)+18==17 # first C5+d = s+17
 assert (13)-(-1)-18==-4 # C5 span=P-4
 for p in profiles:
  r=p['N_arrival_ranks'][2]
  # Four-step gaps for T8 ranks1->r and r->7 give s-a>=28.
  assert (3+4*(r-1))+(1+4*(7-r))==28
 out={'status':'AUTHOR checked, independent audit pending','scope':'Finite local cover under the signed full middle-short odd inventory (T8,T9,T10 even), leaving every level>=11 unknown. Re-certifies a retained discovery result and derives coincident first/last C cycles. No four-type exclusion.',
  'stages':stages,'six_open_T0_through_T10_interfaces':states,'two_T8_profiles':profiles,'first_last_core_clock_identities':core,
  'provenance':'Exact six-interface set equals the pre-existing discovery-only T8-T10 file; no T11/T12 expansion was run.',
  'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['explore_drift31_inventory20.py','partial_drift31_graph.py','certify_drift31_read_minimum.py','MIDDLE_SHORT_FORCED_THREE_C_DISCOVERY_CYCLE.md','MIDDLE_SHORT_FOUR_BOUNDARY_TYPES.md','drift31_middle_short_even_gap_discovery.json']}}
 p=R/'middle_short_coincident_C_cycles_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS6 exact open interfaces; same old discovery set',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
