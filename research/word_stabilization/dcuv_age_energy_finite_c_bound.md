# Discounted C-age energy for recurrent-eight finite factors

Status: independently signed as audit KA, including separate exact literal arithmetic at audits/check_dcuv_age_energy_independent.py/json. This improves the finite-C exponential rate, not DCUV confinement or universal capture.

Consider a finite context-complete recurrent-eight factor, with entry black mass m>=5, the signed disjoint five-cell core, total C-macro count k and raw duration L. Every residual identity carries its saturated C-age a in{0,1,2,3,4}. Give initial identities age4, since they are exempt from the input-age restriction. A packet with c C macros ages every survivor by c (saturating at4), and each fresh output has age c. This is exactly the signed JO source-included, consumer-excluded convention.

Let lambda be the unique real root greater than1 of lambda^2+lambda^3=6 (approximately1.5376561717), and define

E = sum over current residual identities of lambda^a,
B = 6*lambda^2/(lambda^2-1).

For every recurrent-eight packet, write b for its output count minus3c. The D/DC cases have b=1, V/VC/VCC have b=6, and U/UC/UCC have b=9. JO's signed input ages give

sum input weights >= b.

The only tight case is V/VC, whose two required ages2 and3 give lambda^2+lambda^3=6. For D/DC the required age3 suffices. VCC has two age4 inputs, and U variants have two age3 and three age4 inputs; their inequalities are strict already at lambda=3/2. Every initial input was assigned age4 and also satisfies these weight inequalities.

Consequently a packet with c in{0,1,2} satisfies E'<=lambda^c(E+3c). Since B>=3c/(1-lambda^(-c)) for c1,2, this is equivalent to

E'+B <= lambda^c(E+B).

Iteration gives the mass/energy bound

E_final+B <= lambda^k(lambda^4(m-5)+B),
m_final-5+B <= lambda^k(lambda^4(m-5)+B).

No assumption that erased identities persist is made: only the current ordered residual ledger is used.

## Raw duration

Partition the factor into epochs, each ending with the next positive-C packet, followed by a possible final zero-C epoch. Before its final packet, an epoch contains no C macros. An input produced inside that epoch would therefore have age0 when consumed, contradicting JO's universal produced-input minimum2. Thus every consumed input identity in an epoch was present at epoch entry, and distinct consumed identities cannot be reused, including U's recycled cell.

If r is its entry residual mass and c its total C count, literal packet lengths give

epoch raw duration <=10r+15c <=10E_entry+15c.

Indeed D/DC have one input and lengths10/25; V/VC/VCC have two inputs and lengths18/33/48; U/UC/UCC have five inputs and lengths28/43/58. Each row satisfies length<=10*input_count+15*C_count.

The cumulative C counts at epoch entries are a subset of{0,...,k}. The energy upper bound is nonnegative at each such integer. Summing over the entire set yields

L <= 10(lambda^4(m-5)+B)(lambda^(k+1)-1)/(lambda-1)
     -10B(k+1)+15k.

In particular the duration is O((m+1)*lambda^k), with exponential rate approximately1.538^k rather than JV's5^(k/3), approximately1.710^k. This implies only a logarithmic necessary C recurrence rate in an infinite finite-support recurrent-eight tail. It does not upper-bound k, exclude U, or prove capture.

For an entirely rational specialization one may take lambda=8/5 and B=128/13 instead. All input-weight and packet inequalities remain valid; lambda^4=4096/625. The arithmetic replay uses that rational specialization, while the root-valued theorem follows from the displayed symbolic inequalities. No arbitrary-factor trimming extension is claimed here.

## Scope boundary: optimal local age-only multiplier

The following limited certificate-optimality observation has also passed independent analytic review. Consider nonnegative current-age point weights w_a with w_0=1 and the per-C aging bounds w_(a+1)<=rho*w_a. If the local certificate uses only JO's separate age minima, it must admit the RELAXED V input ages(2,3). The zero-C V transaction therefore requires6<=w_2+w_3<=rho^2+rho^3. A fixed additive energy constant cannot repair a zero-C transaction. Thus rho must be at least the stated root lambda.

This is optimality only within that JO-only local point-weight ansatz. It does not assert that ages(2,3) occur jointly on a physical V, that the abstract exponential growth rate is physically attainable, or that producer roles, geometry, correlations, other potentials, or nonlocal proofs cannot give a stronger theorem.
