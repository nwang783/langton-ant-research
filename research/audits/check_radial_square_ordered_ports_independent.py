from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'RADIAL_SQUARE_ORDERED_PORTS_MANIFEST.json';qa=D/'RADIAL_SQUARE_PORT_TERMINOLOGY_ADDENDUM.json';assert sha(mf)=='a7de97d9ee6b3b73447368ac8d3ed872a4879f64e1b36509c6bc44f9fb06b15a'and sha(qa)=='13b706122185ea7578899d570d3086d4c912b7daba6e74b05c7f156129bacf65';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(D/f)==h
for f,h in json.loads(qa.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'RADIAL_SQUARE_ORDERED_PORTS_CHECKED.json').read_text());C=[0j,1+0j,1+1j,1j];V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)];B=set();ports=[];ct=Counter();words={q:''for q in C};full=[]
# Reconstruct the prescribed finite protocol from its analytic construction.
for sweep in range(3):
 for v in range(4):
  ports.extend([v,v]);r=(v+1)%4
  if sweep==0 and v==0:ports.extend([(r+2)%4,(r+1)%4,r,(r-1)%4]*15)
  ports.append(r)
assert ports==J['entry_ports']and len(ports)==96 and Counter(ports)==dict.fromkeys(range(4),24)
for index,(entry,au)in enumerate(zip(ports,J['episodes'])):
 mask=sum(1<<C.index(q)for q in B);assert mask==au['before'];p=C[entry];h=[0,3,2,1][entry];seq=[]
 while p in C:
  i=C.index(p);c='L'if p in B else'R';typ=('outer_L'if not seq else'inner_L')if c=='L'else('entry_R'if not seq else'exit_R');seq.append([i,c,typ]);ct[i,typ]+=1;words[p]+=c
  B.symmetric_difference_update({p});hh=(h+(1 if c=='R'else-1))%4;pp=p+V[hh];full.append(dict(episode=index,cell=xy(p),heading=h,turn=c,next=xy(pp)))
  if typ=='inner_L':assert pp in C
  if typ=='outer_L':assert pp not in C
  p,h=pp,hh
 assert seq==au['reads']and sum(1<<C.index(q)for q in B)==au['after']and[xy(p),h]==au['exit_pose']and entry==au['entry']
assert not B and len(full)==288 and all(w=='RL'*36 for w in words.values())
A=lambda x,y:F(1,2)**(abs(x)+abs(y))
for i,q in enumerate(C):
 counts={k:ct[i,k]for k in ['inner_L','outer_L','entry_R','exit_R']};assert counts==dict(inner_L=30,outer_L=6,entry_R=18,exit_R=18)==J['per_cell_counts'][i]['counts']
 x,y=map(int,(q.real,q.imag));faces=[(x,y),(x-1,y),(x-1,y-1),(x,y-1)];a=[A(*f)for f in faces];turns=[8*(3*a[k]+a[(k-1)%4]+a[(k+1)%4]-a[(k+2)%4])for k in range(4)];j=faces.index((0,0));assert turns[j]==30 and turns[(j+2)%4]==6 and turns[(j+1)%4]==turns[(j+3)%4]==18
O=dict(status='PASS exact all-WHITE-start ordered local port model only, NOT an actual full-board ant construction',manifest=sha(mf),mandatory_terminology_addendum=sha(qa),script=sha(S),ports=ports,external_entries=96,patch_reads=288,all_local_words='(RL)^36',full_patch_read_trace=full,analytic_review=[
'The three4-vertex preparation/cleanup sweeps and fifteen4-entry inner circulations are reconstructed directly. Exact local colors and headings persist between all96 externally selected entries; every cell has36 alternatingRL pairs and returnsWHITE. Full scaled32 radial corner counts30/6/18/18 match independently from the face-weight formula.',
'The automaton has16 colorstates and64 state-entry transitions, as explicitly qualified. Its selected port protocol is externally controlled: no causal exterior routes, times, fields, finite initial seed, larger-box gluing or autonomous repetition are supplied.',
'This disproves only an exclusion based on this central square local alternation and allWHITE initialization. OuterL exits evade the pureinnerL BLACK-root condition; that signed last-exit theorem remains valid. The earlier genuine blank component does not realize these96 outside connectors or the whole infinite summable witness.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
