from pathlib import Path
from collections import Counter
import json,hashlib
P=Path(__file__).resolve();src=P.with_name('check_qolder_relocation_independent.py');exec(compile(src.read_text().split('HB=')[0],str(src),'exec'))
B=ROOT/'core_periodicity_new/U1_age4_predecessor_frozen_20261023_1246';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_U1_age4_predecessor_reduction.json').read_text())
for f,sha in J['dependencies'].items():assert hashlib.sha256((W/f).read_bytes()).hexdigest()==sha
# Build every complete initial-demand set directly from literal reads and flips.
def conflict(chain):
 known={};flipped=set();time=0
 for a,p,h in chain:
  z=p;hh=h
  for t,turn in enumerate(raws[a]+mark):
   wanted=(turn=='L')^(z in flipped)
   if z in known and known[z]!=wanted:return xy(z)
   known[z]=wanted;flipped.symmetric_difference_update({z});hh=(hh+(1 if turn=='R'else-1))%4;z+=(1j,1,-1j,-1)[hh]
   if t+1==len(raws[a]):rawflip=set(flipped);end=(z,hh)
  flipped=rawflip
 return None
peak=lambda a,p,h:2*int(p.imag-p.real)+max(A[(h+1)%4],T[a,(h+1)%4])
H=lambda p:int(p.imag-p.real)
zero=[H(rotation(G[a][3],3))for a in(0,4,7)];assert zero==[2,4,4]
caps={a:(29-max(A[0],T[a,0]))//2 for a in ids if cc[a]};assert caps=={1:6,5:4,6:0,8:4,9:0}
rows=[];ct=Counter()
for s,pose in((5,-4-2j),(6,-4-2j),(8,-3-3j),(9,-3-3j)):
 e=pose+G[s][3];h=G[s][4];assert(e,h)==((-3+2j,3)if cc[s]==1 else(-4+2j,2))
 assert min(28+2*H(pose+z)for z in G[s][0])>30
 for a in ids:
  ah=(-G[a][4])%4;ap=pose-rotation(G[a][3],ah);pk=peak(a,ap,ah);cell=None
  if pk>=30:reason='STRICT_RECORD_REJECTED'
  elif (cell:=conflict([(a,ap,ah),(s,pose,0)]))is not None:reason='PAIR_LITERAL_REJECTED'
  elif cc[a]:
   assert cc[a]==2 and s==5 and e==-3+2j and h==3
   cell=conflict([(a,ap,ah),(s,pose,0),(1,e,3)]);assert cell is not None
   reason='FORCED_DC_THREE_PACKET_LITERAL_REJECTED'
  else:reason='ZERO_C_PREDECESSOR_NECESSARY_SUPERSET'
  r=dict(source=s,predecessor=a,predecessor_pose=[*xy(ap),ah],predecessor_peak=pk,reason=reason,conflict_cell=cell);rows.append(r);ct[reason]+=1
AA={(r['source'],r['predecessor']):r for r in J['rows']}
for r in rows:
 a=AA[r['source'],r['predecessor']]
 for k in('predecessor_pose','predecessor_peak','reason'):assert r[k]==a[k],(r,a)
 if r['reason']=='FORCED_DC_THREE_PACKET_LITERAL_REJECTED':assert list(r['conflict_cell'])==a['conflict']['cell']
assert ct==Counter({'STRICT_RECORD_REJECTED':10,'PAIR_LITERAL_REJECTED':8,'FORCED_DC_THREE_PACKET_LITERAL_REJECTED':2,'ZERO_C_PREDECESSOR_NECESSARY_SUPERSET':12})
# Heading cannot change during zero-C runs. From H5, any such step gives H>=7,
# whereas every subsequent allowed turning packet needs H<=6. Hence no delay.
assert min(zero)==2 and max(caps.values())==6 and [a for a,b in caps.items()if b>=5]==[1]
assert (-3+2j)+rotation(G[1][3],3)==-5+3j and(3+G[1][4])%4==2
result=dict(status='PASS independent full32 predecessor table and all-length forced-turn bound',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(ct),rows=rows,positive_C_W_height_caps=caps,zero_C_W_increments=zero,scope='Strict unfunded outer U1 produced lower age4 only. Immediate predecessor must D/V/U; VC/UC has immediate following DC. Necessary remaining two-C protected return, not exclusion or funding descent.')
P.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k!='rows'})
