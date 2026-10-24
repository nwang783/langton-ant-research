# Executed all-coordinate bounded-seed solver with verified parity templates

2026-10-23 04:24 UTC. New implementation submitted for independent audit.
No growing model is accepted. General template extraction remains absent.

presburger_bounded_seed.py joins the exact A=I read-set compiler to unknown
seed coordinates. It supplies M slots (a_i,bx_i,by_i), with a_i in{0,1} and
unbounded integer coordinates. B is the UNION of the active points, so
inactive slots and duplicates correctly represent every seed of mass<=M,
including the empty seed. There is no guessed coordinate box.

Each supplied template must be a parameter-free [r,x,y] set in the same
ISL context; extra parameters, wrong dimensions/order and foreign contexts
are rejected. Nongrowing positive controls are explicitly not accepted as
growing models.

The only supplied mathematical certificate is the Presburger parity-read
relation Q_s(r,x,y) for each reachable letter. Its exact zero-depth value
and full substitution recurrence are checked by libisl. Therefore an
accepted parity certificate is the TRUE all-depth parity array, independently
of ant legality. A failed certificate is reported as invalid, not as proof
that the presentation has no realizing seed.

Actual representative prefixes define the canonical input boards as in IJ,
now with all seed slots left symbolic. Each bad base/frame relation is
projected to the seed-parameter space; subtracting their union from the
active-bit domain gives exactly the feasible seed assignments. The exact
Q base and recurrence supply the output-toggle identities, with outputs
defined as input XOR Q. No independent reset boards are chosen.

For efficiency a zero-depth slice of every frame is tested first. If those
finite constraints already exclude EVERY seed assignment, returning NO is
complete. Otherwise all depths are checked. All resource errors propagate
as errors/UNKNOWN, never as empty sets. An initial cumulative operation limit
was reached during development; restricting discrepancies to their actual
read guards and using the exact finite precheck completed the frozen controls.

Controls:
- Identity R and identity L at mass bounds0,1,2 produce exact feasible
  parameter formulas. R permits precisely seeds white at the origin; L
  requires the origin black. These are nongrowing controls only.
- The growing R^(5^r) control has no realizing seed at each of those three
  bounds, with ALL integer seed coordinates quantified.
- A forged parity base and a forged parity recurrence are rejected before
  any realization conclusion.

No automatic extraction of arbitrary parity templates or general ant-to-XOR
edge projection is implemented. This is an executed sufficient-certificate
interface to the signed bounded-mass decision theorem, not a new claim of
unrestricted finite-seed decidability or a counterexample.
