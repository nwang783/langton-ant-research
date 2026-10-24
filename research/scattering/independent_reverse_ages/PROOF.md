# Independent ages in the exceptional two-reversal parent

Status: exact geometry and XOR checks pass; independent analytic review is
requested. This is a corollary of the already audited rectangle color proof,
not a new sampled two-parameter color extrapolation.

For any INDEPENDENT integers m,n>=200, start north at zero with exactly

    q_m=(-33-2m,-14-2m), a_n=(-33-2n,41+2n).

Then the first q_m read is104m+10881; the first a_n read is
208m+104n+71330. The full future is the standard SE highway by

    208m+208n+146040, at (40,-50), south, standard phase100.

## Exact stabilization of the complete one-bit parent

Let F_i be the ENTIRE black field of the one-bit input {q_i} at time
208i+70733. The audited parent certificate places its ant at (-15,26), east.
The new checker proves, for every i>=200, that

    F_i restricted to {z>=-250} = one fixed 2442-cell set S.

It constructs F_i from the complete initial bit and every odd write in the
already certified first five segments. No cells are discarded before the
restriction is proved. Parameter-dependent finite points are either uniformly
below the region or constant. For each finite period ray, the inequality
z>=-250 clips its epoch interval exactly. After reindexing, both endpoints
and the complete surviving point sequence are constant in i. XORing all these
restricted components gives S, with a fixed digest in interface.json. This is
an equality on the WHOLE infinite half-plane, not a box comparison.

The same prefix calculation gives u>=-82 for every read before this boundary.
Since u(a_n)=-74-4n<-82 for n>=200, preinstalling a_n cannot alter the q_m prefix.

## Coupling two genuinely different complete histories

Compare the actual state for {q_m,a_n} at time208m+70733 with the audited state
for {q_n,a_n} at time208n+70733. Their poses agree. Their complete fields may
differ greatly, but their restrictions to z>=-250 agree exactly: both are
S XOR {a_n} there.

Every future read of the audited two-bit parent lies in z>=-93. The checker
verifies that bound on every finite segment, every parameterized period and
the final infinite SE tail. First-difference coupling therefore makes the two
futures identical, with time offset208(m-n). This proves the displayed capture
time and first-contact formula. It uses neither m<=n nor n<=m.

The initially exceptional phase72 core on the blank SW ray corresponds to
q_m at blank-front age m+8. Thus this is the missing exceptional-core analogue
of the21 ordinary-core/remote-phase72 families in the adjacent packages.
Together they give all22 fresh classes with sufficiently mature independent
ages. They do not give arbitrary finite-cluster stability, account for three
additional remote scatterers, or by themselves exclude mass-five recurrence.

Run certify_interface.py. Its source template and previously audited color
certificate are both pinned by SHA256. The new code only proves the exact
restriction identity and read-region bounds required for the analytic coupling.

The pinned source color certificate explicitly contains the eternal parents in
segments[4].one_bit_infinite_tail and segments[8].two_bit_infinite_tail. The new
checker asserts both embedded records, including their exact drifts/headings.
