# An exact root-return interface, and a conditional local dictionary obstruction

24 October 2026. Author proof; independent review pending. This concerns the
live complete WHITE drift(3,1), growth8 middle-short branch only. Its exact six
T0..T10 interfaces are signed in6a240f5a/report9f0a6ffa, and its complete
24-event active-C core is signed in22ecb8ce/report56b2df29. Neither open core
order is excluded here.

## 1. Five actual free return words, not a finite alphabet

Cut the actual full period at T8.R0, at physical position z=(-8,0), incoming N.
The complete T8 history is either

    A: N N S N S S S S,
    B: N N S S S N S S,

with alternating R,L starting R. All eight reads belong to this SAME physical
cell. Its first time is0, its last time is P-18, and the fixed closing word
returns to z+d, incoming N, at P. This uses the signed exact P=s-a+18 identity.

There is an exact full-period factorization:

    A: D F1 O F2 E1 G E2 K,
    B: D F1 E1 G O F2 E2 K,

where the fixed words are

    D = RRRR,
    O = RLLL,
    K = LRLRRRRLRRRRLLLLRL.

D starts N/R at z and returns to z,N before its next L. O starts S/R at z
and returns to z,N before its next L. K starts S/L at z, has18 reads and ends
at z+d,N. These are literal paths, not commuting formal letters.

Each E is the word from an S/R read of z up to, but EXCLUDING, the immediately
next S/L read of z. It is a nonempty closed-head-pose excursion, with no
intermediate read of z. Every event in it has active C level at least7, so no
C1,C3,C5 class, on ANY translate, is visited. Its length is divisible by4,
but neither length, multiplicity, mass change nor exterior support is bounded.

Each F is the word from N/L at z up to, but excluding, the next S/R at z.
It returns to the same position with opposite heading. It starts LR. Its
first event is on C5; all subsequent events have active C level at least7.

G is the word from S/L at z up to, but excluding, the next S/R at z. It
returns to the same head pose, starts LLL, and its second read is exactly the
one-event core channel Z=T7.L1. Every other event is on active C level>=7.

Thus all five free words have exact physical endpoint and exclusion semantics.
They are NOT independently executable modules: their input fields and R owners
can cross their boundaries or the full period. No finite-state assertion or
bound on their words follows from this factorization.

### Exact four-step imported owner

For A, the imported T8.R2(S)->T8.L3(N) lifetime has age exactly4. For B the
corresponding T8.R4(S)->T8.L5(N) also has age4. In both cases the actual path is

    T8.R(S) -> T9.L(W) -> T6.L3(S) -> T5.L3(E) -> T8.L(N),

at physical positions

    (-8,0), (-9,0), (-9,-1), (-8,-1), (-8,0).

The first four turns are O=RLLL. There is no intermediate T8 read. T6.L3
consumes the exported T6.R2 from the Y channel; this is not an initial BLACK
input. The same-physical T6 producer lies on the preceding representative
copy of Y. Removing that seam would lose its true ownership.

The two E intervals lie strictly between the known core channels, by the
signed two cyclic orders. The decomposition therefore retains all core reads
and every exterior event; it does not infer an unread region from a field mask.

## 2. A small constructive attempt using actual standard returns

A natural finite constructive family replaces each free word by an actual
consecutive-cell return from standard104, rotated to the required root heading
and filtered by the exact active-C exclusions above. The COMPLETE finite
dictionaries so obtained, considering every consecutive pair in the full
standard drift-orbit histories, are:

E, five words:
RRRR; RRLLLLRR; RRRLLLLR; RRLLRRRRLLRR; RRRLLRRRRLLR.

F, seven words:
LRRR; LRLLLLRR; LRRLLLLR; LRLLRRRRLLRR; LRRLLRRRRLLR;
LRLLRRLLLLRRLLRR; LRLLRRRRLLRLLRRRRLLR.

G, three words:
LLLL; LLLRRRRL; LLLRRLLRRRRLLRRL.

All15 supplied returns are genuine positive finite factors of the SAME
certified standard infinite future. The certificate saves their complete
initial and final BLACK fields, every actual read and every L's actual R owner.
It does not discard the unread archive or call each factor WHITE-input.
Their individual legality emphatically does not imply their joins are legal.

Restricting all five free words this way gives7,350 specified combinations.
Every combination fails even finite physical color alternation, hence cannot
repeat on any board. However the proof is substantially more local than that
finite product, and does not need to restrict the last two free words.

## 3. The all-suffix local obstruction

The exact stronger statement is:

A: if F1,F2 belong to the seven-word F dictionary and E1 belongs to the
five-word E dictionary, the finite prefix D F1 O F2 E1 is illegal on every
initial board. G,E2,K and every later continuation may be arbitrary.

B: if F1 belongs to F and E1 belongs to E, the finite prefix D F1 E1 is
illegal on every initial board. G,F2,E2,K and every later continuation may
be arbitrary.

The transparent cover has64 terminal bad prefixes. Each contains TWO
CONSECUTIVE reads of the same physical cell with the SAME turn, together with
their exact positions, times and all intervening positions. No input-color
choice can repair such a violation.

For A, all seven D F1 prefixes are legal. Four fail when O is appended. Of the
remaining3x7 F2 choices,20 fail, leaving exactly one32-read prefix. All five
E1 choices fail after it. These are4+20+5=29 terminal witnesses, covering all
7x7x5=245 relevant choices without restricting any suffix.

For B, all7x5 D F1 E1 choices fail, giving35 terminal witnesses. Every branch
of this exact prefix tree is retained; no SMT, period cutoff, unexplained
solver status or large unexamined computation is used.

The sole A prefix before E1 is

    RRRRLRRRRLLLLRLLRRRRLLRLLRRRRLLR.

It is a genuine prepared32-read positive factor from exactly
{(-10,1),(-9,-1),(-8,2)} BLACK cells, with all other cells WHITE. It returns to
z with heading S and leaves exactly nine BLACK cells. Its full field and
trace are retained. This is only a positive PREFIX; none of the five standard
E returns can legally follow it. No claim is made that no other E can follow.

## 4. Exact scope

This rules out one explicit reuse architecture for the live nonstandard core,
not the core itself. An eventual completion must use an exterior return outside
the stated standard dictionary at the specified early point. Such a return may
exist at arbitrary length; larger prepared returns, different connectors and
fully self-fed continuations remain open. The theorem neither classifies all
return words nor proves WHITE unit winding, growth>=12, controller uniqueness
or finite-seed highway entry.

Artifacts: certify_middle_short_return_dictionary.py and
middle_short_return_dictionary_certificate.json. The latter binds the signed
core dependencies and contains all six physical O-return paths, all15 whole
standard source factors, the complete64-leaf cover and the32-read positive.
