# High-macro junctions force a triangular run normal form

24 October 2026. Author result pending independent review. The local
cover assumes only complete WHITE histories of at most four reads at
all its displayed/count-closure cells. It is an exact junction cover,
not a period, length, support or imposed-radius scan. Open ports retain
arbitrarily old exterior chronology.

## 1. Complete local macro and junction domain

In its own incoming-E frame each high macro is exactly one of

    A = RR3: source EWE, sink SSS;
    B = RLR3: source EWE, LEFT NSSS, sink EEE;
    C = RR4: source EWEW, sink SSSS.

The displayed words are physically rotated while traversing the macro.
Each macro has incoming and outgoing cycle flow TWO. The internal edges
are flow THREE or FOUR. These are the actual short macros from the
signed mixed RR closure f008184d, not repaired transitions. Their other
ranks remain complete and present.

Join any ordered pair of these macros by either one or two passive
flow-two LEFT V contacts. There are 3*3*2=18 primary physical stencils.
Normalize the first source to (0,1), incoming E, then traverse every b
edge to fix ALL coordinates and headings. Add only cells that complete
two already known neighboring ports and iterate this finite corner
closure. At each missing corner retain the empty history and EVERY
1..4-read WHITE history on the physical incoming axis.

Match every physical count, including zero, then every ordinal edge.
A literal return to one physical cell must hit its next complete rank.
Remaining exact successor edges take one step and same-cell rank gaps
are at least four. No stream-height/global-M or critical-side filter is
used in this executable.

## 2. Exact finite result

There are precisely 3,816 count-compatible completed patches:

    3,556 literal physical-rank failures;
      232 positive exact-clock cycles;
       28 necessary OPEN patches.

Every one-V junction is excluded. Every junction whose SECOND macro is
RLR3 is excluded, including both the V and VV separators. The only open
ordered pairs, all with separator VV, are

    RR3 -> RR3:  1;
    RR3 -> RR4:  1;
    RR4 -> RR3:  1;
    RR4 -> RR4:  1;
    RLR3 -> RR3: 20;
    RLR3 -> RR4:  4.

These are necessary local complete port/clock patches only. The 28 open
patches have unfilled exterior channels; none is declared an attained
board factor, phase schedule, translating front or renewable controller.
No older reader at an open channel can repair a rejected internal
literal rank return, but a larger completion of an open patch is not
asserted or excluded.

## 3. Run normal form on a critical GLOBAL-M boundary

Now assume a complete WHITE cap-four front, actual FULL P,d, and a
b-circle Gamma at GLOBAL maximum M=c_right+1 with no one-use edge.
The signed whole-flow inventory f008184d makes every maximal flow-three
macro RR3 or RLR3 and every flow-four macro RR4. All other RIGHT contacts
are flat flow-two X/Y. No omitted long-three template is imported here.

Consider any maximal high-macro run between consecutive flat RIGHT
contacts, with no flat inside. Between two of its high macros, the
flow-two LEFT separator has one or two contacts: three LEFTs would close
a physical unit square, incompatible with the embedded essential b
circle. A crossing O/U cannot be first in that separator, because its
immediate predecessor is a high sink, whereas signed f59ebed0 forces a
flat predecessor. It cannot be second by signed dba869f4. Therefore the
separator consists entirely of passive V contacts.

Section 2 forces every internal separator to be VV, and every macro
AFTER the first to be RR3 or RR4. Thus the exact run language is

    (RR3 or RR4), (VV, RR3 or RR4)*;
    RLR3,         (VV, RR3 or RR4)*.

In particular a high run contains AT MOST ONE genuine flow-three LEFT
crossing, and it must be in its FIRST macro. No high macro can internally
launch another RLR3 crossing. Its launch must instead come through the
preceding flat interface. RR3/RR4 rail length and their repeated choices
remain unrestricted; this is not a bound on the number or clock span
of high macros.

The exact open one-RR-pair-to-next-RR-pair geometry returns to the same
incoming heading after RR,VV, so successive sources lie on an axial
rail with displacement two in the source's first outgoing direction.
The word is a physical run normal form, not a chronological collapse or
an ant splice: every odd source/sink read, fourth use and late L3 remains.

## 4. Scope and remaining matching problem

This does not by itself exclude a high run, a two-flat or many-flat
circle, a noncritical M, or a circle containing a one-use edge. It does
not pay any source by original fuel or bound stock ages. Full-drift
voltages are still required when a run reaches its next flat; a strict
spatial step in an axial rail alone is not a contradiction.

The remaining exterior problem is exact exit/entry matching between
these flat-ended rails and actual same-contact LEFT excursions. In
particular different rails may be owned by different translated roots.
The run normal form must not be mistaken for an attained translating
front or a globally acyclic macro graph.

Files: check_high_macro_junctions.py/json. The finite physical-port and
rank utility is imported from the signed retained checker; its height
part is explicitly omitted, so no maximum condition is hidden locally.
