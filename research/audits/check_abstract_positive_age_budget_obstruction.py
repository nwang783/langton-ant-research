from pathlib import Path
import json,hashlib
S=Path(__file__);P=20
pairs=[(8,0,1),(12,16,0),(1,13,0),(5,9,0),(6,10,0),(18,2,1),(19,3,1),(11,15,0)]
roots=[4,17,14,7]
assert len(set(roots+[r for r,l,k in pairs]+[l for r,l,k in pairs]))==P
ages=[l+k*P-r for r,l,k in pairs];assert ages==[12,4,12,4,4,4,4,4]and all(0<a<P and a%4==0 for a in ages)
edges=[];adj=[[]for _ in range(P)]
def add(a,b,k,kind,owner):
 idx=len(edges);edges.append(dict(a=a,b=b,voltage=k,kind=kind,owner=owner));adj[a].append((b,k,idx));adj[b].append((a,-k,idx))
for j,(r,l,k)in enumerate(pairs):
 add(r,l,k,'alpha',j);add((r+1)%P,(l+1)%P,k+(l==P-1)-(r==P-1),'beta',j)
for r in roots:add(r,(r+1)%P,int(r==P-1),'root',r)
assert all(len(v)==2 for v in adj)
# Every alpha/beta component has a consistent integer lift; internal circuits are zero voltage.
seen={};fibres=[]
for a in range(P):
 if a in seen:continue
 seen[a]=0;todo=[a];vs=[]
 while todo:
  b=todo.pop();vs.append(b)
  for c,k,ei in adj[b]:
   if edges[ei]['kind']=='root':continue
   if c in seen:assert seen[c]==seen[b]+k
   else:seen[c]=seen[b]+k;todo.append(c)
 fibres.append(dict(events=sorted(vs),lifts=[seen[b]for b in sorted(vs)]))
seen=set();seenedges=set();circuits=[]
for a in range(P):
 if a in seen:continue
 b=a;prev=-1;vol=0;rootsteps=0;debt=0;steps=[];owncounts=[0]*len(pairs)
 while b not in seen:
  seen.add(b);c,k,ei=next(e for e in adj[b]if e[2]!=prev);edge=edges[ei];sgn=1 if b==edge['a']else-1
  assert ei not in seenedges;seenedges.add(ei)
  duration=c+k*P-b
  if edge['kind']=='root':assert duration==sgn;rootsteps+=sgn
  else:
   j=edge['owner'];assert duration==sgn*ages[j];debt+=duration;owncounts[j]+=sgn
  steps.append(dict(a=b,b=c,voltage=k,edge=ei,sign=sgn,elapsed=duration));vol+=k;b=c;prev=ei
 assert b==a and vol*P==rootsteps+debt
 circuits.append(dict(winding=vol,root_sigma_sum=rootsteps,lifetime_age_sum=debt,owner_coefficients=owncounts,steps=steps))
assert len(seen)==P and len(seenedges)==len(edges)==P
assert [(c['winding'],len(c['steps']))for c in circuits]==[(-3,14),(0,2),(0,2),(0,2)]
assert sum(abs(c['winding'])for c in circuits)==3 and sum(c['root_sigma_sum']for c in circuits)==-4
# This is NOT an ant factor: actual R/L kinematics fails the same-cell requirements.
L={l for r,l,k in pairs};word=''.join('L'if i in L else'R'for i in range(P));v=[1j,1,-1j,-1];p=0j;h=0;events=[];board={};repeat_failure=None
for t,c in enumerate(word):
 events.append((p,h,c))
 if p in board and board[p]==c and repeat_failure is None:repeat_failure=dict(earlier=next(i for i in range(t-1,-1,-1)if events[i][0]==p),later=t,cell=[int(p.real),int(p.imag)],same_turn=c)
 board[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=v[h]
assert h==0 and p==-4-4j
failures=[]
for j,(r,l,k)in enumerate(pairs):
 delta=events[l][0]+k*p-events[r][0]
 if delta:failures.append(dict(owner=j,R=r,L=l,voltage=k,physical_displacement=[int(delta.real),int(delta.imag)]))
assert len(failures)==7 and failures[0]['physical_displacement']==[-2,-4]
out=dict(status='VERIFIED ABSTRACT COUNTERMODEL ONLY: not an ant factor/front/controller',period=P,output_roots=roots,input_roots=[],pairs=[dict(R=r,L=l,voltage=k,age=a)for(r,l,k),a in zip(pairs,ages)],edges=edges,fibres=fibres,circuits=circuits,S=3,actual_turn_word=word,actual_word_drift=[-4,-4],actual_word_heading_restored=True,physical_pairing_failures=failures,finite_word_repeated_color_failure=repeat_failure,scope=['Positive lifetime ages divisible4 and smaller than the period, exact beta conjugacy, zero-voltage internal circuits, all-output unmatched roots, complete event/edge coverage and the expanded clock identity do NOT imply S<=1.','All declared inputs are absent only in this ABSTRACT owner matching. It does not provide a physically WHITE front. Seven of eight declared same-cell lifetime pairings fail actual R/L kinematics, so it is NOT a counterexample to the normalized winding budget for actual ant histories.','This precisely identifies an indispensable spatial/actual-read ownership condition beyond the signed clock representation. It adds no front exclusion, no abstract-to-physical realization and no global-attraction result.'],script_sha256=hashlib.sha256(S.read_bytes()).hexdigest())
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(hashlib.sha256(S.with_suffix('.json').read_bytes()).hexdigest());print('word_failure',repeat_failure)
