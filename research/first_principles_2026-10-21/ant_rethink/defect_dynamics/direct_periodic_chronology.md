# Exact direct chronology for a proposed periodic turn word

## Result and scope

A proposed nonzero translating turn word can be checked directly, without
guessing a wake first. The criterion below is necessary and sufficient for
the word to repeat forever from some finite black set. It does not classify
all such words or prove that an arbitrary trajectory reaches one.

This is a reformulation of the established lifted-rank/ordered-visit
condition, not a claim of a new invariant. The finite seed construction and
its support restriction are stated explicitly because the unrestricted
ray-sum formula would incorrectly make the seed infinite on odd classes.

## 1. The criterion

Let w=w_0...w_(P-1) be a word in R,L. Draw its path from a specified initial
heading, with p_i the physical cell processed at update i. Suppose the
heading returns after P updates and

    p_P=p_0+d,  d!=0.

Partition the P events into translation classes modulo Z*d. In one class,
choose a representative q and write p_i=q+a_i*d. The integer a_i is the
longitudinal coordinate within this class. Order its events by

    decreasing a_i, then increasing i at equal a_i.

**Criterion.** The word repeats forever from some finite-support initial
black board if and only if every ordered class spells R,L,R,L,..., starting
with R. Equivalently, writing L_i=1 for a left turn,

    L_i = ( #{j in the same class : a_j>a_i}
            + #{j<i : p_j=p_i} ) mod 2.

### Necessity

Choose K large enough that q+K*d is initially white and K>=max a_i. Such K
exists because the initial black set is finite. Every event type i in this
class visits that physical cell once, at time

    (K-a_i)*P+i.

Thus its event order is exactly decreasing a_i and then increasing i.
Repeated visits to one physical cell alternate colors. Its first visit is
white. The stated R,L alternation follows.

### Sufficiency and an explicit finite seed

Put alpha=min a_i and beta=max a_i in each class. Its entire forward read
set consists of q+a*d for integers a>=alpha. Define the initial color by

    B0(q+a*d) = #{i : a_i>a} mod 2,  for alpha<=a<=beta,
    B0(q+a*d) = 0 otherwise.

Only finitely many classes and finitely many a occur, so B0 is finite.
Consider event i in period k, at physical position q+a*d with a=a_i+k.
The event types j already processed at this physical cell are exactly

    a_i<a_j<=a,

together with the equal-position events j<i. Adding their visit parity to
the initial bit B0 contributes all a_j>a_i, plus those equal-position
earlier events. The resulting color is precisely L_i by the criterion.
Induction on event time therefore reproduces the word forever.

The initial colors are uniquely determined on the forward read set.
Arbitrary finitely many extra black cells outside that set are never read
and may be added without changing the trajectory.

## 2. The ray-sum formula needs a support restriction

Let V(p) be the parity of the number of visits to p in the one-period word,
and let S=union_{k>=0}{p_i+k*d : 0<=i<P}. The constructed seed is equivalently

    B0(p) = XOR_{k>=1} V(p+k*d),  for p in S,
    B0(p) = 0,                   for p outside S.

For each p the sum is finite. The restriction p in S is essential. Without
it, an odd translation class would give an infinite black ray behind the
period footprint. The standard highway has twelve odd classes, so its
unrestricted ray-sum would not be a finite seed.

The class alternation also gives

    #R-#L = number of classes with an odd number of events.

This is the black-count increase over one period. It is a consequence of
the chronology criterion, not an additional condition added to the solver.

## 3. Axial drift (2,0)

With p_i=(x_i,y_i), two events are in the same class exactly when

    y_j=y_i and x_j=x_i (mod 2).

The required parity is therefore

    L_i = XOR_j [ y_j=y_i and x_j>x_i and x_j=x_i (mod 2) ]
          XOR XOR_{j<i} [ p_j=p_i ].

For heading N at time zero, position parity cycles through

    (0,0), (1,0), (1,1), (0,1)

as i runs modulo four, regardless of turns. Thus same-class events must
satisfy j=i (mod 4); this removes three quarters of the pair terms.

For an axial period one may also normalize y_i<=0 and choose initial
heading N. The vertical displacement is zero, and vertical steps occur,
so the cyclic path reaches its maximum y by an upward step somewhere.
Choose that arrival as time zero, translate its position to the origin,
and retain the same cyclic period word. The upper-y normalization is a
symmetry choice, not a width bound.

## 4. Encoding and independent SAT verification

`periodic_word_smt.py` uses Boolean heading signs and signed bit-vector
coordinates. Axis alternation is built in. At every event, exact reachability
bounds from the beginning and endpoint keep the coordinates inside the
signed range. The transverse comparison is sign-extended, so arithmetic
wrap cannot create spurious class equality.

The turning bit is the XOR of the leading-first comparisons, with earlier
equal-position events added. There is no relaxation of visit order, and no
assumed period ceiling beyond the specific instance being solved.

Every SAT word is checked again by a separate ordinary-integer routine. It
reconstructs every ordered class, constructs the finite seed above, replays
one full period, and verifies the exact infinite-ray discrepancy criterion.
Thus a SAT model is not accepted merely because the SMT solver prints SAT.

The negative solver reports below were not exported as independently checked
proof objects. They are exploratory solver results, not a new formally
verified exclusion theorem.

## 5. Completed bounded runs

| Instance | Fixed word? | Result | Solver time |
|---|---|---|---:|
| P104, drift(-2,2), standard word | Yes | SAT; independent exact tail check passed | 0.047 s |
| P24, drift(0,-2), T24 word | Yes | UNSAT | 0.002 s |
| P12, drift(2,0) | No | UNSAT | 0.013 s |
| P28, drift(2,0) | No | UNSAT | 0.918 s |
| P52, drift(2,0) | No | UNKNOWN: 30 s timeout | 30.269 s |
| P104, drift(2,0) | No | UNKNOWN: 30 s timeout | 30.110 s |

The fixed positive control reconstructs a 13-black-cell seed and has twelve
odd classes among twenty-two. Its growth is twelve. The fixed T24 negative
control is a physically consistent one-period walk whose infinite axial
repetition requires non-finite support; it must fail the leading-first
finite-support condition and does.

This negative control also has an immediate ordinary-integer check. For
drift (0,-2), its class x=0,y odd has ordered events 23,3 with letters L,R;
its class x=-2,y even has ordered events 8,12,20,16 with letters L,R,L,R.
Both start with L on the leading visit, violating the required initial
white color far along the highway.

No alternative highway was found. Neither UNKNOWN instance is excluded.
No expanded or long search followed these runs.

Result files are `periodic_word_smt_controls.jsonl`,
`periodic_word_smt_axial28.jsonl`, `periodic_word_smt_axial52.jsonl`, and
`periodic_word_smt_axial104.jsonl`.

## 6. Dependency and reproduction

The primary runtime initially had no Z3 or SAT/SMT executable. The public
package `z3-solver==5.3.1.0` was installed into the local `deps` directory;
its API reports Z3 5.3.1. It was a prebuilt manylinux x86-64 wheel. No Z3
source build or solver correctness audit was performed.

The 82 MB dependency directory is not part of the research artifact. Recreate
it with:

    python3 -m pip install --target ant_rethink/defect_dynamics/deps z3-solver==5.3.1.0

Then, from the workspace root:

    python3 ant_rethink/defect_dynamics/periodic_word_smt.py --controls --period 12
    python3 ant_rethink/defect_dynamics/periodic_word_smt.py --period 28 --timeout 15000
    python3 ant_rethink/defect_dynamics/periodic_word_smt.py --period 52 --timeout 30000
    python3 ant_rethink/defect_dynamics/periodic_word_smt.py --period 104 --timeout 30000

The analytic equivalence above is independent of Z3. The tested SAT witness
is verified by integer arithmetic and finite-ray checks. Trust in the UNSAT
reports includes the solver implementation and execution environment.
