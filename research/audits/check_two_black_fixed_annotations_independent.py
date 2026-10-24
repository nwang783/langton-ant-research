from pathlib import Path
from collections import Counter
import json,gzip,hashlib
R=Path('/workspace/shared/langton');P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
M=json.loads((P/'TWO_BLACK_FIXED_WORD_ANNOTATIONS_MANIFEST.json').read_text())
for f,h in M['files'].items():assert sha(P/f)==h
ind=R/'audits/two_black_fixed_windows_independent.txt';assert sha(ind)==sha(P/'TWO_BLACK_WORD_ALL_FIXED_OUTPUT.txt')
source_audit=R/'audits/generic_P104_fixed_cohort_independent.json';assert sha(source_audit)=='ca1747663654fb773d268e29aca98715ae02e89ca58caf4d6eb71838ff8d8bd4'
B=json.loads((P/'PRISTINE_COHORT_ADVANCE_CHECKED.json').read_text());H=B['blank_tail_word'];assert len(H)==104
phases={H[i:]+H[:i]:i for i in range(104)};assert len(phases)==104
moves=[1j,1,-1j,-1];xy=lambda z:[int(z.real),int(z.imag)];counts=Counter();hist=Counter();nj=0;updates=0;windows=0;uncompressed=hashlib.sha256()
with gzip.open(P/'TWO_BLACK_WORD_JOBS.jsonl.gz','rt')as jf,open(P/'TWO_BLACK_WORD_ALL_FIXED_INPUT.txt')as inf,open(ind)as rawf,gzip.open(P/'TWO_BLACK_FIXED_WORD_ANNOTATIONS.jsonl.gz','rt')as af:
 for jl,il,rl,al in zip(jf,inf,rawf,af,strict=True):
  j=json.loads(jl);a=json.loads(al);assert j['id']==a['id']==nj
  nums=list(map(int,il.split()));expected=[nj,len(j['cells'])]+[n for p in j['cells']for n in p]+[len(j['windows'])]+[w['time']for w in j['windows']];assert nums==expected
  raw=rl.split();assert int(raw[0])==nj and len(raw)==len(j['windows'])+1
  assert (a['source'],a['kind'],a['index'],a['initial_black'])==(j['source'],j['kind'],j['index'],j['cells'])
  assert len(a['windows'])==len(j['windows'])
  for w,z,tok in zip(j['windows'],a['windows'],raw[1:],strict=True):
   t,pose,delta,word=tok.split(':');pose=list(map(int,pose.split(',')));delta=list(map(int,delta.split(',')));assert int(t)==w['time'];phase=phases[word]
   assert z=={'kind':w['kind'],'time':int(t),'pose_before':pose,'actual_displacement':delta[:2],'heading_restored':True,'canonical_phase':phase,'actual_word':word}
   p=0j;h=pose[2]
   for ch in word:h=(h+(1 if ch=='R'else-1))%4;p+=moves[h]
   assert xy(p)==delta[:2] and h==pose[2]and delta[2]==0 and abs(p.real)==abs(p.imag)==2
   if w['kind']=='terminal':assert delta[:2]==j['terminal_drift']
   counts[w['kind']]+=1;hist[w['kind'],phase]+=1;windows+=1
  uncompressed.update(al.encode());updates+=j['updates'];nj+=1
assert(nj,windows,updates)==(102488,217233,3437614232)
ref=json.loads((P/'TWO_BLACK_FIXED_WORD_ANNOTATIONS_CHECKED.json').read_text());assert uncompressed.hexdigest()==ref['complete_jsonl_uncompressed_sha256']
assert ref['canonical_reference_word']==H and dict(counts)==ref['window_counts']
assert sorted((r['kind'],r['phase'],r['count'])for r in ref['canonical_phase_histogram'])==sorted((k[0],k[1],v)for k,v in hist.items())
report={'status':'PASS complete fixed-family/window canonical annotations; direct certB leaves remain unannotated','script_sha256':sha(Path(__file__)),'manifest_sha256':sha(P/'TWO_BLACK_FIXED_WORD_ANNOTATIONS_MANIFEST.json'),'independent_source_coverage_audit_sha256':sha(source_audit),'independent_CPP_sha256':sha(R/'audits/replay_two_black_fixed_windows_independent.cpp'),'independent_executable_sha256':sha(R/'audits/replay_two_black_fixed_windows_independent'),'independent_raw_output_sha256':sha(ind),'independent_run_time_log':(R/'audits/two_black_fixed_windows_independent.time').read_text(),'blank_reference_binding':{'file':'PRISTINE_COHORT_ADVANCE_CHECKED.json','sha256':sha(P/'PRISTINE_COHORT_ADVANCE_CHECKED.json')},'anchors':nj,'windows':windows,'counts':dict(counts),'full_fine_updates':updates,'canonical_nonmatches':0,'family_only_pristine_bad_cut_bound':270504+6*375,'analytic_review':['Independent literal-data parser already rebuilt all source anchors, exact slab parameter maps and 506 child coverage','Fresh independent epoch-tag complete-board C++ replay, no author simulator headers, reproduced every byte of all217233 windows; all3,437,614,232 fine reads counted','Every full window literal word, phase, incoming pose, drift and restored heading reclassified against signed actual blank standard104','Full Rid/Rtr observation/corridor transport proved in retained source duplicates exact canonical switch words; separation preserves both corridor window types for all parameters','Finite base arbitrary length <=s and <=J+1 canonical pieces give272754 for covered families only'],'NOT_COVERED':['Dynamic direct certB terminal words','universal canonical624375 before-third bound','global capture or fixed-cohort fuel after reset']}
out=R/'audits/two_black_fixed_annotations_independent.json';out.write_text(json.dumps(report,indent=2)+'\n');print(sha(out));print(report['status'])
