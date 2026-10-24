from pathlib import Path
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
note=R/'kernel_cycle_lift_2026-10-24/REMOTE_HELP_CHRONOLOGY_NOT_FUEL.md'
assert sha(note)=='9869d3733a9cb221b0063a86491424e1e690855922630cf16dcf83f64c5ff3a7'
deps={'kernel_cycle_lift_2026-10-24/FINITE_SOURCE_OLD_REMOTE_HELP.md':'a858ddf0a392e5242dbee99e5882db3a0e7a1ea6f65095faf85807953c19711b','audits/check_finite_source_old_remote_help_independent.json':'3548a29a9e80a7359b32fdff75bd12688d1a71778f7841a970b30e27f8af1d44','active_w_archive_itinerary_2026-10-23/ACTIVE_EPISODES.md':'ad3cb9f07e078bcbaaa02622004f56254b211de2ed238fa2bd031e7d5e3d5721'}
for p,h in deps.items():assert sha(R/p)==h
out={'status':'PASS chronological dependency only, not fuel or an age rank','author_note':sha(note),'dependencies':deps,'analytic_review':[
'An old helper at distance strictly greater than4M from departure head cannot be active at cutd or cutd-1: signed fixed-edge metric gives distance at mostM atd andM+1 atd-1. M>=1 givesM+1<=2M<4M. It is black atd-1 because the sole update d-1 reads a local cell, not the helper.',
'The marked lifetime remains black until its consuming readc. It is local withinM+1, whereas remote helper y is distinct. A helper consumption j provided in[d,c] therefore actually lies in[d,c). No rebirth is silently substituted.',
'If helper has ever been active befored, there is a last actual active-to-dormant transition s<=d. Since it is dormant at bothd-1 andd, this transition has s<d. Signed gate law identifies the transition as bridge-L deletion leaving the surviving helper on the departed side. Its lifetime has no read on[s,j), so this is a valid completed marked episode even with later unproductive reattachments.',
'If it has never been active, it is an initial dormant black lifetime. An R-born lifetime is active immediately after its birth, so cannot be such a root. Initially active lifetimes that later became dormant belong to the transition case, not the root case.',
'Every existing arrow has interleaving intervals s<d<=j<c. This decreases two nonnegative integer indices, not containment, LIFO order, duration, birth age, or component mass. Thus backward chains are finite but a DAG can share a helper among multiple long parent episodes.',
'The parent cap only applies fromd-1. Recursing to an older s requires a cap on[s-1,j]; sustained-tail bounds need a separate finite-prefix boundary for earlier s. A short helper episode need not crossF(M), so is not required to have a further helper.',
'No finite fuel, bounded branching, fixed initial-mass charge, effective F, or eventual-translation/standard-capture conclusion follows. Infinite forward creation of short helpers is not excluded by this well-founded backward chronology.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
