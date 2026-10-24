# Unequal-aspect43-cell loop and its complete two-contact scattering

23 October2026,10:15UTC. Author exact certificates complete; independent review
pending. This generalizes the separately signed equal-arm LF family. No
renewal or counterexample is claimed.

Let H be the retained standard104 turn word. For integers r,s>=3 define

    L_(r,s) = R H^r H[:68] R H^s H[:68]
              R H^r H[:68] R H^s H[:60].

The seed is the13-cell NE launch at(1,0), together with the same ten-cell
orthogonal-corner stencil at the three successive rotated corners. The four
corner positions are

    c0=(0,0),
    c1=(2r+3,2r+6),
    c2=(2(r-s)-3,2(r+s)+9),
    c3=(-2s-6,2s+3).

The complete43-cell seed is preserved in the JSON certificate as affine cell
families, not merely as local guards. From(0,0,N), the word has length
208(r+s)+268 and returns exactly to(0,0,N). Its complete output mass is
24(r+s)+87. Of the43 original black cells,11 survive and32 are erased;
the complete XOR has24(r+s)+108 cells. Origin is black, so the unmodified next
turn is L, not the R needed to repeat the loop.

`certify_unequal_four_corner_loop.py` checks684 affine read families and1604
nonempty prior-read relations over ALL r,s>=3. Its output JSON contains both
complete initial and complete final fields. Nine unequal literal controls
agree, but those samples are not the all-parameter proof.

## Whole-field scattering for both arms large

For EVERY r,s>=50, the actual continuation from the returned pose is

    C H^(s-10) D H^infinity,

with the identical fixed C4954 and D9458 words retained from the square case.
C ends at(13,33,N). The intermediate NW front is not permanent: it strikes the
remote SW-directed side of the original loop after s-10 full periods. D starts
at(33-2s,13+2s,N), and ends at(2-2s,38+2s,N). The subsequent NW tail is valid for
all future repetitions against the COMPLETE board, including every other old
side and endpoint guard.

The final canonical104 tail begins at total time

    208r+312s+13640,

at pose(2-2s,38+2s,N), with mass24r+36s+795 and drift(-2,2).
Neither the aspect ratio nor r-s is bounded. Threshold50 is sufficient, not
claimed minimal.

`certify_unequal_four_corner_capture.py` performs exact set comparisons on the
full two-parameter output, applies both complete collision XORs, and checks all
104 unbounded final read families with their262 nonempty prior relations.
No temporary highway segment is promoted to capture. Its JSON retains the
complete tail-entry field and binds the loop certificate hash.

Scope: these precise unmodified seed families only. Fixed repairs, other
corner interfaces, thin corridors, and different two-phase architectures are
not excluded by this result.
