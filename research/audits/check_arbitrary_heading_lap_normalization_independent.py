from pathlib import Path
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'stateful_growth_quadratic_2026-10-23'
ns={'__file__':str(SELF.parent/'check_quadratic_lap_validator_independent.py')};exec((SELF.parent/'check_quadratic_lap_validator_independent.py').read_text().split('def finiteK')[0],ns)
integ,normalized,xy=ns['integ'],ns['normalized'],ns['xy']
def preprocess(blocks,h):
 bs=list(blocks);skip=0
 if all(b==0 for w,a,b in bs):
  if all(a==0 for w,a,b in bs):return dict(rejected=True,kind='empty')
  bs=[(w,a,a+b)for w,a,b in bs];skip=1
 for i,(w,a,b)in enumerate(bs):
  if not a:continue
  dp,dh,_=integ(w,0)
  if dh or not dp:
   power=8 if dh else 2;witness=max(0,(power-b+a-1)//a)+skip
   return dict(rejected=True,kind='rotation'if dh else'closed',power=power,witness_lap=witness,block=i)
 theta=sum(b*integ(w,0)[1]for w,a,b in bs)%4;group=4 if theta else 1
 if theta:bs=[(w,4*a,a*s+b)for s in range(4)for w,a,b in bs]
 nb,A,B,bundled,fs=normalized(bs,h)
 if theta:assert A==0j
 return dict(rejected=False,skipped_initial_empty_laps=skip,original_lap_rotation=theta,original_laps_per_group=group,A=xy(A),B=xy(B),bundled=bundled,blocks=nb)
def raw(bs,h,start,count):
 p=0j;hh=h;ev=[]
 for n in range(start,start+count):
  for w,a,b in bs:
   for j in range(a*n+b):
    for t in w:
     ev.append((xy(p),hh,t));hh=(hh+(1 if t=='R'else-1))%4;p+=(1j,1,-1j,-1)[hh]
 return ev
examples=[('nonrestoring_variable_power',[('R',1,1)],1),('zero_drift_variable_power',[('RRRR',1,1)],1),('rotating_laps',[('LRRL',1,1),('R',0,1)],1),('quadratic_restored_laps',[('LRRL',1,1)],1),('empty_first_lap',[('LRRL',1,0)],1),('halfturn_laps',[('LRRL',1,1),('RR',0,1)],0),('negative_quarter_laps',[('LRRL',1,1),('L',0,1)],2),('odd_drift_core_bundling',[('RL',1,1)],0),('empty_domain',[('R',0,0)],0),('skip_then_rotate',[('LRRL',2,0),('RR',0,0)],3)]
ref={r['name']:r for r in json.loads((D/'normalize_affine_laps.json').read_text())['records']};reports=[]
for name,bs,h in examples:
 q=preprocess(bs,h);q['name']=name
 if not q['rejected']:
  mult=q['original_laps_per_group']*(2 if q['bundled']else 1)
  actual=raw(bs,h,q['skipped_initial_empty_laps'],6*mult);grouped=raw(q['blocks'],h,0,6);assert actual==grouped
  q['physical_read_comparisons']=len(actual)
 if name in ref:
  r=ref[name];assert q['rejected']==r['rejected']
  for k in('witness_lap','power','original_lap_rotation','original_laps_per_group','skipped_initial_empty_laps','physical_read_comparisons'):
   if k in r:assert q[k]==r[k]
  for k in('A','B'):
   if k in r:assert q[k]==tuple(r[k])
 reports.append(q)
# Every nonzero quarter rotation annihilates an arbitrary vector's four-rotation sum.
for theta in(1,2,3):
 assert sum((2+3j)*((-1j)**(theta*s))for s in range(4))==0
 # The resulting grouped affine coefficient vanishes independently of constant drift.
 assert sum(4*(2+3j)*((-1j)**(theta*s))for s in range(4))==0
p=D/'arbitrary_heading_affine_lap_addendum.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='df9ebd03a6499635f7470593a2230a9cc3cebae6dd415d3b9ba0a4b24a32292e'
assert hashlib.sha256((D/'normalize_affine_laps.py').read_bytes()).hexdigest()=='424d18c1691e5e795d721178796f428ded9cd73ac7cd7042373e4e8131de12ad'
out=dict(status='PASS arbitrary-heading literal affine-count lap preprocessing',note_sha256=sha,records=reports,analytic='A nonrestoring growing word eventually contains w^8: w^4 returns pose; two identical closed-pose words force even local visit multiplicity, zero full XOR, and an impossible bounded periodic physical orbit. Restoring zero-drift growing words similarly fail at w^2. Remaining whole-lap rotation is constant; four actual laps cancel the drift slope, preserving every actual read. Empty initial lap is a harmless index shift. Core odd-drift bundling is additionally retained when theta=0.',scope='General finite-expression realizability and standard-capture decision reduction, not discovery of a nonstandard finite-seed orbit. Wrapper group metadata records the preprocessing factor; core bundled flag supplies an additional factor2 when needed.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print([(r['name'],r.get('physical_read_comparisons'))for r in reports])
