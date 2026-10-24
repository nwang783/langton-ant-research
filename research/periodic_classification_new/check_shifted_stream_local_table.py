#!/usr/bin/env python3
"""Literal local controls for the shifted-stream proof. No theorem module imported.
This checks all complete white histories surviving the signed cap-three
same-first/third-heading exclusion. It is not an independent audit.
"""
from itertools import product
from pathlib import Path
import json
rows=[]
for parity in range(2):
 axis=1-parity
 histories=[()]
 for n in range(1,4):
  for hs in product((axis,axis+2),repeat=n):
   if n==3 and hs[0]==hs[2]:continue
   histories.append(hs)
 assert len(histories)==11
 for hs in histories:
  incoming=[0]*4;outgoing=[0]*4
  for i,h in enumerate(hs):
   incoming[h]+=1;outgoing[(h+(1 if i%2==0 else -1))%4]+=1
  N=outgoing[0]+incoming[2];E=outgoing[1]+incoming[3]
  S=outgoing[2]+incoming[0];W=outgoing[3]+incoming[1]
  if parity==0:
   nw=0;ne=N;se=ne-E;sw=se+S
   assert sw-nw==W
   H=[nw+1,ne,se+1,sw]
  else:
   nw=0;ne=-N;se=ne+E;sw=se-S
   assert nw-sw==W
   H=[nw,ne+1,se,sw+1]
  H=[v-min(H) for v in H];mx=max(H)
  assert H.count(mx)>=2
  assert all(max(H[j] for j in range(4) if j!=omit)==mx for omit in range(4))
  if len(hs)==0:assert sorted(H)==[0,0,1,1] and H[0]==H[2] and H[1]==H[3]
  elif len(hs)==1 or len(hs)==3:assert sorted(H)==[0,1,1,1]
  elif len(hs)==2:assert sorted(H)==[0,0,1,1] and H[0]!=H[2]
  # Horizontal maximum pair gives vertical odd edges/horizontal doubled matching.
  if H[0]==H[1]==mx and H[2]<mx and H[3]<mx or H[2]==H[3]==mx and H[0]<mx and H[1]<mx:
   assert len(hs)==2 and N==S==1 and sorted((E,W))==[0,2]
  rows.append(dict(parity=parity,incoming_headings=list(hs),ports_NESW=[N,E,S,W],shifted_NW_NE_SE_SW=H))
# East and west dominoes, complete white R then L at each endpoint.
dominoes=[]
for e in (1,3):
 for turn in (1,-1):
  incoming=(e-turn)%4;outgoing=(e+turn)%4
  assert incoming%2==0 and outgoing==(incoming+2)%4
  # Incoming north arrives from the south, then outgoing south returns south.
  side=-1 if incoming==0 else 1
  assert (1 if outgoing==0 else -1)==side
  dominoes.append(dict(edge_heading=e,turns=[turn,turn],incoming=incoming,outgoing=outgoing,side=side))
res=dict(status='PASS_LOCAL_CONTROLS_ONLY',oriented_histories=len(rows),geometric_states_each_parity=[len({tuple(r['ports_NESW']) for r in rows if r['parity']==p}) for p in (0,1)],rows=rows,dominoes=dominoes)
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k not in ('rows','dominoes')}))
