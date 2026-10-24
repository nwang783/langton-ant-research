#!/usr/bin/env python3
"""One complete proposed112-event full-drift inventory, not a claimed controller."""
import json
from pathlib import Path
from check_extremal_read_coupling import quotient,D
DRIFT=(2,-2)

def main():
 z=json.load(open('check_single_used_first_circle.json'));H={}
 hs=['W','','N','SS','WE','WWE','SNNS','SSNS','EEE','WWEEWW']
 for i,w in enumerate(hs):
  t=i//2-1;r=i%2;H[r,t-r]=tuple('NESW'.index(x)for x in w)
 for q in z['all_standard_stable_histories']:
  p=tuple(q['point'])
  if sum(p)<2:continue
  r,k=quotient((p[0]+1,p[1]+1),DRIFT);assert r not in H;H[r]=tuple('NESW'.index(x)for x in q['headings'])
 ps=sorted(H,key=lambda p:(sum(p),p[0]));ix={p:i for i,p in enumerate(ps)};hist=[H[p]for p in ps];out={};bad=[]
 for p,i in ix.items():
  for h in range(4):
   src=[j for j,x in enumerate(hist[i])if(x+(1 if j%2==0 else-1))%4==h]
   if not src:continue
   q,k=quotient((p[0]+D[h][0],p[1]+D[h][1]),DRIFT);ii=ix.get(q);dst=[]if ii is None else[j for j,x in enumerate(hist[ii])if x==h]
   if len(src)!=len(dst):bad.append({'source':p,'heading':h,'src':src,'target':q,'dst':dst});continue
   for a,b in zip(src,dst):out[i,a]=((ii,b),k)
 P=sum(map(len,hist));assert P==112 and sum(len(h)%2 for h in hist)==12
 assert not bad,bad
 nodes=[(i,j)for i,h in enumerate(hist)for j in range(len(h))];assert len(out)==len(nodes)and len({v[0]for v in out.values()})==len(nodes)
 seen=set();cycles=[]
 for start in nodes:
  if start in seen:continue
  at=start;k=0;seq=[]
  while at not in seen:
   seen.add(at);seq.append({'cell':ps[at[0]],'rank':at[1],'lift':k});at,dk=out[at];k+=dk
  assert at==start;cycles.append({'events':seq,'length':len(seq),'winding':k})
 result={'period_inventory':P,'growth':12,'full_drift':DRIFT,'normal_read_height':13,'complete_named_histories':{str(p):''.join('NESW'[x]for x in H[p])for p in ps},'full_port_count_mismatches':bad,'full_event_cycles':cycles,'status':'PENDING_CHRONOLOGY'if len(cycles)==1 and cycles[0]['winding']==1 else'REJECTED_FULL_EVENT_PERMUTATION'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print({'period':P,'cycle_lengths_windings':[(c['length'],c['winding'])for c in cycles],'status':result['status']})
if __name__=='__main__':main()
