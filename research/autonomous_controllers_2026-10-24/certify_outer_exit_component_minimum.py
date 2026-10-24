#!/usr/bin/env python3
"""Outer basin extrema and exact cut chronology. Four-output target OPEN."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
from check_extremal_read_coupling import event_word,quotient,D
from certify_exit_component_turn_flux import analyze
R=Path(__file__).resolve().parent

def probe(w,h=0):
 a=analyze(w,h);E,d,_=event_word(w,h=h);P=len(w);H={tuple(v['class']):v for v in a['all_complete_read_histories']};normal=lambda q:d[0]*q[1]-d[1]*q[0]
 # These controls have separated spine ranges. General proof does NOT require it.
 order=sorted(a['components'],key=lambda c:min(normal(q)for q in c['last_spine']['cells']));idx={c['component_id']:i for i,c in enumerate(order)}
 ranges=[(min(normal(q)for q in c['last_spine']['cells']),max(normal(q)for q in c['last_spine']['cells']))for c in order]
 assert all(x[1]<y[0]for x,y in zip(ranges,ranges[1:]))
 lo=min(map(normal,H));hi=max(map(normal,H));ext=[]
 white=all(v['events'][0]['c']=='R'for v in H.values())
 for value,rank in[(lo,0),(hi,len(order)-1)]:
  vv=[v for q,v in H.items()if normal(q)==value];assert all(idx[v['component']]==rank for v in vv)
  if white and d[0]and d[1]:assert all(len(v['events'])==1 and v['events'][0]['c']=='R'for v in vv)
  ext.append({'normal_value':value,'ordered_basin':rank,'complete_extreme_histories':vv})
 cr=[]
 for e in a['all_actual_cross_component_steps']:
  t=e['source_phase'];q,k=quotient(e['source_position'],d);v,l=quotient(e['target_position'],d)
  aa=H[q]['events'];bb=H[v]['events'];A=aa[0]['canonical_time']+k*P;B=aa[-1]['canonical_time']+k*P;C=bb[0]['canonical_time']+l*P;F=bb[-1]['canonical_time']+l*P
  assert A<=t and B>=t+4 and C<=t+1<=F
  if white:
   assert aa[0]['c']=='R'and bb[0]['c']=='R'
   if e['target_complete_rank']==0:assert C==t+1 and e['target_turn']=='R'
  cr.append({'source_phase':t,'source_basin':idx[e['source_component']],'target_basin':idx[e['target_component']],'source_first_time':A,'source_last_time':B,'target_first_time':C,'target_last_time':F,'source_turn':e['source_turn'],'source_rank':e['source_complete_rank'],'target_turn':e['target_turn'],'target_rank':e['target_complete_rank'],'actual_next_source_read':e['required_next_same_cell_read']})
 return {'period':P,'drift':d,'word':w,'heading':h,'WHITE':white,'ordered_basins':[{'original_id':c['component_id'],'O':c['O'],'I':c['I'],'charge':c['color_charge'],'fixed_heading_Phi':c['heading_branch_flux'],'Phi_mod4':c['heading_branch_flux']%4,'Q':c['branch_cut_wrap_count'],'spine_range':rr,'read_classes':c['read_classes']}for c,rr in zip(order,ranges)],'extrema':ext,'every_cut_crossing_first_last_clock':cr,'complete_analysis':a}

def prepared_normal_form(w):
 E,d,h=event_word(w);P=len(w);H=defaultdict(list)
 for e in E:
  q,k=quotient(e['p'],d);H[q].append((e['t']-k*P,k,e))
 cap=[];rays=[];profiles=[]
 for q,es in sorted(H.items()):
  es.sort();assert all(a[2]['c']!=b[2]['c']for a,b in zip(es,es[1:]));low=min(k for _,k,_ in es);high=max(k for _,k,_ in es);cn=[]
  for n in range(low,high):
   available=[e for e in es if e[1]<=n];first=min(available,key=lambda e:e[0]);
   if first[2]['c']=='L':cn.append(n);cap.append((q[0]+n*d[0],q[1]+n*d[1]))
  ray=high if es[0][2]['c']=='L'else None
  if ray is not None:rays.append({'class':q,'start_lift':ray,'start_position':(q[0]+ray*d[0],q[1]+ray*d[1]),'step':d})
  profiles.append({'class':q,'cap_lifts':cn,'ray_start':ray,'lowest_read_lift':low,'highest_read_lift':high,'stable_events':[{'canonical_time':t,'lift':k,**e}for t,k,e in es]})
 T={tuple(x['class']):x for x in profiles}
 def bit(p):
  q,k=quotient(p,d);x=T.get(q)
  return False if x is None else(k in x['cap_lifts']or x['ray_start']is not None and k>=x['ray_start'])
 flips=set()
 for e in E:
  p=tuple(e['p']);assert(bit(p)^(p in flips))==(e['c']=='L');flips.symmetric_difference_update({p})
 assert all(v['stable_events'][-1]['c']=='L'for v in profiles)
 checks=[]
 for v in profiles:
  q=v['class']
  for k in range(v['lowest_read_lift']-1,v['highest_read_lift']+3):
   p=(q[0]+k*d[0],q[1]+k*d[1]);b=bit(p)^(p in flips);shift=bit((p[0]-d[0],p[1]-d[1]));assert b==shift;checks.append([q,k,int(b)])
 finite=[]
 for N in[1,2,3,5]:
  before=set();state=set();seen=set();p=(0,0);h=0;reads=[]
  for t,ch in enumerate(w*N):
   if p not in seen:
    if ch=='L':before.add(p);state.add(p)
    seen.add(p)
   assert(p in state)==(ch=='L');reads.append((t,p,h,ch));state.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  assert before=={q for q in seen if bit(q)}
  finite.append({'copies':N,'complete_minimal_initial_BLACK':sorted(before),'complete_final_BLACK':sorted(state),'final_head':p,'heading':h,'all_reads':reads})
 return {'complete_forward_cap':sorted(cap),'complete_forward_input_rays':rays,'full_class_profiles':profiles,'one_period_full_field_translation_checks':checks,'terminal_all_L_no_output':True,'finite_prepared_controls':finite}

def main():
 src=json.loads((R/'exit_component_turn_flux_certificate.json').read_text())['base_controls'];base={n:probe(a['word'])for n,a in src.items()};w=src['S104']['word'][::-1].translate(str.maketrans('RL','LR'));inv=probe(w);norm=prepared_normal_form(w)
 assert[(c['O'],c['I'],c['Phi_mod4'])for c in inv['ordered_basins']]==[(0,7,1),(0,5,3)]
 assert len(norm['complete_forward_input_rays'])==12
 controls=[]
 for h in range(4):
  z=probe(src['S104']['word'],h);assert[(c['O'],c['I'])for c in z['ordered_basins']]==[(4,0),(8,0)];controls.append(z)
 # Reuse existing signed OPEN minimum interface only as an explicit non-completion reminder.
 minimum=json.loads((R/'drift31_read_minimum_certificate.json').read_text());one=next(x for x in minimum['all25_open_interfaces']if x['lower_index']==6 and x['V4_index']==0)
 H=one['complete_histories'][3:];assert H==[[2],[3,1],[2,2],[1,1,3],[2,2,0,0]]
 last={i:i+[3,-1,-3,1][(v[-1]+(1 if len(v)%2 else-1))%4]for i,v in enumerate(H)if v};assert last=={0:1,1:4,2:1,3:6,4:5}
 named={'signed_interface_indices':[6,0],'complete_named_histories':H,'last_arrows':last,'minimum_chain':[0,1,4,5],'minimum_chain_named_odd_outputs':[0],'unknown_upper_class':5,'warning':'This is not the complete outer basin. Unknown higher cells may provide arbitrarily many further outputs, so this is NOT a counterexample to O_outer>=4.'}
 deps=['PHYSICAL_EXIT_COMPONENT_SIGNED_HANDOFF_2003.md','PHYSICAL_EXIT_SPINES_ORDER_COMPONENTS_AND_FLUX_CUTS.md','exit_component_turn_flux_certificate.json','DRIFT31_UNCONDITIONAL_READ_MINIMUM_INTERFACE.md','drift31_read_minimum_certificate.json','../audits/check_drift31_read_minimum_independent.json']
 out={'scope':'Non-axis WHITE outer basin has at least one permanent singleton by read-footprint extremum. Four-output lower bound and modulo-four boundary cancellation remain OPEN. Exact first/last cut clocks, standard positives and pure-input reversed-standard premise check retain complete fields.','base_controls':base,'all4_standard_rotations':controls,'reversed_standard_prepared_premise_check':{'analysis':inv,'full_background':norm},'one_named_odd_OPEN_minimum_interface':named,'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in deps}}
 path=R/'outer_exit_component_minimum_certificate.json';path.write_text(json.dumps(out,indent=2)+'\n');print('PASS author',hashlib.sha256(path.read_bytes()).hexdigest(),'inverse cap',len(norm['complete_forward_cap']),'rays',len(norm['complete_forward_input_rays']))
if __name__=='__main__':main()
