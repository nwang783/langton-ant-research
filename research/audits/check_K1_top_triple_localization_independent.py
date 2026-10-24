from pathlib import Path
import hashlib,json
SELF=Path(__file__).resolve(); R=SELF.parents[1]; D=R/'K1_pipeline_detours_2026-10-23'
s=(R/'audits/check_nonleaf_max_RIGHT_tradeoff_independent.py').read_text(); ns={'__file__':str(SELF)};exec(s[:s.index('source=next(')],ns)
rows=ns['triples'];assert len(rows)==12
assert sum(x['type']=='internal' for x in rows)==8
ends=[x for x in rows if x['type']!='internal'];assert len(ends)==4
assert all(len(x['word'])==3 and x['word'][0]==x['word'][2] for x in ends)
f=D/'K1_top_triple_paths_boundary_or_bounded_hole_v2.md'; h=hashlib.sha256(f.read_bytes()).hexdigest();assert h=='f70ef4c1b35c504d80e97d1b5544ec8817904e0f4be4e9b4600a87fd9143c6af'
deps=['check_nonleaf_max_RIGHT_tradeoff_independent.json','check_G3_contractibility_and_max_leaf_independent.json','check_exceptional_nodes_two_level_patches_independent.json','check_essential_contour_walk_localization_independent.json','check_K1_ceiling_band_low_minima_independent.json']
out={'status':'PASS top triple-use middle-node ceiling-boundary or bounded-hole localization','source_hash':h,'fresh_middle_connections':rows,'dependency_report_hashes':{p:hashlib.sha256((R/'audits'/p).read_bytes()).hexdigest() for p in deps},'analytic_review':[
'Fresh complete WHITE histories recover eight internal G3 ordinal-two L1/R2 partners and four same-R three-read endpoints. The constant sheet is M-1. A cyclic G3 component exhausts its canonical middle node; a source-sink path stays on one node without asserting consecutive actual cursor visits.',
'Under the signed essential level walk, every essential sheet c_right=M-1 node has the high ceiling band on its geometric RIGHT. Its incident C=M component remains there by the high contact barrier. Its L=M-3 plateau remains on the LEFT by the low barrier. This applies to either essential winding sign and the final outer boundary.',
'A contractible middle node containing a G3 path has a max-RIGHT endpoint, so is CCW. The whole adjacent L plateau remains in its physically bounded LEFT disk. That disk cannot contain or cross any essential curve. Its adjacent max-C sector connects it to the same complementary ceiling band without crossing another canonical half-level. Distinct same-sheet CCW disks are disjoint, so a shared low plateau forces the same middle node, not distinct nodes.',
'For an essential low minimum in a ceiling band, the essential-middle alternative would put it in the neighboring non-ceiling band. It cannot reach a DIFFERENT ceiling band either: the whole L<=M-3 contact component cannot cross ANY sheet-c_right ceiling boundary. The contractible alternative is physically bounded. Thus no top G3 edge or top same-R endpoint touches that essential minimum.',
'The separately signed low-minimum odd-root theorem and top-root classification then imply NON-TOP payment for such an essential minimum. No new root-count injectivity, original fuel or per-renewal charge is inferred.',
'A valley L plateau may touch two distinct G3 paths on its neighboring ceiling boundaries while those paths preserve different C-max components. This escape is retained. The prepared W20 staircase is not promoted to a complete WHITE-front realization.'
], 'scope':'Complete WHITE cap-four K1 actual full-drift translating front, with required positive output. Structural localization only; no exclusion of essential boundary paths or cross-band L-stock chronology.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
