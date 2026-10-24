from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'postforeign_erosion_return_port_restoration_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'C_repair_shadow_manifest.json';assert sha(MF)=='04f74edcdf8e5192817e14458e163809d7d883bd82f64f32f7557d8b4b6a8610';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
J=json.loads((D/'C_repair_shadow.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,tr,rot,K,center,xy,meet=[ns[k]for k in('W','M','tr','rot','K','center','xy','meet')];raw=lambda ts:''.join(W[a]for a in ts);vec=[1j,1,-1j,-1];controls=[]
for r in J['three_exact_prepared_or_genuine_controls']:
 ts=r['tokens'];pre=ts[:-6];assert ts==pre+'VCCVCD'and pre in('','UQ','UB');z=tr(raw(ts)+M);good=not pre;assert(z['bad']is None)==good
 src=tr(raw(pre));vs=len(raw(pre));cs=vs+len(raw('VCCV'));ds=cs+len(W['C']);hole=src['p']+rot(src['h'])*(-1-1j);shadow=src['p']+rot(src['h'])*(-1-2j);tagA=src['p']+rot(src['h'])*1j
 if good:word=raw(ts)+M
 else:
  fail,prev,q,ch=z['bad'];assert(fail,prev,q,ch)==(ds+8,28+(57 if pre=='UQ' else 67),shadow,'R');word=(raw(ts)+M)[:fail];assert tr(raw(ts[:-1]))['bad']is None and tr(raw(ts[:-1])+M)['bad']==z['bad']
 c=tr(word);seed={q for q,b in c['req'].items()if b};assert sorted(map(xy,seed))==r['complete_seed']and len(seed)==r['initial_black_mass'];B={q:('initial',None)for q in seed};p=0j;h=0
 for t,ch in enumerate(word):
  before=B.get(p);assert(ch=='L')==(p in B)
  if ch=='L':B.pop(p);h=(h-1)%4
  else:B[p]=('R',t);h=(h+1)%4
  rr=r['executed_fine_reads'][t];assert(rr['cell'],rr['turn'],rr['before_identity'],rr['after_identity'])==(xy(p),ch,list(before)if before else None,list(B[p])if p in B else None)
  if t==cs+1:assert p==tagA and before==('R',vs+11)and ch=='L'
  if t==cs+12:assert p==hole and ch=='R'
  if t==ds+5:assert p==hole and before==('R',cs+12)and ch=='L'
  p+=vec[h]
  if str(t+1)in r['exact_cut_snapshots']:
   snap=r['exact_cut_snapshots'][str(t+1)];core={p+rot(h)*q for q in K};assert(snap['hole_BLACK'],snap['hole_identity'],snap['hole_CORE'],snap['original_A_alive'],snap['shadow_BLACK'],snap['shadow_identity'])==(hole in B,list(B[hole])if hole in B else None,hole in core,B.get(tagA)==('R',vs+11),shadow in B,list(B[shadow])if shadow in B else None)
   if t+1==ds:assert B[hole]==('R',cs+12)and hole in core and core<=set(B)
 if pre:assert p==shadow and B[shadow]==('R',prev)and word[-1]==raw(ts)[ds+7]
 else:assert len(seed)==8
 def chord(a,p,h):z=tr(W[a],p,h);return center(p,h),center(z['p'],z['h'])
 cp=tr(raw(ts[:-2]));dp=tr(raw(ts[:-1]));old=chord('V',src['p'],src['h']);assert meet(*old,*chord('C',cp['p'],cp['h']))is None and meet(*old,*chord('D',dp['p'],dp['h']))==(0,1)
 controls.append(dict(tokens=ts,seed_mass=len(seed),executed_reads=len(word),C_RAW_complete=True,C_plus_real_M11_complete=good,repair_tick=cs+12,repair_L_tick=ds+5,shadow_failure=None if good else ds+8,full_D_executed=good))
out=dict(status='PASS actual C-RAW CORE-hole repair and distinct foreign-shadow obstruction, preserving RAW versus marked completion',manifest_sha256=sha(MF),script_sha256=sha(S),controls=controls,analytic_review=['The prepared8 VCCVCD+M factor genuinely attains an oldV-start/newD-end contact. Both real UQ/UB prefixes instead complete every C RAW read, including physical oldA deathC1 and new holeR12; no oldV contact occurs along that C chord.','At Cexit the repaired hole is in the geometrical EXIT K, and all K cells are physically BLACK in each complete board. This does not promote C+M recognition: nextD L5 consumes the new repair, but nextD R8 demandsWHITE at a distinct SAME original Q R57/B R67 shadow. Every actual fine identity and cut was independently replayed.','Thus core repair itself is not contact-forcing. In genuine controls the next requiredM fails at read9 and no fullD or its proxy is executed; the actual next turn isL. Both active-core R restoration and L removal count. No postforeign age, residual-only funding theorem or arbitrary-tail counterexample is asserted.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
