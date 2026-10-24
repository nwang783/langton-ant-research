"""Exact integer replay of a CONDITIONAL max-plus confinement certificate.
Its transfer exclusions are research targets, NOT established ant invariants.
"""
import json,re,math,sys
from pathlib import Path
MODEL=sys.argv[1]if len(sys.argv)>1 else 'dcv_packet_maxplus_observed.json'
OUT=sys.argv[2]if len(sys.argv)>2 else 'dcv_conditional_confinement.json'
J=json.load(open('dcv_residual_core_resources.json'));G=J['geometry'];K=J['kept_packet_types'];model=json.load(open(MODEL))['model']
V=json.load(open(MODEL))['values']
rot=lambda p,h:complex(*p)*(-1j)**h;center=lambda h:complex(-1,1)*(-1j)**h
u=lambda a,k,h:V[f'u_{a}_{k}_{h}'];w=lambda a,k,h:V[f'w_{a}_{k}_{h}'];c=lambda h:V[f'c{h}'];checked=0
for a in K:
 e=G[a]['endpoint'];dh=e[2]
 for h in range(4):
  cy=int(center(h).imag);old=[c(h)]+[2*int(rot(p,h).imag)-cy+u(a,k,h)for k,p in enumerate(G[a]['inputs'])];bound=max(old)
  endpoint=2*rot(e[:2],h)+center((h+dh)%4)-center(h)
  new=[int(endpoint.imag)+c((h+dh)%4)]+[2*int(rot(p,h).imag)-cy+w(a,k,h)for k,p in enumerate(G[a]['outputs'])]
  assert all(t<=bound for t in new);checked+=len(new)
P={tuple(map(int,l.split()[:7]))for l in open('dcv_protected_patch2_kernel.tsv')};bad=[];extra=[]
for e in J['transfer_edges']:
 a,k=e['producer'];b,j=e['consumer'];q=G[a]['outputs'][k]
 for x,y,hr in e['poses']:
  violations=[h for h in range(4)if u(b,j,(h+hr)%4)>w(a,k,h)]
  if violations:
   rec={'source_packet':a,'source_output':q,'target_packet':b,'target_input':G[b]['inputs'][j],'target_pose':[x,y,hr],'violating_global_headings':violations}
   if (a,b,x,y,hr,*q)in P:extra.append(rec)
   else:bad.append(rec)
# Every observed transfer must obey the potential in all four orientations.
observed=0
for line in open('dcv_packet_transfers_fuel20.log'):
 if not line.startswith('EDGE '):continue
 a,x,y,b,xx,yy,hr=map(int,line.split()[1:])
 if a not in K or b not in K:continue
 k=G[a]['outputs'].index([x,y]);j=G[b]['inputs'].index([xx,yy]);assert all(u(b,j,(h+hr)%4)<=w(a,k,h)for h in range(4));observed+=1
I=max(v for k,v in V.items()if k.startswith('u_'));coreoffs=[int(center(h).imag)+c(h)for h in range(4)];initial=max(I,*coreoffs);mout=min(I,*(v for k,v in V.items()if k.startswith('w_')))
result={'status':'CONDITIONAL ONLY','integer_weights':V,'packet_output_checks':checked,'observed_transfer_checks':observed,'initial_token_weight':I,'initial_max_offset':initial,'core_position_margin':math.ceil((initial-min(coreoffs))/2),'residual_black_margin':math.ceil((initial-mout)/2),'protected_relation_excludes':extra,'unproved_bad_transfers':bad}
Path(OUT).write_text(json.dumps(result,indent=2));print({k:v for k,v in result.items()if k not in ['integer_weights','protected_relation_excludes','unproved_bad_transfers']});print('unproved bad transfers',len(bad),'protected exclusions',len(extra))
