"""Deterministic past of one specified wave-entry memory repair.
Only q=(14,-7) is toggled at the exact prepared launch output. Its membership
outside the entire forward4352 READ set is verified. No cap search is run.
This is not itself an initially realizable repair or a finite-seed claim.
"""
from pathlib import Path
from collections import defaultdict
import json,time,hashlib
from probe4352_return_end_limit import RayBoard,first_bad,trace,H,V,L
import inverse4352_tail_completion as T
P=Path(__file__).resolve().parent
def build():
 b=RayBoard();groups=defaultdict(list)
 for i,q,h,c in list(trace(L['inverse_tail_word'],tuple(L['inverse_tail_pose'][0]),L['inverse_tail_pose'][1]))[:-1]:
  groups[q[0]-q[1],q[0]%2].append((i-104*(q[0]//2),q[0]//2,c))
 for(t,a),g in groups.items():
  g.sort();mn=min(x[1]for x in g);mx=max(x[1]for x in g)
  for n in range(mn,mx):
   f=next(x for x in g if x[1]<=n)
   if f[2]=='L':b.toggle((a+2*n,a+2*n-t))
  if g[0][2]=='L':
   for r in range(39):b.lower((a+2*(mx+r),a+2*(mx+r)-t))
 for t,a in L['other_full_black_profiles']:
  for r in range(a,78,2):b.full.symmetric_difference_update({(t,r)})
 for q in L['fresh_cap']:b.toggle(tuple(q))
 for _,q,h,c in list(trace(L['forward_prelude_word'],tuple(L['forward_entry_pose'][0]),L['forward_entry_pose'][1]))[:-1]:b.toggle(q)
 return b
def main():
 b=build();q=(14,-7);assert not T.future_read(q)and b.color(q);b.toggle(q)
 # At entry(-2,3),W the inverse conjugate pose is(-1,3),E.
 p=(-1,3);h=1;initial=b.manifest();word=[];recent='';events=[];firstdiv=None;clock=time.time()
 original=L['inverse_prefix'];I=''.join('L'if c=='R'else'R'for c in H[::-1]);rot={H[i:]+H[:i]:'H'for i in range(104)};rot.update({I[i:]+I[:i]:'inverse_H'for i in range(104)})
 def step():
  nonlocal p,h,recent,firstdiv
  c='L'if b.color(p)else'R'
  if firstdiv is None and len(word)<len(original)and c!=original[len(word)]:
   firstdiv={'time':len(word),'pose':[p,h],'original':original[len(word)],'actual':c};print('divergence',firstdiv,flush=True)
  b.toggle(p);h=(h+(1 if c=='R'else-1))%4;p=p[0]+V[h][0],p[1]+V[h][1];word.append(c);recent=(recent+c)[-208:];return c
 while True:
  candidate=None;kind=None
  if len(recent)>=8 and recent[-8:]in('LR'*4,'RL'*4):candidate=recent[-2:];kind='alternating_staircase'
  elif len(recent)==208 and recent[:104]==recent[104:]and recent[104:]in rot:candidate=recent[104:];kind=rot[candidate]
  if candidate is not None:
   w=candidate;bad,d=first_bad(b,p,h,w);e={'offset':len(word),'kind':kind,'pose':[p,h],'word':w,'first_bad':bad,'drift':d};events.append(e);print('flight',e,flush=True)
   if bad is None:break
   for i in range(bad):assert step()==w[i%len(w)]
   e['contact']={'offset':len(word),'pose':[p,h],'wanted':w[bad%len(w)],'actual':'L'if b.color(p)else'R'};step();recent='';continue
  step()
  if len(word)%100000==0:print('steps',len(word),'pose',p,h,'F',len(b.F),flush=True)
 out={'scope':__doc__,'status':'EXACT_PREPARED_PERIODIC_PAST','repair':q,'repair_future_unread':True,'initial_board':initial,'initial_inverse_pose':[[-1,3],1],'word':''.join(word),'events':events,'first_divergence_from_original_inverse':firstdiv,'final_pose':[p,h],'final_finite_xor':sorted(b.F),'seconds':time.time()-clock,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (P/'prepared4352_repaired_launch_past.json').write_text(json.dumps(out,indent=2)+'\n');print('finished',len(word),time.time()-clock,flush=True)
if __name__=='__main__':main()
