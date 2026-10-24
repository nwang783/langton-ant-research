#!/usr/bin/env python3
"""Exact terminal-excursion decomposition, not an output budget."""
from pathlib import Path
from collections import Counter
import json,hashlib
from check_extremal_read_coupling import event_word,D
from certify_exit_component_turn_flux import analyze
R=Path(__file__).resolve().parent

def build(w,h=0):
 a=analyze(w,h);E,d,_=event_word(w,h=h);P=len(w)
 lab={e['t']:x['component']for x in a['all_complete_read_histories']for e in x['events']}
 def pos(t):
  k,i=divmod(t,P);p=E[i]['p'];return(p[0]+k*d[0],p[1]+k*d[1])
 out=[]
 for c in a['components']:
  edges=c['selected_last_edges'];start=edges[0]['last_source_phase'];t=start;rows=[]
  for e in edges:
   assert t%P==e['last_source_phase'];gap=e['selected_edge_last_clock_gap'];end=t+gap;n=gap-1
   assert n%4==0 and pos(t+1)==pos(end)
   same=[j for j in range(t+1,end+1)if pos(j)==pos(end)]
   parts=[]
   for u,v in zip(same,same[1:]):
    ww=''.join(w[j%P]for j in range(u,v));parts.append({'start':u,'end':v,'length':v-u,'word':ww,'charge':ww.count('R')-ww.count('L'),'incoming_heading':E[u%P]['hi'],'return_heading':E[v%P]['hi'],'component_event_counts':dict(Counter(lab[j%P]for j in range(u,v)))})
   ww=''.join(w[j%P]for j in range(t+1,end));charge=ww.count('R')-ww.count('L')
   assert sum(x['length']for x in parts)==n and sum(x['charge']for x in parts)==charge
   rows.append({'selected_edge':e,'selected_source_time':t,'target_arrival_time':t+1,'target_last_time':end,'terminal_word':ww,'length':n,'charge':charge,'target_position':pos(end),'component_event_counts':dict(Counter(lab[j%P]for j in range(t+1,end))),'consecutive_same_physical_cell_returns':parts})
   t=end
  assert t==start+P
  selected=sum(1 if w[e['last_source_phase']]=='R'else-1 for e in edges)
  assert sum(x['length']+1 for x in rows)==P and selected+sum(x['charge']for x in rows)==w.count('R')-w.count('L')
  out.append({'basin':c['component_id'],'O':c['O'],'I':c['I'],'spine':c['last_spine'],'period_interval':[start,start+P],'selected_actual_turn_charge':selected,'effective_spine_turn_charge':sum(x['effective_quarter_turn']for x in c['effective_spine_turn_details']),'terminal_excursions':rows})
 return {'period':P,'drift':d,'word':w,'heading':h,'spine_partitions':out}

def main():
 src=json.loads((R/'exit_component_turn_flux_certificate.json').read_text())['base_controls'];base={n:build(a['word'])for n,a in src.items()}
 S=base['S104'];c=next(c for c in S['spine_partitions']if c['O']==4);long=next(x for x in c['terminal_excursions']if x['length']==96);ps=long['consecutive_same_physical_cell_returns']
 assert[(p['length'],p['charge'])for p in ps]==[(8,-2),(76,8),(8,0),(4,4)]
 assert ps[0]['word']=='LRLLLLRR'and ps[2]['word']=='LLRRRRLL'
 assert long['component_event_counts']=={0:86,1:10}and ps[0]['component_event_counts']=={1:1,0:7}
 controls=[]
 for name,a in src.items():
  for h in range(4):
   z=build(a['word'],h);assert[(c['O'],c['I'],[(e['length'],e['charge'])for e in c['terminal_excursions']])for c in z['spine_partitions']]==[(c['O'],c['I'],[(e['length'],e['charge'])for e in c['terminal_excursions']])for c in base[name]['spine_partitions']]
   controls.append({'name':name,'heading':h,'partitions':len(z['spine_partitions'])})
 frame=10289;cuts=[frame+31,frame+39,frame+115,frame+123,frame+127];B={};p=(0,0);h=0;states={};E=[]
 for t in range(cuts[-1]+1):
  if t in cuts:states[t]={'time':t,'head':p,'heading':h,'full_BLACK':sorted(B)}
  if t==cuts[-1]:break
  ch='L'if p in B else'R';e={'time':t,'position':p,'heading':h,'turn':ch}
  if ch=='L':e['R_owner']=B.pop(p)
  else:B[p]=t
  E.append(e);h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 assert ''.join(e['turn']for e in E[frame:frame+104])==S['word']
 assert ''.join(e['turn']for e in E[cuts[0]:cuts[1]])=='LRLLLLRR'
 assert len(states[cuts[1]]['full_BLACK'])-len(states[cuts[0]]['full_BLACK'])==-2
 assert all(E[t]['position']!=E[cuts[0]]['position']for t in range(cuts[0]+1,cuts[1]))
 literal={'frame':frame,'all96_terminal_reads':E[cuts[0]:cuts[-1]],'full_fields':states,'negative_first_return':E[cuts[0]:cuts[1]],'neutral_later_first_return':E[cuts[2]:cuts[3]],'dependency_full_infinite_front':'exit_component_turn_flux_certificate.json'}
 deps=['PHYSICAL_EXIT_COMPONENT_COLOR_TURN_AND_BOUNDARY_FLUX.md','exit_component_turn_flux_certificate.json','../global_attraction_bridge_2026-10-24/PRIMITIVE_SPINE_CLOCK_MANIFEST.json','../audits/check_exit_component_flux_independent.json']
 out={'scope':'Every selected physical last spine gives one partition of the ENTIRE actual period into selected departures and terminal closed-position excursions. No per-basin assignment, positivity, input budget or classification. Standard has an actual negative elementary first return on a last-spine root.','base_controls':base,'all20_rotations':controls,'literal_standard':literal,'dependencies':{s:hashlib.sha256((R/s).read_bytes()).hexdigest()for s in deps}}
 path=R/'physical_last_spine_excursions_certificate.json';path.write_text(json.dumps(out,indent=2)+'\n')
 print('PASS author',hashlib.sha256(path.read_bytes()).hexdigest(),'negative field sizes',len(states[cuts[0]]['full_BLACK']),len(states[cuts[1]]['full_BLACK']))
if __name__=='__main__':main()
