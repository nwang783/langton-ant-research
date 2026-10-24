#!/usr/bin/env python3
"""One supplied all-quad short-mode O16 inventory, exact two-ended cover."""
import json,hashlib
from pathlib import Path
from collections import Counter
import certify_drift31_inventory20 as m
from partial_drift31_graph import quotient31,D
ROOT=Path(__file__).resolve().parent

def mismatch(H):
 for t,h in sorted(H.items()):
  for ho,(dx,dy)in enumerate(D):
   q,k=quotient31((-t+dx,dy));tt=-q[0]
   if tt not in H:continue
   A=m.depart(h,ho);B=[j for j,z in enumerate(H[tt])if z==ho]
   if len(A)!=len(B):return{'source_level':t,'target_level':tt,'heading':ho,'full_drift_voltage':k,'source_departure_ranks':A,'target_arrival_ranks':B}
 return None

def main():
 m.ODD={0,1,2,6,7,13,14,16};m.PROOF.clear();m.COUNTS.clear()
 src=json.loads((ROOT/'drift31_circle_middle_reads_certificate.json').read_text());s=next(s for s in src['eight_OPEN_interfaces']if len(s['T5'])==4 and len(s['T6'])==5 and len(s['T7'])==5)
 B=[{t:tuple(h)for t,h in enumerate(s['complete_named_histories'])}|{t:()for t in[-3,-2,-1]}];T=[{16:(0,),17:(),18:(),19:()}]
 for t in [15,14,13,12,11]:T=m.expand(T,t,'top')
 for t in [8,9]:B=m.expand(B,t,'bottom')
 assert len(T)==8 and len(B)==16
 joins=[];C=Counter()
 for bi,b in enumerate(B):
  for ti,t in enumerate(T):
   H=b|t;w=mismatch(H)
   if w:k='physical_port_count_mismatch'
   else:k,w=m.GG(H)
   assert k!='open'
   if k=='closed_component':assert w['winding']<=0 or w['other_local_events']>0
   joins.append({'bottom_id':bi,'top_id':ti,'outcome':k,'witness':w});C[k]+=1
 assert C=={'physical_port_count_mismatch':108,'skipped_rank':10,'closed_component':6,'positive_rank_clock_cycle':4}
 result={'scope':__doc__,'full_odd_inventory':sorted(m.ODD),'short_prefix':{str(t):h for t,h in enumerate(s['complete_named_histories'])},'complete_read_extrema':[0,16],'proof_records':m.PROOF,'local_counts':dict(m.COUNTS),'bottom_interfaces':[m.fmt(H)for H in B],'top_interfaces':[m.fmt(H)for H in T],'all128_joins':joins,'join_counts':dict(C),'unknown_middle_level':10,'dependency_hashes':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest()for f in ['certify_drift31_inventory20.py','drift31_circle_middle_reads_certificate.json','DRIFT31_TWO_QUAD_EXTREME_READ_EXCLUSIONS.md','partial_drift31_graph.py','certify_drift31_read_minimum.py']},'warning':'This exact inventory with the supplied short mode only. No wider family exclusion, new controller or opaque UNSAT result.'}
 (ROOT/'drift31_short_inventory16_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print(dict(C))
if __name__=='__main__':main()
