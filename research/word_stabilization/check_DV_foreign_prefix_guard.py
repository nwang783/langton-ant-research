"""Fixed D/V-source first-F-prefix retirement/predecessor interface.
No ant-prefix tree, corpus expansion or bounded no-hit claim.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,hashlib,importlib.util
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent;W=ROOT/'core_periodicity_new';S=ROOT/'seven_word_spatial_return_2026-10-23'
sp=importlib.util.spec_from_file_location('literal',HERE/'check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry']
WP=HERE/'shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';words=[r['word']for r in json.loads(WP.read_text())['macro_words']]
IP=S/'foreign_first_contact_interface.json';I=json.loads(IP.read_text())
CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,z.split()[:8])) for z in CP.read_text().splitlines()}
keep=[0,1,4,5,6,7,8,9];compact={a:i for i,a in enumerate(keep)}
ST={0:(2,2),1:(2,2),4:(2,6),5:(2,6),6:(2,6),7:(0,8),8:(0,8),9:(0,8)}
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def chord(p,h,a):
 c=add((2*p[0],2*p[1]),lit.rot((-1,-1),h));return c,add(c,lit.rot(ST[a],h))
def hit(a,b,c,d):
 u,v,z=sub(b,a),sub(d,c),sub(c,a);de=cross(u,v)
 if de:
  s,t=Q(cross(z,v),de),Q(cross(z,u),de)
  return dict(s=str(s),t=str(t)) if 0<=s<=1 and 0<=t<=1 else None
 if cross(z,u):return None
 k=0 if u[0] else 1;x,y=Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k]);lo=max(Q(0),min(x,y));hi=min(Q(1),max(x,y))
 return dict(s_interval=[str(lo),str(hi)]) if lo<=hi else None

def endpoint_may(d,h,n):
 """Exact zero/one-C atomic endpoint relation; >=2 deliberately unrestricted."""
 if n>=2:return True
 d=lit.rot(d,-h)
 if n==0:
  x,y=d
  return x>=0 and any(y-x-2*v>=0 and (y-x-2*v)%4==0 for v in range(x+1))
 assert n==1
 # N zero-run, C_N=(0,1), W zero-run. All zero-run y increments >=0.
 x,y=d[0],d[1]-1
 if y<0:return False
 for dn in range(y+1):
  for vn in range((y-dn)//3+1):
   for un in range((y-dn-3*vn)//4+1):
    rem=y-dn-3*vn-4*un
    for dw in range(rem+1):
     vw=rem-dw;fouruw=dn+vn-dw-3*vw-x
     if fouruw>=0 and fouruw%4==0:return True
 return False

retire_cache={}
def retirement_certificate(si,out,N,goal):
 key=(si,out,N,goal)
 if key in retire_cache:return retire_cache[key]
 qs=[];sur=[];src=chord((0,0),0,si)
 for n in range(N+1):
  h=(-n)%4
  for a in keep:
   c=G[a]['name'].count('C')
   for z in G[a]['inputs']:
    p=sub(out,lit.rot(z,h));ck=(compact[si],compact[a],*p,h,*out,min(n,5));contact=hit(*src,*chord(p,h,a))
    ep=add(p,lit.rot(G[a]['endpoint'][:2],h));eh=(h+G[a]['endpoint'][2])%4
    source_Cs=G[si]['name'].count('C');source_exit=G[si]['endpoint']
    if (sum(p)+h)%2:why='sector'
    elif ck in COUNT:why='signed_count5'
    elif n<source_Cs:why='before_actual_full_source_completion'
    elif n+c>N:why='full_tail_late'
    elif not endpoint_may(sub(p,source_exit[:2]),source_exit[2],n-source_Cs):why='source_to_clearer_zero_one_C_endpoint'
    elif contact is not None:
     why='earlier_source_base_closed_contact'
     # A positive-C gap puts at least one intervening C atom between bases.
     assert n>=1,(si,out,N,goal,n,a,z,p,ck,contact)
    elif not endpoint_may(sub(goal[:2],ep),eh,N-n-c):why='exact_zero_one_C_endpoint'
    else:why='permissive_survivor';sur.append(dict(age=n,consumer=G[a]['name'],input=z,pose=(*p,h),full_exit=(*ep,eh),remaining_Cs=N-n-c))
    qs.append(dict(age=n,consumer=G[a]['name'],input=z,pose=(*p,h),count_key=ck,reason=why,base_contact=contact))
 cert=dict(source=G[si]['name'],output=out,goal=goal,goal_clock=N,queries=qs,reason_counts=dict(Counter(q['reason'] for q in qs)),survivors=sur)
 retire_cache[key]=cert;return cert

# Bind and independently rederive the finite predecessor alphabet, not merely
# a graph label relation. It is used only for FIRST foreign after complete8.
pair_rows=[];pair_allowed={}
for a in keep:
 for fi in (4,5,6):
  tr=lit.trace(G[a]['word']+words[fi]+lit.M)
  pair_rows.append(dict(predecessor=G[a]['name'],foreign=fi,result=tr if not tr['feasible'] else dict(feasible=True)))
  if tr['feasible']:pair_allowed.setdefault(fi,[]).append(a)
assert pair_allowed=={4:[4,7],5:[4,7],6:[7]}

rows=[]
for interface in I['rows']:
 atom=interface['source_atom']
 if atom not in ('D','V'):continue
 N=interface['permitted_C_ages'][0];p=tuple(interface['foreign_pose']);h=p[2]
 for fi in (4,5,6):
  req=lit.trace(words[fi]+lit.M);assert req['feasible']
  for si in ((0,1) if atom=='D' else (4,5,6)):
   for pre in pair_allowed[fi]:
    v=lit.rot(G[pre]['endpoint'][:2],h);pp=(p[0]-v[0],p[1]-v[1],h)
    reason=None;hard=None;contact=hit(*chord((0,0),0,si),*chord(pp[:2],h,pre))
    sc=G[si]['name'].count('C');se=G[si]['endpoint']
    if sc>N:reason='source_tail_late'
    elif contact is not None:reason='immediate_predecessor_earlier_source_contact'
    elif not endpoint_may(sub(pp[:2],se[:2]),se[2],N-sc):reason='source_to_predecessor_endpoint'
    if reason is None:
     for out in map(tuple,G[si]['outputs']):
      local=lit.rot(sub(out,p[:2]),-h);read=req['first'].get(local)
      if local in lit.K or read and read[0]=='R':
       cert=retirement_certificate(si,out,N,p)
       if not cert['survivors']:
        reason='foreign_old_output_unretirable';hard=dict(output=out,foreign_local=local,foreign_first_read=read,core=local in lit.K,certificate_key=repr((si,out,N,p)));break
    if reason is None:reason='remaining_D_age1_or2'
    rows.append(dict(source_atom=atom,full_source=G[si]['name'],full_source_id=si,foreign=fi,pose=p,age=N,
      immediate_predecessor=G[pre]['name'],predecessor_pose=pp,predecessor_contact=contact,reason=reason,hard_output=hard))
co=Counter(r['reason'] for r in rows)
assert len(rows)==270 and co=={'source_tail_late':15,'immediate_predecessor_earlier_source_contact':35,
 'source_to_predecessor_endpoint':35,'foreign_old_output_unretirable':174,'remaining_D_age1_or2':11}
remaining=[r for r in rows if r['reason']=='remaining_D_age1_or2']
assert Counter((r['source_atom'],r['age'],tuple(r['pose'])) for r in remaining)=={('D',1,(-2,3,3)):7,('D',2,(-4,-2,2)):4}

# Exact one-C endpoint equations, with an obligatory N base before the sole
# C when the chosen full source is plain D. Enumerate counts, not ant prefixes.
one_C_counts=[]
for dn in range(2):
 for vn in range(1):
  for un in range(1):
   for dw in range(2):
    for vw in range(2):
     if dn+3*vn+4*un+dw+vw!=1:continue
     q=dn+vn-dw-3*vw+3
     if q<0 or q%4:continue
     uw=q//4
     if dn+vn+un<1:continue
     one_C_counts.append((dn,vn,un,dw,vw,uw))
assert one_C_counts==[(1,0,0,0,0,1)]
zero_W_counts=[]
for dw in range(2):
 for vw in range(2):
  if dw+vw!=1:continue
  q=3-dw-3*vw
  if q>=0 and q%4==0:zero_W_counts.append((dw,vw,q//4))
assert zero_W_counts==[(0,1,0)]
literal_ends=[]
for seq in ((0,1,7),(1,4)):
 ep=(0,0);h=0
 for a in seq:
  ep=add(ep,lit.rot(G[a]['endpoint'][:2],h));h=(h+G[a]['endpoint'][2])%4
 assert (*ep,h)==(-2,3,3)
 for fi in (4,5,6):
  tr=lit.trace(''.join(G[a]['word'] for a in seq)+words[fi]+lit.M);assert not tr['feasible']
  literal_ends.append(dict(sequence=[G[a]['name'] for a in seq],foreign=fi,conflict=tr))

# Four age-two cases require a genuinely current incoming predecessor bud.
# Source D is noninitial on a U-entry history, and all8 contexts miss(1,-1).
incoming=(1,-1);incoming_rows=[]
incoming_producer_roles=[]
for a in keep:
 ep=G[a]['endpoint'];slot=add(ep[:2],lit.rot(incoming,ep[2]))
 assert list(slot) in G[a]['outputs']
 incoming_producer_roles.append(dict(full_producer=G[a]['name'],full_output=slot,
   full_C_count=G[a]['name'].count('C'),post_exit_clock_at_D_entry=0))
for a in keep:assert incoming not in lit.trace(G[a]['word']+lit.M)['first']
for r in remaining:
 if r['age']!=2:continue
 p=r['pose'];loc=lit.rot(sub(incoming,p[:2]),-p[2]);read=lit.trace(words[r['foreign']]+lit.M)['first'][loc]
 assert loc==(-5,-1) and read==('R',54)
 incoming_rows.append(dict(full_source=r['full_source'],foreign=r['foreign'],predecessor=r['immediate_predecessor'],pose=p,incoming_bud=incoming,foreign_local=loc,read=read,post_exit_C_clock=2))
assert len(incoming_rows)==4

deps=[GP,WP,IP,CP,HERE/'check_foreign_return_interfaces.py',S/'foreign_first_contact_manifest.json',
 S/'complete8_foreign_adjacency_manifest.json',W/'atomic_exit_bud_frozen_20261023_1325/manifest.json',
 W/'U_entry_simplicity_frozen_20261023_1616/manifest.json']
assert hashlib.sha256((S/'complete8_foreign_adjacency_manifest.json').read_bytes()).hexdigest()=='735023bebfa154bd936e9546023367b541006ea1d9f57bb2eb7240bf040017ea'
out=dict(status='AUTHOR_EXACT_DV_SOURCE_PREFIX_INTERFACE_PENDING_INDEPENDENT_REPLAY',
 scope='Actual U-entry uninterrupted complete-eight history until FIRST foreign. Earlier outgoing base D/V only; no actual C-source mapping, foreign Q/B-tail, or postforeign extension. All previousC branches removed only by signed complete8 adjacency.',
 pair_rows=pair_rows,allowed_predecessors=pair_allowed,case_counts=dict(co),cases=rows,
 retirement_certificates={repr(k):v for k,v in retire_cache.items()},
 endpoint_interface='Exact zero/one-C endpoint semigroup; two or more remaining Cs always admitted, a deliberately permissive overapproximation.',
 one_C_endpoint_counts=one_C_counts,DC_source_zero_W_counts=zero_W_counts,
 six_exact_literal_completion_conflicts=literal_ends,incoming_bud_full_producer_roles=incoming_producer_roles,
 incoming_bud_age2_conflicts=incoming_rows,
 conclusion='No D/V-source first contact in the common F-prefix after an actual U-entry eight interval. C-source and foreign tails remain explicit separate obligations.',
 dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps})
(HERE/'DV_foreign_prefix_guard.json').write_text(json.dumps(out,indent=2)+'\n')
print('270 cases',dict(co));print('50 retirement certificates:',len(retire_cache),'query rows',sum(len(c['queries'])for c in retire_cache.values()))
print('remaining7age1: two exact word types, all six literal conflicts; remaining4age2: incoming bud WHITE at54')
