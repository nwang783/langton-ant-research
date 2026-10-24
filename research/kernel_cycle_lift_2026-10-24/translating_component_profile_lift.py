"""Exact finite-input lifting of a supplied translating periodic FULL active profile.
The head/word/profile are only proposals until all drift-ray guards pass. Passive
archives are never pruned; the initial finite seed is constructed when possible.
"""
from finite_component_profile_lift import ports
from active_flight import DIR,cursor,sector,comp,ray_epoch

def kinematics(word,p,h):
 P=[]
 for c in word:
  assert c in 'RL';P.append((p,h));h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 return P,p,h

def required_initial(guard,k):
 return guard['current_black']^(sum(m<=k for m in guard['earlier_read_copy_offsets'])%2)

def lift(word,components,p0=(0,0),h0=0):
 assert word and len(word)==len(components)
 poses,pend,hend=kinematics(word,p0,h0);d=(pend[0]-p0[0],pend[1]-p0[1]);k=sector(p0,h0)
 assert hend==h0 and d!=(0,0),'Scope is heading-restoring NONZERO translation'
 assert sector(pend,hend)==k
 C=[set(map(tuple,a))for a in components]
 for i,(p,h)in enumerate(poses):
  assert comp(C[i],k,cursor(p,h))==C[i]
  assert (p in C[i])==(word[i]=='L')
 G=[];tails=[]
 for i,(p,h)in enumerate(poses):
  for q in sorted(ports(C[i],p,h,k)):
   offsets=[];owners=[]
   for j,(r,_)in enumerate(poses):
    m=ray_epoch(r,q,d)
    if m is not None and(m>0 or(m==0 and j<i)):
     offsets.append(m);owners.append(dict(read_phase=j,copy_offset=m))
   K=max(offsets,default=0);stable=int(q in C[i])^(len(offsets)%2)
   g=dict(phase=i,cell=q,current_black=int(q in C[i]),earlier_read_copy_offsets=sorted(offsets),earlier_read_owners=owners,stabilization_copy=K,eventual_initial_black=stable)
   G.append(g)
   if stable:tails.append(len(G)-1)
 if tails:
  a=tails[0]
  return dict(status='NO_FINITE_INPUT_INFINITE_BLACK_GUARD_RAY',word=word,drift=d,period=len(word),p0=p0,h0=h0,sector=k,guard_count=len(G),black_tail_guard_indices=tails,first_black_tail=G[a],guards=G)
 S={};
 for i,g in enumerate(G):
  for n in range(g['stabilization_copy']):
   if required_initial(g,n):
    q=(g['cell'][0]+n*d[0],g['cell'][1]+n*d[1]);S.setdefault(q,dict(guard=i,copy=n))
 for q,a in S.items():
  for i,g in enumerate(G):
   n=ray_epoch(q,g['cell'],d)
   if n is not None and n>=0 and not required_initial(g,n):
    return dict(status='NO_FULL_PROFILE_INITIAL_BIT_CONFLICT',word=word,drift=d,period=len(word),p0=p0,h0=h0,sector=k,conflict_cell=q,black_requirement=a,white_requirement=dict(guard=i,copy=n),guards=G)
 return dict(status='ACTUAL_FINITE_INPUT_TRANSLATING_FULL_PROFILE',word=word,drift=d,period=len(word),p0=p0,h0=h0,sector=k,initial_black=sorted(S),initial_black_owners=[dict(cell=q,**a)for q,a in sorted(S.items())],maximum_complete_active_mass=max(map(len,C)),guard_count=len(G),guards=G)
