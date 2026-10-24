# A geometric alien overlap that cannot survive internal chronology

23 October 2026, 01:35 UTC. Submitted for independent audit.
Let k=17 and A=[[3,2],[2,9]], with determinant23. In the half-turn-covariant,
source-axis-preserving direction-substitution class, every image has only
source/target A-lattice overlap. Thus the whole family is excluded for finite
support by signed theorem GN. This does not exclude arbitrary occurrence-
dependent macro choices or nonsymmetric images with collapsing first maps.

An east image has E6,W3,N5,S3, with nine horizontal and eight vertical slots.
Its coordinate box is [-3,6] x [-3,5]. For ell(x,y)=-2x+3y, exact prefix slot
maximization gives -17<=ell<=17 throughout each proper east prefix, strictly
between -23 and23. Since ell(Az)=23*z_y, an A-lattice hit is m*A E=(3m,2m).
The x-coordinate box allows only m=-1,0,1,2. Source/target are m=0,1.

For m=-1, reaching x=-3 consumes every west move without an east move.
Parity of the alternating slots and y=-2 force arrival at time5, through
W,S,W,S,W. The remaining12 moves have horizontal letters all E, and six
vertical slots containing five N and one S. This gives exactly6 raw words.
For m=2, x=6 consumes every east move without a west move. The same slot
and parity check forces arrival at time12; the first12 moves have all six
horizontal letters E and vertical letters five N and one S. The remaining
five letters are W,S,W,S,W. Again there are exactly6 raw words.

Every one of these12 raw words has an internal same-cell same-turn conflict,
for BOTH perpendicular initial headings, by zero-based read15. The complete
24 checks are `raw_alien_conflicts.json`, in incoming-heading order N,S.
Its SHA256 is
0ab62cc02f454708cb50826077c353b1a1cdb9b68860cd839a756b0a9370bea0.

A north image has N9,S0,E5,W3, with nine vertical and eight horizontal slots.
The exact proper-prefix dual range is [0,22]. Thus any internal A-lattice hit
has coarse y-coordinate zero and is m*A E. The vertical height2m is
nonnegative. If m>0, the number of horizontal slots by that height is at most
2m, which cannot reach x=3m. If m=0, height zero occurs only at the source.
Thus no non-source internal A-lattice hit occurs in a north image. Half-turn
rotation handles west and south without changing ant chirality.

The independent raw inventory is4704 east words and56 north words. Internal
legality leaves534 east and56 north, all vertex-only. Hence all29,904
half-turn image pairs fall directly under GN. No long-prefix replay or
all-time automaton test is used for this conclusion. Frozen inventory and
scope accounting are `inventory.json` and `result.json`; the generator is
`../search_first_alien_mixing.py`.

This was a justified construction target because k17 is the first parameter
in A_l=[[3,2],[2,2l+1]], k=4l+1 that geometrically permits another coarse vertex
inside an east image. The result shows that geometrical access alone does not
suffice: its minimal excursion already violates ant chronology.
