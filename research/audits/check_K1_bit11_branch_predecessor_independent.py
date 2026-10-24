from pathlib import Path
from itertools import product
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
s=(SELF.parent/'check_K1_straight_double_max_independent.py').read_text().split('rows=[];attempts=0')[0]
s=s.replace("if not lower(('A',2),('B',1),1):return None","\n for a,b in zip(order,order[1:]):\n  if not lower(a,b,1):return None\n for who,di,at in births:\n  for k,x in enumerate(out(hs[who])):\n   if x==di and not lower(at,(who,k),0):return None")
ns={'__file__':str(SELF.parent/'check_K1_straight_double_max_independent.py')};exec(s,ns);choices=ns['choices'];solve=ns['solve'];O=ns['out'];H=lambda s:tuple('NESW'.index(c)for c in s);T=lambda h:''.join('NESW'[x]for x in h)
ns['ports']=[('A',3,'Z'),('Z',0,'Y'),('Y',1,'B'),('B',2,'A'),('B',0,'n'),('n',1,'p'),('p',2,'C'),('C',3,'B'),('n',3,'m'),('m',2,'Y')]
ns['order']=[('A',1),('B',0),('A',2),('B',1),('C',0),('B',2),('C',1)];ns['births']=[('Z',0,('A',1)),('n',1,('B',1))]
rows=[];attempts=0
for mz,my in product(('strict','equal'),repeat=2):
 for aa,z,y,(nn,pp),m in product(('NNS','NNSN','NNSS'),choices(3,mz),choices(0,my),[('NNSN','EWWW'),('SNNN','WWEW')],choices(3,my)):
  if len(m[::2])!=len(y[::2]):continue
  attempts+=1;hs=dict(A=H(aa),Z=z,Y=y,B=H('EEWE'),n=H(nn),p=H(pp),C=H('SSNS'),m=m)
  if solve(hs)is not None:rows.append(dict(prior_other=[mz,my],headings={k:T(v)for k,v in hs.items()}))
assert len(rows)==2 and all(r['prior_other']==['strict','strict']for r in rows)
assert all(r['headings']['A']=='NNSN'and r['headings']['Z']=='WWWE'and r['headings']['Y']=='NNNS'and r['headings']['n']=='NNSN'for r in rows)
ref=json.loads((D/'general_RIGHT_to_max_RIGHT_ports.json').read_text());key=lambda r:tuple(sorted(r['headings'].items()));assert{key(r)for r in rows}=={key(r)for r in ref['rows']}
# Independently enumerate the strict STRAIGHT predecessor, retaining every S-axis 1..4 history at e.
ns['ports']=[('A',3,'Z'),('Z',0,'B'),('B',3,'w'),('w',0,'Y'),('Y',1,'C'),('C',2,'B'),('w',2,'e'),('e',1,'Z')]
ns['order']=[('A',1),('B',0),('A',2),('B',1),('C',0),('B',2),('C',1)];ns['births']=[('Z',0,('A',1)),('w',0,('B',1))]
straight=[]
for (w,y),e in product([('WWEW','NSSS'),('EWWW','SSNS')],choices(2,'strict')):
 hs=dict(A=H('NNSN'),Z=H('WWWE'),B=H('NNSN'),w=H(w),Y=H(y),C=H('EEWE'),e=e);sol=solve(hs)
 if sol is None:continue
 cp,de=sol;seq=[('w',2),('e',1),('Z',3),('B',3),('w',3),('e',2)]
 assert all(cp[v]==cp[seq[0]]and de[v]-de[seq[0]]==i for i,v in enumerate(seq))
 assert cp['e',0]==cp['B',2]and de['e',0]-de['B',2]==2
 straight.append({k:T(v)for k,v in hs.items()})
assert len(straight)==2 and{r['e']for r in straight}=={'SSS','SSSN'}and all(r['w']=='WWEW'and r['Y']=='NSSS'for r in straight)
ref=json.loads((D/'strict_STRAIGHT_to_max_RIGHT_ports.json').read_text());assert{tuple(sorted(r.items()))for r in straight}=={key(r)for r in ref['rows']}
p=D/'K1_bit11_max_RIGHT_branch_predecessor_lock.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='bdddf3ecd69af02831d330a80570c689525da7d6ff3541f8e2436ed54cbe0877'
out=dict(status='PASS universal bit11 maximum-RIGHT predecessor and flat orientation lock',note_sha256=sha,independent_full_RIGHT_candidate_count=attempts,RIGHT_survivors=rows,strict_STRAIGHT_survivors=straight,analytic='Complete white histories include prior selected bit0/RIGHT-L3 alternatives, strict/equal other C heights, all m histories with matched R-face count, physical ordinal ports, full K1 order and canonical birth minima. Only locked row4 RIGHT predecessors survive. Strict STRAIGHT predecessors retain only eSSS/SSSN and the actual wR2,eL1,ZL3,BL3,wL3,eR2 stock route. With signed no LEFT predecessor this universally fixes first helper WWEW and second NSSS at bit11 branched RIGHT.',scope='Necessary local histories only, no global constant-state substitution, exterior realization, recursive supplier type, fuel or K1 exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(attempts,len(rows),len(straight))
