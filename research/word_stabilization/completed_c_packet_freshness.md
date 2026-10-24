# Completed-C packet freshness by spatial-pair descent

Status: independently audited complete proof and finite certificate. The
separate literal-word/complex-coordinate checker verifies all40,510 clauses,
303,989 neighbor obligations,8,085,376 reader obligations, and all6,656 marked
input alignments. See ../audits/check_spatial_packets_independent.py and
../audits/spatial_packets_independent.json.

## Precise domain and proposed theorem

A packet is A C^k, where A is U,V,Q, or B and k is0,1, or2. A packet factor is
right-extendible here in the following specific sense: whenever a packet has
k>0, its next packet begins with V; if the last packet has k>0, an actual
following V macro is also part of the assumed feasible continuation.

This is only a finite right-extension requirement, not an assumption that an
entire infinite trajectory already exists. By the audited C-gap grammar,
every right-infinite feasible five-macro word, after restarting at a non-C,
has this packet form. Every factor of whole packets inherits the same right
extension at its right boundary, even if its final packet ends inside a larger
finite word.

Claim: the FIRST C's phase1 input in every k>0 packet is unread in all previous
packets of the factor. Its preceding A inside its own packet does not read it
either. Thus it is genuinely first read at that C, relative to the factor cut.
No claim is made about an uncompleted terminal C-run without the required V.

## Coordinates and exact finite data

The12 packet labels are:

    a=U, b=UC, c=UCC, d=V, e=VC, f=VCC,
    g=Q, h=QC, i=QCC, j=B, k=BC, l=BCC.

Normalize an earlier packet to origin with heading N. Later packet headings
range over ALL four orientations. Their positions satisfy x+y-h even, the
elementary turn-and-move parity invariant. No stronger C-free lattice is used.

There are42,211 overlapping-footprint pair types under this conservative
parity condition. Complete checks of all packet pairs and triples, including
the required final V when the later packet ends C, eliminate55 types realized
at macro-packet gap1 or2. A simultaneous forbidden-pair kernel contains40,508
of the remaining types. Its clauses are neighbor descent or equal-read
separation, exactly as in cfree_spatial_pair_theorem.md, with packet types in
place of single macros. All motions and read footprints are literal packet
concatenations. No marked-site freshness assumption is used.

For every proposed marked first-C input, enumerate all earlier packet poses
whose footprint reads that point. Exactly TWO alignments are not already in
the40,508-family:

    earlier U, later VC at(-1,5,S);
    earlier V, later VC at(0,4,S).

## The two forced-extension barriers

The later packet is VC in both cases. Its required next V is real, by the
domain condition. Include that next V only in the LATER read template.

- Earlier U at(0,0,N), later VCV at(-1,5,S): physical(0,1) has last read R in
  the source U and first read R in the whole later VCV template.
- Earlier V at(0,0,N), later VCV at(0,4,S): physical(0,0) has last read R in
  the source V and first read R in the whole later VCV template.

For each barrier cell, enumerate all packet types, headings, and literal read
offsets that could give an intermediate reader. There are832 possibilities
per cell. Each creates a forbidden proper subpair with the source or target
in the augmented family. The exact counts are machine-checked in the saved
certificate; no spatial cutoff or lookahead bound is used.

The required next V does not change the later packet's entry position,
endpoint motion, or packet index. Before the template's FIRST read of the
barrier, the rest of that packet and the prefix of its following V have no
read of the barrier by definition. Thus no reader is omitted: after the
source packet, a possible earlier read must be in one of the strictly
intermediate packets, all of which are enumerated.

## All-length induction

Add these two clauses to obtain a40,510-pair family. Select a forbidden-pair
occurrence with smallest positive packet-index gap. All gap1/2 realizations
are excluded by the complete literal controls with inherited right extension.
For gap>=3, a neighbor clause yields a strictly smaller forbidden subpair.
An equal-read clause excludes every intermediate reader by the same
minimality, leaving two equal consecutive read letters at one physical cell.
The two extension clauses use precisely the same argument with their real
forced V included in the later template. This is impossible under flip-after-
read dynamics. All proper packet factors inherit the right-extension premise.

The completed family excludes every earlier-footprint alignment with a
marked first-C input, proving the stated freshness. The preceding A's marker
positions in its own frame are U(-1,4), V(0,3), Q(-3,-4), B(-2,-5), none read
by A. Therefore each positive-C packet spends a different black cell present
at the factor's entry.

## Finite-support consequence

On an entry board with m black cells, at most m packets can have positive C
suffixes. Thus there are finitely many C macros in any purported infinite
finite-support five-macro tail. The remaining C-free infinite suffix is
impossible by the exact C-free finite-fuel theorem. Therefore no such infinite
five-macro tail exists.

This is not by itself the full highway conjecture: arbitrary recurrence of
bad ten-windows remains a separate global obligation.

## Artifacts

- spatial_packet_kernel.py/json/log: discovery of the40,508-family.
- certify_packet_goal_extension.py: the two extended equal-read checks.
- spatial_packet_kernel_complete.json: augmented40,510-family.
- probe_packet_goal_extension.py: diagnostic enumeration of candidate barriers.
