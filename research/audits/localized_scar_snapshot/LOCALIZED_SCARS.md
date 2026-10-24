# Localized correction transport through the exceptional rectangle chain

Status: new exact certificate and analytic reduction; independent review pending.
The existing ordinary-parent and exceptional-rectangle dependencies are independently audited.

## Uniform finite-seed theorem

Use the same normalized head(0,0),N, word W, and coordinates as PROOF.md.
Let

    q_n=(-33-2n,-14-2n),  a_n=(-33-2n,41+2n),
    c_n=(8+2n,-14-2n),   d_n=(8+2n,41+2n).

For r=13,14,27,89, respectively, let

    b_r=(-16,31),(-16,32),(-17,32),(-22,29),
    s_{r,m}=b_r+m(-2,2),
    delta_r=20,120,132,32.

For every m>=100 and n>=m+100, the complete finite five-black-cell input

    {q_n,a_n,c_n,d_n,s_{r,m}}

has the same final standard NW tail and pose as the already certified
four-black rectangle, delayed by exactly delta_r updates. Thus a certified
capture checkpoint is

    time = 728n+200304+delta_r,
    pose = (-2n-58,2n+98),N.

No earliest-capture claim is made. The cell d_n is never read. Omitting
d_n gives the same trace, and omitting c_n,d_n instead gives the old
{q_n,a_n} parent's permanent SE trace after the local insertion, with the
same delay. Both statements retain every previously written cell.

The executable parts are derive_scars.py and certify_scar_transparency.py.
The latter checks11,017,890 exact point/ray nonincidences over the full
nonnegative quadrant u=m-100,v=n-m-100. It does not infer an infinite
family from samples. It reuses the independently audited exact bivariate
arithmetic engine. The old complete color-feasibility proof is an explicit
dependency; this new certificate checks a trace-coupling condition rather
than rerunning that proof.

## Finite scar identity and all-age transport

Let e=(2,-2) be the source SE drift, let P be its clean13-cell source core,
and let D be its12-cell deposit. At phase0 the age-j source is

    C_j = P union union_{i=1,...,j}(D-i e).

Write C_j(r) for the state after the first r letters of W, with the head
still measured from the epoch0 origin. Fix one of the four ordinary
phases. The threshold N_r source recovery is literally replayed, with its
complete final field hash checked. If its final head and heading agree
with the unperturbed source phase rho at epoch k, its full reference field
is

    k e + C_{N_r+k}(rho).

The XOR of this field with the perturbed final field is the finite scar.
The checker tests every scar point against the entire infinite outgoing
trace, not just the next period. The two fields therefore have the same
infinite forward trajectory.

For age m>N_r, the perturbed recovery's additional older deposits are
unread, by the already audited all-age ordinary-source guard. They remain

    union_{i=N_r+1,...,m}(D-i e).

The reference field gains exactly this same set: its new deposit indices
j=N_r+k+1,...,m+k become i=j-k after translation by k e. They cancel in
the XOR. Consequently the scar is independent of the source age.

Mapping into the actual NW q-parent frame by F(p)=(-15,29)-p and then
translating by m(-2,2) gives the exact complete-field identity

    actual field at recovery end
      = unperturbed q-parent field at geometric join XOR S_{r,m},
    S_{r,m}=S_{r,0}+m(-2,2).

The unchanged complete q-parent archive H1 also cancels. Its avoidance by
the perturbed recovery was proved in the ordinary-interface theorem.
The scar data are, in phase order13,14,27,89:

    sizes:          9,31,31,15
    z ranges:      [15,19],[-1,17],[-1,15],[3,9]
    u base ranges: [-50,-44],[-50,-42],[-54,-46],[-52,-46]
    epoch shifts k: 1,1,2,2
    output phases: 97,102,103,57.

At source impact phase r, the recovery length is R_r. The actual elapsed
length and the geometrically corresponding reference length differ by

    delta_r = r+R_r-104k-rho.

The checker computes these four delays; it does not assume them.

