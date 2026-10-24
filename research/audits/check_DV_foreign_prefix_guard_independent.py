from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'word_stabilization/DV_foreign_prefix_guard_frozen_20261023_2220'
ns={'__file__':str(R/'audits/check_U_foreign_prefix_buds_independent.py')};exec(Path(ns['__file__']).read_text().split('COUNT=')[0],ns)
W,M,walk,inv,center,xy=(ns[k]for k in('W','M','walk','inv','center','xy'));names=list(inv);K={-1-1j,-1,-1j,0,1}
ns2={'__file__':str(R/'audits/check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns2['__file__']).read_text().split('geometries=[]')[0],ns2);meet=ns2['meet']
COUNT={tuple(map(int,s.split()[:8]))for s in(R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()}
a=json.loads((D/'DV_foreign_prefix_guard.json').read_text());catalog=json.loads((R/'seven_word_spatial_return_2026-10-23/foreign_first_contact_interface.json').read_text())
def zc(x,y):
 return x>=0 and y>=x and (y-x)%2==0 and ((y-x)%4==0 or x>=1)
def endpoint(delta,h,n):
 assert n>=0
 if n>=2:return True
 q=delta*(1j)**h;x,y=map(int,(q.real,q.imag))
 if n==0:return zc(x,y)
 Y=y-1
 return Y>=0 and any(zc(u,v)and zc(Y-v,u-x)for v in range(Y+1)for u in range(v+1))
# Independently verify the closed-form zero-C semigroup against literal count sums.
for x in range(-2,15):
 for y in range(-2,35):
  explicit=any(x==d+v and y==d+3*v+4*u for d in range(15)for v in range(15)for u in range(10))
  assert zc(x,y)==explicit

def chord(p,h,name):
 start=center(p,h);end=start+2*inv[name[0]]['p']*(-1j)**h
 return tuple(xy(start)),tuple(xy(end))
def contact(name,p,h,other):return meet(*chord(0j,0,name),*chord(p,h,other))
# Fully independent retirement classification for every advertised subproblem.
certs={};total=0;retire_counts=Counter()
for key,cert in a['retirement_certificates'].items():
 source=cert['source'];q=complex(*cert['output']);N=cert['goal_clock'];goal=complex(*cert['goal'][:2]);sc=source.count('C');assert q in inv[source]['outputs'];generated=[];sur=[]
 for n in range(N+1):
  h=(-n)%4
  for target in names:
   c=target.count('C')
   for slot in sorted(inv[target]['inputs'],key=lambda z:(z.real,z.imag)):
    p=q-slot*(-1j)**h;ep=p+inv[target]['p']*(-1j)**h;eh=(h+inv[target]['h'])%4;ck=(names.index(source),names.index(target),*xy(p),h,*xy(q),min(n,5));hit=contact(source,p,h,target)
    if(int(p.real+p.imag)+h)%2:why='sector'
    elif ck in COUNT:why='signed_count5'
    elif n<sc:why='before_actual_full_source_completion'
    elif n+c>N:why='full_tail_late'
    elif not endpoint(p-inv[source]['p'],inv[source]['h'],n-sc):why='source_to_clearer_zero_one_C_endpoint'
    elif hit is not None:assert n>=1;why='earlier_source_base_closed_contact'
    elif not endpoint(goal-ep,eh,N-n-c):why='exact_zero_one_C_endpoint'
    else:why='permissive_survivor';sur.append((n,target,*xy(slot),*xy(p),h))
    generated.append((n,target,*xy(slot),*xy(p),h,why));retire_counts[why]+=1
 expected=[(r['age'],r['consumer'],*r['input'],*r['pose'],r['reason'])for r in cert['queries']]
 assert set(generated)==set(expected)and len(generated)==len(expected)
 assert set(sur)=={(r['age'],r['consumer'],*r['input'],*r['pose'])for r in cert['survivors']}
 certs[key]=(source,q,N,goal,bool(sur));total+=len(generated)
assert(len(certs),total)==(50,4646)
allowed={}
for name in names:
 for f in'FQB':
  if walk(''.join(W[c]for c in name)+W[f]+M)['feasible']:allowed.setdefault(f,[]).append(name)
assert allowed=={'F':['V','U'],'Q':['V','U'],'B':['U']}
rows=[];counts=Counter();remaining=[];provided={(r['full_source'],'DCVUFQB'[r['foreign']],tuple(r['pose']),r['immediate_predecessor']):r for r in a['cases']}
for geo in catalog['rows']:
 atom=geo['source_atom']
 if atom not in('D','V'):continue
 N=geo['permitted_C_ages'][0];fp=complex(*geo['foreign_pose'][:2]);h=geo['foreign_pose'][2]
 for f in'FQB':
  fg=walk(W[f]+M)
  for source in (['D','DC']if atom=='D'else['V','VC','VCC']):
   for pre in allowed[f]:
    pp=fp-inv[pre]['p']*(-1j)**h;sc=source.count('C');ref=provided[(source,f,tuple(geo['foreign_pose']),pre)]
    if sc>N:why='source_tail_late'
    elif contact(source,pp,h,pre)is not None:assert N>=1;why='immediate_predecessor_earlier_source_contact'
    elif not endpoint(pp-inv[source]['p'],inv[source]['h'],N-sc):why='source_to_predecessor_endpoint'
    elif ref['hard_output']is not None:
     hard=ref['hard_output'];q=complex(*hard['output']);local=(q-fp)*(1j)**h;assert q in inv[source]['outputs']and(local in K or fg['req'].get(local)is False)
     cs,cq,cn,cg,sur=certs[hard['certificate_key']];assert(cs,cq,cn,cg,sur)==(source,q,N,fp,False);why='foreign_old_output_unretirable'
    else:why='remaining_D_age1_or2';remaining.append((source,f,N,xy(fp),pre))
    assert why==ref['reason'];counts[why]+=1;rows.append((source,f,N,*xy(fp),h,pre,why))
assert len(rows)==len(provided)==270 and dict(counts)==a['case_counts'];assert len(remaining)==11
assert Counter((n,tuple(p))for s,f,n,p,pre in remaining)=={(1,(-2,3)):7,(2,(-4,-2)):4}
# Solve the surviving count equations without a word search or arbitrary cap.
# From D exit to foreign, N+oneC+W, y equation forces dN+3vN+4uN+dW+vW=1.
sol=[]
for dn in range(2):
 for dw in range(2):
  for vw in range(2):
   if dn+dw+vw!=1 or dn<1:continue
   k=dn-dw-3*vw+3
   if k>=0 and k%4==0:sol.append((dn,0,0,dw,vw,k//4))
assert sol==[(1,0,0,0,0,1)]
conflicts=[]
for seq,t in[(['D','DC','U'],49),(['DC','V'],85)]:
 for f in'FQB':
  tr=walk(''.join(W[c]for s in seq for c in s)+W[f]+M);assert not tr['feasible'];conflicts.append((seq,f,tr))
# Exact first inconsistency independently found by a direct parity reader.
for seq,f,tr in conflicts:
 p=0j;h=0;par=set();req={}
 for i,ch in enumerate(''.join(W[c]for s in seq for c in s)+W[f]+M):
  before=(ch=='L')^(p in par)
  if p in req and req[p]!=before:break
  req[p]=before;par.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 assert i==(49 if seq==['D','DC','U']else 85)
r=1-1j
for name in names:
 assert r not in inv[name]['full']['req'];slot=inv[name]['p']+r*(-1j)**inv[name]['h'];assert slot in inv[name]['outputs']
for source,f,n,p,pre in remaining:
 if n!=2:continue
 local=(r-complex(*p))*(-1);assert local==-5-1j;tr=walk(W[f]+M);assert tr['req'][local]is False;assert next((i,ch)for i,(q,h,ch)in enumerate(tr['reads'])if q==local)==(54,'R')
manifest=D/'manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='fbd81fc5e622c6caa5c23c4f3e8493de4e3461cc3444ba006e8d681c3adb8ebf'
for f,v in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==v
for f,v in json.loads(manifest.read_text())['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==v
out={'status':'PASS D/V-source first-foreign common-prefix first-contact exclusion','manifest_sha256':sha,'case_counts':dict(counts),'retirement_subproblems':len(certs),'retirement_queries':total,'retirement_counts':dict(retire_counts),'analytic':['The exact zero-C endpoint semigroup is x>=0,y>=x,y-x even, and either y-x divisible4 or x>=1. One-C reachability is the Minkowski sum of this N semigroup, C_N=(0,1), and its W rotation. Its enumeration is bounded by the required total nonnegative y displacement, not a path length cap. Two or more C turns remain wholly permissive.','Each fresh full-source output is current only after the real source tails finish. All possible retiring full packets are included through foreign clockN, with actual source completion, full consumer completion, sector and signed COUNT5, exact zero/one-C endpoint relations, and only genuinely nonadjacent positive-gap base contacts. Each used hard-output certificate has no survivor. No foreign simplicity is assumed.','The remaining seven age1 obligations give exactly D,DC,U,foreign or DC,V,foreign by nonnegative count equations and the obligatory N base before a full turning C packet. All six supplied words conflict in RAW, at49 or85.','For the four age2 cases the D source is noninitial because the retained path began U-family. Its actual predecessor installs current bud(1,-1). All eight source complete contexts miss it, and signed post-exit maturity keeps it current through two Cs irrespective the older producer source clock. Q/B require it before-white at RAW54. The initial-D exception is not silently removed.'],'scope':'Only chronological FIRST contact in common F-prefix of FIRST foreign after actual U-entry complete8 history, outgoing old source D/V. Actual C source and Q/B-tail contacts remain separate. No generic seven-word cover, whole-proxy simplicity or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts,total)
