# The failed crossing actually realizes the extra-L obligation

23 October 2026, 16:06 UTC. Exact qualification from an existing frozen
transient, not a new ant simulation or a general crossing theorem.

The countermodel-owned files prepared1564_first_crossing_cell_history.json
and prepared1564_router_crossing.json give these actual reads at (383,380):

    94896 R(E); 205680 L(W); 205684 R(W);
    205688 L(W); 205692 R(E).

The last four are the first contacts of the supplied actual transient.
The twelve intervening turns are

    LLLL RRRR LRRR.

Each four-turn factor returns to that physical cell. The first two
return with incoming W, while the third returns with incoming E.

Thus the opposite-heading R pair R(E),R(W), impossible as two consecutive
visits, IS realized locally with the necessary intervening L. The actual
R(W) at 205684 uses the originally desired N output, four reads after
the first merge. The one-cell obligation is not a global obstruction to
realizing that corner pairing at a later time.

There are 20 recorded visits at this cell, including the last earlier
read and all visits in the actual transient through time 240864. The
last is at 221724. Their turns alternate, and every adjacent pair shares
exactly one incoming or outgoing physical port, as the all-cap lemma
requires. This is a partial whole-history window: the frozen prior read
is not represented as a proved first-ever visit. Relative window counts
are seven E and thirteen W inputs, and five N and fifteen S outputs.

In particular no cap-four plateau or two-R classification applies at
this cell. The countermodel's final wrong NE flight is a full-transient
fact; it does not follow merely from the first local merge. A compatible
clean-port crossing still needs a complete trace-level construction or
obstruction, retaining these repeated visits and all residual trails.

actual_contact_annotations.json checks the small literal twelve-turn
transport and annotates every consecutive pair in the supplied window.
No initial 200000-read prefix was replayed, no field was inferred anew,
and no asymptotic lane claim was added.
