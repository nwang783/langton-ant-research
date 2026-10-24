#!/usr/bin/env python3
"""Exact occurrence-voltage R-lap constraints for a fixed complete C trace."""
from collections import defaultdict
from pathlib import Path
import json,hashlib
from check_extremal_read_coupling import event_word,quotient
from check_all_cut_wave_interfaces import WORDS
from certify_active_C_entry_exit_forests import active_C
D=[(0,1),(1,0),(0,-1),(-1,0)]

def build(w,h0=0):
 E,d,_=event_word(w,h=h0)
 cut=(max(e['t'] for e in E if e['c']=='L')+1)%len(w)
 h=E[cut]['hi'];p=E[cut]['p'];w=w[cut:]+w[:cut]
 chunks=w.split('L')[:-1];assert w.endswith('L');ks=list(map(len,chunks));N=len(ks)
 assert set(ks)<=set([0,1,2,4]);opts=[i for i,k in enumerate(ks) if k in (0,4)]
 H=defaultdict(list);meta={};chosen={i:int(ks[i]==4) for i in opts};cursor=[]
 def ev(i,j,p,kind,var=None):
  q,k=quotient(p,d);x={'block':i,'slot':j,'p':p,'class':q,'lift':k,'order':(i-N*k,j),'kind':kind,'var':var}
  H[q].append(x);return x
 for i,k in enumerate(ks):
  a=active_C(p,h);cursor.append((p,h,a))
  if i in opts:
   pp,hh=p,h;ee=[]
   for j in range(4):
    ee.append(ev(i,j,pp,'R',i));hh=(hh+1)%4;pp=(pp[0]+D[hh][0],pp[1]+D[hh][1])
   assert (pp,hh)==(p,h);meta[i]=ee
  else:
   for j in range(k):
    ev(i,j,p,'R');h=(h+1)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  ev(i,4,p,'L');h=(h-1)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 for hs in H.values():hs.sort(key=lambda e:e['order'])
 return dict(word=w,cut=cut,drift=d,heading=E[cut]['hi'],position=E[cut]['p'],ks=ks,optional=opts,chosen=chosen,histories=H,cursors=cursor)

def constraints(z,white=True):
 cons=[];bad=[]
 def con(q,typ,es,target):
  cons.append({'class':q,'type':typ,'vars':[e['var'] for e in es], 'target':target,'occurrences':[{'phase':e['var'],'voltage':-e['lift'],'block':e['block'],'slot':e['slot'],'position':e['p'],'order':e['order']} for e in es]})
 for q,hs in z['histories'].items():
  mm=[j for j,e in enumerate(hs) if e['var'] is None]
  if not mm:
   con(q,'all_optional',hs,'<=1');continue
  a=mm[0];b=mm[-1]
  con(q,'prefix_'+hs[a]['kind'],hs[:a],0 if hs[a]['kind']=='R' else (1 if white else '<=1'))
  for x,y in zip(mm,mm[1:]):
   pair=hs[x]['kind']+hs[y]['kind'];es=hs[x+1:y]
   if pair=='RR':bad.append({'class':q,'type':'mandatory_RR','events':[hs[x],hs[y]]})
   con(q,pair,es,1 if pair=='LL' else 0)
  con(q,'suffix_'+hs[b]['kind'],hs[b+1:],0 if hs[b]['kind']=='R' else '<=1')
 return cons,bad

