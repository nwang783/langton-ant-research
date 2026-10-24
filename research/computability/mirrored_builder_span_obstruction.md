# Vertical-span obstruction for mirrored advancing endpoint builders

Status: independently analytically audited on 2026-10-22 at22:53 UTC. This restricts a proposed builder architecture; it does not exclude arbitrary two-ended ant dynamics.

## 1. Symmetric endpoint geometry

Fix the half-turn

    T(x,y)=(-1-x,S-y).

Suppose a sequence of nonempty actual closed-pose ant intervals has COMPLETE board XOR masks A_n contained in

    R_n union T(R_n),
    R_n subset [q_n-w,q_n+w] times [l,u],

where w,l,u,S are fixed and q_n tends to positive infinity. The initial and final physical pose of each interval agree. Its start need not equal that of another interval. Suppose one fixed cell z=(x_0,y_0) is read during every interval. Then

    2*abs(y_0-S/2) <= u-l.                       (1)

In particular every fixed cell read during infinitely many such intervals lies in the central vertical band S/2 plus or minus (u-l)/2.

Proof. Use centered coordinates X=x+1/2, Y=y-S/2. The half-turn is negation. Write Q_n=q_n+1/2 and H=u-l. Any point in conv(R_n union -R_n) is a convex combination with total right-hand weight mu. Its horizontal coordinate satisfies

    abs(X-(2mu-1)Q_n) <= w.

The right-hand Y interval is [l-S/2,u-S/2] and the left-hand interval is its negative. Consequently

    abs(Y) <= H/2 + abs(2mu-1)*abs(u+l-S)/2
           <= H/2 + (abs(X)+w)*abs(u+l-S)/(2Q_n).

The closed-pose hull theorem from one_sided_cpu_hull_obstruction.md puts every read cell in conv(A_n), hence in this enclosing hull. Substitute the fixed z and let n tend to infinity, obtaining(1). The case u+l=S already has no correction term. QED.

The sets R_n only need to bound the complete net changes. They need not bound all temporary work. Any lasting controller change must be included: a fixed central XOR term cannot simply be omitted. For an exactly restoring or finite-phase controller, take a full phase cycle so its changes cancel before applying the lemma.

## 2. Application to the eight-pass target

The proposed architecture is
../causal_reduction/periodic_port_builders/eight_pass_builder_plan.md.
Its right excursion has entry(0,2,E), exit(-1,1,W), so S=3. A fixed left cap, restored settled bulk, translated fixed right cap, and six-column growth put every full right-excursion XOR in one bounded-width advancing right patch. Half-turn gluing puts the complete pair XOR in the two patches required above.

The fourth bulk pass transfers the upper rail from row8 to row11. It reads row11 in every mature bulk column. Choose one fixed such column beyond the bounded left cap; its row11 cell is read on every sufficiently large pair of excursions. Hence(1) requires

    u-l >= 2*11-3 = 19.

Thus an exact regenerative realization of this architecture cannot have its endpoint XOR confined to rows0..11, or to ANY vertical interval of span less than19. At least20 row levels are needed in the allowed right-end change region, unless some other premise changes.

This does NOT rule out taller finite right caps. Nor does it rule out a different port sum S, distributed persistent changes through the old bulk, nonrestoring unbounded controller memory, or a different pass schedule. The core bulk identities and modular charge checks remain valid. The obstruction is additional all-history geometry that must be checked before small-height cap synthesis.

If the actual cap's support is vertically bounded by a larger interval, use that larger bound: it is the complete XOR span, not just the stable hardware rows, that matters.
