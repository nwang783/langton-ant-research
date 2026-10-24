# Independent audit of the fresh-A cap-shift inequality

21 October 2026. This note checks the mathematical proof in
`../global/fresh_a_cap_shift_inequality.md`. It is an internal review, not a
proof of global highway capture.

## Result checked

For a completed capped segment with A initially white, arbitrary other
initial colors, and the heading sector fixed in the cited proof,

    7 Delta_A - 4 Delta_B + Delta_C <= 8M - L_C.

Here L_C is the number of black lower C corners. The proof has no period or
time bound. I found no gap after independently deriving the run accounting
and replaying the endpoint and sponsor arguments below.

## Run accounting

The C row splits into upper runs and black lower corners. Every upper run
starts and ends at white C events; all its interior C events are black.
If P counts its short right moves, R its long left moves, D their total
left displacement, z its zero-displacement first returns, and M its top
visits, then the number of C events is P+R+z+1. Its change in black C count
is therefore 3-P-R-z.

Each nontrivial excursion with k left edges and j top diamonds has
Delta_A=2j-k-1 and Delta_B=k-2+j. A short has Delta_B=1.
Combining these exact counts gives

    S_run = 3+2M-5P-11D,

where S is the negative of the proposed nonnegative cap change. A black
lower C corner contributes -1 to S, so these events help the claimed bound.

## Endpoint roofs

A zero-displacement excursion is a first return to its physical C cell.
Its endpoint colors are opposite. It must therefore be first or last in
its upper run, and there are at most two such excursions.

For a first zero excursion z_ab, direct replay leaves

    (B_s,A_s,B_(s-1)) = (a,b,0).

If a=0, the following excursion is short. If a=1,b=0, the next path visits
the already used T_(s+1), which would leave the cap. If a=b=1, the next
excursion contains an extra white B upper corner and is long; it cannot
have a right roof. Thus an initial zero excursion's second roof uses a
roof slot that is absent on the following long excursion.

For a final zero excursion with two roofs, the previous excursion cannot
be short: that short would leave its shared B cell black, while the final
zero's left roof requires that B event to be white. Its predecessor is
therefore long. That long cannot have a left roof, since it would use the
same top cell as the final zero's left roof. This uses a second, distinct
roof slot if a single long meets both endpoint zeros.

Hence M<=2R+2<=2D+2. For D>=1 this implies S_run+2P<=0. For D=0, M<=2;
the only possible positive run has P=1,M=2 and S_run=2. It has the form
z_01 at C_(s-1), short through B_s, z_10 at C_s.

## The earlier-short charge

In a positive run, T_s and T_(s+2) have not been visited before the run.
A_s starts the run black. Since it started the entire segment white,
its one prior white event was its departure to T_(s+1). It cannot have
had a black event afterward: no second white event is available until
the positive run visits T_s. Thus A_s stays black throughout this interval.

The middle top visit has read A_(s+1) white and left it black. That cell is
white again at the positive run's start. Its other white port is still
unused, so exactly one intervening black lower A_(s+1) event erased it.
The next B_s read must be black. If it were white, it would turn N and
erase A_s too early. Consequently that B event leaves B_s white.

The positive run requires B_s black. The first B_s visit after this erasure
and before the run is therefore white. An incoming W would again erase
A_s, so that visit has incoming E and outgoing S. It is a short upper
excursion. This proves the required sponsor exists in actual chronology.

Different positive runs have different indices s, because each uses T_s
and T_(s+2). Their sponsor shorts lie on different B_s cells. The charge is
therefore injective. It does not assume that the sponsors occur in the
immediately preceding run.

## Capacity check

A long-containing run can pay 2 for every one of its P shorts by the
already proved S_run+2P<=0.

In a run with D=0, every endpoint roof forbids its adjacent endpoint short
from being a sponsor: otherwise the future positive run would need to
visit the same outer top cell again. If P>=2, the endpoint shorts are
different and c<=P-M, where c is the number of assigned shorts. Thus

    S_run+2c <= 3-3P <= 0.

If P=1, the cases M=0 and M=1 have respective capacities one and zero.
The case M=2 is a positive run and has zero capacity. Its +2 is paid by
its earlier sponsor. Summing over the finite segment proves the result.

## Scope checks

No initial whiteness is needed on B or C. Initially black T cells are
never processed under the cap. Initial whiteness of A is essential, even
when the segment has no black upper A bridges: the sponsor proof needs
the initial black state at A_s to have been made by the middle top visit.

This proof does not cover an unfinished final upper run. It also gives a
change in a row functional; one must retain its initial row terms before
using it at a shifted cap.
