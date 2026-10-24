from pathlib import Path
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
note=R/'kernel_cycle_lift_2026-10-24/RADIUS_PARAMETRIZED_HELPER_ROUTE.md';assert sha(note)=='9ae256db9411c91c95d5a40f59f1eb68ddf9f557150e9fcac5d2e05052abddd6'
deps={'audits/check_finite_source_old_remote_help_independent.json':'3548a29a9e80a7359b32fdff75bd12688d1a71778f7841a970b30e27f8af1d44','audits/check_remote_help_chronology_independent.json':'1c1b2052e9e9f30c95d5933cbb85bc39d0166a681636739e546e55ce078ed2ed'}
for p,h in deps.items():assert sha(R/p)==h
out={'status':'PASS existence-only far actual helper and route lower bounds','author_note':sha(note),'dependencies':deps,'analytic_review':[
'For each integerR, finite complete-board ensemble defines a finite maximum of FINITE marked first-read timesG(R); F(M)=G(4M). Erasing only unread initial-cut cells outsideR>=4M retains the entire marked component and exact first marked read. OriginalR,M retained, no effective horizon inference.',
'For an R-born helper with birthb<d and consumptionj>=d at the SAME physical celly, the actual head route y atb to p_d atd to y atj gives d-b>=L and j-d>=L, hence j-b>=2L. No cap befored is needed for this inequality.',
'Let s be its LAST active-to-dormant transition at or befored. Its first reactivationa afters MUST exceed d: any earlier reactivation followed by dormancy atd would require a later departure<=d, contradicting maximality ofs. Therefore s<d<a<=j, even if later unproductive reattachments followa.',
'With capM at s-1, departurehead distance to helper is at mostM+1. Cap at actual activationa is already in[d,c], and gives distance at mostM. Triangle inequalities yield d-s>=L-M-1, a-d>=L-M, completed dormantgap a-s>=2L-2M-1. The exact consuminghead gives j-d>=L and j-s>=2L-M-1.',
'In ONE fixed finite-seed trajectory with commonM and unbounded completed markedlags, increasingR permits choosing lag>G(R). A fixed helper consumption j has L<=j-d<=j, so unbounded distances force infinitely many distinct consuming events. Only finitely many initiallyblack or bounded-time-born lifetimes exist, each consumed at mostonce; removing those leaves arbitrarily late-born R helpers, whose ages>=2L diverge.',
'Under a sustainedM tail, only finitely many helper lifetimes can have departure s before the tail, so discard that finite prefix cohort. Remaining helpers meet the departuremetric and have unbounded completed dormantgaps. The statement is conditional on commoncap and unbounded parentlags, not proof they occur.',
'Fixed4M helper and farR helper need not be the same event. No effective lag-to-radius rate, injection of parents to helpers, decreasing archive resource, finite fuel or capture theorem is claimed.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
