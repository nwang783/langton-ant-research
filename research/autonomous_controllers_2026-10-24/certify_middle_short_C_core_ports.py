#!/usr/bin/env python3
"""Exact four-channel / three-lifetime boundary of the signed three-C core."""
from pathlib import Path
import json,hashlib
from certify_active_C_entry_exit_forests import active_C
from check_extremal_read_coupling import D
from partial_drift31_graph import quotient31
R=Path(__file__).resolve().parent

def extract(H):
 H={int(t):h for t,h in H.items()};nodes={(t,r) for t,hs in H.items() for r in range(len(hs))}
 core=set()
 for t,r in nodes:
  c=active_C((-t,0),H[t][r]);T=3*c[1]-c[0]
  if T in [1,3,5]:core.add((t,r))
 assert len(core)==24 and sum(r%2==0 for t,r in core)==14
 out={};inc={}
 for t,hs in H.items():
  p=(-t,0)
  for d in range(4):
   src=[r for r,h in enumerate(hs) if (h+(1 if r%2==0 else-1))%4==d]
   q,k=quotient31((p[0]+D[d][0],p[1]+D[d][1]));tt=-q[0]
   if tt not in H:continue
   dst=[r for r,h in enumerate(H[tt]) if h==d];assert len(src)==len(dst)
   for a,b in zip(src,dst):out[t,a]=((tt,b),k);inc[tt,b]=((t,a),k)
 starts=sorted(v for v in core if v not in inc or inc[v][0] not in core);assert set(starts)=={(7,2),(4,3),(7,1),(5,3)}
 chains=[];seen=set()
 for s in starts:
  v=s;k=0;ch=[]
  while True:
   assert v not in seen;seen.add(v);t,r=v;p=(-t+3*k,k);h=H[t][r];ch.append({'node':v,'lift':k,'position':p,'heading':h,'turn':'R' if r%2==0 else'L','C_face':active_C(p,h)})
   assert v in out
   u,dk=out[v]
   if u not in core:break
   v=u;k+=dk
  before,nu=inc[s];after,dnu=out[v]
  assert before not in core and before[1]%2==1 and v[1]%2==1
  chains.append({'start':s,'events':ch,'word':''.join(e['turn']for e in ch),'incoming_outside_node':before,'incoming_edge_voltage':nu,'outgoing_outside_node':after,'outgoing_edge_voltage':dnu,'last_lift':k})
 assert seen==core and sorted(len(c['events'])for c in chains)==[1,2,9,12]
 imports=[];exports=[];internal=[];permanent=[]
 for t,hs in H.items():
  for r in range(0,len(hs)-1,2):
   src=(t,r);dst=(t,r+1);row={'R_node':src,'L_node':dst,'same_physical_position':(-t,0),'R_heading':hs[r],'L_heading':hs[r+1]}
   if src in core and dst in core:internal.append(row)
   elif src in core:exports.append(row)
   elif dst in core:imports.append(row)
  if len(hs)%2 and(t,len(hs)-1) in core:permanent.append((t,len(hs)-1))
 assert len(internal)==9 and len(exports)==2 and len(imports)==1 and permanent==[(0,0),(1,0),(2,0)]
 assert [x['R_node'] for x in exports]==[(6,2),(7,2)]
 assert imports[0]['R_node'][0]==8 and imports[0]['L_node'][1] in [3,5]
 # The X->Y exterior interval is literally one L at T7 rank3.
 x=next(c for c in chains if c['start']==(7,2));y=next(c for c in chains if c['start']==(4,3));assert x['outgoing_outside_node']==(7,3) and y['incoming_outside_node']==(7,3)
 assert out[7,3][0]==(4,3)
 return {'T8_word':H[8],'all24_core_events':sorted(core),'four_actual_core_channels':chains,'nine_internal_lifetimes':internal,'two_exported_lifetimes':exports,'one_imported_lifetime':imports,'three_core_permanent_outputs':permanent,
  'core_read_counts':{'R':14,'L':10},'fixed_exterior_channel':{'node':[7,3],'word':'L','R_owner':[7,2],'age':12},
  'remaining_exterior_permanent_outputs':'T6,T7,6c+1,6a+2,6a+4 (five full odd classes)',
  'cyclic_core_order':'Y,W,Z,X,Y' if H[8].index(0,2)==3 else 'Y,Z,W,X,Y',
  'warning':'Four known core channels are not a finite state for the unbounded exterior. No lifetimes are initial BLACK inputs.'}

def main():
 z=json.loads((R/'middle_short_coincident_C_cycles_certificate.json').read_text());out=[extract(H)for H in z['six_open_T0_through_T10_interfaces']]
 sig=lambda a:json.dumps({k:v for k,v in a.items() if k!='warning'},sort_keys=True)
 assert len({sig(a)for a in out})==2
 result={'status':'AUTHOR checked, independent audit pending','scope':'Exact necessary four-channel interface of the signed three-C core, with all higher fields and routes unrestricted; not a controller or proof of exterior impossibility.',
  'six_named_interface_checks':out,'two_core_types':list({sig(a):a for a in out}.values()),
  'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['MIDDLE_SHORT_COINCIDENT_FIRST_LAST_C_CORE.md','middle_short_coincident_C_cycles_certificate.json','partial_drift31_graph.py','ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md']}}
 p=R/'middle_short_C_core_ports_certificate.json';p.write_text(json.dumps(result,indent=2)+'\n');print('PASS',len(out),'interfaces,2 core types',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
