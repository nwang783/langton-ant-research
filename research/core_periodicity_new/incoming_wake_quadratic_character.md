# The quadratic wake character with nonwhite input

Status: analytically approved by the independent auditor on 2026-10-22 at 22:06 UTC. The separate checker also exhausts all qualifying raw words through length16. This is a necessary periodic-profile identity, not a proved global convergence statement.

The white-input theorem and notation are in

    ../sources/kehao95-core/wake_synthesis/verification/general_wake_parity/PROOF.md.

Consider a translating periodic turn word with non-axis full drift d=(a,b), a>0, a+b even. Instead of white input, suppose each physical drift class has a fixed incoming color beta_v in {0,1}; the incoming black class mask has finite quotient support. A finite moving cap is allowed, provided sufficiently far-ahead stable reads see this specified input. Let m_v be the class visit multiplicity, O_v=m_v mod2, and

    D_v=(-1)^beta_v O_v.

Thus D is the signed black-field change and the raw R-minus-L growth is g=sum D_v, possibly negative. Heading reset still gives 4|g. The odd-used edge graph is the same G_d(O), since its horizontal and vertical boundaries depend only on multiplicity parity, not initial color.

At a vertex let p_v be the parity of the number of positive incident ports across its incoming and outgoing edge occurrences. This is determined by G_d(O). Let q_d(O), E, and N_+ have the exact meanings in the cited proof.

The candidate necessary condition is

    Omega_d(O)=1,
    q_d(O)=1+a+sum_v beta_v p_v  (mod2).                 (A)

The new sum may involve vertices outside O: an even-used class can have p_v=1. It remains finite because the odd-edge graph is finite. Do not replace this sum by its restriction to O.

## Port-sign derivation

Use the Q-vertical, C-horizontal convention. At each visit, L means unequal incoming/outgoing positive-port bits at Q and equal bits at C. Write I for the total port-list inversion parity and K for the sum of the stable ranks of all L visits, modulo two.

The purely algebraic port-list calculation in the cited proof does not assume white input. It yields

    K = I + sum_Q p_v(m_v-1)
            + sum_C [p_v(m_v-1)+binom(m_v,2)].

The local signed turn balance gives

    m_v=2p_v+D_v (mod4) at Q,
    m_v=2p_v-D_v (mod4) at C.

Consequently the local correction equals

    Q: p_v(O_v+1),
    C: O_v(p_v+1)+beta_v O_v.

The white-input endpoint cancellation identity applies to the unchanged odd-edge graph. Therefore

    K = I+N_+(O)+|O intersect C|+sum_C beta_v O_v.

Chronological first-to-first edge pairing still factors one full-period successor cycle, so I+E=1. Hence

    K = 1+q_d(O)+sum_C beta_v O_v.                     (B)

## Stable-color derivation of K

Stable visits alternate. If beta_v=0, L occurs at odd ranks, so its local contribution to K is floor(m_v/2) modulo2. If beta_v=1, L occurs at even ranks, so its local contribution is zero. Thus

    K = total_number_of_L_reads
        +sum_v beta_v floor(m_v/2)+sum_v beta_v O_v.

Using the preceding congruences,

    floor(m_v/2)=p_v+beta_v O_v       at Q (mod2),
    floor(m_v/2)=p_v+(1-beta_v)O_v   at C (mod2).

It follows that

    K = total_number_of_L_reads
        +sum_v beta_v p_v+sum_C beta_v O_v.            (C)

Since the period contains P/2 horizontal moves, P/2=a modulo2. Since g is divisible by4, total_L=(P-g)/2=a modulo2. Equating(B) and(C) proves(A).

## Scope and possible use

The winding parity condition is unchanged. The signed mod4 residue conditions must be rederived or applied to the signed D, not to the unsigned O alone. Formula(A) is only a necessary condition and does not assert realizability.

For a candidate same-sector consumer of one standard bilateral wake, beta is its fixed incoming wake profile. The extra term can be evaluated from beta and the proposed odd-used mask without any period bound. No general consumer exclusion or nonstandard periodic front follows yet.

Changing the checker convention reverses edge orientations and complements both port lists. The parity p_v is unchanged because the two lists together have 2m_v entries. Thus the proposed correction is convention independent, as is the original q_d.