def uniform_propagation(z,white=True):
 # NO identification of different translated copies is used here.  A phase
 # value means every translate (or every sufficiently late translate) is fixed.
 cons,bad=constraints(z,white);vals={};threshold={};proof=[]
 if bad:return {'possible':False,'values':vals,'thresholds':threshold,'proof':[], 'contradiction':bad[0], 'constraints':cons,'mandatory_RR':bad}
 while True:
  changed=False
  for j,c in enumerate(cons):
   known=sum(vals.get(v,0) for v in c['vars']);unknown=[v for v in c['vars'] if v not in vals];cap=1 if c['target']=='<=1' else c['target']
   # Each raw constraint is assumed valid at translates ell >= B.  This is
   # the relative threshold needed for all already forced occurrences.
   cut=max([0]+[threshold[e['phase']]-e['voltage'] for e in c['occurrences'] if e['phase'] in vals])
   if known>cap or (c['target']!='<=1' and known+len(unknown)<cap):
    return {'possible':False,'values':vals,'thresholds':threshold,'proof':proof,'contradiction':{'constraint':j,'known_sum':known,'unknown_occurrences':len(unknown),'relative_anchor_threshold':cut},'constraints':cons,'mandatory_RR':bad}
   forced=None
   if known==cap:forced=0
   elif c['target']!='<=1' and known+len(unknown)==cap:forced=1
   if forced is not None:
    for v in sorted(set(unknown)):
     occurrences=[e for e in c['occurrences'] if e['phase']==v]
     bound=min(cut+e['voltage'] for e in occurrences)
     vals[v]=forced;threshold[v]=bound
     proof.append({'constraint':j,'phase':v,'value':forced,'relative_phase_threshold':bound,'relative_anchor_threshold':cut,'known_sum_before_batch':known,'unknown_occurrences_before_batch':len(unknown)})
     changed=True
  if not changed:break
 return {'possible':True,'values':vals,'thresholds':threshold,'proof':proof,'constraints':cons,'mandatory_RR':bad}

def realize(z,values):
 return ''.join('R'*(4*values[i] if i in z['optional'] else k)+'L' for i,k in enumerate(z['ks']))

def verify_assignment(z,values,white):
 w=realize(z,values);E,d,h=event_word(w,h=z['heading'],p=z['position']);assert d==z['drift'] and h==z['heading']
 H=defaultdict(list)
 for e in E:
  q,k=quotient(e['p'],d);H[q].append((e['t']-len(w)*k,e['c']))
 for es in H.values():
  es.sort();assert all(a[1]!=b[1] for a,b in zip(es,es[1:]));assert not white or es[0][1]=='R'
 con,bad=constraints(z,white);assert not bad
 for c in con:
  v=sum(values[i] for i in c['vars'])
  assert v<=1 if c['target']=='<=1' else v==c['target']
 return {'period':len(w),'read_classes':len(H),'inputs':sum(es[0][1]=='L' for es in H.values()),'outputs':sum(es[-1][1]=='R' for es in H.values()),'word':w}

def serial(z):
 return {k:v for k,v in z.items() if k!='histories'}|{'maximal_candidate_histories':[{'class':q,'events':v} for q,v in sorted(z['histories'].items())]}

