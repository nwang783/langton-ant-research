# Expansive fixed affine identities cannot have periodic ant tails

2026-10-23 01:18 UTC. Independently analytically signed as audit GT. No finite-support
assumption is needed. No existence of such an ant is asserted.

Let an actual classical-ant path satisfy, for all sufficiently large n,

    p(kn+c)=A p(n)+d,

where k>=2 and c are integers, d is constant, and A is an expansive real
2x2 matrix. Then its movement sequence is not eventually periodic.

Suppose otherwise. An eventually periodic movement sequence gives

    p(n)=n v+w(n)

at all sufficiently large integers, where v is constant and w is bounded
(indeed eventually periodic). Dividing the affine identity by n and taking
limits gives A v=k v. Substitution then gives

    w(kn+c)=A w(n)+d-c v.

Because 1 is not an eigenvalue of A, define

    z=(I-A)^(-1)(d-c v),       q(n)=w(n)-z.

Thus q(kn+c)=A q(n). Choose n large enough that all iterates of f(n)=kn+c
stay in the identity domain and tend to infinity. For every r>=0,

    q(n)=A^(-r) q(f^r(n)).

The second factor is bounded uniformly and A^(-r) tends to zero. Therefore
q(n)=0 at every sufficiently large n. This means p(n)=n v+z eventually,
so every late movement equals v. Actual ant movements are unit vectors
whose axes alternate at every step. They cannot be constant. Contradiction.

This removes the former sufficient spectral restriction rho(A)<k for
proving aperiodicity of an ACTUAL fixed-affine model. A finite-support model
of this exact kind, if one were constructed, would automatically contradict
eventual highway capture.

The fixed aligned offset is essential. This argument does not cover
p(kn+c)=A p(n)+b(S(n)) with a state-dependent offset, arbitrary directive
limits without a same-path identity, or a position recurrence imposed only
on a sparse subsequence. In particular it does not contradict the signed
standard104 accepting matrix control, whose phase-dependent offsets are
nonconstant: see check_matrix_standard_positive.py/json and audit FS.
