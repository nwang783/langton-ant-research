from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'second_ordinary_after_first_foreign_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
man=D/'small_second_ordinary_geometry_manifest.json';assert sha(man)=='6d2d6a5811faaae52db980edfd0c03180f303431331abd4f2824d76dc05f3690';mf=json.loads(man.read_text())
for p,h in mf['files'].items():assert sha(D/p)==h
for p,h in mf['dependencies'].items():assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_foreign_kinked_barrier_turn_independent.py'))};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns);W,M,walk,center,xy,meet,cross,minus=[ns[k]for k in ['W','M','walk','center','xy','meet','cross','minus']];a=json.loads((D/'small_second_ordinary_geometry.json').read_text());tr={x:walk(W[x])for x in 'DCVUFQB'}
def pose(x,p=0j,h=0):return p+tr[x]['p']*(-1j)**h,(h+tr[x]['h'])%4
def chord(x,p=0j,h=0):q,k=pose(x,p,h);return xy(center(p,h)),xy(center(q,k))
def pieces(x,p=0j,h=0):
 pts=[xy(center(p,h)),xy(center(*pose('F',p,h)))];ep=pose(x,p,h)
 if x!='F':pts.append(xy(center(*ep)))
 return list(zip(pts,pts[1:])),ep,pts
assert all((W[x]+M).startswith(M)for x in 'DCVU')
triples=[];local=[]
for A in 'FQB':
 pcs,pp,pts=pieces(A);low=min(q[1]for q in pts);assert pp[1]==2 and xy(center(*pp))[1]==low
 for b1 in 'DCVU':
  c1=chord(b1,*pp);p2=pose(b1,*pp);assert c1[1][1]<low
  for b2 in 'DCVU':
   c2=chord(b2,*p2);assert max(q[1]for q in c2)<low and all(meet(*pc,*c2)is None for pc in pcs)
   hi=meet(*c1,*c2)
   if cross(minus(c1[1],c1[0]),minus(c2[1],c2[0])):assert hi[:2]==(F(1),F(0))
   else:assert hi==(c1[1],) and c1[1]==c2[0]
   triples.append((A,b1,b2,c1,c2))
   rr=next(z for z in a['all48_foreign_first_second_chord_clearance_rows']if(z['foreign'],z['first_ordinary'],z['second_ordinary'])==(A,b1,b2));assert list(map(list,c1))==rr['first_chord']and list(map(list,c2))==rr['second_chord']
assert len(triples)==48
contacts=[];collinear=[]
for old in 'VU':
 oc=chord(old);fp=pose(old)
 for A in 'FQB':
  _,pp,_=pieces(A,*fp)
  for b1 in 'DCVU':
   p2=pose(b1,*pp)
   for b2 in 'DCVU':
    nc=chord(b2,*p2);hit=meet(*oc,*nc)
    if hit is None:continue
    den=cross(minus(oc[1],oc[0]),minus(nc[1],nc[0]))
    if not den:collinear.append((old,A,b1,b2,hit));continue
    ss,tt,_=hit;assert 0<=ss<1 and 0<tt<=1
    w=W[old]+W[A]+W[b1]+W[b2]+M;z=walk(w);assert not z['feasible'];contacts.append((old,A,b1,b2,z['i'],xy(z['q']),z['first']))
assert collinear==[]
assert {q[:4]for q in contacts}=={('V','F','C','V'),('V','F','C','U'),('U','F','C','U'),('U','Q','C','U')}
cu=walk(W['C']+W['U']+M);assert not cu['feasible']and(cu['i'],cu['first'])==(29,1)
z=walk(W['V']+W['F']+W['C']+W['V']+M);assert(z['i'],z['first'],z['q'])==(102,2,-1-1j);assert z['i']-len(W['V']+W['F']+W['C'])==13
# Formal clock sum with a fixed firstforeign and no new foreign wrap.
ranks={'U':0,'V':1,'D':2,'C':2};angles=[]
for b1 in 'DCVU':
 c=(b1=='C')
 for old in 'DCVU':
  for b2 in 'DCVU':
   for n in range(5):
    if old=='C'and n==0:continue
    N=n+c
    if N>4 or(N==0 and ranks[old]<=ranks[b2])or(N==4 and ranks[old]>=ranks[b2]):continue
    angles.append((old,b1,b2,n,N,(2-N)%4,(-n)%4))
assert len(angles)==217 and Counter(z[1]for z in angles)=={'D':56,'C':49,'V':56,'U':56}
refs={(z['old_source'],z['first_ordinary'],z['second_ordinary'],z['actual_old_source_to_FOREIGN_C_age'],z['total_ordinary_C_before_second'],z['second_heading_relative_old_source'],z['foreign_heading_relative_old_source'])for z in a['conditional217_old_source_angle_interfaces']};assert refs==set(angles)
out={'status':'PASS small second-ordinary local geometry/last-old-base cuts and conditional angle interface only','author_manifest':sha(man),'local_triples':48,'distinct_ordinary_joins':16,'immediate_old_V_U_contexts':96,'all_four_contacts':contacts,'additional_parallel_contacts':collinear,'conditional_angle_cases':217,'by_first_atom':dict(Counter(z[1]for z in angles)),'analytic_review':[
'At the actual F/Q/B entry normalization, all repaired foreign pieces lie at or above their terminal correctedY. The first S ordinary chord drops by at least2 doubled units. The second S chord dropsY or, after firstC, its E chord never increasesY. Its entire chord is therefore strictly below every actual foreign piece. The F56 internal cut is a real finecut, not a new core.',
'Each first ordinary chord is strictly Y-decreasing; the second begins at its minimum. A horizontal secondU after firstC touches only the endpoint; parallel D/C continuations also share only that point. Thus all sixteen ordinary joins are genuine adjacency only, with no hidden reversal/overlap.',
'Actual complete-old8/firstforeign adjacency leaves only a plainV/U last base. The conservative96 contexts include even forbiddenV/B pairs. Fresh closed-segment intersections, including parallel cases and endpoints, yield exactlyfour positive contacts and NO ignored parallel contact. Three contain immutable rawCU repeatedL29/1; VFCV requires oldcore(-1,-1)L again102 afterL2, finalVtick13/read14. No history or prepared exterior can repair an unread same-color conflict.',
'Two successive actual RAW words plus final actualM11 supply the first returned atom context too, including rawD length10. Therefore the signed one-return proxy theorem applies to the whole preceding arc, and any new second contact must source from an earlier preforeign atom, not A,b1 or the lastoldV/U.',
'With exactly one foreign and preceding-C bit0, adding b1 contributes exactly one quarter-clock iff b1=C. The tangent is(N+2)pi/2+alpha(old)-alpha(b2), N=n+1[b1=C]. Jordan-first-contact reasoning yields0<=N<=4 and the same strict endpoint ranks. Genuine oldC additionally requires n>=1. This gives217 angle-only cases; the actual funding age at foreign remains n (or n+j-1 for oldC), NEVER N.',
'No older-source position catalogue, second-return simplicity, postforeign old8 maturation, invented returned fullproducer, secondforeign theorem or capture follows. Foreign/core/b1 identity transfer remains a genuine missing contract.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
