# Standard transport preserves the nonstandard factor sequence

## Statement

Let W be the standard 104-letter turn word, and let L10 be the set of all
length-ten factors of the two-sided periodic word W^infinity. A factor outside
L10 is called nonstandard here. This is a statement about turn words; it does
not assume that an arbitrary modified word is a physical ant trajectory.

Suppose a turn word has the form U V, where V has at least nine letters. Let P
be a cyclic rotation of W whose first nine letters agree with those of V.
Then the words U V and U P V have the same ordered sequence of nonstandard
length-ten factors, counted with multiplicity. In particular, inserting P
adds zero nonstandard factors.

The assertion applies to finite words with |V|>=9 and to infinite words. It
also applies with a specified finite prehistory before the first counted
event, provided the same prehistory is used on both sides.

## Proof

Locate the insertion at index zero. A length-ten factor that starts at a
negative index and crosses the insertion uses at most nine letters of V.
Those letters agree with the corresponding prefix of P, so this factor is
unchanged. Factors wholly before the insertion are also unchanged.

Every original factor whose starting index is nonnegative reappears 104
positions later. Its letters are still the same consecutive letters of V.

The only remaining factors of U P V start at indices 0 through 103. Each is
a factor of P followed by the first nine letters of V. Since these nine
letters agree with the prefix of P, all 104 factors belong to L10. Thus the
new factors are all standard, and every old nonstandard factor appears once
in the same order. This proves the assertion.

## Consequence for certified corridor transport

When a physical corridor theorem proves that lengthening a corridor inserts
standard periods at specified transits, the lemma removes those periods
without changing the nonstandard-factor sequence. One must check that each
inserted period is the standard word with the required phase. Positional
period 104 alone is not the stated word hypothesis.

For the corridor families whose external checker makes this additional
standard-word comparison, the illegal-factor sequence is independent of the
corridor lengths in the certified parameter region. This follows by applying
the lemma once per inserted period and once per transit.

This explains how travel time can grow without adding any nonstandard local
turn events. It gives a sound quotient of an already certified family. It
does not establish a finite list of such quotient words for arbitrary finite
initial support, or a decreasing rank on transitions between scar states.

## Attribution and scope

The word-insertion argument is elementary. No novelty claim is made. Its
application here uses the physical transport framework in
[the revised two-black-cell manuscript](https://github.com/imfinn/langton-two-black/blob/main/paper/TWO_BLACK_CELLS_REVISED.md),
sections 4–6. The manuscript's unrestricted theorem covers at most two
initially black cells and explicitly does not provide a general scar-network
termination theorem. The source was read on 21 October 2026; its retrieved
file blob was `b1b550fbac0a970f343ccc61509168e832bee71d`.
