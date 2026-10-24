from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1]
ns={'__file__':str(R/'audits/check_foreign_U_tag_interfaces_independent.py')};exec(Path(ns['__file__']).read_text().split('results={}')[0],ns)
G,G8,W,M,K,L,Z,at,xy,walk,oldcenter=(ns[k]for k in('G','G8','W','M','K','L','Z','at','xy','walk','oldcenter'))
gates=set()
for a in'FQB':
 for tag in L:
  for slot in G[a]['I']:
   for h in range(4):
    p=tag-at(slot,0,h)
    if(int(p.real+p.imag)+h)%2 or L&{at(q,p,h)for q in K|G[a]['white']}or oldcenter(p,h):continue
    gates.add((a,p,h))
assert len(gates)==69
guards={-1-1j,-1+1j,-1j,2j};last={q:G['U']['rawreads'][q][-1]for q in guards}
assert set(last.values())=={(2,'L'),(14,'L'),(3,'L'),(20,'L')}
assert G['C']['I']==set() and G['C']['O']=={1+2j,2,2+1j}
for a in'DCVU':
 assert all(q.imag>=0 and q.real+q.imag>=0 for q in G[a]['O'])
for a in'DVU':assert G[a]['p'].imag>=G[a]['p'].real>=0 and G[a]['h']==0
assert G['C']['p']==1j and G['C']['h']==3
roles=[]
for q in sorted(guards,key=lambda z:(z.real,z.imag)):
 assert q.imag<4 and q.imag-q.real<5
 for a in'DVU':
  for slot in G[a]['O']:
   p=q+slot;hits=L&{p-z for z in G[a]['ctx']};why='sector'if(int(p.real+p.imag)+2)%2 else'held_star'
   if why=='held_star':assert hits
   roles.append((xy(q),a,xy(slot),xy(p),why))
assert len(roles)==64 and Counter(r[-1]for r in roles)=={'sector':32,'held_star':32}
S=[]
for a,p,h in gates:
 if h!=2:continue
 inp={p-z for z in G[a]['I']};bad={p-z for z in K|G[a]['white']};hit=inp&guards
 if hit:why='source_deletion_guard'
 elif(a,p)==('Q',-2-4j):assert bad&{2,2+1j};why='right_renewal_requires_clock4'
 else:
  assert(a,p)==('B',-1-5j);pred=p+G['U']['p'];assert L&{pred-z for z in G['U']['ctx']};why='only_U_predecessor_context'
 S.append((a,*xy(p),why))
assert len(S)==15 and Counter(r[-1]for r in S)=={'source_deletion_guard':13,'right_renewal_requires_clock4':1,'only_U_predecessor_context':1}
# Regenerate marker-only survivors directly using the signed 138-row result.
prior=json.loads((R/'audits/check_foreign_U_star_predecessors_independent.json').read_text());assert prior['status'].startswith('PASS')
author=json.loads((R/'foreign_U_star_predecessors_2026-10-23/foreign_U_star_predecessors.json').read_text());marker=set()
for r in author['rows']:
 if r['reason']!='necessary_interface_not_asserted_attained':continue
 a=r['foreign'];p=complex(*r['foreign_pose'][:2]);h=r['foreign_pose'][2];tags=L&{at(q,p,h)for q in G[a]['I']}
 if any((q-p)/((-1j)**h)not in G[a]['rawreads']for q in tags):marker.add((a,*xy(p),h))
assert marker=={('F',3,3,0),('F',3,-2,1),('Q',3,5,0)}
marker_details=[]
for a,p,h,tag in[('F',3-2j,1,1+1j),('Q',3+5j,0,1j)]:
 local=(tag-p)/((-1j)**h);assert local not in G[a]['rawreads'] and G[a]['reads'][local][0]==(len(W[a])+1,'L');assert tag in{at(q,at(G[a]['p'],p,h),(h+G[a]['h'])%4)for q in K};marker_details.append((a,xy(local),G[a]['reads'][local][0]))
