from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1]
s=(SELF.parent/'check_DV_foreign_prefix_guard_independent.py').read_text();exec(s.split('certs={};total=0')[0])
SELF=Path(__file__).resolve();D=R/'word_stabilization/DV_foreign_tail_guard_frozen_20261023_2237';a=json.loads((D/'DV_foreign_tail_guard.json').read_text());catalog=json.loads((R/'seven_word_spatial_return_2026-10-23/foreign_tail_first_contact.json').read_text())
block='certs={};total=0'+s.split('certs={};total=0')[1].split('allowed={}')[0];block=block.replace('(50,4646)','(38,2898)');exec(block)
provided={(r['full_source'],r['foreign'],tuple(r['pose']),r['immediate_predecessor']):r for r in a['cases']};counts=Counter();remaining=[];nrows=0
for f,geos in catalog['rows'].items():
 for geo in geos:
  atom=geo['source_atom']
  if atom not in('D','V')or 0 not in geo['preceding_C_bits']:continue
  N=geo['permitted_C_ages'][geo['preceding_C_bits'].index(0)];fp=complex(*geo['foreign_pose'][:2]);h=geo['foreign_pose'][2];fg=walk(W[f]+M)
  for source in(['D','DC']if atom=='D'else['V','VC','VCC']):
   for pre in(['V','U']if f=='Q'else['U']):
    pp=fp-inv[pre]['p']*(-1j)**h;sc=source.count('C');ref=provided[(source,f,tuple(geo['foreign_pose']),pre)]
    if sc>N:why='source_tail_late'
    elif contact(source,pp,h,pre)is not None:
     assert N>0 or(sc==0 and(pp,h)!=(inv[source]['p'],inv[source]['h']));why='immediate_predecessor_earlier_source_contact'
    elif not endpoint(pp-inv[source]['p'],inv[source]['h'],N-sc):why='source_to_predecessor_endpoint'
    elif ref['hard_output']is not None:
     hard=ref['hard_output'];q=complex(*hard['output']);local=(q-fp)*(1j)**h;assert q in inv[source]['outputs']and(local in K or fg['req'].get(local)is False);cs,cq,cn,cg,sur=certs[hard['certificate_key']];assert(cs,cq,cn,cg,sur)==(source,q,N,fp,False);why='foreign_old_output_unretirable'
    else:why='residual_D_or_V_interface';remaining.append((source,f,N,fp,h,pre,pp))
    assert why==ref['first_reason'];counts[why]+=1;nrows+=1
