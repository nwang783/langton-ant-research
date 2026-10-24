from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/U1_shadow_ports_frozen_20261023_1315';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_U1_three_C_shadow_port_cut.json').read_text());C5={tuple(map(int,l.split()[:8]))for l in(B/'05_01_closure.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)}
upper={-1+4j,2j,3j};assert upper<G[7][3]
def score(a,pos,h):
 e=pos+rotation(G[a][0],h);dh=(h+G[a][1])%4;outs=sorted(G[a][4],key=xy)
 return max(2*H(e)+A[dh],*(2*H(pos+rotation(o,h))+w[f'w_{a}_{i}_{h}']for i,o in enumerate(outs)))
assert score(7,0j,1)==30
ports=[];queries=[];cores=[];first=[];wrong=[]
for z,black in G[7][2].items():
 if z.imag<1:continue
 goal=1-z.imag+(z.real-1)*1j;gh=1;val=score(7,goal,gh)
 assert rotation((1-1j)-goal,-gh)==z
 if(int(goal.real+goal.imag)+gh)%2:wrong.append(xy(z));continue
 assert int(z.real+z.imag)%2
 port=(*xy(z-1-1j),3);ports.append((port,xy(z),black))
 upperacts=[28+2*H(goal+rotation(u,gh))for u in upper];assert min(upperacts)>val
 first.append((port,sorted(v-val for v in upperacts)));assert sorted(v-val for v in upperacts)==[2,4,8]
 if not black:continue
 assert z in G[7][3]and z in{-1+2j,-1+4j,3j}
 for a in ids:
  h=(-G[a][1])%4;pos=-rotation(G[a][0],h);o=[o for o in G[a][4]if pos+rotation(o,h)==1-1j];assert len(o)==1;o=o[0]
  rel=rotation(goal-pos,-h);dh=(gh-h)%4;age=3+counts[a];key=(mp[a],mp[7],*xy(rel),dh,*xy(o),age)
  if counts[a]<2:assert key in C5;queries.append((xy(z),a,key))
  else:
   cor=2*H(pos)+A[h];assert cor==28>val;cores.append((xy(z),a,cor,val,30+cor-val))
assert len(queries)==18 and len(cores)==6 and len(ports)==8
AP={(tuple(q['earlier_A_pose']),tuple(q['bud_goal_cell']),bool(q['before_black']))for q in J['all8_forbidden_A_ports']};assert set(ports)==AP
AQ={(tuple(q['U_input']),c['predecessor'],tuple(c['query'])) for q in J['goal_input_cases'] for c in q['predecessor_cases']if c['reason']=='EXACT_COUNTED_EXCLUDED'};assert set(queries)==AQ
assert set(wrong)&set(map(xy,G[7][3]))=={(-1,1),(0,2)}
assert sorted(p for p,_,_ in ports)==[(-2,1,3),(-2,3,3),(-1,0,3),(-1,2,3),(0,1,3),(0,3,3),(1,0,3),(1,4,3)]
assert(-3,2,3)not in[p for p,_,_ in ports]
result=dict(status='PASS independent U1 three-C halfplane port barrier',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),ports=ports,queries=queries,core_cases=cores,first_boundary_upper_activation_margins=first,wrong_sector_input_cells=wrong,scope='Full unfunded U1 with I>=28, ONLY marked W boundaries exactly3C before U goal. Five bud-white cuts and three exact-origin counted/core funding cuts. Factor-first boundary separately funded by necessarily entry-old upper5 inputs. Such a clock may be skipped; forced q4 DC(-3,2,W) remains outside; no wholeU1 closure.')
P.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k!='queries'})
