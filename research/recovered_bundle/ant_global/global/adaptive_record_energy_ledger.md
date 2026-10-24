# An exact energy ledger at successive virgin records

21 October 2026. This is a state-dependent reduction using the completed and
unfinished fresh-A cap inequalities. It does not give a decreasing global
budget or prove eventual highway capture.

## 1. Consecutive record heights and adaptive cuts

Assume finite initial black support. Fix the heading sector in which an
even-height row x+y=h is entered from below with heading E. Work above the
initial black support and the initial ant. Once this virgin region is
reached, successive completed upper caps
have heights h_j with h_(j+1)=h_j+2: the first fresh odd-level read sends the
ant to the next even level.

Let t_j be the first unprocessed black-top event at height h_j, immediately
before the ant leaves that cap for the first time. Assume the relevant
records exist. All earlier processed visits to row h_j were white and unique.
The immediately preceding event is at height h_j-1 and departs E. There are
two possibilities.

1. It is white, arrives N, and turns E. Set a_j=t_j-2. At a_j the ant is on
   row h_j-2 and is about to depart N.
2. It is black, arrives S, and turns E. The event at t_j-2 is then a white
   top event on row h_j. That fresh top was itself entered from a white A
   event arriving N at t_j-3. Set a_j=t_j-4. Again the ant is on row h_j-2
   and is about to depart N.

Why is the A event in case 2 white? With A initially white and with no
previous cap exit, any black upper A turn requires its right top port to
have been used earlier. Its outgoing top is already black. It cannot be
the predecessor of the fresh white top at t_j-2.

An unconditional cut t_j-2 would be wrong in case 2. The adaptive two- or
four-event cut is essential.

For the next cap H_j=h_j+2, the ant at a_j is at level H_j-4, below C. The
new T and A rows have never been visited and are white. The initial colors
on the new B and C rows are the actual colors left on the old T and A rows.

The intervals I_j=[a_j,a_(j+1)) are consecutive. Measured relative to H_j,
the endpoint a_(j+1) is on B, at height H_j-2, about to depart N. It has
incoming E on black, or incoming W on white. The whole interval stays under
the cap H_j.

## 2. The initial energy of the next interval is an exact visit count

For actual black counts on a physical row, write b_r(t). Define

    E_H(t)=12b_H(t)-8b_(H-1)(t)+4b_(H-2)(t)-b_(H-3)(t).

At the start of I_j, T and A are white. Its initial energy is therefore

    Q_j=E_(H_j)(a_j)
       =4b_(H_j-2)(a_j)-b_(H_j-3)(a_j).

Let M_j and Delta_(A,j), Delta_(B,j), Delta_(C,j) be the interval counts.
There is no processed black upper A turn in I_j. Such a turn would lead
immediately to the first black top event, but the adaptive cut a_(j+1)
occurs before that turn. Since the endpoint is on B, the exact port identity
has no A/T endpoint correction. It gives

    N_(A,j)=4M_j-Delta_(A,j).

At a_(j+1), the next cap is H_j+2. Its new T,A are still white, and its B,C
are the current T,A. Thus

    Q_(j+1)=4M_j-Delta_(A,j)=N_(A,j).              (1)

This is an exact recurrence for the inherited two-row energy.

At a genuine next-record cut, M_j>=1 and at least one selected black lower A
event has occurred. Indeed, a top diamond already seen before an admissible
B endpoint belongs to a completed nontrivial upper excursion, or its selected
black A event has already occurred in the current upper excursion. The only
exceptional unfinished-right-diamond B,W endpoint would have a black next A
cell, whereas an adaptive cut has a white next A cell. Thus

    Q_(j+1)=N_(A,j)=2M_j+(number of black lower A events)>=3.

## 3. Exact shift and the lower-corner term

Set

    R_j=8M_j-7Delta_(A,j)+4Delta_(B,j)-Delta_(C,j).

