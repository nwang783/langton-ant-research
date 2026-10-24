# One proposed D/W5 family fails at every parameter

Status: author exact affine/ordered-age proof PASS, 2026-10-23 15:18 UTC. This rejects ONE informed candidate family, not the general D/W5 gate.

For every integer w>=0 the complete packet word

DC,D,VC,VC,V^(w+2),VCC,V^w,D,V,V

is physically impossible on every board. This is an all-parameter proof, not a bounded word scan.

The fixed prefix ends at(-5,0,E), C-clock3. The E-oriented V run advances(3,-1) per packet. For w>=1, its THIRD V starts at(1,-2,E) and consumes q=(4,-2) as its lower input(0,3). For w0, the far VCC starts at that SAME pose and consumes q as the same lower input. Neither full V nor full VCC outputs its local(0,3), so that identity is retired at clock3 and is not reinstalled by the same producer.

After V^(w+2), the far VCC enters at(3w+1,-w-2,E) and exits at(3w+5,-w-2,W), clock5. The W-oriented V^w run advances(-3,+1) per packet, so the late D ALWAYS starts at(5,-2,W), clock5. Its input is again q=(4,-2).

Any identity now occupying q was genuinely born after the earlier retirement, at a full producer start clock>=3. Its C-age at this D is therefore<=2. Signed JO requires every produced D input age>=3, contradiction. The old entry identity exemption cannot be reused: that identity was explicitly retired at clock3. Any earlier raw contradiction also excludes the word and does not weaken this necessary-ledger argument.

The generator checks all affine endpoint coefficients, both w0/w>=1 consuming slots, exact absent outputs and the signed D minimum. No parameter range, path-depth bound or larger search is used. The surviving general D/W5 immediate V/U predecessor alternatives remain OPEN.
