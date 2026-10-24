#!/usr/bin/env python3
"""Complete uncapped handoff domains and conditional cycle-span identities."""
import json,hashlib
from pathlib import Path
from certify_active_C_entry_exit_forests import analyze
R=Path(__file__).resolve().parent

def handoffs(z):
 A={tuple(h['class']):h['first_time'] for h in z['C_face_histories']};B={tuple(h['class']):h['last_time'] for h in z['C_face_histories']};P=z['period']
 F={tuple(e['source']):e for e in z['first_entry_edges']};FC={tuple(v) for c in z['first_entry_cycles'] for v in c['vertices']};FW={tuple(v) for c in z['WHITE_first_entry_cycles'] for v in c['vertices']};BC={tuple(v) for c in z['last_exit_cycles'] for v in c['vertices']};H={e['t']:hh for hh in z['read_histories'] for e in hh['reads']};out=[]
 for b in z['last_exit_edges']:
  u=tuple(b['source']);v=tuple(b['target']);nu=b['voltage']
  if A[v]+nu*P!=B[u]+1:continue
  f=F[v];assert tuple(f['target'])==u and f['voltage']==-nu and f['L_phase']==b['L_phase']
  rs=H[b['L_phase']]['reads'];white=f['WHITE_first'];n=len(rs);L=next(r for r in rs if r['t']==b['L_phase']);h=L['hi'];turns=''.join(r['c'] for r in rs);heads=[r['hi'] for r in rs]
  if white:
   assert turns in ['RL','RLR'] and heads[:2]==[h,h]
  else:assert turns in ['L','LR'] and heads[0]==h
  if rs[-1]['c']=='R':assert heads[-1]==(h+2)%4
  su=B[u]-A[u];sv=B[v]-A[v]
  assert f['clock_gap']==su+1 and b['clock_gap']==sv+1
  if v in FC:assert su<P
  if u in BC:assert sv<P
  out.append({'source':u,'target':v,'voltage':nu,'L_phase':b['L_phase'],'complete_read_class':H[b['L_phase']]['class'],
   'complete_history':rs,'first_is_WHITE':white,'permanent_output':rs[-1]['c']=='R','source_span':su,'target_span':sv,
   'first_edge_gap':f['clock_gap'],'last_edge_gap':b['clock_gap'],'on_full_first_cycle':v in FC,'on_WHITE_first_cycle':v in FW,'on_last_cycle':u in BC})
 return out

def main():
 Z=json.loads((R/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls'];base={n:handoffs(z) for n,z in Z.items()};s=base['S104'];assert len(s)==1 and s[0]['L_phase']==26 and s[0]['on_WHITE_first_cycle'] and s[0]['on_last_cycle'];assert ''.join(e['c'] for e in s[0]['complete_history'])=='RLR';assert (s[0]['source_span'],s[0]['target_span'])==(13,101)
 assert not base['M10'];assert len(base['F80'])==2 and not any(e['on_WHITE_first_cycle'] for e in base['F80'])
 reps=[]
 for n in ['S104','M10','F80']:
  w=Z[n]['word']
  for h in range(4):
   for q in [1,2,3,5]:
    v=handoffs(analyze(w*q,h));assert len(v)==len(base[n])*q;reps.append({'name':n,'heading':h,'power':q,'count':len(v)})
 out={'status':'AUTHOR checked, independent audit pending','scope':'Exact conditional handoff domains and spans only. No existence of any handoff or shared-cycle handoff is proved.',
  'base_controls':base,'representation_controls':reps,'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md','active_C_entry_exit_forests_certificate.json','JOINT_C_FIRST_LAST_TEMPORAL_FORESTS.md']}}
 p=R/'C_literal_handoff_domains_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print({n:len(v) for n,v in base.items()});print('PASS',len(reps),hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
