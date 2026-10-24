"""Exact minimized finite-window automaton of any-board marked packet factors.
No infinite-language claim. Out-of-patch abstractions may reset to empty history.
"""
from pathlib import Path
import json,sys,hashlib
R=Path(__file__).resolve().parents[1];D=R/'core_periodicity_new/chronology_dcuv';G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];keep=[0,1,4,5,6,7,8,9];depth=int(sys.argv[1])if len(sys.argv)>1 else 5;O=D/f'literal_factor_dfa_k{depth}.json';legal={()};front={()};conflicts=[];endpoints={():[0,0,0]}
def trace(seq):
 word=''.join(G[a]['word']for a in seq)+'LLLLRLRRRRL';x=y=h=0;last={};ds=[(0,1),(1,0),(0,-1),(-1,0)]
 for t,c in enumerate(word):
  q=x,y
  if q in last and last[q][0]==c:return False,{'cell':q,'previous_read':last[q][1],'conflicting_read':t,'turn':c}
  last[q]=c,t;h=(h+(1 if c=='R'else-1))%4;dx,dy=ds[h];x+=dx;y+=dy
 return True,None
assert depth >= 2, 'window must be at least two'
counts=[1]
for d in range(1,depth+1):
 nf=set()
 for s in sorted(front):
  for a in keep:
   ss=s+(a,);ok,c=trace(ss)
   if ok:nf.add(ss)
   else:conflicts.append({'word':ss,'conflict':c})
 legal|=nf;front=nf;counts.append(len(nf))
states=sorted(s for s in legal if len(s)<depth);index={s:i for i,s in enumerate(states)};T=[]
for s in states:
 row=[]
 for a in keep:
  ss=s+(a,);row.append(index[ss[-(depth-1):]]if ss in legal else-1)
 T.append(row)
part=[0]*len(states);rounds=0
while True:
 keys={};new=[]
 for row in T:
  sig=tuple(part[j]if j>=0 else-1 for j in row)
  if sig not in keys:keys[sig]=len(keys)
  new.append(keys[sig])
 rounds+=1
 if new==part:break
 part=new
classes=[[]for _ in range(max(part)+1)]
for i,c in enumerate(part):classes[c].append(states[i])
QT=[]
for C in classes:
 rows={tuple(part[j]if j>=0 else-1 for j in T[index[s]])for s in C};assert len(rows)==1;QT.append(list(rows.pop()))
J={'format':'literal_packet_window_dfa_v1','window':depth,'keep':keep,'geometry_file':str(D/'literal_residual_geometry.json'),'geometry_sha256':hashlib.sha256((D/'literal_residual_geometry.json').read_bytes()).hexdigest(),'legal_counts_by_length':counts,'states':states,'state_to_class':part,'classes':classes,'transitions':QT,'initial_class':part[index[()]],'rejected_extensions':conflicts,'minimization_rounds':rounds,'scope':'Every contiguous block must avoid exact any-board illegal literal factors up to this finite window; no assertion of sufficiency or eventual behavior.'};O.write_text(json.dumps(J,separators=(',',':')));print(json.dumps({'file':str(O),'counts':counts,'suffix_states':len(states),'classes':len(classes),'rounds':rounds,'rejections':len(conflicts)}))
