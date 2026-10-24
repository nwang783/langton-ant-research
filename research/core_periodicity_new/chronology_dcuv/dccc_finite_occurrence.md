# DCCC is finite in a finite-support DCUV packet tail

Status: independently SIGNED, 2026-10-23 02:07 UTC. Audit artifact: audits/dcuv_dccc_fresh_independent.json.

Consider any context-complete factor of the ten packet types D, DC, DCC, DCCC, V, VC, VCC, U, UC, UCC, starting with m black cells. Its entry core has five cells, so there are m−5 initial residual identities. Maintain identities by removing all packet input identities and then installing a fresh identity at every output. This is essential even on the U-family recycled input/output cell.

DCCC has one residual input. If this input were supplied by an earlier output identity, the signed complete-context identity gives full protection across all strict intermediate packets. Rotate the producer's pose to heading zero. An output q of type a and the input z of DCCC at relative heading h determine the consumer displacement uniquely as q−R_h z. All340 alignments are enumerated by dccc_fresh_query.json. Exactly170 violate the invariant checkerboard sector x+y+h ≡ 0 mod2, and all170 compatible alignments belong to HB's signed ordinary forbidden relation. Thus no earlier packet output can supply this input.

Consequently every DCCC consumes an initial residual identity. An identity is consumed only once, even if its physical cell is later recolored. There are at most m−5 DCCC packets in the factor. The same bound applies to every prefix of an infinite context-complete packet tail, so DCCC occurs finitely often there.

After the last DCCC one may restart with its remaining black debris included in the new finite initial configuration. The remaining packet alphabet has nine types, retaining DCC. This does not assert that any of the198 D/C/V-only transfer clauses is valid across U-family intermediates, and it does not yet exclude an infinite DCUV tail.
