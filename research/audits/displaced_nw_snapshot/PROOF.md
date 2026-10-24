# The two displaced northwest retained-core channels

Status: new complete-field bivariate certificates; independent review pending.

## Exact three-cell families

The normalized initial pose is(0,0),N. Write q_n=(-33-2n,-14-2n).
For r=70 or75 define

    r=70: s=(-22-2m,30+2m), a=(-33-2n,57+2n);
    r=75: s=(-21-2m,30+2m), a=(-33-2n,45+2n).

For every m>=100 and n>=m+100, starting with exactly the three black
cells {q_n,s,a} gives a permanent standard southwest tail. Explicit
certified checkpoints are:

    r=70: time520n+153920, pose(-2n-76,-2n-20),N, W phase29;
    r=75: time416n+104m+148096, pose(-2m-72,2m-28),S, W phase55.

These are not asserted to be the earliest possible capture checkpoints.
More importantly for composition, the ENTIRE trajectory, including its
infinite final tail, satisfies

    r=70: u=x-y <=58, z=x+y <=87;
    r=75: u=x-y <=58, z=x+y <=75.

The bounds are uniform in both m,n, not only eventual or sample bounds.
No previously written field cell is removed or replaced by a clean core.

## Executable certificate

certify.py loads the candidate template for the selected phase and checks
its complete field from the stated three black inputs. Use

    python certify.py 70
    python certify.py 75

The independently audited bivariate XOR engine uses u0=m-100>=0 and
v0=n-m-100>=0 as independent parameters. Every fixed read color and every
read of every finite periodic segment is checked exactly. A separate
infinite-tail certificate then checks all final future reads, including
the full old field and all affine history rays. Each104-letter periodic
word is required to be a cyclic phase of the canonical standard word.

The first input reads are also exhaustively checked:

    q:104n+10881,
    s:208n+104m+70738+r,
    a:312n+79234 for r70, or312n+74446 for r75.

The time and final pose are computed from the certified segments and
asserted against the displayed formulas. The two runs perform56,942,728
and50,790,499 exact isolated point-incidence exclusions, respectively.
The literal simulation and multivariate candidate extraction are retained
separately as discover.py/extract.py. They do not prove the theorem.

For the global geometric bounds, the checker takes every fixed read
point and both endpoints of every periodic read ray. A linear functional
attains its maximum at an endpoint of the epoch interval. Its parameter
coefficients give the uniform bound over the whole nonnegative quadrant.
The final southwest drift has delta-u=0 and delta-z=-4, so its first
period bounds its entire future. This establishes the two displayed
all-future inequalities directly from the certified read set.

## Exclusion of two more recurrent retained-core rays

Fix m>=100 and either phase. The ordinary-interface theorem in the parent
directory already proves the complete {q_n,s} parent. Its NW tail is not
on the original rail. Its exceptional phase72 rays, at m=0, are

    r70: (-35,59)+j(-2,2),
    r75: (-37,49)+j(-2,2).

At general m the whole ray is translated by m(-2,2). Since a shares
q_n's column x=-33-2n, an exceptional a-hit forces m+j=n-1 or n-2,
respectively. Thus its row is precisely y=2n+57 or y=2n+45. The
three-cell families above are therefore the exact forced branches, not
chosen examples of possible placements.

At hypothetical recurrent mass-five checkpoints with this fixed core,
the audited incidence lemmas give the first collider q_n and either a
four-edge strand or a four-cycle. The index n tends to infinity, so the
new parameter cone eventually applies. The core is encountered before
any other remote cell, by the ordinary-interface prefix bounds.

- In the first four-edge orientation, the northwest remote a has one
  bounded coordinate and z tending to minus infinity, so it cannot meet
  the constant-z NW tail. The other two remote cells have u tending to
  plus infinity and also cannot interrupt the parent. Its standard tail
  is permanent.
- In the transposed orientation, only a can meet the NW parent. The other
  remote cells have, respectively, u or z tending to plus infinity.
- In a four-cycle, c has u tending to plus infinity and d has z tending
  to plus infinity, so again only a can interrupt first.

For the latter two shapes, an ordinary a-hit is impossible on a
noncapturing orbit: the favorable-sector lemma gives the complete
ordinary future u<=u(a)+58. It lies below the fixed-m canonical archive
lower bound and below the other remote sites by their diverging axial
gaps. The source's all-age guard protects the old outgoing wake as well.
If a is not hit at all, the parent already captures. Hence the only
remaining possibility is the exceptional a specified above.

After that hit, the new complete three-cell parent has the uniform
all-future bounds u<=58 and z<=87 (or75). Thus it never reads the two
remaining remote cells once the checkpoint index is sufficiently large.
First-difference coupling gives permanent capture for the actual
five-cell checkpoint, contradicting recurrent mass five.

Consequently both whole retained-core rays are excluded for fixed
m>=100, conditional only on the already audited global incidence and
ordinary-interface lemmas and the pending audit of this new certificate.
Together with the other results, this would handle19of the22 asymptotic
fresh NW core classes. The three NE-output classes29,56,62 are not
covered; their exceptional opposite-corner hit introduces an independent
geometric depth.
