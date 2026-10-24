# Exact upper-excursion decomposition under a two-row fresh cap

This is a further structural consequence of the physical event graph in
`fresh_excursion_third_row_charge.md`. It describes actual finite
trajectories, including arbitrary old colors on the next rows. It does
not claim capture or a monotone global budget.

## 1. Setup

Use the same coordinates and hypotheses as that note: initially white
rows T and A at levels 0 and -1; arbitrary B,C and lower rows; a finite
trajectory starting and ending below C and never crossing above T.
Let Q=2M-Delta_A be the number of black A events. Let D count extra white
B upper corners after removing the M corners charged to top diamonds.

A C upper excursion starts with a departure from C into the region
strictly above C, and ends at the next visit to the C row. Such excursions
are complete because the entire trajectory starts and ends below C.
Every C upper departure has heading E and every upper return has incoming
heading S. An upper excursion can end at a different C cell from its start.

## 2. The event graph consists of directed paths

Its vertices are black A events, with an edge for each extra B corner,
directed from that corner's predecessor at A_(r+1) to its successor at A_r.
Each vertex has at most one incoming edge and at most one outgoing edge:
the relevant B events, if present, immediately precede and follow it.
Along every edge actual event time increases by two and the A index
decreases by one. The finite graph therefore has no cycles and consists
of directed paths, including isolated vertices.

It has exactly Q-D connected components. Write c_+ for the number of
components containing at least one edge. The number of isolated vertices
is exactly

    I = Q-D-c_+,
    0 <= c_+ <= D.

The event-level charge already proved gives K_C>=I. Equivalently,

    K_C+2D-Q >= D-c_+ >= 0.

Thus the nonnegative slack Z from the third-row note has the more explicit
decomposition

    Z = (K_C-I)+(D-c_+).

The second term counts the internal vertices of nontrivial directed paths,
or equivalently the sum of k-1 over paths with k>=1 edges.

## 3. Each graph path is exactly one nontrivial C upper excursion

Start such an excursion at C_r. Its first step E reaches B_(r+1).

If that B event is white, it turns S and immediately reaches C_(r+1).
This is a two-step right move and contains no A or T event.

Otherwise the B event is black, turns N, and reaches A_(r+1).
If this A event is black, the first event-graph vertex is reached directly.
If it is white, it makes its unique upper departure, traverses the top
diamond through T_(r+2), and returns to that same B cell on white. The B
corner then returns to A_(r+1), which is now black. Thus at most one top
diamond precedes the first black A event.

After a black A_s event, the ant moves W to B_(s-1).

- If that B event is black, it turns S and ends the C upper excursion at
  C_(s-1).
- If it is an extra white corner, it turns N to a black A_(s-1) event,
  traversing precisely the next event-graph edge.
- If it is a charged white corner, it must be the first endpoint of its
  top diamond. It traverses that diamond, returns to B_(s-1) on black, and
  immediately turns S to C_(s-1), ending the upper excursion.

No other case exists. In particular, a charged second endpoint cannot
immediately follow a black A event: its predecessor A event is the white
upper-arrival event in its diamond.

Consequently every nontrivial C upper excursion contains exactly one
maximal event-graph path and at most one top diamond at each end. A path
with k edges has k+1 black A vertices and connects

    C_r to C_(r-k).

If j in {0,1,2} is the number of its top diamonds, its step length is

    4+2k+4j.

Conversely every event-graph component occurs in this way, because every
black A event lies in one completed C upper excursion.

## 4. Exact consequences and their limits

The number of nontrivial upper excursions is Q-D. Each contains at most
two top visits, so

    M <= 2(Q-D),
    Delta_A+D <= floor(3M/2).

This last inequality also follows by charging the black endpoint of each
top diamond to a black B event, so it is not an independent new mechanism.
The decomposition explains its chronological content.

Each graph edge contributes one unit of leftward displacement to its
nontrivial C upper excursion. Across all these excursions that total is D.
All remaining upper excursions are two-step right moves through white B
lower corners. Their number is

    L_B = 3M-2Delta_A+Delta_B-3D.

The total number of C upper excursions is therefore

    L_B+(Q-D) = 5M-3Delta_A+Delta_B-4D,

agreeing with the exact row-flow identity. Their total signed horizontal
displacement is L_B-D. These statements concern the upper excursions only;
the pieces of trajectory below C can make unrelated displacements.

The refined third-row identity can also be written

    N_C = 12M-8Delta_A+4Delta_B-Delta_C
          -12D+4c_+-4(K_C-I).

Both K_C-I and D-c_+ are nonnegative, but their meaning remains local to
this completed excursion.

The precise obstacle to copying the same charge one row lower is visible
here. A nontrivial path with k>0 ends at a different physical C cell.
Its endpoint colors are not forced to alternate, and both cells may have
arbitrary old initial colors. It therefore need not give a new black C
corner. Only the k=0 components are literal physical first returns. Also,
C white events no longer all belong to unique fresh top diamonds: they
can be supplied by repeated interactions with B. The crucial argument
that an extra corner has black endpoints thus does not automatically
reproduce with C replacing A.

The 24-step sharp witness from the third-row note makes one tempting
strengthening explicitly false. It has Q-D=2 graph components but K_C=1.
The isolated component is the C first return from event 1 to event 13,
contains the black A event 7 and two top diamonds, and has length 12.
The one-edge component is the upper excursion from event 13 to event 23,
contains black A events 15 and 17 and one top diamond, and has length 10.
The black C corner at event 13 is shared as the first excursion's endpoint
and the second excursion's start. Thus there is no injective charge of
all graph components to black C corners: K_C>=Q-D would already fail on
this one-black, 24-step actual trajectory.

The decomposition gives an exact variable-length scattering rule at the
old substrate, including a token count Q and displacement count D. To turn
it into a global capture argument one still needs to control the lower
excursions, the signed changes in the old C row, and the change of fresh
cap when a new record is reached. None is discarded here.
