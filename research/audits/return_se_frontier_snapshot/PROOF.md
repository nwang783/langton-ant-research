# Retained cores on the southeast return beside an older northwest rail

Status: exact strip interface,22 local certificates, and13 finite three-cell
transfers completed. Independent audit pending. The ten sparse-recurrence
exclusions below use the already audited global incidence lemmas.

## 1. Complete finite inputs and the uniform interface

Use u=x-y,z=x+y and headings N,E,S,W=0,1,2,3. Let p_r be the phase-r
pre-update read position of canonical W, starting at0 with headingS.
For each of the22 fresh phases r, put

    q_n=(-33-2n,-14-2n), a_n=(-33-2n,41+2n),
    A=(-62,2), O=A+m(-2,2), s=O+p_r.

The input is exactly {q_n,a_n,s}, head0,N. There are no dynamically
installed bits and no suppressed portions of the history. Assume

    m>=100, k=n-m>=100.

At time T=416n-104m+122376, the head is O,S. The retained bit s has
not yet been read. In source coordinates relative to O, the complete
finite field without s agrees on the ENTIRE infinite strip |u|<=200
with the explicit infinite field

    C_infinity XOR T_old,
    C_infinity = P union {d-j(2,-2): d in D, j>=1},
    T_old = {(47,27)-d+j(-2,2): d in D, j in Z}.

Here P and D are the canonical13-cell active core and12-cell deposit.
The core toggle p_r is then added to both fields. This identity is
uniform in m and k and in all z; it is not a finite window comparison.

The old rectangle certificate supplies the color-valid prefix through
segment6 and the first k periods of segment7. The new checker explicitly
verifies that the omitted c_n,d_n bits and all22 proposed cores are unread
on that prefix. Freshness for every earlier SE period follows by exact
phase/drift incidence. It constructs the full finite field by XORing
all prefix writes, without deleting any archive.

It then XORs the proposed infinite model. Terms whose entire u support
lies outside[-200,200] are excluded by coefficientwise inequalities in
m-100 and k-100. Every remaining term is an interval in a full-SE-drift
translation class, indexed by(z,x modulo2). Clipping that interval to
the strip has exact integer endpoints. The XOR of all endpoint sets is
empty in every class. This proves the field identity for every parameter
value, including any non-generic coincidences among terms.

The discarded center history is on the high-u side; the remote a-history
is on the low-u side. Both remain present outside the strip. A negative
control at NE depth10^60 lies inside the strip and is detected, showing
that the proof does not truncate its unbounded z direction.

Source: certify_strip_interface.py, strip_interface.json.

## 2. Exact local outcomes and finite transfer

certify_parallel_model.py independently replays all22 local words on the
explicit infinite field, compares optimized and literal background parity
on every read, and verifies each entire infinite standard104-tail by
exact interval XOR. Every finite recovery read has |u|<=200.

Thirteen outputs also keep every infinite tail read inside that strip:

    SW:29,32,38,55,56,62,71;
    NE:15,45,46,47,57,72.

Consequently all thirteen are permanent standard-highway theorems for
the COMPLETE finite three-cell inputs above. If tau_r and(p_r_out,h_r)
are the recorded local checkpoint data, the finite theorem's checkpoint is

    time T+tau_r,
    pose O+p_r_out, h_r.

The exact values, phases, words and hashes are in
parallel_model_certificate.json. No earliest-onset claim is made.

The other nine outputs are SE:

    13,14,27,28,60,61,70,75,89.

Their finite recoveries transfer, but their tails eventually leave the
strip toward the preserved central archive. The infinite-model tail
certificate alone therefore makes NO permanent finite-seed assertion for
these nine classes. This is an explicit composition boundary.

Six recoveries actually cross the older parallel rail. In particular,
phase72 is redirected into a NE standard output rather than following
the isolated one-toggle exceptional return. Thus the older rail is part
of the mechanism, not an omitted harmless backdrop.

## 3. Ten immediate retained-mass-five exclusions

The entire pre-core prefix has u<=58,z<=71. After insertion of the local
recovery, the complete finite prefix still has u<=58,z<=82. The outgoing
canonical core also has z<=82. Hence, for every NE case, the COMPLETE
stationary archive after removing the outgoing canonical clean core has
z<=82, independently of n. No historical field has been discarded.
The exact canonical-core and sector calculations are in
certify_mass5_interfaces.py and mass5_interfaces.json.

Consider the established recurrent mass-five incidence shapes with fixed
m and n tending to infinity. Before s is reached, the original blank and
q_n parents ignore it: its u is below the blank/central-history range and
its z belongs to[-63,-53], outside q's first NW passage. An ordinary a-hit
captures by the diverging half-plane gap. Thus the only relevant a is the
old exceptional a_n, which leads to the interface just proved.

In either four-edge shape, any other remote marker is eventually outside
the old D82 parent trace and the bounded-u post-core output. In the cycle,
c has u tending to positive infinity and d has z tending to positive
infinity. Therefore a SW output never meets either remaining marker.
This excludes the seven SW phases outright.

For NE phases46,47,57, the outgoing phase72 exceptional ray has coordinate
parity(odd,even), while the possible opposite corner d has parity(even,odd).
So d can only interrupt in one of the favorable nine ordinary channels.
The invariant x+y+h modulo2 is0; at a phase-zero NE head h=E and z is odd.
A d of odd z therefore has an even fresh phase, exactly one of the ten
favorable fresh phases, with72 excluded by the finer coordinate parity.

The favorable ordinary continuation has z>=z(d)-58. Since z(d) tends to
infinity, it misses the whole archive z<=82. It also misses a and c by
the two diverging side gaps. The existing all-age ordinary theorem
protects the current NE wake itself. This excludes those three phases.

Thus the following ten complete retained-core rays are excluded for fixed
m>=100, under the established global mass-five incidence hypotheses:

    29,32,38,46,47,55,56,57,62,71.

The three NE phases15,45,72 have compatible exceptional opposite rays and
remain open here. The nine SE outputs also require the central-archive
return to be analyzed. The thirteen three-cell capture theorems must not
be confused with thirteen full five-cell recurrence exclusions.
