from pathlib import Path
from itertools import product
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
s=(SELF.parent/'check_K1_straight_double_max_independent.py').read_text().split('rows=[];attempts=0')[0]
s=s.replace("if not lower(('A',2),('B',1),1):return None","\n for a,b in order:\n  if not lower(a,b,1):return None")
ns={'__file__':str(SELF.parent/'check_K1_straight_double_max_independent.py')};exec(s,ns);choices=ns['choices'];solve=ns['solve'];outs=ns['out'];H=lambda w:tuple('NESW'.index(c)for c in w);T=lambda h:''.join('NESW'[c]for c in h)
ns['ports']=[('A',3,'Z'),('Z',0,'Y'),('Y',1,'B'),('B',2,'A'),('B',0,'n'),('n',1,'p'),('p',2,'C'),('C',3,'B'),('n',3,'m'),('m',2,'Y'),('C',1,'v'),('v',2,'D'),('v',0,'a'),('a',3,'p')]
ns['order']=[(('A',2),('B',1)),(('B',2),('C',1)),(('C',2),('D',1))]
ac=[a for a in choices(2,'strict')if outs(a).count(3)==3 and a.count(0)==1];assert{T(a)for a in ac}=={'SNS','SNSS','SSSN'}
rows=[]
for mm,a,v,dd in product(('WWW','WWWE'),ac,('EEE','EEEW'),('SSN','SSNS','SSNN')):
 hs={k:H(w)for k,w in dict(A='NNSN',Z='WWWE',Y='NNNS',B='EEWE',n='NNSN',p='EWWW',C='SSNS',m=mm,v=v,D=dd).items()};hs['a']=a
 sol=solve(hs)
 if sol is None:continue
 cp,de=sol
 def eq(x,y,d):assert cp[x]==cp[y]and de[x]-de[y]==d,(x,y,d)
 eq(('a',0),('C',1),-2)
 if T(a)=='SSSN':
  eq(('a',3),('C',2),2);eq(('C',3),('C',2),4)
  seq=[('v',1),('a',3),('p',3),('C',3),('v',2)]
  for i,x in enumerate(seq):eq(x,seq[0],i)
 else:
  eq(('a',1),('C',2),2);eq(('p',2),('C',2),3);eq(('C',3),('p',3),1)
  # p.R2 -> p.L3 has >=4 spacing, so C.L3 >= C.R2+8.
 rows.append({k:T(w)for k,w in hs.items()})
ref=json.loads((D/'locked_RR_to_straight_ports.json').read_text());canon=lambda d:tuple(sorted(d.items()));assert len(rows)==18 and{canon(r)for r in rows}=={canon(r['headings'])for r in ref['rows']}
# Following LEFT rotates the signed LR lower helper NNNS to EEEW at physical p.
assert T(tuple((c+1)%4 for c in H('NNNS')))=='EEEW'!='EWWW'
# Actual contact-lattice right directions close a contractible square after three RIGHT vertices.
P=(1,-1);F=(0,0);G=(1,1);HH=(2,0)
vec=[(b[0]-a[0],b[1]-a[1])for a,b in zip((P,F,G,HH),(F,G,HH,P))];assert vec==[(-1,1),(1,1),(1,-1),(-1,-1)]
p=D/'K1_RR_stock_gate_forces_strict_STRAIGHT_v2.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='5b2530a08eb3881423afea19c60f466c0aa57c83627da39517f4ae383097c5da'
out=dict(status='PASS RR stock gate strict-STRAIGHT continuation v2 with late L3 retained',note_sha256=sha,necessary_rows=rows,supplier_histories=[T(a)for a in ac],common_clock='T0(a)=T1(C)-2',early_modes='SNS/SNSS: T1(a)=T2(C)+2, T2(p)=T2(C)+3, T3(C)>=T2(C)+8',late_mode='SSSN: v.L1,a.L3,p.L3,C.L3,v.R2 are consecutive, T3(C)=T2(C)+4',analytic='H RIGHT closes physical contractible contact square; H LEFT forces subsequent LEFT(noLL), RIGHT(rotated NNNS helper contradicts p EWWW), or STRAIGHT(max first LEFT neighbor contradicts bit1), all impossible. Therefore H strict STRAIGHT. Both I bottom birth corners have nonnegative first-port sign, so upper parent(1,3)/(3,3) has birth<=B(H)-8.',scope='Necessary local K1 configuration only. v1 omitted late L3 and is not used. No exterior realization, renewable fuel or universal K1 exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('rows',len(rows),'a',out['supplier_histories'])
