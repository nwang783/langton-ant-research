# One actual two-port excursion can hide unbounded defect work

23 October 2026,18:47 UTC. An exact new finite-seed construction deduced from
the independently signed394-family words. Its INITIAL mass grows with the
parameter. It is NOT a fixed-mass theorem or a noncapture construction.

## 1. Precisely fixed interface and exterior

Use the paired active vertices of coupled_dual_cursors_and_gate_memory.md in
sector zero. The INSIDE region consists of primal vertices with z_x+z_y>=1;
the outside has z_x+z_y<=-1. Physical cells q with q_x+q_y=0 are the cut edges.
Initially ALL these cut cells and the ENTIRE outside field q_x+q_y<=0 are WHITE.
The initial physical pose is the fixed outside port

    p=(-2,2), h=N,   active z sum=-1.

For every integer M>=1 there is a finite seed strictly on the inside, plus
two fixed inside additions, with the following actual continuous trajectory:

- first read R at (-2,2): cross inside through the fixed entry port;
- no further boundary read until the LAST read;
- last read R at (10,-10), heading S: cross outside;
- end at the fixed pose (9,-10,W), active z sum=-1.

The complete returned exterior, including the full infinite boundary, is
IDENTICAL for all M: just the two black cut cells (-2,2) and (10,-10), with
every other q of sum<=0 white. There are exactly TWO boundary R crossings
and ZERO boundary L deletions. This satisfies the exact gate identity:
R_cut=2, L_cut=0, Delta black_cut=2.

Yet duration and wholly-contained internal adjacent-defect count are

    duration =192957+28380M,
    K_internal=91827+13269M.                              (1)

Thus unbounded actual defect work occurs behind an unchanged boundary between
one fixed entry and one fixed exit. The exposure order is perfectly nested:
outside--inside--outside. There is no hidden external itinerary or teleport.

## 2. Explicit supplied word and forced finite input

Read the independently signed prepared4352_capture_manifest.json. Let

    W = its4352 word, entry(-2,3,W), drift(26,26),
    T = its fixed158151-letter source-transition word,
    P = its15324 return word, drift(-78,-78),
    Z = the first17395 letters of its38503 launch-end response.

Define the completely explicit finite word

    V_M = W^(3M+4) T P^M Z.

The signed original394 finite family, viewed at its wave entry, follows this
word for EVERY M>=1. Hence all repeated reads obey the exact flip rule.
Its minimal first-L seed A_M consists exactly of those physical cells whose
FIRST read in V_M is L. This is a finite deterministic seed definition from
an explicit word, not an assumption that a desired trajectory exists.
The all-M physical feasibility comes from the retained complete original-
board chronology, and deleting every unvisited entry black preserves it.

The stage read supports give

- W^(3M+4): min u=q_x+q_y is1;
- T: min u=156M+182>=338;
- P^M: min u=182;
- Z: all reads before its final read have u>=1, and the final read is
  (10,-10),S,R, at Z index17394.

Thus A_M has NO outside or boundary black cell. The two cells
(-1,2),(-1,3) are not read anywhere in V_M: the first W misses them and every
later W copy is shifted to min u>=53; T and P miss them by the displayed
lower bounds; the fixed Z trace misses them too.

Take the ACTUAL initial seed

    B_M=A_M UNION {(-1,2),(-1,3)}

at the fixed outside pose(-2,2,N), and prepend RLL. These three literal steps
are

    (-2,2),N,R ->(-1,2),E,
    (-1,2),E,L ->(-1,3),N,
    (-1,3),N,L ->(-2,3),W.

They insert the entry cut edge and remove the two inside additions, leaving
exactly A_M plus the black entry gate(-2,2). That gate is unread throughout
V_M, whose only boundary read is its distinct last R exit. Therefore the
whole word RLL V_M is legal on this one finite original seed, with no edits
after initialization. This proves the interface statement.

The initial mass is not claimed constant or given by an extrapolated formula.
Direct controls give5925 black cells at M1 and7266 at M2. These values are
implementation controls, not the all-M proof.

## 3. Exact counts, not a repeated-block heuristic

The length of V_M is175559+28380M plus17395 for Z. Adding RLL gives (1).
For K_internal count only eleven-letter windows wholly within RLL V_M, so
there is no dependence on its newly reinitialized inverse history. The
standard forbidden-ten set is the retained84 cyclic ten-factors.

Every supplied period has length greater than ten. After its first copy,
the ten-letter history is fixed, so further copy costs are EXACTLY stationary.
The literal costs are

    firstW after RLL:1973; laterW:1972;
    T afterW:75515;
    firstP afterT:7358; laterP:7353;
    Z afterP:8418.

Their sum is

    1973+(3M+3)*1972+75515+7358+(M-1)*7353+8418
      =91827+13269M.

True initial-history windows can add only a bounded initial adjustment;
the wholly-contained count already establishes the unbounded claim.

## 4. What finite interface forgetting this actually excludes

No deterministic finite separator-state replacement can preserve the exact
internal K cost or timed response for all these archives while using only
finitely many interior summary labels. Entry state, full exterior, full
boundary, and untimed two-event boundary transcript are all fixed, but both
cost and delay are unbounded. A finite set of terminating deterministic
summary states has only finitely many exact cost/delay outputs.

This does NOT rule out a qualitative UNTYPED/UNTIMED two-port map for this
particular family: all its members really return through the same port.
Nor does it rule out an abstraction carrying an UNBOUNDED integer supply,
length, or richer archive record. It does not prove a finite-state abstraction
impossible under every conceivable specification. The scope is exact
cost/timing-preserving renewal or a bounded per-interface defect charge.

Most importantly, even first-entry/last-exit noninterleaving and a fixed
boundary transcript do not bound hidden work. To forget an archive SOUNDLY
for future full dynamics needs a causal no-reentry/no-read shield, such as
the current occupied-fence rule; to retain its cost needs unbounded supply
information here. All M episodes remain finite, and no noncapture assertion
follows.

Source manifests: prepared4352_two_phase_manifest.json SHA256
ffd8a1393f96ad81b6d8515912b00304e5c4527b1a7b949644686e5c05d56715;
prepared4352_capture_manifest.json SHA256
52d80fe06d739254a9d71615de67bfb6639d1f4d1301455b4f332d7110874f9b.