bud=1+3j;local=(bud-(3-2j))/(-1j);assert local==-5-2j and local in G['F']['white'] and G['F']['rawreads'][local][0]==(53,'R')
assert G['U']['rawreads'][bud][-1]==(26,'R') and all(bud in G8[a]['O']for a in('U','UC','UCC'))
qp=3+5j;b=2+4j;vp=qp-G['V']['p'];up=qp-G['U']['p'];assert(vp,up)==(2+2j,3+1j)
assert L&{vp+z for z in G['V']['ctx']} and not L&{up+z for z in G['U']['ctx']}
assert b-up in G['U']['white'] and G['U']['rawreads'][b-up][0]==(22,'R') and b-qp in K
for a in'DCVU':assert G[a]['rawreads'][2][-1]==(8,'R') and 2 in G[a]['O']
endpoints=[]
for age,h in((3,1),(4,0)):
 for a in'DVU':
  for slot in G[a]['I']:
   p=b-at(slot,0,h);end=at(G[a]['p'],p,h)
   if age==3:
    assert end.real>=2
    if end.real==2:assert end==2+3j
   else:assert end.imag>=4
   endpoints.append((age,a,xy(slot),xy(p),xy(end)))
assert len(endpoints)==16 and sum(n==3 and e==[2,3]for n,a,s,p,e in endpoints)==3
assert qp.imag-4<qp.real
bindings={}
for dirname,wanted in [('foreign_U_star_age2_2026-10-23','fd60451d1da0ef80e2575a5a792b1744a9e23bf12d40541d4aa645712f6febfe'),('foreign_U_marker_clocks_2026-10-23','bde8e0afaf1a38b160bd4379b781db1cb95a6e8829a46dea907d1ed2b437f440')]:
 d=R/dirname;p=d/'manifest.json';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha==wanted
 for f,v in json.loads(p.read_text())['files'].items():assert hashlib.sha256((d/f).read_bytes()).hexdigest()==v
 bindings[dirname]=sha
out={'status':'PASS original U-star age-two erosion exclusion and marker-only minimum clocks','manifests':bindings,'source_deleted_cells':{str(xy(q)):v for q,v in last.items()},'source_rebirth_roles':len(roles),'source_rebirth_counts':dict(Counter(r[-1]for r in roles)),'S_gates':S,'marker_ownership':marker_details,'common_bud_endpoints':endpoints,'analytic':['The four source-deleted cells cannot supply untouched entry IDs. A later current residual identity outside the active core must be born in a genuine source tail or subsequent full producer. Before C1, outputs have y>=4; in the W phase through C2 they have y-x>=5. All guarded cells are below both thresholds. At clock2 only plain S-heading D/V/U producers can complete before the foreign; all64 output alignments are wrong-sector or hit held original star in COMPLETE context. This is not fine-time physical whiteness.','Thirteen of15 S-heading erosion gates require a guarded cell as a black residual input outside entry core. Q(-2,-4,S) needs old east disappearance and hence genuine right renewal at4, too late. B(-1,-5,S) requires the only legal plain-U predecessor, whose complete context hits the held original star. Ages0/1 remain separately signed.','For marker-only F(3,-2,E), original exitbud(1,3) is before-white at actual RAW53. Signed source-bud no-retirement-through4 rules out age3, and E heading restricts ages3 mod4, hence>=7. The original star tag is physically unread in RAW and first read by successor phase1.','For marker-only Q(3,5,N), V predecessor hits original star and U(3,1,N) requires common bud(2,4) before-white at RAW22. The first actual post-source-U atom, including an internal C tail, births that bud at source clock0. Signed maturity prevents early retirement; all16 age3/4 consumer endpoints cannot reach U(3,1,N) within clock4. At E age3, endpoint x>=2; equality forces y3 and the sole remaining C then N motion cannot reduce y to1. At N age4 endpoint y>=4 cannot reduce. Age0 fails the exact N cone. Thus Q needs>=8.','The F(3,3,N) marker pose is removed by the separately signed actual predecessor/first-right-renewal and universal bud obstruction, not by treating a prepared marker gate as automatically attained. The minimum-clock claims do not assert attainment or permanence beyond foreign entry.'],'scope':'A genuine U-family creator followed by actual complete-eight history up to its FIRST foreign. Actual source clocks and full contexts retained; no postforeign permanence, all-age erosion exclusion, physical whiteness invariant, foreign budget or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
