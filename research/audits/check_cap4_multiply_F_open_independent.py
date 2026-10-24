from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'CAP4_MULTIPLY_USED_F_OPEN_INTERFACE.md';assert sha(note)=='08185afc177d0c6458bde3a5b5447782c2e12d4fb10993901d874d25956c0fa9';src=D/'freeze_cap4_multiply_used_F_interface.py';assert sha(src)=='48d0f792dbecfc6b5cc9591a2ef2893c982d552ee538635cc3e48d88c782b752';jp=D/'cap4_multiply_used_F_open_interface.json';assert sha(jp)=='155817ca1ef88ac9424d4b0a5c08e69a918810766fd5cba54ed39c0f110bdaf1';ref=json.loads(jp.read_text())
V=(1j,1,-1j,-1);names='NESW';pts=[complex(r,t-r)for t in range(-1,4)for r in(0,1)];hist=['W','','N','SS','WE','WWE','SNN','SSNS','EEWE','WWEW'];ix={p:i for i,p in enumerate(pts)};cl={tuple(map(int,k.split(':'))):v for k,v in ref['representative_clocks'].items()};P=200;dr=2-2j
assert sum(map(len,hist))==24 and max(map(len,hist))==4 and len(cl)==24 and len({v%P for v in cl.values()})==24
q=lambda p:(p-(int(p.real)//2)*dr,int(p.real)//2)
succ={};pred={};edges=[];ports=[]
for i,(p,w)in enumerate(zip(pts,hist)):
 incoming=[names.index(h)for h in w];outs=[(h+(1 if j%2==0 else-1))%4 for j,h in enumerate(incoming)]
 # Sigma+ complete local axis and physical time congruences.
 assert all(h%2==int(p.real+p.imag)%2 for h in incoming)
 for j in range(len(w)):
  assert cl[i,j]%4==(2*int(p.real)-int(p.real+p.imag)%2+1)%4
  if j:assert cl[i,j]-cl[i,j-1]>=4
 for heading in range(4):
  ss=[j for j,h in enumerate(outs)if h==heading]
  if not ss:continue
  t,k=q(p+V[heading])
  if t in ix:
   ti=ix[t];tt=[j for j,h in enumerate(hist[ti])if names.index(h)==heading];assert len(ss)==len(tt)
   for ord,(a,b)in enumerate(zip(ss,tt)):
    assert(i,a)not in succ and(ti,b)not in pred;succ[i,a]=((ti,b),k);pred[ti,b]=((i,a),k);assert cl[i,a]+1==cl[ti,b]+k*P;edges.append(dict(source=[i,a],target=[ti,b],voltage=k,physical_ordinal=ord))
  else:
   for a in ss:ports.append(dict(direction='out',cell=i,rank=a,heading=heading,outside_class=[int(t.real),int(t.imag)],voltage=k))
for (i,j)in cl:
 if(i,j)not in pred:
  hd=names.index(hist[i][j]);s,k=q(pts[i]-V[hd]);assert s not in ix;ports.append(dict(direction='in',cell=i,rank=j,heading=hd,outside_class=[int(s.real),int(s.imag)],voltage=k))
assert edges==ref['all_internal_ordinal_edges']and ports==ref['all_open_ports'];assert sum(z['direction']=='out'for z in ports)==sum(z['direction']=='in'for z in ports)==4
FG={i:(succ[i,0][0][0],succ[i,0][1])for i,w in enumerate(hist)if w and(i,0)in succ};EG={i:(t,k)for i,(t,k)in FG.items()if succ[i,0][0][1]==len(hist[t])-1}
def cycles(g):
 done=set();cs=[]
 for start in g:
  path=[];seen={};v=start
  while v in g and v not in done and v not in seen:seen[v]=len(path);path.append(v);v=g[v][0]
  if v in seen:
   c=path[seen[v]:];cs.append((c,sum(g[t][1]for t in c)))
  done.update(path)
 return cs
fc=cycles(FG);assert len(fc)==1 and fc[0][1]==-1 and not cycles(EG);cs=fc[0][0];assert cs==[5,7,4,6]
uses=[]
for i in cs:
 hd=(names.index(hist[i][0])+1)%4;uses.append(sum((names.index(x)+(1 if j%2==0 else-1))%4==hd for j,x in enumerate(hist[i])))
 # Opposite traversals of this edge are impossible under the given complete endpoint sector histories.
 ti,k=FG[i];assert all((names.index(x)+(1 if j%2==0 else-1))%4!=(hd+2)%4 for j,x in enumerate(hist[ti]))
assert uses==[1,1,2,2]
out=dict(status='PASS finite OPEN cap4 port-and-clock model only',note_sha256=sha(note),json_sha256=sha(jp),event_count=24,period=200,distinct_phases=24,internal_ordinal_edges=edges,all_open_ports=ports,F_cycle_classes=[list(map(int,(pts[i].real,pts[i].imag)))for i in cs],F_winding=-1,F_edge_total_uses=uses,E_cycles=[],analytic_review=[
'All ten proposed COMPLETE named histories, including the empty class, are checked against exact full d=(2,-2) translation reduction and WHITE rank alternation. Every internal occurrence is ordinal matched, every unmatched in/out port is retained, and sector orientation excludes opposite-direction use of the four F edges.',
'The supplied numeric P200 clocks independently satisfy all twenty internal successor equations, every same-cell gap>=4, all required modulo4 pose times, and24 distinct modulo200 event phases. No SMT solver is run or trusted as a proof.',
'The first-R DEPARTURE graph has the displayed negative-winding four-circle with total edge-use1,1,2,2; the first-R-to-LAST-read E graph is acyclic. These are different graphs and the signed single-use E theorem is not contradicted.',
'This is an explicit finite open local interface, NOT a shared physical board, finite literal factor, full200-event cycle, complete cap4 WHITE front or autonomous controller. The176 missing phases and all upper completion obligations remain open. Consequently it only refutes deducing one-use F edges from these finite local port/clock assumptions; global terrain may still exclude the interface.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
