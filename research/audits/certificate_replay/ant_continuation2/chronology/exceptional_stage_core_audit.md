# Exact archive and core audit for the mass-four exceptional chain

Status: the checks described here pass for every integer parameter \(n\ge200\).
They are exact affine and parity checks. The companion script is
**audit_exceptional_stage_cores.py**, with output
**exceptional_stage_core_audit.json**.

The prescribed ant prefixes are proved by the separate checker
**../planar_structure/certify_exceptional_rectangle.py**, whose output is
**../planar_structure/exceptional_rectangle_affine_certificate.json**.
The present checker reconstructs their complete XOR fields independently
from the prescribed words and verifies the two clean-tail normalizations.
It does not repeat the prescribed-prefix color proof. The output records
SHA-256 hashes of the exact template and prefix certificate it audited.

## 1. Conventions and exact affine representation

North is \(+y\), headings \(N,E,S,W\) are \(0,1,2,3\), white turns right,
black turns left, and each update flips the read cell before moving.
The standard word \(W\), its thirteen-cell finite seed \(P\), and its
canonical drift \((2,-2)\) are those in **../../ant_continuation/ant_exact.py**.
The canonical pose at phase zero is \((0,0),S\).

An affine coordinate is \(an+b\), represented by the integer pair \((a,b)\).
The symbolic field is a finite XOR sum of affine points and finite affine
rays
\[
\{b(n)+jv:0\le j<M(n)\},
\]
where \(v\) is one of the four standard diagonal drifts and \(M(n)\) is
an affine positive integer. The representation retains every initial black
cell and every odd write in every prescribed segment.

The audited family is
\[
\begin{aligned}
q&=(-33-2n,-14-2n),\\
a&=(-33-2n,41+2n),\\
c&=(8+2n,-14-2n),\\
d&=(8+2n,41+2n).
\end{aligned}
\tag{1}
\]

The first checkpoint is after template segment 4, at
\[
T_1=208n+70733,\qquad (p_1,h_1)=((-15,26),E).
\tag{2}
\]
The second is after segment 8, at
\[
T_2=416n+146040,\qquad (p_2,h_2)=((40,-50),S).
\tag{3}
\]

The present checker verifies, for the entire parameter range, that \(a,c,d\)
are unread through \(T_1\), and that \(c,d\) are unread through \(T_2\).
This allows the first state to be used for the input \(\{q\}\), and the
second for the input \(\{q,a\}\), by exact first-difference coupling.
Removal is implemented by XOR with the omitted initial bits. It is not an
assumption that a visually recognizable core is a subset of the actual field.

## 2. Phase-correct standard fields

At the first checkpoint the incoming infinite standard word is
\[
W[99:]\;W[:99].
\]
Start the canonical \(P\) from \((0,0),S\), evolve exactly 99 steps, rotate
the resulting complete finite field by \(180^\circ\), and translate its
canonical origin to \((-13,27)\). This gives a 26-cell field \(C_1\) with
the exact pose \((-15,26),E\). Its standard infinite tail has drift
\((-2,2)\), and
\[
-50\le x-y\le-40\qquad\text{on }C_1.
\tag{4}
\]

At the second checkpoint the standard word is
\[
W[100:]\;W[:100].
\]
Evolve canonical \(P\) exactly 100 steps and translate its canonical origin
to \((38,-50)\), with no rotation. This gives a 25-cell field \(C_2\)
at pose \((40,-50),S\). Its infinite tail has drift \((2,-2)\), and
\[
88\le x-y\le98\qquad\text{on }C_2.
\tag{5}
\]

Both clean fields are independently checked by the exact all-future
breakpoint verifier **certify_period**. Their complete cell lists are in the
audit JSON.

Let \(B_1(n)\) be the actual complete field at (2) after the unread
\(a,c,d\) have been XOR-removed, and let \(B_2(n)\) be the field at (3)
after XOR-removing \(c,d\). Define the full archives
\[
H_i(n)=B_i(n)\triangle C_i.
\tag{6}
\]
The affine representation proves the conservative support bounds
\[
\operatorname{supp}H_1(n)\subseteq\{-82\le x-y\le58\},
\tag{7}
\]
\[
\operatorname{supp}H_2(n)\subseteq\{x-y\le93\}.
\tag{8}
\]
These bounds retain all long forward and reverse wakes. In particular,
the second archive can extend arbitrarily far toward negative \(x-y\);
the proof uses only its upper bound.

More strongly, the checker proves **the XOR color of each archive is zero
at every read of the entire corresponding clean infinite tail**, for every
\(n\ge200\). This is an exact ray-parity verification over every future
period, not an observation of a finite number of clean blocks. Thus
the full one-bit parent state at (2) is permanently NW, and the full
two-bit parent state at (3) is permanently SE.

## 3. Literal thirteen-cell normalization

The clean phase-99 state reaches phase zero after five further updates:
\[
(-15,29),N.
\tag{9}
\]
At this pose the chosen clean field is literally a translated
\(180^\circ\) rotation of \(P\), with thirteen cells.
XOR with the complete actual field gives an archive still satisfying (7).
The checker again verifies archive color zero on every future \(W\)-ray.

