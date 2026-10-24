# Finite-order powering for general finite physical macro bases

2026-10-23 07:20 UTC. New separate adapter submitted for review. It depends on
the separately submitted general A=I macro solver, not merely the signed UNIT
adapter. No singular finite-power geometry or changing boundary map is claimed.

Each state has a finite nonempty physical base word with complete pose
(h_in,v,h_out). Check every image's literal base-word concatenation has the
same h_in,h_out and net A*v. Supply and verify an integer order p with A^p=I.
The root must lie on its actual first-letter cycle q. Compose m=lcm(p,q), then
REVALIDATE every powered image against its base pose at A=I, using the general
macro validator. Nonzero, non-unit and zero base displacements are all allowed.
There is no assumed subdivision of a recursive macro into one read.

The KK powering proof uses only additivity of complete displacements and
matching boundary headings, not unit length. Thus the depth-j physical macro
word has net A^j*v and fixed boundary headings. The common power is exact-I;
its prolongable root power-limit is the same cofinal selected limit. The
adapter calls the general A=I macro generated-cover/frame solver. A genuinely
inconsistent finite powered word may safely reject first, with a literal
initial-color conflict certificate. Size/algebra/recursion errors give UNKNOWN;
a transient first-letter root is unsupported, not negative.

`finite_order_macro_adapter.py/json` tests a multi-read zero-displacement
identity, a real two-state multi-read root cycle, a branching closed-pose macro,
and a NONZERO-displacement multi-read half-turn presentation. The latter bases
are the legal nine-read unit-pose words, but the recursive symbols remain full
multi-read macros. Its powered images have81 macro labels and729 physical reads;
the finite color conflict is reported literally. The positive cases return
the same exact three-cell prepared seed and are explicitly nongrowing. Invalid
orders/matrix types are rejected and a powered physical-size cap gives UNKNOWN.

This is a fixed finite-order presentation adapter only. It creates no renewable
builder, accepted growing finite-seed trajectory or global capture theorem.
