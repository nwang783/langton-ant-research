# Exact outward standard104 record guards, and what fresh first returns fail to determine

24 October 2026. AUTHOR exact synthesis, independent review requested. This strengthens the useful sufficient-interface side of the fresh-boundary bridge; it does not prove that arbitrary finite seeds reach any guard.

## 1. Eight actual outward record phases

Use the literal signed H104 in `TERMINAL_TRAP_CERTIFICATE.json`, with canonical starting heading S and displacement d=(2,-2). Let q_i, h_i be its104 pre-read poses relative to its initial head. For an outward integer normal n with a=n.d>0, phase i is a strict new record in the stable tail exactly when

    n.q_i > max( max_(j<i) n.q_j, max_(0<=j<104) n.q_j - a ).

The second term retains EVERY previous period: the immediately preceding period dominates all earlier ones because a>0. A finite initial seed and preperiod contribute only a fixed earlier maximum, so the condition is valid from an explicitly computed epoch onwards. The checker also verifies each selected cut against a complete actual finite-seed board, rather than deleting the older wake.

The COMPLETE phase lists for the following three outward directions are:

| Outward normal | Strict phases | Guard sizes | Required black counts |
|---|---|---|---|
| (1,0), east | 61,71 | 44,55 | 19,19 |
| (0,-1), south | 14,28 | 29,35 | 13,14 |
| (1,-1), actual drift normal | 45,46,55,56 | 19,25,30,36 | 15,16,15,16 |

These are eight phase/direction pairs, not a claim to classify every possible integer supporting normal. Quarter-rotating the ENTIRE board, heading and normal gives the corresponding rotated statements.

At each displayed strict record cut, normalize the head to0. All currently black cells satisfy n.x<0, and the current cell plus whole half-plane n.x>=0 is white. This is precisely compatible with the geometric information supplied at a new boundary.

## 2. Exact finite guards with immediate standard capture

For one selected phase, let W be the corresponding cyclic rotation of H, and let V_j be its read positions from normalized head0 with actual heading h_i. Its entire future read set is

    union_(k>=0,j) { V_j+k d }.

Define G as its intersection with n.x<0. Since n.d>0, it is FINITE: phase j contributes precisely the integer epochs

    0 <= k <= floor((-1-n.V_j)/(n.d)).

Let J consist of those G cells whose FIRST future read in W^infinity is L. The checker constructs all G and J, verifies the exact infinite ray/parity equations on the finite source J, and retains the full first-read table.

**Outward record-guard theorem.** At the indicated head/heading, ANY initial board B with

    B subset {n.x<0},              B intersect G = J

executes W^infinity. Arbitrary further old-side black cells are literally never read. Every required black bit lies on the OLD side, not ahead of a pristine head. Every G bit is necessary for this exact tail because its first read would detect a flip. This is not necessity for eventual capture by another route.

The largest old-side first-read time is266 or270 for the two east guards;179 and165 for the south guards;71,73,81,80 for the four drift-normal guards. These are exact finite fringe depths, not a numerical cap on arbitrary trajectories.

## 3. The smallest interface: phase45 has19 bits

At head0,E, pristine half-plane x-y>=0, the required black set is

    J45={(-4,1),(-4,2),(-3,-2),(-3,-1),(-3,0),(-3,3),
         (-2,-1),(-2,1),(-2,2),(-2,3),(-1,1),(-1,2),
         (0,1),(0,2),(1,2)}.

The only required old-side WHITE cells are

    {(-3,1),(-3,2),(-2,0),(-1,0)}.

These19 cells, plus the pristine forward half-plane, guarantee the exact canonical phase45 tail immediately. All19 are read within its first72 moves, and no other old-side cell is ever read. This criterion therefore avoids the tangential-ray obstruction: the drift has positive projection4 through its record normal.

## 4. Direct comparison with the retained diagonal-record theorem

Write q=(-1,1), sponsor p=(-1,0), z=(0,1). Start at q heading E, with q WHITE, p BLACK, and the entire half-plane x-y>=0 white. The first two turns RL reach head0,E at a genuine first new record. At that cut q is black and p is white. The universal six-step record birth from p is LRRRRL.

If z is BLACK, the exact first physical return to q has total length8 and word

    RLRRRRLL.

If z is WHITE, the first physical return has total length12 and word

    RLRRRRLRRRRL.

The return heading is W. The interiors do not revisit q. There are respectively one and two fresh top visits. These are the retained one-top/two-top scattering branches, with the same restoration of the sponsor. No new assumption about a universal language cover is made.

Phase45 is the first branch. At its record cut, that COMPLETE physical first-return history determines just THREE of the19 old guard bits:

    q black, p white, z black.

The remaining16 bits comprise13 required blacks and3 required whites. For EACH one, the checker flips that initially unread bit, starts from a complete finite old-side board, and replays the identical genuine record birth and first return. The proposed standard word then first diverges at the recorded first-read time. Thus even specifying this favorable signed first-return branch does NOT force the19-bit trap.

Phase55 is the second branch. Its30-cell old guard requires15 blacks and15 whites. The exact two-top first return fixes only q black, p white, z white. The other27 bits comprise14 required blacks and13 required whites; all27 have the same literal one-bit controls. First-return counts and every physical turn/read in that return are unchanged. Full Tait-component connectivity is NOT claimed unchanged, nor assumed by the fresh-record theorem.

The intermediate even-level records45->46 and55->56 occur one R move apart, as predicted by the record phase rule. All four record-compatible guards are certified separately; their chronological relationship does not supply the missing old bits automatically.

## 5. Global attraction target, now in concrete spatial form

The sufficient side is no longer hypothetical: there is an explicit outward pristine record state described by15 black and4 white old-side bits which yields standard104 immediately, and seven companion phase/direction guards. The retained fresh-boundary theorem supplies the correct fresh half-plane, local birth and physical first-return shapes, but the literal countercontrols show that those shapes leave many required old bits independent.

A genuine further bridge must prove that unrestricted lower returns eventually produce one of these guards, or another complete outward guard family. Neither the guard catalog nor its record countercontrols proves that forcing statement. The arbitrary finite-seed standard104 conjecture remains UNSOLVED.

## Artifacts

`check_outward_record_guards.py` uses only exact integer geometry, finite source replay and the local `check_fresh_record_trap_bridge.py` ray/parity helper; it does not import discovery geometry or an approximate detector. `OUTWARD_RECORD_GUARDS_CHECKED.json` retains every literal cyclic word, complete guard, guard first-read table, complete actual finite-seed control board and all43 one-bit first-return countercontrols. `OUTWARD_RECORD_GUARDS_MANIFEST.json` binds its dependencies.
