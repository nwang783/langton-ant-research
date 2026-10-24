# Exact source/sink types refine the all-cap extremal matching

24 October 2026. Additive refinement to ALL_CAP_EXTREMAL_READ_COUPLING.md
(SHA16878553); author proof awaiting independent audit. It does not change the
frozen first theorem or assert classification. All complete WHITE-front
hypotheses and the BLACK reverse-output terminals remain in force.

Use the same graph E: u->v is marked exactly when the source event is u's FIRST
R and its successor is v's LAST read. Split even classes into e_s,e_o according
as first/last incoming headings are SAME/OPPOSITE. Keep n_1,n_o,n_s for singleton,
nonsingleton odd-OPPOSITE, nonsingleton odd-SAME, respectively.

For EVERY E edge u->v:

- A nonsingleton target v has opposite first/last incoming headings.
- A nonsingleton source u is even-SAME or odd-OPPOSITE.

Proof of the target rule: if v's last incoming heading equaled its first, its
earlier first read required an earlier departure from the SAME source neighbor
u. This contradicts the selected u read being first.

Proof of the source rule: v's last read is at F(u)+1. If u is nonsingleton, its
last departure occurs later; it therefore CANNOT use the same outgoing edge as
its first R, since that would revisit v after its last read. An even last-L
has a different outgoing edge exactly when its incoming heading equals u's
first heading. An odd last-R has a different outgoing edge exactly when its
incoming heading is opposite. These exhaust the two sector-compatible headings.

Consequently E has the following COMPLETE necessary port types:

    singleton or odd-OPPOSITE: at most one input and one output;
    even-SAME: source only (at most one output);
    even-OPPOSITE: sink only (at most one input);
    nonsingleton odd-SAME: isolated (no input or output).

In particular, with A=n_1+n_o,

    |E| <= A+min(e_s,e_o),       2|E| <= 2A+e_s+e_o.

These sharpen the earlier safe capacity A+floor((n_s+n_e)/2). They are NOT a
claim that every permitted port occurs, or that disconnected paths splice into
one actual event orbit.

Every E cycle has only singleton and odd-OPPOSITE vertices. At a singleton its
geometric corner is R, because its selected arrival is its first incoming
heading and its outgoing edge is its first R. At an odd-OPPOSITE vertex its
selected incoming heading is the last one, opposite the first, so the geometric
corner to its first-R outgoing edge is L. An essential simple cylinder circle
has equal R and L corners. Thus on EACH E cycle the numbers of singleton and
odd-OPPOSITE classes are equal, each exactly half its length. Therefore, for any
c_E distinct E cycles,

    n_1 >= ||d||infinity*c_E,       n_o >= ||d||infinity*c_E.

The cycle age identity P=sum(H-F)-length remains exact. Since a nonsingleton odd
history has at least two positive physical returns, its age is at least8;
hence P>=3*length for each E cycle. The bound8 is locally SHARP: the actual word
RRRRLRRRR, starting from the entirely WHITE board at head(0,0,N), has origin history
RLR with first/last headings N,S at times0,8. This finite actual control is
not a translating front; it prevents incorrectly demanding age>=12 merely
because both return intervals have length4. Four-step returns need not restore
the incoming heading.

Finally, every coincident selected event in the joint counterflow bound joins
TWO EVEN cells, since both endpoints lie on a reversed last-L cycle. The source
is even-SAME and target even-OPPOSITE, so the improved overlap budget is

    C <= min(e_s,e_o).

This refines a genuine all-cap coupling. It neither removes the overlap term
nor excludes reverse clearing cycles, and it does not promote zero-output cases
already excluded by the stronger retained growth theorem.
