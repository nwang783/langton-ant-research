# Mandatory F106/F107 visited-cell metadata qualifier

24 October 2026. This qualifier binds the immutable F106/F107 note 877ee07b,
checker 55dce079 and JSON c9b39d4d without rewriting any frozen source.

Both literal trajectories visit exactly 63 physical cells. The certificate
later accesses the two specified unused WHITE target cells through a
Python defaultdict, inserting empty entries. Consequently its final
physical_cells metadata says 65 and all_cell_histories stores 65 keys.
That metadata is a count of stored keys, NOT visited cells.

The corrected reading is: 63 visited physical cells; 65 stored histories,
including the two unused WHITE cells (-1,0) and (0,0). Those empty histories
are valid target constraints, not raw ant reads. The full word, input and
output boards, all raw reads, maximum factor multiplicity four, and every
nonempty history are unchanged. The assertion made before those insertions
already checks the 63 visited cells directly.

All prepared finite-factor limitations in 877ee07b remain mandatory.
