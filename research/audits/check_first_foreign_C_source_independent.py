from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23'
ns={'__file__':str(R/'audits/check_U_foreign_prefix_buds_independent.py')};exec(Path(ns['__file__']).read_text().split('COUNT=')[0],ns)
W,M,walk,inv,xy=(ns[k]for k in('W','M','walk','inv','xy'));K={-1-1j,-1,-1j,0,1}
A=json.loads((D/'first_foreign_C_source_exclusion.json').read_text());P=json.loads((D/'foreign_first_contact_interface.json').read_text());T=json.loads((D/'foreign_tail_first_contact.json').read_text())
c=walk(W['C']);full=walk(W['C']+M);assert {q for q,b in full['req'].items()if b}==K and(c['p'],c['h'])==(1j,3);out=(K^c['odd'])-{c['p']+q*(-1j)**c['h']for q in K};assert out=={1+2j,2,2+1j}
for name in inv:assert inv[name]['inputs']==inv[name[0]]['inputs']
roles=[]
for name in('DC','VC','VCC','UC','UCC'):
 word=''.join(W[a]for a in name);raw=walk(word)
 for j in range(1,name.count('C')+1):
  pre=W[name[0]]+W['C']*(j-1);r=walk(pre);cp,ch=r['p'],r['h'];n=len(pre);ctx=word+M
  assert ctx[n:n+11]==ctx[n+15:n+26]==M
  slots={key:cp+q*(-1j)**ch for key,q in [('C_common',2),('C_exit_bud',1+2j),('incoming_exit_bud',1-1j)]}
  for key,q in slots.items():
   reads=[(i,c)for i,(p,h,c)in enumerate(raw['reads'])if p==q];assert reads[-1][1]=='R'and q in inv[name]['outputs']
   if key=='C_common':assert reads[-1][0]==n+8
   elif key=='C_exit_bud':assert reads[-1][0]==n+13
   else:assert reads[-1][0]<n
  roles.append((name,j,xy(cp),ch,j-1,name.count('C')-j,{k:xy(v)for k,v in slots.items()}))
assert len(roles)==7 and 1-1j not in full['req']
assert {(n,j,tuple(s['C_common']))for n,j,p,h,o,rem,s in roles if j==2}=={('VCC',2,(1,6)),('UCC',2,(0,7))}
cases=[];clocklabels=0
for r in P['rows']:
 if r['source_atom']=='C':
  for f in'FQB':cases.append((f,'F_prefix',tuple(r['foreign_pose']),r['permitted_C_ages'][0]));clocklabels+=len(r['permitted_C_ages'])
for f,rs in T['rows'].items():
 for r in rs:
  if r['source_atom']!='C':continue
  clocklabels+=len(r['permitted_C_ages'])
  if 0 in r['preceding_C_bits']:cases.append((f,f+'_tail',tuple(r['foreign_pose']),r['permitted_C_ages'][r['preceding_C_bits'].index(0)]))
assert len(cases)==25 and clocklabels==53
assert cases==[(r['foreign'],r['piece'],tuple(r['pose']),r['C_age'])for r in A['first_contact_cases']]
assert sum(1+rem>age for f,part,pose,age in cases for name,j,p,h,off,rem,slots in roles)==16
rows=[];rawsur=[]
for ci,(f,part,pose,age)in enumerate(cases):
 p=complex(*pose[:2]);h=pose[2];turn=(-1j)**h;fg=walk(W[f]+M);protected=({1+2j}if age<=3 else set())|({2}if age<=2 else set());core={p+q*turn for q in K};white={p+q*turn for q,b in fg['req'].items()if not b};targethit=protected&(core|white)
 for pre in('VU'if f!='B'else'U'):
  pp=p-inv[pre]['p']*turn;predctx={pp+q*turn for q in inv[pre]['full']['req']}
  if targethit:why='target_protected_guard'
  elif protected&predctx:why='protected_old_predecessor_context'
  else:why='remaining';rawsur.append((ci,f,part,pose,age,pre,pp))
  rows.append((ci,pre,why))
