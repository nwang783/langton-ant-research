# Exact bounded V-tip reuse synthesis

The target is a physically feasible five-macro word ending in V whose tip
(local (1,2), first L at phase 13) was read in an earlier macro. Any such word
can be trimmed to begin with the macro containing that cell's last earlier
read. This read must be R, and no intermediate macro reads the cell.

`smt_v_lastwriter.py` fixes the last V entry pose to (0,0,N), requires the first
macro to have last read R at (1,2), and forbids every intermediate macro from
reading (1,2). The pose recurrence uses exact macro endpoints and quarter-turn
rotations. Coordinates are 12-bit signed representations, but horizons below
250 and the first/last pose constraints keep all possible coordinates strictly
inside the nonwrapping range. The ordinary short C-gap grammar is included as
a redundant, already literal-certified restriction.

The direct version also models every entry color and odd-cell update with
functional arrays. This was too slow beyond small horizons, so the productive
version `smt_cegar_v.py` omits the color arrays and refines exact geometry by
literal infeasibility certificates:

1. Obtain a candidate macro word from the SMT model.
2. Replay its full turn word, recording the last read of each physical cell.
3. If equal consecutive reads occur, extract the factor from the earlier
   read's macro through the conflicting macro.
4. Independently replay this factor and confirm its conflict. Forbid that
   factor at every position in this and future bounded searches.
5. If a word is physically feasible, independently simulate it from its
   minimal first-L black seed and verify the final V-tip reuse.

Every learned factor is a translation/rotation-independent exact obstruction,
not an arbitrary blocked model. An UNSAT result therefore excludes the given
last-writer distance, assuming solver correctness. It is NOT an all-length
proof, and a solver timeout or iteration cap proves nothing. Results are not
restricted to the original H-port language unless the optional ports mode is
explicitly enabled; raw physical concatenations are the stronger search space.

The system libz3 is accessed through ctypes; no external package was installed.
`smt_cegar_v_learned.json` preserves all exact conflict factors. Each solver
input and per-horizon log is saved. Independent solver-model validation and
an independent bounded enumerator remain desirable before promoting these
bounded exclusions as audited certificates.
