# Prepared80 has complete active-w peak eleven

24 October 2026. Author exact full-field result, independent audit pending.
This is a prepared travelling wave. Its infinite input is not removed.

## Full field, not a frontier crop

Use the already independently confirmed prepared80 field and incoming N at
(0,0). With d=(4,4), cap C and input/output sets A,O from b71779cc, the exact
bi-infinite cut field is

    B0 = C union union_{k>=0}(A+k*d) union union_{k<0}(O+k*d).

Membership in this infinite set is evaluated by full-drift residue and integer
halfline inequalities. Every unread old output and future input is retained.
The phase field is B0 XOR the literal reads before that phase.

For incoming vector v at cell p, the active C-face is represented at doubled
coordinates 2p+right(v)-v. A BLACK cell(x,y) joins the two C-faces

    (2x-1,2y+1) to(2x+1,2y-1), when x+y is even;
    (2x-1,2y-1) to(2x+1,2y+1), when x+y is odd.

These are the fixed invariant-sector w edges. At every phase0 through80,
a complete BFS checks all four incident physical cells at every discovered
vertex against the exact infinite membership predicate. Every BFS closes,
and the certificate lists every resulting vertex and BLACK edge. No cropped
window or assumed mass cap supplies completeness.

## Exact result

The complete active mass is at most11 at every phase, with unique maximum11
at phase70. That maximum component has the following11 BLACK cells:

    (1,-1),(2,-1),(2,0),(2,1),(3,-1),(3,0),
    (3,1),(4,0),(4,1),(4,2),(4,3).

The exact phase0 root is empty. But the component containing the next input
(0,1) is NOT an isolated input edge: it has six edges,

    (0,1),(-1,0),(-1,-1),(-1,-2),(-1,-3),(0,-4).

These consist of the future input, the two cap edges, and THREE unread old
permanent-output edges. The other current input(3,2) is isolated at this cut.
Omitting the old field would misstate the first imported component.

## All-N finite controls

For every N>=1, the exact finite seed C plus the firstN copies of A realizes
N periods, as independently proved for the falsifier. At every time up to80N,
its BLACK field is a subset of the corresponding infinite preparation: the
missing old outputs and later inputs are unread during that finite trace.
Its complete active component therefore has size at most11.

The N1 finite control already has exactly the displayed11-edge component at
phase70. Every larger-N initial field contains that control's initial field
and has identical reads through that phase. Thus the exact maximum on EACH
first80N interval is11, not just an upper bound. The executable separately
replays all81 complete N1 fields and their full finite components.

This proves arbitrarily long prepared80 finite-seed intervals with complete
active cap11, while the required seed size is2+2N. It does not give an infinite
cap11 orbit from one finite seed. After finite fuel, the supplied repeated word
fails at80N+15; later dynamics are not classified here.

## Meaning for winding arguments

Prepared80's S3 does not require an unbounded active component, an omitted
archive, or an owned lifetime of age at least one period. Its excess winding
coexists with exact peak11 and all owned ages<=56<P80. This refutes those
proposed explanations for the prepared falsifier; it does not refute a
complete-WHITE-only winding theorem or establish any universal cap threshold.

certify_prepared80_complete_active_peak.py
SHA256 550ea23087bea129b7c318a31e4ba43bb25550ec1273f47d7fc5e862b5e5941e
prepared80_complete_active_peak_certificate.json
SHA256 882cb95a4851838c5e372b607ea72433949d29e2d8ff936dec07b07f7c2da4bd
