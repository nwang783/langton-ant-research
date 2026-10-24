from pathlib import Path
from collections import defaultdict
import json,hashlib,heapq
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'RELEVANT_RADIUS_RENEWAL_MANIFEST.json';assert sha(MF)=='94daca63d0aed44a707378a9fea86625f5f50b015aa1efaf0c5872a10676775b';M=json.loads(MF.read_text())
for f,h in M['files'].items():assert sha(D/f)==h
J=json.loads((D/'RELEVANT_RADIUS_RENEWAL_CHECKED.json').read_text());SRC=json.loads((D/'TRANSVERSE_FAR_MODULE_SOURCE.json').read_text())
for f,h in J['source_hashes'].items():assert sha(D/f)==h
ns={};exec(S.with_name('check_return_permanent_debt_independent.py').read_text().split('def check_case')[0],ns);verify,vec,G,xy=[ns[k]for k in('verify_future','vec','G','pair')];B=set(G);p=0j;h=1;word='';first={};poses=[]
for t in range(286):
 poses.append((p,h))
 if p in G and p not in first:first[p]=t
 c='L'if p in B else'R';word+=c;B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=vec[h]
A,U=word[:182],word[182:];assert poses[59]==(1+2j,2)and sorted(first.values())==[1,22,32,58];assert [xy(poses[59][0]),poses[59][1]]==J['source59_pose'];controls=[]
for row in J['controls']:
 n=row['n'];k=n//2;origins=[0j,(7*n-1)+7*n*1j,5*n+(9*n-4)*1j,(n+5)+5*n*1j];rot=[1,1j,-1,-1j];seed={o+r*q for o,r in zip(origins,rot)for q in G};assert sorted(map(xy,seed))==row['seed'];counts=[7*k-4,2*k-5,4*k-6,2*k-6];parts=[61,71,61,56];entries=[0]
 for i in range(3):entries.append(entries[-1]+182+104*counts[i]+parts[i])
 assert entries==row['port_entries']and entries[3]==676*n-821;T=676*n-762;b=156*n-59;c=780*n-1207;q=3*n+(3*n+3)*1j
 seq=''.join(A+U*counts[i]+U[:parts[i]]for i in range(4))+SRC['post_contact_word']+U*2;assert len(seq)==row['physical_reads'];B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda z:(z.real,z.imag)))};p=0j;h=1;deaths={};births={};oldtags=[];positions=[];snap={};firstactual={}
 for t,ch in enumerate(seq):
  positions.append(p)
  if t in(T-1,T,T+1):snap[t]=(dict(B),p,h)
  if p in seed and p not in firstactual:firstactual[p]=t
  old=B.pop(p,None);oldtags.append(old);assert(ch=='R')==(old is None)
  if old is None:B[p]=t;births[t]=p;h=(h+1)%4
  else:deaths[old]=t;h=(h-1)%4
  p+=vec[h]
 positions.append(p);w,dr,ff,tests=verify(B,p,h);assert w==U and dr==2-2j and tests==row['full_tail_parity_tests'];deaths.update({tag:len(seq)+dt for tag,dt in ff.items()})
 for i in range(4):
  for g,offset in first.items():assert firstactual[origins[i]+rot[i]*g]==entries[i]+offset
 assert sorted((xy(pt),t)for pt,t in firstactual.items())==sorted((a['cell'],a['time'])for a in row['original_first_reads']);assert max(firstactual.values())==T-1 and max(deaths[tag]for tag in range(-16,0))==T-1
 BT,pt,ht=snap[T];assert pt==(n+7)+(5*n-1)*1j and ht==3 and BT[q]==b and deaths[b]==c and c-T==104*n-445 and max(abs((q-pt).real),abs((q-pt).imag))==2*n-4
 actualfull=[dict(cell=xy(z),lifetime=tag,death=deaths.get(tag))for z,tag in sorted(BT.items(),key=lambda r:(r[0].real,r[0].imag))];assert actualfull==row['complete_cut_full_field']
 # Independent full-lifetime extrema, with exact set comparisons at all three renewal cuts.
 live={-i-1:z for i,z in enumerate(sorted(seed,key=lambda z:(z.real,z.imag)))};heaps=[[],[],[],[]]
 def ins(tag,z):
  live[tag]=z
  for heap,v in zip(heaps,[z.real,-z.real,z.imag,-z.imag]):heapq.heappush(heap,(v,tag))
 for tag,z in list(live.items()):ins(tag,z)
 prev=None;maxpop=0;profiles=[]
 for t,head in enumerate(positions):
  if live:
   for heap in heaps:
    while heap[0][1]not in live:heapq.heappop(heap)
   xlo,xneg,ylo,yneg=[heap[0][0]for heap in heaps];radius=int(max(abs(xlo-head.real),abs(-xneg-head.real),abs(ylo-head.imag),abs(-yneg-head.imag)))
  else:radius=0
  if prev is not None:assert abs(radius-prev)<=1
  prev=radius;maxpop=max(maxpop,len(live))
  if t in snap:
   field=snap[t][0];exact={z for z,tag in field.items()if tag in deaths};assert set(live.values())==exact;assert radius==max([0]+[int(max(abs((z-head).real),abs((z-head).imag)))for z in exact]);profiles.append(dict(cut=t,rho=radius,whole_relevant_mass=len(live),whole_relevant=sorted(map(xy,live.values()))))
  if t==len(seq):break
  tag=oldtags[t]
  if tag is None:
   if t in deaths:ins(t,head)
  else:assert tag in live;del live[tag]
 assert profiles==row['near_renewal_radius']and maxpop==432 and profiles[1]['rho']==n*2+36 and profiles[1]['whole_relevant_mass']==254
 controls.append(dict(n=n,reads=len(seq),renewal_cut=T,full_radius=profiles[1]['rho'],relevant=254,marker_lower_bound=2*n-4,tail_tests=tests))
