from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';old=R/'audits/check_foreign_kinked_barrier_turn_independent.py';ns={'__file__':str(old)};exec(old.read_text().split('geometries=[]')[0],ns);W,M,walk,xy=(ns[k]for k in('W','M','walk','xy'));K={-1-1j,-1,-1j,0,1};L={0,1,1j,1+1j};a=json.loads((D/'foreign_U_age4_renewal_branch.json').read_text());preds=[]
for name in'DVU':
 tr=walk(W[name]);assert tr['h']==0;p=3+3j-tr['p'];hits=L&{p+q for q in K};preds.append((name,xy(p),sorted(map(xy,hits))))
assert preds==[('D',(2,2),[(1,1)]),('V',(2,0),[(1,0)]),('U',(3,-1),[])]
# At the unique U predecessor its lower pair is exactly the original east pair.
assert{3-1j+q for q in(-1+1j,-1+2j)}=={2,2+1j}
f=walk(W['F']+M);assert f['feasible'];assert not L&{3+3j+p for p,h,ch in f['reads'][:56]};assert [(i,ch)for i,(p,h,ch)in enumerate(f['reads'])if p+3+3j==1j]==[(57,'L')]
W.update(UCC=W['U']+W['C']*2,VC=W['V']+W['C'],DC=W['D']+W['C']);recipe=a['recipe'];prefix=''.join(W[x]for x in recipe[:-1]);assert len(prefix)==182;word=prefix+W['F'];bad=walk(word);assert not bad['feasible']and(bad['i'],bad['q'],bad['first'])==(196,2+4j,36)
t=walk(word[:196]);assert t['feasible'];seed={q for q,b in t['req'].items()if b};assert len(seed)==20 and sorted(map(list,map(xy,seed)))==a['actual_consistent_prefix_seed']
oldtr=walk(prefix+M);assert oldtr['feasible'];oldseed={q for q,b in oldtr['req'].items()if b};assert len(oldseed)==19 and oldseed<seed
board=set(seed);p=0j;h=0;reads=[];dirs=(1j,1,-1j,-1)
for i,ch in enumerate(word[:196]):
 if i in(154,182):assert(p,h)==((3-1j,0)if i==154 else(3+3j,0))
 assert(p in board)==(ch=='L');reads.append((p,ch));board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
assert p==2+4j and p in board and word[196]=='R';assert[(i,ch)for i,(q,ch)in enumerate(reads)if q==p]==[(36,'R')]
assert[(i,ch)for i,(q,ch)in enumerate(reads)if q==1j]==[(11,'R'),(15,'L'),(19,'R')];assert 1j in board
manifest=D/'foreign_U_age4_renewal_branch_manifest.json';assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='5dbafb9bef1c90040ae46e77951ca5ad97a71a442215a5a8313bfe367074d5e5'
out={'status':'PASS immediate original-cycle renewal reduction and one immutable failed F extension','manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'note_sha256':hashlib.sha256((D/'foreign_U_age4_renewal_branch.md').read_bytes()).hexdigest(),'analytic':'D/V immediate predecessors hit held original stars. Remaining plain U at(3,-1,N) consumes the original east pair if intact. An earlier first breaker would already have been at this exact pose by signed directed renewal, violating the still preforeign simple center path. Hence it is the first breaker and exact full-source-entry age4. No postforeign simplicity is used.','known_control':{'original_seed_mass':19,'prefix_seed_mass':20,'consistent_reads':196,'conflict_cell':[2,4],'prior_read':36,'proposed':'R','forced':'L','old_tag_birth':19},'scope':'Necessary age4 F branch; only the single prescribed known renewal extension is rejected. No all-renewal exclusion, attained old-tag retirement or six-C branch result.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
