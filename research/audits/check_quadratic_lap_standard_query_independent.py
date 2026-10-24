from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ns={'__file__':str(SELF.parent/'check_quadratic_lap_validator_independent.py')};exec((SELF.parent/'check_quadratic_lap_validator_independent.py').read_text().split('std=json.loads')[0],ns)
globals().update({k:ns[k]for k in('ROOT','D','ctx','normalized','union','isbounded','Object','_bind','_P')})
std=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());ref=json.loads((D/'quadratic_lap_standard_query.json').read_text());by={r['name']:r for r in ref['records']}
programs=[('standard104_grouped',[(std['word'],1,1)],std['heading']),('infinite_prepared_axial_rail',[('LRRL',1,1)],1),('punctuated_prepared_rail',[('LRRL',1,1),('RRRR',0,1)],1),('rotating_constant_stages',[('RL',1,0),('R',0,1),('RL',1,1),('RRR',0,1)],0)]
reports=[]
for name,blocks,h in programs:
 ctx.reset_operations();bs,A,B,bundled,fs=normalized(blocks,h);doms=[];ls=[]
 for f in fs:
  ds=ctx.set('{[n,b,j,r]:'+f'n>=0 and b={f["block"]} and r={f["phase"]} and 0<=j<{f["a"]}*n+{f["z"]}'+'}');doms.append(ds)
  if f['t']=='L':ls.append(ds)
 domain=union(doms);L=union(ls);R=domain.subtract(L)
 def diag(s):return Object(ctx,'map',_bind('isl_map_intersect_domain',[_P,_P])(ctx.map('{[n,b,j,r]->[n,b,j,r]}')._copy(),s._copy()))
 after=ctx.map('{[n,b,j,r]->[m,c,k,s]:m>n or(m=n and c>b)or(m=n and c=b and k>j)or(m=n and c=b and k=j and s>r)}')
 # Independent successor: globally least actual later event, rather than hand-coded joins.
 S=diag(domain).apply_range(after).apply_range(diag(domain)).lexmin().coalesce();T=S
 for _ in range(103):T=T.apply_range(S).coalesce()
 mismatch=diag(L).apply_range(T).apply_range(diag(R)).union(diag(R).apply_range(T).apply_range(diag(L))).domain().coalesce();finite=isbounded(mismatch.ptr);assert finite>=0
 actual=[]
 for n in range(6):
  for b,(w,a,z)in enumerate(bs):
   for j in range(a*n+z):
    for r,t in enumerate(w):actual.append(((n,b,j,r),t))
 pairs=';'.join('['+','.join(map(str,e))+']->['+','.join(map(str,f))+']'for(e,t),(f,u)in zip(actual,actual[1:]));finiteS=ctx.map('{'+pairs+'}');last=actual[-1][0];cut=ctx.map('{[n,b,j,r]->[m,c,k,s]:0<=n<6 and0<=m<6}'.replace('and0','and 0'));assert S.intersect(cut).is_equal(finiteS)
 if name in by:
  rr=by[name];assert mismatch.is_equal(ctx.set(rr['mismatch_relation']))and bool(finite)==rr['mismatch_finite']
  if finite:
   assert mismatch.is_empty();w=''.join(t for e,t in actual[:104]);phases=[i for i in range(104)if w==std['word'][i:]+std['word'][:i]];assert phases==rr['canonical_phases']and bool(phases)==rr['standard104']
 reports.append(dict(name=name,mismatch_finite=bool(finite),mismatch_relation=str(mismatch),literal_six_lap_successor_checks=len(actual)-1));print(name,'PASS',flush=True)
out=dict(status='PASS independent exact104 successor suffix query',source_sha256=hashlib.sha256((D/'quadratic_lap_standard_query.py').read_bytes()).hexdigest(),records=reports,analytic='Globally least later actual event independently reconstructs the complete successor across copies, zero-count stages and laps. 104 sequential compositions match all three saved mismatch sets; finite mismatch criterion must additionally inspect the canonical cyclic word, so pure LRRL is not mislabeled standard. For a nonempty finite mismatch set, starting a lap after its maximum n is safely beyond all mismatches. This decision concerns actual finite-seed paths only after exact geometry, alternation and finite FirstL have passed.',scope='Fixed standard104 target, not arbitrary unknown period or a new nonstandard finite-seed construction.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
