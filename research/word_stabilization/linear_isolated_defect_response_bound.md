# Linear response from an isolated bad-ten event

Status: derived from the independently audited seven-word linear fuel theorem and the already audited finite-prefix response architecture. It is a response bound, NOT a capture-time bound.

Let J(t-1)=0 and J(t)=1, with complete-board black mass at most m at time t. The prior theorem isolated_defect_response_bound.md proves a later K=J(s-1)J(s) and bounds its delay by composing two monotone H/T envelopes after a270902-history acyclic allowance. All its word-ending and reversible-history conventions remain in force.

The new audited actual-H bound is89M+15 raw turns when full successor+marker context is present. A finite H visit needs100 leading turns and200 trailing turns; the extra trailing successor is essential. Hence replace only the actual-H envelope by

    Hlin(x)=300+89(x+100)+15=89x+9215.

Retain T(x)=12x+400 and N=270902. Then

    Flin(x)=x+Hlin(x)+T(x)=102x+9615,
    Dlin(m)=Flin(Flin(m+N+1000))+2
           =10404m+2829858755.

There is therefore a K event at some t<s<=t+Dlin(m). The old exponential bound remains valid for arbitrary-five factors in its own broader domain; it is not silently replaced there. The linear substitution is justified specifically by the independently checked inclusion of the old actual H149 graph in the new seven-word actual-port graph.

A long standard flight may have arbitrarily many turns with no J, so this does not bound general capture time. Nor does it prove that the total number of K events is finite.
