#!/usr/bin/env python3
"""Complete finite conditional single-used F-circle cover, d=(3,1), g8.
Higher traffic remains unbounded; signed charge bounds circle length, not period.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json,hashlib
from partial_drift31_graph import D,quotient31,graph
from certify_drift31_read_minimum import words,returns_to,depart
ROOT=Path(__file__).resolve().parent

def trace(dirs):
 p=(0,0);pts=[]
 for h in dirs:pts.append(p);p=(p[0]+D[h][0],p[1]+D[h][1])
 assert p==(-3,-1)
 return pts,[3*y-x for x,y in pts]

def mismatch(hist):
 for t,hs in sorted(hist.items()):
  p=(-t,0)
  for ho in range(4):
   src=depart(hs,ho);q,k=quotient31((p[0]+D[ho][0],p[1]+D[ho][1]));u=-q[0]
   if u not in hist:continue
   dst=[j for j,h in enumerate(hist[u])if h==ho]
   if len(src)!=len(dst):return{'source_level':t,'target_level':u,'heading':ho,'voltage':k,'source_complete_ranks':src,'target_complete_ranks':dst}
 return None

def main():
 cases=[];outcomes=Counter();canonical=set()
 for m in(3,5,7):
  for xaxis in(0,1):
   xs=[i for i in range(2*m)if i%2==xaxis];ys=[i for i in range(2*m)if i not in xs]
   for Es in combinations(xs,(m-3)//2):
    for Ns in combinations(ys,(m-1)//2):
     E=set(Es);N=set(Ns);dirs=tuple((1 if i in E else 3)if i in xs else(0 if i in N else 2)for i in range(2*m));pts,levels=trace(dirs);seen={};duplicate=None
     for j,t in enumerate(levels):
      if t in seen:duplicate=[seen[t],j];break
      seen[t]=j
     z={'directions':dirs,'points':pts,'levels':levels}
     if duplicate is not None:z.update(outcome='repeated_full_class',witness_indices=duplicate);outcomes[2*m,'repeated']+=1
     else:
      j=min(range(2*m),key=lambda i:levels[i]);normalized=dirs[j:]+dirs[:j];canonical.add(normalized);z.update(outcome='simple_cycle',minimum_start_index=j,canonical_directions=normalized);outcomes[2*m,'simple']+=1
     cases.append(z)
 assert len(cases)==1576 and canonical=={(3,0,3,2,3,2)}
 dirs=next(iter(canonical));pts,levels=trace(dirs);turns=[(h-dirs[j-1])%4 for j,h in enumerate(dirs)];assert turns.count(1)==turns.count(3)==3;left=[levels[j]for j,r in enumerate(turns)if r==3];assert set(left)=={3,4,5}
 placements=[]
 for k in(2,3):
  for QQ in combinations(left,k):
   Q=set(QQ);hist={}
   for j,t in enumerate(levels):
    A=(dirs[j]-1)%4;hist[t]=(A,)if turns[j]==1 else(A,A,(A+2)%4)+((A,)if t in Q else())
   qx=[sum((-1)**t for t in Q if(-t)%3==r)for r in range(3)];qy=sum((-1)**t for t in Q);f=lambda x:min(x%4,(-x)%4);px=sum(f(2+x)for x in qx);py=f(2+qy);bound=6-k+max(px,py);assert bound<=8
   item={'quadruple_levels':sorted(Q),'complete_circle_histories':{str(t):hist[t]for t in sorted(hist)},'quadruple_signed_x_fibres':qx,'quadruple_signed_y_fibre':qy,'Phi_x':px,'Phi_y':py,'exact_charge_lower_bound':bound}
   bad=mismatch(hist)
   if bad:item.update(outcome='internal_port_mismatch',witness=bad)
   else:
    H=[hist[t]for t in range(6)];kind,G=graph(H,list(range(6)));assert kind=='open';item.update(outcome='OPEN_circle_interface',open_graph=G)
    rel,paths=returns_to(H,G,6);assert rel==[(0,1,4)]and all(p['outgoing_heading']==1 and p['incoming_heading']==0 for p in paths)
    I=3;J=hist[5].count(1);derived=2*(I+J)+1;domain=words(0,derived,0,I,1,J,rel);extended=[]
    for hs in domain:
     kk,gg=graph(H+[hs],list(range(7)));assert kk=='open';extended.append({'history':hs,'graph':gg})
    assert len(domain)==(7 if len(hist[5])==3 else 13)
    item['first_exterior_cell_T6']={'incoming_N':I,'outgoing_E':J,'derived_read_bound':derived,'actual_four_step_first_return':paths,'all_complete_domains':domain,'all_remain_OPEN':True,'extended_graphs':extended}
   placements.append(item)
 assert Counter(p['outcome']for p in placements)=={'internal_port_mismatch':2,'OPEN_circle_interface':2}
 result={'scope':__doc__,'full_drift':[3,1],'growth':8,'signed_charge_note_sha256':hashlib.sha256((ROOT/'SINGLE_USED_FIRST_CIRCLE_CORRECTED_CHARGE.md').read_bytes()).hexdigest(),'candidate_lengths':[6,10,14],'raw_paths':len(cases),'path_outcomes':{str(k):v for k,v in outcomes.items()},'all_geometric_cases':cases,'sole_canonical_geometry':{'directions':dirs,'points':pts,'levels':levels,'turns':turns},'all_quadruple_placements':placements,'limits':'Conditional on an actual SINGLE-USED F circle. No period/width/exterior cap. Two circle interfaces and20 next-cell obligations remain OPEN, not physical controllers.'}
 (ROOT/'drift31_single_used_g8_shapes_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print(result['path_outcomes']);print([(p['quadruple_levels'],p['outcome'])for p in placements])
if __name__=='__main__':main()
