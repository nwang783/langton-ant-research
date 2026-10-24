from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23';ns={'__file__':str(SELF.parent/'check_zero_output_Q2_and_same_curve_ear_independent.py')};exec(Path(ns['__file__']).read_text().split('def close(')[0],ns)
base,locate,outs=[ns[x]for x in('base','locate','outs')];prior=json.loads((D/'bit11_surviving_cleanup_Q1_parent_ports.json').read_text())['rows'];modes=Counter();Jprofiles={}
for r in prior:
 hs=r['headings'];anc='S'if hs['j']=='W'else'R';assert hs['j']in('W','EEWE')
 mode='3'if hs['x']=='EWW'else'4a'if hs['r']=='WEW'else'4b';modes[anc+mode]+=1
 assert tuple(hs[v]for v in('x','r','q','e'))=={'3':('EWW','WEEW','SSS','SNN'),'4a':('EWWW','WEW','SSS','SNNN'),'4b':('EWWW','WEWW','SSSN','SNNN')}[mode]
 physical={-1-1j:hs['r'],-1j:hs['q'],-1:hs['e'],0:hs['Z']};assert hs['Z']=='WWEW'
 if mode in Jprofiles:assert Jprofiles[mode]==physical
 else:Jprofiles[mode]=physical
assert len(prior)==72 and modes==Counter({a+m:12 for a in('S','R')for m in('3','4a','4b')})
matched=[]
for mode,physical in Jprofiles.items():
 hits=[]
 for row in base:
  for turn in range(4):
   hh,ht,en,bd=locate(row,-1-1j,turn)
   if hh==physical:
    assert en==0 and row[2]==() and row[0][0]=='NNSN';hits.append((row,turn))
 assert len(hits)==1;matched.append((mode,hits[0][0][0],hits[0][1]))
low=[]
for row in base:
 for turn in range(4):
  hh,ht,en,bd=locate(row,-3-1j,turn)
  if hh[-2]=='EWWW'and ht.get(-4)==-1 and hh[-3].count('S')==0 and outs(hh[-3]).count('E')==1 and outs(hh[-2-1j]).count('E')==1:
   assert hh=={-3-1j:'EEWW',-3:'NN',-2:'EWWW',-2-1j:'SSS'}
   assert en==-3-1j and not row[2]and row[0][0]=='NNSS';low.append((row,turn))
assert len(low)==1
# History features are invariant under simultaneous rotation of every heading.
assert 'WWEW'[1]=='WWEW'[3] and 'EEWW'[1]!='EEWW'[3]
assert 'EWW'[0]!='EWW'[2]and'EWW'[1]=='EWW'[2]
assert 'SNN'[0]!='SNN'[2]and'SNN'[1]=='SNN'[2]
assert 'NNS'[0]!='NNS'[2]and'NNS'[1]=='NNS'[0]
assert all(w[0]==w[2]for w in('SSS','WEW'))
notes=['early_first_branch_leaf_role_separates_odd_outputs.md','early_all_ancestor_six_mode_disjoint_output_union.md','early_S4_flag_zero_leaf_output_and_two_per_source.md'];hashes={n:hashlib.sha256((D/n).read_bytes()).hexdigest()for n in notes}
out={'status':'PASS exact early first-leaf/S4 lower-leaf roles and disjoint union Nodd>=2*n_A','note_sha256':hashes,'fresh_canonical_rows':len(base),'signed_prior_rows':72,'six_mode_counts':dict(modes),'three_first_J_leaf_completions':matched,'unique_S4_lower_leaf_profile':low[0][0][0],'weights':{'S3':4,'S4a':4,'S4b':2,'R3':3,'R4a':4,'R4b':2},'analytic':['All72 complete ancestor rows split six modes of12. The first J square depends only on lower mode, not S/R ancestry. Fresh110 canonical profiles/all rotations give exactly one completion each, canonical birth at Z and zero possible children. Since its entry WWEW has equal L1/L3, J is flag-one leaf. Its unique parent is the main D, which has both actual J and selected RIGHT G children.','Across all ancestry types, mode3 x/e are positive-flat odd cells. Incoming L1 right-C recovers P0 for x and J for e. An x/e coincidence would force J=P0 and their parents main D=Q1, impossible because D has at least two actual children while Q1 has exactly one. Each individual family injects through the signed P0 or J/source recovery.','Same-R q/r recover their unique higher J leaf, hence D and its canonical Z frame. Distinct q/r corners of that frame cannot identify under a nonzero full-drift translate fixing the same physical face; distinct source J classes cannot collide. Their R-heading type separates them from positive/negative-flat outputs.','R4 t recovers a degree-one lower F, hence cannot equal q/r whose higher J is a leaf. The signed R4 d negative-flat and S singleton families remain disjoint by intrinsic history/multiplicity.','S4 exact ports and opposite height M-1 give uniquely EEWW/NN/EWWW/SSS lower F, canonical incoming flag zero, no possible children. Its unique positive-flat four-read x recovers P0 and source, so F and its same-R t inject across all S4 sources and rotations. This t cannot collide with q/r (flag-zero versus flag-one higher leaf) or R4 t (leaf versus degree-one higher face).','All comparisons align full physical lifts first, then use actual canonical parent, flag and degree. No spatial nonaliasing, separate component or zero-output assumption is substituted. Counting each disjoint reservation once yields weights4,4,2,3,4,2 and hence at least two outputs per early source.'],'scope':'Complete WHITE cap4 K1 front, actual surviving early-source classes only. OUTPUT lower bound, not initial fuel, not added to overlapping global helper/O/rise reservations; no capture or front exclusion.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(hashes)
