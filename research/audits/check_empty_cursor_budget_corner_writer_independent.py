from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'kernel_cycle_lift_2026-10-24';Q=R/'reframe_finite_seed_2026-10-24';p=SELF.with_name('check_cycle_birth_finite_fuel_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
ends,component,step,wvertex,graph=[ns[x]for x in('ends','component','step','wvertex','graph')]
def xy(p):return int(p.real),int(p.imag)
def ck(C):return sorted(map(xy,C))
WORDS=['RRRRL','RRRRLL','RRRRLRRL','RRRRLLRL','RRRRLLRRL','RRRRLLLLRL','RRRRLRLRRL','RRRRLRL','RRRRLRLL','RRRRLRRLL','RRRRLRLRL','RRRRLRRLRL'];rows=[]
for W in WORDS:
 p=0j;h=0;last={}
 for t,c in enumerate(W):last[p]=(c,t);h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
 F={q for q,(c,t)in last.items()if c=='R'};r=wvertex(p,h);assert not component(F,0,r)[1]
 N={r+d for d in(2+2j,2-2j,-2+2j,-2-2j)};U=set().union(*(component(F,0,n)[1]for n in N));a,b=ends(p,0);u=b if a==r else a;V={v for q in U for v in ends(q,0)}
 typ='MASS'if len(U)>2 else'SATURATED_NONFIRST'if len(U)==2 and u not in V else'OPEN'
 rows.append({'word':W,'pose':[xy(p),h],'mandatory_final':ck(F),'import_union':ck(U),'mass':len(U),'first_tip':xy(u),'tip_present':u in V,'type':typ})
assert [z['mass']for z in rows]==[3,3,5,4,5,2,2,1,1,2,1,1]
assert Counter(z['type']for z in rows)=={'MASS':5,'SATURATED_NONFIRST':2,'OPEN':5}
A=json.loads((D/'empty_cursor_import_budget_certificate.json').read_text())
for z,a in zip(rows,A['rows']):assert(z['word'],z['pose'],z['import_union'],z['type'])==(a['word'],[tuple(a['exit_pose'][0]),a['exit_pose'][1]],list(map(tuple,a['mandatory_import_union'])),a['classification'])
seed={-1+1j,-1+2j};H={-1j,1-1j,1+0j};corner={-2+1j,-2+2j};single={-1+0j};nextcorner={-2+4j,-2+5j};controls=[]
for name,B in[('minimal',seed),('prepaid',seed|nextcorner),('remote',seed|{100+100j})]:
 B=set(B);p=0j;h=0;trace=[];word='';firstfail=None
 for t in range(20):
  _,C=component(B,0,wvertex(p,h));mass=len(C)
  if t>10 and mass>6 and firstfail is None:firstfail=t
  trace.append({'cut':t,'head':xy(p),'h':h,'active_w':ck(C),'active_z':ck(component(B,2,2*p+(-1-1j)*(-1j)**h)[1]),'field':ck(B)})
  if t==10:
   extra=nextcorner if name=='prepaid'else{100+100j}if name=='remote'else set()
   assert B==H|corner|single|extra and(p,h)==(-1+3j,0)and not C
   assert component(B,0,ends(next(iter(corner)),0)[0])[1]==corner
   assert component(B,0,ends(-1+0j,0)[0])[1]==single
   assert component(B,0,1-1j)[1]==H
  p,h,c=step(B,p,h);word+=c
 assert word[:10]=='RRRRLRLRRL'and max(len(z['active_w'])for z in trace[:11])==6
 assert firstfail==(14 if name=='prepaid'else 17)
 controls.append({'name':name,'first_cap6_failure':firstfail,'word20':word,'trace':trace})
for a,b in zip(controls[0]['trace'][:11],controls[1]['trace'][:11]):
 assert(a['head'],a['h'],a['active_w'])==(b['head'],b['h'],b['active_w'])and set(map(tuple,b['field']))==set(map(tuple,a['field']))|set(map(xy,nextcorner))
for C0 in[seed,corner]:
 g=graph(C0,0);assert sorted(map(len,g.values()))==[1,1,2]
assert corner=={q-1 for q in seed}
files=['EMPTY_CURSOR_IMPORT_BUDGET_TRAPS.md','check_empty_cursor_import_budget.py','empty_cursor_import_budget_certificate.json','check_corner_writer_port_trap.py','corner_writer_port_trap_certificate.json'];hs={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files};mf=json.loads((Q/'corner_writer_manifest.json').read_text())
for f,h in mf.items():assert hashlib.sha256((Q/f).read_bytes()).hexdigest()==h
out={'status':'PASS general empty-cursor import-budget trap and actual cap6 corner writer obstruction','global_author_hashes':hs,'corner_writer_manifest':mf,'all12_exact_word_geometries':rows,'complete_finite_board_controls':controls,'analytic':['Empty activew means all four incident edgecells are WHITE. Their four successive distinct reads are thereforeR regardless of remote fields, withwstationary. The complete active graph after4R is exactly the4new arms plus the union of ALL old complete components touching the4tips, counted once. No passive-passive connection or cancellation can occur silently.','For any specified oldBLACK subsetF, its components meeting thetips are an actual edge-subsetU_F of that full importunion. If its cardinality>M-4, a capM failure occurs by4R. If equal and the firsttip has no incidentU_F edge, absence of earlier failure forces equalityU_actual=U_F. The firstarm is then a leaf even if otherarms createcycles. The followingL crosses to isolatedfirsttip, leaving a COMPLETE (M-1)-edge archive consisting of other3arms+U_F.','The next isolated-root4R sweep must touch theoldcenter and import that entire archive; its four new edges are disjoint because the newrootwasempty. Thus cap failure occurs within4+1+4=9updates. Completeness follows from already including every oldcomponent touchingthefirststar; any unlisted edge attached to thearchive would already belong tothatunion. This proof is uniformM>=4 and arbitrary unreadexterior, not an extrapolated simulation.','For each of the12 suppliedwords, mandatory finalBLACK cells are exactly those with lastR. Fresh fixed-lattice neighbor-component reconstruction gives7traps and5unresolvedwords with the displayedmasses. The table certifies each listedclass conditionally on actual empty-to-empty execution; this audit does NOT certify completeness of the12-word cap6 grammar.','Actual2cellcorner writer RRRRLRLRRL reaches head(-1,3),N with emptyactive, cap6, completeoutput sameorientedcorner shiftedwest plus singleton plus3star. Any nonnegative additive componenttype potential nonincreasing at EVERY cap6return must therefore give bothsingletonandstarweight0. This is one exact physicalresourceidentity, not an arbitrarytypedrank impossibility.','Its mandatory outputcorner alone saturates the2edge oldbudget awayfromfirsttip, so EVERY actual realization of this returnword must leavecap6 within9furtherupdates, irrespective routing choice. Minimal and remote-cell controls firstfailcut17; a fullyprefunded identicalnextcorner leavesfirstwordunchanged but importsoldoutputcorner onnextfourthR, active8atcut14. Completefieldsandbothfixedgraphrolesare retained.'],'scope':'No cap6 global exit theorem, compiler, infinite growth or capture. Five supplied wordclasses remain unresolved. Componenttype rank obstruction is limited to universal nonincrease with nonnegative passiveweights.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
