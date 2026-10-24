# An eight-read connector surcharge at every allowed pipeline phase

23 October 2026, 14:16 UTC. Author analytic corollary of literal H endpoint histories, pending independent review. This does not exclude longer connectors.

In the signed disconnected H/LR/Q input matching, let

H start at(2l,10+2l,E),
repair LR start at(-1+2t,6+2t,S),
Q start at(0,0,E).

The exact ordering conditions are l>=-1, t>=1 and u=t-l<=2. H ends at(2l+2,2l+12,E), so the connector target relative to that endpoint is

    (2u-3,2u-6,S).

The following bound holds for EVERY integer u<=2, independently of the other pipeline stages and of colors outside the just-completed H reads.

## Forced memory

Relative to H's own start, the endpoint cells have these complete last-event facts:

(2,2): reads32R,36L,40R, so is BLACK at the end;
(2,3): reads33L,37R,41L, so is WHITE at the end;
(3,3): read38R, so is BLACK at the end.

Consequently the next three turns after H are forced L,R,L. Starting at its endpoint with heading E, these three moves are N,E,N and end at relative position(1,2), heading N. No earlier writer or unspecified initial color can change this conclusion: each cell's last displayed literal H read fixes its current color, and the first two connector reads do not revisit the third.

## Exact geometric count

A connector from E to final incoming S with displacement(2u-3,2u-6) must have length n=4k+3. It has2k+1 horizontal and2k+2 vertical moves. Without the memory condition, u<=2 gives the exact geometric minimum

    n_min=11-4u.

At that length all vertical moves point S, and exactly one horizontal move points E. This direction count is realizable and ends S.

With the forced initial N,E,N, at least TWO vertical moves point N. The required vertical displacement then demands at least8-2u south moves, hence at least10-2u vertical moves in total. Thus

    2k+2 >= 10-2u,
    n >= 19-4u = n_min+8.

This strengthened bound is also kinematically sharp after the fixed three-move prefix: at equality the remaining vertical moves all point S, and the remaining horizontal slots contain exactly two E moves and all others W. It is not asserted to be color-realizable.

Therefore changing the allowed longitudinal phase cannot repair the shortest-connector failure. Every physically possible first connector needs an additional eight reads beyond its own geometric minimum. The original displayed phase u=1 needs at least15 rather than7; the most favorable u=2 needs at least11 rather than3. No claim is made about connectors at or above these lengths, later stages, a continuous front, or finite-seed realization.
