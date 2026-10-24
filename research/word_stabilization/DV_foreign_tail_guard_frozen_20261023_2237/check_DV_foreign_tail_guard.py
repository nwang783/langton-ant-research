"""Fixed D/V-source first-Q/B-tail retirement/predecessor interface.
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
IP=S/'foreign_tail_first_contact.json';I=json.loads(IP.read_text())
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

# Signed complete8 adjacency removes preceding-C tail branches. Q has a last
# plain V/U; B only a last plain U. No raw-DCC/DCCC grammar lift is used.
pair_allowed={5:[4,7],6:[7]};rows=[]
for f,interfaces in I['rows'].items():
 fi={'Q':5,'B':6}[f]
 for interface in interfaces:
  atom=interface['source_atom']
  if atom not in ('D','V') or 0 not in interface['preceding_C_bits']:continue
  ix=interface['preceding_C_bits'].index(0);N=interface['permitted_C_ages'][ix];p=tuple(interface['foreign_pose']);h=p[2]
  req=lit.trace(words[fi]+lit.M);assert req['feasible']
  for si in ((0,1) if atom=='D' else (4,5,6)):
   for pre in pair_allowed[fi]:
    v=lit.rot(G[pre]['endpoint'][:2],h);pp=(p[0]-v[0],p[1]-v[1],h)
    sc=G[si]['name'].count('C');se=G[si]['endpoint'];contact=hit(*chord((0,0),0,si),*chord(pp[:2],h,pre))
    reason=None;hard=None
    if sc>N:reason='source_tail_late'
    elif contact is not None:
     # At clock zero explicitly retain the legal adjacent-source exception.
     # No contact used here is the immediate successor of the source base.
     assert N>0 or (sc==0 and pp!=tuple(se))
     reason='immediate_predecessor_earlier_source_contact'
    elif not endpoint_may(sub(pp[:2],se[:2]),se[2],N-sc):reason='source_to_predecessor_endpoint'
    if reason is None:
     for out in map(tuple,G[si]['outputs']):
      local=lit.rot(sub(out,p[:2]),-h);read=req['first'].get(local)
      if local in lit.K or read and read[0]=='R':
       cert=retirement_certificate(si,out,N,p)
       if not cert['survivors']:
        reason='foreign_old_output_unretirable';hard=dict(output=out,foreign_local=local,read=read,core=local in lit.K,certificate_key=repr((si,out,N,p)));break
    if reason is None:reason='residual_D_or_V_interface'
    rows.append(dict(source_atom=atom,full_source=G[si]['name'],full_source_id=si,
      foreign=f,foreign_label=fi,pose=p,age=N,contact=interface['contact'],
      legal_F_entry_adjacent_source_endpoint=interface['legal_F_entry_adjacent_source_endpoint'],
      immediate_predecessor=G[pre]['name'],predecessor_pose=pp,predecessor_contact=contact,
      first_reason=reason,hard_output=hard))
co=Counter(r['first_reason'] for r in rows)
assert len(rows)==106 and co=={'source_tail_late':18,'immediate_predecessor_earlier_source_contact':12,
 'source_to_predecessor_endpoint':16,'foreign_old_output_unretirable':48,'residual_D_or_V_interface':12}
residual=[r for r in rows if r['first_reason']=='residual_D_or_V_interface']
assert Counter((r['source_atom'],r['foreign'],r['age'],tuple(r['pose'])) for r in residual)=={
 ('D','Q',1,(-4,3,3)):2,('D','Q',3,(3,-4,1)):4,
 ('D','B',2,(-3,-3,2)):1,('V','Q',3,(3,-2,1)):2,('V','B',3,(3,-2,1)):3}

# Q west/age1: exact endpoint count equations, no length cap.
plain_D_one_C=[]
for dn in range(2):
 for dw in range(2):
  for vw in range(2):
   if dn+dw+vw!=1 or dn<1:continue
   fouruw=dn-dw-3*vw+5
   if fouruw>=0 and fouruw%4==0:plain_D_one_C.append((dn,0,0,dw,vw,fouruw//4))
assert plain_D_one_C==[]
DC_zero_W=[]
for dw in range(2):
 for vw in range(2):
  if dw+vw!=1:continue
  fouruw=5-dw-3*vw
  if fouruw>=0 and fouruw%4==0:DC_zero_W.append((dw,vw,fouruw//4))
assert DC_zero_W==[(1,0,1)]
literal_completions=[]
for seq in ((1,0,7),(1,7,0)):
 tr=lit.trace(''.join(G[a]['word'] for a in seq)+words[5]+lit.M);assert not tr['feasible']
 literal_completions.append(dict(sequence=[G[a]['name'] for a in seq]+['Q'],conflict=tr))

# The genuine incoming bud exists because every D is noninitial on U-entry
# history. Its post-exit maturity0..2 is1325, not an unshifted full-source age.
incoming=(1,-1);incoming_roles=[]
for a in keep:
 ep=G[a]['endpoint'];slot=add(ep[:2],lit.rot(incoming,ep[2]));assert list(slot) in G[a]['outputs']
 assert incoming not in lit.trace(G[a]['word']+lit.M)['first']
 incoming_roles.append(dict(producer=G[a]['name'],full_output=slot,full_Cs=G[a]['name'].count('C')))
bud_obligations=[]
for r in residual:
 if r['source_atom']!='D' or r['age']==1:continue
 p=r['pose'];local=lit.rot(sub(incoming,p[:2]),-p[2]);read=lit.trace(words[r['foreign_label']]+lit.M)['first'][local]
 if r['age']==2:
  assert r['foreign']=='B' and local==(-4,-2) and read==('R',52)
 else:
  assert r['foreign']=='Q' and r['age']==3 and local==(-3,-2) and read==('R',57)
  pre=4 if r['immediate_predecessor']=='V' else 7;pp=r['predecessor_pose'];plocal=lit.rot(sub(incoming,pp[:2]),-pp[2])
  assert plocal not in lit.trace(G[pre]['word']+lit.M)['first']
  assert pp[0]<=0
 bud_obligations.append(dict(full_source=r['full_source'],foreign=r['foreign'],age=r['age'],pose=p,
   foreign_local=local,first_read=read,predecessor=r['immediate_predecessor'],predecessor_pose=r['predecessor_pose']))
assert len(bud_obligations)==5
age3_E_ends=[]
for a in (0,4,7):
 for z in G[a]['inputs']:
  p=sub(incoming,lit.rot(z,1));ep=add(p,lit.rot(G[a]['endpoint'][:2],1));assert ep[0]>=1
  age3_E_ends.append(dict(consumer=G[a]['name'],input=z,pose=(*p,1),exit=(*ep,1)))
assert len(age3_E_ends)==8

# Last-U lower a is a SOURCE ENTRY-CORE cell, not an entry identity that may
# be renamed. Recompute the universal produced-lower age<=2 exclusion.
lower_guard=[]
for si in keep:
 for n in range(3):
  h=(-n)%4
  for out in G[si]['outputs']:
   p=sub(out,lit.rot((-1,1),h));key=(compact[si],compact[7],*p,h,*out,n)
   reason='sector' if (sum(p)+h)%2 else 'producer_tail_late' if G[si]['name'].count('C')>n else 'signed_count5' if key in COUNT else 'OPEN'
   assert reason!='OPEN'
   lower_guard.append(dict(producer=G[si]['name'],output=out,age=n,consumer='U',input=(-1,1),pose=(*p,h),key=key,reason=reason))
assert len(lower_guard)==204
assert Counter(r['reason'] for r in lower_guard)=={'sector':104,'producer_tail_late':38,'signed_count5':62}
minimum_output_y=[]
for a in keep:
 y=min(z[1] for z in G[a]['outputs']);assert y>=0
 minimum_output_y.append(dict(full_producer=G[a]['name'],minimum_local_output_y=y))
assert [G[a]['endpoint'] for a in (0,4,7)]==[[1,1,0],[1,3,0],[0,4,0]]
core_obligations=[]
for r in residual:
 if r['source_atom']!='V':continue
 assert r['age']==3 and tuple(r['pose'])==(3,-2,1) and r['immediate_predecessor']=='U'
 pp=r['predecessor_pose'];assert pp==(-1,-2,1)
 a_global=add(pp[:2],lit.rot((-1,1),pp[2]));assert a_global==(0,-1) and a_global in lit.K
 si=r['full_source_id'];assert list(a_global) not in G[si]['outputs']
 source_raw=lit.trace(G[si]['word']);raw_last=source_raw['last'][a_global]
 assert raw_last[0]=='L'
 source_exit=G[si]['endpoint'];source_exit_core={add(source_exit[:2],lit.rot(k,source_exit[2])) for k in lit.K}
 assert a_global not in source_exit_core
 if si==4:assert G[si]['endpoint']==[1,3,0]
 else:assert G[si]['name'].count('C')>=1
 core_obligations.append(dict(full_source=G[si]['name'],foreign=r['foreign'],source_start_clock=0,
   required_U=pp,U_clock=3,required_lower_a=a_global,source_entry_core=True,source_full_output=False,
   source_exit_core=False,source_raw_final_read=raw_last,source_raw_exit_colour='WHITE',
   source_full_exit=G[si]['endpoint'],source_full_Cs=G[si]['name'].count('C'),
   required_birth_clock_at_most=0,later_clock_zero_producer_minimum_y=3 if si==4 else None))
assert len(core_obligations)==5

for r in rows:
 if r['first_reason']!='residual_D_or_V_interface':r['final_reason']=r['first_reason']
 elif r['source_atom']=='V':r['final_reason']='last_U_lower_entry_core_rebirth_too_young'
 elif r['age']==1:r['final_reason']='exact_one_C_word_or_literal_conflict'
 elif r['age']==2:r['final_reason']='incoming_bud_post_exit_age2_before_white'
 else:r['final_reason']='incoming_bud_age3_left_halfplane_then_last_base_misses'
final_counts=dict(Counter(r['final_reason'] for r in rows))
deps=[GP,WP,IP,CP,HERE/'check_foreign_return_interfaces.py',
 S/'foreign_tail_first_contact_manifest.json',S/'complete8_foreign_adjacency_manifest.json',
 W/'atomic_exit_bud_frozen_20261023_1325/manifest.json',W/'U_entry_simplicity_frozen_20261023_1616/manifest.json',
 HERE/'DV_foreign_prefix_guard_frozen_20261023_2220/manifest.json']
out=dict(status='AUTHOR_EXACT_DV_TAIL_HISTORY_GUARD_PENDING_INDEPENDENT_REPLAY',
 scope='Chronological FIRST Q/B-tail contact after actual U-entry complete-eight interval, earlier outgoing D/V base. Real full producers and all source clocks retained. No actualC-source, postforeign simplicity, generic214 coverage or global capture claim.',
 counts=dict(co),final_counts=final_counts,cases=rows,
 retirement_certificates={repr(k):v for k,v in retire_cache.items()},
 plain_D_one_C_counts=plain_D_one_C,DC_source_zero_W_counts=DC_zero_W,literal_completions=literal_completions,
 incoming_bud_full_producer_roles=incoming_roles,incoming_bud_obligations=bud_obligations,age3_E_clearer_endpoints=age3_E_ends,
 universal_U_lower_a_age0_1_2_queries=lower_guard,minimum_full_output_y=minimum_output_y,
 final_U_deleted_source_core_rebirth_obligations=core_obligations,
 clock_zero_rebirth_argument='Current final identity at source-entry-core(0,-1) must be born after source starts. Produced lower min3 at goalclock3 forces birth<=0. Positive source C tail finishes>=1, excluding all later births. PlainV ends(1,3,N)at0; any later full producer startingclock0 follows a zero-C N run, hence y>=3, and ALL8 full output localy>=0, including that producer own positive C tails. No output can be at y=-1.',
 conclusion='No D/V-source chronological first contact on the first foreign Q/B tail in this actualU-entry clean-eight scope.',
 dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps})
(HERE/'DV_foreign_tail_guard.json').write_text(json.dumps(out,indent=2)+'\n')
print('106 cases',dict(co));print('all resolved:',final_counts)
print(len(retire_cache),'retirement subproblems',sum(len(c['queries'])for c in retire_cache.values()),'rows;204 minimum-age queries')

