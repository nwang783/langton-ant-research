# Fixed-heading projection sharpens finite-C duration to quadratic

Status: proposed on 2026-10-23 07:54 UTC; independent review pending. The root-box premise is the independently reviewed geometric genealogy theorem in dcuv_c_age_spatial_cubic_bound.md. This strengthens its duration corollary, not its scope or any confinement conclusion.

Consider the same finite context-complete recurrent-eight factor, entry mass m>=5, entry residual mass r0=m-5, total C count k and raw duration L. Its current residual support at cumulative C count j lies within the union of L-infinity boxes of radius j+4 about the r0 entry residual cells.

Partition into epochs of zero-C packets followed by the next positive-C packet, or a final zero-C suffix. All packets before an epoch's terminal packet have zero C and therefore preserve the heading. Thus EVERY packet start in the epoch has the same heading h. The terminal packet may change it only after its own start.

Let p_h(z) be the coordinate sum of the point z after rotating by inverse heading h. For D,V,U zero-C packets, the change in this progress coordinate is respectively2,4,4. The packet-start progress values throughout an epoch are consequently strictly increasing and have one fixed parity, including the terminal positive-C packet's start. No assertion about the terminal packet's own progress displacement is needed.

Every consumed residual input identity in an epoch is an epoch-entry identity, by the signed zero-C fuel argument: an intra-epoch producer would have pre-consumer C age0 even at the final packet, contrary to JO. At epoch-entry C count j, each such input is therefore within distance j+4 of SOME original entry residual root. Its progress differs from the root's by at most2j+8.

Use the distinguished input of the genealogy table for each packet. Its source-relative progress is1 for D/DC, and3 for V/VC/VCC/U/UC/UCC. Hence the packet's start progress lies in

[p_h(root)-2j-11, p_h(root)+2j+7].

This integer interval has span4j+18 and therefore contains at most2j+10 integers of any one parity. The strict increase of packet-start progress implies that the number N_epoch of packets in the epoch is at most

N_epoch <= r0*(2j+10).

Union bounds are harmless even if root intervals overlap, and roots may be arbitrarily far apart. This argument counts packet starts, not every raw intermediate head position.

The literal packet lengths satisfy length<=28+15*c, where c is that packet's C count. Consequently

epoch duration <=28*r0*(2j+10)+15*c_epoch.

Epoch-entry C counts form a subset of {0,...,k}, with no repetitions. Summing over the larger full set and using total C count k gives

L <=28*r0*sum_{j=0}^k (2j+10)+15*k
  =28*(m-5)*(k+1)*(k+10)+15*k.

This is a diameter-free quadratic-C bound for complete recurrent-eight factors. In particular, fixing the finite entry mass, an infinite such tail would need C count at least of square-root order in elapsed raw time. It does NOT upper-bound C count, exclude DCUV, supply joint U freshness, cover arbitrary raw boundary factors, or prove universal standard104 capture.
