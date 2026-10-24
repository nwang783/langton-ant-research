"""Exact arithmetic replay for a conditional directional max-plus potential."""
from pathlib import Path
import json,sys
MODEL,REL,OUT=sys.argv[1:];m=json.loads(Path(MODEL).read_text());assert m['status']=='sat';V=m['values'];ax,ay=m['direction'];dot=lambda z:ax*int(z.real)+ay*int(z.imag);rot=lambda p,h:complex(*p)*(-1j)**h;center=lambda h:complex(-1,1)*(-1j)**h;J=json.loads(Path('dcv_residual_core_resources.json').read_text());G=J['geometry'];K=J['kept_packet_types'];u=lambda a,k,h:V[f'u_{a}_{k}_{h}'];w=lambda a,k,h:V[f'w_{a}_{k}_{h}'];c=lambda h:V[f'c{h}'];checks=0
for a in K:
 e=G[a]['endpoint'];dh=e[2]
 for h in range(4):
  cy=dot(center(h));old=[c(h)]+[2*dot(rot(p,h))-cy+u(a,k,h)for k,p in enumerate(G[a]['inputs'])];new=[dot(2*rot(e[:2],h)+center((h+dh)%4)-center(h))+c((h+dh)%4)]+[2*dot(rot(p,h))-cy+w(a,k,h)for k,p in enumerate(G[a]['outputs'])];assert all(z<=max(old)for z in new);checks+=len(new)
P={tuple(map(int,l.split()[:7]))for l in Path('dcv_protected_patch2_kernel.tsv').read_text().splitlines()};F={tuple(map(int,l.split()))for l in Path(REL).read_text().splitlines()};bad=[];signed=[];base=[]
for e in J['transfer_edges']:
 a,k=e['producer'];b,j=e['consumer'];q=G[a]['outputs'][k]
 for x,y,hr in e['poses']:
  v=[h for h in range(4)if u(b,j,(h+hr)%4)>w(a,k,h)]
  if not v:continue
  row=(a,b,x,y,hr,*q);r={'tuple':row,'violating_global_headings':v};(base if row in P else signed if row in F else bad).append(r)
controls=0
for l in Path('dcv_packet_transfers_fuel20.log').read_text().splitlines():
 if not l.startswith('EDGE '):continue
 a,x,y,b,xx,yy,hr=map(int,l.split()[1:])
 if a not in K or b not in K:continue
 k=G[a]['outputs'].index([x,y]);j=G[b]['inputs'].index([xx,yy]);assert all(u(b,j,(h+hr)%4)<=w(a,k,h)for h in range(4));controls+=1
out={'status':'CONDITIONAL ONLY: supplied relation audit status and remaining exclusions must be discharged','direction':[ax,ay],'packet_inequalities':checks,'observed_transfer_controls':controls,'unproved_bad_transfers':bad,'given_relation_exclusions':signed,'original_protected_exclusions':base,'integer_weights':V};Path(OUT).write_text(json.dumps(out,indent=2));print({'direction':[ax,ay],'remaining':len(bad),'given_relation_exclusions':len(signed),'original_protected':len(base)})
