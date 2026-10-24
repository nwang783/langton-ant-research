# Two opposite-corner continuations with complete old history

## Scope and exact families

Let `m>=100`, `n-m>=100`, and `k>=100`, independently. Let

- `q_n=(-2n-33,-2n-14)`;
- `s_m=(6-2m,-43-2m)+Q_NE(r)`, where `Q_NE(r)` is the phase-r read
  of the canonical word W from `(0,0),E`;
- for r=70, `D_k=(2k-10,2k-69)`;
- for r=75, `D_k=(2k+48,2k+9)`.

Start the actual ant at `(0,0),N` with exactly these three cells black.
The exact complete-history certificates prove:

| r | first D read | certified capture | pose and phase |
|---|---|---|---|
|70|208n+104k+68135|208n+208k+127655|(-14,29),W, phase103, NW drift|
|75|208n+104k+113683|208n+312k+219742|(2k+11,2k+41),N, phase0, NW drift|

These are certified capture times, not necessarily first capture times.
There is no restriction comparing n and k.

## Complete-field transfer, not an infinite-rail approximation

The parent `../bridge.json` proves equality between the entire original
finite field and its fixed endcap model on the whole half-plane z>=-250.
It lists every omitted component, including the old blank packet, old SW
endpoint, q packet, old NE deposits, local recovery writes and both starting
cores. Before this interface D lies above every read of the original
q+s prefix. Its presence therefore merely toggles the same cell in both
fields at cap entry.

`certify.py` retains the endcap packet, both canonical rail families for
100 periods, the complete incoming core, and D. Every omitted deposit of
the infinite cap model lies below -250. The complete finite-kernel color
replay, including the infinite final tail, has every read z>=-105. Thus
both the kernel-to-model and model-to-original transfers follow from the
same explicit whole-half-plane coupling. No older field is discarded when
the ant reverses or crosses its own rail.

The two exact bivariate-engine replays use only one active variable,
k=U+100. They check respectively 9,646,408 and 65,464,268 isolated
nonincidences. The second variable is fixed at zero. All variable blocks
are cyclic standard104 words; these families do not provide unbounded
nonstandard-event counts at fixed initial mass.

`certify_interface.py` independently binds the exact formulas to the
inherited cap certificates and full-history interface. The entire finite
archive, including the final canonical core, has u in [-82,122] for70
and [-82,142] for75. This includes the original prefix, not just the newly
simulated cap.

## Two further mass-five recurrence exclusions

Fix m first and apply the previously audited exposed-corner/incidence
reduction. In a four-edge configuration the NE parent cannot reach an
opposite corner: all three remaining cells leave its bounded-u strip.
In a four-cycle the only possible next exceptional cell is D_k. Its age
k tends to infinity; ordinary impacts already escape beyond the bounded
archive. The other corners are

`A=(-2n-33,D_k.y)` and `C=(D_k.x,-2n-14)`.

For70, `u(A)=-2(n+k)+36` and `u(C)=2(n+k)+4`. Both miss the entire
finite three-cell prefix, and C misses its infinite NW tail. The final
NW exceptional72 ray has even x whereas A has odd x. Any later A impact
therefore belongs to the nine favorable ordinary channels. Its whole
recovery stays at u<=u(A)+58, strictly below the complete old archive and
all remaining cells. This is the established fixed-core recurrence
argument; no unverified finite-age threshold is silently added.

For75, `u(A)=-2(n+k)-42`, `u(C)=2(n+k)+62`. These exclude both from the
finite prefix. The final NW tail has z in [4k+45,4k+55], whereas
`z(A)=2k-2n-24`, so A also misses the complete infinite tail. C is excluded
by its u bound. In this case the stronger uniform statement is proved:
adding both A and C initially leaves the displayed entire three-cell
trajectory unchanged for every independent m,n-m,k>=100. Hence this
specific five-cell family captures at the same displayed time.

Together with the ten parity exclusions and four scar exclusions in the
parent directory, this closes16 of22 return-NE phase classes. The six
matching adjacent-corner classes15,29,45,56,62,72 are separate work. This
is neither arbitrary-core stability nor a proof of the highway conjecture.
