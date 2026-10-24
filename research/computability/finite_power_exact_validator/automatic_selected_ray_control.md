# Executed automatic required-color test on genuine nested occurrences

2026-10-23 05:06 UTC. Implementation awaiting independent review.
This is a known negative presentation used as a control, not a new exclusion class.

Take images RLLLLRRRR / LRRRRLLLL for every incoming heading, spatial A=I,
root0=(incoming N, R). In its exact occurrence graph, choosing child1 twice
is the genuine cycle0→3→0 with total offset(1,1). Repeating that cycle a times
selects an actual read at(a,a) in phi^(2a)(root), whose required color is white.

The exact earlier-sibling decomposition gives its PRIOR read parity

    C(a)=XOR_(k=0..a-1) [Q_0(2k+1,k+1,k+1)+Q_3(2k,k,k+1)].

Any initial board realizing the prescribed word must therefore have initial
black bit C(a) at(a,a). This statement does not require the selected read to
be the first visit. For an inconsistent prescribed word, selected requirements
can themselves already rule out finite support; no sufficiency is inferred.

`automatic_selected_ray_control.py` builds both rational parity arrays from
literal images and their exact Laurent transfer. Each reduced rational series
has a45-state Cartier automaton. Direct affine pullback uses carry states:
at every low-to-high binary digit it emits the three affine-output bits into
the Cartier machine and updates the integer carries. Negative final carries
mean an invalid negative output index and give zero; nonnegative final carries
are flushed exactly. The two pulled-back one-variable predicates minimize to
2 and3 states.

The bounded F2 projection explicitly supplies0<=k<a, so every counted k has
one encoding within the visible a's bit length. Its finite-vector construction
returns a6-state relation C(a). The exact automatic boundedness sentence is
FALSE: infinitely many selected cells require initial black.

Controls compare257 finite parity sums and48 positions from a separately
computed literal spatial-polynomial recurrence through depth48. The saved
transition/acceptance table and full output are in
`automatic_selected_ray_control.json`. All calculations are exact integers,
finite fields or finite automata; there is no numerical cutoff interpreted as
nonexistence.

The underlying unit-nine presentation was already excluded by other exact
controls, including its non-ray signed denominator. The new result is that the
critical unknown-mass mechanism has been executed on an UNBOUNDED family of
genuine occurrences with non-Presburger-looking parity, without supplying an
initial coloring or a hand-guessed parity template. The complete finite-cover,
canonical-selector and all-chronology pipeline remains unimplemented.
