# A sealed live cohort forces a genuine component import

23 October 2026. Exact time-ordered all-input graph theorem and a literal
DC-to-U corollary. This is a finite conditional import criterion, not a
bound on general support recycling or on all U packets.

## General live-cut theorem

Use the historical incidence graph of `reconvergence_budget.md`. At a packet
boundary, let Q be one historical component and let P be its ENTIRE set of
current live residual identities. Suppose every identity in P survives
strictly until a later target packet T. Thus no strict-intermediate packet
consumes an identity of P. Retired historical identities are not live inputs.

Then Q cannot be touched by any strict-intermediate packet: if the first such
packet had an input in Q, that input would have to lie in P. Nor can an
outside packet create a Q-descended identity or join Q without taking a live
input from Q. Consequently P is still the entire live set of Q immediately
before T. This is an induction on the chronological strict-intermediate
packets and retains every input, not a chosen parent projection.

Suppose T consumes k>=1 members of P and a-k>=1 additional identities.
Every additional identity is in a historical component OTHER than Q. If
those additional inputs occupy g_out distinct components, then

    g(T)=1+g_out, 1<=g_out<=a-k,
    delta beta=a-1-g_out,
    component-merger units=g_out.

In particular T spends at least one genuine merger and adds at least k-1
reconvergence units. A collection of DISTINCT target events admitting such
certificates has size at most r0-1 in the whole factor, since historical
components merge at most r0-1 times. Multiple certificates for one target
must not be counted as separate merger events.

This theorem is not merely a root-label test: it requires an exact LIVE
cut, including dormant current archive identities. Stabilized root sets or
absence of recent reads do not establish the premise. An old same-component
archive outside P invalidates a certificate that lists only the new cohort.

## Literal DC-to-U corollary

Normalize the DC source as in `u_bulk_spare_mask_lemma.md`. Assume its component
has exactly its four fresh current outputs A,B,C,D immediately after the
source, with no other current same-component identity. Keep all four outputs
current until a U-family target consumes the three original spares B,C,D.

The exact mask lemma forces target head(3,-1,N) and input set

    {A=(2,0), B=(2,3), C=(3,1), D=(3,2), Z=(2,1)}.

Since A,B,C,D are the entire protected cohort, Z is in another historical
component. There are exactly TWO input components, so

    delta c=-1, delta beta=5-2=3.

Such sealed-cohort DC/U target events are at most r0-1. Neither Z's initial
root nor its identity needs to be new: it may be a produced helper output
inside the external component. This is an import of another HISTORICAL
component, not a fresh-initial-token rule.

There is also a literal identity-history obligation: Z=(2,1) lies in the
source DC's exit core at pose(1,2,W), and not among its residual outputs.
It must therefore enter the residual set as a fresh output of some strict
intermediate packet before it can be this target input. The signed ordered
ledger, not a color-only recoloring argument, is required here. No actual
supported path installing Z while preserving A,B,C,D is asserted.

## Why this does not finish a global budget

For completeness, current live mass is nondecreasing along historical
component descendants. A packet with a inputs and b outputs merges its g
input components, and the resulting live mass is their combined old live
mass plus b-a. The recurrent-eight values b-a are nonnegative:0 or3 for the
D family,4+3C for V/U families. Thus an old component never shrinks to a
smaller live archive after a merger or internal packet.

In particular a DC source whose entire postcomponent consists of its four
outputs had only one current identity in its component beforehand. Such
sealed sources are an early, restrictive case. Later components can retain
unconsumed archive identities beyond a new source's outputs. Those identities
may support arbitrary same-component reconvergence in the abstract model;
the import theorem does not bound that recycling. It gives a precise place
where an additional literal archive-exclusion theorem would be needed.

This is a conditional finite merger budget plus a local physical mask/history
obligation. It makes no universal capture, all-U import, or repeated-cleanup
exclusion claim. Independent review requested.
