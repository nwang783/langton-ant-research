# Two black cells can satisfy the endpoint clock constraints

## Scope

This note gives a family of candidate endpoint states. It does not assert that
the ant can travel between them, or reach them from the blank start. The family
shows why row and column parity plus all critical one-sided endpoint clock
inequalities do not prove that mass at most two occurs only finitely often.
The root analysis proposed the family. The algebra below checks it independently.

## Family

For each n>=1 let

    B_n={(0,2n),(2n+1,2n)},
    p_n=(2n+1,-4n-1),       h_n=S.

The invariant sector is sigma=+1. The corrected row parity is empty and the
corrected column parity is {0}, as for the blank state at (0,0),N. The mass
change two also gives the required heading change N to S modulo four.

## All critical one-sided clocks

Let a,b>1 satisfy (a-1)(b-1)=4. Put

    m=2n+1,      c=2b/(b+1),      d=2/(b+1).

Thus 0<d<1<c<2. Take the four monomial components of the critical potential
in `clock_escape/evidence/critical/proof.md`. At centre zero the four values
for X_n are

    NE=(a^m-1)b^(2n) - c a^m b^(-4n-1),
    NW=(1-a^(-m))b^(2n) - c a^(-m)b^(-4n-1),
    SE=(1-a^m)b^(-2n) + d a^m b^(4n+1),
    SW=(a^(-m)-1)b^(-2n) + d a^(-m)b^(4n+1).

The blank start values are (d,d,-c,-c). Each X_n value exceeds its blank
value. In fact NE>1, NW>1, SE>0, and SW>-1.

For NW, multiply NW-1 by a^m. The result is

    (a^m-1)(b^(2n)-1)-1-c b^(-4n-1)>4-1-2>0.

The first product is at least (a-1)(b-1)=4.

For NE, multiply NE-1 by b^(4n+1), and set D=b^(4n+1). The result is

    (a^m-1)(b^(6n+1)-1)-(c-1)a^m-1-D.

Geometric sums and criticality give

    (a^m-1)(b^(6n+1)-1) >=4 a^(m-1)D.

The term b^(4n+1) occurs in the second geometric sum because n>=1.
Also a(c-1)=(b+3)/(b+1)<2. The displayed difference is therefore greater than

    a^(m-1)(4D-2)-1-D >=3(D-1)>0.

For SE, write it as

    a^m b^(-2n) [d b^(6n+1)-1]+b^(-2n).

The bracket is positive since 2b^(6n+1)>b+1. Finally SW>-b^(-2n)>-1 because
all its other terms are positive.

Changing the centre multiplies each one-sided potential, for both endpoint
and source, by the same positive factor. Thus every translated critical
one-sided endpoint inequality passes as well.

## Limit of this check

Each one-sided critical component is nondecreasing, but it can have zero
increments. It need not tend to positive infinity along an actual orbit.
Only suitable combined or radial clocks have a uniform positive time gain.
The argument above does not supply a reachable endpoint, an orbit segment,
or a counterexample to eventual mass growth. It only blocks this particular
endpoint-only proof strategy. Actual chronological constraints remain needed.
