#!/usr/bin/env python3
"""Author certificate controls, not a full finite-control/cap compiler."""
import hashlib,json,pathlib
from directed_palette_front import literal_trace,DIRECTIONS
HERE=pathlib.Path(__file__).resolve().parent
standard=json.loads((HERE.parent/'recovered_bundle/ant_global/root/standard.json').read_text())
H=standard['word'];h0=standard['heading'];L=len(H)
rows,drift,hh=literal_trace(H,h0)
assert hh==h0 and drift==(-2,-2) and L==104
ell=lambda q:-26*(q[0]+q[1])
phi=[i-ell(q) for i,(q,b) in enumerate(rows)]
x=y=0;h=h0;edges=[]
for i,c in enumerate(H):
 next_h=(h+(1 if c=='R' else -1))%4;dx,dy=DIRECTIONS[next_h]
 gain=ell((dx,dy))+phi[(i+1)%L]-phi[i]
 assert gain==1
 edges.append(dict(source=i,target=(i+1)%L,word=c,heading=h,
                   final_heading=next_h,drift=[dx,dy],corrected_gain=gain))
 x+=dx;y+=dy;h=next_h
R=max(phi)-min(phi);K=R
assert R==279
assert set(tuple(e['drift']) for e in edges)==set(DIRECTIONS)
# One cannot choose a strict positive functional for all four raw unit moves;
# the supplied cyclic control potential supplies progress nevertheless.
board=set(map(tuple,standard['seed']));x=y=0;h=h0;last={};maxgap=0
for time,c in enumerate(H*30):
 p=(x,y);assert (p in board)==(c=='L')
 if p in last:maxgap=max(maxgap,time-last[p]);assert time-last[p]<=K
 last[p]=time
 if p in board:board.remove(p)
 else:board.add(p)
 h=(h+(1 if c=='R' else -1))%4;dx,dy=DIRECTIONS[h];x+=dx;y+=dy
assert (x,y)==(30*drift[0],30*drift[1])
# Geometric progress is not itself survival: a two-edge controller with
# opposite raw displacements has a certificate, but repeated literal
# chronology fails on its second cycle, irrespective of initial colors.
A='RRLLRRLL';B='LLRR';ra,da,ha=literal_trace(A,0);rb,db,hb=literal_trace(B,ha)
assert ha==hb==0 and da==(4,0) and db==(-2,0)
toy_phi=[0,-3]
assert da[0]+toy_phi[1]-toy_phi[0]==1
assert db[0]+toy_phi[0]-toy_phi[1]==1
last={};conflict=None
for i,(p,bit) in enumerate(literal_trace((A+B)*2,0)[0]):
 if p in last and last[p][1]==bit:
  conflict=dict(cell=p,earlier=last[p][0],later=i,required_black=bit);break
 last[p]=(i,bit)
assert conflict is not None
out=dict(scope='Supplied control-potential certificate checks only; no compiler or synthesis.',
         standard_control=dict(states=L,edges=edges,potential=phi,
                               functional=[-26,-26],delta=1,phase_ell_span=0,
                               potential_range=R,K=K,literal_steps_checked=30*L,
                               observed_max_repeat_gap=maxgap,seed=standard['seed']),
         progress_not_survival_control=dict(words=[A,B],headings=[0,0],drifts=[da,db],
                                           functional=[1,0],potential=toy_phi,delta=1,
                                           all_board_conflict=conflict),
         theorem_sha256=hashlib.sha256((HERE/'control_state_progress_potential.md').read_bytes()).hexdigest())
(HERE/'control_progress_potential_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(standard_states=L,corrected_gain=1,K=K,
                     observed_max_repeat_gap=maxgap,raw_unit_directions=4,
                     toy_all_board_conflict=conflict),indent=2))
