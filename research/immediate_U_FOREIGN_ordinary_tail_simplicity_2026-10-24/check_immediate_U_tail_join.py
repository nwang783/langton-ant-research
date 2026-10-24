"""Exact source-owner exhaustion for the SPECIAL factor U A ordinary* + M.
No second FOREIGN or general preFOREIGN D/C/V source is silently included.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def mul(k,p):return k*p[0],k*p[1]
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return (*q,h)
def center(p):return add(mul(2,p[:2]),l.rot((-1,-1),p[2]))
def contact(a,b,c,d):
 u=sub(b,a);v=sub(d,c);z=sub(c,a);det=cross(u,v)
 if det:
  s=F(cross(z,v),det);t=F(cross(z,u),det)
  return None if not(0<=s<=1 and 0<=t<=1)else dict(parallel=False,old_s=s,new_t=t,overlap=False,point=add(a,mul(s,u)))
 if cross(z,u):return None
 k=0 if v[0]else 1
 ts=[F(a[k]-c[k],v[k]),F(b[k]-c[k],v[k])];lo=max(F(0),min(ts));hi=min(F(1),max(ts))
 if lo>hi:return None
 point=add(c,mul(lo,v));kk=0 if u[0]else 1;s=F(point[kk]-a[kk],u[kk])
 return dict(parallel=True,old_s=s,new_t=lo,overlap=lo<hi,new_t_interval=(lo,hi),point=point)
DV={'D':[(2,2)],'C':[(2,2)],'V':[(2,6)],'U':[(0,8)],'F':[(-6,-2)],'Q':[(-6,-2),(0,-4)],'B':[(-6,-2),(2,-6)]}

def pieces(labels):
 p=(0,0,0);out=[]
 for i,A in enumerate(labels):
  z=center(p)
  for j,v in enumerate(DV[A]):
   d=l.rot(v,p[2]);end=add(z,d);out.append(dict(word_index=i,atom=A,piece_index=j,a=z,b=end));z=end
  p=after(W[A],p);assert center(p)==z
 return out

def verify_simple(ps):
 rows=[]
 for j in range(len(ps)):
  for i in range(j):
   old,new=ps[i],ps[j];h=contact(old['a'],old['b'],new['a'],new['b'])
   adjacent=j==i+1
   legal=bool(h and adjacent and not h['overlap']and h['point']==old['b']==new['a'])
   assert h is None or legal,(i,j,h)
   rows.append(dict(old_index=i,new_index=j,closed_contact=h,legal_only_genuine_terminal_adjacency=legal))
 return rows
# Every FORE/firstordinary local pair, including Q-tail/U codirected point.
local_pairs=[]
for A in'FQB':
 assert W[A][:11]==l.M
 pre=pieces('U'+A);verify_simple(pre)
 for b in'DCVU':
  ps=pieces('U'+A+b);local_pairs.append(dict(source_foreign=A,first_ordinary=b,pieces=ps,all_closed_pair_checks=verify_simple(ps)))
assert len(local_pairs)==12
# Ordinary adjacent pieces cannot reverse overlap, independent of rail length.
joins=[]
for a in'DCVU':
 for b in'DCVU':
  ep=after(W[a]);u=DV[a][0];v=l.rot(DV[b][0],ep[2]);assert cross(u,v)!=0 or u[0]*v[0]+u[1]*v[1]>0
  joins.append(dict(old=a,new=b,old_tangent=u,next_tangent=v,never_reversing=True))
# Real M contexts, including D10 spill. All atoms other than D contain M;
# D plus the next actual first L provides it, including final supplied M.
providers=[]
for a in'DCVUFQB':
 assert(W[a]+l.M).startswith(l.M)
 providers.append(dict(next_atom=a,own_RAW_length=len(W[a]),actual_M_source='own first11 reads'if len(W[a])>=11 else'ownD10 plus actual following firstL',prefix=(W[a]+l.M)[:11]))
spill=[]
for b in'DCVUFQB':
 assert W[b][0]=='L'and(W['D']+W[b]).startswith(l.M);spill.append(dict(after_D=b,actual_first_L=True))
assert l.M[0]=='L';spill.append(dict(after_D='actual_final_M11',actual_first_L=True))
# Three disjoint old-owner classes exhaust THIS factor, not arbitrary G7.
owner_rows=[dict(old_owner='unique preFOREIGN plain U chord, including its ENTRY',dependency='old_U_arbitrary_ordinary_tail_source_join_2026-10-24/manifest.json',why='The selected preFOREIGN complete-eight factor is exactly the actual plain U; its actual M is supplied by the next F/Q/B first11. No UC/UCC tail or old preFOREIGN D/C/V atom exists in this selected proxy.'),dict(old_owner='proper actual pieces of that FIRST F/Q/B',dependency='original_FOREIGN_all_owners_2026-10-24/manifest.json',why='All proper F-prefix/Q-tail/B-tail sources, genuine internal kink outgoing owners, and complete-context LOSS/MISS cases are signed. The FORE EXIT is not falsely foreign-owned; it routes to first ordinary b1.'),dict(old_owner='any already executed postFOREIGN ordinary D/C/V/U chord',dependency='one_foreign_all_ordinary_owners_2026-10-24/manifest.json',why='The all-owner theorem is arbitrary suffix length and includes first-D boundaries, leading C/CC and terminal DCC. This class owns the FORE EXIT when an ordinary suffix exists, and all ordinary old vertices by outgoing ownership.')]
# Whole-board positive regressions, not a source-free output permanence claim.
controls=[]
for labels in['UF','UQ','UB','UFD','UQVCCV','UBVCCV','UQCC','UBCC','UQUDCC']:
 raw=''.join(W[A]for A in labels);tr=l.trace(raw+l.M);assert tr['feasible']
 seed={q for q,(c,t)in tr['first'].items()if c=='L'};B=set(seed);p=(0,0,0);reads=[];cuts=[];ends={};off=0
 for i,A in enumerate(labels):off+=len(W[A]);ends[off]=(i,A)
 for t,c in enumerate(raw+l.M):
  q=p[:2];assert(q in B)==(c=='L')
  if c=='L':B.remove(q)
  else:B.add(q)
  reads.append(dict(tick0=t,cell=q,turn=c));p=after(c,p)
  if t+1 in ends or t+1==len(raw+l.M):cuts.append(dict(actual_read_count=t+1,boundary=ends.get(t+1),pose=p,complete_BLACK=sorted(B)))
 ps=pieces(labels);controls.append(dict(labels=labels,complete_seed=sorted(seed),mass=len(seed),all_actual_reads=reads,all_real_RAW_and_M_cuts=cuts,pieces=ps,all_closed_pair_checks=verify_simple(ps)))
D=['seven_word_spatial_return_2026-10-23/first_foreign_all_source_join_manifest.json','audits/check_first_foreign_all_source_join_independent.json','old_U_arbitrary_ordinary_tail_source_join_2026-10-24/manifest.json','audits/check_old_U_all_tail_source_join_independent.json','original_FOREIGN_all_owners_2026-10-24/manifest.json','audits/check_original_FOREIGN_all_owners_independent.json','one_foreign_all_ordinary_owners_2026-10-24/manifest.json','audits/check_all_ordinary_owner_join_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
for p in D:
 if p.startswith('audits/'):
  d=json.loads((R/p).read_text());assert d['status'].startswith('PASS')
# Immutable source-join statements are explicitly read; neither is extended
# from one/three returned atoms or from a prepared-positive absence scan.
assert 'U-source' in json.loads((R/D[2]).read_text())['scope']
assert 'ordinary outgoing old owner' in json.loads((R/D[6]).read_text())['scope']
assert 'proper piece' in json.loads((R/D[4]).read_text())['scope']

def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return{k:enc(x)for k,x in v.items()}
 if isinstance(v,(list,tuple)):return[enc(x)for x in v]
 return v
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_COMPOSITION_REVIEW',scope='Select an ACTUAL finite RAW factor whose labels are exactly U A w, A one FIRST F/Q/B immediately after that PLAIN U, w ANY finite word over D/C/V/U, with actual final M11. Arbitrary prepared/earlier physical history before selectedU is allowed, but is not drawn in this selected proxy. Its auxiliary OPEN proxy, through the last RAW of w (or A if w empty), is simple. The final real M11 is physical funding context, not an appended auxiliary D or a further complete atom. This is a SPECIAL-prefix theorem, not general G7/preFOREIGN D/C/V/multipleFOREIGN simplicity.',all3_old_owner_classes=owner_rows,all12_foreign_firstordinary_local_pairs=local_pairs,all16_ordinary_nonreversing_adjacent_joins=joins,all7_real_M_providers=providers,all8_D10_actual_spill_sources=spill,all9_complete_physical_positive_controls=controls,
 finite_to_geometry_proof=[
 'The selected plainU is an actual complete-eight U packet, not a UC/UCC tail. Its actual final M is the following FOREIGN first11. Direct closed checks and signed89 show the prefix U A is simple. If w is empty, the result already follows.',
 'Otherwise suppose a nonadjacent contact occurs, and choose its earliest new ordinary piece and first positive onset. The earlier selected proxy is simple by this stopping choice, not by an induction hypothesis. Each word/piece is injective; actual ordinary joins never reverse, and all12 initial FORE/b1 contexts have only legitimate point adjacency (Qtail/U codirected continuation included). Thus no exceptional adjacent overlap bypasses old-owner selection.',
 'An old vertex belongs to its outgoing piece. U EXIT is FORE ENTRY and is properly FORE-prefix-owned. A genuine Q/B kink is tail-owned, never an invented core. The FORE EXIT is b1-owned for a later actor; for b1 itself it is only legitimate initial adjacency. An ordinary old terminal belongs to the next already executed ordinary chord, unless it is the current actor ENTRY, which is only immediate terminal adjacency. A newENTRY repeat elsewhere would already have been the preceding executed actor END, so an earliest positive new contact can always be selected, including same-direction collinear onset and new terminal endpoints.',
 'The old owner is therefore exactly one of the three disjoint source classes above. There is only ONE old preFOREIGN atomic chord and it is genuine U; no old preFOREIGN D/C/V source can be manufactured from the unexecuted final M. Signed907 excludes that U owner; signed8da excludes any proper originalFOREIGN owner; signeda213 excludes all postFOREIGN ordinary owners including FORE-EXIT aliases, leading C/CC and terminalDCC. Each is applied at the same GLOBAL-first stopping condition and to the SAME actual finite factor and final M.',
 'All owner alternatives contradict their independently signed source theorem. Hence no such contact exists. No producer maturity or identity permanence is being reset at the FOREIGN. The argument exhausts only this special U A prefix, not arbitrary preFOREIGN G8 prefixes or anotherFOREIGN.'
 ],limits=['No generic preFOREIGN D/C/V source exclusion or arbitrary G7/secondFOREIGN theorem.','No claimed simplicity of the fine physical ant path, the physical finalM path, or a further RAW inferred from D10 inside that marker.','No all-output permanence: genuine UQ/UB VCCV controls physically erode firstV A throughCORE and remain simple.','No changes to any frozen secondFOREIGN proof dependency, automatic iteration, whole-field quotient, language coverage, finite-seed capture or physical termination.'],dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in D})
(H/'immediate_U_tail_join.json').write_text(json.dumps(enc(out),indent=2)+'\n')
print('Special U A ordinary*+realM owner exhaustion: preU / properFORE / postordinary.12 local pairs,16 joins,7 M providers+8 D spills,9 full-board positives.')
