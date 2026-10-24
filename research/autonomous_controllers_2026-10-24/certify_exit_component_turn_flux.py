#!/usr/bin/env python3
"""Exact physical last-departure component color/turn/boundary accounting.
No componentwise positivity, output budget, or controller classification.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib,sys
from check_extremal_read_coupling import event_word,quotient,D,cycles
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'computability'))
from periodic_tail_checker import first_mismatch
from check_rigid_reachability import State

def analyze(w,h0=0):
 E,d,h=event_word(w,h=h0);P=len(w);assert h==h0 and d!=(0,0)
 H=defaultdict(list);rep={};lift={};rank={}
 for e in E:
  q,k=quotient(e['p'],d);H[q].append((e['t']-P*k,e));rep[e['t']]=q;lift[e['t']]=k
 for q,es in H.items():
  es.sort(key=lambda a:a[0]);assert all(e['c']!=f['c']for (_,e),(_,f)in zip(es,es[1:]))
  for j,(_,e)in enumerate(es):rank[e['t']]=j
 G={};last_edges={}
 for q,es in H.items():
  lam,e=es[-1];u,k=quotient((q[0]+D[e['ho']][0],q[1]+D[e['ho']][1]),d);G[q]=(u,k)
  gap=H[u][-1][0]+k*P-lam;assert gap>=1
  nxt=E[(e['t']+1)%P];assert rep[nxt['t']]==u
  last_edges[q]={'source':q,'target':u,'voltage':k,'last_source_phase':e['t'],'last_source_turn':e['c'],
   'departure_heading':e['ho'],'target_actual_arrival_phase':nxt['t'],'target_actual_arrival_rank':rank[nxt['t']],
   'target_last_rank':len(H[u])-1,'selected_edge_last_clock_gap':gap}
 cc=cycles(G);assert cc and all(c['winding']==1 for c in cc)
 col={v:i for i,c in enumerate(cc)for v in c['cells']}
 for q in H:
  u=q
  while u not in col:u=G[u][0]
  col[q]=col[u]
 labels=[col[rep[i]]for i in range(P)];stats=[]
 for i,c in enumerate(cc):
  cells=sorted(q for q in H if col[q]==i);ins=[q for q in cells if H[q][0][1]['c']=='L'];outs=[q for q in cells if H[q][-1][1]['c']=='R']
  events=[e for e in E if labels[e['t']]==i];g=sum(1 if e['c']=='R'else-1 for e in events);assert g==len(outs)-len(ins)
  wraps=sum((1 if e['c']=='R'and e['hi']==3 else-1 if e['c']=='L'and e['hi']==0 else 0)for e in events)
  st={'component_id':i,'read_classes':cells,'input_classes':ins,'permanent_output_classes':outs,'I':len(ins),'O':len(outs),'color_charge':g,
    'last_spine':c,'selected_last_edges':[last_edges[v]for v in c['cells']],
    'all_actual_turn_phases':[e['t']for e in events],'branch_cut_wrap_count':wraps,
    'outgoing_cross_counts':[0]*4,'incoming_cross_counts':[0]*4,'out_minus_in_direction_counts':[0]*4,'blocks':[]}
  # Effective spine turn uses the selected predecessor's arrival direction,
  # NOT necessarily the target's actual last incoming direction.
  sp=[]
  for j,v in enumerate(c['cells']):
   prev=c['cells'][j-1];incoming=last_edges[prev]['departure_heading'];outgoing=last_edges[v]['departure_heading'];delta=(outgoing-incoming)%4;assert delta in[1,3]
   actual=H[v][-1][1];sp.append({'class':v,'selected_incoming_heading':incoming,'actual_last_incoming_heading':actual['hi'],
     'outgoing_heading':outgoing,'actual_last_turn':actual['c'],'effective_quarter_turn':1 if delta==1 else-1})
  assert sum(a['effective_quarter_turn']for a in sp)==0;st['effective_spine_turn_details']=sp
  stats.append(st)
 crossings=[]
 for e in E:
  j=(e['t']+1)%P;a=labels[e['t']];b=labels[j]
  if a==b:continue
  dr=e['ho'];stats[a]['outgoing_cross_counts'][dr]+=1;stats[b]['incoming_cross_counts'][dr]+=1
  q=rep[e['t']];r=rank[e['t']];es=H[q];assert r<len(es)-1 # never a last departure
  nexttime,f=es[r+1];age=nexttime-es[r][0];assert age>=4 and age%4==0
  k=lift[e['t']]-lift[f['t']];assert tuple(e['p'])==(f['p'][0]+k*d[0],f['p'][1]+k*d[1]);assert f['t']+k*P-e['t']==age
  crossings.append({'source_phase':e['t'],'target_phase':j,'actual_step_period_voltage':int(j==0),'direction':dr,
   'source_component':a,'target_component':b,'source_position':e['p'],'target_position':(e['p'][0]+D[dr][0],e['p'][1]+D[dr][1]),
   'source_complete_rank':r,'source_complete_count':len(es),'source_first_read':r==0,'source_turn':e['c'],
   'target_complete_rank':rank[j],'target_turn':E[j]['c'],
   'required_next_same_cell_read':{'phase':f['t'],'period_voltage':k,'turn':f['c'],'incoming_heading':f['hi'],'gap':age,'same_component':a}})
 for i,st in enumerate(stats):
  b=[x-y for x,y in zip(st['outgoing_cross_counts'],st['incoming_cross_counts'])];assert sum(b)==0;phi=sum(j*v for j,v in enumerate(b));st['out_minus_in_direction_counts']=b;st['heading_branch_flux']=phi
  assert st['color_charge']==4*st['branch_cut_wrap_count']+phi
  starts=[j for j in range(P)if labels[j]==i and labels[j-1]!=i]
  if not starts:assert len(stats)==1;starts=[0]
  for a in starts:
   b=a
   while b<a+P-1 and labels[(b+1)%P]==i:b+=1
   es=[E[t%P]for t in range(a,b+1)];hin=es[0]['hi'];hout=es[-1]['ho'];g=sum(1 if e['c']=='R'else-1 for e in es);delta=(hout-hin)%4;delta=delta-4 if delta==3 else delta
   assert(g-delta)%4==0
   st['blocks'].append({'start_phase':a,'end_unwrapped_phase':b,'length':b-a+1,'word':''.join(e['c']for e in es),
     'incoming_heading':hin,'outgoing_heading':hout,'actual_signed_turn_sum':g,'principal_endpoint_turn':delta,'residual_full_turns':(g-delta)//4})
  psi=sum(b['principal_endpoint_turn']for b in st['blocks']);wind=sum(b['residual_full_turns']for b in st['blocks']);assert st['color_charge']==4*wind+psi
  st['principal_boundary_flux']=psi;st['block_residual_full_turn_sum']=wind
 # Every BLACK lifetime owner is at the same cell and hence in the same component.
 owners=[]
 for q,es in H.items():
  for (ta,a),(tb,b)in zip(es,es[1:]):
   if a['c']=='R':owners.append({'class':q,'component':col[q],'R_phase':a['t'],'L_phase':b['t'],'age':tb-ta,'owner_period_relative_to_L':lift[b['t']]-lift[a['t']]})
 return {'word':w,'period':P,'drift':d,'initial_heading':h0,'read_class_count':len(H),'components':stats,
  'all_actual_cross_component_steps':crossings,'all_same_component_R_to_L_owners':owners,
  'all_last_departure_edges':[last_edges[q]for q in sorted(H)],
  'all_complete_read_histories':[{'class':q,'component':col[q],'events':[{'canonical_time':t,**e}for t,e in es]}for q,es in sorted(H.items())]}

def sig(a):
 return sorted((c['O'],c['I'],len(c['read_classes']),c['color_charge'],c['principal_boundary_flux'],c['block_residual_full_turn_sum'],len(c['blocks'])if len(a['components'])>1 else 0)for c in a['components'])

def main():
 src=json.loads((R/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls'];base={n:analyze(z['word'])for n,z in src.items()};controls=[]
 expected={'S104':[(8,0,16,8,-4,3),(4,0,6,4,4,0)],'M10':[(1,1,4,0,0,0)],'F80':[(14,2,31,12,0,3)],'P1564':[(301,197,557,104,0,26)],'Q4352':[(590,406,1162,184,0,46)]}
 for n,z in base.items():
  rows=[(c['O'],c['I'],len(c['read_classes']),c['color_charge'],c['principal_boundary_flux'],c['block_residual_full_turn_sum'])for c in z['components']];assert sorted(rows)==sorted(expected[n])
  for h in range(4):
   for power in[1,2,3,5]:
    aa=analyze(z['word']*power,h);assert sig(aa)==[tuple(power*x for x in row)for row in sig(z)]
    for c in aa['components']:
     original=next(o for o in z['components']if c['O']==power*o['O']and c['I']==power*o['I'])
     assert c['out_minus_in_direction_counts']==[power*original['out_minus_in_direction_counts'][(j-h)%4]for j in range(4)]
    controls.append({'name':n,'heading':h,'power':power,'component_signature':sig(aa),'branch_cut_data':[(c['O'],c['branch_cut_wrap_count'],c['heading_branch_flux'])for c in aa['components']]})
  EE,_,_=event_word(z['word'])
  for cut in[1,len(EE)//3,len(EE)//2,len(EE)-1]:
   ww=z['word'][cut:]+z['word'][:cut];aa=analyze(ww,EE[cut]['hi']);assert sig(aa)==sig(z)
   controls.append({'name':n,'phase':cut,'initial_heading':EE[cut]['hi'],'component_signature':sig(aa)})
 S=base['S104'];assert len(S['all_actual_cross_component_steps'])==8
 firstcross=[e for e in S['all_actual_cross_component_steps']if e['source_first_read']];assert len(firstcross)==1 and firstcross[0]['source_phase']==38 and firstcross[0]['target_phase']==39
 # Genuine full finite-field standard realization, with all cross-step source histories.
 capture=9977;frame=capture+3*104;stop=frame+3*104;B={};p=(0,0);h=0;E=[];saved={};want={capture,frame,frame+104};hist=defaultdict(list)
 for t in range(stop+1):
  if t in want:saved[t]={'time':t,'full_black_field':sorted(B),'head':p,'heading':h}
  if t==stop:break
  c='L'if p in B else'R';e={'time':t,'position':p,'incoming_heading':h,'turn':c}
  if c=='L':e['actual_R_owner']=B.pop(p)
  else:B[p]=t
  E.append(e);hist[p].append(e);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 for t in[capture,frame]:
  a=saved[t];assert first_mismatch(State(frozenset(map(tuple,a['full_black_field'])),a['head'],a['heading']),S['word'])is None
 assert ''.join(e['turn']for e in E[frame:frame+104])==S['word']
 actual_cross=[]
 for row in S['all_actual_cross_component_steps']:
  i=frame+row['source_phase'];e=E[i];j=i+row['required_next_same_cell_read']['gap'];assert E[j]['position']==e['position']and E[j]['turn']!=e['turn']
  seen=[q['time']for q in hist[e['position']]if i<q['time']<=j];assert seen==[j]
  actual_cross.append({'normalized_crossing':row,'literal_source':e,'literal_target':E[i+1],'literal_next_same_cell_read':E[j]})
 assert hist[E[frame+38]['position']][0]['time']==frame+38
 # Full prepared profiles/passive strands are dependencies, not silently cropped.
 lif=json.loads((R/'lifetime_boundary_graph_certificate.json').read_text())['controls'];ten=json.loads((R/'prepared_ten_boundary_winding_certificate.json').read_text());eighty=json.loads((R.parent/'audits/winding_budget_counterexample_2026-10-24/prepared80_counterexample.json').read_text())
 backgrounds={n:lif[n]['complete_background']for n in['P1564','Q4352']}
 backgrounds['M10']={'all_n_exact_relation':ten['all_n_exact_relation'],'literal_two_cell_control':ten['literal_two_cell_control'],'scope':ten['scope']}
 backgrounds['F80']={k:eighty[k]for k in['cap','input_ray_starts','input_ray_drift','one_period_output','scope']}
 lower=[]
 for H0 in json.loads((R/'middle_short_coincident_C_cycles_certificate.json').read_text())['six_open_T0_through_T10_interfaces']:
  H={int(t):hs for t,hs in H0.items()};edges={}
  for t,hs in H.items():
   r=len(hs)-1;hd=(hs[-1]+(1 if r%2==0 else-1))%4;dx,dy=D[hd];edges[t]=(t+3*dy-dx,dy)
  paths=[]
  for t in range(11):
   v=t;k=0;path=[]
   while v in edges:
    assert v not in [x['source']for x in path];u,dk=edges[v];path.append({'source':v,'target':u,'voltage':dk});v=u;k+=dk
   paths.append({'start':t,'path':path,'unknown_endpoint_class':v,'total_voltage':k})
  ends={p['unknown_endpoint_class']for p in paths};assert len(ends)==1 and ends.issubset({11,12})
  lower.append({'complete_T0_through_T10':H,'all11_last_departure_paths':paths,'five_permanent_outputs_in_one_exit_basin':[0,1,2,6,7],
   'remaining_permanent_output_count':3,'scope':'The actual physical-component interpretation uses the separately signed unit-shift spine theorem. No minimum output budget or second-component existence is inferred.'})
 out={'status':'AUTHOR exact identity and literal WHITE signed-flux countercontrol; independent audit pending',
  'scope':'Physical LAST-DEPARTURE components, not C faces, first-entry basins, last-L reverse graphs or lifetime-boundary circuits. No per-component output lower bound is inferred.',
  'middle_short_lower_merge':lower,'base_controls':base,'all100_rotation_power_phase_controls':controls,'full_prepared_backgrounds':backgrounds,
  'literal_standard_positive':{'period_frame':frame,'full_states':list(saved.values()),'all104_reads_and_actual_owners':E[frame:frame+104],
    'all_eight_crossings_and_required_next_reads':actual_cross,'actual_first_R_crosses_components':{'source':E[frame+38],'target':E[frame+39]},'exact_all_future_checker':None},
  'dependencies':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in[R/'active_C_entry_exit_forests_certificate.json',R/'middle_short_coincident_C_cycles_certificate.json',R/'lifetime_boundary_graph_certificate.json',R/'prepared_ten_boundary_winding_certificate.json',R.parent/'audits/winding_budget_counterexample_2026-10-24/manifest.json',R.parent/'global_attraction_bridge_2026-10-24/PRIMITIVE_SPINE_CLOCK_MANIFEST.json']}}
 dest=R/'exit_component_turn_flux_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(controls),'representations; standard signed fluxes',[(c['O'],c['principal_boundary_flux'],c['block_residual_full_turn_sum'])for c in S['components']]);print(hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':main()
