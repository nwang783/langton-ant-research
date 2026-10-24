from pathlib import Path
from collections import defaultdict
from itertools import product,combinations
import json,hashlib,subprocess,random
P=Path(__file__).resolve();ROOT=P.parents[1];S=ROOT/'audits/check_short_refinement_cnf_independent.py';exec(compile(S.read_text().split('# White palette semantic reconstruction')[0],str(S),'exec'))
Q=json.loads((U/'forward108_prepared_control.json').read_text())['word'];O=U/'q_self_rewrite';J=json.loads((O/'local_core.json').read_text());allowed={(-8,0),(-7,1),(-6,0),(-5,1),(-4,0)}
rr,e,eh=walk(Q,(0,0),1);source=defaultdict(list)
for t,(x,y,h,c)in enumerate(rr):source[x-y,x%2].append((t-108*(x//2),c))
for vv in source.values():vv.sort();assert all(a[1]!=b[1]for a,b in zip(vv,vv[1:]))
BI={a for a,v in source.items()if v[0][1]=='L'};BO={a for a,v in source.items()if v[-1][1]=='R'};assert len(BI)==3 and len(BO)==11
th=fullhist(Q,(0,14),3);TI={a for a,v in th.items()if v[0][1]=='L'};assert TI=={(-8,0),(-7,0),(-6,1)}and TI-BO=={(-8,0)}and not(BO&set(th)-TI)
assert BO&allowed=={(-5,1)}
coarse,e,eh=walk(Q,(0,14),3);assert coarse[72]==(-2,6,3,'L')and(e,eh)==((-2,12),3)
groups=defaultdict(lambda:defaultdict(list))
for j,(x,y,h,c)in enumerate(coarse):
 target=walk(c,(x,y),h)[1:]
 for k,w in enumerate(palette[c]):
  rows,e,eh=walk(w,(x,y),h);assert(e,eh)==target
  for i,(xx,yy,hh,turn)in enumerate(rows):groups[xx-yy,xx%2][xx//2,j,i,turn].append(2+10*j+k)
def circuit(inp,keep):
 C=[[1]]
 for j in range(108):
  xs=list(range(2+10*j,12+10*j));C.append(xs);C.extend([[-a,-b]for a,b in combinations(xs,2)])
 nv=1081;gates=[]
 for a,evs in sorted(groups.items()):
  if a not in keep:continue
  prev=1 if a in inp else-1
  for ev,xs in sorted(evs.items()):
   act,nxt=nv+1,nv+2;nv+=2;C.extend([[-x,act]for x in xs]);C.append(xs+[-act]);C.append([-act,prev if ev[3]=='L'else-prev])
   for bp,ba,bn in product((False,True),repeat=3):
    if bn!=(bp!=ba):C.append([(-v if b else v)for v,b in zip((prev,act,nxt),(bp,ba,bn))])
   gates.append((a,ev,xs,prev,act,nxt));prev=nxt
 return nv,C,gates
nv,C,gates=circuit(BO,allowed);rn,RC=read_cnf(O/'local_core.cnf');assert nv==rn==1641 and len(C)==7181 and canon(C)==canon(RC)
for f,key in(('local_core.cnf','cnf_sha256'),('local_core.rup','rup_sha256')):assert hashlib.sha256((O/f).read_bytes()).hexdigest()==J[key]
proof=json.loads(subprocess.run([str(ROOT/'causal_reduction/morphic_candidates/check_drat'),str(O/'local_core.cnf'),str(O/'local_core.rup')],capture_output=True,text=True,check=True).stdout);assert proof['valid']and proof['RUP']==25 and proof['RAT']==0 and proof['deletions']==0
repair=palette['L'].index('RRRRL');assert len('RRRRL')==min(len(w)for w in palette['L']if w[0]=='R');selrep=[repair if i==72 else 0 for i in range(108)]
rng=random.Random(10814);tests=[([0]*108,TI,'identity_own'),([0]*108,BO,'identity_source'),(selrep,BO,'first_color_repair')]
for n in range(24):
 sel=[0]*108
 for p in rng.sample(range(108),n+1):sel[p]=rng.randrange(1,10)
 tests.append((sel,BO,'sparse'))
records=[]
for sel,inp,label in tests:
 word=''.join(palette[c][k]for c,k in zip(Q,sel));hist=fullhist(word,(0,14),3);alt=all(all(a[1]!=b[1]for a,b in zip(v,v[1:]))for v in hist.values());first=all((v[0][1]=='L')==(a in inp)for a,v in hist.items());legal=alt and first
 nv,cs,gs=circuit(inp,set(groups));val={1:True}
 for j,k in enumerate(sel):
  for i in range(10):val[2+10*j+i]=k==i
 def lit(x):return val[abs(x)]if x>0 else not val[abs(x)]
 words=defaultdict(list)
 for a,ev,xs,prev,act,nxt in gs:
  val[act]=any(lit(x)for x in xs);val[nxt]=lit(prev)!=val[act]
  if val[act]:words[a].append(ev[3])
 assert dict(words)=={a:[c for t,c in v]for a,v in hist.items()}
 assert all(any(lit(x)for x in cl)for cl in cs)==legal
 records.append(dict(label=label,length=len(word),first_colors=first,alternating=alt,legal=legal))
assert records[0]['legal']and not records[1]['legal']and records[2]['first_colors']and not records[2]['alternating']
out=dict(status='PASS independent supplied opposite-Q interface, five-orbit relaxed CNF and RUP',note_sha256=hashlib.sha256((U/'q_self_rewrite_obstruction.md').read_bytes()).hexdigest(),source_input_classes=3,source_output_classes=11,target_input_classes=sorted(TI),missing_class=[-8,0],retained_five_colors={str(a):a in BO for a in sorted(allowed)},variables=1641,clauses=7181,RUP=25,cnf_sha256=J['cnf_sha256'],rup_sha256=J['rup_sha256'],controls=records,scope='Fixed Q108 scaffold at(0,14,W), stationary legal exact-pose1/5/9 choices. Dropping every other orbit chronology still UNSAT. No changing choices, other images/scaffolds, arbitrary self-rewrite, cap/bootstrap or noncapture claim.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='controls'})
