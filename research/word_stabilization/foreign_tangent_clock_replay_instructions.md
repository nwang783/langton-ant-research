# Replay instructions for the graph-clock certificate

The frozen checker is a byte-identical source snapshot; its original relative ROOT layout is intentionally preserved. Do not execute that deeper copy as though it had been relocated.

Working commands, from any directory:

    python /workspace/shared/langton/word_stabilization/check_foreign_tangent_graph_clock.py
    python /workspace/shared/langton/audits/check_foreign_tangent_graph_clock_independent.py

The first reads the immutable original quotient and reproduces the author's certificate at its original location. The independent checker is the preferred no-author-import replay. The frozen manifestc4d33c77 and its source/proof/JSON hashes remain unchanged. This instruction file is not a proof premise.
