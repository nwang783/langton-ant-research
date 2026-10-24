from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23'
p=SELF.parent/'check_K1_early_parent_square_independent.py';env={'__file__':str(p)};exec(p.read_text().split('rows=[];attempts=0')[0],env)
ns=env['ns'];base=env['base'];H=env['H'];T=env['T'];O=ns['out'];choices=env['choices'];ns['mode']='new';ns['parent_birth']='g';ns['birth']=('u',1);ns['order']=[('A',1),('B',0),('A',2),('B',1),('D',0),('B',2),('D',1)]
ports=env['baseports'];prior=[p for p in json.loads((D/'bit11_early_parent_left_square_ports.json').read_text())['rows']if p['headings']['u']=='EEW'];assert prior
flat=choices(1,'equal');inventory=[]
for h in flat:
 firstW=h.index(3);earlyS=[k for k,o in enumerate(O(h))if o==2 and k<firstW];assert len(earlyS)<=1;inventory.append((T(h),firstW,earlyS))
tried=surv=0
for pr in prior:
 ns['parent_birth']=pr['parent_birth']
 ns['ports']=ports+([('v',1,'D')]if pr['kind']=='S'else[('v',1,'w'),('w',2,'D'),('D',3,'B')])
 hs={v:H(h)for v,h in pr['headings'].items()};assert T(hs['t'])=='NNSS'and T(hs['g'])in('SSN','SSNN','NNSS')
 sol=ns['solve'](hs);assert sol;cp,de=sol;assert cp['t',1]==cp['B',2]and de['t',1]-de['B',2]==5
 if pr['parent_birth']=='x':
  assert cp['g',3]==cp['B',1]and de['g',3]-de['B',1]==-5
 # Existing P0 clock gives second fS at gL1-1<=alpha-7;
 # first fW=tL1+1=B2+6>alpha. Exhaust full flat suppliers.
 ns['ports']=ns['ports']+[('t',3,'f'),('f',2,'g')]
 for h in flat:tried+=1;surv+=ns['solve'](dict(hs,f=h))is not None
assert surv==0
note=D/'K1_all_early_zero_L3_parents_excluded_branch_clock.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='f614a375db1f498af1e59e776687c7cb8927a0501a9e5417b1c1621f41a2175c'
out=dict(status='PASS all early zero-L3 supplier exclusions and safe main-clock branch coefficient22',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),prior_rows=len(prior),flat_histories=inventory,candidates=tried,survivors=surv,analytic='For g LEFT, the second f south departure precedes alpha-6. For g STRAIGHT NNSS, it is gL3-1=beta-6. In both cases the first f west arrival is B2+6>beta. All flat histories prohibit two such early south departures. Every surviving early branch is consequently the signed15-gap L3 mode, with nonbranch successor gaps18/23/27; these disjoint main intervals give extra23/28/32, versus22/26 for lower/upper long cases, hence P>=5ell+22*n_bit11_branches.',remaining='Only source-L3 early-LEFT modes remain; n_bit11_branches excludes other rise/fall branch modes. No exterior realization or original-fuel budget.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(len(prior),len(flat),tried,surv)
