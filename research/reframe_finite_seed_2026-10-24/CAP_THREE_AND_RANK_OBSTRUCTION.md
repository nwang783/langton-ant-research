# A complete cap-three exit rank, and an exact cap-four obstruction

24 October2026. Author finite certificate; independent audit requested. This
is a small-active-component theorem and a falsified ranking class, not capture.

## 1. Exact finite local kernel

At each cut normalize the actual physical head to(0,0),N by translation and
quarter rotation. The entire w-black active component becomes a connected edge
set rooted at w=(1/2,-1/2). Enumerate every such set of at most M edges. The
complete enumeration starts from empty and repeatedly adds any edge incident
to any existing vertex or the root. Every finite connected rooted edge set has
an edge ordering of this form (a rooted spanning tree first, remaining edges
last), so induction gives completeness. No radius bound or random sampling is
used. Rooted counts at masses0,...,5 are1,4,18,88,439,2224.

At an L remove the actual current edge, cross it, retain the arrival component,
and emit the other component if nonempty. At an R either attach an isolated
vertex, close a cycle, or import a whole connected component D rooted at the
other endpoint. Enumerate all D with |C|+|D|+1<=M whose vertices are disjoint
from C and w. This is precisely every R import that can preserve the cap.
The full joined field C union D is used for the literal transition. Any other
background components are unchanged and cannot affect this one step.

Normalize the new active component/pose again. Passive module types are
rootless edge graphs modulo translation and quarter rotation, NOT reflection.
This retains the two possible diagonal edge embeddings through an explicit
w-lattice graph, rather than classifying physical midpoint sets alone.

Thus every physical update whose entry AND exit active masses are<=M appears
in the finite kernel, on finite or infinite initial backgrounds. Imported or
emitted components are complete, not selected marker subsets. An infinite
component cannot be imported while preserving a finite cap.

## 2. Cap-three theorem

For M=3 the kernel has111 active states and80 cap-preserving transitions.
The JSON component_kernel_M3.json assigns to every active state a nonnegative
INTEGER rank A(C), between0 and9. Every listed transition satisfies

    A(C_after) <= A(C_before)-1.

All passive-component weights found during the search are ZERO. Therefore the
rank does not count or assume anything about the exterior archive at all.
The discovery LP is not a proof dependency: the final integer inequalities,
complete state list, complete transition generation and geometric normalization
are checkable with exact integers only.

Consequently, starting at ANY cut with active w mass<=3, at least one of the
next10 updates leaves an active component of mass>=4 (or infinite). Equivalently
there are never11 consecutive physical cuts all with active mass<=3.

Indeed,10 consecutive cap-preserving updates would lower a rank initially<=9
below zero. No finite-support assumption is needed for this small-cap result.
For a finite-support ant this in particular gives infinitely many active-mass
>=4 cuts. This does NOT prove eventual mass>=4, eventual active mass>=4, any
larger sustained lower bound, or standard104 capture. No optimality of10 is
claimed here.

## 3. The first additive-resource extension fails exactly

For M=4 the same complete kernel has550 active states,10 passive graph types,
and432 cap-preserving transitions. Consider any proposed rank

    A(active normalized shape) + sum_{dormant components D} W(type(D)),

where all W are nonnegative and every legal kernel transition is required to
lower the rank strictly. This entire ranking class is impossible, even allowing
arbitrary real coefficients and arbitrary values for the finitely many A.

The obstruction is not a solver timeout or merely numerical infeasibility.
The file kernel_M4_rank_obstruction.json provides an EXACT five-transition
closed active-state walk, each with integer multiplicity1. Its turn word is
RRRRL. It starts with an empty active component, grows the four-edge star, and
deletes the first edge, returning to the EMPTY normalized active shape. It
consumes no dormant module and emits one three-edge star. Summing the putative
strict inequalities would require W(star)<0, contradiction.

Without quotienting headings by rotation, concatenate the four rotated copies:
the same obstruction has20 steps, restored heading and zero displacement. The
four emissions still have nonnegative total weight.

Each one-step local transition, and the first five-step block, is physically
legal. But repeatedly using that closed kernel walk is NOT a real trajectory:
the ignored emitted star causes the blank ant's first actual R import at update8.
That import makes its active component larger than four. This is the mandatory
zero-drift regression already checked in the independently audited flight
operator. The resource-relaxed loop supplies NO counterexample and NO reusable
physical writer.

## 4. Exact next obligation

The cap-four failure identifies a concrete missing state variable: emitted
module POSITIONS relative to the real head, not a larger scalar penalty for
module counts. Any successful next rank or simulation must at least distinguish
the fresh three-edge star left by RRRRL and the actual R endpoint that reattaches
it three updates later. A rule that simply discards it, or keeps only its type
count, cannot enforce that collision.

One bounded candidate is to retain the most recently detached COMPLETE component
with its relative coordinates until actual reimport or an explicitly charged
forgetting event. Its frozen state and contact geometry are physical, not a
permitted teleportation or external reset. Whether such finite chronological
memory suffices even at cap four is OPEN; no enhanced rank is supplied here.

## 5. Reproduction and status

component_kernel.py constructs all states, all cap-preserving local transitions,
and the candidate rank. component_kernel_M3.json contains the integer rank and
every literal transition. kernel_rank_obstruction.py reconstructs the exact
nonnegative circulation; kernel_M4_rank_obstruction.json contains its five
physical transition rows. The scipy LP calls are discovery tools. The integer
rank and circulation equations, plus complete enumeration, are the certificates.

The independent active-flight theorem remains separately signed, with its
mandatory lifetime-metadata clarification. These additional cap-three and
cap-four conclusions are new AUTHOR results pending independent audit.
