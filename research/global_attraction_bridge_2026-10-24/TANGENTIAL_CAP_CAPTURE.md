# A causal seven-cell tangential wake cannot fund an outward ladder

Status: author checked, frozen for independent audit. This is an all-parameter scoped counterarchitecture, not a universal attraction result.

## Main conclusion

For every integer K>=0, start at (1,1), S, with the seven black cells

    S={(0,1),(0,2),(0,3),(2,4),(3,2),(3,3)}
    together with a_K=(5+2K,-4-2K).

This is a genuine constant-original-mass architecture, not an edited prewritten wake. The complete half-plane x+y<1 is initially white. The ant itself writes an arbitrarily long tangential standard wake with drift d=(2,-2), then encounters the initially unread cap a_K at exactly T_K=279+104K. Every member captures into an exact standard104 future.

For all K>=11 the entire post-contact turn word has one fixed length-2184 certificate F, independent of K. Relative to a_K, the certified endpoint is (6,14), W, with standard drift (2,2). All complete older fields are retained. There are exactly 20 strict pristine SW record cuts in the whole orbit, at successive x+y levels 0,-1,...,-19. None matches an outward capture guard at that cut. There is no further SW record thereafter. Thus extra tangential wake length does not buy extra outward SW progress.

More generally, for all K>=0, the number of guard-avoiding genuinely pristine record TIME CUTS among the eight coordinate/diagonal directions is at most 3168. This is only a bound for this seven-cell family. It is not a mass-only theorem for arbitrary seven-cell boards.

## Exact causal launch

Let W=R L C6 be the signed 234-move launch from the six-cell seed S. It reaches the complete field E with |E|=50, from which H104 repeats with drift d=(2,-2). Let Q be the 104 tail read positions, M their odd-toggle set (|M|=32), and P45 the odd-toggle set of Q[0:45]. The literal words are in the certificate.

The ray a_0+Z d meets the launch read set only at negative indices. A tail phase i that reads a_K has time 234+104(K+e)+i, where every compatible offset e is nonnegative and 104e+i>=45; the minimum is phase45, e=0. The expected turn there is R. Thus a_K stays genuinely unread and black until T_K, while all earlier turns are exactly

    W H^K H[0:45].

Its actual turn at T_K is L, the first symbol of F. No field has been modified at this late cut. This all-K first-contact argument was already independently signed in the fresh-record package and is reconstructed by the new checker.

## The full contact field and why extra wake is unusable

Translate a_K to the origin. The COMPLETE black field immediately before reading it is the finite symmetric difference

    B_K = {0} XOR (P45-a_0)
          XOR (E-a_0-Kd)
          XOR XOR_{ell=1..K}(M-a_0-ell d).

For K>=11, the difference B_K XOR B_11 is supported on the following exact union of rays:

    e-a_0-kd,  e in E, k>=11;
    m-a_0-ell d, m in M, ell>=12.

These are 50 source rays and 32 wake rays. Some formal terms cancel, but no cancellation is needed for the obstruction: EVERY ONE of these 82 complete rays is disjoint from EVERY read of the normalized future F V^infinity, where V is the certified 104-word at the endpoint and has drift (2,2).

The checker proves this by exact integer ray intersection, not by a long finite simulation. Intersection with the 2184 finite reads of F is tested directly. Intersection with each of the 104 infinite V-phase rays reduces to a two-variable integer linear system, including both nonnegative parameter conditions. Every system has no admissible solution. Therefore the two full boards differ only on cells that the complete proposed future never reads. Induction transfers the entire actual infinite future from K=11 to every K>=11.

This is the exact regeneration failure. The distant extra wake survives in the board but is causally inaccessible to this particular post-contact continuation. It is not discarded or mistaken for zero mass.

## What the continuation really consumes

The contact-time cohort has mass 58+12K. For all K>=11, F consumes exactly 113 of its genuine lifetimes: the initial cap and 112 R-born wake lifetimes. Their relative coordinates, birth identities, and L-consumption offsets are recorded. The oldest consumed wake birth is T_K-910; the last consumption is at T_K+1872. Each birth formula is checked as the last prior H-ray visit, with its actual R letter, and is valid for every K>=11.

The remaining 12K-55 contact-cohort lifetimes are never read again, including throughout the infinite final tail. For K=11 this is checked against all future tail rays. For greater K the exact unread difference-ray argument transfers it. The full final black mass at the chosen certificate cut is 224+12K. No repeatable-state equality or fuel regeneration is claimed.

## The finitely many short wakes

The certificate supplies complete literal histories, complete final boards, and infinite ray-parity tail checks for K=0,...,10, plus the K=11 anchor. Their post-contact certificate delays are:

    K:       0    1    2    3    4    5    6    7    8    9   10   11
    delay: 624 1352  624  936 1976 1456 1456 1872 2184 2184 2184 2184

These are sufficient certificate cuts, not claimed earliest standard-word onset times. The longer-wake all-K theorem comes from the unread-ray proof, not from extrapolating this table.

## Pristine-record bound and exact scope

For K>=11, W, one H period, F, and one V period determine the minimum of x+y on the complete path, because H is tangential and V increases x+y by 4 each period. The minimum is -19. The head starts at level2; the first visit to level1 is not pristine because the cap is still black on that level. Every first visit to levels0 through -19 is pristine, since all initial black cells have x+y>=1 and no prior read reached that lower level. These are the 20 stated SW records. At each, finite future turn comparisons rule out all 104 cyclic standard words, hence every catalogued sufficient capture guard.

For all K, the complete history has arbitrary pieces of total length at most 234+2184 and two standard-word pieces: H^K H[0:45] and the infinite final V tail. The independently signed standard-piece interior lemma permits at most L+375s guard-avoiding pristine record time cuts. Thus 2418+750=3168. If counting direction-marked cuts rather than time cuts, the immediate bound is 8*3168=25344. No prepared head-position record is substituted for the actual pristine-half-plane test.

This architecture does recycle a substantial amount of self-produced material and turn toward the virgin side temporarily. What it does not do is make that use grow with the rail-length parameter. A two-cap or more complicated tip might do something different; this theorem excludes only the exact causal one-cap family above.

## Reproduction

Run `python check_tangential_cap_capture.py`. The manifest binds the proof, literal certificate, checker, output, and signed source dependencies. Independent audit is required before calling the package PASS.
