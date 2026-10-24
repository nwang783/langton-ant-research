# The retained ten-read prepared factor has boundary winding three

24 October 2026. Author exact diagnostic; independent audit pending.
This is not a new wave or a finite-seed autonomous controller.

The literal word RRRRLLLLRL is already retained among the minimum-board and
empty-cursor controls. With incoming N at(0,0), its complete initial BLACK set
is{(-1,-1),(-1,0)}. The actual ten reads return incoming N at(1,1) and leave
exactly{(0,0),(1,-1)} BLACK. Every unread cell is WHITE in this finite control.

Under full drift(1,1), its complete stable read histories are two RLRL classes,
one BLACK-input singleton L, and one output singleton R. The input is event5
at(-1,0); the output is event2 at(1,-1). Both are actual lifetime endpoints,
not an omitted prepared-background assumption.

The exact alpha/beta graph has no internal components and two boundary paths:

- Vertical path O2 to I5 has voltage+2, physical displacement(0,3).
- Horizontal path O2 to I5 has voltage-1, physical displacement(-3,0).

Traversing the vertical path from O to I and the horizontal path backwards
gives one two-root boundary cycle with FULL winding2-(-1)=3. Thus primitive
unit boundary winding is false for general complete alternating prepared
fronts, even when every actual lifetime and the one actual event cycle are
retained. This does not disprove a complete-WHITE-specific theorem.

## Exact all-N finite fuel relation

Put d=(1,1), C=(-1,-1), I=(-1,0), O=(1,-1). For every integer n>=1, initialize

    B0 = {C} union {I+k*d : 0<=k<n},

with head(0,0), N. Exactly n copies of the ten-read word occur. At time10n,

    B(10n) = {C+n*d} union {O+k*d : 0<=k<n},
    head = n*d, incoming N.

Proof: the literal one-period relation replaces C and I by C+d and O.
The complete full-drift input and output classes are distinct and each is
read only at its indicated single phase per period. Hence all later input
cells and earlier output cells remain unread during the induction step.
There are no hidden helper fields or discarded output cells.

The next five turns still agree with the word, but at time10n+5 the next
input I+n*d is WHITE and the actual turn is R rather than the required L.
An infinite run of this exact word therefore requires infinitely many
prelaid BLACK input cells. The all-N finite examples are not regenerative
controllers and do not contradict finite-seed highway conjectures.

The certificate includes full literal fields, all complete stable histories,
the full boundary graph, and finite controls n=1,2,3,10,31. The all-N claim
uses the exact induction above, not those samples alone.

## Artifacts

certify_prepared_ten_boundary_winding.py
SHA256 3505150c66cca008f2fe3fd565a4fc0f154c39647dea68988f662810b886a2a8
prepared_ten_boundary_winding_certificate.json
SHA256 33330d07c4e865039935d4d06eab173987b6c344852f0529e881c55c1d1b5a4b

No claim of novelty relative to literature or the retained library is made.
Only this newly computed boundary-winding diagnostic is being added.
