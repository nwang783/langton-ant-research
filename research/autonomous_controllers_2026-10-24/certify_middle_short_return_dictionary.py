#!/usr/bin/env python3
"""Exact T8 first-return interface and a finite supplied-return prefix cover.
No arbitrary period cap: unrestricted suffixes are rejected at 64 finite leaves.
"""
from pathlib import Path
from collections import defaultdict, Counter
import json, hashlib, sys
from check_extremal_read_coupling import event_word, D
from certify_active_C_entry_exit_forests import active_C
from partial_drift31_graph import quotient31
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'computability'))
from periodic_tail_checker import first_mismatch
from check_rigid_reachability import State
K='LRLRRRRLRRRRLLLLRL'
ROOT=(-8,0)

def literal(word,h=0,p=ROOT):
 E,d,hh=event_word(word,h=h,p=p);last={};first={}
 for e in E:
  q=e['p'];first.setdefault(q,e)
  if q in last and last[q]['c']==e['c']:
   return {'legal':False,'word':word,'earlier':last[q],'later':e,
    'intervening_positions':[x['p'] for x in E[last[q]['t']+1:e['t']]],'start_position':p,'start_heading':h}
  last[q]=e
 B={q for q,e in first.items() if e['c']=='L'};initial=sorted(B)
 for e in E:
  assert ('L'if e['p']in B else'R')==e['c'];B.symmetric_difference_update({e['p']})
 return {'legal':True,'word':word,'start_position':p,'start_heading':h,'full_minimal_initial_black':initial,
  'full_final_black':sorted(B),'final_position':(p[0]+d[0],p[1]+d[1]),'final_heading':hh,'events':E}

def palettes(z):
 w=z['word'];P=len(w);ans={x:{}for x in ['E','F','G']}
 for cl in z['read_histories']:
  for e,f in zip(cl['reads'],cl['reads'][1:]):
   a=e['canonical_time'];b=f['canonical_time'];word=''.join(w[t%P]for t in range(a,b));typ=None
   if e['c']=='R' and e['hi']==f['hi']:typ='E';h=2
   if e['c']=='L' and (f['hi']-e['hi'])%4==2:typ='F';h=0
   if e['c']=='L' and e['hi']==f['hi']:typ='G';h=2
   if typ is None:continue
   ee,d,hh=event_word(word,h=h,p=ROOT);assert d==(0,0)
   assert all(e['p']!=ROOT for e in ee[1:])
   lev=[3*active_C(q['p'],q['hi'])[1]-active_C(q['p'],q['hi'])[0]for q in ee]
   good=(min(lev)>=7)if typ=='E'else(lev[0]==5 and min(lev[1:])>=7 and word[:2]=='LR')if typ=='F'else(word[:3]=='LLL'and lev[1]==5 and min(lev[:1]+lev[2:])>=7)
   if good:ans[typ].setdefault(word,{'word':word,'standard_start_phase':a%P,'standard_length':b-a,'standard_read_class':cl['class'],
      'standard_consecutive_events':[e,f],'normalized_heading':h,'normalized_C_levels':lev})
 return {k:[v[s]for s in sorted(v,key=lambda s:(len(s),s))]for k,v in ans.items()}

def lower_returns(H):
 H={int(t):h for t,h in H.items()};out={}
 for t,hs in H.items():
  p=(-t,0)
  for d in range(4):
   src=[r for r,h in enumerate(hs)if(h+(1 if r%2==0 else-1))%4==d]
   q,k=quotient31((p[0]+D[d][0],p[1]+D[d][1]));u=-q[0]
   if u not in H:continue
   dst=[r for r,h in enumerate(H[u])if h==d];assert len(src)==len(dst)
   for r,s in zip(src,dst):out[t,r]=((u,s),k)
 odd=3 if H[8][3]==0 else 5;v=(8,odd-1);lift=0;path=[]
 for j in range(5):
  t,r=v;p=(-t+3*lift,lift);path.append({'node':v,'lift':lift,'position':p,'heading':H[t][r],'turn':'R'if r%2==0 else'L'})
  if j<4:v,dk=out[v];lift+=dk
 assert [e['node'][0]for e in path]==[8,9,6,5,8]
 assert path[0]['position']==path[-1]['position']==ROOT and v==(8,odd)
 assert ''.join(e['turn']for e in path)=='RLLLL'
 same=[r for r in [2,4,6] if H[8][r]==H[8][r+1]==2];assert len(same)==2
 return {'T8_history':H[8],'opposite_return_five_events':path,'same_heading_R_to_L_pairs':[(r,r+1)for r in same],
  'mode':'A'if odd==3 else'B','period_word_template':'D F1 O F2 E1 G E2 K'if odd==3 else'D F1 E1 G O F2 E2 K'}

