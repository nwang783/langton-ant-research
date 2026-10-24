# Independent audit of full two-cell axis-drift exclusion

23 October2026,04:49UTC. The author note `periodic_classification_new/axis_negative_drift_extreme_exclusion.md` is accepted under its complete-white-front hypotheses.

Fix actual full drift(-2,0), not merely a primitive displacement. Translate the lowest active row to y=0 and choose the checker sector so A=(0,0) has vertical exits and B=(1,0) horizontal exits. Their histories have common length m>0. No lower neighbor is active, forcing B's incoming directions S and A's incoming directions W,E alternately. At C=(0,1),D=(1,1), equal horizontal counts give equal complete history length n. The N-arrival ranks p_j at C and S-departure ranks q_j at D are increasing, with m entries each.

Direct seam calculation, independently of positive-drift notes, gives an E edge d=c+1 and W edge d=c+1-P. Lower excursion j has c_p=d_q+3+(j mod2)P. A W source preceding an E source therefore has its W target before that E target. If a D prefix had more E occurrences than the equal-length C prefix, an E target in the prefix would have its source after the C prefix, while a W source in the C prefix would have its target after the D prefix. This contradicts that ordering. Thus the signed q-prefix count minus signed p-prefix count is nonpositive.

The period is a multiple of four: exactly P/2 movements are horizontal and their net displacement is even. P=4 would leave exactly the four necessary bottom/two-next-row classes, each read once, giving RRRR and zero drift. Thus all four-step returns are proper. After a second lower mark is forced, m>=2 and n>=3 imply P>=12, making the eight-step return proper too.

If q0 is even, the E,S,W,N return forces p0=q0+2, violating the reversed ballot before any C mark. Hence q0 is odd. Its W source k has c_p0=c_k+4-P, so p0<k. If p0 were odd, reversed ballot and W ordinals would give k<=p0. Thus p0 is even. The S,W,N,E return forces q1=q0+1 and E ordinals give p0=q0-1.

The actual compass word W,S,W,N,E,S,E,N first returns to C after eight steps, with intermediate C translated by(-2,0). Hence p1=k+1. Since k lies between the first two C marks, it is unmarked and even. W ordinals give k=q0+3, p1=q0+4. The S,E,N,W return gives q2=q0+2. At p1 and q2 the W ordinals both equal(q0+3)/2. Consequently the next lower excursion yields c_p2=c_p1+4-P<c_p1, contrary to p2>p1. If fewer than three lower marks exist, one of the already forced marks gives the contradiction earlier.

This excludes all multiplicities, widths and periods for actual full drift(-2,0). A genuine half-turn or quarter-turn preserves handed turns, covering(+2,0),(0,2),(0,-2). No reflection is used. The theorem does not cover larger axis displacement, arbitrary drift, nonperiodic paths or universal finite-seed capture.

Novelty check: the retained `periodic_growth_closure/PROOF.md` has all-growth arithmetic for the two-cell axis and excludes growth4/12, but explicitly does not exclude growth8 or larger permitted values. Thus the all-growth exclusion is stronger than that retained statement. Earlier layer calculations remain correct independent controls, now unnecessary for this displacement.
