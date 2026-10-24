# An exact obstruction to fixed-port, one-tape compiler architectures

22 October 2026. Status: qualitative scope independently confirmed, including
arbitrary initial backgrounds. The finite-prefix numerical bound, including its
final-window correction, also independently passed audit. Logical corollary of the independently audited
finite-controller pumping theorem in
../core_periodicity_new/compact_closed_excursion_export.md.
No general nonuniversality theorem and no highway proof is claimed.

## 1. The physical architecture being excluded

Suppose one actual ant trajectory, on any initial background, is interpreted at strictly
increasing checkpoint times t_n as the successive configurations of a
source computation. Assume that, for this compiled instance, there are:

- a finite set P of physical ant checkpoint poses;
- a fixed finite set C of controller cells;
- a fixed finite window W in Z^2;
- locations q_n with ||q_(n+1)-q_n||_infinity<=v for a fixed finite v;

such that the COMPLETE net board change between consecutive checkpoints
is contained in C union(q_n+W).

All temporary work between checkpoints is allowed, at any distance and
for any duration. The condition is only that every other cell is restored
exactly by the next checkpoint. The rest of the tape may be arbitrarily
large initially and need not have bounded mass. There are no external head
resets or unrecorded controller modifications.

Then the checkpoint sequence is finite. In particular this architecture
cannot faithfully represent an infinite source computation.

The constants and sets may depend on the compiled machine and input; they
need not be uniform across all compiler outputs. The exclusion applies
separately to each finite compiled instance.

## 2. Why the translated clocks matter

For identical endpoint poses and complete board XOR A, the audited clock
family gives

    elapsed time <= |A|*(3^ceil(d/2)-1),

where d is the smaller of the two diagonal spans of A. The pose and every
unchanged tape cell cancel from the clock difference. Thus a complete XOR
inside one bounded translated patch bounds elapsed time independently of
the patch's distance from the physical port.

Let N=|P|*2^|C|. Among N+1 successive checkpoints, some two have identical
pose and identical controller restriction. Their combined XOR therefore
lies only in at most N moving windows. Bounded q increments put their
union inside one uniformly bounded patch around the initial q location.
The clock bounds the time between those two checkpoints. The XOR is
nonempty, since an exact full-state recurrence would contradict the clock.
At least one changed cell must have been reached from the bounded port set
and returned from, so the moving window's location is uniformly bounded.

For an infinite checkpoint sequence this applies at every starting index.
All net changes then lie in one fixed finite region, and some COMPLETE
checkpoint state repeats, which is impossible.

## 3. Explicit finite-prefix version

Take W contained in [-r,r]^2, all checkpoint positions within sup-radius
R_P, and integer v>=0. Set

    L=r+Nv,
    T=(2L+1)^2*(3^(2L)-1),
    Q=ceil(R_P+L+T/2).

Every valid block of N checkpoint intervals bounds its first moving-window
center by Q. In a finite sequence of M>=N intervals, this controls all
centers except possibly the final N-1; bounded increments put those within
Q+Nv. Therefore all checkpoint XORs lie in a mutable set of size at most

    D=|C|+(2*(Q+Nv+r)+1)^2.

There are at most |P|*2^D possible COMPLETE checkpoint states: the exterior
board is frozen, regardless of its size or contents. Such states cannot
repeat. Hence M+1<=|P|*2^D when M>=N. For shorter sequences M<N already.
The maximum of these bounds is a computable architecture-only upper bound
on the number of successful checkpoint transitions.

This bounds interpreted transitions, not the physical cost of a final
unsuccessful attempt to reach another checkpoint. A purported compiler
may cease to obey its architecture; the theorem does not decide its later
unrestricted physical behavior.

## 4. The precise Turing-machine corollary

A natural but invalid proposed design is a finite ant CPU at a fixed port,
with one spatially embedded tape. After each simulated source step the ant
returns to that port, changes only its finite controller and a bounded
neighborhood of the simulated tape head, and leaves the rest of the tape
unchanged. If adjacent source tape positions have bounded physical spacing,
the simulated head's move has bounded q increment. This design satisfies
the hypotheses above and cannot run indefinitely from any finite seed.

Consequently no exact universal compiler with these properties can include
all nonhalting source runs. A halting reduction cannot simply assume that
such a reusable fixed CPU plus one locally updated tape has been built.

This is stronger than observing that exact finite-state cycles are absent:
the simulated tape may grow without bound in the intended architecture,
and its controller may act aperiodically. The translated clock still
prevents the required physical return sequence.

## 5. Explicit escape routes, not constructions

The theorem does NOT exclude:

- a physical ant head that follows the simulated head instead of returning
  to a bounded pose set;
- two spatially separated moving write windows, such as two growing ends;
- distributed net garbage left along each journey;
- a controller whose spatial footprint grows;
- unbounded jumps of the simulated write-window location.

Any of these could evade this particular proof. None by itself supplies a
compiler, an undecidability reduction, or a finite-seed nonhighway orbit.

The arbitrary-background extension is independently confirmed: for each
finite interval, copy its entry colors on the finite read set into a finite
seed. This preserves its entire trajectory, endpoint poses, and complete
XOR, so the clock bound transfers exactly. Any alleged exact full-state
cycle transfers in the same way and is impossible. Therefore the pumping
argument does not require globally finite initial support. Infinite initial
hardware alone does not evade this architecture obstruction.

## Subsequent geometric strengthening

The independently audited `one_sided_cpu_hull_obstruction.md` removes the moving-window, write-count, and bounded-motion assumptions when the entire allowed mutable memory lies strictly on one side of the finite physical CPU poses. It gives at most |P|*2^|C| actual checkpoints by the complete closed-pose hull identity. This does not subsume two-sided moving-window layouts, so the original theorem remains useful.

The independently audited `oblique_strip_clock_obstruction.md` extends the bounded-write fixed-strip variant from the two diagonal directions to every non-axis strip. Axis-parallel and translating-strip exceptions remain explicit.
