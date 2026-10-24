#!/usr/bin/env python3
"""Exact negative control to an oriented-record geometric shortcut, not an ant path."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
G=json.loads((ROOT/'chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
D=json.loads((ROOT/'chronology_dcuv/literal_factor_dfa_k5.json').read_text())
w=[5,0,1,4,7,1,5,4]; H0=[28,26,28,14]; A=[0,22,20,10]
def rot(z,h):
 x,y=z;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def value(p,h,r):return 2*sum(rot(p,r))+A[(h+r)%4]
p=(0,0);h=0;H=H0[:];events=[]
for n,a in enumerate(w*20):
 oldp=p;oldh=h; dx,dy=rot(G[a]['endpoint'][:2],h);p=(p[0]+dx,p[1]+dy);h=(h+G[a]['endpoint'][2])%4
 v=[value(p,h,r) for r in range(4)];records=[r for r in range(4) if v[r]>H[r]]
 assert all(a in (4,7) and (oldh+r)%4==1 for r in records)
 events.append(dict(step=n,packet=a,pose=[*oldp,oldh],next_pose=[*p,h],records=records,oldH=H[:],new_values=v))
 H=[max(x,y) for x,y in zip(H,v)]
assert p==(20,-20) and h==0
# Whole-period cycle establishes legality of every window, including wrap-around.
c=D['initial_class'];seen={};period=0
while c not in seen:
 seen[c]=period
 for a in w:
  c=D['transitions'][c][D['keep'].index(a)]
  assert c>=0
 period+=1
# Independent direct literal replay, retaining the actual required first color.
p=0j;heading=1j;initial={};parity=set();first=None;rawstep=0
for n,a in enumerate(w*3):
 for t in G[a]['word']:
  required=(t=='L');init_needed=required^(p in parity)
  if p in initial and initial[p]!=init_needed:
   first=dict(packet_index=n,packet=a,raw_step=rawstep,cell=[int(p.real),int(p.imag)],initial_color_already_required=initial[p],initial_color_now_required=init_needed)
   break
  initial[p]=init_needed
  if p in parity:parity.remove(p)
  else:parity.add(p)
  heading*=1j if t=='L' else -1j;p+=heading;rawstep+=1
 if first:break
assert first
out=dict(status='GEOMETRY_PLUS_K5_COUNTERCONTROL_NOT_PHYSICAL',scope='Only V phase1 and U phase1 strict records allowed; eleven signed event exclusions do not imply confinement in this geometric/window relaxation.',word=w,drift=[1,-1],initial_H=H0,dfa_transient_periods=seen[c],dfa_cycle_periods=period-seen[c],literal_first_conflict=first,twenty_period_records=events)
path=ROOT/'chronology_dcuv/oriented_record_geometry_dfa5_east_pump_replay.json';path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='twenty_period_records'},indent=2))