def cover(pal):
 P={k:[x['word']for x in a]for k,a in pal.items()};leaves=[];stages=[];positive32=None
 for mode in ['A','B']:
  seq=[('D',['RRRR']),('F1',P['F'])]+([('O',['RLLL']),('F2',P['F']),('E1',P['E'])]if mode=='A'else[('E1',P['E'])])
  todo=[('',[])]
  for name,choices in seq:
   nxt=[]
   for pre,lab in todo:
    for j,w in enumerate(choices):
     trace=literal(pre+w);labels=lab+[(name,j)]
     if trace['legal']:
      nxt.append((pre+w,labels))
      if mode=='A'and name=='F2':assert positive32 is None;positive32=trace
     else:leaves.append({'mode':mode,'last_block':name,'block_choices':labels,'literal_consecutive_same_turn_witness':trace})
   stages.append({'mode':mode,'block':name,'attempts':len(todo)*len(choices),'surviving_prefixes':len(nxt)})
   todo=nxt
  assert not todo
 assert Counter((x['mode'],x['last_block'])for x in leaves)=={('A','O'):4,('A','F2'):20,('A','E1'):5,('B','E1'):35}
 assert len(leaves)==64 and len(positive32['word'])==32
 assert len(positive32['full_minimal_initial_black'])==3 and len(positive32['full_final_black'])==9
 assert positive32['final_position']==ROOT and positive32['final_heading']==2
 return {'complete_prefix_tree_stages':stages,'all64_terminal_witnesses':leaves,'unique_32_read_prepared_survivor_before_E1':positive32,
  'scope':'Mode A permits arbitrary G,E2 and every later continuation. Mode B permits arbitrary G,F2,E2 and every later continuation. Only the stated initial return dictionaries are restricted.'}

def main():
 z=json.loads((R/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls']['S104'];pal=palettes(z)
 assert {k:len(v)for k,v in pal.items()}=={'E':5,'F':7,'G':3}
 h=json.loads((R/'middle_short_coincident_C_cycles_certificate.json').read_text())['six_open_T0_through_T10_interfaces'];ret=[lower_returns(H)for H in h]
 for w,heading,dh,hi in [('RRRR',0,(0,0),0),('RLLL',2,(0,0),0),(K,2,(3,1),0)]:
  es,d,hh=event_word(w,h=heading,p=ROOT);assert d==dh and hh==hi
 # Materialize all 15 source factors inside a genuine complete standard future.
 frame=9977+3*104;cuts={9977}
 for ls in pal.values():
  for row in ls:row['blank_start']=frame+row['standard_start_phase'];row['blank_end']=row['blank_start']+len(row['word']);cuts.update([row['blank_start'],row['blank_end']])
 B={};p=(0,0);head=0;E=[];states={}
 for t in range(max(cuts)+1):
  if t in cuts:states[t]={'time':t,'full_black_field':sorted(B),'head':p,'heading':head}
  if t==max(cuts):break
  c='L'if p in B else'R';e={'time':t,'position':p,'heading':head,'turn':c}
  if c=='L':e['actual_R_owner']=B.pop(p)
  else:B[p]=t
  E.append(e);head=(head+(1 if c=='R'else-1))%4;p=(p[0]+D[head][0],p[1]+D[head][1])
 cap=states[9977];assert first_mismatch(State(frozenset(map(tuple,cap['full_black_field'])),cap['head'],cap['heading']),z['word'])is None
 for ls in pal.values():
  for row in ls:
   a,b=row['blank_start'],row['blank_end'];ee=E[a:b];assert ''.join(e['turn']for e in ee)==row['word']
   assert states[a]['head']==states[b]['head'];assert all(e['position']!=states[a]['head']for e in ee[1:])
   row['source_full_initial_state']=states[a];row['source_full_final_state']=states[b];row['source_events_and_actual_owners']=ee
 out={'status':'AUTHOR checked, independent audit pending','scope':'Exact live middle-short return interface and conditional local supplied-return obstruction; no open core order, arbitrary excursion, controller or capture classification.',
  'six_exact_lower_return_interfaces':ret,'fixed_words':{'D':'RRRR','O':'RLLL','K':K},'standard_return_dictionaries':pal,
  'arbitrary_suffix_prefix_cover':cover(pal),'full_standard_capture':cap,'full_standard_future_mismatch':None,
  'finite_family_size_if_all_five_free_words_restricted':2*5*5*7*7*3,
  'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in['MIDDLE_SHORT_C_CORE_FOUR_CHANNEL_OWNER_INTERFACE.md','MIDDLE_SHORT_COINCIDENT_FIRST_LAST_C_CORE.md','middle_short_coincident_C_cycles_certificate.json','active_C_entry_exit_forests_certificate.json','C_TRACE_LAP_OWNERSHIP_AND_FIXED_GEOMETRY_RIGIDITY.md']}}
 dest=R/'middle_short_return_dictionary_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n');print('PASS64 bad-prefix leaves,15 genuine standard source factors,6 exact return interfaces',hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':main()
