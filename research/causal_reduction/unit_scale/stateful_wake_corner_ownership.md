# Stateful repeated-hit control and its exact ownership failure

Status: finite literal discovery controls, not an all-parameter scattering theorem or a single-ant return route. All fields from earlier runs are retained; each new arrival is explicitly supplied with its 13-cell standard phase seed. No renewal claim follows from the repeated changes of direction.

The signed first collision C emits an NE highway from (91,-63,E), normal coordinate x-y=154. In the finite setup n=m=100, after 100 outgoing periods, a new NW arrival at (315,-300,N), line x+y=15, turns NE as well. It reaches a canonical H phase at time 13335, pose (83,-59,E), normal142. The complete second initial and output boards and word are stored in `stateful_wake_corner_second_hit.json`.

This motivates, but does not prove, a third arrival on line27 and a translated second interaction by (0,12). `probe_stateful_wake_corner_third_hit.py` performs precisely this one test. It first completes the second tail phase and advances100 NE periods, retaining all cells, then supplies the disjoint13-cell phase seed at (327,-300,N). The predicted repetition fails. Actual time77127 gives a permanent canonical NE front at (57,41,E), normal16, not130.

Two exact ownership witnesses explain why the first two hits are not a translation rule.

1. Comparing the third literal word with H^6 followed by the second literal word, the first difference is at zero-based time12016 and cell(91,-66), incoming N. The predicted read is R, while the actual read is L. This cell is already black in the first complete collision output; it survives into the third input. This is an inherited-cell error, not a finite-tail detector issue.

2. Even removing that old-collision discrepancy would not establish the repeat. Define Q to be the second literal word after its first110 full H periods, extended to the next canonical phase. Q has length1895, starts at(95,-80,N), ends at(83,-59,E), and reads707 cells. Its translated copy Q+(0,12) has an immediate color-history incompatibility with Q: cell(80,-73) is last read R at Q-time614 and is first read R at translated-Q-time222. Thus any intervening route must toggle this cell an odd number of times. The outgoing NE H-ray from(83,-59,E) has all read normals x-y in[135,145], while this cell has153. The next standard NW arrival on line27 has all read sums x+y in[20,30], while this cell has7. Neither standard part can supply the missing toggle.

The second witness is independent of the initial coloring: absent an intervening read at that cell, two R reads cannot be consecutive. It is a conditional interface obstruction, not a ban on a new route that deliberately repairs the cell. In particular it does not assume the supplied arrivals can be executed by the departing ant.

## Reproduction

`check_stateful_wake_corner_ownership.py` recomputes canonical poses, first-difference position, the two Q histories and exact strip bounds from the frozen words and boards. Its output is `stateful_wake_corner_ownership.json`.
