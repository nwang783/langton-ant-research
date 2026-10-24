# Exact short two-leg orthogonal candidate check

24 October 2026. Author complete bounded-family result; independent review
not requested yet. No new controller or general interface exclusion.

Let F_a be cyclic phase a of the supplied standard104 turn word, a=0..103.
Test exactly the two families

    F_a R F_b L,       F_a L F_b R,       a,b=0..103.

This is21,632 supplied words, each length210 and formal R-minus-L count24.
They restore the heading. Their full drift coordinates are both odd and
nonzero, so any complete WHITE survivor would not be a standard repetition.
The motivation is the retained one-shot90-degree standard corner, not an
assumption that its ten prepared markers regenerate. The two104-step legs
are short and interact; this is not the mature fixed-orientation profile
conversion problem.

For each word, the checker reconstructs all210 physical reads, retains its
actual full drift d, partitions by Z*d and orders each complete stable
history by t-k*210. ALL21,632 candidates have two CONSECUTIVE stable reads
at one class with the SAME turn. The complete certificate stores the class,
phase indices, longitudinal offsets and stable times of such a pair for
EVERY candidate. This contradicts flip-on-read alternation independently
of the first color. Thus no candidate is even an eventual translating word
on an arbitrarily precolored fixed board; changing finite input fuel does
not repair this specific nonalternation. The certificate's statement is
about this exact supplied-word family only.

All104 standard phases, both singly and doubled with their corresponding
FULL drift, pass the same WHITE complete-history checker as208 positive
controls. No drift is divided to a primitive vector.

Files: check_two_phase_orthogonal_concatenation.py and matching JSON;
two_phase_orthogonal_rejection_certificate.json contains all21,632 explicit
witnesses. The run took about3s; no solver result or timeout is involved.

This does not cover longer single-turn legs F_a^m/F_b^n, longer routing
words, three or more legs, arbitrary phase-switching fields, or any general
autonomous controller. The retained finite ten-cell corner, its complete
prepared output, and its failure of unchanged reuse remain separate facts.
No external literature novelty claim is made.
