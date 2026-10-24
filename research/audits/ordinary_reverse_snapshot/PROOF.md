# Ordinary scattering followed by a remote reversal: an archive interface

Status: every exact checker passes. Independent review is requested. This is a
restricted return theorem and an explicit obstruction to an overbroad interface,
not the highway conjecture or a self-renewing scattering circuit.

## 1. Complete input and parameters

Use the usual coordinates and headings N,E,S,W = 0,1,2,3. Put u=x-y and z=x+y.
Let P, D and W be the exact canonical southeast phase-zero core, twelve-cell
deposit and standard 104-letter word in ant_exact.py. Set

    C42 = P XOR (XOR over 1<=j<=42 of (D-j(2,-2))).

This is the entire finite field, with 517 black cells, not a cropped picture
whose omitted part is assumed blank. At position zero and heading south it
follows W forever. Let Q_r be the phase-r read in its current W period.

The ordinary fresh phases are

    13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,75,89.

For each r, the previously checked ordinary one-defect recovery has a specified
endpoint p_r, heading h_r, outgoing phase phi_r and drift d_r. Define e_r by
advancing that endpoint by (72-phi_r) mod104 letters of its outgoing word.
For any integer k>=100, install two toggles at

    Q_r and e_r+k*d_r.

The executable independently replays the old ordinary certificate before using
its endpoint. It then proves the whole new trajectory from C42 with BOTH bits
already present. The second bit's exact first-contact time is

    104k + r + ordinary_steps_r + ((72-phi_r) mod104).

Thus this is a genuine first phase-72 reversal, not a selected later read.

## 2. All 21 complete finite kernels capture

Every one of these 21 two-toggle families has a standard translating infinite
future for every k>=100. The candidate words were extracted from two runs only
as a discovery step. Their proof instead represents the complete field as exact
affine points and finite rays, checks every finite word's required initial
colors, every repeated word at every integer epoch, and the entire infinite
tail. The engine is the previously independently audited univariate affine-XOR
checker. All words are restricted to the alphabet R,L; standard-tail membership
and correct heading reset are explicit assertions.

Each certificate_r*.json records exact capture time, pose and phase, plus the
first-contact and archive bounds. These are sufficient capture boundaries, not
claims of earliest eventual standard-word onset. All initial fields here have
519 black cells, counting the complete mature kernel and the two toggles.

The same prescribed trajectories hold with arbitrarily many, or infinitely
many, additional old canonical deposits. Every finite-prefix read has u>=-140
in the worst channel; the omitted deposits j>=43 have u<=-163. A final reverse
NW tail, when present, lies in a z-band strictly above every old deposit. No
old canonical point is silently discarded.

## 3. Thirteen arbitrary-history-protected return channels

For the thirteen phases

    15,29,32,38,45,46,47,55,56,57,61,62,71,

the ENTIRE future, including its infinite tail, stays in u>=-160. Consequently
one may replace the initial field anywhere in u<-160 by an arbitrary finite
black pattern, with no change to the prescribed future. Equivalently, every
finite field agreeing with the specified two-toggle kernel on u>=-160 has the
same certified trajectory. This follows by first-difference coupling, not by
claiming that the older field disappears.

The precise uniform lower bounds are, in the displayed phase order,

    -128,-68,-66,-72,-140,-104,-104,-92,-52,-100,-70,-64,-60.

These are genuine out-and-back packets: the remote phase-72 impact reverses the
first outgoing highway. Some return blocks read old self-written wake before
capturing. Arbitrary old material BEHIND the interface is protected, whereas
further scatterers in front are not covered by this theorem.

The phase57 packet is a rotated/rebased version of the existing literature
return-scattering-closure.md example in the local kehao95-core checkout. No
novelty is claimed for that channel, or for convergence of general two-black
initial states. The deliverable here is the uniform 21-channel archive split,
its explicit complete-field guards, and the simultaneous all-distance controls.

## 4. Eight backward channels require a real endcap condition

The remaining phases are

    13,14,27,28,60,70,75,89.

Their certified finite-kernel tails move NW, through arbitrarily negative u.
It would be false to extend the arbitrary-history protection in Section3 to
these channels. The checker gives an explicit FIXED additional black bit b_r
in u<-160 for each channel, independent of k. Before tail entry the bit is
unread. On the final NW tail it is first read at an exact affine time 208k+C_r,
where the unperturbed reference expects white and the extra bit is black.

Construction: the final pose is (2k+a,-2k+b). At its phase72 read after k+1000
whole tail periods, the k terms cancel, giving a fixed old location. Enumerating
all 104 phase rays proves this is its first read. It lies above the old canonical
deposit z-band and below the forward interface, so it was not an initial kernel
bit and cannot have been touched earlier.

These controls disprove only an UNCHANGED-FUTURE interface for arbitrary history.
They do not assert noncapture after the new collision, or prove any renewable
circuit. They identify exactly which compositional condition is missing: one
must certify the backward tail's interaction with the actual complete endcap,
or impose a region that this actual history avoids. Finite support alone does
not give the required no-interaction statement.

## 5. Complete blank-prefix realization with two independent distances

At time9977 the initially blank ant is at (-15,10), west, on canonical phase0.
Its complete 715-black field equals the rotated P core XOR a stationary
702-cell archive E. Literal replay checks -21<=z(E)<=35 and the full standard
future. The exact identity P XOR Odd(W) = (P+(2,-2)) XOR D then gives its
complete field after m periods, not just the local cells.

At that time put O_m=(-15-2m,10-2m), and let R(x,y)=(y,-x). For each protected
phase r and independent integers m>=100, k>=100, the finite initial seed

    { O_m+R(Q_r), O_m+R(e_r+k*d_r) }

has the certified packet future after time9977+104m. Both bits are explicitly
unread before their stated encounters. In source canonical coordinates the
entire stationary blank archive satisfies u<=16-4m<-160; the extra old deposits
are likewise behind the interface. Hence the real blank transient is retained
and harmless throughout the packet. Exact global times and positions are
encoded in interfaces.json. This is a genuine two-cell finite-seed corollary,
not a transfer from an infinite rail without an endpoint guard.

This corollary does not yet exclude all retained cores at recurrent mass five:
other remote initial cells can interrupt a packet, and the eight backward
channels still need their actual blank-history return analyzed. No global
interaction graph, monotone event budget, or mass-six theorem is asserted.

## Reproduction

Run certify.py separately for each of the 21 listed phases, then run
certify_interfaces.py. The small certify_manifest.py checks the pinned source,
complete channel coverage, and output hashes. Discovery scripts and sampled
words are not inputs to a proof except through templates which are subsequently
fully checked.
