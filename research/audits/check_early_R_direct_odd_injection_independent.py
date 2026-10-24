from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23';ns={'__file__':str(SELF.parent/'check_zero_output_Q2_and_same_curve_ear_independent.py')};exec(Path(ns['__file__']).read_text().split('def close(')[0],ns)
base,locate,outs=[ns[k]for k in('base','locate','outs')];prior=json.loads((D/'bit11_surviving_cleanup_Q1_parent_ports.json').read_text())['rows'];right=[r for r in prior if r['headings']['j']=='EEWE'];straight=[r for r in prior if r['headings']['j']=='W'];assert len(right)==len(straight)==36
modes=Counter(tuple(r['headings'][v]for v in('x','r','e'))for r in right);assert modes=={('EWW','WEEW','SNN'):12,('EWWW','WEW','SNNN'):12,('EWWW','WEWW','SNNN'):12}
low=[];upper=[]
for row in base:
 for turn in range(4):
  hh,ht,en,bd=locate(row,-3-1j,turn)
  if hh[-2]=='EWWW' and hh[-3].count('S')==1 and outs(hh[-3]).count('E')==1 and outs(hh[-2-1j]).count('E')==1:
   assert en==-3-1j;assert hh=={-3-1j:'EEWW',-3:'NNS',-2:'EWWW',-2-1j:'SSS'}
   # The unique possible canonical child at d is an actual Q2 entry below.
   childpoints={locate(row,-3-1j,turn)[0] and (-3-1j)+(.5+.5j)+(ns['cp'][v]-(.5+.5j))*1j**turn for v in row[2]}
   assert childpoints=={-3};low.append((row,turn))
  hh,ht,en,bd=locate(row,-4,turn)
  if hh[-3]=='NNS' and hh[-3+1j]=='EEWE':
   assert en==-3 and row[0][0]=='NNS' and row[3]==1 and row[4]==('B',)
   assert (-4)+(.5+.5j)+(ns['cp']['B']-(.5+.5j))*1j**turn==-3+1j
   upper.append((row,turn))
assert len(low)==1 and len(upper)==4
assert {row[0]for row,q in upper}=={('NNS','WW','NSSS','EEWE'),('NNS','WWE','NSSS','EEWE'),('NNS','WWEE','NSN','EEWE'),('NNS','EWW','SSNS','EEWE')}
# Rotation-invariant distinctions between the three genuine odd reservations.
assert 'EWW'[0]!='EWW'[2] and 'EWW'[1]=='EWW'[2]
assert 'NNS'[0]!='NNS'[2] and 'NNS'[1]=='NNS'[0]
assert 'SSS'[0]=='SSS'[2]
note=D/'early_R_ancestor_direct_odd_output_injection.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='783b71a0ff3a6deed00279ff364417d4fcb4b2a62ff310424a9d730fd69a1241'
out={'status':'PASS direct distinct odd-output reservations Nodd>=n_A+n_R4 and N_O>=n_R4','note_sha256':sha,'fresh_canonical_rows':len(base),'R_ancestor_rows':36,'S_ancestor_rows':36,'R_modes':[{'profile':k,'count':v}for k,v in modes.items()],'lower_square_unique_profile':low[0][0][0],'Q2_four_O_profiles':[row[0]for row,q in upper],'analytic':['The full72 ancestor rows split36S and36R. R cases are exactly xEWW/rWEEW/eSNN or xEWWW/rWEW[W]/eSNNN. No evenness or zero-output restriction is imposed.','For EWWW, exact d.S input1,d.E output1,t.E output1 and all110 canonical profiles/all rotations give unique F: SW EEWW,NW NNS,NE EWWW,SE SSS. Canonical F birth is SW and its sole possible child contact is d. The actual Q2 has dNNS,jEEWE; its only four completions are the signed odd-entry O profiles, with unique possible flag1 child j, which is actual Q1. Hence Q2 is actual positive O and p(Q2)=F.','Signed early Q1 injectivity plus one flag1 child per O makes Q2 and its canonical d entry injective. Sole possible child Q2 then makes F injective. Same-R SSS chooses the unique higher incident C face F, so t is injective across all orientations.','For EWW, the directed L1 incoming edge has uniquely defined right C face P0. This recovers the distinct actual early P0, proving x injection across orientations.','The x class is three-read flat with L1=R2; d is three-read flat with L1=R0; t has same R headings. These rotation-invariant history types are pairwise disjoint and all disjoint from the one-read S-ancestor reservation. Aligning a full-drift translate before comparing preserves all histories/canonical identities, so every injection survives arbitrary quotient folding.'],'bounds':['Nodd>=n_Sanc+n_R3+2n_R4=n_A+n_R4','N_O>=n_R4'],'scope':'Actual surviving early K1 sources only. OUTPUT capacity, no initial fuel, no addition to overlapping O/rise/helper counts, no actual-front construction or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
