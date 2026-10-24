# Uniform all-multiplicity unit-return density refinement

23 October 2026, 08:44 UTC. Analytic extension, review pending.


Call a cyclic class gap cheap if it is a zero-displacement four-step
return, and let r be the number of other gaps. Winding makes r>=1. The
factor theorem limits every cheap run to three gaps, including across a
cyclic cut, so n<=4r and r>=ceil(n/4).

If D>=4, every noncheap gap costs at least8 (a longer zero return has
length divisible by4, while a nonzero gap costs at least2D>=8). At least
one winding gap costs at least2D. Therefore

    P >= 4(n-r)+8(r-1)+2D
      >= 4n+4*ceil(n/4)+2D-8.                    (2)

This holds for every n>=1 and strengthens the basic packing for n>=5.
For D3, each noncheap gap costs at least6, giving

    P >= 4n+2*ceil(n/4),                         (3)

rounded up to the compulsory residue P=2mod4. These are visit-density
constraints on actual ant trajectories with any input coloring, not just
white fronts. They do not assume all physical ranks lie within one period.
