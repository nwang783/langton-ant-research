from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'foreign_renewal_bud_obstruction_2026-10-23';old=R/'audits/check_foreign_kinked_barrier_turn_independent.py';ns={'__file__':str(old)};exec(old.read_text().split('geometries=[]')[0],ns);W,M,walk,xy=(ns[k]for k in('W','M','walk','xy'));K={-1-1j,-1,-1j,0,1};a=json.loads((D/'renewal_F_bud_obstruction.json').read_text());base={};bud=2+4j;target=3-1j;rows=[]
def inventory(w):
 raw=walk(w);full=walk(w+M);assert raw['feasible']and full['feasible'];I={q for q,b in full['req'].items()if b}-K;O=({q for q,b in full['req'].items()if b}^raw['odd'])-{raw['p']+q*(-1j)**raw['h']for q in K};return raw,full,I,O
for name in'DCVU':
 raw,full,I,O=inventory(W[name]);assert 2 in O and [(i,ch)for i,(q,h,ch)in enumerate(full['reads'])if q==2]==[(8,'R')];base[name]=(raw,full,I,O)
 if name=='C':assert not I and(raw['p'],raw['h'])==(1j,3)
 else:
  for c in range(0,2 if name=='D'else 3):
   _,_,II,OO=inventory(W[name]+W['C']*c);assert II==I and 2 in OO
assert(base['U'][0]['p'],base['U'][0]['h'])==(4j,0)
for age,h in((3,1),(4,0)):
 for name in'DVU':
  tr,full,I,O=base[name];assert tr['h']==0
  for slot in I:
   p=bud-slot*(-1j)**h;end=p+tr['p']*(-1j)**h
   if age==3:
    assert end.real>=2
    if end.real==2:assert end==2+3j and end+1==3+3j
    else:assert end.real+1>target.real
   else:assert end.imag>=4>target.imag
   rows.append((age,name,tuple(xy(slot)),(*xy(p),h),(*xy(end),h)))
assert len(rows)==16;assert set(rows)=={(r['C_age'],r['consumer'][0],tuple(r['input_slot']),tuple(r['pose']),tuple(r['base_endpoint']))for r in a['endpoint_rows']}
assert sum(r[0]==3 and r[4][0]==2 for r in rows)==3
for name in'DVU':
 p=base[name][0]['p'];assert p.real>=0 and p.imag>0 and(p*(-1j)).real>0
assert base['C'][0]['p']*(-1j)==1
assert bud-target not in base['U'][1]['req']
f=walk(W['F']+M);assert not f['req'][-1+1j];assert next((i,ch)for i,(q,h,ch)in enumerate(f['reads'])if q==-1+1j)==(14,'R')
manifest=D/'manifest.json';assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='c1637f139a0555c710f4652ef18c4b8216a7de101ee16f9abd0b2316f9863f7f'
# The signed1344 statement explicitly treats a FIRST internal C at the full
# producer's birth clock and distinguishes a SECOND C's shifted clock.
maturity=R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/00_atomic_common_output_four_C.md';assert hashlib.sha256(maturity.read_bytes()).hexdigest()=='df49d94d2a41ff4933f7d124c2eea776d0e6fc9a0f72edbb94d036ef989e854b'
out={'status':'PASS universal exactage4 right-U-renewal immediate-F obstruction','manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'note_sha256':hashlib.sha256((D/'renewal_F_bud_obstruction.md').read_bytes()).hexdigest(),'atomic_fresh_births':4,'retirement_endpoint_rows':16,'age3_equality_endpoints':3,'analytic':'First actual post-U atom starts clock0 and writes(2,4) atR8. If it is internal first C, signed1344 uses full birth clock0, not C exit1; later C tails preserve the identity. Every retirement before renewing full Uentry at4 must start3E or4N. At3E x>=2; x>2 overshoots after the unique remaining C, equality2 forces endpoint(2,3), no intervening positive-x base and only later N-U upward motion. At4N y>=4 cannot reach targety-1. All full inputs equal base inputs, including marker/core absorption, and no C input exists. The renewing U context misses the bud; immediate F requires it white atphase14.','scope':'All genuine U/UC/UCC sources and arbitrary retained-eight connectors satisfying the signed age4 first renewal. No other foreign gate,6C contact, postforeign simplicity or seven-word termination conclusion.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
