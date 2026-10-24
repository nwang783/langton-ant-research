# Eleven initial-southwest retained-core rays are excluded at mass five

Status: exact interface checker passes; independent analytic review requested.
This is not a whole-arm exclusion. The first argument covers phases15,45,46,47,57;
the later sections add60,70 and13,14,27,89. All use fixed blank-front age m>=100.

Let Q_r be the cell read at phase r of canonical SE word W, starting at zero,
south. Let R(x,y)=(y,-x), O_m=(-15-2m,10-2m). The retained one-black local core
is

    s=O_m+R(Q_r), r in {15,45,46,47,57}, fixed m>=100.

No hypothetical recurrent mass-five fixed-pose checkpoint sequence can have
this local core, under the previously audited critical-clock and incidence
lemmas. The remote distances tend to infinity while m is fixed.

## Complete-history interface

Use source coordinates R^{-1}(x-O_m). The one-black parent eventually travels
NE for each of these five r. The first far exceptional phase72 marker is
Q=e_r+k(2,2), k>=100. The audited ordinary_reverse_interface package proves the
ENTIRE two-cell future, including every return through the older canonical
wake. Its blank-seed transfer retains the complete original blank archive:
all omitted history is in u<-160, while the certified future stays in u>=-160.

The new checker extracts these exact bounds from those checked words:

    r   complete future u range   finite-prefix z lower   archive z lower
    15        [-128,74]                   -29                   -73
    45        [-140,62]                   -29                   -73
    46        [-104,64]                   -31                   -73
    47        [-104,64]                   -31                   -73
    57        [-100,68]                   -31                   -73

The finite prefix includes the move to a phase-zero SW tail. Both its pose
and phase are independent of k. The complete fixed XOR archive relative to
that canonical13-cell tail core is supported in z>=-73, uniformly k>=100.
This is a bound on the ACTUAL complete archive, not merely read positions:

* Every new write is among the bounded prefix reads.
* The first core and remote marker obey the same bound.
* The original stationary blank archive has u_actual>=-34; source z equals
  u_actual+25, hence is at least -9 and therefore at least the conservative -73.
* The omitted older canonical deposits have z>=-3.
* The phase-zero thirteen-cell core is explicitly included in the bound.

Before the core is hit there is an additional finite blank prefix depending
on the fixed m. This only enlarges the fixed u-strip; it introduces no k
dependence. The new checker pins the already audited package manifest and
its individual certificate/template hashes. No new color extrapolation is used.

## Four remote cells

The previously reviewed first-contact/exposure lemma can be rotated180 degrees
for the NE parent. It makes the first distant hit favorable. All nine ordinary
favorable impacts are excluded by the usual58-unit escaping-half-plane guard,
so this first hit must be the exceptional Q above.

There is exactly one bounded core and four escaping checkpoint cells. The
remote incidence component is therefore a four-edge strand or a four-cycle.
Every remote degree-two vertex has opposite b signs on its two edges.

For either four-edge orientation, every remote cell except Q has |u| tending
to infinity. The complete two-cell parent is contained in a fixed u-strip
for fixed m, so it never reads any of those three cells. Capture is permanent.

For a four-cycle, write the first NE corner Q=(r,t), the adjacent corners
A=(l,t), C=(r,b), and the opposite corner S=(l,b). Exposure gives r-l and t-b
both tending to positive infinity. Since u(Q) stays bounded,

    u(A)=u(Q)-(r-l) -> -infinity,
    u(C)=u(Q)+(t-b) -> +infinity.

Thus A,C miss the complete parent. Both Q and S have positive z-clock sign;
the negative-direction z clock forces z(S)->-infinity. The finite two-cell
prefix has z>=-73, so S can only be read on the final SW tail. If it is never
read, capture is already permanent.

## The opposite corner cannot reverse the returned tail

Q and S have opposite parity in BOTH coordinates: the two side transitions
of the cycle each cross a degree-two remote row/column with opposite b signs.
Both have odd x+y in source coordinates. The exact checker verifies that the
fresh sites in this sector are precisely the favorable ten phases. It also
checks, separately for each of the five returned tail phases, that its fresh
phase72 ray has the SAME coordinate parity as Q, not S.

Hence a first S contact is one of the nine ordinary favorable impacts. Every
read after that impact has z<=z(S)+58. This misses the complete old archive
(z>=-73), the fixed core, and A,C because

    z(A)-z(S)=t-b -> infinity,
    z(C)-z(S)=r-l -> infinity.

The original Q and its written history are already in the protected archive.
The canonical incoming wake is handled by the audited all-age ordinary
scatterer guard. The outgoing capture is permanent, contradicting recurrent
mass five. This excludes the five stated core rays for every fixed m>=100.

No conclusion is drawn for the other17 initial-SW fresh classes, the remaining
return-NE strip, or arbitrary local cores. The r57 two-cell return itself was
already present in the literature; the new use here is the full-archive,
remote-cycle parity coupling.

