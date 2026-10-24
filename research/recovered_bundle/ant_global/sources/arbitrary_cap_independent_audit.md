# Independent audit of the arbitrary-color cap theorem

21 October 2026. The statement audited is in
`../boundary/arbitrary_cap_third_row.md`. This audit checks the written
argument and gives a separate literal implementation. It is not external
peer review or proof-assistant verification.

## Conclusion

I find the all-color extension valid under its stated cap, endpoint, and
arrival-sector hypotheses. A stronger charge than the first draft is valid:

    K_C + 2D_0 >= Q.

Here D_0 is the number of white B upper corners that are not charged to a
zero-bridge top diamond. No penalty for positive-roof endpoints is needed.
The first draft's possible-collision bound was safe but weak. In fact the
charge map on unmarked black lower A events is injective.

## Exact assumptions retained

The entire finite segment stays at x+y<=0 and starts and ends at x+y<=-4.
The arrival sector gives horizontal arrivals on even rows. Consequently a
top event can only arrive E, read white, and depart S. Every visited top
cell is visited once and was initially white. Initially black top cells
are not visited. The theorem does not say that a black top read is allowed.

All initial colors below the top row are arbitrary. In particular, black
events at A can occur at initial rank zero; a proof that silently starts
every A cell white would be invalid. The argument below does not do that.

## Upper roofs and the nonnegative D term

A black A event with incoming S and outgoing E uses both available upper
ports. No white A event can then occur at that cell. Color alternation
rules out another black event. Thus it is the first and only visit to an
initially black cell. These are the H bridges.

Every maximal chain of top events and bridges is a complete roof, because
the complete segment starts and ends below C. A roof with k bridges has
k+1 top events and ends at a B cell displaced k sites from its first B
cell. A zero-bridge roof is a physical first return to the same B cell.
Its endpoints have opposite colors, and exactly one endpoint is a white
B upper corner. Its top cell identifies this charged corner uniquely.

With J_0 zero roofs, J_+ positive roofs, and

    rho = H-J_+ = sum_(positive roofs)(k-1),

we have M=J_0+J_++H, rho>=0, and

    D_0 = E_B-J_0 >=0,
    D   = E_B-M+2H = D_0+rho >=0.

## The charge map exists without fresh A colors

Let an unmarked black lower A_s event mean a black N-to-W event whose
neighboring B events are not among the D_0 uncharged white upper corners.
Every adjacent white B corner must therefore be the charged corner of a
zero roof. An incoming white corner must be its roof's second endpoint;
an outgoing white corner must be its roof's first endpoint. The other
adjacent B possibilities are direct black events.

Thus the chosen A event lies in a literal C_(s-1) first return. This return
has a right zero roof, a left zero roof, both, or neither. It contains no C
event in its interior. Its endpoint colors are opposite. Exactly one
endpoint is a black C upper corner. This defines the charge.

At most two Q vertices are marked by each uncharged white B upper corner.
The number of unmarked events is at least Q-2D_0. Events on different A
cells charge different C cells. It remains to rule out a same-cell collision.

## A direct four-case proof of injectivity

Suppose two such returns at the same C cell share a black C charge. One
return ends at that event, and the next return starts at that same event.
They are contiguous: there is no time gap at their common endpoint. A
black C upper corner departs E, so the second return starts by visiting B_s.

1. If the first return has no right zero roof, it visits B_s once on
   black and leaves it white. No part of the rest of that return visits
   B_s. The second return therefore reads B_s white with incoming E,
   turns S, and reaches C_s. It cannot be a first return through A_s to
   C_(s-1). This is a contradiction.

2. If the first return has a right roof but no left roof, its final B_s
   color is black. Its selected black A_s event leaves A_s white. The
   second return goes through B_s to this white A_s, then E to T_(s+1).
   The first return's right roof already used that top cell. A second
   top visit would leave the cap. This is a contradiction.

3. The remaining case has both roofs. The first return leaves

       B_s black, A_s black, B_(s-1) white.

   The second return begins C->B_s->A_s->B_(s-1). Its A_s event is black,
   and the following B_(s-1) event is a white upper corner. This corner
   cannot be the charged corner of a zero roof: the only possible top
   cell T_s was already used in the first return's left roof. It is an
   uncharged corner and marks the second A event, contrary to the
   definition of an unmarked event.

Case 1 also covers the neither-roof case. These alternatives exhaust all
assigned returns. Thus the charge map is injective. The proof uses actual
physical cells throughout. It makes no quotient identification and no
assumption about their initial colors or chronological ranks.

## Algebra and the stronger final form

Set

    Z_0 = K_C+2D_0-Q >=0.

The direct row-port counts give

    Q   = 2M-Delta_A-3H,
    N_A = 4M-Delta_A-4H,
    N_B = 8M-4Delta_A+Delta_B-8H-4D.

Substituting these into N_C=4(N_B-N_A+M)-4K_C-Delta_C gives

    N_C = 12M-8Delta_A+4Delta_B-Delta_C
          -8D_0-4H-16rho-4Z_0.

Equivalently, if Z is defined as in the draft,

    Z=K_C+2D+H-Q = Z_0+H+2rho >= H+2rho,

and

    N_C = 12M-8Delta_A+4Delta_B-Delta_C-8D-4Z.

Both displays are exact identities with the stated nonnegative terms. The
stronger upper bound retains -4H-8rho in addition to -8D. For H=rho=0,
the original fresh-cap theorem and its sharp witness are recovered.

## Independent finite checks

`check_arbitrary_cap_independent.py` uses an ordinary coordinate set for
the complete finite black field. It generates arbitrary initial colors on
the top, A, B, C, and lower rows. It retains completed capped segments,
reconstructs every roof, identifies every charged zero roof and every
unmarked A event, and assigns charges by the actual neighboring C visits.
It checks all identities and the stronger injectivity assertion.

The deterministic run uses 30,000 initial fields, four different black
densities, and up to 180 literal updates per field. It checks 451,630
completed segments. These include 38,136 with top visits, 3,577 with
initially black A bridges, and 643 with a positive roof of at least two
bridges. No charge collision occurs. The complete report retains witness
fields and event lists for the latter two cases.

The finite tests check the definitions and catch implementation/sign errors.
The cap proof and the four-case physical argument, not the number of tests,
establish the unrestricted finite-segment statement.

## Global limit

The theorem permits repeated completed excursions under one fixed cap with
old colors retained. It still does not bound changes of the cap. Changing
the cap changes the roles of the rows and the counted events. Signed color
changes and activity farther below the interface remain. No all-input
highway conclusion follows from this audit.
