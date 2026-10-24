from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23'
p=SELF.parent/'check_K1_early_parent_square_independent.py';env={'__file__':str(p)};exec(p.read_text().split('rows=[];attempts=0')[0],env)
ns=env['ns'];base=env['base'];H=env['H'];T=env['T'];O=ns['out'];choices=env['choices'];ns['mode']='new';ns['parent_birth']='g';ns['birth']=('u',1);ns['order']=[('A',1),('B',0),('A',2),('B',1),('D',0),('B',2),('D',1)]
ports=env['baseports'];prior=[p for p in json.loads((D/'bit11_early_parent_left_square_ports.json').read_text())['rows']if p['parent_birth']=='g'and p['headings']['u']=='EEW'];assert prior
flat=choices(1,'equal');inventory=[]
for h in flat:
 firstW=h.index(3);earlyS=[k for k,o in enumerate(O(h))if o==2 and k<firstW];assert len(earlyS)<=1;inventory.append((T(h),firstW,earlyS))
tried=surv=0
for pr in prior:
 ns['ports']=ports+([('v',1,'D')]if pr['kind']=='S'else[('v',1,'w'),('w',2,'D'),('D',3,'B')])
 hs={v:H(h)for v,h in pr['headings'].items()};assert T(hs['t'])=='NNSS'and T(hs['g'])in('SSN','SSNN')
 sol=ns['solve'](hs);assert sol;cp,de=sol;assert cp['t',1]==cp['B',2]and de['t',1]-de['B',2]==5
 # Existing P0 clock gives second fS at gL1-1<=alpha-7;
 # first fW=tL1+1=B2+6>alpha. Exhaust full flat suppliers.
 ns['ports']=ns['ports']+[('t',3,'f'),('f',2,'g')]
 for h in flat:tried+=1;surv+=ns['solve'](dict(hs,f=h))is not None
assert surv==0
note=D/'K1_early_LEFT_parent_zero_L3_flat_supplier_obstruction.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='c946e4f796b682d8fb56c82808b337c6151df15e66ca20ace3c96869d2b588a3'
out=dict(status='PASS complete zero-L3 early-LEFT supplier exclusion',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),prior_rows=len(prior),flat_histories=inventory,candidates=tried,survivors=surv,analytic='The second f south departure supplies g L1 before alpha-6, but the first f west arrival follows the exact B R2-to-t L1 five-edge route and occurs after alpha. Every complete flat E/W cap4 history has at most one south output before its first west arrival. Both possible P1 canonical parents are irrelevant.',remaining='Early STRAIGHT x mode and both source-L3 LEFT modes with strict f EEEW remain; no general K1 or fuel exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(len(prior),len(flat),tried,surv)
