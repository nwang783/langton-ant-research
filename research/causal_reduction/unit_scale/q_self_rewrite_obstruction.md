# Opposite-Q one-bit-deficit interface: a five-orbit short-repair obstruction

Status: author literal/CNF/RUP checked; independent semantic review pending. Fixed stationary exact-pose1/5/9 architecture only. No claim about other images, changed scaffolds, arbitrary temporal choices, or finite-seed existence in general.

Let Q be the frozen forward108 word in forward108_prepared_control.json. At (0,0,E), drift(2,2), it has three required-black classes (-8,1),(-7,0),(-6,0), and eleven output-black classes, as recorded in forward108_self_interfaces.json. Classes are (x-y,x mod2).

Place a second Q at (0,14,W), drifting(-2,-2). Its required-black classes are (-8,0),(-7,0),(-6,1). The first Q's complete output supplies the latter two, and agrees with EVERY required-white class of the second Q. Thus exactly one new black class, (-8,0), is missing. This is a genuine almost-interface between two nonstandard prepared fronts, not a standard-rail interface.

The first missing-class read is second-Q phase72, L at(-2,6) with incoming W. Its shortest white-starting exact-pose repair is RRRRL: fourR reads around a square, then the originalL. The resulting112-read word has no remaining first-color mismatch with the source output, but has literal repeated-R conflicts on other cells. It is not a valid front. The full source/target profiles and exact literal control are retained.

## Exact palette obstruction

At EVERY one of the108 coarse turns independently choose any internally legal exact-pose image of length1,5,9, from the same previously signed ten-image palette per turn. Preserve the coarse pose after every image. Require a stationary periodic body with the second-Q coarse path; output is unconstrained.

Even after allowing arbitrary entry colors on every orbit except the following five, no body is legal:

- (-8,0): white;
- (-7,1): white;
- (-6,0): white;
- (-5,1): black;
- (-4,0): white.

All five colors agree with the first Q's full output. Unconstrained cells remain physically consistent within their complete histories; the reduced CNF in fact drops all chronology constraints on those cells, which is an even more permissive relaxation. Its UNSAT therefore implies the asserted exclusion.

For a selected fine event at p in coarse phasej and local offseti, complete same-cell order is the lexicographic key (floor(p_x/2),j,i), since actual drift is(-2,-2). The existing Boolean first-color/XOR circuit is reused without its104-phase nonidentity clause. Every phase has exactly one chosen image; all final colors are free.

Full certificate: q_self_rewrite/self_rewrite.cnf/rup, 9,289variables,37,585clauses,29 checked monotone RUP additions.

Five-orbit relaxed certificate: q_self_rewrite/local_core.cnf/rup, 1,641variables,7,181clauses,25 checked monotone RUP additions. CNF SHA88c3eec63eebf710210c4a976c2bfeb8337458fa50b82e0e922c6539f5cee14f. RUP SHAce8b7ea2e3e757355a4355c7023ded3b909d9c45e0fe830e762ea0a76cb44e9d.

The identity Q on its own inferred input is a literal/CNF positive. The identity on the proposed source output, the minimal RRRRL phase72 attempt, and24 independently chosen sparse refinements all give identical circuit/literal results. These27 controls are in q_self_rewrite/controls.json.

The source Q still requires its own prepared input. No physical cap, bounded-fuel producer, or repeated composite route is supplied. This narrowly closes one especially favorable self-interface under the retained local palette, without enlarging that palette or scanning connector lengths.
