from pathlib import Path
import json,hashlib
S=Path(__file__);D=S.parents[1]/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'T_TERMINAL_RAY_EXPOSURE_MANIFEST.json';assert sha(MF)=='5aeade0832f03ee73e6739a44711e92c47a5a057c51d217920574c6d4f26d3a9';mf=json.loads(MF.read_text())
for kind in ('files','dependencies'):
 for f,h in mf[kind].items():assert sha(D/f)==h
J=json.loads((D/'T_TERMINAL_RAY_EXPOSURE_CHECKED.json').read_text());T=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());B=json.loads((D/'T_PORT7_ABSORBER_CHECKED.json').read_text());ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);K,geometry,sim,xy=[ns[k]for k in('K','geometry','sim','xy')];W=sim(K,104)['word'];out={}
for lab,word,tail in [('T',T['T_recovery'],T['T_tail_word']),('T7',B['word'],B['tail_word'])]:
 pts,_,p,h=geometry(0j,0,word);qs,_,e,eh=geometry(p,h,tail);d=e-p;first={};rows=[]
 for i,q in enumerate(pts):
  if q.real==q.imag and q.real>=0 and q.real%2==0:first.setdefault(int(q.real)//2,i)
 for i,q in enumerate(qs):
  sol=[]
  if d.real==d.imag:assert q.real!=q.imag
  else:
   num=q.imag-q.real;den=d.real-d.imag
   if num%den==0:
    k=int(num//den);r=q+k*d
    if k>=0 and r.real>=0 and r.real%2==0:
     a=int(r.real)//2;sol.append([a,k]);first[a]=min(first.get(a,10**99),len(word)+104*k+i)
  rows.append({'phase':i,'point':xy(q),'solutions':sol})
 got={'first_reads':[[a,t]for a,t in sorted(first.items())],'tail_ray_tests':rows,'drift':xy(d)};assert got==J[lab];assert set(first)==set(range(10 if lab=='T' else 19));out[lab]=got
assert J['chronological_T7_extra_ports']==sorted([[t,a]for a,t in out['T7']['first_reads']if a>=8])
q=202+201j;seed=K|{q+a*(2+2j)for a in (0,1,3,5,6,7,10,11)};seq=W*100+W[:13]+B['word'][:18600]+'L';z=sim(seed,len(seq),expected=seq);r=J['nearer_bit_skipping_control'];near=q+20+20j;far=q+22+22j;ids={p:-i-1 for i,p in enumerate(sorted(seed,key=lambda p:(p.real,p.imag)))}
assert len(seed)==21 and z['first'][far]==29013 and near not in z['first'] and z['B'][near]==ids[near] and z['dead'][ids[far]]==29013
assert sorted([[xy(p),i]for p,i in z['B'].items()])==r['whole_post_collision_black']and [xy(z['p']),z['h']]==r['post_collision_pose'] and sorted(map(xy,seed))==r['seed'] and len(seq)==r['physical_reads']
for a in J['safe_far_indices']:assert a>=19 and a not in dict(out['T7']['first_reads'])
reports=['check_T_port7_absorber_independent.json','check_last_M_register_scattering_independent.json'];assert all(json.loads(S.with_name(f).read_text())['status'].startswith('PASS')for f in reports)
O={'status':'PASS exact complete T/T7 terminal-ray exposure and nonmonotone first-input control','manifest':sha(MF),'script':sha(S),'dependencies':{f:sha(S.with_name(f))for f in reports},'exposure':out,'finite_control_reads':len(seq),'analytic_review':['Every finite read and all104 exact integer ray intersections are reconstructed. T exposes exactly0..9; T7 exactly0..18. The post-M T continuation lies in x<=qM.x+38<qT.x, since the signed spacing is at least228, and adds no nonnegative original T-ray hit.','Fresh phase13 launch ensures all additional forward-ray cells were unread before entry. First-difference coupling therefore retains any finite original cohort beyond10 for T or19 for T7 without changing the complete future. This extends literal source classes, not full-halfplane equality, and preserves the required WHITE lower ports. No arbitrary old archive is admitted.','The literal21-cell source first consumes farther original ray11 at29013 while nearer original ray10 remains BLACK and unread. Full post-L state is verified; no conclusion is drawn about its later fate or capture. Counterfactual extra-input coupling is not instantaneous relevance loss in a single orbit.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
