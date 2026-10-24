# Primary source and evidence check

Checked 21 October 2026. This note records source access and exact scope. It
does not represent an external mathematical review.

## Langton-ant sources

1. Atharva Jillhewar, `langtons-ant-highway`, pinned commit
   `76a7e234e577d992d086c204c3dea00ae72cf10a`,
   `research-notes/growth12_research_2026-08-17.md`.
   URL: https://github.com/Atharva12456/langtons-ant-highway/blob/76a7e234e577d992d086c204c3dea00ae72cf10a/research-notes/growth12_research_2026-08-17.md
   The file exists and contains the all-period axis and even-diagonal growth-four
   exclusions cited in the supplied work. It labels primitive-diagonal growth
   four and growth eight open at that research stage. The width-ten bounded
   searches described there are incomplete. Its exclusions concern possible
   periodic highways, not entrance from every finite seed.

2. Hao Ke, `langtons-ant-core`, pinned commit
   `22e0c9edcc566a4c2f7a9bf92f5cd05c19199617`,
   `wake_synthesis/proof/periodic-growth-closure.md`.
   URL: https://github.com/kehao95/langtons-ant-core/blob/22e0c9edcc566a4c2f7a9bf92f5cd05c19199617/wake_synthesis/proof/periodic-growth-closure.md
   The file exists. It attributes the signed-residue and lifted-rank arguments
   to Jillhewar, supplies an explicit dependency chain and unit-diagonal
   exclusion, and proves the claimed lower bound eight for periodic wake
   growth. It explicitly does not prove capture of arbitrary finite seeds.

3. Kossi Roland Etse, *How Long Can The Escaping Ant Be Confined?*, MFCS 2026,
   publication date 21 August 2026.
   URL: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2026.49
   DOI: 10.4230/LIPIcs.MFCS.2026.49.
   The official Dagstuhl record and the paper exist. The subject is first exit
   from a finite domain. It gives a general bound, a factorial bound for square
   domains, and polynomial bounds for fixed-height rectangles. It also states
   that a coloring cannot repeat during one confined trajectory segment.
   None of these assertions says that the ant never returns to the region or
   that it enters a standard highway.

4. Hao Ke, canonical one-bit highway stability.
   URL: https://github.com/kehao95/langtons-ant-core/blob/22e0c9edcc566a4c2f7a9bf92f5cd05c19199617/highway_stability/proof/canonical-highway-one-bit-stability.md
   The written proof reduces arbitrary canonical age and one flipped site to
   739 finite cases, with an exact infinite-tail guard. It claims bounds of
   64,584 recovery steps and Chebyshev radius 78 after impact. The current
   top-level README says the original 739-case certificate is still missing
   from the release package. Reading this proof is not a replay of that missing
   evidence. Its guard argument would also extend a successful base case to
   the backward-infinite wake: the entire extra ray set is avoided. The result
   does not iterate automatically after a second perturbation, because the
   first recovery retains a scatter scar and old wakes.

## Supplied width-ten result

The three uploaded files include the analytic fresh-boundary note and two
descriptions of the finite width-ten exclusion. They are not by themselves a
complete replay package. However, the preceding workspace still exists at

    /workspace/scratch/e9806c664975/ant_research/phase2

and contains the referenced checker, raw runs and audit artifacts. Thus it is
incorrect to say the computation is unavailable merely because the attachments
contain only prose. This analysis inspected the reported coverage audit metadata
and the existence of the final raw run, but did not rerun the whole enumeration.
The finite classification is not a missing premise for the compactness theorem
written in this directory.

## OpenAI mathematics release

Official announcement, 6 October 2026:
https://openai.com/index/sharing-ai-progress-in-mathematics/

Primary repository:
https://github.com/openai/math

The README inspected through the GitHub tool reports 719 current manuscripts
in 372 families, about 4,000 attempted problems, and about three hours of Pro
thinking compute per result on average. It says the work has different levels
of verification and about 42 percent of top-line results have formalizations.
The original public collection was larger; current counts must not be called
719 separately accepted or externally reviewed solutions.

The inspected `CONTENTS.md` has no Langton-ant match. Its success on other
problems is a reason to attempt serious research. It is not evidence that a
specific uncompleted Langton argument is valid.

## Source copies

Exact fetched copies of the first two pinned notes were retained as intermediate
working files. Those third-party copies are not included in the delivered
research bundle; use the pinned URLs above. The source retrieval was through
the selected GitHub plugin. No repository was modified and no external message
was sent.
