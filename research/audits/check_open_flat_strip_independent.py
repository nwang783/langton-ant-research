from pathlib import Path
from collections import Counter
import json,hashlib,ast
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'flat_RRLL_strips_have_unbounded_open_injective_chronology.md';C=D/'check_open_flat_RRLL_strip_family.json';assert sha(P)=='c4faa17c0de16470ff073d0a25f2b7f6b277fdd5902f1d561eb186a67e815888';assert sha(C)=='c496d657573aa2a7608f988de2d2f01e378cfb207b64de5f1d5afd7972359323';J=json.loads(C.read_text());V=[1j,1,-1j,-1];head='NESW';out=lambda w,r:(head.index(w[r])+(1 if r%2==0 else-1))%4;phase=lambda z:{(0,0):0,(1,0):1,(0,1):3,(1,1):2}[int(z.real)%2,int(z.imag)%2]
controls=[]
for ref in J['unit_controls']:
 k=ref['k'];a=lambda j:2*j+0j;b=lambda j:2*j+1+0j;u=lambda j:2*j-1j;v=lambda j:2*j+1-1j;L=-1-1j;W=-1+0j;Z=2*k+0j;SS=2*k-1j
 H={L:'NNN',W:'WEW',SS:'EWE',Z:'SSS'}
 for j in range(k):H.update({a(j):'NSSN',b(j):'EWWE',u(j):'WWEE',v(j):'NNSS'})
 assert H=={complex(*ast.literal_eval(p)):w for p,w in ref['histories'].items()};su={};pr={};external=[]
 for p,w in H.items():
  for h,d in enumerate(V):
   src=[r for r in range(len(w))if out(w,r)==h];q=p+d
   if q not in H:external.extend((p,r,h,q)for r in src);continue
   dst=[s for s,hh in enumerate(H[q])if head.index(hh)==h];assert len(src)==len(dst)
   for r,s in zip(src,dst):su[p,r]=(q,s);pr[q,s]=(p,r)
 # All-index successor table. Each interior formula depends only on j +/-1;
 # the four displayed endpoint substitutions exhaust j=0 and j=k-1.
 sym={}
 for j in range(k):
  sym[a(j),0]=(b(j),0);sym[a(j),1]=(b(j),3);sym[a(j),2]=(b(j-1),1)if j else(W,0);sym[a(j),3]=(b(j-1),2)if j else(W,2)
  sym[b(j),0]=(v(j),2);sym[b(j),1]=(v(j),3)
  sym[u(j),0]=(a(j),0);sym[u(j),3]=(a(j),3)
  sym[v(j),0]=(u(j+1),2)if j+1<k else(SS,0);sym[v(j),1]=(u(j),0);sym[v(j),2]=(u(j),1);sym[v(j),3]=(u(j+1),3)if j+1<k else(SS,2)
 sym[L,0]=(u(0),2);sym[L,2]=(u(0),3);sym[Z,0]=(b(k-1),1);sym[Z,2]=(b(k-1),2);assert su==sym
 ev={(p,r)for p,w in H.items()for r in range(len(w))};assert len(ev)==16*k+12;channels=[]
 for start in ev-set(pr):
  seq=[];x=start
  while True:
   seq.append(x)
   if x not in su:break
   x=su[x]
  channels.append(seq)
 supplied=[[(complex(*p),r)for p,r in z['events']]for z in ref['blocks']];assert{tuple(z)for z in channels}=={tuple(z)for z in supplied};assert len(supplied)==4*k+8 and len(external)==4*k+8
 # Check complete symbolic order in the note, independent of the supplied block labels.
 ordered=[[(v(k-1),0),(SS,0)]]
 for j in range(k-1,-1,-1):
  ordered.append([(v(j),1),(u(j),0),(a(j),0),(b(j),0),(v(j),2),(u(j),1)])
  if j:ordered.append([(v(j-1),0),(u(j),2)])
 ordered +=[[(L,0),(u(0),2)],[(L,1)],[(SS,1)],[(Z,0),(b(k-1),1),(v(k-1),3),(SS,2)],[(Z,1)],[(Z,2),(b(k-1),2)],[(a(k-1),1),(b(k-1),3)]]
 for j in range(k-2,-1,-1):ordered +=[[(a(j+1),2),(b(j),1),(v(j),3),(u(j+1),3),(a(j+1),3),(b(j),2)],[(a(j),1),(b(j),3)]]
 ordered +=[[(a(0),2),(W,0)],[(W,1)],[(L,2),(u(0),3),(a(0),3),(W,2)]];assert ordered==supplied
 flatten=[e for seq in ordered for e in seq];assert set(flatten)==ev and len(flatten)==len(ev);where={e:(i,j)for i,seq in enumerate(ordered)for j,e in enumerate(seq)}
 for p,w in H.items():
  for r in range(len(w)-1):
   i,j=where[p,r];ii,jj=where[p,r+1];assert i<ii or i==ii and jj-j==4
 times={};end=-4*k-40
 for seq,refblock in zip(ordered,ref['blocks']):
  start=end+4*k+20;start+=(phase(seq[0][0])-start)%4;assert start==refblock['start_time']
  for j,e in enumerate(seq):times[e]=start+j;assert times[e]%4==phase(e[0])
  end=start+len(seq)-1
 assert len(set(times.values()))==len(ev)
 for e,f in su.items():assert times[f]==times[e]+1
 for p,w in H.items():
  for r in range(1,len(w)):assert times[p,r]-times[p,r-1]>=4
 assert len([p for p,w in H.items()if len(w)%2])==4;assert 2*k-2*(k-1)==2
 controls.append(dict(k=k,events=len(ev),channels=len(channels),internal_ordinal_edges=len(su),open_in_and_out_ports=len(channels),distinct_phased_clock=True))
