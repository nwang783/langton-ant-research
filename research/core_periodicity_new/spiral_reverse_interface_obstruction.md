# A reversed seven-arm interface needs distributed repair

Status: independently analytically audited on 2026-10-22 at22:48 UTC, with a no-import literal clock/coordinate replay in ../audits/check_spiral_reverse_clocks_independent.py/json. This is a scoped obstruction, not an exclusion of debris-emitting renewal.

The inward-spiral endpoint E_n is the complete(7n+2)-cell board from quadratic_inward_spiral.md, normalized to head(0,0),N. It has sector+1. Let I be exact time reversal:

    I(B,p,h)=(B,p-d(h),h+2),       I F I=F^-1.

A rotated/translated copy of I(E_n) supplies an exact outward traversal of the inward word. The literal I(E_n) is in the opposite sector. To put it in the original sector with a half-turn, use

    g(q)=t-q,          t_x+t_y odd,
    Y_n=g I(E_n).

Then Y_n has board t-E_n and pose(t+(0,1),N). This is the particular clean outward interface considered here; arbitrary outward algorithms need not have this form.

## 1. Positive critical clocks of the endpoint

Use z=x+y and sigma=+1. The inherited monotone critical clocks are

    Psi_+=-sigma sum_B chi(q)3^z(q)+a(e)3^z(p),
    Psi_-=-sigma sum_B chi(q)3^-z(q)+a(-e)3^-z(p),

where e=+1 for N,E and -1 for S,W, a(+1)=1/2,a(-1)=-3/2. Their increments are nonnegative in every literal update, as proved in
../continuation_2026-10-22/ant_continuation/wake_clock/proof_notes.md, Section3.

Put A_n=Psi_+(E_n), C_n=Psi_-(E_n). The fixed nine-cell cap contributes signed board terms113/27 and113/3. The seven arms for each j=2,...,n contribute

    (2/3)(9^j+9^-j)-11/9,
    6(9^j+9^-j)-19,

respectively. Therefore

    A_n=253/54 + sum_(j=2)^n [(2/3)(9^j+9^-j)-11/9],
    C_n=217/6 + sum_(j=2)^n [6(9^j+9^-j)-19]
       =9A_n-8n+2.

In particular, for every n>=1,

    A_n >= (1/2)9^n >0,       C_n >=4*9^n >0.           (1)

The inequalities follow at n=1 by direct arithmetic, then by comparing each displayed increment with the increment of the stated geometric lower bound.

## 2. Clean reverse copies are unreachable

Time reversal negates each critical clock exactly. For example, shifting the incoming head backward by e in the z direction gives

    a(-e)3^(z-e)=-a(e)3^z,

and the sector changes sign. Thus Psi_+(I X)=-Psi_+(X), and similarly for Psi_-.

A half-turn/translation exchanges the two clocks, multiplying them by positive powers. If s=t_x+t_y, then

    Psi_+(Y_n)=-3^s C_n,
    Psi_-(Y_n)=-3^-s A_n.                               (2)

Both are negative. Since both clocks are already positive at E_n and nondecreasing forward, E_n cannot reach Y_m for ANY m>=1 and ANY translation t of the required parity. No cutoff on the connecting turn word is imposed.

## 3. A repair must reach both transverse ends

Suppose instead that a state Z is reachable after E_n, has exactly the target pose of Y_m, and differs from Y_m's board on a finite set D of k>=1 cells. Let z_max and z_min be the extreme z coordinates of D. A changed cell contributes at most3^z to an increase of Psi_+, and at most3^-z to an increase of Psi_-. Therefore positivity of the reachable clocks and(2) imply

    k3^z_max >3^s C_m,
    k3^-z_min >3^-s A_m.

The target head has z=s+1. Hence

    z_max-z(head) > log_3(C_m/(3k)),
    z(head)-z_min > log_3(3A_m/k).                       (3)

Using(1), the repair must extend beyond the head in BOTH diagonal directions by at least

    2m-log_3 k+log_3(4/3),
    2m-log_3 k+log_3(3/2),

respectively, with the strict inequalities understood from(3). In particular, if D is contained in a diagonal band |z-z(head)|<=w, then

    k3^w >3A_m >=(3/2)9^m.                             (4)

If D lies in an l_infinity radius-r cap at the head, w<=2r, so

    2r+log_3 k >2m+log_3(3/2).

Thus a bounded-count, bounded-radius local cap cannot turn the seven-arm endpoint into its clean same-sector outward-reversal interface for an unbounded family. Constantly many repair cells placed at the distant arm ends remain possible; this theorem does not exclude them.

## 4. Why signed cuts alone did not give this obstruction

The exact exploratory probe_spiral_reverse_charges.py/json compares both conserved mod4 charge arrays. For m=n, the half-turn translation t=(-n-4,n-1) leaves total cyclic-distance mismatches4 on columns and4 on rows for the checked n. For m=n+1, t=(-n-5,n) gives5 and3. These are finite controls only, not an all-n formula or an asserted reachable interface.

They refute the tempting expectation that every sector-compatible reverse copy necessarily has a charge discrepancy growing with n. The clock obstruction is different: it requires distributed high-weight repair even when the modulo-four mismatch is small. It does not say that a bounded NUMBER of arbitrarily remote repair cells is impossible.
