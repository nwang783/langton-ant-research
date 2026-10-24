# Fresh diagonal records: exact local transfer and the global gap

## Status

This note gives exact consequences of the supplied fresh-cap theorem. It does not prove the highway conjecture and does not claim priority. The six-step table below is also a direct proof that does not require that theorem. The first-return form is the `k=0`, `j=1 or 2` case of its upper-excursion decomposition.

## 1. A scope correction about escape

The known unboundedness theorem means that no finite region contains the entire future path. It does not assert that every fixed cell has only finitely many future visits. The latter is transience. Etse's MFCS 2026 work bounds a first exit from a finite domain, and does not remove this distinction.

Primary source: Kossi Roland Etse, *How Long Can The Escaping Ant Be Confined?*, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.49 .

The prior local research already proves a conditional diagonal-half-plane transience result and a conditional strip-to-periodic result. These facts must not be used without their confinement hypotheses.

## 2. Record levels advance by two in the relevant phase

Write `s=x+y`. Fix the heading sector in which even s has horizontal arrivals and odd s has vertical arrivals. A first visit to a white odd row from below has incoming heading N. The required right turn sends the ant east, immediately increasing s once more. Thus a virgin upper record at an odd level is followed by the next even record before a return.

Beyond the maximum level of the initial finite black support, completed upper caps are therefore on the even phase. When a cap moves from s to s+2, the new T and A rows are virgin. The former T and A rows become B and C. The problem is their old color history; there is no need to assume that the former T is still a fresh A row.

## 3. Six-step record transfer

Let p be the first old-cap cell from which the ant exits above `x+y=s`, at a time when the whole region `x+y>s` is white. Before this exit, its incoming heading is E. An incoming W would require a previous position above the old cap. Its color must be black, since white with incoming E turns south.

Translate p to `(0,0)`. The six processed events are:

| Event | Cell | Incoming | Color | Outgoing |
|---:|---|---|---|---|
| 0 | (0,0) | E | black | N |
| 1 | (0,1) | N | white | E |
| 2 | (1,1) | E | white | S |
| 3 | (1,0) | S | white | W |
| 4 | (0,0) | W | white | N |
| 5 | (0,1) | N | black | W |

The turn word is `LRRRRL`. The ant ends at `(-1,1)`, heading W. The exact board change is

`B_after = B_before union {(1,0),(1,1)}`.

These two cells were initially white. In particular, `(0,0)` is black again and `(0,1)` is white again. All lower cells and all other old-cap cells are unchanged. Translation gives the formula for general p.

This is a universal statement about arbitrary colors below and on the old cap, subject only to the stated black sponsor and virgin upper region. The path reads no other old cell.

**Consequence.** A fresh record birth does not consume its old black sponsor. That cell is restored. Each such macro has net black growth two. A proof that charges every new record to a different initially black cell is therefore invalid.

## 4. The first physical return has two cases

Let `q=p+(-1,0)` and `z=p+(-1,1)`. Include the departure from q that first entered p. That departure is possible with either color at q: incoming N when q is white, incoming S when q is black.

After the six-step macro:

- If z is black, its next turn is left to S. The ant returns to q after eight total updates.
- If z is white, the next five turns are `RRRRL`. This makes one more fresh top diamond and returns to q after twelve total updates.

No interior event visits q or the row below q. The end heading is S. The endpoint color at q is opposite its departure color.

The first branch visits one top square and the second branch visits two. This is precisely the zero-edge component in the supplied cap decomposition, with one or two top diamonds.

If q was black on departure, it is white on return and then turns W, entering the lower region. If q was white on departure, it is black on return and turns E, beginning a further upper excursion. In the first branch, this next upper excursion can immediately reach the next new cap. Thus the local law does not force a return below all four rows before another record.

## 5. Exact checks

`record_birth.py` checks the literal six-step path and all four choices of the q and z colors. It checks the full changed set, the final pose, first-return status, the number of top visits, and the read footprint. No long simulation or extrapolation is involved. All cases pass. The complete event records are in `record_birth.json`.

## 6. What would still be needed for a global argument

The cap bookkeeping remains valid when new records are two levels apart. To combine caps, a proof must retain three pieces of information:

1. The old T and A colors now occupy the new B and C rows.
2. A black sponsor can be restored by its own new top loop.
3. A first return to C can launch another upper excursion instead of leaving the region.

The finite initial support does not itself bound the number of later sponsor restorations. The local identities give no such bound. A proof would need a decreasing quantity that also accounts for the newly made black lifetimes, or a classification of all permitted sequences of these returns. Neither follows from the displayed six-step transfer.

## 7. Other global routes inspected

The earlier workspace already contains a correct conditional crossing-sequence reduction: a finite-support path confined in a fixed diagonal strip becomes periodic. It also contains a quantitative lower bound on the transverse width of a directionally escaping nonperiodic path. These statements do not establish their confinement or directional hypotheses.

The same workspace already rejects monotonicity of several frozen-loop and Tait-graph quantities by exact examples. The active loop can split and then recover the same old loop partition two steps later. Simple component count, cycle rank, or detached-loop size is therefore insufficient as a strictly decreasing quantity.

No proof of global capture, no proof of transience for every finite seed, and no alternative highway was obtained in this investigation.
