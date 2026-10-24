#!/usr/bin/env python3
"""Exact inverse tests for an automatic walk using binary time/complex-base grid.

The example is the genuinely aperiodic dragon geometry, which is rejected as
an ant path. This is a negative control, not a counterexample to the conjecture.
"""
from automatic_relations import Rel,TRUE,FALSE,linear,initial_left_cells,bad_alternation
from gaussian_automatic import dragon_graph,dragon_left,neighbor,UNITS,decode
from pathlib import Path
import json,time

def directions():
    states=[(-1,0)];idx={states[0]:0};tr=[]
    for prev,count in states:
        row=[]
        for bit in [0,1]:
            nxt=(bit,(count+(prev^bit if prev>=0 else 0))%4)
            if nxt not in idx:idx[nxt]=len(states);states.append(nxt)
            row.append(idx[nxt])
        tr.append(row)
    return [Rel(('t',),tr,{i for i,(prev,c) in enumerate(states) if (c+(max(prev,0)))%4==d}).minimal() for d in range(4)]

def eventually_periodic(left):
    later=(left.rename(t='r')&linear({'r':1,'t':-1,'p':-1},0)).exists('r')
    same=left.iff(later)
    future=linear({'t':1,'T':-1},0,'>=')
    return (future.implies(same).forall('t')&linear({'p':1},1,'>=')).exists('T','p').truth()

def validate_geometry(g,dirs):
    total=g.exists('z').forall('t').truth()
    other=g.rename(z='w')
    nonunique=(g&other&~linear({'z':1,'w':-1},0)).witness()
    dtotal=FALSE
    for d in dirs:dtotal=dtotal|d
    assert dtotal.forall('t').truth()
    for i in range(4):
        for j in range(i):assert (dirs[i]&dirs[j]).witness() is None
    # Consecutive outgoing directions must differ by a quarter-turn.
    clock=linear({'s':1,'t':-1},1)
    turnbad=FALSE
    for i in range(4):
        for j in [i,(i+2)%4]:turnbad=turnbad|(dirs[i]&dirs[j].rename(t='s')&clock)
    assert turnbad.witness() is None
    both=g&g.rename(t='s',z='w')&clock
    failures=[]
    for d,unit in zip(dirs,UNITS):
        bad=(both&d&~neighbor(unit)).witness();failures.append(bad)
    return {'total':total,'nonunique_witness':nonunique,'bad_move_witnesses':failures}

def main():
    start=time.monotonic();g,ns,ds=dragon_graph();dirs=directions();left=dragon_left()
    geometry=validate_geometry(g,dirs)
    assert geometry['total'] and geometry['nonunique_witness'] is None and not any(geometry['bad_move_witnesses'])
    # Independently construct L from the old and new directions plus initial N.
    inferred=dirs[2]&linear({'t':1},0)
    for old in range(4):
        inferred=inferred|((dirs[old].rename(t='s')&dirs[(old+1)%4]&linear({'t':1,'s':-1},1)).exists('s'))
    assert (~inferred.iff(left)).witness() is None
    first=initial_left_cells(g,left);bad=bad_alternation(g,left);w=bad.witness()
    assert w is not None and not first.bounded()
    periodic=eventually_periodic(left);assert not periodic
    out={'status':'PASS: exact automata negative control','geometry':geometry,'position_dfa_states':len(g.tr),'first_left_set_dfa_states':len(first.tr),'first_left_set_finite':False,'consecutive_equal_turn_relation_states':len(bad.tr),'alternation_violation':dict(w,physical_cell=decode(w['z'])),'turn_stream_eventually_periodic':periodic,'elapsed_seconds':time.monotonic()-start,'scope':'This dragon walk is geometrically valid and aperiodic, but is not an ant trajectory on any coloring and also has infinitely many first-L cells. No highway counterexample.'}
    p=Path(__file__).resolve().parent
    (p/'automatic_dragon_inverse.json').write_text(json.dumps(out,indent=2)+'\n')
    (p/'automatic_dragon_models.json').write_text(json.dumps({'position':{'variables':g.vs,'transition':g.tr,'accepting':sorted(g.ac),'start':g.start},'left':{'variables':left.vs,'transition':left.tr,'accepting':sorted(left.ac),'start':left.start}},indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
