# Short chronological proof of the one-sided first-departure forest

23 October 2026, 11:30 UTC. Alternative proof candidate of the already
independently signed finite-root theorem. No stronger claim is added.

Include each initially-black physical cell as an isolated TERMINAL from
the start. Whenever an initially-white cell is read for the first time,
add the directed edge from it to the cell entered after its R turn. Do not
add edges on later reads or on initially-black cells.

A discovery run is a maximal consecutive string of reads at previously
UNREAD initially-white cells. All of its turns are R. Except for a run
beginning at time0, let u be the cell read immediately before the run and
let I be the direction of entry into its first fresh cell v. The first
three R moves from v go to

    v+R(I),       v+R(I)-I,       v-I=u.

Since u was already read, this discovery run contains at most THREE fresh
white cells. It may stop earlier at any previously-read cell or at an
initially-black cell. Its new first-departure edges form just one directed
path from its fresh cells to that old/black endpoint.

Crucially, no old white first-departure edge can point into these new
previously-unread cells: its target was read immediately after that old
cell's earlier first R. Thus attaching this new path to the completed
older graph cannot create a new cycle or join two old components. It only
adds a path to one already-established root component. If the endpoint is
initially black, its terminal was included from the start.

The only exceptional run is the one starting at the initial head at time0,
if that cell is initially white. It ends at a black terminal before four
R turns, or else its FOUR R turns close exactly the initial unit face.
That is the unique possible directed cycle. If the head is initially
black, even the first white discovery run has the ordinary old source and
there is no exceptional cycle.

Induct over completed discovery runs. Every new white path attaches to an
initially-black terminal component or the one initial unit-cycle component.
A finite observation ending midway through a discovery run has one open
fresh path, but that run necessarily completes within at most three/four
fresh reads; it cannot be an infinite new-white run. Every actual visited
white cell therefore has a finite path to one of these roots.

With m initial black cells there are at most m+1 root components. This
proof needs no finite-width, visit-cap, eventual-periodicity, infinite-ray
compactness or eight-step polygon classification. Initial black support
need be finite only for the numerical root count. Infinite incoming trees
and unbounded branching at the same root remain uncontrolled.
