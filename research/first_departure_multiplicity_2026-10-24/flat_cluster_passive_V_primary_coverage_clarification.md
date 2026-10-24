# Flat-cluster passive-V primary coverage clarification

24 October 2026. This supplements the frozen exact-three-flat cluster
note b71c5709, without changing its enumeration or source files.

For a singleton LEFT gap between two flat RIGHTs that touches no RR
run, BOTH outside neighbors of those RIGHTs are LEFT. Thus the physical
five-corner window is exactly the signed constant-flow-two GLOBAL-M
window e597889e. Its complete eight surviving primary words ALL have
current LEFT in {O,U}, never passive V. This is the necessary FIRST
implication excluding V from that primary gap. Then the separate signed
critical local-island theorem c9574fb8 excludes singleton U and gives
the stated O/Y/immediate-V restrictions.

The c957 root theorem alone would NOT exclude a passive V, because V is
not a root. The frozen prose's short attribution to that local-island
result must be read with the explicit e597 five-corner dependency above.
In particular the gap word (1,1) with two passive V contacts is excluded
by e597 at either of its two complete five-corner windows, not by calling
V a singleton root or silently deleting it.

The outside LEFTs may themselves belong to LL pairs; they are their
actual immediate physical contacts, so the window still applies. Their
flow is two because each adjacent RIGHT is flat. Arbitrarily old corner
histories were retained by e597's full 5,700-patch cover. No homogeneous
whole-circle or no-old-stock premise is imported.