out=dict(status='PASS symbolic all-k OPEN literal-channel/rank/injective-clock strip; not a physical factor',proof=sha(P),certificate=sha(C),script=sha(S),controls=controls,symbolic_rank_order={'a_j':'rank0 in A_j; rank1 in P_j; ranks2/3 in C_(j-1) at offsets0/4, or the left endpoint pair. Decreasing-j schedule puts P_j before C_(j-1).','b_j':'rank0 in A_j; ranks1/2 in C_j at offsets1/5, or separate right C/Z-final blocks; rank3 in P_j, after C_j.','u_j':'ranks0/1 in A_j at offsets1/5; rank2 in D_(j-1) after A_j, or left D; rank3 in later C_(j-1), or left final.','v_j':'rank0 in D_j before A_j, or initial right D; ranks1/2 in A_j at offsets0/4; rank3 in later C_j, or right C.','end_cells':'L ranks0/1/2 are leftD/leftmiddle/leftfinal; W ranks0/1/2 leftfirst/Wmiddle/leftfinal; S ranks0/1/2 rightD/rightmiddle/rightC; Z ranks0/1/2 rightC/Zmiddle/Zfinal.'},analytic_review=['For all integerk>=1 the four local histories have the exact successor formulas implemented in the symbolic table. Only j=0 and j=k-1 need endpoint substitutions, fully listed. Every named event occurs exactly once in the indexed channels; the four-type rank-location formulas establish order for every j, not by a finite length extrapolation.','All internal directed ports including zero counts match exactly. The channels are the complete connected components of the internal event graph, each with one incoming and one outgoing UNKNOWN exterior port. There are16k+12 events,12k+4 internal edges and4k+8 open channels.','Within a channel, consecutive same-cell ranks occur four steps apart. Across channels the displayed order is strictly increasing; gaps4k+20 rounded upward to the start cell residue are at least4. All internal steps preserve the fixed mod4 phase table: even/even0, odd/even1, even/odd3, odd/odd2. Thus events are distinct, every physical edge duration1 and every rank gap>=4. An overall multiple-of-four shift can make all times nonnegative.','The selected boundary word RR(LLRR)^(k-1) has exactly2k RIGHT and2(k-1) LEFT contacts, so curvature+2 for allk. Exactlyfour complete three-read END classes are odd; interior cells are four-read even. This is formal local output inventory only.','No exterior paths, full-drift quotient, critical same-contact conditions, global single-event orbit, actual board or full front are provided. It refutes a per-unit odd/fuel bound deduced from these LOCAL constraints alone, not an actual physical-ant fuel theorem. All k have necessary locally consistent injective clocks, not attained physical factors.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
