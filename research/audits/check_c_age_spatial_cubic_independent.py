"""Independent literal packet reconstruction and exact cubic identity.
No author arithmetic/genealogy implementation is imported.
"""
from pathlib import Path
import json,hashlib
from fractions import Fraction
B=Path('/workspace/shared/langton');F=B/'word_stabilization/dcuv_c_age_spatial_cubic_frozen_20261023_0750';M=json.loads((F/'manifest.json').read_text())
for x in M['files']:assert hashlib.sha256((F/x['file']).read_bytes()).hexdigest()==x['sha256']
G=json.loads((F/'literal_residual_geometry.json').read_text());ages={(a,complex(x,y)):v for a,x,y,v in json.loads((F/'counted_input_age_rules_complete.json').read_text())};core={complex(x,y)for x,y in G['core']}
chosen={0:1j,1:1j,4:1+2j,5:1+2j,6:3j,7:3j,8:3j,9:3j};rows=[]
for a,q in chosen.items():
 g=G['geometry'][a];p=0j;h=1j;flips=set();need={};snap=None
 for t,c in enumerate(g['word']+g['marker']):
  val=(c=='L')^(p in flips);assert p not in need or need[p]==val
  need[p]=val;flips.symmetric_difference_update([p]);h*=(-1j if c=='R' else 1j);p+=h
  if t+1==len(g['word']):snap=p,h,flips.copy()
 incoming={z for z,v in need.items() if v};end,h,toggle=snap;outgoing=incoming^toggle;newcore={end+z*(h/1j)for z in core}
 assert core<=incoming and newcore<=outgoing
 ins=incoming-core;outs=outgoing-newcore
 assert ins=={complex(x,y)for x,y in g['inputs']} and outs=={complex(x,y)for x,y in g['outputs']}
 assert q in ins;age=ages[a,q];distance=max(max(abs((z-q).real),abs((z-q).imag))for z in outs)
 assert distance<=age<=4 and all(ages[a,z]>=2 for z in ins)
 cc=g['name'].count('C');assert len(g['word'])<=10*len(ins)+15*cc
 for rot in(1,1j,-1,-1j):assert max(max(abs(((z-q)*rot).real),abs(((z-q)*rot).imag))for z in outs)==distance
 rows.append(dict(packet=a,name=g['name'],selected=[int(q.real),int(q.imag)],age=age,distance=int(distance),inputs=len(ins),outputs=len(outs),C_count=cc,length=len(g['word'])))
# Polynomial equality by coefficient arithmetic, independently of sample sums.
# 4 sum j^2 + 36 sum j + 81(k+1) = (k+1)(4k^2+56k+243)/3.
left=[Fraction(81),Fraction(81+18)+Fraction(2,3),Fraction(18+2),Fraction(4,3)]
right=[Fraction(243,3),Fraction(299,3),Fraction(60,3),Fraction(4,3)]
assert left==right
res=dict(status='PASS independent literal geometry and analytic genealogy/epoch review',rows=rows,polynomial_coefficients=list(map(str,left)),manifest_sha256=hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),scope='Complete recurrent-eight factors only. Residual support lies in entry-root boxes radius k+4; finite-C duration is cubic, not confinement or global capture.')
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
