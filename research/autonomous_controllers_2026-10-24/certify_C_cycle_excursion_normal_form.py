#!/usr/bin/env python3
"""Actual closed-pose excursion decomposition and standard's self-fed M10.
No module's isolated prepared roots are treated as full-controller roots.
"""
from pathlib import Path
from collections import Counter,defaultdict
import json,hashlib,sys
from certify_active_C_entry_exit_forests import analyze,active_C
from check_extremal_read_coupling import event_word
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'computability'))
from periodic_tail_checker import first_mismatch,plan
from check_rigid_reachability import State
D=[(0,1),(1,0),(0,-1),(-1,0)]

def decompose(z):
 w=z['word'];P=len(w);F={tuple(x['source']):x for x in z['first_entry_edges']};out=[]
 for cy in z['WHITE_first_entry_cycles']:
  es=[F[tuple(v)]for v in cy['vertices']];cut=min(e['R_owner_phase']for e in es)
  es=sorted(es,key=lambda e:(e['R_owner_phase']-cut)%P);parts=[]
  for j,e in enumerate(es):
   start=(e['R_owner_phase']-cut)%P;age=e['R_to_L_age'];end=start+age
   nxt=(es[(j+1)%len(es)]['R_owner_phase']-cut)%P+(P if j==len(es)-1 else 0)
   assert end<nxt
   ew=''.join(w[(cut+t)%P]for t in range(start,end));cw=''.join(w[(cut+t)%P]for t in range(end,nxt))
   ee,dd,hh=event_word(ew);assert dd==(0,0)and hh==0 and ew[0]=='R' and cw[0]=='L'
   assert all(x['p']!=(0,0)for x in ee[1:])
   parts.append({'R_owner_phase':e['R_owner_phase'],'L_phase':e['L_phase'],'start':start,'end':end,
    'excursion_word':ew,'connector_word':cw,'excursion_growth':ew.count('R')-ew.count('L'),
    'connector_growth':cw.count('R')-cw.count('L')})
  assert ''.join(x['excursion_word']+x['connector_word']for x in parts)==w[cut:]+w[:cut]
  assert sum(x['end']-x['start']+len(x['connector_word'])for x in parts)==P
  sk=''.join(x['connector_word']for x in parts);whole,_,_=event_word(w,h=z['initial_heading']);ch=whole[cut]['hi'];_,dd,hh=event_word(sk,h=ch);assert dd==tuple(z['drift'])and hh==ch
  out.append({'period_cut_phase':cut,'parts':parts,'geometric_skeleton':sk,'skeleton_is_not_claimed_legal':True})
 return out

