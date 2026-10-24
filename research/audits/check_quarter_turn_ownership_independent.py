"""Literal untouched-bit check; no legality of the proposed intervening T is assumed."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];P=R/'causal_reduction/unit_scale'
H=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
cf=P/'opposite_wake_quarter_turn_word.json';tf=P/'opposite_wake_through_phase21_word.json'
C=json.loads(cf.read_text())['word'];T=json.loads(tf.read_text())['word']
def walk(w,p,h):
    reads=[]
    for t,c in enumerate(w):
        reads.append((t,p,c));h*=(-1j if c=='R'else 1j);p+=h
    return reads,p,h
q=5+4j;rc,pc,hc=walk(C,23-20j,1j)
hist=[(t,c)for t,z,c in rc if z==q]
assert len(hist)==11 and ''.join(c for t,c in hist)=='RLRLRLRLRLR'
assert(pc,hc)==(91-63j,1)
rn,_,_=walk(C,27-16j,1j);nexthist=[(t,c)for t,z,c in rn if z==q];assert nexthist[0]==(888,'R')
rt,pt,ht=walk(T,99-96j,1j);assert(pt,ht)==(59-48j,1j)
norm=lambda z:int(z.real-z.imag)
assert(min(norm(z)for _,z,c in rt),max(norm(z)for _,z,c in rt))==(101,213)
rh,ph,hh=walk(H*16,pt,ht);assert(ph,hh)==(27-16j,1j)
assert min(norm(z)for _,z,c in rh)==37
ro,po,ho=walk(H,pc,hc);assert(po-pc,ho)==(2+2j,hc)
assert(min(norm(z)for _,z,c in ro),max(norm(z)for _,z,c in ro))==(147,157)
assert q not in {z for _,z,c in rt+rh+ro}
cl=lambda z:(int(z.real)%2,int(z.real+z.imag)%4)
assert cl(3-(91-63j))==cl(2+1j)!=cl(3)
result={'status':'PASS independent phase and untouched-bit obstruction',
        'first_C_q_read_history':hist,'shifted_C_first_q_read':[888,'R'],
        'T_read_normal_range':[101,213],'sixteen_NW_periods_min_normal':37,
        'all_NE_tail_normal_range':[147,157],
        'scope':'Conditional prescribed C/T/C attempt; the omitted return route must have even XOR at q. No T all-parameter legality signoff, no route existence, and no general repair or renewal exclusion.',
        'hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in (cf,tf,P/'quarter_turn_two_phase_ownership.md')}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
