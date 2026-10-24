# A capped prefix bound with an unfinished upper excursion

This note supplies the chronological part of the exact endpoint identities in
`../global/partial_cap_port_identity.md`. It uses the stronger injective charge
proof in `arbitrary_cap_third_row.md`. Initial colors are arbitrary.

## Statement

Start at x+y<=-4 in the sector with horizontal incoming headings on T and B.
Stop at any finite time before a processed step leaves the cap x+y<=0. Count
processed events only. The current endpoint is unprocessed. Set

    F=12M-8Delta_A+4Delta_B-Delta_C.

Then

    N_C <= F+14.

The more precise endpoint bounds are:

| Endpoint | Additional condition | Bound on N_C-F |
|---|---|---:|
| T, incoming E | none | 14 |
| A, incoming N | none | 6 |
| A, incoming S | none | 2 |
| B, incoming E | none | 2 |
| B, incoming W | preceding A event was black | -2 |
| B, incoming W | preceding A event was white | 10 |
| C, incoming N | none | 0 |
| C, incoming S | none | 2 |
| below C | none | 0 |

In particular the endpoint may be an unprocessed black T cell, immediately
before the first step that raises the cap. Thus the theorem does not require
a completed return below C.

The constant 14 is sharp with the other coefficients fixed, even when T and A
start white. The two-black, twelve-step witness is proved in the companion port
identity note and retained in `../global/partial_cap_sharp_witness.json`.

## 1. Complete and partial roofs

Every processed top event is white, because a black top event would leave the
cap. Every processed top cell has been visited exactly once. The final endpoint
may be a second, unprocessed top arrival.

Use the roofs from the completed-cap theorem. Call a roof complete here only
when its ending B event is also processed. All but at most one roof are
complete. Let J_0 and J_+ count the complete zero-bridge and positive roofs.
Let H count all processed black A upper corners, including any in a partial
roof. Put

    rho=H-J_+.

Each complete positive roof contributes at least one bridge, and the partial
roof contributes a nonnegative number. Therefore rho>=0.

Let eta be one at an endpoint A,S or at an endpoint B,W whose immediately
preceding A event was white. Let eta be zero in all other cases.

At A,S or the stated B,W endpoint, the partial roof has k+1 processed T events
and k processed bridges. At a T,E endpoint, the partial roof has k processed
T events and k processed bridges; its final T event is still unprocessed.
At the other endpoints there is no partial roof containing a processed T
event. It follows exactly that

    M=J_0+J_++H+eta.

This does not require the A bridge cells to start black: the one endpoint that
can reuse an upper port is retained in the partial roof instead of being
mistaken for a complete roof.

Each complete zero roof gives one distinct processed white B upper corner.
Define

    D_0=E_B-J_0 >= 0.

The D from the port identity therefore satisfies

    D=E_B-M+2H=D_0+rho-eta.

In particular D can be -1 at an unfinished roof. It must not be discarded as
nonnegative at every possible endpoint.

## 2. Unmarked lower A events and the one possible unfinished charge

Mark a processed black lower A event when an immediately adjoining processed
white B upper corner is not charged to a complete zero roof. There are D_0
such corners, and each marks at most two black A events.

For an unmarked event whose adjoining B events are processed, the same local
construction as in the completed theorem gives its C first return: the two
sides are direct, or use one complete zero roof. The first return has a
unique black C upper corner at one endpoint. All complete assigned returns
have different charges, by the two-return color argument in the completed
proof.

The construction cannot stop inside a complete zero roof. It can stop on a
direct outgoing side only at B,W, immediately after the selected black A
turn, or at C,S, at the return's unprocessed C endpoint. These are the only
possible unfinished charges:

- At B,W with black A predecessor, at most the final processed black A event
  has an unprocessed adjoining B event. Remove that one event from the charge
  construction.
- At C,S, at most one assigned return ends at the current unprocessed C event.
  Its black charge, if the endpoint is black, has not yet been counted in K_C.
  Remove at most that one charge.

There is only one active upper excursion at the endpoint. The assigned return
contains only its selected lower black A event. Thus either omission costs at
most one event, not an unbounded number of events along a partial chain.

At an unfinished roof (A,S or B,W with a white A predecessor), there is no
unmatched lower black A event inside the roof. Its A events are white endpoints
and black *upper* bridges. If a black lower A event immediately precedes its
white B starting corner, that corner is not charged to a complete zero roof,
so the event is marked and has already been included in the 2D_0 allowance.
The same reasoning covers a partial roof ending at T,E.

Let nu be one at C,S or at B,W with a black A predecessor, and zero elsewhere.
The injective assignment therefore proves

    K_C >= Q-2D_0-nu.

Put

    Z_0=K_C+2D_0-Q >= -nu.

The completed theorem is the special case eta=nu=0.

## 3. Combine the charge with the exact endpoint algebra

The companion note proves, from upper-port counts alone,

    N_C=F-8D-4Z+epsilon,
    Z=K_C+2D+H-Q.

The endpoint values of epsilon are 14,6,-14,2,-6,0,-2,0 in the table's order
before splitting the B,W row. Since D=D_0+rho-eta,

    Z=Z_0+H+2rho-2eta.

Consequently the following identity is exact:

    N_C=F+epsilon+16eta
        -8D_0-4H-16rho-4Z_0.

Here D_0,H,rho are nonnegative and Z_0>=-nu. Therefore

    N_C-F <= epsilon+16eta+4nu.

Substitution gives each endpoint bound in the table. Their maximum is 14.
This proves the universal capped-prefix inequality.

For the first-record endpoint T,E, eta=nu=0, so there is the stronger exact
form

    N_C=F+14-8D_0-4H-16rho-4Z_0,
    D_0,H,rho,Z_0>=0.

No incomplete visit is treated as a completed charge in this formula.

## 4. What is still needed globally

These bounds permit stopping at a record exit. They do not identify the rows
of consecutive caps. After the cap rises by two, old T and A become new B and
C. Their stored colors must remain in the signed Delta terms. Also the +14
allowance is paid at every new endpoint, rather than from a proved finite
initial budget. A global capture proof still needs a bound on the accumulated
interaction with that changing substrate.