def main():
 R=Path(__file__).resolve().parent
 W={**WORDS,'M10':'RRRRLLLLRL','F80':json.loads((R/'prepared80_budget_falsifier_independent_confirmation.json').read_text())['word']}
 base={}
 for n,w in W.items():
  z=build(w);p=uniform_propagation(z,True);prepared=uniform_propagation(z,False);positive=verify_assignment(z,z['chosen'],False)
  assert prepared['possible'] and all(z['chosen'][i]==v for i,v in prepared['values'].items())
  if n=='S104':
   assert p['possible'] and len(p['values'])==32 and p['values']==z['chosen'] and realize(z,p['values'])==z['word'];verify_assignment(z,p['values'],True)
  else:assert not p['possible']
  base[n]={'geometry':serial(z),'WHITE_uniform_propagation':p,'prepared_propagation_summary':{'forced':len(prepared['values']),'unforced':len(z['optional'])-len(prepared['values'])},'literal_supplied_assignment':positive,
   'one_cell_word_period_range':[len(w)-4*sum(z['chosen'].values()),len(w)-4*sum(z['chosen'].values())+4*len(z['optional'])]}
 # Rotation, phase and full-period-power controls do not replace full d by a primitive vector.
 reps=[]
 for n,w in W.items():
  cases=[(h,q,0) for h in range(4) for q in [1,2,3,5]]+[(0,1,k) for k in sorted({1,len(w)//3,len(w)//2,len(w)-1})]
  for h,q,k in cases:
   ww=w[k:]+w[:k];z=build(ww*q,h);p=uniform_propagation(z,True);v=verify_assignment(z,z['chosen'],False)
   assert p['possible']==(n=='S104')
   if n=='S104':assert len(p['values'])==len(z['optional']) and p['values']==z['chosen']
   reps.append({'name':n,'heading':h,'power':q,'phase_cut':k,'C_transitions':len(z['ks']),'optional_laps':len(z['optional']),'WHITE_possible':p['possible'],'forced_count':len(p['values']),'positive_period':v['period'],'positive_inputs':v['inputs']})
 # The abstract ladder has no mandatory L between two forced R occurrences.
 ladder=json.loads((R/'disconnected_C_ladder_attempt_certificate.json').read_text());lw=''.join('R'*k+'L' for k in ladder['minimal_R_exponents']);lz=build(lw,1);lp=uniform_propagation(lz,False);assert not lp['possible'] and lp['mandatory_RR']
 # Fresh complete prepared P/Q normal-form replay, retaining passive bulk and XOR cap.
 from check_wave_roots_and_stock_scope import prepared
 full=[prepared('prepared_wave_five_band_normal_form.json','P1564','full_black_orbit_profiles'),prepared('three_standard_band_wave_normal_form.json','Q4352','full_black_profiles')]
 # Fresh actual finite S104 positive future, including every unread archive bit.
 from certify_joint_C_temporal_forests import D,first_mismatch,State
 B=set();pos=(0,0);h=0;start=10392
 for _ in range(start):
  c='L' if pos in B else 'R';B.symmetric_difference_update({pos});h=(h+(1 if c=='R' else -1))%4;pos=(pos[0]+D[h][0],pos[1]+D[h][1])
 sw=base['S104']['geometry']['word'];assert first_mismatch(State(frozenset(B),pos,h),sw) is None
 finite={'blank_time':start,'complete_BLACK':sorted(B),'head':pos,'heading':h,'word':sw,'exact_infinite_first_mismatch':None}
 deps=['check_extremal_read_coupling.py','check_all_cut_wave_interfaces.py','ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md','active_C_entry_exit_forests_certificate.json','prepared80_budget_falsifier_independent_confirmation.json','prepared_ten_boundary_winding_certificate.json','DISCONNECTED_C_LADDER_KINEMATIC_ATTEMPT.md','check_wave_roots_and_stock_scope.py']
 out={'status':'AUTHOR checked, independent audit pending','scope':'Exact fixed spatial C-transition traces, with independently indexed lap choices in every translate. Standard trace forces eventual standard104 from finite entry fields; the four supplied prepared traces cannot persist from a finite field. No arbitrary trace or global entry/classification result.',
  'base_controls':base,'representation_controls':reps,'ladder_forced_RR_obstruction':{'geometry':serial(lz),'proof':lp},'complete_P_Q_background_replays':full,'complete_finite_standard_positive':finite,
  'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in deps}}
 p=R/'C_trace_lap_ownership_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n')
 for n,b in base.items():
  p=b['WHITE_uniform_propagation'];print(n,'C',len(b['geometry']['ks']),'lapvars',len(b['geometry']['optional']),'WHITE',p['possible'],'forced',len(p['values']),'proof',len(p['proof']),'thresholds',min(p['thresholds'].values()),max(p['thresholds'].values()))
 print('PASS',len(reps),'representations, full backgrounds and finite positive',hashlib.sha256((R/'C_trace_lap_ownership_certificate.json').read_bytes()).hexdigest())
if __name__=='__main__':main()
