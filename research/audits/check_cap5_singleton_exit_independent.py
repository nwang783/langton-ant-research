from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();p=SELF.with_name('check_cap4_exit_cap5_grammar_independent.py');ns={'__file__':str(SELF)};exec(p.read_text().split('# Empty start physical chronology')[0],ns)
D,T,paths,expected,ends,component,step,wvertex,key,xy=[ns[x]for x in('D','T','paths','expected','ends','component','step','wvertex','key','xy')];lattice=0
cert=json.loads((D/'kernel_M5_scc.json').read_text());records=[];zero=[]
for i,r in enumerate(cert['first_return_cycles']):
 P=tuple(expected(z)for z in r['transitions']);assert P in [tuple(T[z]for z in path)for path in paths]
 ins=[len(t[4])for t in P if t[4]];outs=[len(t[6])for t in P if t[6]];drop=ins.count(1)-outs.count(1);assert drop>=0
 records.append({'index':i,'word':r['word'],'imports_sizes':ins,'emission_sizes':outs,'singleton_drop':drop})
 if not drop:zero.append(i)
assert zero==[0,11]and sum(z['singleton_drop']>0 for z in records)==108
# Independent complete-board replay of the two sole zero-drop paths, retaining exact full components and actual moving cursor.
macros=[]
for name,B,word in [('A',set(),'RRRRL'),('B',{-1+1j},'RRRRLRL')]:
 p=0j;h=0;trace=[];wseq=[wvertex(p,h)];imports=[];emits=[]
 for t,ch in enumerate(word):
  w=wvertex(p,h);_,C=component(B,lattice,w);old=set(B)
  if p not in B:
   a,b=ends(p,lattice);v=b if a==w else a;Z=component(B,lattice,v)[1]
   if Z and Z!=C:imports.append(key(Z))
  p,h,c=step(B,p,h);assert c==ch
  wn=wvertex(p,h);_,N=component(B,lattice,wn)
  if c=='L':
   E=old-{next(q for q in old if q not in B)}-N
   # Only the old active component may emit: unrelated passive components are not counted.
   E=C-{next(q for q in old if q not in B)}-N
   if E:emits.append(key(E))
  if wn!=wseq[-1]:wseq.append(wn)
  trace.append({'tick':t,'turn':c,'head_after':xy(p),'heading':h,'w_after':xy(wn),'active_size':len(N),'board_after':key(B)})
 assert h==3 and not component(B,lattice,wvertex(p,h))[1]
 assert wseq==([1-1j,-1+1j]if name=='A'else[1-1j,-1+1j,-3+3j])
 assert key({0-1j,1-1j,1+0j})in emits
 assert sorted(map(len,imports))==([]if name=='A'else[1])
 assert sorted(map(len,emits))==([3]if name=='A'else[1,3])
 macros.append({'name':name,'word':word,'w_sequence':list(map(xy,wseq)),'imports':imports,'emissions':emits,'trace':trace})
# Enumerate every binary choice from scratch at each depth; prohibit only past starts, never past middle vertices.
levels=[]
for n in range(1,10):
 words=[]
 for ds in product((1,2),repeat=n):
  p=0j;starts=set();ok=True
  for i,s in enumerate(ds):
   starts.add(p);v=1j**i
   if any(p+k*v in starts for k in range(1,s+1)):ok=False;break
   p+=s*v
  if ok:words.append(''.join(map(str,ds)))
 levels.append(words)
assert list(map(len,levels))==[2,4,8,10,12,10,8,4,0]
author=json.loads((D/'singleton_return_certificate.json').read_text())
assert [z['stride_words']for z in author['geometric_survivors']]==levels
assert [z['singleton_drop']for z in author['component_counts']]==[z['singleton_drop']for z in records]
mf=json.loads((D/'singleton_manifest.json').read_text())
for f,h in mf.items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS finite-complete-support cap-five exit','dependencies':mf,'grammar_audit_sha256':hashlib.sha256(SELF.with_name('check_cap4_exit_cap5_grammar_independent.json').read_bytes()).hexdigest(),'all110_singleton_ledgers':records,'zero_drop_paths':zero,'actual_complete_macros':macros,'all_binary_geometric_survivors':levels,'analytic':['At empty-active cuts every black w edge is in a complete passive component. An R step either joins an already active vertex, or imports exactly the complete other component. An L step can detach at most one complete component. No passive-passive merge or edge deletion happens without an actual active interaction. Thus the exact singleton component count changes by emissions minus imports on every physically valid local-kernel first return, even when some emitted component is later imported within that return.','All110 independently reconstructed first-return paths have nonpositive singleton change; only A(index0) and B(index11) have zero. Both actual paths and complete full boards were independently replayed. A emits3star, B imports1 and emits1+3star. The two stars are identical in the starting frame; the w cursor moves one or two collinear diagonal-grid edges, with the same counterclockwise quarter-turn of physical heading.','Throughout any consecutive A/B run, a produced3star remains a complete passive component. Neither path ever imports a component of size>=3. No other operation can touch or change that star while keeping it passive; if an attachment occurs it is a forbidden import and exits the two-path run. A later macro segment therefore cannot reach its root: every newly reached w vertex has active mass0 or1, but that unchanged root carries3edges. This forbids only earlier macro starts and allows all old B middle-vertex crossings.','Independent exhaustive binary choices through depth9 give counts2,4,8,10,12,10,8,4,0. The geometry is a necessary relaxation, so no physical run of9 zero-drop returns exists. No finite sampling of initial boards or assumed segment self-avoidance is used.','If a finite-support orbit were eventually capped at5, the finite kernel with nonempty DAG forces infinitely many empty cuts. Its finite nonnegative singleton count can drop strictly only finitely often, eventually leaving only A/B, contradiction. Therefore every finite-support orbit has infinitely many active-mass>=6 cuts. From an empty cut with S singleton components, at most9S+8 complete returns are possible before exit or a final cap-preserving suffix; the nonempty DAG bounds that suffix.'],'scope':'An exact small-active-cap exclusion for complete finite support. No standard104 attraction, uniform global component bound, or finite-state reduction across arbitrary imports. Infinite backgrounds can have infinite singleton fuel and are not covered.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('zero',zero,'counts',list(map(len,levels)))
