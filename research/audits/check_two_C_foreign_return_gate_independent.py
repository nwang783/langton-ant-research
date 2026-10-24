from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'foreign_U_ancestry_obstructions_2026-10-23';old=R/'audits/check_foreign_kinked_barrier_turn_independent.py';ns={'__file__':str(old)};exec(old.read_text().split('geometries=[]')[0],ns);W,M,walk,xy=(ns[k]for k in('W','M','walk','xy'))
a=json.loads((D/'two_C_return_gate.json').read_text());K={-1-1j,-1,-1j,0,1};L={0,1,1j,1+1j};q=-1j;masks={};rows=[];steps={}
for name in'DCVU':
 raw=walk(W[name]);full=walk(W[name]+M);assert raw['feasible']and full['feasible'];out={p for p,b in full['req'].items()if b}^raw['odd'];out-={raw['p']+p*(-1j)**raw['h']for p in K};masks[name]=out
 assert sorted(map(list,map(xy,out)))==a['atomic_output_masks'][name]
 assert all(p.imag>=0 and p.real+p.imag>=0 for p in out)
 if name!='C':
  assert raw['h']==0;p=raw['p'];nw=p*1j;assert p.imag>=0 and p.imag-p.real>=0 and nw.imag-nw.real>=0;steps[name]=[int(p.imag-p.real),int(nw.imag-nw.real)]
  for slot in out:
   p=q+slot;core={p-z for z in K};sector=int(p.real+p.imag+2)%2;hits=L&core
   if not sector:assert hits
   rows.append((name,xy(slot),(*xy(p),2),'wrong_active_sector'if sector else'held_star_in_entry_core',tuple(sorted(map(xy,hits)))))
assert set(rows)=={(r['atom'],tuple(r['output_slot']),tuple(r['producer_pose']),r['reason'],tuple(map(tuple,r['core_hits'])))for r in a['S_output_alignment_rows']}
assert Counter(r[0]for r in rows if r[3]=='held_star_in_entry_core')=={'V':3,'U':5}
u=walk(W['U']);assert(u['p'],u['h'])==(4j,0);assert[(i,ch)for i,(p,h,ch)in enumerate(u['reads'])if p==q]==[(3,'L')]
c=walk(W['C']);assert(c['p'],c['h'])==(1j,3)
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
for gid,base,nc in[(0,'D',0),(1,'D',1),(4,'V',0),(5,'V',1),(6,'V',2),(7,'U',0),(8,'U',1),(9,'U',2)]:assert G[gid]['word']==W[base]+W['C']*nc
for name,p in[('F',-3-3j),('Q',-3-5j),('B',-2-6j)]:
 tr=walk(W[name]);ctx=walk(W[name]+M);assert(p-tr['p'],(2+tr['h'])%4)==(1-1j,0);local=p-q;reads=[(i,ch)for i,(z,h,ch)in enumerate(ctx['reads'])if z==local];assert reads==[(len(W[name])+1,'L')];assert ctx['req'][local]
 assert q not in{p-z for z in K};assert not L&{p-z for z in ctx['req']}
 dc=walk(W['D']+W['C']+M);assert next((i,ch)for i,(z,h,ch)in enumerate(dc['reads'])if z+1-1j==1)==(11,'L')
manifest=D/'manifest.json';assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='b6b6ac61e7dd234efd0752a2329046fceb9d46c0ec2542d303b97e4d7913a24f'
out={'status':'PASS all-word exact-two-C obstruction for the three prescribed foreign return gates','manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'note_sha256':hashlib.sha256((D/'two_C_return_gate_obstruction.md').read_bytes()).hexdigest(),'active_S_output_alignments':8,'zero_C_N_W_H_increments':steps,'analytic_review':'The creator deletes q at read3. Before first C every atomic output has y>=4. Between first and second C every output has H=y-x>=5. After second C every parity-valid zero-C producer of q places a held original star in its entry core. This exhausts all atomic residual-emission times, including internal C tails, without bounding zero-C lengths. At the foreign entry q is outside core; foreign raw never reads it and actual successor phase1 requires black.','scope':'Only the fixed F(-3,-3,S),Q(-3,-5,S),B(-2,-6,S) gates after exactly2C. No6C exclusion, Jordan assumption, attained ancestry or global seven-word termination.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
