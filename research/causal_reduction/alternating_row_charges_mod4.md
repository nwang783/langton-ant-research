# Exact alternating-row charges modulo four

Status: elementary derivation, 22 October 2026; independently audited via the
mixed-shuttle incidence check and the later swept-front/column-filter review.
These are not real-valued monotone fuel charges. They do not by themselves
exclude the dense-to-sparse rail transfer considered here.

Let a:Z->Z be arbitrary and choose an integer antiderivative A satisfying
A(y+1)-A(y)=a(y). Let f(x,y)=(-1)^x a(y). On every finite black board define

    Q_a(B,p,h) = sum_{(x,y) in B} f(x,y) + g(p,h)  (mod 4),

where p=(x,y), headings are N,E,S,W, and

    g_N = 2A(y),
    g_E = 2A(y)+(-1)^x a(y),
    g_S = 2A(y)+2a(y),
    g_W = 2A(y)-(-1)^x a(y).

Then Q_a is exactly conserved. For a right turn the black-board charge
increases by f(p), and for a left turn it decreases by f(p). Directly checking
the eight heading/turn combinations gives respectively

    g(p+e_{h+1},h+1)-g(p,h) = -f(p) (mod 4),
    g(p+e_{h-1},h-1)-g(p,h) = +f(p) (mod 4).

For example, N->E uses the sign flip of (-1)^x after moving east. E->N uses
2A(y+1)=2A(y)+2a(y), and 2(-1)^x a(y)=2a(y) modulo four. The other cases
are the same identities. Arbitrary a selects independent row charges; the
quarter-turn rotated construction gives analogous column charges.

The modular qualification matters: the equality for E->N generally fails
over the integers when x is odd. Thus these cannot be treated as ordered or
nonnegative resources. Nor should the infinite sum on a dense rail background
be used without a finite-difference normalization.

For a periodic westgoing interface of even horizontal displacement p, removing
the p solid cells in each of rows 0 and -2 has alternating sum zero. Its pose
correction also returns to the same value after an even horizontal translation.
Consequently these charges impose no immediate obstruction to converting the
infinite dense rail (solid rows 0,-2; odd black cells in row -1) to the sparse
rail (only the odd black cells in row -1). Any stronger endcap claim must use
additional information.

## Crossing a column versus returning from it

The rotated head correction away from a selected column k is2A(x), where
A(x)=0 for x<=k and A(x)=1 for x>=k+1. Therefore any finite trajectory
segment whose endpoints lie strictly on opposite sides of column k changes
that column's alternating vertical black sum by2 modulo4. This holds in
either crossing direction. If both endpoints lie on the same side, its
change is0 modulo4. The head directions at the endpoints do not matter,
because the local a(x) term vanishes away from k.

Consequently a white-input rightward translating front leaves charge2, not0,
in every sufficiently remote settled column. Returning right-half-plane
builders have charge0 because their complete excursion endpoints lie on the
same side of every positive column. Confusing these two contracts wrongly
admits wake candidates. Column parity alone sees neither distinction.
