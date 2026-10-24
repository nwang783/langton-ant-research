# Every legal finite trace has a certified highway completion

Research date: 22 October 2026. Status: exact consequence of the recovered four-cell exterior-completion theorem, not a newly discovered physical gadget. This records an obstruction to finite-observation and truncation arguments; it does not prohibit all computability reductions.

## 1. Effective trace-language equality with four extra black cells

Fix a launch pose. For a finite turn word u, draw its prescribed path. At each visited cell, its consecutive requested turns must alternate. This condition is necessary and sufficient for finite-word realizability. When it holds, define B_u to contain exactly those visited cells whose first requested turn is L. Let mu(u)=|B_u|.

The complete finite seed B_u executes u, by induction on visits. Every seed executing u must contain B_u and must leave all first-R cells white. Thus mu(u) is the exact minimum initial black mass needed to execute the finite word.

Apply the existing four-cell exterior-completion theorem to this complete seed, protecting its entire u prefix. It effectively supplies four new black cells E outside a protected square. The seed B_u union E executes u and then has a certified standard104 tail.

Consequently, if m_H(u) is the minimum black mass of a standard-capturing finite seed executing u, then

   mu(u) <= m_H(u) <= mu(u)+4.

In particular the set of legal finite prefixes of standard-capturing finite-seed trajectories is EXACTLY the set of legal finite prefixes of arbitrary-background trajectories, including infinite and noncomputable backgrounds. The construction only reads the finite word, not the rest of the background.

The upper bound is inherited from the four-cell theorem. No claim is made that four is optimal for arbitrary finite-trace completion, or that m_H(u)>mu(u) for any u. Under HC they would always be equal.

## 2. Positive seeds converge to any proposed counterexample

For any complete finite seed B and any T, the completion theorem constructs a capturing seed B union E_T whose trajectory agrees through T and whose four additions lie outside the radius-T ball. Therefore B union E_T converges to B in the pointwise/product topology as T grows. This remains true if B is a hypothetical noncapturing seed.

Thus the noncapturing subset, if nonempty, has empty interior in the finite-support configuration space with its product topology. No finite observed prefix and finite list of inspected cells can certify noncapture uniformly over arbitrary undisclosed remote finite perturbations.

This is not a claim that a fully supplied finite input is inaccessible: its sparse encoding includes the promise that ALL other cells are white, a global fact not supplied by a finite spatial cylinder. A finite noncapture proof could use that complete-input promise and a valid all-time invariant. Density alone says nothing about computable many-one reductions from discrete machine descriptions.

## 3. Why infinite-background universality cannot be transferred by truncation

The Gajardo-Moreira-Goles construction prepares infinitely many circuit copies in a trapezoidal array. Truncating its background far enough reproduces any prescribed finite computation prefix. Section 1 shows something stronger: that same finite computation prefix can always be reproduced by a finite seed GUARANTEED to settle into the standard highway later.

Hence agreement for every finite duration after choosing a different larger seed for each duration does not construct one finite seed that computes forever. The quantifiers are

   for every T there exists a finite capturing seed agreeing through T,

not

   there exists one finite seed agreeing for every T.

A usable finite-support universality theorem needs a single effective seed per machine/input, hardware generation or equivalent unbounded writable memory inside its genuine future, and an all-time noninterference/simulation proof. Finite circuit P-hardness and arbitrarily long positive simulations do not provide this.

## 4. Source boundaries

- sources/kehao95-core/four_cell_port/PROOF.md, Theorem 3 and its geometric first-exit proof, supplies the exact four-cell construction and preserves arbitrary protected finite history.
- sources/gajardo-2002.txt, Sections 3 and 4, distinguishes finite circuit P-hardness from infinite-support universality and explicitly leaves finite-support decidability open.
- The per-cell alternation criterion is elementary and also appears in Gajardo's symbolic-projection paper. No claim depends on its separately disputed hyperbolic visit bound.
