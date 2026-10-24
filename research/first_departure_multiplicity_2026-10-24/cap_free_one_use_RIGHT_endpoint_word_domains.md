# Cap-free word domains at one-use RIGHT endpoints

24 October 2026. Author exact local all-multiplicity lemma pending review.
Complete WHITE cell history and ACTUAL total cycle-port counts are used.
No cap on this cell or exterior, global first-R maximum, complete-front
period, global support side or autonomous-controller premise is assumed.
The b-corner is geometrically RIGHT, incoming E/outgoing S, so R0 has
heading E. All other frames follow by physical quarter rotation.

## 1. One-use input, arbitrary positive output

If the incoming E port has total use1, R0 is the ONLY E arrival. Every
later arrival is W. The south departures are R0 plus every odd-rank W
read, so f_out=1+floor(n/2), where n is the complete history length.
For f_out=f>=2 the EXACT words are

    E W^(2f-3), or E W^(2f-2),

of lengths2f-2 and2f-1. For f=1 the only nonempty word is singleton E.
Thus1->2 is exactly EW/EWW;1->3 is EWWW/EWWWW. A one-use input alone
does not force a singleton or an odd-history endpoint.

## 2. Arbitrary positive input, one-use output

If the outgoing S port has total use1, its occurrence is R0. No later
R can arrive E, and no L can arrive W. Thus all odd arrivals are E and
all later even arrivals W. Since total E arrivals are f_in=f, there
are exactly f-1 odd reads. For f>=2 the EXACT words are

    EE(WE)^(f-2), with or without one final W,

again of lengths2f-2 and2f-1. Hence2->1 is exactly EE/EEW and3->1 is
EEWE/EEWEW. The1->1 word is singleton E, consistently with section1.
These domains are both necessary and satisfy the prescribed two port
counts; they do not themselves supply the remaining physical neighbors.

## 3. Optional stream-maximum qualification is explicit

The cap-free directed stream identity at any WHITE first-R corner is
h(C_R0)-h(C_opposite)=R_E-R_W. For EITHER endpoint family above this is
3-f in the even-length case and2-f in the odd-length case.

If an INDEPENDENT premise says R0 selects an incident C-height maximum,
that difference is nonnegative. Then f<=3 in the even case and f<=2
in the odd case. Such a one-use RIGHT endpoint is automatically at most
FOUR reads, WITHOUT imposing any exterior cap. This qualification holds
when the selected R0 C face is actually a GLOBAL maximum, but there is
no all-cap theorem here saying first R always selects a maximum or that
a whole first-R cycle has constant C height. Those are separate issues.

## 4. Partial one-use runs have a cap-free internal alphabet

A RIGHT1->1 vertex is singleton by the proof above. At a LEFT1->1 corner
normalized incoming E/outgoing N, R0 must arrive W. Since Nout=1,
R0 is its only R_W and there can be no L_E. Since Ein=1, the unique E
arrival is therefore R2, and no R4 can occur. The complete words are
exactly WWE or WWEW (three/four reads), independent of exterior cap.

These local statements apply to constant-one-use SEGMENTS, not just
a wholly single-used boundary. They do not identify first-R departures
with target last reads, exclude prepared BLACK input, remove optional
L3, prove an unread exterior row, or infer odd/fuel payment. In particular
the new even SN/EE LL portal endpoints do not rely on a cap assumption
at those two cells, though the larger portal still fixes its own rows.
