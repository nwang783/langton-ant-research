# Elementary deterministic ancestry at a macro seam

This identity is literal geometry built into the five macro definitions. It is not a new global restriction or stabilization theorem. It supersedes the more expensive finite-closure proof of the common-star producer restriction.

Every macro C,V,U,Q,B ends with a four-R cursor node, respectively C11,V14,U24,Q60,B70. Every next macro begins LLLLRL. Normalize the final four-R node's first read to (0,0), incoming heading north. Its four R-tokens are written at

1. (0,0), heading north;
2. (1,0), heading east;
3. (1,-1), heading south;
4. (0,-1), heading west.

The macro ends at (0,0), heading north. The following prefix has reads

phase 0: L at (0,0), north;
phase 1: L at (-1,0), west;
phase 2: L at (-1,-1), south;
phase 3: L at (0,-1), east;
phase 4: R at (0,0), north;
phase 5: L at (1,0), east.

Consequently, in every physically feasible concatenation, the immediately preceding terminal star parents the next macro's nodes 1, 4, and 6 by slots 1, 4, and 2, respectively. Node1 has no R-output; node4 has one R-output; node6 has four R-outputs. Slot3 remains outstanding after this prefix.

The node6 edge is forward: writer and consumer both read its cell with incoming east heading. The two cursor vertices differ by (1,1). The new node6's first R has incoming north heading, equal to that of the parent star's first R. Thus the handoff preserves the star orientation.

The slot4 edge is backward: writer heading west, consumer heading east. It returns the new node4 to the parent's cursor vertex. Slot1 is forward and produces a zero-output leaf.

The first macro is the sole boundary exception: its consumed tokens may come from the entry board. This proves immediately that every internally sourced node6 after that boundary is parented by the preceding terminal star. In particular, a C11 producer cannot survive across any intervening macro before feeding node6.

## Relation to the earlier certificate

The independently audited full-five nine-cell certificate is correct but unnecessary for this identity. The stronger immediate-predecessor claim follows from the six read positions above. The C/V/B height-eight theorem remains nontrivial because it also uses fresh V terminal stars, short-word exclusions, and restrictions on other positive-node ancestry. Its common-star and C11-separation steps may be replaced by this elementary seam proof.

## The actual remaining ancestry questions

The deterministic seam consumes three terminal-star tokens, but does not bound the ancestry of the terminal stars themselves. Nor does it control the remaining slot3, the node4 output, or the internal Q/B input stars. Establishing bounded depth or finite productive ends requires new restrictions on those routes, not another certificate for the forced seam.
