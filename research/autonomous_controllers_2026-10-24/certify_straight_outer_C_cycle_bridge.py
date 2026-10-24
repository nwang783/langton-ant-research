#!/usr/bin/env python3
"""Conditional unread-outer-C-row bridge, no arbitrary visit cap."""
from pathlib import Path
import json,hashlib
from certify_active_C_entry_exit_forests import analyze
from check_extremal_read_coupling import quotient,cycles
from check_all_cut_wave_interfaces import WORDS
R=Path(__file__).resolve().parent

def check(a):
 d=tuple(a['drift']);assert d[0]<0 and d[1]==-d[0];m=d[1];H={tuple(z['class']):z['reads']for z in a['read_histories']};F={tuple(z['source']):z for z in a['first_entry_edges']};active={tuple(x['class'])for x in a['C_face_histories']};out=[]
 for cy in a['WHITE_first_entry_cycles']:
  vs=list(map(tuple,cy['vertices']));levels={sum(v)for v in vs};assert len(levels)==1 and len(vs)==m
  level=next(iter(levels));outer=not any(sum(q)==level+2 for q in active);item={'C_vertices':vs,'level':level,'outer_row_unvisited':outer,'outer_row_active_classes':[q for q in sorted(active)if sum(q)==level+2]}
  if outer:
   assert all(sum(q)<=level for q in active)
   G={};rows=[]
   for v in vs:
    e=F[v];p=tuple(e['read_class']);rs=H[p];assert rs[0]['hi']==rs[1]['hi']==0
    q,k=quotient((p[0]+1,p[1]),d);qs=H[q]
    assert len(qs)==1 and qs[0]['c']=='R'and qs[0]['hi']==1
    word=''.join('NESW'[x['hi']]for x in rs);assert word in['NNS','NNSN']
    assert sum(x['c']=='R'and x['hi']==0 for x in rs)==1 and sum(x['c']=='R'and x['hi']==2 for x in rs)==1
    assert not any(x['c']=='L'and x['hi']==2 for x in rs)
    assert sum(x['ho']==1 for x in rs)==1
    G[p]=(q,k);r,l=quotient((q[0],q[1]-1),d);G[q]=(r,l)
    rows.append({'cycle_cell':p,'complete_history':rs,'outer_corner':q,'complete_corner_history':qs,'first_edge_voltage':k,'second_edge_voltage':l})
   cc=cycles(G);assert len(G)==2*m and len(cc)==1 and len(cc[0]['cells'])==2*m and cc[0]['winding']==-1
   item.update({'complete_boundary_rows':rows,'actual_single_used_F_circle':cc[0]})
  else:
   item['selected_read_histories']=[{'class':F[v]['read_class'],'heading_word':''.join('NESW'[e['hi']]for e in H[tuple(F[v]['read_class'])])}for v in vs]
  out.append(item)
 return out

def main():
 tests=[]
 for name,w,h in [('standard',WORDS['S104'],0),('prepared10','RRRRLLLLRL',3)]:
  for power in[1,2,3,5]:
   a=analyze(w*power,h);z=check(a);tests.append({'name':name,'power':power,'word':w*power,'heading':h,'full_drift':a['drift'],'input_count':a['input_count'],'cycles':z})
 assert tests[0]['cycles'][0]['outer_row_unvisited']and not tests[0]['cycles'][1]['outer_row_unvisited']
 assert [x['heading_word']for x in tests[0]['cycles'][1]['selected_read_histories']]==['NNSNSSN','NNSNNSSN']
 assert tests[4]['input_count']==1 and tests[4]['cycles'][0]['outer_row_unvisited']
 out={'status':'AUTHOR conditional all-cap exterior bridge; independent audit pending','scope':'An actually unvisited outer C row is a hypothesis, not a consequence of maximum stream height. It yields a single-used F circle but no finite interior excursion alphabet. Prepared10 retains its BLACK input.',
  'all8_controls':tests,'dependencies':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in[R/'ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md',R/'C_CYCLE_EXCURSIONS_AND_STANDARD_SELF_FEEDING.md',R/'C_STREAM_SIGNED_ENERGY_AND_OWNED_EXCURSION_FUEL.md']}}
 p=R/'straight_outer_C_cycle_bridge_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS outer standard3/4 and prepared10; inner standard7/8 retained outside hypothesis');print(hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
