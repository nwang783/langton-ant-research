from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23'
ns={'__file__':str(R/'audits/check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns)
W,M,walk,xy=(ns[k]for k in('W','M','walk','xy'))
east=2+1j;breaker=3-1j;q=east-breaker;assert q==-1+2j;variants=[]
for name in('U','UC','UCC'):
 t=walk(''.join(W[c]for c in name));reads=[(i,c)for i,(p,h,c)in enumerate(t['reads'])if p==q]
 assert reads[0][1]=='L'and reads[-1][1]=='R'and reads[-1][0]<28
 assert all(p!=q for p,h,c in t['reads'][28:]);assert(q in {p for p,b in t['req'].items()if b}^t['odd'])
 variants.append({'name':name,'q_reads':reads,'full_completion_C_clock':4+name.count('C')})
p=-3+6j;h=3;local=(east-p)/((-1j)**h);assert local==-5-5j
raw=walk(W['B']);full=walk(W['B']+M);assert len(W['B'])==74 and all(p!=local for p,h,c in raw['reads'])
assert full['req'][local]is False and next((i,c)for i,(p,h,c)in enumerate(full['reads'])if p==local)==(82,'R')
manifest=D/'U_east_rebirth_guard_manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='bce8ef93e45d892923f1ac25e609e94b70f95760f727e7e22ca10086d49bd5b5'
for name,value in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==value
out={'status':'PASS two-generation same-cell east black guard through full-cut age5 and B tail exclusion','manifest_sha256':sha,'actual_breaker_variants':variants,'B_before_white':{'pose':[-3,6,3],'local_cell':[-5,-5],'phase':82,'raw_length':74},'analytic':['At any completed old-eight full cut, either the original east identity remains current or its actual first breaker has occurred. Signed directed renewal and exact clock force that event to(3,-1,N) at4.','Its actual U-base deletes the original east cell as an input and recreates it as its own recycled-q output; source C tails preserve the new black identity. The q consumer clock is earliest6 globally.','A breaker UCC completes at6 and cannot lie before a target full cut at<=5. There is no unaccounted internal fine/atomic cut: the statement is explicitly full-packet boundaries after creator completion.','B(-3,6,W) at5 requires the cell before-white, first at successor RAW phase8. The foreign RAW never visits it, so the entry black guard directly contradicts the complete B+M11 context without extending any permanence theorem past foreign entry.'],'scope':'Actual color guard through age5 with an explicit identity replacement, not single-token permanence, all-fine-time black constancy, all-age pose exclusion or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
