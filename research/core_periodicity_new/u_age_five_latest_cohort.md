# Age-five latest-clock U inputs form one producer cohort

23 October 2026 11:09 UTC. Independently signed LN cohort theorem, 11:13 UTC.
Scope: complete recurrent-eight factors, lower q produced with C age exactly5,
and other lower input a of age at least5 or retained from entry. No source
template below is claimed physically attained; no new single-slot minimum,
funding-record exclusion or finite global budget is asserted.

Normalize the U/UC/UCC consumer to (0,0,N). Labels are
a=(-1,1), q=(-1,2), b=(-1,4), c=(0,2), d=(0,3). KV makes all three upper
ages at least5, so every one of the five input identities has age>=5 under
the stated extra hypothesis on a. Entry ages are infinity.

Let S be the nonempty subset with exact age5; q belongs to S. All its source
packet starts have one C clock, and heading E relative to the consumer. The
other inputs have age>5/infinity and are already current before that clock.
Between consecutive births in S there can be NO C packet. Every earlier
producer of a proper partial S-cohort must itself have zero C. All actual
intermediate packets are therefore D/V/U at heading E, whose endpoint
displacements are (1,-1), (3,-1), (4,0), respectively.

The precise zero-C endpoint condition from exit p to next birth pose t is:
write dx=t.x-p.x and ny=p.y-t.y. There must be nonnegative integers d,v,u
with ny=d+v and dx=d+3v+4u. Equivalently dx,ny>=0 and some integer
0<=v<=ny has dx-ny-2v a nonnegative multiple of4. This accounts for arbitrary
zero-C word length; no packet-depth or spatial cutoff is used. Intermediate
literal guards are ignored, conservatively permitting extra histories.

## Complete finite birth-subset certificate

There are exactly103 sector-compatible retained producer placements of at
least one of the five input cells at heading E. At each relevant birth:

- Its complete entry context must avoid every older/current final identity.
- Its outputs must contain the nonempty subset assigned this birth.
- Unassigned outputs may be ignored and later retired, so there is no hidden
  assumption that every output in an input cell is its final identity.
- Unless this completes S, the producer is zero-C and must be endpoint-
  compatible with the next birth by the exact condition above.

For each of the16 possible older subsets not containing q, the checker closes
the entire finite DAG with state (already-current subset, last producer,
number of relevant birth packets). Every edge adds at least one of just five
final identities, so at most five stages is a consequence, not a cutoff.
The103 placements give257 states and289 arcs across these16 DAGs. Only eight
states complete all five inputs. EVERY completion uses exactly ONE producer.
Thus ALL exact-age5 inputs are born together, rather than in different
zero-C-separated packets at the same C clock.

The complete necessary list, with all source headings E, is:

1. a strictly older; S={q,b,c,d}, source U/UC/UCC at(-1,4).
2. b,d strictly older; S={a,q,c}, source V/VC/VCC at(-1,2).
3. b,c,d strictly older; S={a,q}, source VCC at(-7,2) or UCC at(-8,1).

These are eight packet/pose templates. They hold uniformly for U, UC and UCC
consumers because this proof uses their common input shape, KV upper ages,
actual heading chronology and retained producer geometry, not the consumer's
later C suffix. In particular, if a>5 then all four other inputs necessarily
form the first U-family cohort; they cannot have been supplied by separate
same-clock helpers. If a=5, only the latter two cases remain.

## Exact scope and limitations

The finite graph is an overapproximation: unobserved zero-C path colors,
inputs, output multiplicities and old unused identities are not checked.
Its completeness as a necessary abstraction follows by retaining the actual
birth packet for each final input and forgetting only those constraints. An
empty/multi-stage-free graph therefore gives the stated necessity; its
surviving states do not give actual packet words.

In the strict U1 normalization, all eight source created-peak values are
below30: the first family's values are22,22,2; the second's18,18,-2; the last
two10,10. Hence this particular record-score intersection removes none.
The stronger FULL entry-core-plus-creation filter is treated in the later
signed `u1_minimum_clock_cohort_by_phase.md`: it leaves only the second family.
Low creation does not imply a low entry-core value.
The a<5 and q>5 branches remain outside this theorem. Neither exact-age5
attainability nor a finite ancestry, U, reconvergence-rank or C budget follows.
