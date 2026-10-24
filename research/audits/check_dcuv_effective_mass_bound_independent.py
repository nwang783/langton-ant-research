"""Dependency and literal arithmetic check; no mass-tree enumeration is run."""
from pathlib import Path
import json,hashlib,runpy
R=Path(__file__).resolve().parent.parent
D=R/'word_stabilization/dcuv_raw_bridge_effective_frozen_20261023_2100'
m=json.loads((D/'manifest.json').read_text())
for f,h in m['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h,f
for f,h in m['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h,f
# Reuse only the separately implemented auditor's literal walk and graph checks.
a=runpy.run_path(str(R/'audits/check_finite_support_DCUV_closure_assembly_independent.py'))
q=a['q'];words=[r['word']for r in q['macro_words']]
foreign=[dict(index=i,length=len(words[i]),net_black=words[i].count('R')-words[i].count('L'))for i in range(4,7)]
assert [r['length']for r in foreign]==[56,64,74]
assert max(r['net_black']for r in foreign)<=6
assert all(a['literal'](w)['feasible']for w in words)
all8manifest=R/'causal_archive_frontier_2026-10-23/finite_support_complete8_exclusion_manifest.json'
assert hashlib.sha256(all8manifest.read_bytes()).hexdigest()=='da766cab53d45efb5ea75167b176ad851ce3c85212ce9a544d75dcb474a47c93'
out=dict(status='PASS independent raw lift, computable restricted mass-only lifetime and foreign-count recurrence',note_sha256=hashlib.sha256((D/'dcuv_mass_only_effective_lifetime_and_graph_bridge.md').read_bytes()).hexdigest(),author_manifest_sha256=hashlib.sha256((D/'manifest.json').read_bytes()).hexdigest(),all8_manifest_sha256=hashlib.sha256(all8manifest.read_bytes()).hexdigest(),foreign=foreign,analytically_checked=['Macro-prefix tree is decidable, prefix-closed and finitely branching.','An infinite branch with first-L budget m has a single finite union black seed of size at most m; no far-coordinate cropping.','Raw DCUV termination therefore makes the whole tree finite, so exhaustive traversal defines total monotone L(m).','a_(i+1)=a_i+L(a_i)+6 bounds actual masses across a raw block and one foreign macro.','G(m,k)=74*k+sum L(a_i) is total and bounds complete raw duration, not foreign-event count.'],numerical_mass_tree_evaluated=False,scope='Restricted literal DCUV and conditional seven-word factors only; not a global mass-only defect budget or capture theorem.')
(R/'audits/check_dcuv_effective_mass_bound_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
