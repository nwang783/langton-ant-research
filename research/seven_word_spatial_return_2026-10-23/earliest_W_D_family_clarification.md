# D-family necessary-prefix clarification for e74dca08

In the C2(VCC/UCC) containing-role deduction, signed first-W-D means first
W BASE D-family. The actual fullpacket can be D or DC; it need not be plain D.
Read e74dca08's phrase "forced first W fullpacket D" as "forced first W
D-base, with actual fullpacket D or DC."

The proof uses only the necessary physical prefix VCC,D-RAW,M11 or
UCC,D-RAW,M11. If the first W fullpacket is plain D, the conflicting read is
the NEXT actual full word's tick1/read2. If it is DC, the same read belongs
to its OWN first C-tail tick1/read2. Actual C supplies that M11 prefix; no
extra marker is executed and no imaginary fullpacket boundary is installed.

All four actual source/full-consumer contexts VCC+D, VCC+DC, UCC+D,
UCC+DC reproduce the identical repeated-L conflicts at global ticks59/69.
Thus both first-W possibilities are excluded, and the C2 role closure remains
valid. The universal T<=2 portal guard and all exact candidate controls are
unchanged. Frozen e74dca08 sources are preserved, with this mandatory wording
qualification attached.
