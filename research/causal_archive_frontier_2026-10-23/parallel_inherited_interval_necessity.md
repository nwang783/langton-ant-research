# Long post-entry epochs require a growing inherited parallel interval

23 October2026,20:06 UTC. Analytic frontier consequence for review. This proves
an actual inherited-spatial-resource necessity, not a monotone rank and not a
periodic or fixed-width profile theorem.

## 1. The epoch-entry resource is concrete and chronological

Work in an actual U-entry complete-eight factor. Fix one consumer epoch with
full-entry C clock j, heading h, and N packet starts. Normalize the consumer
heading toN and use its physical progress coordinate

    z(q)=q_x+q_y.

Every packet start has one fixed z parity and successive starts increase z
by2 or4. Choose the signed distinguished input convention:

    D/DC: (0,1),
    V/VC: (1,2),
    VCC/U/UC/UCC: (0,3).

Its progress offset d_b is respectively1 or3. By the signed zero-C fuel theorem,
every input consumed during this epoch was already current at epoch entry.
In particular these resources cannot be replenished by another packet inside
the same zero-C epoch, even when an old black cell is recycled with a fresh ID.

Remove the at most4851 packets receiving any perpendicular-source produced
input, by the signed perpendicular-epoch theorem. Also remove packets consuming
an untouched entry identity; there are at most r0 such packets even over the
whole factor, and NONE in an epoch j>20R+211. Call the remaining packets good.
Every input of each good packet is produced in-factor by a parallel or
antiparallel source epoch of even age2,4,...,294. There are at most147 such
source clocks.

For each source clock a used by a good packet's distinguished input, let Q_a
be the set of the EXACT epoch-entry identities actually consumed in that
selected role by these good packets. These are genuine used cells, not dormant
islands or a count of static roots. Put

    lo_a=min_(q in Q_a) z(q),
    hi_a=max_(q in Q_a) z(q),
    ell_a=(hi_a-lo_a)/2.

All these selected-input cell progresses have the same parity, because both
possible offsets1 and3 are odd and all consumer-start progresses have fixed
parity. Hence ell_a is a nonnegative integer.

## 2. Exact inherited-interval inequality

If a good consumer uses q from Q_a in its distinguished slot, then

    z(p_consumer)=z(q)-d_b,       d_b in{1,3}.

Thus its start progress lies in[lo_a-3,hi_a-1]. This interval has span2ell_a+2
and its endpoints have the correct start parity, so it contains exactly
ell_a+2 possible start progresses. The epoch's strict progress makes its
packet starts distinct. Therefore source cohort a can fund at most ell_a+2
good packet starts in this selected role.

Let k<=147 be the number of nonempty used cohorts. Summing actual funding
assignments gives the following necessary inequality for EVERY epoch:

    N <= 4851+r0 + sum_(a used)(ell_a+2).

After the entry-input expiration horizon, it sharpens to

    N <= 4851 +2k + sum_a ell_a
      <= 5145 + sum_a ell_a.                             (1)

Consequently some GENUINELY USED parallel/antiparallel young cohort obeys

    ell_a >= max(0,ceil((N-4851)/147)-2)

whenever N>4851. In particular, an unbounded sequence of post-entry zero-C
epoch lengths requires unbounded inherited progress interval in at least one
of the finitely many recent parallel cohorts. Such a cohort also has physical
L-infinity diameter at least ell_a, since |z(q)-z(q')|<=2||q-q'||_infinity.

This is not a token-count-only assertion: even an arbitrarily large number of
cells squeezed into bounded progress ranges cannot fund arbitrarily many
strictly advancing packet starts.

## 3. A computable prospective interval certificate

The used sets Q_a are an exact ex-post statement. For an effective upper bound
at epoch entry, use instead EVERY currently live produced identity with:

- source clock a in the147 possible even-age cohorts;
- source heading parallel/antiparallel to h;
- physical progress parity opposite the consumer-start parity.

For each nonempty such cohort take its min/max progress interval. These live
intervals contain the actual Q_a and give an online upper certificate in(1).
They are computed from the signed330-context frontier; no older archive or
unbounded past path must be restored. Independently certified permanent IDs,
such as U left-star outputs, may be omitted from the prospective set, but this
refinement is not needed for the proof.

The prospective certificate can overestimate actual fuel, because lateral
geometry, protected siblings, other inputs, or historical colors can prevent
a nominal cell from being used. The USED-cohort formulation in Section2 is
the physically genuine necessary resource.

## 4. The interval is inherited from a long source epoch

For a parallel source heading, the selected input's physical parity forces
its source output to have odd local progress. The literal output progresses
among odd slots lie in{1,3,5,7}. For antiparallel heading their consumer-frame
values lie in{-7,-5,-3,-1}. Thus the output-offset range within one source
epoch is at most6.

If Q_a has progress span2ell_a, the actual SOURCE HEAD STARTS that produced
its endpoint identities must have progress span at least2ell_a-6. Accordingly
the source epoch's half-progress span is at least ell_a-3. Since its zero-C
head starts advance by2 or4, a growing used interval forces growing length
of an actual recent source epoch as well. This is an inherited transport
requirement, not a supply invented by forgetting other contexts.

## 5. Why the all-N young rail does not answer the post-entry case

In the signed family UCC,V^N,VCC,V^(N-1), the return consumes old age-two outputs
in V input(0,3). But its distinguished V input(1,2) is the untouched entry root
(-k,3-3k). Every returning V is therefore an entry-funded exception, precisely
what is removed before(1) is applied. The family gives real unbounded young
reuse, but not an autonomous post-entry source of selected funding.

## 6. Remaining gap

Equation(1) is not a well-founded rank. The young parallel intervals may have
been produced by earlier long epochs; their widths can change, split among
cohorts, and renew. The inequality permits this and does not say that total
interval span decreases. There is no bound on that inherited span independent
of the unbounded global C clock, and the signed growing frontier remains
O(r0*j), not uniform.

Closing the post-entry problem therefore requires an additional theorem about
parallel interval transport: a strict nonrenewable cost, a simultaneous
producer/context obstruction, or a corridor transducer whose evolving
length/width is itself controlled. No complete periodic-profile clock applies
without first proving its missing full periodic bulk-interface hypotheses.
