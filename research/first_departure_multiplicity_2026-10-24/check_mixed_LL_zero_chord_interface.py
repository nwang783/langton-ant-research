"""Complete mixed2/3/4 endpoint interface across a flow2 LL pair.
Fixed144 local histories; all exterior ports remain open, no period/front scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
base=Path(__file__).parent
ns={};exec((base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0],ns);check=ns['check'];out=ns['out']
local={};exec((base/'check_flow2_LL_reset_square.py').read_text().split('rows=[];bad=Counter()')[0],local);detail=local['check']
pos={'Z':(0,0),'A':(1,0),'B':(1,1),'Y':(0,1)}
counts=Counter();rows=[]
for z,a,b,y in product(['NSS','NNSS','NSSN'],['EEWW','EWWE','EWE','EWEW'],['SSNN','SNNS','SSS','SSSS'],['EWW','EEWW','EWWE']):
 hs=dict(Z=z,A=a,B=b,Y=y);ans=check({pos[u]:h for u,h in hs.items()});counts[ans]+=1
 if ans!='open':continue
 verdict,data=detail(hs);assert verdict=='open'
 chord=sum(out(a,i)=='N'for i in range(len(a)));assert chord==b.count('N')
 mixed=a in['EWE','EWEW']and b in['SSS','SSSS'];assert mixed==(chord==0)
 if mixed:assert z in['NSS','NNSS','NSSN']and y in['EWW','EEWW','EWWE']
 else:assert(hs in[dict(Z='NNSS',A='EEWW',B='SNNS',Y='EWW'),dict(Z='NNSS',A='EEWW',B='SNNS',Y='EWWE'),dict(Z='NNSS',A='EWWE',B='SNNS',Y='EEWW')])and chord==2
 critical_ok=z=='NNSS'
 start=None
 if y in['EWW','EWWE']and critical_ok:
  edges={(u,r):(v,s)for u,r,v,s,_,_ in data['edges']};route=[('Y',1),edges['Y',1]];route.append(edges[route[-1]])
  assert route[1]==('Z',3)and route[2]==('A',2 if mixed else 1)
  start=route
 rows.append(dict(histories=hs,zero_chord_mixed=mixed,missing_N_chord_flow=chord,critical_first_track_compatible=critical_ok,actual_LL_cut_prefix=start,**data))
assert dict(counts)=={'clock_cycle':12,'skipped_rank':21,'port':72,'open':39}
assert sum(r['zero_chord_mixed']for r in rows)==36
assert sum(r['critical_first_track_compatible']for r in rows)==15
obj=dict(scope=__doc__,all144_counts=dict(counts),necessary_open_rows=rows,unconditional_open_count=39,critical_additional_chronology_filter='Second LEFT Z cannot be a crossing O/U; use the separately proved actual-side chronology, not local port feasibility.',critical_remaining_count=15,warning='No open row is a full board factor, assigned global event orbit, complete front, proof of arbitrary repetition or fresh-fuel payment. The all-even zero-chord local mode does not contradict the retained global Nodd>0 theorem.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS144:39 open;36 zero-chord +3 flat; critical second-V filter leaves15')