## Two additional cap-parity exclusions: r60 and r70

The newly audited blank_return_cap package supplies the complete two-cell
parents for these two initial-SW core phases, for independent m,k>=100.
The separate certify_cap_interfaces.py checker derives the following bounds
on their ACTUAL complete histories. It composes the already checked local
packet, exactly m+k-20 NE periods, and the exact checked central cap word.
It includes the entire blank prefix and canonical tail-entry core.

For r60, after first SW exceptional Q, the outgoing tail is NW. Before that
tail, every read has -96<=u<=48 and z<=41; the complete fixed archive has
u>=-96. The final tail reads 7<=z<=17, and its u decreases. Consequently the
whole parent has u<=48,z<=41 and is contained in the fixed diagonal cross
{-96<=u<=48} union {7<=z<=17}.

The usual four-edge incidence orientations therefore either avoid the parent
entirely or leave only the NW adjacent corner A. In a four-cycle the SE corner
is excluded by u<=48 and the NE corner by z<=41. The first SW corner Q has
coordinate parity(even,odd), so A has(even,even). The returned NW phase72 ray
has(odd,odd), a mismatch. Any A contact is one of the nine ordinary favorable
phases, whose future lies in u<=u(A)+58. It misses the entire archive u>=-96
and both other corners by their diverging positive axial gaps. Capture follows.

For r70, the outgoing tail is NE. Its entire parent lies in -98<=u<=60, while
its pre-tail reads and entire fixed archive have z<=59. A four-edge strand
has all three unused corners outside the u-strip. In a four-cycle only the
opposite NE corner D can meet the tail. Its coordinate parity(even,odd) is
opposite in both coordinates to Q=(odd,even), whereas the returned phase72
ray again has Q's parity(odd,even). Thus any D contact is ordinary and its
future lies in z>=z(D)-58. This avoids the archive z<=59 and both adjacent
corners, which lag by the diverging axial gaps.

The exact sector checker confirms that the relevant parity sector contains
only the favorable ten phases in BOTH cases. Therefore r60 and r70 are also
excluded for every fixed m>=100. The total scoped count in this document is
now seven initial-SW rays, not five. It still does not close the whole arm.

## Four further rays via an exact live-region reset:13,14,27,89

certify_live_reset.py proves a stronger statement than merely identical output
headings. For each of these four initial-SW core phases and independent ages
m,k>=100, the complete two-cell field at a common return pose(-15,26), east,
restricted to the WHOLE region R={z>=-250}, is exactly the fixed2442-cell field
of the original exceptional q_n parent. The comparison is an exact set equality.

This follows from the already audited actual-field-to-cap bridge and a new
exact identity: after10262 letters of cap13, its complete infinite-ray model
has that pose and that restriction. All four branches share this cap. Every
read before this reset lies in -82<=u<=58 and z<=39, after including the entire
blank prefix. The complete actual fixed archive obeys the same u bounds.
The initial SW distant collider Q has coordinate parity(odd,even).

Crucially, the field below R is NOT erased. It can contain arbitrarily long
old histories and depends on both ages. It is irrelevant only to reference
continuations whose EVERY future read stays inside R. The checked one-bit,
two-bit and independently aged three-bit parents have exactly that property.
This is a reusable live-region reset condition, not a general renewal theorem.

At recurrent mass five, the first distant collision is SW. Exposure excludes
all ordinary favorable channels; the exceptional collision is the second bit
of the certified packet. Before the reset, both axial partners escape its
fixed u-strip. The remaining NE cell in a four-cycle has z->infinity and also
misses that prefix.

After the reset the same two four-edge cases as in the original rectangle
argument apply. In the first orientation all three remaining cells miss the
NW parent. In the transposed orientation only the far NW corner A can collide;
an ordinary contact escapes below the actual archive's u lower bound -82.
An exceptional contact forces A=a_n; its complete SE continuation misses the
two remaining one-bounded-coordinate cells by its bounded z strip.

In a four-cycle, the only possible next collision is A on the NW tail. An
ordinary contact again escapes. Otherwise A=a_n. The following two-bit SE
parent excludes the NE corner D by its z<=71 bound; only the SE corner C can
then collide. The actual entire archive has u<=98, because the pre-reset
archive has u<=58 and every new prefix write/canonical core has u<=98.
An ordinary C contact escapes. Otherwise C=c_p. The two ages n,p need NOT
coincide: the independently checked three-age continuation applies. Its entire
read strip is -93<=z<=75, so it misses D=(8+2p,41+2n), whose z tends to infinity.
All compared futures stay in R, preserving the exact complete-history coupling.

This adds four rays to the earlier seven. The total in this document is now
ELEVEN initial-SW core rays, each for fixed m>=100:

    13,14,15,27,45,46,47,57,60,70,89.

The adjacent independent_reverse_ages package additionally excludes the
initial exceptional72 ray q_m for fixed m>=200. These twelve asymptotic classes
still do not establish a whole-arm or arbitrary-core theorem.
