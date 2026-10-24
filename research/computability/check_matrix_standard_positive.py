#!/usr/bin/env python3
"""Positive control: the certified periodic104 finite seed as a matrix recurrence.
No new counterexample. This checks actual finite first-L extraction, not only rejection.
"""
import sys,json,time
from pathlib import Path
from expanding_matrix_visits import MatrixRecurrence
from automatic_radix import Rel,reverse_msb,linear
from selfsimilar_visit_relations import inverse_tests
st=time.monotonic()
path=Path(__file__).resolve().parents[1]/'recovered_bundle/ant_global/root/standard.json'
data=json.loads(path.read_text());w=data['word'];P=len(w)
# Rotate its incoming heading W to N, preserving its turn word.
h=0;p=(0,0);qs=[];steps=((0,1),(1,0),(0,-1),(-1,0))
for c in w:
    qs.append(p);h=(h+(1 if c=='R'else -1))%4
    p=(p[0]+steps[h][0],p[1]+steps[h][1])
assert h==0;drift=p
base=2;nxt=[];off=[]
for s in range(P):
    row=[];rr=[]
    for j in range(base):
        q,r=divmod(base*s+j,P);row.append(r)
        rr.append((q*drift[0]+qs[r][0]-base*qs[s][0],q*drift[1]+qs[r][1]-base*qs[s][1]))
    nxt.append(row);off.append(rr)
m=MatrixRecurrence(base,((base,0),(0,base)),nxt,off)
print('BUILD',flush=True)
rs,meta=m.difference_machine(1)
print('CARRY',meta,'seconds',time.monotonic()-st,flush=True)
eq=rs((0,0));print('EQ',len(eq.tr),'seconds',time.monotonic()-st,flush=True)
left=reverse_msb(Rel(('t',),nxt,{i for i,c in enumerate(w)if c=='L'},base))
ans=inverse_tests(eq,left)
print('INVERSE',ans,'seconds',time.monotonic()-st,flush=True)
assert ans['first_left_times_finite'] and ans['bad_alternation_witness'] is None
first=left&~(eq&linear(base,{'t':1,'s':-1},1,'>=')).exists('s')
bound=first.implies(linear(base,{'_bound':1,'t':-1},0,'>=')).forall('t').witness()['_bound']
ts=[t for t in range(bound+1)if first.eval(t=t)];seed=sorted(m.point(t)for t in ts)
# Clockwise quarter rotation takes original incoming W to N.
expected=sorted((y,-x)for x,y in data['seed'])
assert seed==expected,(seed,expected)
checks=0
for s in range(400):
    for t in range(400):
        assert eq.eval(s=s,t=t)==(m.point(s)==m.point(t));checks+=1
out={'status':'PASS genuine finite-support standard104 positive control','source':str(path.relative_to(path.parents[2])),'matrix':[[2,0],[0,2]],'radix':2,'states':P,**meta,'equal_cell_states':len(eq.tr),**ans,'first_L_bound_witness':bound,'first_L_times':ts,'minimal_seed':seed,'minimal_seed_size':len(seed),'literal_pair_checks':checks,'elapsed_seconds':time.monotonic()-st}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
