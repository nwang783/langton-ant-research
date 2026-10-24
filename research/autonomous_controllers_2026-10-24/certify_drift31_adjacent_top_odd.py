#!/usr/bin/env python3
"""All-cap exact four-return obstruction below adjacent top odd classes."""
import json,hashlib
from pathlib import Path
from certify_drift31_read_minimum import words,depart,returns_to
from partial_drift31_graph import graph
ROOT=Path(__file__).resolve().parent

def main():
 H={20:(0,),21:(),22:(),23:()};steps=[]
 for t,ih,oh,parity in [(19,1,0,1),(18,2,3,0),(17,1,0,0)]:
  I=len(depart(H[t+(1 if t%2 else 3)],ih));J=H[t+(3 if t%2 else 1)].count(oh)
  dd=[w for w in words(t%2,2*(I+J)+1,ih,I,oh,J)if len(w)%2==parity]
  assert len(dd)==1;steps.append({'level':t,'incoming_heading_count':[ih,I],'outgoing_heading_count':[oh,J],'parity':parity,'domain':dd});H[t]=dd[0]
 assert H[19]==(1,)and H[18]==()and H[17]==(3,3)
 levels=sorted(H);kind,G=graph([H[t]for t in levels],levels);assert kind=='open'
 rel,pp=returns_to([H[t]for t in levels],G,16);assert rel==[(0,0,4)]
 p=pp[0];assert p['outgoing_heading']==3 and p['incoming_heading']==2
 I=len(depart(H[19],2));J=H[17].count(3);assert(I,J)==(1,2)
 allwords=words(0,2*(I+J)+1,2,I,3,J)
 even=[h for h in allwords if len(h)%2==0];assert len(even)==4
 rows=[]
 for h in even:
  si=h.index(2);wi=depart(h,3)[0];assert si!=wi+1
  rows.append({'word':h,'first_S_rank':si,'first_W_departure_rank':wi,'required_equation':'first_S_rank = first_W_departure_rank + 1','failed':True})
 odd_ok=[h for h in allwords if len(h)%2==1 and h.index(2)==depart(h,3)[0]+1]
 assert odd_ok==[(0,0,2)]
 # Literal physical four-step return, without an intermediate read atQ.
 seq=[{'level':16,'event':'first W departure','point':[-16,0]}]
 for((i,j),v)in p['lower_chain']:
  t=levels[i];seq.append({'level':t,'rank':j,'lift':v,'point':[-t+3*v,v]})
 seq.append({'level':16,'event':'first S arrival','point':[-16,0]})
 assert [r['point']for r in seq]==[[-16,0],[-17,0],[-17,1],[-16,1],[-16,0]]
 result={'scope':__doc__,'full_drift':[3,1],'normalization':'actual maximum M=20; V incoming at even T','hypotheses':'M-1 odd; M-2 and M-3 even. M-4 must be odd. No other lower parity or traffic assumption.','upper_propagation':steps,'complete_upper_histories':{str(t):h for t,h in H.items()},'same_physical_four_return':p,'physical_path':seq,'Q_incoming_S_outgoing_W':[I,J],'derived_bound':7,'all_even_complete_histories':rows,'odd_histories_passing_this_one_return':odd_ok,'warning':'The NNS odd control is only a locally allowed complete-history interface, not an actual finite factor or front.','dependency_hashes':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest()for f in ['DRIFT31_TWO_QUAD_EXTREME_READ_EXCLUSIONS.md','certify_drift31_read_minimum.py','partial_drift31_graph.py']}}
 (ROOT/'drift31_adjacent_top_odd_certificate.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS: four even words fail; sole local odd control NNS')
if __name__=='__main__':main()
