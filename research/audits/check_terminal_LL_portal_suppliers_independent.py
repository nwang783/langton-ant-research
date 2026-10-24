from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib,ast
S=Path(__file__).resolve();R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'terminal_LL_portal_entries_force_an_older_sideways_supplier.md':'7d52e9b3','terminal_LL_supplier_same_cycle_scope_qualifier.md':'be3d76da','check_terminal_LL_even_portal_suppliers.py':'68e25d43','check_terminal_LL_even_portal_suppliers.json':'73375971'}
for f,h in files.items():assert sha(D/f).startswith(h)
J=json.loads((D/'check_terminal_LL_even_portal_suppliers.json').read_text());lib=S.with_name('check_global_max_flow2_staircase_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('rows=[];stats=Counter()')[0],ns)
V,out,cv,string,NS,EW,test=[ns[k]for k in('V','out','cv','string','NS','EW','test')];key=lambda p:(p.real,p.imag);dom=lambda p:NS if int(p.real+p.imag)%2==0 else EW
cin=lambda w,h:tuple(i for i,x in enumerate(w)if x==h);cout=lambda w,h:tuple(i for i in range(len(w))if out(w,i)==h)
def compatible(p,w,q,z):
 h=V.index(q-p);return len(cout(w,h))==len(cin(z,h)) and len(cout(z,(h+2)%4))==len(cin(w,(h+2)%4))
def prop(ds):
 ds={p:list(ws)for p,ws in ds.items()};changed=True
 while changed:
  changed=False
  for p in ds:
   for v in V:
    q=p+v
    if q not in ds:continue
    new=[w for w in ds[p]if any(compatible(p,w,q,z)for z in ds[q])]
    if not new:return None
    if len(new)!=len(ds[p]):ds[p]=new;changed=True
 return ds
mapped={'skipped':'skipped_rank','clock':'clock_cycle','global_max':'global_C_max'}
loc=[];lc=Counter()
for a,x,y in product(map(cv,('WWE','WWEW')),NS,EW):
 r,ww=test({1:a,1+1j:cv('SSN'),2:x,2+1j:y});lc[mapped.get(r,r)]+=1
 if r=='open':loc.append((a,x,y))
assert dict(lc)==J['local_counts'] and set(tuple(map(string,z))for z in loc)==set(map(tuple,J['local_open_profiles']))
def code(hs):return tuple((int(p.real),int(p.imag),string(w))for p,w in sorted(hs.items(),key=lambda z:key(z[0])))
ref={code({complex(*ast.literal_eval(p)):cv(w)for p,w in row['histories'].items()}):row for row in J['rows']}
rows={};counts=Counter();opens=Counter();channels=[];higher=[]
for a,x,y in loc:
 fixed={1:a,1+1j:cv('SSN'),2:x,2+1j:y,1j:cv('WE'),2j:cv('SNNS'),-1+2j:cv('EEWW'),-1+1j:cv('SS'),1+2j:cv('WWEE')};points=set(fixed)
 while True:
  cand={p+v for p in points for v in V}-points;add={q for q in cand if sum(q+v in points for v in V)>=2}
  if not add:break
  points|=add
 assert len(points)==12 and points-set(fixed)=={-1+0j,0j,2+2j}
 def visit(ds):
  ds=prop(ds)
  if ds is None:return
  undec=[p for p in ds if len(ds[p])>1]
  if undec:
   p=min(undec,key=lambda p:(len(ds[p]),key(p)))
   for w in ds[p]:visit(ds|{p:[w]})
   return
  hs={p:ws[0]for p,ws in ds.items()};k=code(hs);ans,witness=test(hs);kind=mapped.get(ans,ans);assert k in ref and ref[k]['result']==kind
  assert k not in rows;rows[k]=kind;counts[kind]+=1
  if ans=='global_max':higher.append(witness)
  if ans=='skipped':assert witness[0][0]==witness[-1][0]and witness[-1][1]!=witness[0][1]+1
  if ans=='open':
   opens[tuple(map(string,(a,x,y)))]+=1;assert string(hs[2+2j])in('SNN','SNNS');su={}
   for p,w in hs.items():
    for h,v in enumerate(V):
     if p+v in hs:su.update({(p,i):(p+v,j)for i,j in zip(cout(w,h),cin(hs[p+v],h))})
   paths=[[(2+1j,0),(2+2j,1),(1+2j,1),(1+1j,0)],[(1+1j,0),(1j,0),(2j,1),(-1+2j,3),(-1+1j,1),(1j,1),(2j,2),(1+2j,2),(1+1j,1)]]
   for path in paths:assert all(su[e]==f for e,f in zip(path,path[1:]))
   assert out(hs[2],0)==1 and out(hs[2+1j],0)==0 and out(hs[1+1j],0)==3
   # v's actual R0 incoming W is supplied by X's L1, not X first R.
   assert su[2,1]==(1,0)
   if string(a)=='WWEW':assert string(y)=='WEE'and (2+1j)+2*V[y[0]]==1j
   channels.append(dict(profile=list(map(string,(a,x,y))),R=string(hs[2+2j]),three_step=[[int(p.real),int(p.imag),i]for p,i in paths[0]],eight_step=[[int(p.real),int(p.imag),i]for p,i in paths[1]]))
 visit({p:[fixed[p]]if p in fixed else dom(p)for p in points})
assert set(rows)==set(ref)and counts=={'skipped_rank':228,'global_C_max':6,'open':18}
assert opens=={('WWE','NNS','WEE'):6,('WWE','NNSS','WEEW'):6,('WWEW','NNSN','WEE'):6}
out=dict(status='PASS exact terminal LL even-portal supplier cover and qualified sideways clock/odd reservation',bindings={f:sha(D/f)for f in files},local_counts=dict(lc),closure_counts=dict(counts),open_profiles={str(k):v for k,v in opens.items()},higher_C_witnesses=higher,all18_literal_channels=channels,analytic=[
'Both actual predecessor LEFT histories WWE/WWEW and every zero-to-four WHITE reader at X/H are independently enumerated. Count-compatible closure is the three mandatory two-neighbor corners, not a radius cutoff. All252 leaves and the full13 local profiles match exact sets. Every rank rejection has a literal wrong-next-physical-rank return; six GLOBAL-M violations retain actual sector equations.',
'The GLOBAL-M anchor is valid in the rotated frame: the displayed flow1 LEFT v has equal R counts in its two incoming headings, so its opposite C sectors have equal level. The fixed portal sector supplies M; no arbitrary external first-R maximum is assumed.',
'Every necessary survivor has actual H0->R1->C1->q0 and q0->B0->Y1->Z3->A1->B1->Y2->C2->q1. Thus H.R0 is exactly three updates older than q.R0 and q first lifetime lasts eight. Complete earlier/future histories and exterior channels remain.',
'X first-R N departs E away from v; v R0 is actually supplied by X L1. H first-R W departs N sideways. No local side or predecessor fact forces H into a different b-component; mandatory qualifierbe3d explicitly allows SAME cycle, another cycle or a tree.',
'Terminal four-to-three fall forces odd H=WEE. Its physical heading recovers B=H+2v_h, so equal full-drift H classes determine equal portal classes. H has opposite R0/L1 headings unlike the portal chosen q, and cannot be an O launch witness because its required west predecessor q first-departs W away. Only these specifically distinct reservations may be added; no general older-stock or fuel budget follows.',
'The18 open networks are necessary count/rank/height/clock data, not prepared factors, complete quotients, actual global-M fields or controllers. Failed guide attempts are not exclusions.'
])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
