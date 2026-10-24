#!/usr/bin/env python3
"""Exact two-layer first/last C forests, spans, physical carries and controls."""
from pathlib import Path
import json,hashlib,sys
from certify_active_C_entry_exit_forests import analyze,active_C
from check_extremal_read_coupling import event_word
from certify_C_excursion_triangular_winding import occ
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'computability'))
from periodic_tail_checker import first_mismatch
from check_rigid_reachability import State
D=[(0,1),(1,0),(0,-1),(-1,0)]

def graph(z):
 E,d,h=event_word(z['word'],h=z['initial_heading']);P=len(E)
 V={tuple(x['class']):x for x in z['C_face_histories']};A={v:x['first_time'] for v,x in V.items()};B={v:x['last_time'] for v,x in V.items()};es=[]
 def edge(kind,sl,s,tl,t,nu,g,**extra):
  ts=(A if sl=='A' else B)[s];tt=(A if tl=='A' else B)[t]+nu*P
  assert tt-ts==g and g>=0
  se=occ(E,d,ts);te=occ(E,d,tt)
  assert active_C(se['p'],se['hi'])==s
  assert active_C(te['p'],te['hi'])==(t[0]+nu*d[0],t[1]+nu*d[1])
  row={'kind':kind,'source_layer':sl,'source':s,'target_layer':tl,'target':t,'voltage':nu,'gap':g,'source_time':ts,'target_time':tt,**extra};es.append(row);return row
 for f in z['first_entry_edges']:
  u=tuple(f['target']);v=tuple(f['source']);nu=-f['voltage'];a=A[v]+nu*P;lt=a-1
  assert occ(E,d,lt)['c']=='L' and lt%P==f['L_phase']
  extra={'WHITE_owned':f['WHITE_first'],'first_entry_L_time':lt,'first_entry_L_phase':f['L_phase']}
  if f['WHITE_first']:
   rt=lt-f['R_to_L_age'];rr=occ(E,d,rt);ll=occ(E,d,lt)
   assert rr['c']=='R' and rt%P==f['R_owner_phase'] and rr['p']==ll['p'] and rr['hi']==ll['hi']
   extra.update(R_owner_time=rt,R_owner_phase=f['R_owner_phase'],R_to_L_age=f['R_to_L_age'])
  edge('first','A',u,'A',v,nu,f['clock_gap'],**extra)
 for f in z['last_exit_edges']:
  u=tuple(f['source']);v=tuple(f['target']);nu=f['voltage'];lt=B[u]
  assert occ(E,d,lt)['c']=='L' and lt%P==f['L_phase']
  extra={'last_exit_L_time':lt,'last_exit_L_phase':f['L_phase'],'selected_cell_ends_R':f['ends_R']}
  if f['ends_R']:
   rt=lt+f['L_to_R_gap'];ll=occ(E,d,lt);rr=occ(E,d,rt)
   assert rr['c']=='R' and rr['p']==ll['p'] and (rr['hi']-ll['hi'])%4==2
   extra.update(final_R_time=rt,final_R_phase=f['final_R_phase'],L_to_R_gap=f['L_to_R_gap'])
  edge('last','B',u,'B',v,nu,f['clock_gap'],**extra)
  if A[v]+nu*P==B[u]+1:edge('literal_handoff','B',u,'A',v,nu,1)
 spans=[]
 for v in sorted(V):
  s=B[v]-A[v];assert s>=0
  if s:assert s%P!=0
  k=(s+P-1)//P
  edge('span','A',v,'B',v,0,s)
  edge('canonical_carry','B',v,'A',v,k,k*P-s)
  spans.append({'face':v,'A':A[v],'B':B[v],'span':s,'minimal_carry':k,'carry_gap':k*P-s})
 return {'period':P,'drift':d,'input_count':z['input_count'],'output_count':z['output_count'],
  'first_BLACK_root_phases':z['first_input_entry_phases'],'other_BLACK_input_phases':z['other_BLACK_input_phases'],
  'face_spans':spans,'edges':es,'maximum_span':max(a['span'] for a in spans),'maximum_carry':max(a['minimal_carry'] for a in spans)}

def counter(z,g,u,v,expect):
 u=tuple(u);v=tuple(v);P=z['period'];E,d,h=event_word(z['word']);S={tuple(a['face']):a for a in g['face_spans']}
 f=next(e for e in g['edges'] if e['kind']=='first' and tuple(e['source'])==u and tuple(e['target'])==v)
 b=next(e for e in g['edges'] if e['kind']=='last' and tuple(e['source'])==v and tuple(e['target'])==u)
 w=f['voltage']+b['voltage'];gg=f['gap']+b['gap'];sv=S[v]['span'];su=S[u]['span']
 assert (w,gg,sv,su)==expect
 assert w*P==gg+sv-su
 sequence=[f,next(e for e in g['edges'] if e['kind']=='span' and tuple(e['source'])==v),b,
   next(e for e in g['edges'] if e['kind']=='canonical_carry' and tuple(e['source'])==u)]
 lift=0;t=S[u]['A'];walk=[];start=t
 for e in sequence:
  assert e['source_time']+lift*P==t
  t+=e['gap'];lift+=e['voltage'];assert e['target_time']+(lift-e['voltage'])*P==t
  ev=[occ(E,d,i) for i in range(t-e['gap'],t)]
  walk.append({'kind':e['kind'],'from':t-e['gap'],'to':t,'duration':e['gap'],'voltage':e['voltage'],'target_lift':lift,'all_events':ev})
 assert t-start==lift*P and lift>0
 return {'u':u,'v':v,'collapsed_winding':w,'first_last_gap_sum':gg,'F_to_B_span_at_v':sv,'B_to_F_span_at_u':su,
  'exact_identity_wP_equals_gap_plus_v_span_minus_u_span':True,'repaired_winding':lift,'repaired_duration':t-start,'full_actual_contiguous_arcs':walk}

