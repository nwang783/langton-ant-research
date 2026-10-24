from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'three_read_one_use_staircases_have_a_reader_independent_collision.md';JF=D/'check_three_read_one_use_staircase_return.json';assert sha(P)=='c1873e7f333f90f799b1b48286defe2add6ea9c430f79b5e02320a891620024c'and sha(JF).startswith('ccbf3d6b')and sha(D/'check_three_read_one_use_staircase_return.py').startswith('7d9d2ea4');J=json.loads(JF.read_text());H='NESW';V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)]
def out(w,r,b=False):return H[(H.index(w[r])+(1 if (r%2==0)!=b else -1))%4]
def net(hs,black=frozenset()):
 su={}
 for p,w in hs.items():
  for h,d in zip(H,V):
   if p+d not in hs:continue
   aa=[r for r in range(len(w))if out(w,r,p in black)==h];bb=[r for r,hh in enumerate(hs[p+d])if hh==h];assert len(aa)==len(bb),(p,h,w,hs[p+d],aa,bb)
   su.update({(p,r):(p+d,s)for r,s in zip(aa,bb)})
 return su
fixed={-1j:'WWE',0j:'N',1+0j:'WWE',1+1j:'N',2+1j:'WWE',1-1j:'SSNN',2+0j:'SSNN'};Z=2-1j
# Algebra derives the ENTIRE domain: re=rw=a<=2; WHITE n=4a or4a-1,
# BLACK n=4a or4a+1. No trial upper length is used to establish completeness.
rows=[];counts=Counter();seen=set()
for black in[False,True]:
 for a in range(3):
  for n in({4*a,4*a+1}if black else{4*a,4*a-1}):
   if n<=0:continue
   for es in product('EW',repeat=n):
    w=''.join(es)
    if w.count('E')!=2 or sum(out(w,r,black)=='N'for r in range(n))!=2:continue
    re=sum(w[r]=='E'for r in range(n)if(r%2==0)!=black);rw=sum(w[r]=='W'for r in range(n)if(r%2==0)!=black);assert re==rw==a
    key=black,w;assert key not in seen;seen.add(key);au=next(v for v in J['rows']if v['reader_starts_BLACK']==black and v['reader_word']==w);su=net(fixed|{Z:w},{Z}if black else set());start=[r for r in range(n)if out(w,r,black)=='N'][1];end=w.index('E');path=[(Z,start)];u=path[0]
    while len(path)==1 or u[0]!=Z:
     assert u in su;u=su[u];assert u[0]==Z or u not in path;path.append(u)
    expect=[(Z,start),(2+0j,3),(1+0j,1),(1-1j,0),(-1j,0),(0j,0),(1+0j,2),(1-1j,1),(Z,end)];assert path==expect and len(path)==9;assert[[xy(p),r]for p,r in path]==au['actual8_channel'];assert end!=start+1
    why='backward_rank'if end<=start else'skipped_rank';assert au['result']==why;counts[('BLACK'if black else'WHITE')+'_'+why]+=1;rows.append(dict(BLACK=black,word=w,start_rank=start,end_rank=end,path=[[xy(p),r]for p,r in path],result=why))
assert len(rows)==40 and seen=={(v['reader_starts_BLACK'],v['reader_word'])for v in J['rows']};assert sum(not v['BLACK']for v in rows)==18
for w in['WWWWEWE','WWWWEWEW']:
 row=next(v for v in rows if not v['BLACK']and v['word']==w);assert(row['start_rank'],row['end_rank'])==(2,4)
# Separate NONMAXIMAL cap4 bridge is independently reconstructed, not assumed.
cap=[]
for n in range(5):
 for ss in product('NS',repeat=n):
  w=''.join(ss)
  if w.count('S')!=2 or sum(out(w,r)=='W'for r in range(n))!=2:continue
  hs={-1j:'WWE',0j:'N',1+0j:'WWE',1-1j:w};su=net(hs);fail=[]
  for p,ww in hs.items():
   for r in range(len(ww)):
    u=(p,r);path=[u];used={u}
    while u in su:
     u=su[u];path.append(u)
     if u[0]==p:
      if u[1]!=r+1:fail.append(path)
      break
     assert u not in used;used.add(u)
  cap.append(dict(word=w,result='rank'if fail else'open',witness=[[xy(p),r]for p,r in fail[0]]if fail else None))
assert [v['word']for v in cap]==['NNSS','NSSN','SNNS','SSNN']and [v['word']for v in cap if v['result']=='open']==['SSNN']
# The GLOBAL-M uncapped bridge is exactly the already audited00 reader case.
dep=R/'audits/check_one_use_L3_transport_independent.json';assert sha(dep)=='ad205d481891b627c1fa783be2f185a112ae784eca5768149867cf68f004069e';old=json.loads(dep.read_text());assert [v for v in old['necessary_profiles']if v[:2]==[0,0]]==[[0,0,'SSNN']]
O=dict(status='PASS reader-independent physical staircase return collision with separate GLOBAL-M and cap4 bridges',proof=sha(P),certificate=sha(JF),script=sha(S),signed_uncapped_dependency=sha(dep),all40_count_derived_histories=rows,counts=counts,independent_nonmaximal_cap4_common_reader_domain=cap,analytic_review=[
'The supplied completeWHITE staircase A WWE,rN,BWWE,sN,CWWE has genuine one-use boundary edges. GLOBAL-M supplies both SSNN common readers by the signed uncapped00 LRL theorem. Independently, explicit cap4 withoutM leaves exactlyNNSS/NSSN/SNNS/SSNN from Sin2/Wout2; the firstthree have literal samephysical next-rank failures. Thus the separate nonmaximal cap4 corollary has a real checked premise bridge.',
'With U/V SSNN, the complete outer ports are Ein2/Nout2. Their physical ordinal matching gives exactly Z.secondN -> V3 -> B1 -> U0 -> A0 -> r0 -> B2 -> U1 -> Z.firstE, eight actual steps and no intermediate Z. No repaired edge, voltage reset, exterior path or unknown ordinal is inserted.',
'If the endpoint firstE is not the next physicalZ rank, this actualreturn already reverses/skips chronology. If it were next, all prior arrivals wereW, so the starting secondN wasR_W and leftBLACK; its nextE read mustL_E and departN a thirdtime, contradicting the completeport. Initialcolor and arbitraryearlierstock do not affect this argument.',
'Ein2=Nout2 gives R_E=R_W=a<=2. CompleteWHITE lengths4a or4a-1 and BLACK lengths4a or4a+1 follow exactly fromalternation. Independent generation gives18WHITE and22BLACK histories, all withthe assertedactual eightstep rankcollision. The seven/eightread WWWWEWE[/W] shields specifically skip L3 fromR2toR4.',
'The local contradiction applies to physicalpoints even if somefull-drift classes alias; additionalidentifications cannotrepair it. Rotation is merely lattice symmetry. No criticality, period bound, old-age/fuel payment or globalallcapfirstRmax premise is used.',
'Only the specified three-read L0,R,L0,R,L0 staircase is excluded under either stated reader-supplying hypothesis. Four-readLEFT/mixedbits/LL/RR/changedgeometry and generalone-use runs remain outside; no wholefront or capture conclusion follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(counts,cap);print(sha(S.with_suffix('.json')))
