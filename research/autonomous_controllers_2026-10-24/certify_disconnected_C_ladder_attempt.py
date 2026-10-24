#!/usr/bin/env python3
"""One explicit planar nonbacktracking C walk, with a six-leaf color cover."""
from pathlib import Path
from collections import defaultdict
from itertools import product
import json,hashlib
from certify_active_C_entry_exit_forests import active_C
from check_extremal_read_coupling import event_word
R=Path(__file__).resolve().parent
D=[(0,1),(1,0),(0,-1),(-1,0)]
C=[(0,0),(1,0),(1,-1),(0,-1),(0,0),(0,1),(1,1),(1,2),(0,2),(0,1),(0,0),(1,0),(1,1),(1,2),(0,2),(0,1),(1,1),(1,0)]
def physical(c):return(c[0]-c[1],c[0]+c[1]-1)

def main():
 assert len(C)==18 and C[-1]==(1,0)
 for a,b in zip(C,C[1:]):assert abs(a[0]-b[0])+abs(a[1]-b[1])==1
 # Also retain the seam's previous and next C vertex.
 ext=[(C[-2][0]-1,C[-2][1])]+C+[(C[1][0]+1,C[1][1])]
 assert all(a!=c for a,b,c in zip(ext,ext[1:],ext[2:]))
 H=defaultdict(list);N=17
 for i,(x,y) in enumerate(C[:-1]):H[y].append((i-N*x,i))
 forest=[];G=defaultdict(set)
 for y,es in sorted(H.items()):
  (fa,i),(la,j)=min(es),max(es);prev=C[(i-1)%N];cur=C[i];nxt=C[j+1];last=C[j]
  fp=(prev[1],prev[0]-cur[0]-(i==0));lp=(nxt[1],nxt[0]-last[0])
  forest.append({'row':y,'first_C_index':fa,'last_C_index':la,'first_occurrence_phase':i,'last_occurrence_phase':j,'first_parent_row':fp[0],'first_parent_voltage':fp[1],'last_successor_row':lp[0],'last_successor_voltage':lp[1]})
  G[y].add(fp[0]);G[fp[0]].add(y);G[y].add(lp[0]);G[lp[0]].add(y)
 seen=set();components=[]
 for y in sorted(G):
  if y in seen:continue
  ss=[y];seen.add(y);co=[]
  while ss:
   u=ss.pop();co.append(u)
   for v in G[u]-seen:seen.add(v);ss.append(v)
  components.append(sorted(co))
 assert components==[[-1,0],[1,2]]
 p=(1,0);h=1;ks=[]
 for a,b in zip(C,C[1:]):
  aa,bb=physical(a),physical(b);assert active_C(p,h)==aa
  q=(max(aa[0],bb[0]),max(aa[1],bb[1]));k=0
  while p!=q:
   h=(h+1)%4;p=(p[0]+D[h][0],p[1]+D[h][1]);k+=1;assert k<=3
  assert k!=3;ks.append(k)
  h=(h-1)%4;p=(p[0]+D[h][0],p[1]+D[h][1]);assert active_C(p,h)==bb
 assert (p,h)==((2,1),1)
 opt=[i for i,k in enumerate(ks) if k==0];assert opt==[0,6,7,8,10,11,13,14,15]
 leaves=[]
 def rec(i,p,h,seen,ev,bits):
  assert i<len(ks),'unexpected complete legal expansion'
  for k in ([0,4] if ks[i]==0 else [ks[i]]):
   bb=bits+([k//4] if ks[i]==0 else []);ee=ev[:];ss=seen.copy();pp=p;hh=h;bad=None
   for turn in 'R'*k+'L':
    e={'time':len(ee),'position':pp,'heading':hh,'turn':turn,'C_step_block':i}
    if pp in ss and ss[pp]['turn']==turn:bad=(ss[pp],e);break
    ss[pp]=e;ee.append(e);hh=(hh+(1 if turn=='R' else -1))%4;pp=(pp[0]+D[hh][0],pp[1]+D[hh][1])
   if bad:
    first={}
    for e in ee:first.setdefault(e['position'],e['turn'])
    seed={p for p,c in first.items() if c=='L'};field=set(seed)
    for e in ee:
     assert ('L' if e['position'] in field else 'R')==e['turn'];field.symmetric_difference_update({e['position']})
    assert ('L' if bad[1]['position'] in field else 'R')!=bad[1]['turn']
    leaves.append({'bit_prefix':bb,'block_of_failure':i,'covered_full_choices':2**(len(opt)-len(bb)),
     'all_legal_prefix_reads':ee,'consecutive_same_turn_witness':bad,'full_minimal_initial_BLACK':sorted(seed),'full_BLACK_at_failure':sorted(field),
     'head_at_failure':pp,'heading_at_failure':hh,'actual_required_turn':'L' if pp in field else 'R'})
   else:rec(i+1,pp,hh,ss,ee,bb)
 rec(0,(1,0),1,{},[],[])
 assert [a['bit_prefix'] for a in leaves]==[[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1],[1]]
 assert sum(a['covered_full_choices'] for a in leaves)==512
 # Independent coverage/geometry pass over the fixed local-lap family, not a period scan.
 for bits in product([0,1],repeat=9):
  matches=[a for a in leaves if list(bits[:len(a['bit_prefix'])])==a['bit_prefix']];assert len(matches)==1
  ex=ks[:]
  for i,b in zip(opt,bits):ex[i]=4*b
  w=''.join('R'*k+'L' for k in ex);E,d,hh=event_word(w,h=1,p=(1,0));assert d==(1,1) and hh==1
  at=0
  for j,k in enumerate(ex):
   assert all(active_C(E[t]['p'],E[t]['hi'])==physical(C[j]) for t in range(at,at+k+1));at+=k+1
  bad=matches[0]['consecutive_same_turn_witness'][1];e=E[bad['time']]
  assert e['p']==bad['position'] and e['c']==bad['turn']
 out={'status':'AUTHOR checked, independent audit pending','scope':'The C walk is planar/nonbacktracking but NOT an actual ant control. All local-lap expansions of this one specified geometry fail finite color compatibility. No general connectivity theorem or controller exclusion.',
  'C_lattice_path':C,'physical_C_faces':[physical(c) for c in C],'C_transition_period':17,'ant_periods_are_not_17':[30,34,38,42,46,50,54,58,62,66],
  'full_spatial_drift':[1,1],'initial_head':[1,0],'initial_heading':1,'minimal_R_exponents':ks,'optional_four_R_blocks':opt,
  'abstract_first_last_forests':forest,'abstract_union_components':components,'six_leaf_complete_color_cover':leaves,
  'dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['certify_active_C_entry_exit_forests.py','check_extremal_read_coupling.py']}}
 p=R/'disconnected_C_ladder_attempt_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS6 leaves cover512 fixed-geometry expansions',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
