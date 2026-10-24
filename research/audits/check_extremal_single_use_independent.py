from pathlib import Path
from itertools import product
import hashlib,json,random
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'EXTREMAL_SINGLE_USE_EDGE_LEMMA.md';assert sha(note)=='5648cb495d0dd7fdcc4c35caed84deea60b0d0dd0149aec77234b99565afc1fe'
base=R/'periodic_classification_new/white_first_departure_counterflow.md';assert sha(base)=='44302c05565a1320b3793e3f279a6355ce099387f1b2f853bca2046895446c7a'
p=S.with_name('check_all_cap_extremal_read_coupling_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('std=json.loads')[0],ns);trace,key,loops,V=[ns[k]for k in ['trace','key','loops','V']]
def sf(m,A):return[A if k==0 or k%2 else(A+2)%4 for k in range(m)]
def tf(m,A):return[A]if m==1 else[A]*(m-1)+[(A+2)%4]
# Complete bounded local controls corroborate the explicit all-m formulas.
local=0
for m in range(1,13):
 for A in range(4):
  source=[];target=[]
  for suffix in product((A,(A+2)%4),repeat=m-1):
   q=[A,*suffix];outs=[(h+(1 if k%2==0 else-1))%4 for k,h in enumerate(q)]
   if all(z!=outs[0]for z in outs[1:]):source.append(q)
   if all(z!=q[-1]for z in q[:-1]):target.append(q)
  assert source==[sf(m,A)]and target==[tf(m,A)]
  assert (sf(m,A)==tf(m,A))==(m in(1,3));local+=2**(m-1)
# At the triple A,A,-A: selected incoming -A, selected outgoing R(A),
# remaining first-input neighbor -A and later-output R(-A) lie in right sector.
ports=[]
for A in range(4):
 inc=(A+2)%4;out=(A+1)%4;assert(out-inc)%4==3
 offin=(A+2)%4;offout=(A+3)%4
 # Normalize A=N: cycle north->center->east, offports south/west.
 assert((offin-A)%4,(offout-A)%4)==(2,3);ports.append((A,inc,out,offin,offout))
std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());stand=[]
for mul in(1,2,3):
 for h in range(4):
  ev,d,eh=trace(std['word']*mul,h);P=len(ev);hist={};flow={}
  for t,q,hi,ho,c in ev:
   r,k=key(q,d);hist.setdefault(r,[]).append((t-k*P,hi,ho,c,t));flow[r,ho]=flow.get((r,ho),0)+1
  for es in hist.values():es.sort()
  E={}
  for r,es in hist.items():
   first=es[0];v,k=key(r+V[first[2]],d)
   if first[0]+1==hist[v][-1][0]+k*P:
    assert flow[r,first[2]]==1;assert[z[1]for z in es]==sf(len(es),es[0][1]);tar=hist[v];assert[z[1]for z in tar]==tf(len(tar),tar[0][1]);E[r]=(v,k)
  cy=loops(E);assert len(cy)<=1
  for c,w in cy:assert w==-1 and all(len(hist[v])in(1,3)for v in c)and sum(len(hist[v])==1 for v in c)==len(c)//2
  stand.append(dict(period=P,rotation=h,marked_edges=len(E),cycles=len(cy)))
# Finite physical factors, explicitly retaining boundary exceptions.
rng=random.Random(314159);checked=excepted=0
for z in range(80):
 pts=[complex(x,y)for x in range(-3,4)for y in range(-3,4)];B=set(rng.sample(pts,rng.randrange(15)));q=0j;h=z%4;hist={};ev=[];flow={}
 for t in range(2000):
  c='L'if q in B else'R';ho=(h+(1 if c=='R'else-1))%4;event=(t,q,h,ho,c);ev.append(event);hist.setdefault(q,[]).append(event);flow[q,ho]=flow.get((q,ho),0)+1;B.symmetric_difference_update({q});q+=V[ho];h=ho
 for u,hs in hist.items():
  first=hs[0]
  if first[4]!='R'or first[0]==1999:continue
  v=ev[first[0]+1][1];ht=hist[v]
  if ht[-1][0]!=first[0]+1:continue
  if hs[-1][0]==1999 or ht[0][0]==0 or ht[0][4]!='R':excepted+=1;continue
  assert flow[u,first[3]]==1;assert[e[2]for e in hs]==sf(len(hs),first[2]);assert[e[2]for e in ht]==tf(len(ht),ht[0][2]);checked+=1
out={'status':'PASS all-cap single-use extremal edge formulas and at-most-one E cycle','author_note':sha(note),'first_departure_source':sha(base),'local_formula_controls':local,'triple_right_side_ports':ports,'standard_full_drift_controls':stand,'finite_marked_edges':checked,'finite_boundary_exceptions':excepted,'analytic_review':[
'In a fixed physical ant sector every cell has one fixed incomingaxis and the perpendicular outgoingaxis. Thus each physical edge is usable in only ONE direction. The first read atsource is its first departure; targetarrival is simultaneously its lastread. Exact physicaledgeordinal matching forces totaluse1. Reverse traversal is not an omitted possibility.',
'Two allowed incomingheadings plusalternatingR/L force all-m source A,A,-A,A,-A,... and target A^(m-1),-A (singletonseparate). Comparingformulas gives ONLYsingletonorRLRtriple A,A,-A at any internalE vertex. Boundedformula controls do not supply the all-m argument.',
'An Ecycle is an actual firstRdeparturecycle, so signed cap-free theorem makes it embedded essential winding-1. Its incoming cycleheading is targetLAST, outgoing is sourceFIRSTR. Singleton givesRcorner, triple givesLcorner. At triple the two unusedcycleports, eachusedtwice, lie strictly in local RIGHT sector; singletonhasnootherusedports. Unitgrid edges cannot crosscircleexceptatvertices, and physicalusededgegraph is connected as imageofsingleeventorbit.',
'Therefore no used support can lie in LEFT component of anyEcircle: a connectingpath would first attach via a forbiddenleftport. Two disjoint orientedessentialwinding-1 circles are linearlyordered on cylinder; each would have to contain the other onitsRIGHT, impossible. Indegree/outdegree<=1 makes distinctEcycles vertexdisjoint; latticequotient remains embedded and axesprevent edgecrossingwithoutvertex. AtmostONE, not guaranteedexistence.',
'Cycleell oddoutputclasses are exactlyhalf singleton/halftriple. Alternatingaxes give horizontal=vertical=ell/2, so ell>=2||d||inf and ell/2 congruent eachdriftcoordinate mod2. Atg8, ell<=8 and signedunitdiagonalexclusion removesell2; only4,6,8 conditionalpossibilities. This does not use missinghistoricalwidth10g8exhaustion.',
'All outputroots, arbitrary evenhistoriesoffcycle and acyclic/emptyE remainallowed. No all-capclassification, growth8exclusion, positivecontrollerconstruction or eventualcapture follows.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],checked,excepted)
