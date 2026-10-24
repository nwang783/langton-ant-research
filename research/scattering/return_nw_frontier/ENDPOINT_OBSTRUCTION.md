# An old triggering bit can be restored rather than consumed

Status: exact certificate replay passed; independent review pending.

For the complete five-cell r28 family, m>=100 and n-m>=100, the pristine
three-rail infinite model is initially exact on the whole source strip
|u|<=200. Nevertheless its predicted infinite NW tail first disagrees with
the finite configuration after

    104(n-m)+7647 source steps,
    equivalently at global time728n+202729.

The disagreement is at the point

    b_n=(1-2n,58+2n).

This is not one of the five initial black cells. The complete earlier history
visits it exactly once, at time312n+111081, reading white and writing black.
It is then untouched until the new return, so its age is416n+91648. The
pristine model predicts a white read; the true finite field reads black.
This is an arbitrarily delayed, rigorously identified old-endpoint interaction,
not a numerical failure to see a sufficiently distant marker.

The 642-letter endpoint recovery visits this same point at relative phases
63,115,119,127,139,151, reading L,R,L,R,L,R. Thus the point ends BLACK again,
and remains black forever afterward. The outgoing standard NW highway has
all read levels35<=z<=45, whereas z(b_n)=59. It captures because of the
changed outgoing route, not because this triggering memory bit was exhausted.

The checker verifies every old visit over all parameters, excludes every
initial marker, verifies there is no earlier new-prefix visit, binds the first
word mismatch to the separately certified infinite model, and checks the
permanent outgoing separation. This illustrates two distinct limitations:

1. An infinite local rail model cannot be promoted to an infinite finite-seed
   trajectory without retaining distant endpoint information or proving an
   all-future avoidance condition.
2. Counting consumed triggering black bits is not a monotone resource argument:
   this particular old bit is exactly restored.

It does NOT prove restoration of the entire endpoint pattern, a renewable
circuit, or an obstruction to every finite-state interaction graph. A reusable
scattering theorem would need a complete interface state, its restoration or
update law, and guards against the full incoming and outgoing wake histories.

Artifacts: certify_endpoint_history.py, endpoint_history_certificate.json,
full_return_template_r28.json and full_return_certificate_r28.json.
