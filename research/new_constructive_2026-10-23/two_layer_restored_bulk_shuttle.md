# Full bulk restored, both endpoint caps retained

23 October 2026, 20:04 UTC. Author exact all-parameter continuation, audit pending.
This is a finite physical component, not a renewable shuttle.

Start with the COMPLETE returned field at (0,2,E) from the all-r,k>=10
component in two_layer_carried_endpoint.md/json. Put

    T = LRRL
    E = RLLRRRRLLRRRRLLRLRRRRLRRRRLLLLRLRRRRLRLLLLRRRR (46).

The ACTUAL next word is T^r E T^r RRRRLL, length8r+52, ending at (0,2,E).
At its penultimate RRLL the ant visits the changed endpoint (0,4,E), then
returns to (0,2,E). The entire straight-row bulk is restored, as are ALL
other cells outside the following TWO complete finite endcap changes.

Left endpoint:
  clear (-1,2);
  add (0,3),(0,4),(-1,4).

Right endpoint, all coordinates relative to (2r,0):
  clear (0,1),(1,1);
  add (-1,1),(2,1),(3,2),(3,3),(0,3),(1,3),
      (-1,4),(0,4),(1,4),(2,4),(0,5),(1,5).

These are exact all-parameter complete-field differences. Three black cells
are cleared and fifteen white cells added, giving net black gain12, independently
matching literal R-minus-L counts. The full output relation is frozen, so the
large unchanged remote frame residue is NOT discarded.

The exact chronological checker has60 affine read families,3540 ordered distinct
pairs and59 nonempty prior-read relations, with no bad-color set on the entire
cone r,k>=10. It independently checks the complete18-cell XOR and all three
cleared input cells. The two T sweeps preserve their input heading and move in
opposite directions; their full bulk toggles cancel, not just their black counts.
This word was selected from the same ONE stored r=k=10 orbit, with no new seed,
cap, horizon or parameter exploration.

This does not repeat immediately: the next same T would want R on its second
read at(0,3), but that cell has just been added black by this shuttle. Its two
caps have not reset. No cycle, family capture, indefinitely growing supply, or
counterexample follows. Any new composition must retain all18 changed cells
and the complete passive field, rather than using the restored bulk alone.
