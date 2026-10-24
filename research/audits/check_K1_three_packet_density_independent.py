from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'K1_pipeline_detours_2026-10-23';pair={('i',0):('SE','SW'),('i',2):('NW','NE'),('o',1):('SE','NE'),('o',3):('NW','SW')};O=[];E=[]
for n in range(1,5):
 for hs in product((0,2),repeat=n):
  out=[(h+(1 if k%2==0 else-1))%4 for k,h in enumerate(hs)];fl={('i',h):hs.count(h)for h in(0,2)}|{('o',h):out.count(h)for h in(1,3)};ht={'NW':0}
  while len(ht)<4:
   for edge,(c,l)in pair.items():
    if c in ht:ht.setdefault(l,ht[c]-fl[edge])
    if l in ht:ht.setdefault(c,ht[l]+fl[edge])
  assert all(ht[c]-ht[l]==fl[e]for e,(c,l)in pair.items())
  # O is clockwise-rotated: NE is fixed low0, SW is H<=0.
  rh=tuple((h+1)%4 for h in hs);ro=tuple((h+1)%4 for h in out)
  if ht['SE']<=0 and rh.count(3)==1:
   j=rh.index(3);firstN=ro.index(0);assert j%2==0 and firstN<=j
   if ht['SE']<0:assert j==0
   else:assert j in(0,2)
   O.append([list(rh),ht['SE'],j,firstN])
  if ht['SE']==0 and out.count(1)==1:
   j=out.index(1)
   if 0 in hs and hs.index(0)<j:
    assert hs in((2,0,0),(2,0,0,0));E.append([list(hs),j])
assert len(E)==2
OE={tuple(h)for h,H,j,firstN in O if H==0};assert OE=={(3,1,1),(3,1,1,1),(1,1,3),(1,1,3,1)}
# Independent symbolic cyclic turn-word count for all small overapproximating
# words, not a numerical proof. The all-length inequalities are reviewed in prose.
controls=0
for length in range(1,11):
 for w in product('SRL',repeat=length):
  s=w.count('S');m=w.count('R')
  if not s or m!=w.count('L'):continue
  cyc=''.join(w)*2
  if 'RLL'in cyc or 'LLL'in cyc or 'RRR'in cyc:continue
  counts=Counter(w[i]+w[(i+1)%length]for i in range(length));r=counts['RL'];q=m-r
  assert q==counts['RR']+counts['RS']==counts['LL']+counts['SL']and counts['LL']<=counts['SL']<=s and q<=2*s
  # Start an alternating RL run at an R whose preceding pair is not RL.
  starts=[i for i in range(length)if w[i]=='R'and w[(i+1)%length]=='L'and not(w[(i-2)%length]=='R'and w[(i-1)%length]=='L')]
  lens=[]
  for i in starts:
   k=0
   while w[(i+2*k)%length]=='R'and w[(i+2*k+1)%length]=='L':k+=1;assert 2*k<=length
   lens.append(k)
  assert sum(lens)==r and len(lens)<=s+counts['RR']<=s+q
  if sum(n//3 for n in lens)<=q:assert length<=29*s
  controls+=1
out=dict(status='PASS local O/E history classifications and cyclic density arithmetic controls',note_sha256=hashlib.sha256((B/'K1_three_packet_return_and_straight_density.md').read_bytes()).hexdigest(),O_rows=O,E_rows=E,cyclic_word_controls=controls,scope='Finite three-packet chronology, same-Gamma return injectivity and all-length combinatorial inequalities separately reviewed analytically. Conditional leftmost branch-free complete-white cap4 K1 only; no fuel payment.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
