# Three-C-slab fuel bound from the signed all-input ages

Status: independently signed in audit JV, including a separate literal arithmetic replay at audits/check_three_c_slab_arithmetic_independent.py/json. This does not prove finite C occurrence or DCUV capture.

Consider a finite context-complete recurrent-eight packet factor on a finite board with m black cells at entry, including the signed five-cell core. Let k be its number of C macros and L its number of raw steps. The signed all-input C-age theorem JO implies the following.

## Slab lemma

Suppose every packet starts before the third C macro of the factor: the total C count of packets strictly before each packet is at most2. The last packet may bring the total to3 or4.

Select these distinguished residual inputs:

- D/DC: its sole input, minimum produced age3.
- V/VC: input(1,2), minimum produced age3.
- VCC: both inputs, minimum produced age4.
- U/UC/UCC: all five inputs, minimum produced ages3 or4.

A selected input cannot have been produced within the slab, since the complete source-included/consumer-excluded C count would be at most2. Hence every selected input consumes an identity already residual at slab entry. These identities are distinct across the slab by the ordered remove-then-insert ledger, including U's recycled black cell. Therefore, with packet counts n_a,

w = n_D+n_DC+n_V+n_VC+2n_VCC+5(n_U+n_UC+n_UCC) <= m-5.

Fresh literal geometry gives, packetwise,

raw_length <=18*selected_input_count+15*C_count,
mass_change <=4*selected_input_count+3*C_count.

Consequently L<=18(m-5)+15k for the slab, and its next residual mass r'=m'-5 satisfies r'<=5(m-5)+3k. In particular, every complete factor with at most2 C macros has L<=18(m-5)+30. No initial-support diameter occurs.

## General finite C-count bound

Partition greedily into slabs, ending each nonterminal slab at the first packet that brings its C count to at least3. Packet C counts are0,1,2, so each completed slab contains3 or4 C macros. If there are b nonempty slabs, then b<=floor(k/3)+1. Let r_j be the residual mass entering slab j, indexed from0. Since each slab contains at most4 C macros,

r_(j+1) <=5*r_j+12,
r_j <=5^j*(m-2)-3.

Summing the slab duration inequalities gives

L <=18*(m-2)*(5^b-1)/4 -54*b +15*k
  <=18*(m-2)*(5^(floor(k/3)+1)-1)/4 +15*k.

The displayed quantity is an integer. It is only an exponential finite-C-count bound. In an infinite finite-support recurrent-eight tail it implies C(t)=Omega(log t), not bounded C, bounded U, or a highway theorem.

The already signed203-step arbitrary-factor trimming argument would transfer the monotone upper bound to arbitrary finite literal D/C/V/U macro factors with m replaced by m+21 and an added203. That boundary extension is not needed for the slab lemma and is not silently added to its review request.
