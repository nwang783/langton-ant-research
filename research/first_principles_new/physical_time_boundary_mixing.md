# Physical-time bounds from the permanent spine

22 October 2026. Independently analytically audited quantitative corollary of the packet grammar and stage mass bound.

Fix a finite time immediately before a permanent spine entry, after any completed B at that root, and let the finite black mass there be m. Let T_N be the elapsed ordinary ant updates through the first N complete spine stages, with T_0=0.

## 1. Finger depth is at most its entry mass

The exact G_R(n) pattern has n black cells if n is even, and n+2 if n is odd. Its reflected color-complement G_L(n) has n+4 if n is even, and n+2 if n is odd. These counts include the two root-column and two far-column bits. Therefore every legal G_a(n) requires at least n black cells at its entry, so n is at most the current total black mass.

Each stage has at most three G fingers and at most six other turns: at most two permanent core turns, plus the four parent turns in an optional B. The stage-entry mass m_i is at most m+6i, by the previously audited stage mass bound. Before any of its fingers, at most two earlier Gs can have increased mass by at most8 and at most six other turns can have increased it by at most6. Thus every finger in stage i has depth at most m_i+14.

A finger of depth n lasts4(n+1) updates. Consequently stage i lasts at most

    6 + 3*4(m_i+15) = 12m_i+186.

Summing and using m_i<=m+6i gives

    T_N <= 36N^2 + (12m+150)N.                           (1)

The constants are intentionally loose. Individual finger depths are not uniformly bounded; they are controlled by the stage index and finite starting mass.

## 2. Transfer of the audited mixing estimates

Let N(t) be the number of completed permanent stages by elapsed physical time t. Since t<T_(N(t)+1), equation (1) implies

    N(t) = Omega(sqrt(t)).

This is a trajectory-dependent asymptotic statement after the chosen finite initial cut. It is not a claim that the cut or the permanent spine is effectively detectable online.

The audited boundary-syllable mixing theorem gives exponent-two count M_2(N)=Omega(sqrt(N)) and exponent-one count M_1(N)=Omega(log N). Applying these to the N(t) completed stages yields

    M_2(t) = Omega(t^(1/4)),
    M_1(t) = Omega(log t).                               (2)

Here M_j(t) counts completed permanent stages with exponent j, not physical visits, turns, or arbitrary finite-prefix reduced syllables. These are lower counting bounds only. Neither exponent is proved to have positive physical-time density, and no bounded-depth or attraction conclusion is inferred.
