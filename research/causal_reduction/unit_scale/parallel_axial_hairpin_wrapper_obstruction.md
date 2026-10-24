# Parallel axial hairpins cannot be assembled by a fixed prolongable emitter

Status: author analytic proof, independent review requested. This is an all-length obstruction for the precise positive shuttle alphabet below, not for arbitrary decorated controllers, arbitrary axial paths, changing centers, or two-dimensional assemblies.

## 1. Exact supplied components

Use the independently signed axial hairpin from decorated_axial_hairpin.md:

U=RRLRRRRL, V=LLRLLRLL, W_n=U^n R V^n.

With incoming N it starts at a center c, has the same complete endpoint pose as one R read, and its recursive offset is (2,0). Denote this component b+. Its half-turn rotated copy, incoming S and recursive offset(-2,0), is b-. All other labels below are single-read identities. There may be any finite number of separately decorated copies of either component.

For n>=1, at EVERY interior column c_x+2 <= X <= c_x+2n-1, the COMPLETE field change of b+ is exactly

black(X,c_y+2) -> white,
white(X,c_y-2) -> black,
all other cells on that column unchanged.

This follows directly from the signed full input/output table, not from a minimum-mass assumption. Any initial black cells outside the component's read support remain unchanged. The alternating rails inside the support return to their original values. The reflected b- never reads a column X>c_x.

## 2. Prolongable emitter architecture

Allow one root label a with any fixed finite nonempty physical base word A and a substitution

phi(a)=a w.

The fixed finite typed word w contains any number of the supplied b+/b- copies and identity read labels. Require exact physical pose composition: w is closed at the endpoint pose of A, and each component image has the same endpoint pose as its base read. Thus every occurrence of each component in w has one FIXED physical center, independent of its refinement depth. Require at least one growing hairpin occurrence in w.

The images of the hairpin labels are precisely U b V with the corresponding proper rotation, all its nonrecursive children being identities. Identity labels map to themselves. No image-length bound is imposed on A or w, and no bound or conservation assumption is imposed on root charge.

Then the actual nested physical prefix is

A · w · phi(w) · ... · phi^(r-1)(w).

All these factors begin at the same pose because w and its refinements are closed. If there are no b+ occurrences, rotate the whole system by180 degrees. Therefore assume m+>=1.

## 3. Remote-column bounded potential

Choose an integer X strictly greater than every x-coordinate read by A or by an identity occurrence of w, and at least two greater than every hairpin center's x-coordinate. This is a fixed finite choice. Every b- misses column X at every depth. Every b+ has column X in its stable interior once

n >= N = max(1, max_j ceil((X-c_(j,x)+1)/2)).

Let y_min=min_j(c_(j,y)-2), y_max=max_j(c_(j,y)+2), H=y_max-y_min, with j ranging over b+ occurrences. No late layer reads column X outside these rows. For the CURRENT actual board define

M = sum_(y=y_min)^y_max (y-y_min) * black(X,y).

Regardless of the background, 0 <= M <= H(H+1)/2. Every legally completed b+ lowers M by exactly4. Every b- and every identity occurrence leaves M unchanged. Consequently every legally completed layer phi^n(w), n>=N, lowers M by exactly4m+.

There cannot be infinitely many such layers. More explicitly, the prefix phi^r(a) cannot be legal on ANY initial board once

r >= N + floor(H(H+1)/(8m+)) + 1.

Overlaps between different b+ components do not weaken the argument: if they create a color conflict, legality has already failed; otherwise each component's complete field delta applies in its actual chronological entry board, and the changes add.

## 4. Meaning and boundaries

This closes the natural attempt to fund several opposed axial shuttles by a charge-producing closed root word. A large root charge cannot repair the remote repeated bulk row transfer: root and identity work remains at fixed finite centers, while all shuttles reaching a chosen remote ray move black mass in the same transverse direction inside a fixed-height column.

The result uses the exact supplied b+/b- bulk contract. It does NOT establish a new general no-go for all axial drifting SCCs. It does not cover perpendicular shuttle orientations, another operator that raises the remote-column potential, moving emitter centers, a different recursive image, or nonstationary schedules whose endpoint effects repeatedly visit the chosen column. Each isolated W_n remains a valid prepared positive component.
