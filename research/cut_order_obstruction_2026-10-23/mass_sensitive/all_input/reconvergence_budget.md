# An all-input reconvergence budget for recurrent-eight factors

23 October 2026. Exact topology identity and quantitative CONDITIONAL finite-factor
theorem. No boundedness of the historical rank is proved. This is neither the
one-parent KP auxiliary forest nor the physical cursor-token forest of audit LE.
It is also NOT the cycle rank of the current black Tait graph.

## 1. Retain every input, every output and every retired identity

Consider an actual context-complete recurrent-eight packet factor with initial
complete black mass m, entry residual mass r0=m-5, and packet types

    D, DC, V, VC, VCC, U, UC, UCC.

Use the signed ordered residual identity update E'=(E minus I) union O.
Every input identity is retired before fresh output identities are installed;
same-cell input/output recycling creates DIFFERENT identity vertices.

Build a historical directed incidence graph G:

- one vertex for each of the r0 initial residual identities;
- one vertex for every packet occurrence;
- one new vertex for each fresh output identity;
- edges input identity -> packet, for EVERY input;
- edges packet -> output identity, for EVERY output.

All retired vertices and incidence edges remain. Initial unread debris is
retained as isolated root vertices. An identity's producer is unique and it
has at most one consumer. Produced inputs come from strictly earlier packets.
Thus G is directed-acyclic. This does not make its underlying undirected graph
a forest: two siblings can reconverge at one later multi-input packet.

Let c be its number of undirected connected components and let

    beta=|Edges|-|Vertices|+c

be its undirected cycle rank. Let v count V,VC,VCC packets and u count U,UC,UCC.

## 2. Exact conservation of mergers and reconvergences

Every packet with a inputs and b outputs adds one packet vertex, b identity
vertices, and a+b edges. Initially there are r0 vertices and no edges. Hence

    beta=sum_packets(a-1)-r0+c
        =v+4u-r0+c.                                  (1)

The second equality uses literal input counts1,2,5 for D-,V-,U-family packets.
It is independent of output counts or a chosen auxiliary parent.

More locally, if a packet's inputs come from g DIFFERENT existing components,
then

    delta c=1-g,
    delta beta=a-g>=0.                               (2)

Only g-1 units are paid by joining different old components. All other input
multiplicity creates undirected reconvergence cycles inside already-connected
ancestry. No component can split or vanish from this historical graph. Thus
there are at most r0-1 cross-component merger units on a nonempty factor;
further multi-input excess must accumulate in beta.

The empty r0=0 case is separate: no packet can start because every packet has
at least one residual input. It has c=beta=0 and duration zero. Every nonempty
factor has r0>=1 and c>=1. Therefore, if beta<=B,

    s:=v+u <=v+4u <=B+r0-1.                         (3)

In particular, an infinite actual recurrent-eight tail must have unbounded
historical reconvergence rank. If beta stayed bounded, only finitely many
V/U-family packets could occur; the remaining D/DC tail would contradict
the independently signed D/C/V finite-tail theorem.

## 3. A diameter-independent quantitative bound, with no C-count premise

This can be made an explicit finite-factor bound. Let

    P(M)=193+f(M+21),

where the signed arbitrary-factor D/C/V duration bound is

    f(x)=20*R*(t+1)+18*t,
    R=ceil((114+76*(x-5))/5),
    t=floor((2R+1)^2/3).

The function P is increasing on nonnegative integer complete-board masses.
The source is ../../../word_stabilization/dcv_arbitrary_factor_cubic_trim.md;
its all-length boundary proof, not a finite test, is an inherited dependency.
Every physically realized D/DC stretch is a D/C/V factor, so its duration is
at most P of its entry complete mass.

Split the actual factor at its s V/U-family packets. There are s+1 intervening
D/DC stretches, some possibly empty. Each separator has length at most58 and
net mass gain at most10: its C count is at most two and its residual increment
is3*C+4. Define recursively

    M_0=m,
    M_(j+1)=M_j+P(M_j)+10.

The complete mass entering the jth D/DC stretch is at most M_j. This follows
by induction because every physical read raises mass by at most one, and the
separator adds at most10. Thus the total raw duration L obeys

    L<=sum_(j=0)^s P(M_j)+58s
      =M_s-m+48s+P(M_s).                            (4)

For a bound beta<=B on the entire factor, replace s by S=B+r0-1 in (4), using
monotonicity. Equations (3)--(4) give an explicit iterated-cubic, diameter-
independent runtime bound in initial mass and ALL-INPUT cycle rank, with NO
separate upper bound on C count. Empty factors are handled separately above.

This is a meaningful conditional finite coupled-branch criterion: a new
geometric or chronological theorem bounding beta would finish this restricted
language. The present work does not provide that theorem. It also does not
extend the recurrent-eight conclusion to arbitrary residual UNION6 events.

## 4. Finite root sets are not a decreasing resource

For each output, define its FULL ancestor root set as the union of the root
sets of ALL inputs. Along any directed causal ray, these finite sets can grow
strictly at most r0-1 times and eventually stabilize. This elementary fact
does not bound beta: branches with the same fixed root set may reconverge
arbitrarily many times. A directed cycle is never required.

The companion aged_cleanup_countermodel.md gives an explicit fixed-eight-root
resource DAG with exact DC/V/D input-output COUNTS, all produced inputs age8,
coherent birth-heading congruence, collision-free current cells and the
numerical LB root boxes. Every main generation's three old spares are really
retired before continuation, but V helpers continually merge siblings from
the SAME initial root. Root sets remain singleton, c remains8, while beta
increases once per helper. This shows why mandatory side retirement alone
does not imply imported roots or new initial-root interactions.

That model is deliberately not a literal packet history. It omits exact
relative masks, simultaneous core/white guards, and spatial endpoint continuity
of one head. In particular, the DCV duration theorem used in (4) applies ONLY
to an actual chronological word. Infinite abstract unary combs with beta=0
cannot be rejected by applying P to their teleported local operations.

## 5. Exact physical constraints still needed

The historical graph retains simultaneous input multiplicity and causal
provenance, but does not encode

- the actual packet start/end pose relation;
- one common five-cell core transported between successive packets;
- every forced white entry in each complete RAW+marker context;
- the requirement that all specified input identities coexist at that pose.

LJ's sibling-clearance theorem and LH's multigeneration historical-color
exclusions genuinely use some of these omitted constraints. They must not be
replaced by a claim that finite roots or directed acyclicity forbids cleanup.
Conversely, a sibling retirement need not create a reconvergence: unary D
cleanup has a=1 and delta beta=0. The restricted physical finite-tail theorem,
not topology alone, is what rules out endless all-unary activity in (4).

No claim about external novelty, universal capture, finite initial mass at
all times, or an executable counterexample is made. Independent review requested.
