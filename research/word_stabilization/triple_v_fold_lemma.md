# Three folds separated only by V are impossible

Status: explicit all-parameter witnesses supplied by the word analysis; analytic
no-intervening-read proof and independent literal checker supplied by the
audit analysis,22October2026. No finite parameter search is the proof.

For A,F,D in {B,Q} and integers n,m>=0, the word A V^n F V^m D is physically
infeasible on every initial coloring. Coordinates use an initial north-facing
head at(0,0); phases are zero-based. Write A=B for e=0 and A=Q for e=1.

The literal finite facts checked by `verify_triple_v_fold_lemma.py` are:
V ends at(1,3),N and its footprint has -1<=x<=2,-1<=y<=3. Its reads at
(-1,0),(0,2) are uniquely phase1 L and phase12 R, and(0,3) is absent.
The line (d-3,3d-6), for integer d, intersects its footprint only at d=2,
namely(-1,0). Both folds first read(-1,2) at phase13 L and(-2,1) at phase15 R.
B's last reads at(-2,-3),(0,-1) are phase67 R and phase3 L. Q's last reads
at(-3,-2),(-1,-1) are phase57 R and phase46 R. Q has y>=-4 and omits(-3,-4).
The finite words VB,BB,QB,QQ all fail by consecutive equal-letter reads.

## 1. The middle fold B

If n>0, the prefix ends in VB, already impossible. If n=0, it starts BB or
QB, again impossible. Hence only F=Q needs an unbounded argument.

After A, the pose is(-3-e,-5+e),S. Outward V occurrence j (zero-based) has
head(-3-e-j,-5+e-3j),S. After the middle Q, the head is
(1-e-n,-1+e-3n),N. Return V occurrence j adds(j,3j). Let k=n-m; the final
fold therefore starts at(1-e-k,-1+e-3k),N.

## 2. k>=2

Take q=(-k-e,1+e-3k). Final-fold phase13 is the first read of q and is L.
In outward V occurrence j, q would have local coordinate
(d-3,3d-6), where d=k-j. The finite footprint identity forces d=2,
so j=k-2 is the unique outward occurrence, and its unique read is phase1 L.
The index exists because0<=k-2<n.

The middle Q would need local(-m-3,-3m-6), below y=-4. During return V
occurrence j<m, the local y is3(m-j)+2>=5, above V's footprint. Hence the
outward phase1 L and final phase13 L are consecutive reads of q, a contradiction.
Any initial-fold reads precede the identified outward read and do not matter.

## 3. k=1

Take q=(-2-e,-3+e). Its last initial-fold read is B67 R or Q57 R. An outward
V would require local(-1-j,-2-3j), below its footprint. Middle Q would require
(-m-2,-5-3m), below its footprint. A return V would need y=3(n-j)-2>=4,
since j<m=n-1. Final-fold phase15 is the first read of q and is R. These
are consecutive R reads, a contradiction.

## 4. m>=n and A=Q

For n=0, QQ is already impossible. For n>=1 use q=(-1,-1), last read by
initial Q at phase46 R. Outward V would require x=-3-j, impossible.
Middle Q would need(-3-n,-3-3n), below its footprint.

In return occurrence j, q has local(d-1,3d-1), d=n-j. For j<n-1 its
y-coordinate is at least5, so the first hit is j=n-1 at(0,2), phase12 R.
This occurrence exists because m>=n. The two consecutive R reads conflict.

## 5. m>=n and A=B

Take q=(0,-1), last read in initial B at phase3 L. Outward V would require
x=-3-j, impossible. Middle Q would need(-3-n,-4-3n): absent at n=0 and
below its footprint otherwise.

In the first n return occurrences q has local(d-1,3d), d=n-j>=1. At d=1
this is the absent(0,3), and at larger d it is above the footprint. If m>n,
return occurrence j=n first reads q at local(-1,0), phase1 L. If m=n,
the final fold first reads q at that same local coordinate and phase.
Again the two L reads are consecutive. In the equality case this contradiction
actually holds for ANY next macro, since every macro has the common phase1 L.

These cases exhaust all folds and parameter values. Consequently a feasible
interval over {V,Q,B} has at most two Q/B folds, hence at most three V runs.
The statement concerns exact physical read consistency, not autonomous-coset
legality. It does not establish freshness of V in the full five-macro alphabet.

## 6. Finite fuel for the alphabet {V,Q,B}

A run V^r requires exactly2r+4 black cells at run entry when r>0. Its first
macro has six distinct first-L cells. In every subsequent V the only new
first-L cells are local(-1,0) and(1,2): relative to the preceding V these
are(0,3), which is absent, and(2,5), above its footprint. Both are above
all still earlier V footprints. All other first-L cells were visited by
the immediately preceding V. Thus each later V adds exactly two required
entry-black cells.

A feasible word over {V,Q,B} has the form V^r0 F1 V^r1 F2 V^r2, with
zero,one or two folds and unused runs set to zero. From entry black mass m,
net mass changes V=4,Q=B=6 give the safe inequalities

    2r0 <= m,
    2r1 <= m+6+4r0,
    2r2 <= m+12+4(r0+r1).

These remain valid for empty runs. Hence r0+r1+r2<=13m/2+15, and the total
macro count is at most floor(13m/2)+17. This is a finite-fuel theorem for
{V,Q,B}, not the full alphabet.

In particular, every infinite five-macro tail on a finite-support board
contains infinitely many C or U blocks. Combined with the independent
V-free theorem, it must also contain infinitely many V blocks. Combining
further with the CVB theorem, either U occurs infinitely often, or all of
C,Q,V occur infinitely often. None of these necessary conditions proves
full-five V-tip freshness or eventual standard-language membership.
