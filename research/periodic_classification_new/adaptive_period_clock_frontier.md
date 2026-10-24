# Finite adaptive period lower bounds in physical-clock frontiers

23 October 2026, 07:12 UTC. Proposed safe strengthening of the independently
signed normalized-real frontier; implementation/certificates pending review.

Fix a proved period lower bound N0 and an integer scale/counter cap S>=N0.
Use physical representative clocks X=S*t/P throughout the entire scan.
After exposing a new complete row, let T be the total number of read events
in all exposed rows, and retain only the saturated count Tcap=min(T,S).
Every actual front necessarily has P>=max(N0,Tcap), since each exposed
read is one distinct full-drift event class in its whole period.

For this transition put L=max(N0,Tcap) and U=ceil(S/L). A physical seam-k
successor obeys the necessary strict real difference bounds

    -S*k < X_v-X_u <= U-S*k.                    (1)

Indeed its exact increment is -S*k+S/P, with0<S/P<=S/L<=U.
The scale S never changes, so no coordinate reanchoring or rescaling of old
matrices occurs. Earlier constraints may have larger U; retaining them
without retrospective tightening only weakens the model. Retired variables
are projected and clipped exactly as in the signed real-clock abstraction.

The extra state Tcap has only S+1 possible values. All histories, endpoint
pairings, voltage residues and clipped strict DBM entries remain finite.
Thus complete graph exhaustion without a possible-front outcome is still
an all-width, all-period exclusion, not a cutoff at S: periods below S
are represented before saturation and arbitrarily large periods after it.
No actual front can be discarded just because the lower bound grows.

For actual axis-four drift use the signed N0=16. The first exploratory
cap-five run takes S=64,M=128,q=2, and a literal two-row proper-path filter.
The latter uses the signed path/rank winding necessity, not an additional
period cutoff. Producer:`probe_axis4_adaptive_real_zone.py`.
Core:`probe_adaptive_real_zone_core.py`.

No new cap-five exclusion is claimed from this note. Resource limits are
UNKNOWN. The shared increment S/P, phase distinctness and cyclic block
order are still relaxed, so a retained terminal remains only a candidate.