def replay(seed,word,p=(0,0),h=0,cuts=()):
 B=set(seed);states=[];events=[]
 for t in range(len(word)+1):
  if t in set(cuts)|{0,len(word)}:states.append({'time':t,'head':p,'heading':h,'full_BLACK':sorted(B)})
  if t==len(word):break
  c='L' if p in B else 'R';assert c==word[t]
  events.append({'time':t,'position':p,'incoming_heading':h,'turn':c})
  B.symmetric_difference_update({p});h=(h+(1 if c=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return {'states':states,'all_events':events}

def main():
 base=json.loads((R/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls'];names=['S104','M10','F80'];gs={n:graph(base[n]) for n in names}
 cs={'S104':counter(base['S104'],gs['S104'],(0,-7),(1,-8),(-1,6,17,127)),
  'M10':counter(base['M10'],gs['M10'],(0,-1),(0,1),(0,6,11,17)),
  'F80':counter(base['F80'],gs['F80'],(0,-1),(3,4),(0,6,11,17))}
 assert [cs[n]['repaired_winding'] for n in names]==[1,2,1]
 # Genuine finite standard field, including all archived unread bits.
 W=base['S104']['word'];start=10359;stop=start+104;B=set();p=(0,0);h=0
 for t in range(start):
  c='L' if p in B else 'R';B.symmetric_difference_update({p});h=(h+(1 if c=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 ww=W[70:]+W[:70];assert first_mismatch(State(frozenset(B),p,h),ww) is None
 finite={'S104':replay(B,ww,p,h,cuts=[5,22,23])}
 finite['S104'].update(blank_absolute_start=start,all_future_periodic_checker=None,word=ww)
 M=base['M10']['word'];finite['M10']=replay({(-1,-1),(-1,0),(0,1)},M*2,cuts=[5,16,17]);finite['M10']['scope']='Exactly two paid periods; infinite repetition still needs its infinite input ray.'
 F=base['F80']['word'];finite['F80']=replay({(-1,-1),(-1,0),(0,1),(3,2)},F,cuts=[5,16,17]);finite['F80']['scope']='Exactly one paid period; infinite repetition still needs both infinite input rays.'
 # Exact rigid maps from normalized graph occurrences to every full-board read.
 for n in names:
  reference=[e for a in cs[n]['full_actual_contiguous_arcs'] for e in a['all_events']]
  actual=finite[n]['all_events'];assert len(reference)==len(actual)
  turn=(actual[0]['incoming_heading']-reference[0]['hi'])%4
  def rotate(p):
   x,y=p
   for _ in range(turn):x,y=y,-x
   return x,y
  rp=rotate(reference[0]['p']);off=(actual[0]['position'][0]-rp[0],actual[0]['position'][1]-rp[1])
  for a,b in zip(reference,actual):
   rp=rotate(a['p']);assert (rp[0]+off[0],rp[1]+off[1])==b['position']
   assert (a['hi']+turn)%4==b['incoming_heading'] and a['c']==b['turn']
  finite[n]['normalized_graph_to_replay']={'clockwise_quarter_turns':turn,'translation':off,'reference_start_time':reference[0]['t']}
 reps=[]
 for n in names:
  w=base[n]['word']
  for h in range(4):
   for q in [1,2,3,5]:
    zz=analyze(w*q,h);g=graph(zz);reps.append({'name':n,'heading':h,'power':q,'face_count':len(g['face_spans']),'edge_count':len(g['edges']),'maximum_span':g['maximum_span'],'maximum_carry':g['maximum_carry'],
     'input_count':g['input_count'],'output_count':g['output_count']})
  for cut in sorted({1,len(w)//3,len(w)//2,len(w)-1}):
   g=graph(analyze(w[cut:]+w[:cut]));reps.append({'name':n,'phase':cut,'face_count':len(g['face_spans']),'edge_count':len(g['edges']),'maximum_span':g['maximum_span'],'maximum_carry':g['maximum_carry']})
 deps=['ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md','active_C_entry_exit_forests_certificate.json','prepared80_budget_falsifier_independent_confirmation.json','C_cycle_excursion_normal_form_certificate.json']
 out={'status':'AUTHOR checked, independent audit pending','scope':'Exact necessary two-clock chronology. Collapsed mixed cycles are not chronological cycles. No carry/span bound, canonical module forcing, input exclusion or classification.',
  'base_graphs':gs,'literal_collapsed_cycle_countercontrols':cs,'complete_finite_field_replays':finite,'representation_checks':reps,
  'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in deps}}
 p=R/'joint_C_temporal_forests_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n')
 for n,g in gs.items():print(n,'span',g['maximum_span'],'carry',g['maximum_carry'],'handoffs',sum(e['kind']=='literal_handoff' for e in g['edges']),'input',g['input_count'],'repaired',cs[n]['repaired_winding'],[len(a['full_BLACK']) for a in finite[n]['states']])
 print('PASS',len(reps),'representations',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
