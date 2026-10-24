"""Exact language intersection with finitely many independently illegal factors.
CLI BASE_DFA.json PATTERNS.json PREFIX. Patterns are lists of packet ids.
No assertion that the retained finite language suffices for ant realizability.
"""
from pathlib import Path
import json,sys,hashlib,collections
base,patterns,out=map(Path,sys.argv[1:4]);B=json.loads(base.read_text());G=json.loads(Path(B['geometry_file']).read_text())['geometry'];keep=B['keep'];patterns0=json.loads(patterns.read_text());patterns0=sorted(set(map(tuple,patterns0)));assert patterns0 and all(p and all(a in keep for a in p)for p in patterns0)
proof=[]
for seq in patterns0:
 x=y=h=0;last={};word=''.join(G[a]['word']for a in seq)+'LLLLRLRRRRL';bad=None
 for i,c in enumerate(word):
  q=x,y
  if q in last and last[q][0]==c:bad={'cell':q,'previous_read':last[q][1],'conflicting_read':i,'turn':c};break
  last[q]=(c,i);h=(h+(1 if c=='R'else-1))%4;dx,dy=[(0,1),(1,0),(0,-1),(-1,0)][h];x+=dx;y+=dy
 assert bad is not None,('Do not forbid a feasible literal factor',seq)
 proof.append({'word':seq,'conflict':bad})
prefixes=sorted({p[:n]for p in patterns0 for n in range(len(p))});start=(B['initial_class'],());states=[start];ix={start:0};rows=[]
for c,s in states:
 row=[]
 for ai,a in enumerate(keep):
  cc=B['transitions'][c][ai];ss=s+(a,)
  if cc<0 or any(len(ss)>=len(p)and ss[-len(p):]==p for p in patterns0):row.append(-1);continue
  tail=max((p for p in prefixes if not p or len(ss)>=len(p)and ss[-len(p):]==p),key=len);z=cc,tail
  if z not in ix:ix[z]=len(states);states.append(z)
  row.append(ix[z])
 rows.append(row)
part=[0]*len(states);rounds=0
while True:
 keys={};new=[]
 for row in rows:
  sig=tuple(part[z]if z>=0 else-1 for z in row)
  if sig not in keys:keys[sig]=len(keys)
  new.append(keys[sig])
 rounds+=1
 if new==part:break
 part=new
classes=[[]for _ in range(max(part)+1)]
for i,c in enumerate(part):classes[c].append(i)
QT=[]
for cl in classes:
 rr={tuple(part[z]if z>=0 else-1 for z in rows[i])for i in cl};assert len(rr)==1;QT.append(list(rr.pop()))
J={'format':'literal_packet_forbidden_factor_dfa_v1','keep':keep,'geometry_file':B['geometry_file'],'geometry_sha256':B['geometry_sha256'],'base_dfa_file':str(base.resolve()),'base_dfa_sha256':hashlib.sha256(base.read_bytes()).hexdigest(),'forbidden_factor_file':str(patterns.resolve()),'forbidden_factor_sha256':hashlib.sha256(patterns.read_bytes()).hexdigest(),'forbidden_factors':proof,'unminimized_states':states,'unminimized_rows':rows,'state_to_class':part,'classes':classes,'transitions':QT,'initial_class':part[0],'window':max(B.get('window',0),max(map(len,patterns0))),'minimization_rounds':rounds,'scope':'Exact intersection of the base necessary marked-factor language with avoidance of listed literal-impossible complete-context factors. No infinite-language sufficiency.'};out.with_suffix('.json').write_text(json.dumps(J,separators=(',',':')));print(json.dumps({'product_states':len(states),'classes':len(classes),'patterns':len(patterns0),'rounds':rounds}))
