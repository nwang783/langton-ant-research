from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'reframe_finite_seed_2026-10-24';p=SELF.with_name('check_cycle_birth_finite_fuel_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
component,wvertex=ns['component'],ns['wvertex'];xy=lambda z:(int(z.real),int(z.imag));digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
src=R/'standard_unread_cap_2026-10-23/standard_w_frontier_certificate.json';assert digest(src)=='6c3294eede67916be8c7171e73683cf5009c9fe3846ed0bfb61580181186413a';A=json.loads(src.read_text());ref=json.loads((D/'exact_standard_active_peak.json').read_text());rows=[]
for i,a in enumerate(A['phases']):
 assert a['phase']==i;p=complex(*a['pose'][0]);h=a['pose'][1];v=wvertex(p,h);assert xy(v)==tuple(a['w_cursor']);sector=int(v.real+v.imag)%4;assert sector==2
 B={complex(*q)for q in a['black_frontier']};C=component(B,sector,v)[1];b=ref['phases'][i];assert len(C)==b['complete_active_w_mass'] and sorted(map(xy,C))==list(map(tuple,b['complete_active_component']))
 rows.append({'phase':i,'mass':len(C),'field_mass':len(B),'active':sorted(map(xy,C))})
assert max(z['mass']for z in rows)==42 and[z['phase']for z in rows if z['mass']==42]==[64] and rows[64]['field_mass']==42
manifest=D/'cap7_exit_manifest.json';M=json.loads(manifest.read_text())
for f,h in M['files'].items():assert digest(R/f)==h,(f,digest(R/f),h)
reports=['check_cap7_structure_independent','check_cap7_word_mandatory_filters_independent','check_cap7_exact_word_pairs_independent','check_ST_saturated_port_fuel_independent']
reporthashes={s:digest(SELF.with_name(s+'.json'))for s in reports}
assert reporthashes==dict(zip(reports,['784e4f05cf3475088e92cca5f5c757b8b875335a7488d6ca0ff21acfff042b39','c4d736618bbfaca523fa08bd3bd241bbef76391a0783aefcbf6d0caacacea23f','355653a0fd7fd19d814bc668e9d37d098a4c4bb32f7aa35e8304c6ce0bb3f723','1a7dd41b25073f41bb071083f5952ad5188677aa3c5bcbf07d6d4b4b7806ac44']))
files={f:digest(D/f)for f in('CAP_SEVEN_EXIT_ASSEMBLY.md','cap7_exit_manifest.json','EXACT_STANDARD_ACTIVE_PEAK.md','exact_standard_active_peak.py','exact_standard_active_peak.json')}
assert files['CAP_SEVEN_EXIT_ASSEMBLY.md']=='56fc9eb06bfaf1b6f5271670a90e55773513de1893b8f5d91cca340331e60ac0'
assert files['EXACT_STANDARD_ACTIVE_PEAK.md']=='7fb8cff1af7f973eebc30362b6db01e68cc3d7eb318a1d45fc6b9deffac76074'
out={'status':'PASS cap7 exit assembly and separate exact standard active peak','files':files,'assembly_manifest_files':M['files'],'independent_dependencies':reporthashes,'standard_source_sha256':digest(src),'standard_active_mass_sequence':[z['mass']for z in rows],'all104_complete_components':rows,'analytic_review':[
'The cap7 assembly invokes only independently signed exact necessary reductions and universal S/T fuel, with every immutable dependency hash matched. Finite-support fields remain finite at the tail cut. Infinite capped trajectories have repeated empty cuts, finite-word graph paths eventually stay in a recurrent SCC, U-only needs infinitely many distinct run-entry black cells, and arbitrary S/T mixtures spend a finite nonnegative complete-component count. Thus sustained cap7 is impossible, equivalently every finite-support orbit has infinitely many cuts of active-w mass at least8.',
'This is a finite small-cap exclusion, NOT unbounded component size, a quantitative global escape time, eventual translation, standard104 capture, or a statement about infinite prepared backgrounds. No 154-million-profile list is used.',
'The separate exact-peak extraction uses the entire signed phase-frontier fields, not the earlier upper bound. Fresh BFS in the correct fixed w sector (author0, auditor2) finds maximum42 uniquely at phase64, where all42 frontier edges are active. The signed all-offset archive separation and finite original-archive clearance identify this component with the COMPLETE actual board component after its board-dependent threshold. Every already-standard finite-support tail therefore has exact peak42 per period after clearance. No bound before clearance or attraction follows.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('standard peak42 unique phase64; cap7 assembly56fc9eb0')
