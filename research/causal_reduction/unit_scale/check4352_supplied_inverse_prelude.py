"""Use ONLY the already certified6820-turn source prelude as a launch path.
No longer connector search: infer initial future-unread edits on this fixed
reverse word and test exact inverse-H ownership/additions-only contracts.
"""
from pathlib import Path
from collections import defaultdict
import json,runpy,time
import inverse4352_tail_completion as T
P=Path(__file__).resolve().parent;G=T.G
E=runpy.run_path(str(G/'changed_endpoint_catalog.py'));A=json.loads((G/'second_prepared_wave_input.json').read_text());rows,F,p,h,tau,phi=E['incoming']({tuple(j):[0]for j in A['profiles']},{tuple(q)for q in A['cap']},(20,1))
original=[]
for _ in range(6820):
 c='L'if E['initial_color'](p,rows,F)else'R';original.append(c);E['toggle'](F,p);h=(h+(1 if c=='R'else-1))%4;v=T.V[h];p=(p[0]+v[0],p[1]+v[1])
assert[p[0]-70,p[1]-70]==list(T.POSE)and h==T.HEAD
reverse=''.join(original)[::-1].translate(str.maketrans('RL','LR'))

def fresh_contract(p,h,g,edits,flips,seen):
 current=T.BASE^set(edits)^set(flips)^set(map(tuple,g['extra_initial_XOR']));rr,_,_=T.trace(g['word'],p,h);groups=defaultdict(list)
 for i,(x,y),hh,c in rr:groups[x-y,x%2].append((i-104*(x//2),x//2,c))
 groups={j:sorted(z)for j,z in groups.items()}
 def required(z):
  x,y=z
  for time,k,c in groups.get((x-y,x%2),()):
   if k<=x//2:return c=='L'
  return None
 def other(z):return T.bulk(z)and(z[0]-z[1],z[0]%2)not in groups
 finite=set(seen)
 for(t,a),lo in T.FUTURE.items():
  if(t,a%2)not in groups:continue
  threshold=min(z[1]for z in groups[t,a%2]);x=a+26*lo
  while x//2<threshold:finite.add((x,x-t));x+=26
 cap=set();bad=[]
 for q in finite|current:
  if q not in finite and not T.future_read(q):continue
  prior=required(q);base=other(q)^(bool(prior)if prior is not None else False);want=T.bulk(q)^(q in current)
  if base!=want:
   if prior is not None:bad.append([q,'past'])
   elif base:bad.append([q,'erasure'])
   else:cap.add(q)
 return cap,bad,current

p=(T.POSE[0]-T.V[T.HEAD][0],T.POSE[1]-T.V[T.HEAD][1]);h=(T.HEAD+2)%4;edits=set();flips=set();seen=set();goals=[];best=None;start=time.time();found=None
for i in range(len(reverse)+1):
 for g in T.completion(p,h,edits,flips,seen):
  cap,bad,current=fresh_contract(p,h,g,edits,flips,seen);record={'depth':i,'pose':[p,h],'H_phase':g['phase'],'fresh_additions':len(cap),'forbidden':len(bad),'witnesses':bad[:12]};goals.append(record)
  if best is None or len(bad)<best['forbidden']:best=record;print('best',record,flush=True)
  if not bad:
   found={'inverse_prefix':reverse[:i],'inverse_tail_word':g['word'],'inverse_tail_pose':[p,h],'H_phase':g['phase'],'forward_entry_pose':[(p[0]-T.V[h][0],p[1]-T.V[h][1]),(h+2)%4],'forward_word':reverse[:i][::-1].translate(str.maketrans('RL','LR')),'fresh_cap':sorted(cap),'initial_wave_XOR_edits':sorted(edits^set(map(tuple,g['extra_initial_XOR']))),'forward_entry_cap_vs_full_bulk':sorted(current)};break
 if found or i==len(reverse):break
 c=reverse[i];want=c=='L';now=T.bulk(p)^(p in T.BASE)^(p in edits)^(p in flips)
 if now!=want:
  assert p not in seen and not T.future_read(p),('fixed reverse conflict',i,p,c,now)
  edits.symmetric_difference_update({p})
 flips.symmetric_difference_update({p});seen.add(p);h=(h+(1 if c=='R'else-1))%4;v=T.V[h];p=(p[0]+v[0],p[1]+v[1])
 if i%500==0:print('depth',i,'pose',p,h,'edits',len(edits),'seconds',time.time()-start,flush=True)
out={'scope':__doc__,'found':found,'supplied_forward_word':''.join(original),'tested_inverse_prefix_length':i,'goals':goals,'best':best,'seconds':time.time()-start}
(P/'4352_supplied_inverse_prelude.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE found',bool(found),'goals',len(goals),'best',best,flush=True)
