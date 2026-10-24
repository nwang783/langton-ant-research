# A computable pristine-climb cost and a stronger fresh-record obstruction

2026-10-22, 23:26 UTC. Status: independently audited in full. The no-import complex-coordinate copied-board replay in `../audits/check_pristine_climb_independent.py` and `../audits/pristine_climb_independent.json` verifies all catalogs,92 conflicts, the sharp witness, and the time61 standard record. All metatheorem and speed consequences were analytically reviewed. No highway conclusion is asserted.

## 1. The boundary-value problem

For H>=0 let c(H) be the smallest number of south moves in an actual finite ant interval which starts at (0,0,N), has every cell y>=0 initially white, and stops at its FIRST hit of row H. Colors below row0 are arbitrary. Put c(0)=0. A finite interval only reads finitely many cells, so the same minimum results if the lower initial black set is required finite.

If such an interval spends S south moves, it has H+S north moves. Its first movement is horizontal, its last is north, and axes alternate. Thus its exact length is

    2H+4S.

For fixed H,S this is a completely decidable finite-word feasibility problem, not a semidecision with an unknown time horizon. Enumerate all words of that length, require the indicated first-hit geometry, require alternating turns at every repeatedly read cell, and require R on the first read of every upper-half-plane cell. These conditions are necessary and sufficient by assigning the finitely many first-L lower cells black.

The minimum is finite, with an explicit standard-highway upper bound

    c(H) <= 25*ceil(H/2).

Indeed take the certified standard104 finite seed, rotate it by180 degrees so its drift is(2,2), and cut at its first hit of a row above its entire initial support. Explicitly, the half-turned seed has maximum black height6; its FIRST hit of row7 is time61, pose(2,7,N), phase61 of the certified word. Thus all cells on or above its entry row are still white. A literal104-read replay has direction counts(N,E,S,W)=(27,27,25,25) and endpoint(4,9,N). These values are bound in `pristine_standard_record.json`. The standard tail continues at its cyclic phase. Every104 moves advance height2 and contain25 south moves, so the first hit H rows higher occurs within ceil(H/2) periods. This provides an admissible finite lower board for every H. 

Consequently c is total computable by a bounded finite search, with an elementary exponential upper bound on a naive implementation. This does NOT make the full highway problem decidable.

## 2. Superadditivity and exact small values

Cut any admissible climb to H+K at its first hit of row H. Its prefix costs at least c(H). At that moment every row>=H is still initially white and untouched, and the incoming heading is north. After translation its suffix is an admissible K-climb, hence costs at least c(K). Therefore

    c(H+K) >= c(H)+c(K).

The audited one-south normal form F=RRRRLR gives c(1)=1. No two adjacent one-south crossings are possible, while F followed by G=RRRLLLLRLR is feasible, so c(2)=3.

The new exact finite certificate gives

    c(3)=7.

`check_three_row_climb.py` generates every one-row first-hit word with S=1,2,3,4 south moves. Their complete catalog sizes are1,1,4,16. Every three-row climb with total S<=6 splits into three such words, because each crossing needs at least one S and hence no crossing can exceed4. The certificate checks all92 triples with total S<=6; each violates alternating reads or a first upper white read, by read27 at the latest. It also supplies the legal sharp witness

    RRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLR,

ending at(1,3,N), with exactly7 south moves. Full catalog, all92 literal conflicts, and witness are in `check_three_row_climb.json`. The direct independent-method discovery probe exhausts the entire H3,S6 tree in29,332 nodes, but that large tree is unnecessary once the small catalog certificate is checked.

It follows for every H that

    c(H) >= C(H) = 7*floor(H/3) + d[H mod3],
    d[0]=0, d[1]=1, d[2]=3.

The finite catalog is local. Applying it repeatedly is an exact all-length theorem, not extrapolation from sampled trajectories.

Superadditivity and the standard upper bound also give a finite asymptotic slope

    lambda = lim c(H)/H = sup_{H>=1} c(H)/H,
    7/3 <= lambda <= 25/2.

The computable increasing sequence max_{1<=H<=n} c(H)/H approximates lambda from below. No computable convergence rate or computability of lambda is claimed.

## 3. Affine-inflation consequences

All conditions below concern a finite-support actual ant and an EVENTUAL identity p(kn+c0)=a*p(n)+b0. They have no finite-controller or heading-preservation assumption. c0,b0 denote affine offsets, not the climb-cost function.

For the independently audited axial/quarter-rotation fresh-record setup, let k=4ell+epsilon, epsilon in{-1,0,1} be the allowed movement-axis phase, A=|a| an integer, and

    s=ell+(epsilon-A)/2,
    b=max(0,A-ell-1).

The pristine part of the predecessor macro is an admissible b-climb. Therefore the earlier inequality s>=b+floor(b/2) strengthens to

    s >= c(b) >= C(b).

For the independently audited diagonal family a in{±m±mi}, write k=2m+4r and

    L=max(0,2m-r-1).

The two outward macros at a north-entered diagonal record include an admissible L-climb, with at most2r south moves. Hence

    2r >= c(L) >= C(L).

These are effective all-length necessary tests, and may be sharpened by further rigorously established c-values. They are not sufficient conditions for inflation and do not construct finite-seed alternatives to the standard highway.

## 4. A global coordinate-speed consequence

This consequence does NOT assume any inflation identity. Let Q be the axis-aligned bounding box of the finite initial black set together with the initial head. Once the trajectory first enters a row one unit above Q, it is in the pristine-climb setup. If it later reaches H further rows above that entry, the elapsed interval up to its first such hit has at least2H+4c(H) moves. Rotate this argument for each of the four coordinate directions.

Since 3*(2H+4C(H))>=34H-20 for every integer H>=0, every time t satisfies

    distance_infinity(p(t),Q) <= 1+(3t+20)/34.

The right side may be rounded down for an integer bound. In particular,

    limsup_{t->infinity} ||p(t)-p(0)||_infinity/t <= 3/34.

More generally the superadditive slope in Section2 yields the potentially stronger nonnumerical bound

    limsup ||p(t)-p(0)||_infinity/t <= 1/(2+4*lambda).

For this last statement, apply c(H)/H -> lambda along arbitrarily large attained record heights; directions which remain bounded need no estimate. Standard104 has coordinate speed1/52, consistent with lambda<=25/2. There is NO implication that a smaller finite-H c-value constructs an infinite faster finite-seed trajectory: the minimizing lower seed can vary with H. Nor does this speed ceiling show eventual direction, transience, periodicity, or capture.
