#!/usr/bin/env python3
"""All-cap terminal C channel after two genuine permanent R outputs."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,sys
from certify_active_C_entry_exit_forests import analyze,active_C
from check_extremal_read_coupling import event_word,quotient
from check_all_cut_wave_interfaces import WORDS
from certify_C_excursion_triangular_winding import occ
from partial_drift31_graph import graph
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'computability'))
from periodic_tail_checker import first_mismatch
from check_rigid_reachability import State
D=[(0,1),(1,0),(0,-1),(-1,0)]

def pair_controls(w,h=0):
 z=analyze(w,h);E,d,_=event_word(w,h=h);P=len(w);H={e['t']:(hh,j) for hh in z['read_histories'] for j,e in enumerate(hh['reads'])};C={tuple(a['class']):a for a in z['C_face_histories']};O={hh['reads'][-1]['t'] for hh in z['read_histories'] if hh['reads'][-1]['c']=='R'}
 def owner(t):
  e=occ(E,d,t);assert e['c']=='L';hh,j=H[t%P]
  if j==0:return {'BLACK_input':True,'L_time':t,'L_position':e['p']}
  a,b=hh['reads'][j-1:j+1];rt=t-(b['canonical_time']-a['canonical_time']);r=occ(E,d,rt);assert r['c']=='R' and r['p']==e['p']
  return {'BLACK_input':False,'R_time':rt,'L_time':t,'position':r['p'],'R_heading':r['hi'],'L_heading':e['hi'],'R_C_face':active_C(r['p'],r['hi'])}
 out=[]
 for i in sorted(O):
  if(i+1)%P not in O:continue
  a,b=occ(E,d,i),occ(E,d,i+1);assert a['c']==b['c']=='R';v=active_C(a['p'],a['hi']);assert active_C(b['p'],b['hi'])==v
  p2=occ(E,d,i+2)['p'];h2=occ(E,d,i+2)['hi'];hr=(h2+1)%4;p3=(p2[0]+D[hr][0],p2[1]+D[hr][1]);assert len({a['p'],b['p'],p2,p3})==4
  q,k=quotient(v,d);cs=C[q];after=[occ(E,d,e['canonical_time']+k*P) for e in cs['visits'] if e['canonical_time']+k*P>i+1]
  mode=after[0]['c'];initial=1 if mode=='L' else 2
  assert [e['t'] for e in after[:initial]]==list(range(i+2,i+2+initial))
  assert ''.join(e['c'] for e in after[:initial]) in ['L','RL']
  assert after[initial-1]['c']=='L';ex=after[initial-1]['t'];transits=[]
  for e in after[initial:]:
   assert e['c']=='L' and e['p']==p3
   en=occ(E,d,e['t']-1);assert en['c']=='L' and en['p']==p2 and active_C(en['p'],en['hi'])!=v
   ow=[owner(en['t']),owner(e['t'])]
   transits.append({'entry':en,'exit':e,'owners':ow})
  extern=[o for t in transits for o in t['owners'] if not o['BLACK_input'] and o['R_time']>ex and tuple(o['R_C_face'])!=v]
  assert len(extern)>=max(0,2*len(transits)-1)
  if mode=='R' and transits:assert transits[0]['owners'][0]['R_time']==i+2
  out.append({'first_R_time':i,'C_face':v,'permanent_output_cells':[a['p'],b['p']],'remaining_corners':[p2,p3],'initial_exit':after[:initial],
   'complete_remaining_C_history':after,'all_later_two_L_transits':transits,'external_R_owners_after_initial_exit':len(extern),'lower_bound':max(0,2*len(transits)-1)})
 return out

def main():
 W={**WORDS,'M10':'RRRRLLLLRL','F80':json.loads((R/'prepared80_budget_falsifier_independent_confirmation.json').read_text())['word']};base={n:pair_controls(w) for n,w in W.items()};assert [len(base[n]) for n in W]==[3,118,216,0,4]
 positive=next(p for p in base['S104'] if p['first_R_time']==29);assert len(positive['all_later_two_L_transits'])==2
 assert [[a['entry']['t'],a['exit']['t']] for a in positive['all_later_two_L_transits']]==[[115,116],[127,128]]
 reps=[]
 for n in ['S104','M10','F80']:
  for h in range(4):
   for q in [1,2,3,5]:
    rows=pair_controls(W[n]*q,h);assert len(rows)==len(base[n])*q;reps.append({'name':n,'heading':h,'power':q,'permanent_pairs':len(rows)})
 # Complete lower named histories of every live middle-short boundary type.
 words=['S','W','S','EEWE','SSNS','EEWE','NNNSS','EEEWW'];HH=[tuple('NESW'.index(c) for c in s) for s in words];kind,G=graph(HH,list(range(8)));assert kind=='open';chain=max(G['chains'],key=len);assert len(chain)==17
 events=[]
 for j,((t,r),k) in enumerate(chain):
  p=(-t+3*k,k);h=HH[t][r];events.append({'time_relative':j,'level':t,'rank':r,'lift':k,'position':p,'heading':h,'turn':'R' if r%2==0 else'L','C_face':active_C(p,h)})
 assert ''.join(e['turn'] for e in events)=='RLRRRRLRRRRLLLLRL'
 cap=[e for e in events if e['C_face']==(-7,-2)];assert [e['time_relative'] for e in cap]==[2,3,4,5,6,14]
 assert ''.join(e['turn'] for e in cap)=='RRRRLL'
 # All four incident complete cell histories supply exactly these six reads.
 allface=defaultdict(list)
 for t,hs in enumerate(HH):
  for r,h in enumerate(hs):
   q,k=quotient(active_C((-t,0),h),(3,1));allface[q].append((t,r,k))
 q,k=quotient((-7,-2),(3,1));assert len(allface[q])==6
 # The other completely known C face has RRRRLRL, followed by its final L.
 q3,k3=quotient((-6,-1),(3,1));assert len(allface[q3])==8
 core={'full_drift':[3,1],'complete_T0_through_T7':words,'all25_named_successor_chains':G['chains'],'forced17_events':events,'forced15_word':''.join(e['turn'] for e in events[2:]),'complete_first_C_history':cap,
  'second_complete_C_event_count':8,'first_parent_alternatives':{'C5':['C3-d through T5.L1','C9 through T8.L1, requiring T8 prefix SS'],'C7':['C5 through T7.L1','C11 through T10.L1, requiring T10 prefix SS']},
  'terminal_pair':{'events':['T6.R4','T7.R4'],'physical_positions':[[-6,0],[-7,0]],'C_face':[-7,0],'corner2_T10':[-7,1],'corner3_T9':[-6,1],'initial_exit_modes':['T10.N/L','T10.N/R -> T9.E/L'],'later_transit':'T10.S/L -> T9.E/L','outside_owner_headings':['T10.S/R','T9.W/R']}}
 # Fresh complete blank replay and exact future certificate. This is a local
 # no-input countercontrol, not a repeated full(3,1) front.
 B=set();p=(0,0);h=0;E=[];CH=defaultdict(list);PH=defaultdict(list);snap={}
 cuts={7895,7910,7922,9977,10006,10009,10094,10106,10344,10359}
 for t in range(10449):
  if t in cuts:snap[t]={'time':t,'head':p,'heading':h,'complete_BLACK':sorted(B)}
  if t==10448:break
  c='L' if p in B else'R';e={'time':t,'position':p,'heading':h,'turn':c,'C_face':active_C(p,h)};E.append(e);CH[e['C_face']].append(e);PH[p].append(e)
  B.symmetric_difference_update({p});h=(h+(1 if c=='R' else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 ss=snap[9977];assert first_mismatch(State(frozenset(map(tuple,ss['complete_BLACK'])),ss['head'],ss['heading']),W['S104']) is None
 drift=(E[10081]['position'][0]-E[9977]['position'][0],E[10081]['position'][1]-E[9977]['position'][1]);assert drift==(-2,-2)
 def later_hits(q,key):
  ans=[]
  for i in range(104):
   p=E[9977+i][key];nums=[]
   for a,b,d in zip(q,p,drift):
    if (a-b)%d:break
    nums.append((a-b)//d)
   else:
    if nums[0]==nums[1] and 9977+i+104*nums[0]>=10448:ans.append((i,nums[0]))
  return ans
 corners=[(-14,0),(-13,0),(-15,-1),(-14,-1),(-13,-1),(-15,-2),(-14,-2),(-13,-2)]
 hist={str(i):PH[p] for i,p in enumerate(corners)}
 assert [''.join('NESW'[(e['heading']-2)%4] for e in hist[str(i)]) for i in range(8)]==['S','W','S','EEWE','SSNS','EEWE','NNNS','EEEW']
 assert all(not later_hits(p,'position') for p in corners)
 for q in [(-14,-1),(-15,-2)]:assert not later_hits(q,'C_face')
 assert ''.join(e['turn'] for e in E[7895:7910])==core['forced15_word']
 assert [e['time'] for e in CH[(-14,-1)]]==[7895,7896,7897,7898,7899,7907]
 assert [e['time'] for e in CH[(-15,-2)]]==[7900,7901,7902,7903,7904,7908,7909,7921]
 # Standard contains the same literal15 word, but not the early retirement.
 assert W['S104'][55:70]==core['forced15_word']
 standard=analyze(W['S104']);se,sd,_=event_word(W['S104']);sf=active_C(se[55]['p'],se[55]['hi']);sq,sk=quotient(sf,sd);row=next(a for a in standard['C_face_histories'] if tuple(a['class'])==sq)
 assert len(row['visits'])==15 and row['last_time']+sk*104==309
 out={'status':'AUTHOR checked, independent audit pending','scope':'Conditional all-length permanent-output terminal channel; exact middle-short first/last entry alternatives; literal standard and blank local countercontrols. No middle-short type excluded or completed.',
  'base_permanent_pair_controls':base,'representation_controls':reps,'middle_short_necessary_C_interface':core,
  'standard15_word_positive':{'phase':55,'same_C_face_complete_reads':15,'first_time':55,'last_time':309},
  'blank_early_retirement_countercontrol':{'start':7895,'full_eight_physical_histories':hist,'complete_two_C_histories':[CH[(-14,-1)],CH[(-15,-2)]],'exact_difference_from_middle_short':['T6 NNNS, not NNNSS','T7 EEEW, not EEEWW'],'all_future_clearance':'All104 full-drift ray equations tested separately for each selected cell and face; no later hits.','capture_word':W['S104'],'capture_drift':drift,'full_field_snapshots':snap},
  'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['MIDDLE_SHORT_FOUR_BOUNDARY_TYPES.md','partial_drift31_graph.py','ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md','C_TRACE_LAP_OWNERSHIP_AND_FIXED_GEOMETRY_RIGIDITY.md','active_C_entry_exit_forests_certificate.json']}}
 dest=R/'C_permanent_pair_terminal_channel_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n');print('PASS',sum(map(len,base.values())),'base pairs,',len(reps),'representations, complete blank countercontrol',hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':main()
