# A logarithmic global renewal law from actual active-component inheritance

23 October 2026, 22:15 UTC. Author derivation; independent audit requested.
The frozen cycle-birth finite-fuel note is unchanged. This is a lower bound
on necessary actual renewals, not an upper defect budget or capture proof.

## 1. Exact event counts on any physical interval

At an arbitrary actual interval entry let m be the complete finite black mass
and beta the total cycle rank of the w-black graph. For its T physical updates,
let:

- A count all wholly contained literal RRRR factors;
- H count R updates whose inserted w-black edge has already-connected
  endpoints, i.e. raises the w-black cycle rank by one.

No reset or arbitrary elimination is made at any event. Old components,
restored travel edges, head and heading remain actual. Then

    T <= 6*(m+2)*3^(beta+A+2H).                       (1)

For T>0 this gives

    A+2H >= log_3(T/(6*(m+2)))-beta.                 (2)

Thus these concrete renewal events must recur at least logarithmically in
physical time, with explicit entry-mass/rank dependence. The right side may
be negative for short intervals; the inequality is still valid.

Every RRRR factor creates a z-black unit cycle on its fourth R. Every H event
is a literal w-black cycle birth. If B counts physical updates that create a
cycle in either black graph, A+2H<=3B. Therefore

    B >= (log_3(T/(6*(m+2)))-beta)/3.                (3)

This is an unrestricted finite-seed, arbitrary-word recurrence theorem.
It is NOT a positive density theorem, and none of these events is identified
with a nonstandard defect.

## 2. Ordinary and exceptional actual blocks

Partition the interval into complete blocks R^r L and its final R run.
Every actual R run has length at most four: four R's return to the same
physical pose with that cell now black, so a fifth R is impossible. Hence
complete blocks have at most five updates and the final run at most four.

Call a complete block exceptional if at least one condition holds:

1. r=4;
2. an R in it creates a w-black cycle;
3. its final L deletes a nonbridge w-black edge.

All other blocks are ordinary. An ordinary block has r<=3, every R adds a
bridge at the stationary w, and its final L crosses/deletes an edge already
black at block entry. The signed causal bridge law gives EXACT inheritance:
the post-L active component is the far component of the ENTRY active
component minus that L edge. Every newly R-attached component stays on the
old side, with all its edges physically retained. Thus each ordinary block
strictly lowers the active component's edge count by at least one.

Let E be the number of exceptional COMPLETE blocks. Blocks of type1 number
at most A. Blocks of type2 number at most H. Every nonbridge L lowers global
w-rank by one, while only the H updates can raise it. Thus type3 blocks
number at most beta+H. The union bound gives

    E <= beta+A+2H.                                 (4)

The terminal R run may itself contribute A or H; counting it can only weaken
this upper bound and creates no omitted state or timing charge.

## 3. Epoch accounting with complete passive memory

The E exceptional blocks separate ordinary blocks into E+1 epochs. At epoch
j entry let M_j be the COMPLETE black mass and let n_j be the number of
ordinary blocks in it. Exact component inheritance gives n_j<=M_j.
Each ordinary block raises mass by at most two, so the epoch raises total
mass by at most2M_j. Its following exceptional block raises mass by at most
three, since r<=4. Consequently

    M_(j+1)<=3M_j+3,
    M_j<=(m+2)*3^j-2.

This counts all abandoned R-written components in the global mass, even if
an exceptional block later imports them. There is no original-root budget
on their descendants and no replacement of a component by a bounded summary.

Summing the ordinary block counts and adding actual fine-step costs gives

    sum n_j <= (m+2)*(3^(E+1)-1)/2 - 2*(E+1),
    T <= 4*sum n_j + 5E + 4
      <= 2*(m+2)*(3^(E+1)-1)-3E-4
      <= 6*(m+2)*3^E.

Together with(4), this proves(1). The only planar input needed for the
inside-hull interpretation is the separately signed fact that a new black
edge outside the current separated rectangle union cannot close any cycle.
Every renewal counted in A or H is therefore an actual finite-hull
reconnection; topology-free outward extension alone cannot supply it.

## 4. Precisely what is, and is not, learned

A no-renewal interval has finite fuel. Long nonstandard LRRL transport on a
prepared rod nevertheless stays paired-forest and bi-exterior at every cut;
its duration grows with the actual prepared mass. No standard local word is
forced before renewal. Nor does(2) limit how often cycles may be created,
erased and recreated. The standard104 highway does so repeatedly itself.

The theorem supplies a full-state global causal constraint: every sustained
trajectory needs literal RRRR square creation or a genuinely connected-endpoint
w-graph insertion, with a quantitative count. It does not classify those
renewals as standard/nonstandard, show eventual periodicity, or make any
nonstandard event resource well founded. Universal capture remains open.
