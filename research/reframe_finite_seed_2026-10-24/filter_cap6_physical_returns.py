"""Exact finite-prefix lifting by full-C port constraints and read parity.
This is an AUTHOR implementation of the separately developed finite-lift principle.
"""
from active_flight import *
from pathlib import Path
import json,time
OUT=Path(__file__).parent
OPEN={'RRRRLRL','RRRRLRLL','RRRRLRRLL','RRRRLRLRL','RRRRLRRLRL'}
def incident(v):
 return {((v[0]+dx)//2,(v[1]+dy)//2)for dx in(-1,1)for dy in(-1,1)}
def lift(r,verify=True):
 bits={};parity=set();p=(0,0);h=0;phases=[]
 def need(q,b):
  orig=b^(q in parity)
  if q in bits and bits[q]!=orig:return False
  bits[q]=orig;return True
 def guard(C):
  vs=vertices(C,1)|{cursor(p,h)};ports=set().union(*(incident(v)for v in vs))
  assert C<=ports
  return all(need(q,int(q in C))for q in sorted(ports))
 for i,t in enumerate(r['transitions']):
  C={(p[0]+rot(tuple(q),h)[0],p[1]+rot(tuple(q),h)[1])for q in t['input_component']}
  if not guard(C):return None
  phases.append((p,h,C))
  assert (p in C)==(t['turn']=='L')
  if p in parity:parity.remove(p)
  else:parity.add(p)
  h=(h+(1 if t['turn']=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 if not guard(set()):return None
 phases.append((p,h,set()));B={q for q,b in bits.items()if b};seed=set(B)
 if verify:
  p=(0,0);h=0
  for i,(pp,hh,C)in enumerate(phases):
   assert p==pp and h==hh and comp(B,1,cursor(p,h))==C,(i,r['word'],seed)
   if i<len(phases)-1:p,h=step(B,p,h)
 return sorted(seed)
if __name__=='__main__':
 st=time.time();R=json.loads((OUT/'kernel_M6_scc.json').read_text())['first_return_cycles'];yes=[];no=[];seeds={};counts={}
 for i,r in enumerate(R):
  if r['word']not in OPEN:continue
  seed=lift(r)
  if seed is None:no.append(i)
  else:yes.append(i);seeds[i]=seed
  c=counts.setdefault(r['word'],{'feasible':0,'infeasible':0});c['feasible'if seed is not None else'infeasible']+=1
 out={'scope':'Exact finite-prefix full-field lift, not composability between different returns. Author controls pending audit.','surviving_word_classes':sorted(OPEN),'feasible_indices':yes,'infeasible_indices':no,'minimal_finite_seeds':seeds,'counts':counts,'elapsed_seconds':time.time()-st};(OUT/'cap6_physical_return_filter.json').write_text(json.dumps(out,indent=2)+'\n');print('feasible',len(yes),'infeasible',len(no),'counts',counts,'seconds',time.time()-st)