def main():
 cert=json.loads((R/'active_C_entry_exit_forests_certificate.json').read_text());base=cert['base_controls'];dec={n:decompose(z)for n,z in base.items()}
 W=base['S104']['word'];E8=''.join(W[(46+i)%104]for i in range(8));E92=''.join(W[(56+i)%104]for i in range(92));M='RRRRLLLLRL'
 assert E8=='RRRLLLLR'and W[45:]+W[:45]=='R'+E8+'L'+'R'+E92+'L'
 assert 'R'+E8+'L'==M and (E92.count('R')-E92.count('L'))==12
 # Full literal blank realization, in a certified standard tail, retaining every field bit.
 capture=9977;frame=capture+3*104;start=frame+45;stop=start+104
 B={};p=(0,0);h=0;E=[];saved={};lifes=[]
 for t in range(stop+1):
  if t in[capture,start,start+10,stop]:saved[t]=(dict(B),p,h)
  if t==stop:break
  c='L'if p in B else'R';row={'time':t,'position':p,'incoming_heading':h,'turn':c}
  if c=='L':r=B.pop(p);row['actual_R_owner']=r;lifes.append((r,t))
  else:B[p]=t
  E.append(row);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 assert ''.join(e['turn']for e in E[start:stop])==W[45:]+W[:45]
 bc,pc,hc=saved[capture];assert len(bc)==715 and first_mismatch(State(frozenset(bc),pc,hc),W)is None
 bs,ps,hs=saved[start];be,pe,he=saved[stop];rot=W[45:]+W[:45]
 assert first_mismatch(State(frozenset(bs),ps,hs),rot)is None
 qs,d=plan(State(frozenset(bs),ps,hs),rot);assert d==(-2,-2)
 owned=[];matrix=Counter();outputs=[]
 for e in E[start:stop]:
  rel=e['time']-start;target='A10'if rel<10 else'B94'
  if e['turn']=='L':
   owner=e['actual_R_owner'];rrel=owner-start;source='A10'if rrel%104<10 else'B94';shift=rrel//104
   matrix[(source,target)]+=1
   owned.append({'R_time':owner,'L_time':e['time'],'R_relative_to_cut':rrel,'L_relative_to_cut':rel,'source_block':source,'target_block':target,'owner_period':shift,'cell':e['position'],'age':e['time']-owner})
 # For all perpetual stable owners, use the complete standard read classes, not the finite stop.
 owner_by_phase={};outs=[]
 for hh in base['S104']['read_histories']:
  rs=hh['reads'];assert rs[0]['c']=='R'
  for j,e in enumerate(rs):
   if e['c']=='L':owner_by_phase[e['t']]=(rs[j-1]['t'],e['canonical_time']-rs[j-1]['canonical_time'])
  if rs[-1]['c']=='R':outs.append(rs[-1]['t'])
 assert len(owned)==46 and matrix=={('A10','A10'):3,('B94','A10'):2,('A10','B94'):2,('B94','B94'):39}
 assert all((t-45)%104>=10 for t in outs)and len(outs)==12
 for e in E[start:stop]:
  if e['turn']=='L':
   phase=(e['time']-frame)%104;r,age=owner_by_phase[phase];assert e['actual_R_owner']==e['time']-age and (e['actual_R_owner']-frame)%104==r
 required=[(frame-42,frame+50),(frame+43,frame+51),(frame+47,frame+107),(frame+53,frame+65)]
 assert all((r,l)in lifes for r,l in required)
 # Minimal complete finite field for isolated M, and exact untouched-field union in this context.
 EE,md,mh=event_word(M,h=hs,p=ps);reads={e['p']for e in EE};first={}
 for e in EE:first.setdefault(e['p'],e['c'])
 mini={q for q,c in first.items()if c=='L'};actual_input=bs.keys()&reads;assert mini==actual_input and len(mini)==2
 mini_after=set(mini)
 for e in EE:
  assert ('L'if e['p']in mini_after else'R')==e['c'];mini_after.symmetric_difference_update({e['p']})
 ba,pa,ha=saved[start+10];unread=set(bs)-reads
 assert set(ba)==mini_after|unread and len(mini_after)==2 and len(unread)+2==len(ba)
 controls=[]
 for n,z in base.items():
  for h in range(4):
   for q in[1,2,3]:
    zz=analyze(z['word']*q,h);dd=decompose(zz);controls.append({'name':n,'heading':h,'power':q,'cycle_count':len(dd),'excursion_counts':[len(x['parts'])for x in dd]})
 out={'status':'AUTHOR exact all-cap normal form and genuine standard self-feeding control; independent audit pending',
  'scope':'Known standard104, not a new controller. Excursion removal gives only a geometric skeleton. No fields, owners or whole-front WHITE hypotheses are discarded.',
  'base_decompositions':dec,'standard_module_words':{'A10':M,'B94':'R'+E92+'L','E8':E8,'E92':E92},
  'full_blank_realization':{'capture_cut':capture,'period_frame':frame,'A10_start':start,'B94_start':start+10,'period_end':stop,
   'states':[{'time':t,'full_black_field':sorted(B0),'head':p0,'heading':h0}for t,(B0,p0,h0)in sorted(saved.items())],
   'all104_events':E[start:stop],'all46_actual_owned_lifetimes':owned,'block_matrix':[{'source':s,'target':t,'count':v}for(s,t),v in sorted(matrix.items())],
   'permanent_output_phases_all_in_B94':sorted(outs),'M10_full_input':sorted(mini),'M10_full_local_output':sorted(mini_after),
   'M10_complete_untouched_field':sorted(unread),'exact_infinite_checker_result_at_capture':None,'exact_infinite_checker_result_at_module_cut':None,'full_drift':d,
   'key_recycling_pairs':[{'R_time':r,'L_time':l,'R_relative_to_frame':r-frame,'L_relative_to_frame':l-frame,'cell':E[r]['position']}for r,l in required]},
  'representation_controls':controls,
  'dependencies':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in[R/'ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md',R/'active_C_entry_exit_forests_certificate.json',R.parent/'computability/periodic_tail_checker.py',R.parent/'computability/check_rigid_reachability.py']}}
 p=R/'C_cycle_excursion_normal_form_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS genuine standard M10/B94 mutual ownership; full fields',[(t,len(b))for t,(b,p,h)in saved.items()]);print(hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
