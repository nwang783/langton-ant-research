# Status

Core geometry theorem: proved and independently passed on 2026-10-23.

Frozen proof: PROOF.md
SHA256: 8647be7a9158e11985f60a7643c64411d0cd396e73449ed02032c084f7e7303f

Result: any vertex-simple n-edge unit square-lattice open path has |R-L|<8 sqrt(n-1)+2 for n>=2, with n<=1 giving zero. The sharp asymptotic order is Theta(sqrt(n)); outward square spirals provide the lower bound. The constant 8 is not claimed optimal.

Report: /workspace/shared/langton/audits/check_simple_path_signed_turning_independent.json
Report SHA256: 73de9da368f95973f32a11515b3730ce85f0dbf680355678c8173558cf61d26b
Checker: /workspace/shared/langton/audits/check_simple_path_signed_turning_independent.py
Checker SHA256: 35bc16d86309e7d7c5448e2e3d21571a4472f42f5b6f1da0528c63f9b920ec73

Reviewer explicitly passed the full secant-triangle lift, endpoint polar-angle identity, midpoint truncation and radius<1/4 ray separation, unordered distinct-height charging, signs, endpoint degeneracies, and independent spiral/staircase/crossing controls. The ant-specific bridge theorem and global cubic application are separate claims, not certified by this geometry note.
