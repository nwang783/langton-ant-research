"""Reconstruct W20 geometry, stream, ordinal repair and all star inventories without author code."""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];R=ROOT/'K1_pipeline_detours_2026-10-23';W='LRRRRLLLLRLLLLRLRRRR';V=(1j,1,-1j,-1);xy=lambda z:(int(z.real),int(z.imag));results=[]
for a in (1,2,3):
 word=W*a;P=len(word);dy=2*a;p=1+0j;h=0;physical=[];hist=defaultdict(list)
 for t,c in enumerate(word):
  o=(h+(1 if c=='R'else-1))%4;k=int(p.imag)//dy;cell=p-k*dy*1j
  hist[cell].append((t-k*P,t,h,o,c));physical.append((p,h,o,c));p+=V[o];h=o
 assert p==1+dy*1j and h==0
 for cell,slots in hist.items():
  slots.sort();assert all(x[4]!=y[4]for x,y in zip(slots,slots[1:]))
 # Solve ALL dual face differences including unused edges, not supplied stream heights.
 xmin=min(int(q.real)for q,_,_,_ in physical)-3;xmax=max(int(q.real)for q,_,_,_ in physical)+3
 flow=Counter()
 for q,hi,ho,c in physical:
  k=int(q.imag)//dy;flow[(xy(q-k*dy*1j),ho)]+=1
 eq=defaultdict(list)
 def relation(c,l,f):
  eq[c].append((l,-f));eq[l].append((c,f))
 for x in range(xmin,xmax+1):
  for y in range(dy):
   # north edge through(x,y), direction even source north / odd source south.
   if (x+y)%2==0:src=(x,y);ho=0;cf=(x,y);lf=(x-1,y)
   else:src=(x,(y+1)%dy);ho=2;cf=(x-1,y);lf=(x,y)
   relation(cf,lf,flow[src,ho])
   # east edge through(x,y).
   if (x+y)%2:src=(x,y);ho=1;cf=(x,(y-1)%dy);lf=(x,y)
   else:src=(x+1,y);ho=3;cf=(x,y);lf=(x,(y-1)%dy)
   relation(cf,lf,flow[src,ho])
 heights={next(iter(eq)):0};stack=list(heights)
 while stack:
  q=stack.pop()
  for z,d in eq[q]:
   value=heights[q]+d
   if z in heights:assert heights[z]==value
   else:heights[z]=value;stack.append(z)
 assert len(heights)==len(eq)
 shift=1-max(v for(x,y),v in heights.items()if(x+y)%2==0);heights={q:v+shift for q,v in heights.items()}
 labels={};events={};tau=list(range(P));ex=[]
 for cell,slots in hist.items():
  counts=Counter()
  for rank,(ct,t,hi,ho,c)in enumerate(slots):
   counts[ho]+=1;q,_,_,_=physical[t];center=q+V[ho]/2-V[ho]*1j/2;cf=(int(round(center.real-.5)),int(round(center.imag-.5))%dy)
   labels[t]=heights[cf]-counts[ho]+1;events[t]=dict(cell=xy(cell),rank=rank,input='black'if slots[0][4]=='L'else'white',turn=c)
  if ''.join(s[4]for s in slots)=='RLRL':
   x,y=slots[1][1],slots[2][1];assert slots[2][0]-slots[1][0]==4;tau[x],tau[y]=tau[y],tau[x];ex.append((x,y))
 sigma=[tau[(t+1)%P]for t in range(P)];node={};cycles=[]
 for t in range(P):
  if t in node:continue
  u=t;cc=[]
  while u not in node:node[u]=len(cycles);cc.append(u);u=sigma[u]
  assert u==t and len({labels[x]for x in cc})==1
  drift=sum(V[physical[x][2]]for x in cc);assert drift.real==0 and int(drift.imag)%dy==0
  cycles.append(dict(level=labels[t],length=len(cc),winding=int(drift.imag)//dy,black_input_reads=sum(events[x]['input']=='black'for x in cc),events=[events[x]for x in cc]))
 edges=[(node[x],node[y])for x,y in ex];root=next(i for i,c in enumerate(cycles)if c['level']==0)
 assert len(cycles)==4*a+1 and len(edges)==4*a and cycles[root]['length']==4*a and cycles[root]['winding']==1
 assert all(y==root for x,y in edges)and sorted(x for x,y in edges)==[i for i in range(len(cycles))if i!=root]
 low=[c for c in cycles if c['level']==-1];top=[c for c in cycles if c['level']==1]
 assert len(low)==len(top)==2*a and all(c['length']==4 and c['winding']==0 for c in low+top)
 assert Counter(c['black_input_reads']for c in low)=={0:a,2:a}
 results.append(dict(full_period=P,drift=[0,dy],cycles=cycles,edges=edges,N2=len(edges),C=len(cycles),excess=len(edges)-len(cycles)+1))
out=dict(status='PASS independent literal prepared W20 stream and star reconstruction',note_sha256=hashlib.sha256((R/'prepared_W20_sheet_star_control.md').read_bytes()).hexdigest(),reports=results,scope='Prepared singleton-black L cells explicitly retained. Not a white front, a fuel budget, or a causal completion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print([(r['full_period'],r['N2'],r['C'],r['excess'])for r in results])
