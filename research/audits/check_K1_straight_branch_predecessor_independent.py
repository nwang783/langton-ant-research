from pathlib import Path
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1]
# Reuse our own independently implemented equality-component solver, changing
# only the named physical interface and K1 endpoint inequality.
p=SELF.with_name('check_K1_straight_double_max_independent.py');s=p.read_text().split('rows=[];attempts=0')[0]
s=s.replace("if not lower(('A',2),('B',1),1)","if not lower(('V',2),('U',1),1)")
n={'__file__':str(SELF)};exec(compile(s,str(p),'exec'),n)
n['ports']=[('V',2,'a'),('a',3,'r'),('r',0,'U'),('U',1,'V'),('U',3,'z'),('z',2,'q'),('q',1,'r')]
choices=n['choices'];out=n['out'];solve=n['solve'];product=n['product'];rows=[];attempts=0
for ma,mr in product(('strict','equal'),repeat=2):
 for v,u,a,r,q in product([(3,3,1),(3,3,1,3),(3,3,1,1)],[(0,0,2),(0,0,2,2)],choices(2,ma),choices(3,mr),choices(2 if mr=='strict'else 0,mr)):
  if mr=='strict'and len(r[::2])!=len(q[::2]):continue
  attempts+=1;hs=dict(V=v,U=u,a=a,r=r,q=q,z=(3,3,1,1));ans=solve(hs)
  if ans is None:continue
  cp,de=ans;row={'a_other':ma,'r_other':mr,'h':{k:''.join('NESW'[x]for x in v)for k,v in hs.items()}}
  if mr=='strict':assert ma=='strict'and row['h']==dict(V='WWEW',U='NNS',a='SSSN',r='WWW',q='SNS'if len(q)==3 else'SNSN',z='WWEE')
  else:
   assert row['h']['r']in('WEE','WEEW')and row['h']['q']in('NSS','NNSS','NSSN')
   assert cp['q',0]==cp['U',1]and de['q',0]-de['U',1]==-2
  rows.append(row)
assert len(rows)==26 and sum(r['r_other']=='strict'for r in rows)==2
# Compare exact survivor sets only after reconstructing them.
author=json.loads((ROOT/'K1_pipeline_detours_2026-10-23/straight_branch_predecessor_right_ports.json').read_text())
key=lambda r:(r['a_other'],r['r_other'],tuple(sorted(r['h'].items())))
assert{key(r)for r in rows}=={key({'a_other':r['a_other'],'r_other':r['r_other'],'h':r['headings']})for r in author['rows']}
# LEFT predecessor contradiction: a flat q never has two E departures
# before its first S input; actual ordinal links force precisely that.
flat=choices(0,'equal')
for h in flat:assert out(h)[:h.index(2)].count(1)<=1
# STRAIGHT strict predecessor: both q R heads S, two total S arrivals,
# and no E output, because r=WWW has no E incoming port.
ss=[h for h in choices(2,'strict')if h.count(2)==2 and out(h).count(1)==0]
assert set(ss)=={(2,0,2),(2,0,2,0)}
note=ROOT/'K1_pipeline_detours_2026-10-23/K1_straight_branch_predecessor_alternative.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='a1f32674b55569559888acafd854403fa7e70b91e1da75ae9a196bc27228740b'
o=dict(status='PASS independent branchful predecessor alternatives',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),candidates=attempts,rows=rows,strict_straight_q=['SNS','SNSN'],equal_K_clock='T0(q)=T1(U)-2; B(K)<=B(F)-3',birth_consequence='Both TOP K contacts have input before output; parent is lower diagonal(-1,-3)or(1,-3), with B(parent)<=B(F)-8.',scope='Only complete WHITE cap4 K1 straight equal-M branch entrance. No global LEFT placement, realization, iterative descent, root fuel or exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(o,indent=2)+'\n');print(o['status'],attempts,len(rows))
