# Marked-A transport after the span calculation

23 October 2026. Proposed local lemmas, submitted for independent review.
No global A/B balance or cap-three exclusion is claimed.

Use complete white RLR/RL histories, the signed same-type exclusion and short-D-path classification. A=AAB and B=ABB. Headings N,E,S,W are 0,1,2,3; A0 has headings N,N,S, B3 has W,E,E. A `marked A0` is an A0 whose east neighbor is the complete RL source S3 (headings W,E, both departures north). Rotate this definition for the other orientations.

## 1. The missing BA detour, also allowing a D square

Start with the one-A path

    p=(0,0) -> u=(0,1) -> q=(-1,1),

and its forced opposite A r=(-1,0). Write F<M<T for u's times. The signed span lemma gives

    F_r=M-2,  T_r=T+2.

Suppose the D predecessor b=(-1,-1) of r is B3. This includes either a three-edge BA path or the A of an AABB D square whose immediately preceding D vertex is B. In either case the exact source-pair chronology gives

    F_b=F_r-1=M-3,  T_b=T_r+3=T+5.

For the BA case the three intervening reads from r's third R to b's third R are the D sink and source. For the square case they are the other A's middle L and the other B's middle L. Thus the same formula is valid in both cases.

Let c=(0,-1), f=(0,-2), e=(-1,-2). The H input to b comes from c. Cell c cannot receive a southward arrival from p, because the complete source p only departs north. Its departure west into b must therefore be its L with incoming north. Hence c is exactly the RL sink D0, and

    L_c=F_b-1=M-4.

Its doubled incoming edge comes from f. There are two possibilities:

* If f is a triple, the signed two-D-face rule makes it B3, opposite the H-corner B3 at b. Its D predecessor e cannot be a triple because b->e is a single H edge, whereas an interior D turn at e would require that edge doubled. Thus e is the D source and e->f->c is a one-B path.
* Otherwise f is the RL source S3. Its last L occurs at M-5 and is fed by an R at e at M-6. The later H exit from b enters e at T+6. The earlier e read cannot be L, because that would require the already unavailable south arrival from b. It is first R, incoming north. The later e read cannot be L, since its east exit would read f a third time. It is third R, incoming south. The middle heading is north because b has only one south exit. Therefore e is A0 and

        F_e=M-6,  T_e=T+6.

The signed one-A gap gives M-F>=8, so F_e>F. Between first reads at u and e, the actual path has displacement(-1,-3), starts with an east move, and ends with a north move. Equal numbers of horizontal and vertical moves force at least five moves of each axis: the last north move and net vertical displacement -3 require at least four south moves. Hence F_e-F>=10, M-F>=16, and

    (T-F) - (T_e-F_e) = M-F-12 >=4.

This reconstructs the previously signed BA-plus-one-edge detour and extends its same formula to the B-preceded A of a D square. It does not cover the A preceded by A in that square.

## 2. An A preceded by A on a D square cannot be an H sink-pair corner

Normalize an AABB D square to

    s=(-1,0) B0 -> b=(0,0) A1 -> v=(0,1) A0
       -> t=(-1,1) B1 -> s.

Suppose v is marked by p=(1,1) S3, and its H face has just the one D edge
p->z, z=(1,2), with z the RL sink D0. Thus its other H corner q=(0,2) is B3, by the signed one-D-face rule. Put T=T_v. Exact H-face timing gives

    T_q=T-1.

The D-square second traversal exits v at T and enters t's third R at T+1. That R exits north into w=(-1,2) at T+2.

But q=B3 has its doubled incoming edge from w heading east, and q's last read was already at T-1. Therefore w must have two east departures before T-1, yet it receives the displayed north arrival at T+2. Its complete allowable history makes this impossible:

* A double with both departures east has incoming headings N,S; the later north arrival would have to be its first read, after both departures.
* A triple with doubled east departures has either A2 or B0 geometry. For A2, the north arrival is its third R and would supply a third, later arrival at q. For B0, the north arrival is its first R, again later than the two required departures.
* A singleton cannot supply two departures.

Consequently this particular D-square/H-sink overlap is impossible. In the marked setting, the alternative H-face geometry is a two-edge one-A face whose opposite A maps to v. The analogous B-side overlap is NOT excluded: an independently replayable radius-three open-boundary clock model survives for it.

## 3. What this does not establish

The marked-A continuation can reach one-B paths, can pass through more zero-index tiles, and can reach the A-preceded A on an AABB square. No injection from all one-A paths to distinct one-B paths is supplied. Multiple one-A corners along a transport chain cannot be counted as separate terminal B corners without further work.

The auxiliary open-boundary necessary solver found the Section 2 overlap UNSAT locally and the B-side overlap SAT locally. These solver outcomes are controls only; Section 2's argument is the proposed proof. The general cylinder searches and four-cell catalogs elsewhere in this directory remain fixed-support/local computations, not unrestricted exclusions.