assert nrows==106 and dict(counts)==a['counts']and len(remaining)==12
assert Counter((s[0],f,n,tuple(xy(p)))for s,f,n,p,h,pr,pp in remaining)=={('D','Q',1,(-4,3)):2,('D','Q',3,(3,-4)):4,('D','B',2,(-3,-3)):1,('V','Q',3,(3,-2)):2,('V','B',3,(3,-2)):3}
# The low y equation permits only dN=1 when a real N base precedes the sole C.
assert not any((dn-dw-3*vw+5)>=0 and(dn-dw-3*vw+5)%4==0 for dn in range(2)for dw in range(2)for vw in range(2)if dn+dw+vw==1 and dn>=1)
assert [(dw,vw,(5-dw-3*vw)//4)for dw in range(2)for vw in range(2)if dw+vw==1 and 5-dw-3*vw>=0 and(5-dw-3*vw)%4==0]==[(1,0,1)]
conflicts=[]
for labels in('DCDUQ','DCUDQ'):
 p=0j;h=0;req={};par=set()
 for i,ch in enumerate(''.join(W[c]for c in labels)+M):
  before=(ch=='L')^(p in par)
  if p in req and req[p]!=before:break
  req[p]=before;par.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 conflicts.append((labels,i,xy(p)))
assert conflicts==[('DCDUQ',122,(-1,-1)),('DCUDQ',39,(0,1))]
r=1-1j;ends=[]
for name in names:
 assert r not in inv[name]['full']['req'];assert inv[name]['p']+r*(-1j)**inv[name]['h']in inv[name]['outputs']
for base in'DVU':
 for slot in inv[base]['inputs']:
  p=r-slot*(-1j);ep=p+inv[base]['p']*(-1j);assert ep.real>=1;ends.append((base,xy(slot),xy(ep)))
for source,f,n,p,h,pre,pp in remaining:
 if source[0]!='D'or n==1:continue
 local=(r-p)*(1j)**h;fg=walk(W[f]+M);assert fg['req'][local]is False;first=next((i,c)for i,(q,hh,c)in enumerate(fg['reads'])if q==local)
 if n==2:assert(f,local,first)==('B',-4-2j,(52,'R'))
 else:
  assert(f,n,local,first)==('Q',3,-3-2j,(57,'R'));assert pp.real<=0 and(r-pp)*(1j)**h not in inv[pre]['full']['req']
# Rebuild the universal produced lower-a minimum3 with full source completion.
minrows=[]
for source in names:
 for n in range(3):
  h=(-n)%4
  for out in inv[source]['outputs']:
   p=out-(-1+1j)*(-1j)**h;key=(names.index(source),names.index('U'),*xy(p),h,*xy(out),n)
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif source.count('C')>n:why='producer_tail_late'
   else:assert key in COUNT;why='signed_count5'
   minrows.append((source,n,xy(out),xy(p),h,why))
assert len(minrows)==204 and Counter(r[-1]for r in minrows)=={'sector':104,'producer_tail_late':38,'signed_count5':62}
for source in names:assert min(q.imag for q in inv[source]['outputs'])>=0
coreproof=[]
for source,f,n,p,h,pre,pp in remaining:
 if source[0]!='V':continue
 assert(n,p,h,pre,pp)==(3,3-2j,1,'U',-1-2j)
 q=pp+(-1+1j)*(-1j);assert q==-1j and q in K and q not in inv[source]['outputs'];exitcore={inv[source]['p']+z*(-1j)**inv[source]['h']for z in K};assert q not in exitcore
 last=[(i,c)for i,(z,hh,c)in enumerate(inv[source]['raw']['reads'])if z==q][-1];assert last[1]=='L';coreproof.append((source,f,last,xy(inv[source]['p']),source.count('C')))
assert len(coreproof)==5 and inv['V']['p']==1+3j
manifest=D/'manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='35f51ab959f5356dd1007e08c26ebc1e957006899c8194e95c50e3d089865976'
for f,v in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==v
for f,v in a['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==v
out={'status':'PASS D/V-source chronological first-Q/B-tail contact exclusion','manifest_sha256':sha,'case_counts':dict(counts),'retirement_subproblems':len(certs),'retirement_queries':total,'retirement_counts':dict(retire_counts),'forced_RAW_conflicts':conflicts,'produced_lower_age_queries':len(minrows),'produced_lower_counts':dict(Counter(r[-1]for r in minrows)),'deleted_core_obligations':coreproof,'analytic':['The signed tail catalogue retains source-outgoing and new-tail incoming endpoint conventions. All106 b0 cases and38 retirement subproblems use actual full-source completion and full-consumer completion, exact zero/one-C semigroup endpoints and signed COUNT5; >=2 remaining Cs are permissive. At clock0 actual source-end adjacency is explicitly checked rather than silently excluded.','Two D/Q age1 cases: a real N turning base after plainD makes the nonnegative endpoint equation insoluble; DC requires exactly one W D and one W U, whose two orders fail RAW at122/39.','The genuine incoming predecessor bud exists for noninitial D in the U-entry factor. It survives through2Cs, excluding B RAW52. At age3 all E first-clearer endpoints have x>=1, cannot precede lastV/U at x<=0; those last complete contexts miss the bud, while Q RAW57 requires it WHITE.','All five residual V-source cases require plain U(-1,-2,E)at3 with lower input at original source-core cell(0,-1). Every V/VC/VCC source leaves this physical cell WHITE, outside full outputs and exit core. A future residual there must be genuinely newly produced after source, not an entry identity or surviving core ID.','Universal full-source lower-a minimum3 is reconstructed in204 roles:104sector,38own-tail-too-late,62COUNT5. Therefore a supplier to Uat3 must start no later than sourceclock0. VC/VCC sources finish at1/2, so later suppliers cannot qualify. PlainV exits(1,3,N)at0; all later clock0 heads follow N zero-C runs and have y>=3, while ALL eight full-output local y offsets are nonnegative, including their own tails. None can output y=-1.'],'scope':'FIRST Q/B-tail new contact after an actual U-entry complete8 history, earlier outgoing D/V source. No mixed-path iterative simplicity, generic graph coverage, eventual entry or universal capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts,total)
