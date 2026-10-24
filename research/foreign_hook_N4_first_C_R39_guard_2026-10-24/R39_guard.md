# The first-C route cannot reach one clock-four hook-loss gate

Status: author frozen, pending independent review.

## Exact target and scope

Normalize an actual Q/B RAW exit to head(0,0,N). Suppose the first subsequent ordinary RAW is C. There is no actual ordinary D/C/V/U continuation, of any length, reaching the following target U entry after exactly four ordinary Cs, with actual final M11:

* Q target U(-1,-5,N).
* B target U(0,-6,N).

No U ancestry or simple proxy assumption is needed. This excludes the initial-C branch of one of the two N4 hook-loss gates per foreign. Initial D/V/U routes and the other N4/W5 gates remain open here.

The clock starts at the FOREIGN EXIT. All C atoms are actually executed; no foreign half-turn is counted as literal Cs and no C tail is executed in advance.

## One genuine foreign R39 identity

Q and B both have a genuine last-R output at source-local(-4,1), own RAW R39/read40. It becomes external CURRENT g=(0,-5) after Q or g=(1,-6) after B. In each target frame, g has local coordinate(1,0), in target U entry K.

A valid target therefore requires that g have left external CURRENT earlier. The proof excludes that first CURRENT loss, rather than claiming the physical identity would need to be dead. If an earlier capture had left the same identity physically alive in CORE, it would still be a CURRENT loss and would be covered.

## Arbitrary rails, exact first-loss bounds

Write the continuation before target as

    C W C S C E C N U,

where W,S,E,N are arbitrary possibly empty ordinary-base rails in their named heading. There are no additional C atoms in a rail. C has no external BLACK input and preserves any older CURRENT residual. Any first CURRENT loss of g must therefore be a true D/V/U input, including marker-owned external-to-CORE capture.

The eight actual input roles give universal bounds:

* W input head y<=gy+1.
* S input head x>=gx-1.
* E consuming RAW exit H=x+y>=gx+gy-1.
* N consuming RAW exit x>=gx.

These bounds include every U upper/lower coordinate and every unread-CORE marker input; they are not restricted to physical L reads owned by the RAW itself.

W: the initial C ends at(0,1,W). All W heads have y>=1, but a g input would have y<=gy+1<1. Thus g cannot first leave CURRENT in W.

S: all W head x are nonpositive, and the next C moves x left by one. Hence all S heads have x<=-1. B needs input head x>=0, impossible. For Q, the only possible x-boundary inputs are the three U coordinates with local x=-1. Their heads are(-1,-4,S),(-1,-3,S),(-1,-1,S). The signed Q hook minimum-four-C theorem keeps all four hook IDs CURRENT at this S clock two. Each of these three literal contexts has a hook CURRENT/core or BLACK/first-WHITE conflict. Thus no S loss occurs, including the empty-W case.

E: the target H is -6 in both cases, while g H is -5. N cannot be empty because the actual raw C,U pair has an immutable L/L conflict at global tick29 versus1, inside U RAW. Every nonempty N rail has H increment at least two. Since the fourth C adds one to H, the last E head before it must have H<=-9. But any E loss of g has actual RAW exit H>=-6, and later E head H never decreases. It cannot reach that final E head. Thus g cannot leave CURRENT in E.

N: every N loss of g has actual RAW exit x>=gx, while target x=gx-1. Later N head x never decreases, so no such prior loss can reach the target. All four C atoms preserve CURRENT g.

Consequently the SAME R39 identity remains external CURRENT at target entry, but is in target entry CORE. This partition contradiction excludes the target. No generic producer maturation, proxy Jordan assumption or external-field reset is used.

## Controls and exact limits

The motivating named control family fixed no initial N run, one D/V W-base, arbitrary endpoint-exhaustive S/E rails, then one D/V N-base before the target U. It yielded300 count records and3,264 failed complete whole words, with and without an immediate creating-U prefix. They remain regression controls only: the theorem above allows arbitrary W/S/E/N lengths and orders and does not extrapolate from the finite tests.

Only the stated initial-C branches and exact two targets are excluded. The separate hook-missing contact class, initial D/V/U paths, other hook-loss gates, a second foreign, arbitrary-tail simplicity, coverage and capture are not resolved.
