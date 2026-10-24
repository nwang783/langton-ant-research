from pathlib import Path
from collections import Counter
import math
SELF=Path(__file__).resolve();S=SELF.with_name('check_D_first_W5_gate_independent.py');exec(compile(S.read_text().split('rows=[];late=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/three_C_center_touch_frozen_20261023_1533';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_three_C_center_touch.json').read_text());steps={'D':1+1j,'C':1+1j,'V':1+3j,'U':4j};geoms=[];center=-1-1j
for a,u0 in steps.items():
 for b,v0 in steps.items():
  u=2*u0;v=rotation(2*v0,1);corners=[center-rotation(center,1)+s*u-t*v for s in(0,1)for t in(0,1)]
  for x in range(math.ceil(min(z.real for z in corners)/2),math.floor(max(z.real for z in corners)/2)+1):
   for y in range(math.ceil(min(z.imag for z in corners)/2),math.floor(max(z.imag for z in corners)/2)+1):
    if(x+y+1)%2:continue
    p=complex(x,y);z=2*p+rotation(center,1)-center;den=det(u,v);s=Fraction(det(z,v),den);t=Fraction(det(z,u),den)
    if 0<=s<1 and 0<t<=1 and not(0<s<1 and 0<t<1):geoms.append((a,b,xy(p),s,t))
auth={(r['earlier_atom'],r['later_atom'],tuple(r['later_pose'][:2]),Fraction(r['earlier_parameter']),Fraction(r['later_parameter']))for r in J['all_24_canonical_nonproper_geometries']};assert set(geoms)==auth and len(geoms)==24
roles=[]
for a in ids:
 name='D'if a in(0,1)else'V'if a in(4,5,6)else'U';roles.append((name,a,0,0,0,counts[a]))
 for j in range(counts[a]):
  p,h,_,_=walk(raws[base[a]]+C*j);roles.append(('C',a,p,h,j,counts[a]-j))
assert len(roles)==15
for r,(name,a,p,h,j,rem)in zip(J['all_15_actual_source_roles'],roles):assert(r['atom'],r['full_source'],tuple(r['atomic_entry']),r['clock_shift'],r['remaining_C'])==(name,a,(*xy(p),h),j,rem)
# Rebuild the full obligation index sets from our complete geometric inventory.
geo_by_index={i:(r['earlier_atom'],r['later_atom'],tuple(r['later_pose'][:2]))for i,r in enumerate(J['all_24_canonical_nonproper_geometries'])}
expected_core=set();expected_retired=set()
for gi,(a,b,pp)in geo_by_index.items():
 for ri,(name,src,p,h,j,rem)in enumerate(roles):
  if name!=a:continue
  targets=(4,5,6)if b=='V'and pp==(-3,0)else(7,8,9)if b=='U'and pp==(-4,-1)else(0,1)if b=='D'and pp==(-1,0)and a in('D','C')else()
  for dst in targets:expected_core.add((gi,ri,dst))
 if a=='U'and(b,pp)in[('D',(-1,2)),('V',(-3,2)),('U',(-4,1))]:
  for src in(7,8,9):
   for dst in((0,1)if b=='D'else(4,5,6)if b=='V'else(7,8,9)):expected_retired.add((gi,src,dst))
assert len(expected_core)==108 and expected_core=={(r['geometry_index'],r['source_role_index'],r['target'])for r in J['all_108_old_core_age_cases']}
assert len(expected_retired)==24 and expected_retired=={(r['geometry_index'],r['source'],r['target'])for r in J['all_24_retired_U_input_age_cases']}

# Exact old-core and old-retired-cell bounds, including second-C containing birth.
assert all(q.imag>=0 for a in ids for q in G[a][4])
assert all(G[a][0].imag>=1 for a in(0,4,7))
for r in J['all_108_old_core_age_cases']:
 name,a,p,h,j,rem=roles[r['source_role_index']];cell=complex(*r['old_core_cell']);assert cell in K
 aa,bb,pose=geo_by_index[r['geometry_index']];slot=complex(*r['input']);assert aa==name and slot in G[r['target']][3] and complex(*pose)+rotation(slot,1)==cell
 if r['required_age_at_least']==3:
  assert p+rotation(cell,h) not in G[a][4]
  if rem:upper=3-rem
  else:
   assert j==0 and name!='C' and counts[a]==0 and cell.imag<G[a][0].imag;upper=2
 else:upper=3+j;assert r['required_age_at_least']==5
 assert upper==r['produced_age_upper'] and upper<r['required_age_at_least']
for r in J['all_24_retired_U_input_age_cases']:
 a=r['source'];cell=complex(*r['retired_original_input']);assert cell in G[a][3] and cell not in G[a][4]
 upper=2 if r['required_age_at_least']==3 else 3-counts[a]
 if r['required_age_at_least']==3:assert cell.imag<G[7][0].imag
 assert upper==r['replacement_age_upper'] and upper<r['required_age_at_least']
# Fresh literal standalone C guards and current common-output target maps.
cneed=walk(C+mark)[2];assert cneed[3j] is False and cneed[1+1j] is False
for a,b,pos,s,t in geoms:
 pp=complex(*pos)
 if b=='C'and pos==(-1,0):assert rotation(2-pp,-1)==3j
 elif b=='U'and pos==(-2,-1):assert pp+rotation(-1+4j,1)==2
 elif a=='U'and b=='C'and pos==(-1,2):assert rotation(1j-pp,-1)==1+1j
# Independently regenerate all exact minimum-age and old-output queries.
upper=[];shadow=[];lower=[]
for a in ids:
 for q in G[a][4]:
  for b in(7,8,9):
   for n in range(5):
    h=(-n)%4;p=q-rotation(-1+4j,h);cq=(mp[a],mp[b],*xy(p),h,*xy(q),n);hb=(a,b,*xy(p),h,*xy(q))
    why='BEFORE_SOURCE_EXIT'if n<counts[a]else'WRONG_SECTOR'if(int(p.real+p.imag)+h)%2 else'SIGNED_HB_EXCLUDED'if hb in HB else'SIGNED_COUNT5_EXCLUDED'
    if why=='SIGNED_COUNT5_EXCLUDED':assert cq in C5
    upper.append((cq,why))
for a in(7,8,9):
 for n in range(4):
  h=(-n)%4
  for b in ids:
   for slot in G[b][3]:
    p=1j-rotation(slot,h);cq=(mp[a],mp[b],*xy(p),h,0,1,n)
    why='BEFORE_SOURCE_EXIT'if n<counts[a]else'WRONG_SECTOR'if(int(p.real+p.imag)+h)%2 else'SIGNED_COUNT5_EXCLUDED'
    if why=='SIGNED_COUNT5_EXCLUDED':assert cq in C5
    shadow.append((cq,why))
for a in(4,5,6,7,8,9):
 assert 0 in G[a][4]
 for b in(0,1):
  cq=(mp[a],mp[b],-1,0,1,0,0,3);excluded=cq in C5
  assert excluded or(a in(4,5,6)and b==0)
  lower.append((a,b,cq,excluded))
for name,actual in [('all_1020_upper_minus1_4_age_five_queries',upper),('all_276_U_output_0_1_early_retirement_queries',shadow)]:assert set(actual)=={(tuple(r['query']),r['reason'])for r in J[name]}
assert len(upper)==1020 and len(shadow)==276 and len(lower)==12
assert {(a,b,cq,excluded)for a,b,cq,excluded in lower}=={(r['source'],r['target'],tuple(r['query']),r['reason']=='SIGNED_COUNT5_EXCLUDED')for r in J['all_12_old_source_0_0_to_D_queries']}
# Completely fresh literal boards, ordered identities, and exact first contacts.
controls=[]
for sup in J['two_actual_boundary_controls']:
 word=sup['word'];raw=''.join(raws[a]for a in word);need=walk(raw+mark)[2];seed={q for q,c in need.items()if c};assert set(map(xy,seed))==set(map(tuple,sup['seed']))
 field=set(seed);ledger={q:('entry',None,None)for q in seed-K};p=0j;h=0;clock=0;edges=[];lastcons=None
 for pi,a in enumerate(word):
  assert field==set(ledger)|{p+rotation(q,h)for q in K} and not(set(ledger)&{p+rotation(q,h)for q in K})
  cons=[]
  for q in G[a][3]:cons.append(ledger.pop(p+rotation(q,h)))
  for q in G[a][4]:z=p+rotation(q,h);assert z not in ledger;ledger[z]=(a,q,clock)
  lastcons=cons
  for atom,wr in [('D'if base[a]==0 else'V'if base[a]==4 else'U',raws[base[a]])]+[('C',C)]*counts[a]:
   begin=2*p+rotation(center,h);oldclock=clock
   for c in wr:
    assert(p in field)==(c=='L');field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
   clock+=atom=='C';finish=2*p+rotation(center,h);edges.append((atom,begin,finish,oldclock))
  assert field==set(ledger)|{p+rotation(q,h)for q in K}
 assert lastcons==[(6,0j,0 if word[0]==6 else 0)]
 for c in mark:assert(p in field)==(c=='L');field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 hits=[]
 for bi,(_,b0,b1,bc)in enumerate(edges):
  for ai,(_,a0,a1,ac)in enumerate(edges[:max(0,bi-1)]):
   u=a1-a0;v=b1-b0;z=b0-a0;den=det(u,v)
   if den:
    s=Fraction(det(z,v),den);t=Fraction(det(z,u),den)
    if not(0<=s<=1 and 0<=t<=1):continue
   else:
    if det(z,u):continue
    axis=(lambda q:q.real)if v.real else(lambda q:q.imag);t0=Fraction(int(axis(-z)),int(axis(v)));t1=Fraction(int(axis(u-z)),int(axis(v)));t=max(Fraction(0),min(t0,t1));hi=min(Fraction(1),max(t0,t1))
    if t>hi:continue
    axis2=(lambda q:q.real)if u.real else(lambda q:q.imag);s=Fraction(int(axis2(z)),int(axis2(u)))+t*Fraction(int(axis2(v)),int(axis2(u)))
   hits.append((bi+t,ai+s,ai,bi,s,t))
 first=min(z[0]for z in hits);canon=set()
 for time,old,ai,bi,s,t in hits:
  if time!=first:continue
  if s==1:ai+=1;s=0
  if t==0:bi-=1;t=1
  canon.add((ai,bi,s,t))
 assert len(canon)==1;ai,bi,s,t=next(iter(canon));assert edges[ai][0]=='V'and edges[bi][0]=='D'and s==0 and t==1 and edges[bi][3]-edges[ai][3]==3
 assert first==sup['first_contact_path_time'] and len(seed)==sup['entry_mass']
 controls.append(dict(word=word,mass=len(seed),raw_length=len(raw),first_contact=str(first),canonical=[ai,bi,str(s),str(t)]))
out=dict(status='PASS independent canonical three-C nonproper contact reduction and both actual controls',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),geometries=[(a,b,p,str(s),str(t))for a,b,p,s,t in geoms],roles=len(roles),old_core_cases=108,retired_input_cases=24,upper_age_queries=len(upper),shadow_queries=len(shadow),old_output_queries=lower,controls=controls,scope='Only V-family source to plainD(-1,0,E) consuming original(0,0) survives nonproper first contact gap3. Actual masses8/9 realize it. No following full packet, factor-first restriction, noncontact, or global closure is inferred from a terminal marker.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in['geometries','old_output_queries']})