## The remote cells and both complete continuations

Before the core recovery ends, a_n lies strictly below the complete
recovery prefix's lower-u bound, c_n lies above its upper-u bound, and d_n
lies above its upper-z bound. These are checked as affine inequalities on
the whole cone. Hence those remote bits are unchanged during the local
insertion. The geometric join is strictly before the original a_n impact,
which is phase72 at NW epoch n+5. This time inequality is also checked.
The finite-scar identity therefore holds with the unchanged remote bits
included on both sides.

Between the join and a_n, the reference follows the incoming NW standard
tail. Scar avoidance of that entire tail was checked when constructing
the scar. Starting with segment6 of the old exceptional rectangle template,
the new checker tests every finite read and every complete periodic read
ray against every scar point. Segment6 already starts before the a-hit,
so there is no unguarded seam.

Crucially, two infinite continuations are checked separately:

1. The SE tail from the end of old segment8, with c_n,d_n omitted.
2. The final NW tail after the entire rectangle template.

Protecting only the finite middle corridor would not establish the first
claim. Both infinite read-ray tests pass over the whole parameter cone.
First-difference coupling now proves that the unchanged reference trace
is valid forever on the scar-modified field. The checker sums the old
macro durations to728n+200304 and checks its final pose; adding delta_r
establishes the displayed checkpoint.

## Archive and geometric interfaces for recurrence

The finite changed recovery reads have |z| at most19,17,17,17,
respectively. Thus they lie in D82 for every m. All remaining reads are
in the audited reference parent traces, which also lie in D82. The
intermediate {q_n,a_n,s_{r,m}} parent therefore stays inside D82 forever.

Its finite prefix and stationary canonical SE archive still have u<=98
and z<=71. Before the join these bounds follow from the ordinary-parent
prefix bounds. Afterwards the archive is exactly the old {q_n,a_n}
archive XOR the stationary scar. The latter has u<=-4m-42<98 and z<=19,
so the union gives the same bounds. The clean canonical outgoing core is
unchanged, and no support from the original field has been discarded.

## Four additional retained-core rays excluded

Fix any m>=100 in one of these four classes, and suppose it is the unique
persistent local black cell at recurrent mass-five checkpoints. The global
incidence lemmas give q_n and one of the two four-edge strands or a
four-cycle, with n tending to infinity. The cone condition eventually holds.

The core is blank-inert, and the initial q-parent reaches it before any
remaining remote cell, as in the audited ordinary-interface argument.
After recovery it has the exact original NW rail, with a stationary scar.

- In the first four-edge orientation, a,d lie outside D82, while c is
  beyond the upper-u bound. Thus no remaining remote hit is possible.
- In the transposed orientation, c,d lie outside D82. The only possible
  interruption is a on the NW tail. An ordinary a-hit has u<=u(a)+58,
  below the fixed-m complete archive and below the other remote cells by
  their diverging axial gaps. The favorable-sector check is the same one
  used in the audited ordinary-ray theorem. Hence a must be exceptional,
  which forces a=a_n because the geometric rail is exactly the original
  one. The new intermediate parent stays in D82 and never meets c,d.
- In a four-cycle, a is again the only first possible interruption and
  must equal a_n. The new intermediate parent has unchanged SE geometry,
  u-prefix/archive upper bound98, and complete z upper bound71. Only c
  can interrupt. An ordinary c-hit has u>=u(c)-58 and avoids that archive
  and the other remote cells by the same diverging-gap argument as the
  audited original rectangle proof. Therefore c=c_n and d=d_n. The new
  complete five-cell certificate gives permanent capture, with d unread.

All cases contradict recurrent mass five. This removes these four whole
fixed-core rays for m>=100, not arbitrary one-black cores. Together with
the twelve independently audited ordinary rays and the separately audited
entire phase72 half-ray, it addresses17of the22 asymptotic fresh classes.
The two displaced NW classes70,75 and the three NE classes29,56,62 remain.
