from pathlib import Path
from itertools import product
import hashlib,json,collections
R=Path('/workspace/shared/langton');P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for l in(P/'DRIFT31_MIDDLE_READ_SHA256SUMS').read_text().splitlines():h,f=l.split(None,1);assert sha(P/f)==h
J=json.loads((P/'drift31_circle_middle_reads_certificate.json').read_text());src=json.loads((P/'drift31_single_used_g8_shapes_certificate.json').read_text())
v=[1j,1,-1j,-1];d=3+1j;lev=lambda p:int(3*p.imag-p.real);o=lambda h,r:(h+(1 if r%2==0 else-1))%4
rank=lambda w,h,ot=False:[r for r,a in enumerate(w)if(o(a,r)if ot else a)==h]
def graph(H):
 su={};pr={};events={(t,r)for t,w in H.items()for r in range(len(w))}
 for t,w in H.items():
  for h in range(4):
   q=-t+v[h];u=lev(q);k=int(q.imag)
   if u not in H:continue
   aa=rank(w,h,True);bb=rank(H[u],h);assert len(aa)==len(bb)
   for a,b in zip(aa,bb):su[t,a]=((u,b),k);pr[u,b]=((t,a),k)
 chains=[];seen=set();skips=[]
 for st in sorted(events-set(pr)):
  at=st;k=0;seq=[];prev={}
  while True:
   assert at not in seen;seen.add(at);seq.append((at,k));t,r=at;p=-t+k*d
   if p in prev:
    b,j=prev[p]
    if r!=b+1:skips.append((b,r,seq[j:]))
   prev[p]=(r,len(seq)-1)
   if at not in su:break
   at,dk=su[at];k+=dk
  chains.append(seq)
 assert seen==events
 return su,chains,skips
counts=collections.Counter();surv=[];allret=[]
for placement in src['all_quadruple_placements']:
 if placement['outcome']!='OPEN_circle_interface':continue
 base={int(k):w for k,w in placement['complete_circle_histories'].items()}
 for h6 in placement['first_exterior_cell_T6']['all_complete_domains']:
  H={**base,6:h6};su,chains,skips=graph(H);assert not skips
  row=next(q for q in J['all20_T6_cases']if q['circle_histories']==[base[t]for t in range(6)]and q['T6_history']==h6)
  rel=[];pathmap={}
  for seq in chains:
   (t,r),k=seq[0];ih=H[t][r];start=-t-v[ih]
   (u,s),kk=seq[-1];oh=o(H[u][s],s);end=-u+kk*d+v[oh]
   if lev(start)!=7 or start!=end:continue
   assert all(-a+z*d!=start for(a,b),z in seq)
   a=rank(H[t],ih).index(r);b=rank(H[u],oh,True).index(s);assert(ih,oh)==(2,3)
   key=(a,b,len(seq)+1);rel.append(key);pathmap[key]=(start,seq)
  assert set(rel)=={(p['outgoing_ordinal'],p['incoming_ordinal'],p['duration'])for p in row['actual_T7_first_returns']}
  for p in row['actual_T7_first_returns']:
   key=(p['outgoing_ordinal'],p['incoming_ordinal'],p['duration']);start,seq=pathmap[key]
   assert [int(start.real),int(start.imag)]==p['physical_base']and json.dumps(seq)==json.dumps(p['lower_chain'])
  I=len(rank(h6,3,True));bound=2*(I+3);assert row['T7_incoming_W_outgoing_S']==[I,3]and row['T7_derived_bound']==bound
  rb=any((a,b)==(1,0)for a,b,L in rel)and any(a==2 and b!=1 for a,b,L in rel)
  if rb:
   assert row['outcome']=='rotated_first_arrival_Rule_B';counts['Rule_B_T6_modes']+=1;continue
  dom=[]
  for n in range(bound+1):
   for w in product((1,3),repeat=n):
    wi=rank(w,3);so=rank(w,2,True)
    if len(wi)!=I or len(so)!=3:continue
    if all(wi[b]==so[a]+1 for a,b,L in rel):dom.append(list(w))
  assert dom==row['complete_T7_domain']
  for w in dom:
   su,ch,bad=graph({**H,7:w});q=next(q for q in row['all_domain_outcomes']if q['history']==w)
   if bad:
    assert q['outcome']=='skipped_rank';ww=q['witness'];sg=ww['segment'];found=False
    for b,a,path in bad:
     if (b,a)==(ww['rank_before'],ww['rank_after'])and json.dumps(path)==json.dumps(sg):found=True;assert len(path)==5 and(b,a)in[(1,4),(2,5)]
    assert found;counts['skipped_rank']+=1
   else:assert q['outcome']=='open';counts['open']+=1;surv.append((base[5],h6,w))
assert dict(counts)==J['counts']and len(surv)==8
assert {(tuple(a),tuple(b),tuple(c))for a,b,c in surv}=={(tuple(q['T5']),tuple(q['T6']),tuple(q['T7']))for q in J['eight_OPEN_interfaces']}
report={'status':'PASS conditional all-cap complete middle-read reduction for the two supplied single-used F-circle inventories','proof_sha256':sha(P/'DRIFT31_CIRCLE_MIDDLE_READ_REDUCTION.md'),'certificate_sha256':sha(P/'drift31_circle_middle_reads_certificate.json'),'script_sha256':sha(Path(__file__)),'counts':dict(counts),'open_histories':surv,'analytic_checks':['All omitted levels UNKNOWN; exact physical voltage y with full drift(3,1), not primitive folding','All boundary-return paths have exact same physical start/end and no intervening read of that cell; every ordinal and full lift reconstructed','Rotated RuleB: before first W, all arrivals E. Its immediately preceding read is the specified S departure, hence an E/R read. First W is therefore L and itself the next S departure ordinal. The other fixed return from that departure skips the required W1','Complete binary words through derived n<=2(I+3), no external/global cap, regenerate all18 final words; ten explicit length-four skipped-rank paths reject and eight remain necessary OPEN'],'not_claimed':['complete controller','growth8 exclusion','single-used F-circle existence']}
p=R/'audits/drift31_middle_reads_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
