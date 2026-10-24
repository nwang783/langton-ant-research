from pathlib import Path
from collections import Counter
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'causal_archive_frontier_2026-10-23';K={p for p,b in walk(mark)[2].items()if b};G={}
for s in(0,1,4,5,6,7,8,9):
 e,h,_,fl=walk(raws[s]);bb={p for p,b in walk(raws[s]+mark)[2].items()if b};G[s]=(bb-K,(bb^fl)-{e+rotation(q,h)for q in K})
selected={0:1j,1:1j,4:1+2j,5:1+2j,6:3j,7:3j,8:3j,9:3j};H=lambda q:int(q.real+q.imag)
assert all(q in G[s][0]for s,q in selected.items());assert{H(q)for q in selected.values()}=={1,3}
odd={H(q)for _,outs in G.values()for q in outs if H(q)%2};assert odd=={1,3,5,7}
for s in(0,4,7):
 e,h,_,_=walk(raws[s]);assert h==0 and H(e)in(2,4)
assert len(range(2,295,2))==147 and 4851+2*147==5145
for lo in range(-10,11):
 for ell in range(20):
  hi=lo+2*ell;assert len(range(lo-3,hi,2))==ell+2
ref=json.loads((D/'parallel_inherited_interval_controls.json').read_text());assert{str(s):list(xy(q))for s,q in selected.items()}==ref['selected_inputs']
# Funding tags are original observables, not reset incidence roots.
ns={'__file__':str(SELF.parent/'check_U1_U_origins_diagnostic_independent.py')};exec((SELF.parent/'check_U1_U_origins_diagnostic_independent.py').read_text().split('def chords(s,p,h):')[0],ns)
A=ns['A'];peaks=ns['peaks'];weights=ns['weights'];OG=ns['G'];o=-1+7j;idx=sorted(OG[9][1],key=xy).index(o)
assert A[1]==peaks[9,1]==22
inputH=max(H(rotation(q,1))for q in OG[9][0]);assert inputH==5
oldvalue=2*H(rotation(o,1))+weights[f'w_9_{idx}_1'];assert oldvalue==22
truebound=max(A[1],peaks[9,1],28+2*inputH);resetvalue=28+2*H(rotation(o,1));assert(truebound,resetvalue)==(38,44)
p=D/'parallel_inherited_interval_necessity.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='4420e81f69c832598b02ad6e5d3b34b4e4459299050f86d31b7c9fceeb30680b'
f=ROOT/'core_periodicity_new/funding_frontier_dependency_review_20261023_2003.md'
out=dict(status='PASS inherited parallel-interval necessity and original-funding frontier interface',parallel_note_sha256=sha,funding_review_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),selected_inputs={s:xy(q)for s,q in selected.items()},odd_output_progresses=sorted(odd),cohort_count=147,post_entry_bound='N<=4851+sum(ell_a+2)<=5145+sum ell_a',funding_control=dict(source='UCC',phase=1,entry_and_created=22,max_input_height=5,true_initial_activation_max=38,output=xy(o),original_produced_value=oldvalue,artificial_reset_activation=resetvalue),analytic='Each actually used selected cell has odd offset1/3 from a distinct parity-fixed epoch start. A cohort span2ell therefore permits at mostell+2 starts. After entry funding expires, at most4851 transverse exceptions and147 even-age parallel cohorts remain. Odd source output offsets span6, so source head half-span>=ell-3. These are actual inherited intervals, not a decreasing rank. Exact330 recognition can retain original funding tags alongside separately reset genealogy, but cannot infer uniform states from bounds that still depend on unbounded C-clock.',scope='No original V1/U1 closure, no new coverage beyond11/13, no component separation from birth identity, no periodic-profile or finite-state/capture claim.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(out['funding_control'])
