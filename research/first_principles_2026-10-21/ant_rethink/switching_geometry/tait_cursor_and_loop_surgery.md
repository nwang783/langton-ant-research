# Exact Tait cursor dynamics and the limits of a loop-stack reduction

## Scope

This is an exact reformulation of the ordinary two-color Langton rule. It
does not prove eventual periodicity. The underlying Tait-graph construction
is already in Jillhewar's paper, Section 4, at commit
`76a7e234e577d992d086c204c3dea00ae72cf10a`:
https://github.com/Atharva12456/langtons-ant-highway/blob/76a7e234e577d992d086c204c3dea00ae72cf10a/paper/main.tex

The cursor description below makes the physical transition explicit. The
compressed rule supplies a useful restriction: its walk never immediately
backtracks. The proposed reductions to a permanently discarded component or
a single last-in-first-out stack both fail on short exact blank-board traces.

## 1. Coordinates and the graph

Use Cartesian coordinates with y increasing northward. Headings are
E,S,W,N, encoded by 0,1,2,3. White turns right; black turns left; the cell is
toggled before the ant moves.

Choose the parity sector in which even x+y cells receive vertical arrivals.
Starting at (0,0) facing north has this sector. The other sector follows by
rotation. A black cell z=(x,y) represents the present undirected edge

    e_z = {(x,y-1),(x-1,y)}       if x+y is even,
    e_z = {(x-1,y-1),(x,y)}       if x+y is odd.

The graph vertices are the lower-left corners of the odd checkerboard unit
plaquettes. These form a square lattice rotated by 45 degrees. A finite black
board is a finite present-edge set on that lattice.

The cursor vertex is the plaquette on the right side of the ant's incoming
edge. If the physical cell is p and its incoming heading is h, the cursor is
v=p+o_h, where

| h | E | S | W | N |
|---|---|---|---|---|
| o_h | (-1,-1) | (-1,0) | (0,0) | (0,-1) |

The physical cell p is one of the four corners of this plaquette, and e_p
is an edge incident to v. The clockwise order of the ports, expressed as
plaquette corners, is SW, NW, NE, SE.

## 2. Exact one-update rule

At cursor vertex v and port e:

1. If e is absent, insert it and keep the cursor at v.
2. If e is present, delete it and move the cursor to the other endpoint.
3. At the resulting vertex, select the next clockwise port after e.

This is exactly one physical ant update. It follows by checking the two
colors at the four possible incoming headings. No state information is
discarded.

## 3. Compression between cursor crossings

At a fixed cursor vertex, process successive absent ports clockwise,
inserting each, until the first present port is encountered. Delete that
edge and cross it. If all four ports are absent, insert all four and then
delete and cross the first one.

After any crossing, the incoming edge at the new vertex has just been
deleted. It is absent. Start scanning at the next clockwise port. Let r
be the number of insertions before the next crossing. Then

    r is in {0,1,2,4}.

The value 3 cannot occur: its candidate departure edge is precisely the
absent incoming edge. If the other three edges are also absent, the scan
inserts all four before it can cross an edge.

| r | Physical updates | Black-count change | Cursor turn |
|---:|---:|---:|---|
| 0 | 1 | -1 | left |
| 1 | 2 | 0 | straight |
| 2 | 3 | 1 | right |
| 4 | 5 | 3 | left |

Thus the cursor walk between crossings does not immediately reverse an
edge. The r=4 case occurs exactly when its arrival vertex has degree zero.
It inserts a four-edge star, then deletes and crosses its first edge, leaving
three present edges at that vertex.

For r=0,1,2, the degree at departure is at most two. A degree-three departure
occurs only in the r=4 case. Degrees at vertices elsewhere can change when
an incident edge is inserted or deleted from the other endpoint.

The signed lifted clockwise turn r-1 equals the black-count change. The
geometric left turn in the r=4 case has an additional full clockwise turn
in this lift. Therefore, on any segment of the compressed walk,

    black-count change = geometric quarter-turn sum
                         + 4*(number of degree-zero arrivals).

This identity concerns a chosen geometric turn of -1,0,+1 for left, straight,
right. It is an accounting identity, not a decreasing quantity.

The script `check_tait_cursor.py` exhausts all 32 local arrival cases: four
incoming port choices and eight edge masks with absent incoming edge. It
compares each compressed case with the original ant rule. Every case passes,
including the turn, duration, mass change, and departure-degree checks.

## 4. Frozen loop surgery

For a fixed board B, keep the colors fixed and let F_B route every admissible
directed physical state by the turn rule. The resulting frozen trajectories
are finite directed loops when B has finite support. In the Tait picture they
are boundaries of regular neighborhoods of the present graph components,
with untouched white plaquette loops elsewhere.

At the active physical state a=(p,h), let b=(p,h+2) be the other admissible
incoming state at that cell. Toggling p swaps the two outgoing images:

    F_(B toggled at p) = F_B o (a b).

The true ant next occupies the old state F_B(a). There are two cases.

* If a and b lie on different frozen loops, their loops merge.
* If one frozen loop has cyclic order a,d,...,b,e,...,a, toggling splits it
  into the active loop d,...,b,d and the inactive loop e,...,a,e.

The active loop strictly shortens at every split. A merge can make it longer.
This gives an exact split-and-merge description, with the active loop marked.

## 5. Why detached loops cannot simply be deleted

The blank-board trace starts at (0,0), north. Time t below means immediately
before physical update t, with the initial state at time 0.

* At t=4 it splits off a dormant frozen loop of length 16.
* At t=8 the active loop reattaches that same loop.

Hence detachment alone does not certify permanent inaccessibility.

A single last-in-first-out stack also fails:

* At t=15, a dormant loop of length 4 is split off.
* At t=16, a dormant loop of length 12 is split off.
* At t=17, a second dormant loop of length 12 is split off.
* At t=18, the active loop reattaches the loop born at t=15, while both
  later-born loops remain dormant.

The exact state lists, board, and event history are in
`loop_stack_counterexample.json`, generated by
`loop_stack_counterexample.py`. These are finite counterexamples to the
proposed reductions, not evidence for an infinite recurrent trajectory.

## 6. Why the local switch is not an abelian processor

Consider one initially white physical cell in the vertical-arrival sector.
With incoming directions north then south, the two outgoing directions are
east then east. With south then north, they are west then west. The final
color is white in both cases, but the output multiset changes with input order.

Thus the ordinary local commutativity condition used for abelian networks
fails. This does not exclude a larger-state conjugacy or a global normal form.
It does exclude treating these two input orders as interchangeable without
another argument.

## 7. Cycle rank does not supply the missing monotonicity

Write beta=E-V+k for the total cycle rank of the finite present graph.
From the empty board, beta reaches 69 within the first 12,000 physical steps.
The standard period later adds 12 edges, 13 nonisolated vertices, and one
component, so its net change in beta is zero. The emitted component is a
12-edge tree.

This makes cycle rank a plausible measure of nontrivial old geometry, but it
does not bound it in terms of initial rank: the empty board has initial rank
zero. Nor is the cursor's component rank monotone; it ranges from zero to
five over the measured standard period.

The computations in `component_stats.py` and `beta_blank_12000.json` diagnose
these proposals. They do not prove a global bound or eventual stabilization
of cycle rank.

## 8. Remaining route

Any valid normal-form argument must retain enough information to predict
which dormant component can reattach and from which side. The exact cursor
rule reduces the local cases, but its edge bits are shared between endpoints.
Insertions can change an unvisited neighbor's future local state. A proof of
global capture still needs control of this nonlocal feedback.
