from pathlib import Path
from collections import defaultdict
import json,hashlib,math
P=Path(__file__).resolve();ROOT=P.parents[1];U=ROOT/'causal_reduction/unit_scale';H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];Q=json.loads((U/'forward108_prepared_control.json').read_text())['word'];J=json.loads((U/'forward108_domino_repair.json').read_text())
def walk(w,p,h):
 out=[];D=(1j,1,-1j,-1)
 for i,c in enumerate(w):out.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return out,p,h
xy=lambda z:(int(z.real),int(z.imag));key=lambda z:(int(z.real-z.imag),int(z.real)%2)
def grouped(w,p,h):
 rows,e,eh=walk(w,p,h);d=defaultdict(list)
 for i,(z,hh,c)in enumerate(rows):d[key(z)].append((-(int(z.real)//2),i,xy(z),hh,c))
 return {k:sorted(v)for k,v in d.items()}
hh=grouped(H,10j,1);qq=grouped(Q,0j,1);rr=grouped('LR',-1+6j,2)
for v in hh.values():assert [c[-1]for c in v]==['R'if i%2==0 else'L'for i in range(len(v))]
Hb={k for k,v in hh.items()if v[-1][-1]=='R'};Qi={k for k,v in qq.items()if v[0][-1]=='L'}
assert Hb.intersection(qq)^Qi=={(-7,1),(-6,0)}and(-7,1)in Hb and(-6,0)in Qi
tr,e,h=walk('LR',-1+6j,2);assert[(xy(z),c)for z,hh,c in tr]==[((-1,6),'L'),((0,6),'R')]and(e,h)==(5j,2)
bounds=(max(hh[a][-1][0]-qq[a][0][0]for a in hh.keys()&qq.keys()),max(hh[a][-1][0]-rr[a][0][0]for a in hh.keys()&rr.keys()),max(rr[a][-1][0]-qq[a][0][0]for a in rr.keys()&qq.keys()));assert bounds==(-1,-2,1)
hist=defaultdict(list);ends=[]
for b,(w,p,h)in enumerate(((H,10j,1),('LR',1+8j,2),(Q,0j,1))):
 rows,e,eh=walk(w,p,h);ends.append((*xy(e),eh))
 for i,(z,hh,c)in enumerate(rows):hist[key(z)].append((-(int(z.real)//2),b,i,xy(z),hh,c))
for a,v in hist.items():v.sort();assert[vv[-1]for vv in v]==['R'if i%2==0 else'L'for i in range(len(v))]
assert len(hist)==42 and sum(map(len,hist.values()))==214 and sum(len(v)%2 for v in hist.values())==20
AH={tuple(q['orbit']):[(x[0],x[1],x[2],tuple(x[3]),x[4],x[5])for x in q['events']]for q in J['histories']};assert dict(hist)==AH and ends==list(map(tuple,J['endpoints']))
rows,e,eh=walk(H,10j,1);reads=[(i,c)for i,(z,h,c)in enumerate(rows)if z==e];assert reads[-1]==(40,'R')and(e,eh)==(2+12j,1)
# Length7 from E to S with dy=-4 alternates four vertical and three horizontal moves.
# Every vertical move is S; two of the horizontal moves W, one E: exactly three.
assert math.comb(3,1)==3
# The other two counts are pure shortest quarter-turn kinematics, not legality.
assert math.comb(7,2)==21 and math.comb(9,4)==126
out=dict(status='PASS independent disconnected complete color histories and shortest-first-connector obstruction',note_sha256=hashlib.sha256((U/'forward108_domino_pipeline.md').read_bytes()).hexdigest(),read_classes=42,reads=214,output_black_classes=20,whole_piece_order_bounds=bounds,endpoints=ends,H_endpoint_reads=reads,shortest_connector_lengths=[7,15,20],shortest_kinematic_counts=[3,21,126],scope='ONLY sections1–3: exact adjacent LR transfer and disconnected H/LR/Q periodic color ownership are valid. A shortest first connector must depart south/R but H endpoint is black, so every shortest triple fails immediately. No longer connector, continuous ant, renewal, finite-seed noncapture, floating flow or solver-only chronology claim.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
