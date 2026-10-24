#!/usr/bin/env python3
"""Exhaust all pristine closed-head-pose words using the CERTIFIED blank tail,
then reject every single insertion into one standard104 period by exact FULL-drift
stable chronology. There is no arbitrary excursion-duration bound.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib,sys
R=Path(__file__).resolve().parent;BASE=R.parent
sys.path.insert(0,str(BASE/'computability'))
from periodic_tail_checker import first_mismatch,plan,multiplier
from check_rigid_reachability import State
V=[(0,1),(1,0),(0,-1),(-1,0)]
def trace(w,h=0):
 p=(0,0);E=[]
 for t,c in enumerate(w):
  E.append((t,p,h,c));h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
 return E,p,h

def quotient(p,d):
 j=0 if d[0]else 1;k=p[j]//d[j]
 return(p[0]-k*d[0],p[1]-k*d[1]),k

def main():
 black=set();p=(0,0);h=0;stream='';returns=[];entry=None
 for t in range(10081):
  if t==9977:entry=State(frozenset(black),p,h)
  if t>0 and p==(0,0)and h==0:
   returns.append({'length':t,'root_BLACK':p in black,'full_output_black':sorted(black),'growth':len(black),'word':stream})
  c='L'if p in black else'R';stream+=c;black.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
 tail=stream[9977:];assert len(tail)==104 and first_mismatch(entry,tail)is None
 qs,d=plan(entry,tail);assert d==(-2,-2)
 no_return=[]
 for i,q in enumerate(qs):
  k=multiplier((-q[0],-q[1]),d);assert k is None or k<0
  no_return.append({'phase':i,'absolute_read_position':q,'possible_origin_lift':k})
 assert [z['length']for z in returns]==[4,16,52,184,276,384,436,472,660,6168,6764,8048,8052,8056,8068]
 assert [z['length']for z in returns if not z['root_BLACK']]==[52,184,384,472,660,6168,8048,8056,8068]
 path=BASE/'recovered_bundle/ant_global/root/standard.json';S=json.loads(path.read_text())['word'];assert S==tail
 rows=[]
 for z in returns:
  U=z['word']
  for cut in range(104):
   w=S[:cut]+U+S[cut:];E,D,Hend=trace(w);assert Hend==0 and D==(-2,2);P=len(w);classes=defaultdict(list)
   for t,q,h,c in E:
    r,k=quotient(q,D);classes[r].append({'phase':t,'physical_position':q,'lift':k,'canonical_time':t-P*k,'turn':c})
   for es in classes.values():es.sort(key=lambda x:x['canonical_time'])
   witness=None
   for q,es in sorted(classes.items()):
    pair=next(((a,b)for a,b in zip(es,es[1:])if a['turn']==b['turn']),None)
    if pair is not None:
     witness={'representative':q,'complete_stable_class':es,'consecutive_same_turn_phases':[pair[0]['phase'],pair[1]['phase']]};break
   assert witness is not None,('SURVIVING INSERTION',len(U),cut)
   rows.append({'pristine_length':len(U),'standard_cut':cut,'total_period':P,'full_drift':D,'word_sha256':hashlib.sha256(w.encode()).hexdigest(),'status':'NONALTERNATING_ON_ANY_INITIAL_BOARD','witness':witness})
 assert len(rows)==1560
 deps={str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[path,BASE/'computability/periodic_tail_checker.py',BASE/'computability/check_rigid_reachability.py']}
 J={'status':'AUTHOR ALL-PRISTINE-POSE-EXCURSION SINGLE-INSERTION EXCLUSION; independent audit pending','scope':'Every nonempty finite factor whose physical first reads are all WHITE and that returns to its original position AND heading; inserted once into a standard104 period at any of104 cuts. Prepared-input or multiple insertions are not covered.','blank_tail_certificate':{'entry_time':9977,'entry_pose':[entry.p,entry.h],'complete_entry_black':sorted(entry.black),'word':tail,'full_drift':d,'exact_all_future_checker_result':None,'all_future_origin_ray_checks':no_return},'all_pristine_same_pose_returns':returns,'root_WHITE_count':9,'root_BLACK_count':6,'standard_word':S,'dependency_hashes':deps,'all_1560_insertion_witnesses':rows}
 (R/'all_pristine_pose_insertions_certificate.json').write_text(json.dumps(J,indent=2)+'\n')
 print('PASS exact blank all-future tail, all15 pristine pose returns, all1560 single-insertion failures')
if __name__=='__main__':main()
