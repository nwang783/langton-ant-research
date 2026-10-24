# Finite marked-rank parameters above the rank-two second-row branch

23 October 2026, 04:45 UTC. Independently signed analytic continuation.
The auditor independently reconstructed the transducer across 308 controls.

The signed rank-two second-row result has length five. Its third-row
marks, with arbitrary complete common length L, are

    p=(a+2,b-1,b,b+2),  q=(a,b,b+1,b+2),
    a,b even, b>=a+4, L>=b+3.

We claim that necessarily

    (a,b) is (0,4), (0,6), or (2,6).

This does NOT bound L or the fourth row.

## Exact top-port prefix

Before input index a all top ports are the ordinary ordered three-step
bounces, with voltage j mod2. Indices a,a+1 are swapped, with words SWN
and SESWNEN, voltages zero and one, and lengths three and seven.
After index a+1 and before index b-2, ports are ordered three-step bounces
with voltage 1-(j mod2). At index b-2 there is an ordered nineteen-step
path of voltage two, with literal compass word

    S E S E N W S W N E S E S W N E N E N.

These formulas follow by exact horizontal ordinal matching through the
already fixed three rows. They are independent of all later unmarked
visits. They are reproduced as an exploratory control by
`probe_axis_layer_transducer.py`. The remaining suffix is not needed here.

Four initial ordinary ports exclude a>=4. Thus a=0 or2.

## Two terminal-excursion substitutions

The signed singleton-bounce contradiction uses its first three literal
ordinary paths to force an E edge from its third C mark to its fourth
D mark. If only its fourth lower excursion is changed, the contradiction
still follows whenever that excursion has ordered output, length ell,
voltage v, and ell+1-v*period<0. All preceding ordinal and first-return
steps are unchanged.

Similarly the signed reverse-bounce contradiction uses its first two
literal reverse-phase paths to force an E edge from its second C mark
to its third D mark. It survives the same substitution in its third
excursion under the same inequality. Its parity-padding extension also
survives: every first return used still lies between actual events.

We use ell=19,v=2. For b>=8 the already built strip has at least
2+10+2*(b+3)>=34 events, so the inequality is strict.

## Excluding b>=8 when a=0

Its first four ports have exactly the rank-zero second-row pattern:
inputs0,1 swapped, lengths3,7, voltages0,1; inputs2,3 ordered, lengths3,3,
voltages1,0. The prefix portion of the signed rank-zero proof therefore
forces, at the next row, the three-mark balanced core

    P=(h,h+1,h+2), Q=(h,h+2,h+3), h even,

and forces every later P,Q mark at or beyond h+4. That prefix argument
uses only the four ports just listed, not the eventual form of later
ports. Cut the upper matched histories before h+4. The remaining lower
ports begin at old index3. Their first three are ordinary ordered bounces
with voltages0,1,0. If b=8, their fourth is the nineteen-step voltage-two
path; if b>=10, their fourth is ordinary voltage one. In either case the
singleton contradiction, with the permitted terminal substitution when
needed, rules out b>=8.

## Excluding b>=8 when a=2

Its first five ports have exactly the prefix used in the signed rank-two
second-row proof: two standard bounces, the swapped pair at indices2,3,
and the ordinary voltage-one bounce at index4. The prefix part of that
proof therefore forces its four-mark balanced core

    P=(h+2,k-1,k,k+2), Q=(h,k,k+1,k+2),
    h,k even, k>=h+4.

This prefix argument uses no lower port beyond index4: its only use of
that fifth port is to rule out the alternative sixteen-step-return case.
The matched cut before k+3 is odd. After the signed parity padding, its
remaining ports start at old index4 with reverse-phase voltages1,0,1,... .
If b=8, their third is instead the nineteen-step voltage-two path; if
b>=10, their first three are ordinary reverse-phase bounces. The reverse
obstruction, with terminal substitution where needed, excludes both.

Thus b<=6. Combining b>=a+4 with even a=0 or2 gives exactly the three
claimed pairs. No finite-cap solver result is used as a premise.
