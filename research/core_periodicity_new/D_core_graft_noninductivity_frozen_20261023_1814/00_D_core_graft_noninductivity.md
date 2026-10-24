# Core-graft connectivity is not locally inductive by itself

This is an exact relaxation control, not a reachable historical-color counterexample.

Let K be the canonical five-cell core at pose (0,0,N). The eight-cell black board is K union {(0,1),(-2,0),(0,-2)}. It performs literal D followed by the actual marker. Its raw exit is (1,1,N), and its raw exit board is the new core together with D's fresh residual output (2,0) and the two unchanged remote residual cells.

Use the even checkerboard dual: an even-sum cell (x,y) is the diagonal edge between (x-1/2,y-1/2) and (x+1/2,y+1/2); an odd-sum cell joins (x-1/2,y+1/2) to (x+1/2,y-1/2). The core is a five-edge tree.

Assign the two untouched cells (-2,0) and (0,-2) ONE ARTIFICIAL historical component color C. Initially its two edge pieces are joined by adjoining the old core: the attachments are respectively (-3/2,1/2) and (1/2,-3/2). Neither edge meets the new core. Thus after the legal D rewrite the same two colored pieces remain disconnected even after adjoining the new core.

The coloring is deliberately not asserted to arise from an actual prefix. This establishes only that the predicate 'each disconnected historical-color edge graph becomes connected after adding the current core' is not an inductive consequence of that predicate plus the local D guard. A successful causal core-port invariant must exclude this artificial history or retain additional information. There is no physical monochromatic-U counterexample, no component-merger theorem, and no global fuel claim here.

The checker independently performs all ten raw D steps plus the eleven actual marker reads and records the raw exit separately. It also reconstructs the doubled-coordinate dual graphs and their exact connected components.
