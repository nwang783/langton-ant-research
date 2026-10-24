# Epoch-reset confinement for a DCUV factor with u U macros

Status: independently SIGNED, 2026-10-23 02:42 UTC, using signed DCV198, the DCV mass-only bound, and signed DCUV residual/boundary ledgers. This does not assert that u is bounded in an infinite tail.

Consider a physically feasible, context-complete factor of the eight recurrent packets D, DC, V, VC, VCC, U, UC, UCC, starting with m>=5 black cells. Let u be its number of U-family packets, equivalently its number of raw U macros. Define

B=57+38(m−5)+60u,
R=ceil(2B/5), A=(2R+1)^2, t=floor(A/3).

Claim: every visited cell and every newly produced black cell lies in the radius-R square around the entry head, and the factor has at most

20R(t+1)+28t

fine steps. Remote initial black debris need not lie in this square and remains untouched. Thus duration is O((m+u)^3), independently of the initial seed diameter.

## Four potentials with epoch labels

Use each rotation of L(x,y)=x+3y and the signed DCV max potentials. The core term is2L(p)+a_h with a=(2,52,54,−8). A typed DCV output carries its signed weight w in[−60,60], indexed by producer type, slot and heading; the maximum DCV input weight is60. A baseline token instead carries weight60 in every rotation.

Track the core and produced residual identities only. Initially unread residual tokens are inactive until first consumed, as in the signed deferred-activation proof. The DCUV ordered ledger guarantees such an initial identity is outside every previous complete packet context; input consumption permanently retires it. U's recycled input/output cell receives a new identity.

At a U-family packet, remove all inputs, reset every surviving active residual token to baseline weight60, and give every new U output baseline weight60. This begins a new DCV epoch. A later DCV input either has baseline weight60, which dominates its required input weight, or is supplied by a typed DCV producer since the last U packet. In the latter case all strict intermediate packets are among the five recurrent DCV types. The signed198 relation therefore applies with its genuine language premise. No DCV clause is used across a U packet.

An inactive initial token consumed by a DCV packet is inserted momentarily at baseline weight60. The signed activation calculation bounds the increase of each max potential by76. There are at most m−5 such activations. An inactive token consumed directly by a U packet needs no separate activation: the U-step bound below uses the old core term alone.

## Uniform reset cost

Resetting any surviving typed token from weight at least−60 to60 raises its term by at most120; the max over arbitrarily many such tokens also rises by at most120. Existing baseline tokens do not rise.

For every U/UC/UCC packet and every heading, compare its new core term and each new baseline output term against the old core term. Direct literal geometry gives a maximum difference100. Hence the entire U step, including reset, raises each max potential by at most max(120,100)=120. This argument is independent of its input ancestry.

Thus at every packet boundary the relevant rotated potential is at most

2L(p_entry)+54+76(m−5)+120u.

The ordinary DCV packet-prefix maximum is36. The U-family prefix maximum is40, and the common core maximum is14. These are all below the60 allowance obtained from the minimum active token weight−60. Therefore all produced black cells, core cells and fine read positions satisfy the four strips |x+3y|<=B and |−3x+y|<=B relative to the entry head. Inverting the two forms yields |x|,|y|<=2B/5.

## Duration

The total black mass is at most m+A, because all changed cells lie inside the square while initially remote debris is unchanged. Raw mass increments are D:0, C:3, V:4, U:4. Therefore C+V+U<=floor(A/3)=t. Each intervening D run has at most2R macros, since D translates by a fixed rotated(1,1). There are at most t+1 such runs. A non-D raw macro has length at most28, giving the stated duration.

For a hypothetical infinite DCUV tail of fixed entry mass, the bound implies u(T)=Omega(T^(1/3)) as fine time T grows. This is only a necessary recurrence rate, not a contradiction. A separately proved one-initial-token-per-U lemma would bound u<=m−5 and yield a DCUV exclusion and mass-only cubic duration bound, but that lemma remains open.

Independent analytic and literal-arithmetic signoff: audits/check_dcuv_epoch_reset_independent.py/json. The finite prefix and geometry controls supplement, rather than replace, the epoch-reset argument.
