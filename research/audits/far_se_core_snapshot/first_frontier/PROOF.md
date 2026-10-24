Current status: all 22 first-band recurrence classes now close under the established incidence lemmas. All exact checkers have passed; independent audit remains pending. See ../PROOF.md for the consolidated theorem and coupling.

# The first far-southeast retained-core interface

Status: exact complete-history interface and all21 ordinary local transfers
passed. The twelve recurrence exclusions below have not yet been independently
reviewed. The whole far-SE arm is not yet closed.

## Exact complete-history transfer

Set A=(40,-52), SE=(2,-2), O=A+m SE, and let p_r be the phase-r read position
of W starting at0,S. The retained core is s=A+p_r+m SE. The full three-cell
input is {q_n,a_n,s}, ant0,N, with m>=100,n-m>=100.

The old q+a parent reaches A,S at time416n+146044, after old segments0..8 and
the first four letters of the phase100 SE tail. Its complete field is P+A XOR
E_n. Every point of the stationary archive E_n satisfies u<=97,z<=71. This
includes every old finite point and every deposition ray; no history is
truncated. The full earlier read bounds are u<=98,z<=71.

The exact one-period identity P XOR Odd(W)=(P+SE) XOR D gives, after m clean
periods, the canonical age-m state at O XOR the same stationary E_n. Comparing
with the infinite-age canonical state adds only the older deposits, whose
global u is also at most97. Therefore throughout the entire forward half-plane
u_source>=-200 the actual field equals the mature clean SE field. The source
time is416n+104m+146044. The full prefix before the source has u<=4m+98,z<=71.
The original c_n and d_n are separately excluded by these bounds, binding the
inherited old rectangle prefix to the two-cell q+a parent.

The22 fresh core bases cover exactly every(z,x modulo2) class for
-15<=z<=-5. Their u values lie between95 and102. Hence every fixed site in this
band with u>=502 has a unique representation with m>=100. All earlier clean
periods and earlier within-period reads miss that core.

All21 ordinary one-bit channels are independently replayed from their exact
finite threshold-age certificates. The older canonical deposits are proved
invisible to both the recovery and the infinite tail. Every future read stays
in u_source>=-200, so the complete old q+a archive is irrelevant. Exact output
poses/times, stationary archive bounds and outgoing phases are saved in
ordinary_interfaces.json. Phase72 is not included in this ordinary theorem.

## Twelve proposed recurrence exclusions

Fix m and let the recurrent mass-five checkpoint's remote scale escape. The
blank and q parents cannot read this far-SE core. A noncapturing first NW
remote interaction therefore still forces a_n, by the established incidence
and ordinary58-unit guards. In a four-edge strand, the unused corners have
one bounded Cartesian coordinate and the other escapes. The complete q+a
prefix lies in the established two diagonal strips, while the fixed-m local
recovery and its outgoing highway lie in another bounded union of diagonal
strips. Thus those unused strand corners are eventually missed.

In the four-cycle, the two remaining corners are c=(r,-2n-14) and
 d=(r,2n+41), with r,n tending to infinity. The finite new prefix has a fixed-m
upper u bound and a fixed z bound, so c and d cannot intervene before the
ordinary parent reaches its outgoing tail.

* SW outputs29,32,38,55,56,62,71 miss both remaining right-column corners.
* SE outputs28,60,61 can meet only c. Their exceptional phase72 rays have odd,
  odd coordinates, whereas c is even,even. Every possible hit is therefore
  one of the nine favorable ordinary channels. Its future lies at
  u>=u(c)-58, eventually above the entire stationary archive. Also
  u(c)-u(d)=4n+55, so d is missed.
* NE outputs15,45 can meet only d. Their exceptional rays are odd,even, whereas
  d is even,odd. The possible ordinary continuations lie at z>=z(d)-58,
  eventually above the archive, while z(d)-z(c)=4n+55 protects c.

certify_corner_sectors.py checks every outgoing cyclic phase and the preserved
(x+y+h) modulo2 sector. Thus possible later corner hits really belong to the
favorable ten fresh phases, not an assumed orientation-independent subset.
The archive comparisons use fixed m before sending n,r to infinity.

Remaining first-band classes are the four transparent-scar candidates
13,14,27,89; two SE exceptional-c branches70,75; three NE exceptional-d
branches46,47,57; and the phase72 reversal. They are not counted as excluded
here. The final far-SE NW-passage band55<=z<=65 also remains to be classified.

## Four additional scar classes

`certify_scars.py` proves complete-field rejoins for r=13,14,27,89. It
reconstructs the threshold-age finite field, compares it with the exact clean
reference at the same pose, and checks the four delays 20,120,132,32. At all
larger ages the extra old deposits have exactly the same indices in the
perturbed and reference states and cancel. The stationary old q+a archive
also cancels without being deleted. The comparison point precedes segment
10 since its reference time is less than 104(n-m)-2084. Both remaining
markers are outside the complete altered recovery's checked read bounds.
The finite scar is invisible to the continuing SE parent, all subsequent
rectangle segments, and the final infinite NW tail. Thus these four complete
five-cell families capture at 728n+200304+delta with the original final pose.
The same four-edge/cycle argument adds their four recurrence exclusions,
bringing the presently proved interface/guard/scar classes to sixteen.

## Six remaining templates (now all exactly verified)

For r=70,75 an exceptional SE collision with c forces its x coordinate to
2n-8, 2n+4, respectively. For r=46,47,57 an exceptional NE collision with d
forces x=2n+4m+134, 2n+4m+134, 2n+4m+138. Each complete five-cell checker keeps
both corners and all old history. The other corner is separately tested for
never being read. In a transposed four-edge strand these forced x values
cannot match a bounded column, so only the guarded ordinary case remains.

For r=72, the complete three-cell q+a+s parent has its own full-history
checker. Its proposed final NW tail, together with bounds u<=4m+C and z<=C',
would protect it from both later cycle corners for every fixed m and all
sufficiently large n. Neither this parent nor the five forced-corner branches
is inferred from an infinite-past scattering experiment. All six exact executions have now finished successfully. Their outputs and
forced-corner bindings are checked by ../certify_manifest.py.
