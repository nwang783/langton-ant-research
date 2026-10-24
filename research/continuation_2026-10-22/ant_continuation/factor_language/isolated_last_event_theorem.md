# A last forbidden ten turn window cannot be isolated on its left

## Status

This is a new result from this session, with no claim of publication priority.
It is a restricted theorem. It does not prove that the number of events is finite.
The proof uses an exact finite enumeration and the prior project
statement that an all-future ten-legal finite-support orbit eventually has the
standard 104-turn word. That prior statement is in Hao Ke's
`factor_language/proof/ten.md`, Theorems A and B. The reviewed snapshot was
compared with the pinned commit below. It differs only by one added terminal
newline; both SHA-256 values are in `../SOURCES.json`.

Primary source URL:
https://github.com/kehao95/langtons-ant-core/blob/22e0c9edcc566a4c2f7a9bf92f5cd05c19199617/factor_language/proof/ten.md

The new finite enumeration has two implementations. Both passed. There is no
Lean proof or external mathematical review.

## Definitions

Use the classical rule: white turns right, black turns left, then flip the
current cell and move one unit. Let W be the standard 104-letter turn word.
The code uses its lexicographically least cyclic phase:

```
LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRR
```

Let F be its 84 cyclic length-ten factors. A finite turn word is ten-legal when
each contained ten-letter factor is in F. At time t, let J(t) be one if the
true ten-letter turn word ending at t is outside F. The ant rule is reversible,
so the definition uses actual inverse steps when t is near the chosen input time.

## Theorem

For an orbit from a finite black set, if J(t)=1 and J(t-1)=0, there is an integer
u>t with J(u)=1.

Equivalently, whenever there is a last J event, the immediately preceding update
is also a J event. This does not say that every event has an adjacent event.

The same finite enumeration proves a statement with no finite-support premise:
an actual stream with J(t-1)=0, J(t)=1, and no later J event cannot eventually
equal a cyclic phase of W repeated forever.

## Proof

For a prescribed finite word, the path is fixed after an initial pose is fixed.
The word is physically feasible exactly when consecutive reads of every physical
cell request opposite letters. Necessity follows from the flip. For sufficiency,
make each first-L cell black initially, and each first-R cell white. Induction on
the steps proves execution. This uses a finite initial field for every finite word.

Enumerate all physically feasible ten-legal words of length 150. There are 6,605.
For each such word, put an edge from its first 149 letters to its last 149 letters.
This gives a finite graph G with 6,501 vertices. Every actual infinite ten-legal
continuation, after it has 149 preceding legal letters, follows G. The graph can
also contain paths that are not physically feasible at a longer length. Only the
inclusion of all physical paths is needed here.

Let C be the 104 vertices which are cyclic 149-letter factors of W. Compute R,
the vertices from which C is reachable in G. Reverse graph search gives |R|=925.
The search follows every edge; it does not use a time or seed-size cutoff.

Now enumerate every feasible word z of length 160 with these conditions:

1. Its first ten letters form a member of F.
2. Its ten-letter factor ending at index 10 is outside F.
3. Every ten-letter factor ending at indices 11 through 159 is in F.

Indices start at zero. There are 84 possible initial ten-letter words. Exactly
42 feasible next-letter extensions satisfy condition 2. Extending them under
condition 3 and physical consistency gives exactly 20 complete words. For each
of these 20 words, its final 149-letter suffix is outside R. These are direct
finite checks. Their full outputs are retained, and two separate implementations
produce exactly the same sorted set.

Suppose J(t-1)=0 and J(t)=1, with no later event. The actual turns from t-10
through t+149 form one of the 20 words. Its final history is outside R. All later
updates follow G. It cannot later have a W history, since that would give a path
into C, contrary to the definition of R. This proves the arbitrary-coloring
statement.

For a finite initial field, the state after update t still has a finite black
set. No later J event means its future turn stream is ten-legal. Ke's conditional
attraction theorem then makes that future eventually standard W. The preceding
paragraph rules this out. Therefore another J event must occur. QED.

## Complete finite checks

The Python checker uses a map from each visited position to its last requested
letter. It adds an extension exactly when the requested next color alternates
and the relevant ten-window has the required membership status. Induction on
word length proves that every feasible candidate is generated once.

The C++ checker uses its own recursive path update and mutable cell-read map.
It starts at the empty word, branches on both letters, and applies the same
mathematical conditions directly. It reconstructs G and R independently.

Results:

| Item | Result |
| --- | ---: |
| Allowed ten-letter factors | 84 |
| Feasible ten-legal words of length 150 | 6,605 |
| Graph vertices | 6,501 |
| Vertices that can reach the standard cycle | 925 |
| Feasible one-event center extensions | 42 |
| Feasible length-160 survivors | 20 |
| Survivor suffixes that can reach the standard cycle | 0 |

The sorted 150-word file has SHA-256:

```
6b76e51621e15d2304f1c0baa28790cc267cabafca3fc03250dea8721b2b4794
```

This agrees with the independently retrieved source certificate hash. The 20
sorted survivors, one per line including the final newline, have SHA-256:

```
98a66c8fabfc29ff9e731430be3f6b7a4e56d6779d3eddb8b2da96ec573f0b58
```

Every survivor's central forbidden ten-factor is `RLRRRRLRRL`. The theorem does
not need a claim that this is the only possible forbidden factor in an arbitrary
orbit. It is only the surviving factor under the stated finite constraints.

## Reproduction

Run from this directory:

```
python3 one_defect_exit.py 10
python3 isolated_defect.py --pre 10 --post 149
g++ -O3 -std=c++17 check_one_defect.cpp -o check_one_defect
./check_one_defect cpp_isolated_words.txt
```

The file `words150.txt` can be deleted before the Python run to force complete
reconstruction. The C++ run always reconstructs the full graph.

## Limit of the result

The theorem permits an infinite sequence of isolated J events. Each event can
have a later event without any last event. The stronger statement that finitely
many adjacent event pairs imply eventual standard motion is still unproved.
The expanded no-adjacent-pair graph has a large non-simple component; its finite
state count alone does not prove that physical paths in it terminate.