# Exact temporal regression plus analytic endpoint proof: consecutive intervals interleave;
# d_j=(j+2)^2-1 < b_(j+2)+1. At t=n^2+r, 0<=r<=2n,
# use n-1 if r<=n, else n: both elapsed/remaining are >=n.
for n in range(2,1001):
 for r in range(2*n+1):
  t=n*n+r;j=n-1 if r<=n else n;assert j*j+1<=t<=(j+2)**2-1 and min(t-j*j,(j+2)**2-1-t)>=n
for z in J['non_ant_interval_regressions']:
 n=z['m'];mins=[max(min(t-j*j,(j+2)**2-1-t)for j in(n-1,n)if j*j+1<=t<=(j+2)**2-1)for t in range(n*n,(n+1)**2)];assert min(mins)==z['min_two_sided_depth']
out=dict(status='PASS exact relevant-radius evolution, non-ant interval distinction and all-n uniform cohort-renewal obstruction',manifest=sha(MF),script=sha(S),controls=controls,analytic_review=['At any actual update, C* changes only by removing the BLACK head lifetime or adding a future-consumed newly born R at the head. Its old-head radius remains unchanged, including empty/head-only radius0; the unit move changes maximum L-infinity distance by at most1. This is retrospective and not a future-fate algorithm.','Once finitely many relevant original lifetimes retire, every radius witness is R-born. Unit-speed birth-to-cut and cut-to-death paths give elapsed and remaining times at least rho. Nontranslation therefore forces two-sided lifetime clearance at every late cut via signed compact-recurrence criterion, not merely isolated long intervals.','NON-ANT intervals b_n=n^2,d_n=(n+2)^2-1 have overlap at most2 and strict endpoint order/no containment. At t=n^2+r use n-1 for r<=n, n otherwise, proving clearance>=n. This refutes a temporal nesting deduction only, not any ant/geometric theorem.','All-even-n>=20 signed full16-cell family gives fourth source entry676n-821 and last original first-read offset58. Therefore complete original-cohort retirement cut676n-762 has true pose(n+7,5n-1),W from literalG59. Original marker(3n,3n+3) still survives to780n-1207, giving rho>=2n-4 under entire all-future relevant cap432. No interpolation from controls used.','Full n20/40/80 histories, original lifetimes, all finite C* radius updates, complete renewal fields and infinite tail parity independently replayed. Measured radii76/116/196 are controls only. The result defeats a uniform radius bound based only on initial cohort size16 and population cap432 at cohort completion. Each orbit eventually captures, so orbit-dependent eventual compact recurrence, persistent single-orbit rho escape and universal attraction remain unresolved.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