The phase-100 state reaches phase zero after four further updates:
\[
(40,-52),S.
\tag{10}
\]
Here the chosen clean field is a translation of \(P\), again with exactly
thirteen cells. Its complete XOR archive satisfies
\[
x-y\le97.
\tag{11}
\]
It too is checked to be zero on all future \(W\)-rays.

It is harmless to retain the weaker bound \(x-y\le98\) from the separate
geometric proof. The distinction between the phase-100 archive bound 93
and the phase-zero bound 97 comes from moving some finite old wake into
the archive when choosing a new thirteen-cell core.

## 4. Exact exceptional fresh rays

The canonical phase-72 read is \((8,-2)\). At stage 1, the first upcoming
phase-72 read occurs after 77 updates and is
\[
(-23,31),N.
\]
The corresponding ray is
\[
(-23,31)+k(-2,2),\qquad k\ge0,
\tag{12}
\]
and hence has \(x+y=8\).
The axial partner \(a\) of \(q\) lies on this ray exactly at \(k=n+5\).
Its contact time in the prescribed template is
\[
312n+71330.
\tag{13}
\]

At stage 2, the first upcoming phase-72 read occurs after 76 updates:
\[
(48,-54),S.
\]
Its ray is
\[
(48,-54)+k(2,-2),\qquad k\ge0,
\tag{14}
\]
and hence has \(x+y=-6\).
The axial partner \(c\) in (1) lies on it at \(k=n-20\).
Its template contact time is
\[
520n+144036.
\tag{15}
\]

These are phase statements relative to the supplied word \(W\).
They do not identify every point of a diagonal with an exceptional channel;
the heading, lattice parity, and first-read phase are retained.

## 5. Audit of the affine parity engine

The engine was inspected against the following mathematical identities.
This is an independent mathematical audit of its arithmetic, rather than
an independent second implementation of the entire prescribed-prefix checker.

For a fixed word, record one required initial bit at each distinct read
cell. If a cell has been visited an odd number of times earlier in the
same word, its required initial bit is the prescribed read bit XOR one.
Every subsequent occurrence must give the same initial requirement.
The set of odd reads is exactly the net field change of the word.
This justifies grouping repeated reads into a single color constraint.

For a periodic segment, let the current read in epoch \(k\) be \(q+kv\).
An old isolated black point \(b\) contributes exactly when
\[
b-q=kv.
\]
An old ray \(b+je\), \(0\le j<M\), contributes when
\[
kv-je=b-q.
\tag{16}
\]
For nonparallel \(v,e\), the unique candidate values are
\[
k=\frac{(b-q)\times e}{v\times e},
\qquad
j=\frac{(b-q)\times v}{v\times e}.
\tag{17}
\]
The signs used in both formulas agree with (16).
For parallel drifts, the engine first checks collinearity and lattice
divisibility, then computes the resulting interval of epochs. The only
parallel cases used are \(e=v\) and \(e=-v\).

A net-flip cell \(b\) from an earlier copy of the same periodic word
contributes at the current phase precisely when
\[
b-q=mv,\qquad m>0,\quad k\ge m.
\tag{18}
\]
This is the step function used for the current segment's own accumulated
wake. Its threshold has zero parameter slope because both local points
have the same affine base.

Every contribution therefore gives an interval of integer epochs.
Its parity indicator is represented by toggling its two endpoints:
\[
\mathbf1_{[\ell,h]}(k)
=\mathbf1_{k\ge\ell}\oplus\mathbf1_{k\ge h+1}.
\tag{19}
\]
Cancellation of every boundary is a sufficient exact proof that the total
read parity equals the required value for all epochs. For the infinite-tail
check, an interval extending forever contributes only its starting boundary.

All affine orders used to clip these intervals are checked on the whole
range \(n\ge200\), by their slope and endpoint value. If an order changes
in the allowed range, the checker raises an assertion instead of choosing
the order at a sample. A possible isolated integer point or line incidence
above the threshold is likewise rejected, unless the relevant exact
equation already accounts for it. Affine divisibility checks reject cases
that would require an unhandled parameter residue class.

The complete rectangle proof also checks its final infinite word using
the entire retained field. It does not declare a tail merely because
several periods agree. In the present normalization audit the same exact
interval machinery is used with required archive color zero and no archive
writes. That proves the pointwise avoidance needed by subsequent
first-difference coupling.

## 6. Scope of the conclusion

These files establish the needed one- and two-collider parent states and
their complete archives for all \(n\ge200\). The separate
**mass4_later_collision_guards.py** derives the full read-set bounds needed
to show arbitrary remaining cells stay unread before these parent states,
and to exclude the nine ordinary second- and third-collision channels.

The full rectangle certificate proves a permanent standard NW tail for
the forced family (1). Combining that certificate with the reachability
reductions is a separate theorem-level argument. Neither a finite range
of probes nor the core normalization alone proves the general highway
conjecture, and no novelty claim is made here.
