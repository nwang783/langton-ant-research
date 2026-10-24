"""58 supplied cap7 words: exact history plus sound mandatory-field propagation.
No profile expansion or SAT solver. Unresolved words are returned, never accepted.
"""
from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import DIR,cursor,ends,vertices,comp
from finite_component_profile_lift import ports
SRC=ROOT/'reframe_finite_seed_2026-10-24/cap7_turn_word_quotient.json';J=json.loads(SRC.read_text());M=7

def analyze(W,propagate):
 p=(0,0);h=0;pose=[];last={};seed=set();readtrace=[]
 for t,c in enumerate(W):
  pose.append((p,h))
  if p in last and last[p][1]==c:
   return dict(word=W,status='NO_LITERAL_WORD_COLOR',conflict_cell=p,previous=last[p],next=[t,c])
  if p not in last and c=='L':seed.add(p)
  last[p]=(t,c);readtrace.append(dict(cut=t,cell=p,turn=c));h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 pose.append((p,h));R=set(last);B=set(seed);fields=[]
 for t in range(len(W)+1):
  fields.append(set(B))
  if t<len(W):B.symmetric_difference_update([pose[t][0]])
 FB=set();FW=set();log=[]
 def out(status,**extra):
  return dict(word=W,status=status,first_L_minimal_seed=sorted(seed),visited_cells=sorted(R),forced_unread_initial_black=sorted(FB),forced_unread_initial_white=sorted(FW),forcing_log=log,read_trace=readtrace,**extra)
 for t in(0,len(W)):
  p,h=pose[t]
  for q in ports(set(),p,h,1):
   if q in fields[t]:return out('NO_EMPTY_ENDPOINT',cut=t,black_port=q)
   if q not in R and q not in FW:FW.add(q);log.append(dict(kind='initial_white_empty_endpoint',cut=t,cell=q))
 if propagate:
  while True:
   change=False
   for t,(p,h)in enumerate(pose):
    B=fields[t]|FB;C=comp(B,1,cursor(p,h))
    if len(C)>M:return out('NO_CAP7_MANDATORY_COMPONENT',cut=t,mandatory_component=sorted(C))
    for q in sorted(ports(C,p,h,1)-R-FB-FW):
     D=comp(B|{q},1,cursor(p,h))
     if len(D)>M:
      FW.add(q);change=True;log.append(dict(kind='initial_white_cap',cut=t,cell=q,overlarge_component=sorted(D)))
   for t in range(1,len(W)):
    p,h=pose[t];P=ports(set(),p,h,1);B=fields[t]|FB
    if P&B:continue
    choices=P-R-FW
    if not choices:return out('NO_INTERIOR_NONEMPTY',cut=t,ports=sorted(P))
    if len(choices)==1:
     q=next(iter(choices))
     if q not in FB:FB.add(q);change=True;log.append(dict(kind='initial_black_nonempty_unit',cut=t,cell=q,ports=sorted(P)))
   if not change:break
 F=fields[-1]|FB;p,h=pose[-1];r=cursor(p,h);N={(r[0]+a,r[1]+b)for a in(-2,2)for b in(-2,2)};U=set()
 for v in N:U|=comp(F,1,v)
 a,b=ends(p,1);u=b if a==r else a
 status='TRAP_MASS'if len(U)>M-4 else'TRAP_SATURATED_NONFIRST'if len(U)==M-4 and u not in vertices(U,1)else'OPEN'
 return out(status,exit_pose=[p,h],mandatory_final_black=sorted(F),mandatory_neighbor_import=sorted(U),forced_import_mass=len(U),first_tip_in_forced_field=u in vertices(U,1))

raw=[analyze(w,False)for w in J['word_counts']]
strong=[analyze(w,True)for w in J['word_counts']]
for a,b in zip(raw,strong):
 a['kernel_profile_multiplicity']=J['word_counts'][a['word']];b['kernel_profile_multiplicity']=J['word_counts'][b['word']]
res=dict(status='AUTHOR sound cap7 whole-word mandatory-field and import-budget filters',source_sha256={str(SRC.relative_to(ROOT)):hashlib.sha256(SRC.read_bytes()).hexdigest()},word_count=len(strong),raw_word_only=raw,first_return_unit_propagation=strong,remaining_words=[a['word']for a in strong if a['status']=='OPEN'],scope='Literal histories and endpoint/mandatory-field contradictions are exact negative results. Unit propagation adds only logically forced unread initial cells from first-return nonempty clauses and cap7 upper bounds. OPEN is unresolved, not a realization. Full-profile-specific old support is not promoted to whole-word support. Grammar coverage is a separate author dependency.')
(OUT/'cap7_word_budget_filters_certificate.json').write_text(json.dumps(res,indent=2)+'\n')
from collections import Counter
print(json.dumps({'raw_counts':dict(Counter(a['status']for a in raw)),'strong_counts':dict(Counter(a['status']for a in strong)),'remaining_words':res['remaining_words'],'extra_mandatory_old_inputs':[{'word':a['word'],'old_black':a['forced_unread_initial_black'],'status':a['status']}for a in strong if a.get('forced_unread_initial_black')],'improvements':[{'word':a['word'],'raw':a['status'],'strong':b['status']}for a,b in zip(raw,strong)if a['status']!=b['status']]},indent=2))
