from pathlib import Path
import json,hashlib
P=Path(__file__);R=P.parent.parent;D=R/'two_track_UCC_F_return_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'foreign_covariance_manifest.json';assert sha(mf)=='065576a1cdcbf9de7715c57cb50a2f51f0a23efcd6ec661ddda0cc23894847f3';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
bp=P.with_name('check_two_track_plain_DVU_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('geom={}')[0],ns);W,M,K,trace,field_geom,xy,raw,g=[ns[k]for k in('W','M','K','trace','field_geom','xy','raw','g')]
ref=json.loads((D/'foreign_covariance.json').read_text());rows=[]
for A,a,b,dd,dv in [('F',4,2,0,-3),('Q',4,4,1,-4),('B',3,5,3,-5)]:
 t,ek,O=field_geom(W[A]);assert(t['p'],t['h'])==(-a-b*1j,2)and min(p.imag for p,h,c in t['reads'])==-b
 assert max(q.imag for q in K)<2
 for du in(0,1):assert dd+2*du+dv-2*du==1-a and dd+2*du+3*(dv-2*du)+4*du==-7-b
 rows.append({'foreign':A,'RAW_length':len(W[A]),'endpoint':[*xy(t['p']),t['h']],'RAW_minY':-b,'drop_X_minus_drop_Y':7+b,'hole_below_RAW_margin':2,'hole_exit_relative_Y_at_least':2})
controls=[]
for c in ref['actual_complete_finite_partial_prefix_controls']:
 A,X,Y=c['foreign'],c['S_rail'],c['N_rail'];seq='UCC'+X+A+Y;word=raw(seq);t=trace(word);assert(t['p'],t['h'])==(-2j,0);part=trace(word+W['U'][:13]);assert part['conflict']is None;B={complex(*q)for q in c['complete_initial_BLACK']};assert B=={q for q,b in part['req'].items()if b};birth=set(B);gr=[]
 for i,(q,h,z)in enumerate(part['reads']):
  assert(q in B)==(z=='L');B.symmetric_difference_update({q})
  if q==g:gr.append((i,z))
 assert gr==[(1,'L')]and g not in B and(part['p'],part['h'])==(g,3)and len(part['reads'])==c['successful_actual_reads'];bad=trace(word+W['U']+M);assert bad['conflict']==(len(word)+13,1,g,'L')
 mismatch={a:next(i for i,z in enumerate(W['U'][:13]+'R')if(W[a]+M)[i]!=z)for a in'DCVUFQB'};assert mismatch==c['all_seven_current_marker_mismatch_ticks0'];controls.append({'foreign':A,'S':X,'N':Y,'seed_mass':len(birth),'actual_reads':len(part['reads']),'g_WHITE_at_target_tick13':True})
out={'status':'PASS exact F/Q/B covariance of signed UCC plain-DVU two-track hole guard','manifest_sha256':sha(mf),'dependencies':m['dependencies'],'literal_foreign_rows':rows,'full_prefix_controls':controls,'analytic_review':['Signed6d9a85d8 already exhausts all16 actual S and N full-output roles, including entry-core deletion and residual export. These exclusions depend only on source UCC, fixed targetU0,-2N, and plain zero-C rails, not on which single foreign intervenes.','Actual F/Q/B RAW endpoints and complete read minima are reconstructed independently, not replaced by marker or corrected-center endpoints. Exact endpoint count equations yield dropX=dropY+9/11/12. The source hole is at least2 below each actual foreign RAW minimum and has N-exit relativeY=dropY+2 outside canonicalK. Thus no hidden Q/B CORE carry/export can supply it.','All four complete finite partial boards replay through target ticks0..12; target tick13/read14 is actually R on same source-deleted g. Every seven-word continuation then disagrees. No completed target, proxy contact, additional C/foreign, different connector, or postforeign maturity claim.']};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(P),sha(P.with_suffix('.json')))
