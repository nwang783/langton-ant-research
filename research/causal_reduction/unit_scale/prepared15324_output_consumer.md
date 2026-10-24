# An opposite-direction consumer of the 4352 wave's complete output

23 October 2026, 17:49 UTC. Independent all-future prepared-field audit passes.
Finite-original realization is stated separately in
`prepared4352_two_phase_finite_family.md`.

## Exact prepared source-end state

Use headings N,E,S,W=0,1,2,3; u=x+y and t=x-y. Normalize the394-cell producer
by subtracting (26N,26N) from its coordinates. The explicit source-end board
is defined without a finite-window approximation:

* The canonical13-cell H source is at (113,88,W), and its SW H halfwake is
  retained from that start through all future SW copies.
* The other four writer profiles are full bi-infinite standard profiles, at
  lanes (t,x mod2,heading)=(89,0,E),(9,0,W),(-57,0,E),(-5,0,W).
* All4352 wave copies indexed k<=2 are toggled, where copy k starts at
  (-2+26k,3+26k,W).
* Copy3 is toggled for its first2331 reads only.

This exact XOR board is the source-end contact field at pose(113,91,S).
The original13 cells, the incomplete original writer, every other writer,
and all nonstandard past reads are included. The code stores the complete
board as mod-(26,26) full profiles, upper rays and a finite XOR set.

The deterministic ant on that field executes the supplied142764-turn
transition, including two temporary NW104 segments whose complete future
checks fail after464 and568 further reads. It reaches (13,7,N).

## New all-future return wave

From that state the ant repeats a primitive word of length15324 with drift
(-78,-78), preserving heading N. Its word SHA256 is
`12c75ada3474e89e5fb99af4bb029ab9f7aa4de232d4fc6c213601d1c849db27`.
The full word and preceding transition are in
`prepared4352_output_return_wave.json`.

One period has3557 physical read orbits modulo(-78,-78), normal hull[-28,46],
charge+408,8476 bad ten-windows and7353 adjacent bad-ten defects. Complete
input histories on those read orbits start black on1439 classes and end black
on1847 classes. The independently checked minimum finite input for n periods
is1439n+101, for every n>=1. This growing input demand is supplied by the
previous nonstandard writer in the separate finite construction; it is not
created by treating an infinite prepared board as a finite seed.

The full bulk input is precisely the mature4352 output, including the old
standard black cells that4352 never read. On its own read-normal hull the
return wave does not use the exterior helper bands. Thus this is a genuinely
new stateful output-consumer interface, not another standard-wake consumer
and not one of the previously tested1564/4352 pairings.

## Exact all-future certificate

`certify4352_output_return_wave.py` reconstructs the complete source-end board
and literally executes the142764 transition. For a return read q, write
q=c+k(-78,-78) with c=(a,a-t),0<=a<78. At cell index n, a period-slot at k is
eligible exactly when k<=n; chronological order is decreasing k, then the
literal slot index. Every such full orbit has alternating turns.

Before all slots are eligible, the finitely many boundary indices are checked
individually. Afterwards the required first color is fixed. The initial
board's color on that ray changes only at its exact upper-ray thresholds or
finite-XOR exceptions. Evaluating those transition indices and adjacent
integers proves every future read, with no repetition cutoff. The author
certificate has3763 complete color tests, two full literal return periods,
and one far active-color flip on EACH of the3557 physical orbits, all rejected.

The independent checker reconstructs the field without author imports, runs
7320 critical tests and all3557 far flips, and verifies the primitive word,
input demand and counts. Its artifacts are
`audits/check_4352_output_return_wave_independent.py/json`.

No infinite nonstandard trajectory from one finite seed, profile renewal,
third phase, or universal-capture conclusion is implied by this prepared
all-future statement.
