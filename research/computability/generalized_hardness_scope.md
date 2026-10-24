# Generalized hardness results and the missing planar reversal port

22 October 2026. Status: primary-source scope check. These papers do not establish finite-support universality, undecidability, or a counterexample for the classical planar ant.

## 1. What the later complexity papers actually change

Tsukiji and Hagiwara, *Recognizing the Repeatable Configurations of Time-Reversible Generalized Langton's Ant is PSPACE-Hard* (2011), adds permanent gray cells at which the particle moves straight without flipping. Its square-grid repeatability theorem uses these extra cells. It is not a theorem for the two-color classical rule.

Primary PDF: https://mdpi-res.com/d_attachment/algorithms/algorithms-04-00001/article_deploy/algorithms-04-00001.pdf , abstract and Sections 1.1–1.4.

Hagiwara and Tsukiji, *Hardness of Approximation for Langton's Ant on a Twisted Torus* (2020), removes gray cells by changing topology. Page 4 explicitly identifies H/V polarity as the obstruction to a same-port reversal on the plane. An odd torus twist changes this polarity after a wrap and supplies the missing reversal. The reusable circuit therefore does not transfer unchanged to the planar finite-white problem.

Primary PDF: https://mdpi-res.com/d_attachment/algorithms/algorithms-13-00344/article_deploy/algorithms-13-00344-v2.pdf , especially page 4 and Section 2.

## 2. Exact rule-level reason in our conventions

This section is a direct calculation, also developed independently in causal_reduction/pose_sector_and_reverse_sweeps.md. It explains why copying a reversible gate diagram does not supply a legal autonomous reset.

Write a complete state as X=(B,p,h), with d_h the unit vector in heading h. Define

    J(B,p,h)=(B,p-d_h,h+2).

Then J is an involution and

    F J = J F^(-1),

where F is one classical ant update. Indeed, let q=p-d_h be the predecessor cell of X. Its current bit is opposite the bit read on the preceding forward step. Reading that bit from the reversed heading h+2 therefore gives the reversed predecessor heading, and the next movement goes to the predecessor of q. The field flip is exactly the preceding forward flip undone.

Thus a finite legal trace from X to Y can always be traversed backwards as a legal trace from JY to JX. But this is NOT an instruction that a forward ant can move from Y to JY. The invariant

    sigma(B,(x,y),h)=(x+y+h) mod 2

is preserved by every legal update, because both spatial parity and heading parity flip. J changes sigma, since it shifts the pose by one cell and rotates heading by two quarter-turns. Consequently no finite forward trace, on ANY arrangement of black and white cells, can connect Y to JY. Changing the finite board cannot cure this pose mismatch.

For a right-half-plane excursion from (0,r,E) to (-1,s,W), reversal starts at (0,s,E) and ends at (-1,r,W), using the final field as its input. It swaps the entry and exit rows and belongs to the opposite pose sector. Running finitely many such inverse excursions merely consumes the corresponding finite prepared history. It does not give an infinite renewable controller from a finite seed.

The half-turn-copy autonomization in halfstrip_builder_reductions.md is different: it uses a second forward-growing field and matches actual forward ports. It never asks the ant to reverse itself at one unchanged edge.
