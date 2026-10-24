"""Exact first departure of the actual R252 finite producer from its4352 wave.
No capture or renewal is inferred beyond the named first contact.
"""
from pathlib import Path
import json,sys,hashlib
from check4352_noncrossing_producer import setup,H,W,V
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
start,B,ss,caps=setup(252,1);initial=set(B);p=start;h=3;t=0;last={}
for s in ss:
 if s['kind']=='wave':break
 word=H*s['count']if s['kind']=='H'else s['word']
 for c in word:
  assert(p in B)==(c=='L');last[p]=[t,h,c,s['kind'],s.get('index')];B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1];t+=1
entry=t;fm=first_mismatch(State(frozenset(B),p,h),W);assert fm is not None
print('entry',entry,'first_mismatch',fm,flush=True)
# first_mismatch uses a dictionary containing exact step and pose.
if isinstance(fm,int):delta=fm
else:delta=fm['step']if'step'in fm else fm['time']
for i in range(delta):
 c=W[i%len(W)];assert(p in B)==(c=='L');last[p]=[t,h,c,'wave',i//len(W)];B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1];t+=1
actual='L'if p in B else'R';want=W[delta%len(W)];assert actual!=want
out={'scope':__doc__,'R':252,'initial_mass':len(initial),'wave_entry_time':entry,'wave_departure_offset':delta,'complete_periods':delta//len(W),'word_phase':delta%len(W),
 'time':t,'pose':[p,h],'wanted':want,'actual':actual,'prior_read':last.get(p),'initial_black':p in initial,
 'field_mass':len(B),'field_sha256':hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest(),'field_before_contact':sorted(B)}
(P/'prepared4352_first_finite_endpoint.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='field_before_contact'},indent=2))
