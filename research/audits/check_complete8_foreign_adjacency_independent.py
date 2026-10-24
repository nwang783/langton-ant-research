from pathlib import Path
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23'
ns={'__file__':str(R/'audits/check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns)
W,M,walk,xy,dirs=(ns[k]for k in('W','M','walk','xy','dirs'));a=json.loads((D/'complete8_foreign_adjacency.json').read_text());rows=[]
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];names=['D','DC','V','VC','VCC','U','UC','UCC']
for name,i in zip(names,[0,1,4,5,6,7,8,9]):assert ''.join(W[c]for c in name)==G[i]['word']
for ref in a['rows']:
 source=ref['source'];f=ref['foreign'];sw=''.join(W[c]for c in source);word=sw+W[f]+M;tr=walk(word)
 if not tr['feasible']:
  tick=tr['i'];q=tr['q'];phase=tick-len(sw);assert 0<=phase<len(W[f]);r=ref['conflict'];assert(tick,phase,xy(q),word[tick])==(r['global_tick'],r['foreign_phase'],tuple(r['cell']),r['proposed_turn'])
  prior=walk(word[:tick]);events=[(j,ch)for j,(p,h,ch)in enumerate(prior['reads'])if p==q];assert events==list(map(tuple,r['previous_reads']))and events[-1][1]==word[tick]
  rows.append([source,f,'impossible',phase,xy(q)])
 else:
  seed={q for q,b in tr['req'].items()if b};assert seed=={complex(*q)for q in ref['prepared_seed']};B=set(seed);p=0j;h=0
  for i,ch in enumerate(word):
   if i==len(sw)+len(W[f]):assert(xy(p),h)==(tuple(ref['raw_foreign_exit']['head']),ref['raw_foreign_exit']['heading'])
   assert (p in B)==(ch=='L');B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
  rows.append([source,f,'actual finite pair',len(seed)])
assert len(rows)==24 and{(r[0],r[1])for r in rows if r[2]=='actual finite pair'}=={('V','F'),('V','Q'),('U','F'),('U','Q'),('U','B')}
assert walk(W['C']+W['F']+M)['feasible'] # Scope control: raw CF is NOT prohibited.
manifest=D/'complete8_foreign_adjacency_manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='735023bebfa154bd936e9546023367b541006ea1d9f57bb2eb7240bf040017ea'
for name,value in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==value
out={'status':'PASS all24 literal complete-eight/foreign adjacency pairs and five full-board controls','manifest_sha256':sha,'rows':rows,'analytic':['All19 contradictions lie inside foreign RAW, so neither finite nor infinite unseen support can repair them. Initial color requirements at the same physical cell disagree.','Each surviving pair is physically replayed from its exact first-L seed with the real terminal M11. This proves pair feasibility only, not arbitrary incoming history or inherited graph-class realization.','Every actual last complete-eight packet before a first foreign is one of these eight. Only plain V or plain U survives; therefore the actual immediately preceding atom is not C. Standalone raw C F remains legal and is not silently grouped as a complete-eight predecessor.'],'scope':'Local full-packet adjacency; no global seven-word coverage, postforeign permanence, proxy simplicity or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
