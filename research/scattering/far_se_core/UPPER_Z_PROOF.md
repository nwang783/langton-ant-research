# An upper half-plane exclusion for the retained mass-five core

The exact geometry and recurrence coupling passed independent audit.
The independent univariate computation is audits/upper_z_independent.json.

The exact certified pristine parents have complete read bounds
  blank: z<=35; q_n: z<=39; q_n+a_n: z<=71;
  q_n+a_n+c_n: z<=75,
for every n>=200, including each parent's infinite standard tail.
`certify_upper_z.py` checks every finite read and every affine repeated ray
of the original rectangle. On a positive-z finite ray it checks its last
point; on a nonpositive-z ray it checks its first point. All affine n
coefficients at the selected endpoints are nonpositive. The infinite rays
have nonpositive z drift. It reports maxima 35,39,71,75 exactly. This is a
geometry corollary of the already-audited words, not a new color-validity
claim.

Suppose a recurrent mass-five fixed-pose sequence has retained local core
{s}, with z(s)>=76, and four escaping remote cells. The existing incidence
and exposed-corner lemmas apply unchanged. The blank orbit misses s. An
ordinary first remote SW impact stays in z<=z(q)+58 and misses fixed s and
the other exposed remote corners for all sufficiently large indices.
Hence q must be exceptional. The exact q parent misses s by z<=39. At its
first NW impact, an ordinary response stays in u<=u(a)+58, which tends to
minus infinity and misses fixed s and the protected archive/other corners.
Hence a must be exceptional. The q+a parent misses s by z<=71. At its first
SE impact, an ordinary response stays in u>=u(c)-58, which tends to plus
infinity and likewise misses fixed s and the protected cells. Hence c must
be exceptional.

The existing four-edge strand alternatives cannot realize all these forced
exceptional alignments. In the four-cycle, the exceptional chain fixes the
original q_n,a_n,c_n,d_n rectangle. Its whole remaining trajectory has z<=75
and its d_n is never read. It therefore misses s forever and captures on the
standard NW highway, contradicting recurrent mass five.

Thus, under the established incidence hypotheses, every retained mass-five core must satisfy z<=75. This does not
assert eventual mass>=6, or capture from arbitrary finite seeds. It does not
handle the negative-z arm containing sites visited by the blank highway.