Then the energy on the current four rows at the end of I_j satisfies

    E_(H_j)(a_(j+1))-Q_(j+1)=Q_j+R_j.             (2)

Let L_j count black lower C corners in I_j. The unfinished-prefix theorem,
with the next-A color required at an adaptive cut, gives

    R_j >= L_j-c_j,

where c_j is 3 if a_(j+1) has incoming E, or 0 if it has incoming W.
Consequently the exact discarded difference at the shift obeys

    E_(H_j)(a_(j+1))-E_(H_j+2)(a_(j+1))
        >= Q_j+L_j-c_j.                           (3)

Here are the needed refinements of the generic B-endpoint table. At B,E,
the generic maximum 5 occurs only immediately after an initial zero excursion
with two diamonds. Its next A cell is black, so this is not an adaptive cut.
The largest remaining score is 3, after an initial zero with only its right
diamond. At B,W, a white A predecessor in a right diamond gives a black next
A cell and is excluded; in a left diamond B is black and departs S, also
excluded. After a selected black A event, the general score is at most zero.
The sole exceptional score 2, after an initial two-diamond zero, again has a
black next A cell and is excluded. These are exactly the local phases in the
unfinished-prefix proof.

The lower-corner term has not been dropped. For j after the first interval,
Q_j>=3, so the discarded difference is at least L_j and is nonnegative.
However, neither Q_j nor L_j is a priori bounded by a finite initial resource.

## 4. Energy is generated during the intervals

Write D_j,Z_j for the exact prefix charging quantities. At an incoming-E
adaptive cut they are nonnegative and the port identity gives

    Delta E_(H_j)=N_(C,j)+8D_j+4Z_j-2.

At an incoming-W adaptive cut the preceding A event is black; there is no
unfinished top roof. Here D_j>=0 and Z_j>=-1, and the exact identity gives

    Delta E_(H_j)=N_(C,j)+8D_j+4Z_j+6.

Thus nonnegative energy loss at cap shifts does not by itself give a finite
budget. The intervals generate energy through visits to C and the other
nonnegative charge counts. These are actual trajectory counts; they have
not been bounded by the initial black support.

There is a precise obstacle even before a physical row leaves the ledger.
The C row of I_j is the A row of I_(j-1), but its visits in I_j can reach
physical cells that were never visited on A in I_(j-1). The identity of the
physical row does not imply equality of visit footprints or a bound on the
new visits by Q_j=N_(A,j-1). Repeated visits inside the old footprint also
need further chronological control.

## 5. The exact old-information term that is still missing

During I_j, a physical even row H_j is T. During I_(j+1), the same row is B.
After a_(j+2), it is below all four rows counted by the current cap. The same
is true of the odd row H_j-1, which is first A and then C.

For N>j+2 define the later changes

    Omega_even(j,N)=b_(H_j)(a_N)-b_(H_j)(a_(j+2)),
    Omega_odd(j,N) =b_(H_j-1)(a_N)-b_(H_j-1)(a_(j+2)).

These are exact signed sums of writes to those old rows after they leave the
four-row record ledger. They need not be zero. A trajectory can make lower
excursions and revisit them while respecting every later cap condition.

Any attempt to replace the sequence of four-row energies by one potential
on the full board must retain these Omega terms, with the chosen physical
row weights. Equations (1)--(3) do not bound them. The old rows' initially
white status cannot be reused after their first two appearances in the
ledger.

There is also an explicit allowance of three at an incoming-E record cut.
Although Q_j>=3 absorbs it in the shift-loss inequality, the interval energy
production remains. A standard highway directed toward increasing x+y already
has infinitely many such records, so proving that all records cease would be
the wrong target.

Thus the remaining global issue has a concrete form: control the later
Omega terms and the sequence of active substrate states strongly enough
to force their eventual standard repeating form. The new inequalities
restrict each finite interval but do not supply that control by themselves.