assert Counter(r[-1]for r in rows)=={'target_protected_guard':8,'protected_old_predecessor_context':11,'remaining':21}
assert {(ci,pre)for ci,pre,why in rows if why=='remaining'}=={(r['case'],r['base'])for r in A['classified_predecessor_assignments']if r['reason']=='remaining_exact_obligation'}
# Exact N semigroup; rotated coordinates give every zero-C cone.
def cone(delta,h):
 z=delta*(1j)**h;x,y=map(int,(z.real,z.imag));return [(x-v,v,(y-x-2*v)//4)for v in range(max(0,x+1))if y-x-2*v>=0 and(y-x-2*v)%4==0]
assert cone(-1+1j,3)==[(1,0,0)]
sol=[]
for d in range(4):
 for v in range(2):
  for e in range(4):
   for f in range(4):
    if d+3*v+e+f!=3:continue
    r=d+v-e-3*f-1
    if r>=0 and r%4==0:sol.append((d,v,0,e,f,r//4))
assert set(sol)=={(2,0,0,1,0,0),(0,1,0,0,0,0)}
conflicts=[]
for labels in['CDVQ','CDUB','CDDCDUB','CVCUB']:
 p=0j;h=0;req={};odd=set();reads={};tick=0;failure=None
 for a in labels:
  for phase,ch in enumerate(W[a]):
   b=(ch=='L')^(p in odd)
   if p in req and req[p]!=b:failure=(a,phase,tick,xy(p));break
   req[p]=b;reads.setdefault(p,[]).append((tick,ch));odd.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h];tick+=1
  if failure:break
 conflicts.append((labels,failure))
assert [x[1][:2]for x in conflicts]==[('Q',59),('B',69),('B',42),('U',14)]
endpoints=[]
for guard in(2,1-1j):
 for age,h in((3,1),(4,0)):
  for a in'DVU':
   for slot in inv[a]['inputs']:
    p=guard-slot*(-1j)**h;ep=p+inv[a]['p']*(-1j)**h;endpoints.append((guard,age,a,slot,p,ep,h))
assert len(endpoints)==32
for guard,age,a,slot,p,ep,h in endpoints:
 if guard==2 and age==3:
  assert ep.real>=2
  if ep.real==2:assert ep==2-1j and cone(2j,0)==[]
 if guard==2 and age==4:assert cone(3+1j-ep,0)==[]
 if age==3:
  ss=cone(guard+2-3j-ep,1);assert ss==[]or(ss==[(2,0,0)]and ep==guard-1j)
assert sum(bool(cone(g+2-3j-ep,1))for g,n,a,s,p,ep,h in endpoints if n==3)==6
classified=Counter()
for ci,f,part,pose,age,pre,pp in rawsur:
 p=complex(*pose[:2]);h=pose[2];fg=walk(W[f]+M)
 if age==1:
  assert pp==-1+2j and h==3 and (f,pre)in[('Q','V'),('B','U')];why='age1'
 elif age==2:assert(f,pre,p,pp)==('B','U',-4-2j,-4+2j);why='age2'
 elif age==3 and part=='F_prefix':
  assert p.real==1;local=(2-p)*(1j)**h;assert fg['req'][local]is False;why='age3_prefix'
 elif age==3:
  guard=1-1j if f=='Q'else 2;assert p==guard+2-3j;local=(guard-p)*(1j)**h;assert local==-3-2j and fg['req'][local]is False;assert next((i,c)for i,(q,hh,c)in enumerate(fg['reads'])if q==local)==(57,'R');why='age3_tail'
 else:assert age==4 and p==3+1j and 2-p in K;why='age4_prefix'
 classified[why]+=1
assert classified=={'age1':2,'age2':1,'age3_prefix':10,'age3_tail':3,'age4_prefix':5}
manifest=D/'first_foreign_C_source_exclusion_manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='37e71e6bd55f1bd9ea748e2fb9221bf474309e494ba788f35e56419ca2bdd384'
for f,v in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==v
for f,v in A['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==v
out={'status':'PASS actual C-source chronological first-foreign contact exclusion','manifest_sha256':sha,'full_producer_roles':roles,'clock_labels':clocklabels,'b0_geometries':len(cases),'completion_records':175,'impossible_early_completions':16,'first_filters':dict(Counter(r[-1]for r in rows)),'remaining_exclusions':dict(classified),'forced_word_conflicts':conflicts,'analytic':['Every source C is one of seven actual full-producer tail roles. Its actual entry and exit M11 are present in full RAW+marker. Atomic age n maps to full-source age n+j-1. In particular the second-C common maps to full VCC(1,6) or UCC(0,7). No source identity is reset at an internal C cut.','Signed common1344 gives atomic common first consumption>=3, including shifted second C. Signed exit-bud1325 gives C exitbud first consumption>=4 because C exits at1, and the genuine incoming predecessor bud first consumption>=3 from C entry. C has no external residual inputs; every full input set is the corresponding base input set, so core/marker-only retirement is covered.','The complete8 adjacency law removes preceding-C labels only in this actual first-foreign scope. The remaining25 geometries have40 real V/U predecessors. Eight foreign core/white conflicts and11 old predecessor complete-context conflicts are legitimate; a foreign black INPUT is not rejected merely by an old-eight maturity law.','At age1 the actual W cone forces one D before the fixed V/Q or U/B pair. At age2 exact count equations force two words. All four fail by immutable RAW read parity. Nonfinal first-C roles that cannot complete their source in time are independently retained as impossible timing records, not treated as standalone producers.','Age3 prefix retirement endpoints have E x>=2 versus foreign x1. Age3 tail first clearers can reach the target only by exactly two subsequent plain D bases, forbidden immediately before foreign. This uses the genuine incoming guardian for Q and C-common for B, not an unproved foreign permanence.','At age4 the E age3 equality endpoint(2,-1) must use the sole C to(3,-1,N). Remaining zero-x N motion is only U and raises y by4, never to1. All eight N age4 endpoints fail the exact zero-C cone. Full consumers may contain the remaining C but must complete by actual foreign entry; two tails cannot fit.'],'scope':'Outgoing actual C source only at chronological FIRST new contact of FIRST foreign after an actual U-entry complete8 path. No avoidance of later contacts after an earlier new contact, global kinked proxy simplicity, generic seven-word cover or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(classified)
