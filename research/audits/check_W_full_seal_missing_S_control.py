from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'seven_word_spatial_return_2026-10-23';ns={'__file__':str(SELF)};exec((SELF.parent/'check_foreign_kinked_barrier_turn_independent.py').read_text().split('geometries=[]')[0],ns);walk,W,M,xy=ns['walk'],ns['W'],ns['M'],ns['xy']
word=''.join(W[c]for c in'UVVCCVV')+M;rr=walk(word);assert rr['feasible'];seed={q for q,b in rr['req'].items()if b};assert len(seed)==16
board=set(seed);p=0j;h=0;birth={q:-1 for q in seed};tag=5j;hits=[];sourceborn=None;returnedstart=28+18+48+18
for t,ch in enumerate(word):
 assert('L'if p in board else'R')==ch
 if p==tag:hits.append((t,ch,birth.get(p)))
 if ch=='L':birth.pop(p)
 else:birth[p]=t
 board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
# Source first V is genuine plain V, the next packet is VCC rather than its own C.
source=walk(W['U']);assert(source['p'],source['h'])==(4j,0)
assert returnedstart==112
assert hits[-1][0]==returnedstart+19 and hits[-1][1]=='L'
sourceR=hits[-1][2];assert 28<=sourceR<46
p0=1+3j;N=1+3j;C1=1j;C2=-1;S=-1-3j;assert p0+N+C1+C2+S==4j
manifest=D/'ordered_W_full_output_seal_manifest.json';mh=hashlib.sha256(manifest.read_bytes()).hexdigest();assert mh=='6ea48d5dc26b7265ad55e83a99c5282a71fdbfc41f86f88b94934844306c3ac1'
out={'status':'NOT PASSED: two plain-source endpoint exclusions omit an arbitrary S run after C2','blocked_manifest_sha256':mh,'exact_missing_endpoint_equations':['d+v-e-3f-4g-a-b=0','d+3v+4u+e+f-a-3b-4c=0'],'nonzero_geometric_solution':{'N_V':1,'S_V':1,'all_other_counts':0},'actual_genuine_U_entry_control':{'full_packets':['U','V','VCC','V','V'],'literal_word_with_actual_M11':word,'initial_complete_black_cells':sorted(map(xy,seed)),'initial_pose':[0,0,0],'physical_reads':len(word),'final_black_cells':sorted(map(xy,board)),'final_pose':[*xy(p),h],'plain_V_source_entry':[0,4,0],'last_V_consumer_entry':[0,8,2],'source_A_global':[0,5],'source_tag_read_history':hits,'source_birth':sourceR,'physical_consumption':returnedstart+19,'owner':'following actual word RAW phase2 after final plain V; marker-only V input(0,3)'},'scope':'This is a genuine complete-eight U-entry physical control refuting the plain-source endpoint/ownership argument as stated. It is not a realization of the narrower prescribed foreign endpoint and does not by itself refute every possible replacement full-seal theorem. Earlier signed ordered matching and identity bottleneck are unaffected. No at-most-one/full-output-seal consequence is signed.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(hits)
