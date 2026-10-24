"""Fresh local physical port/face/ordinal reconstruction for the penultimate source registers."""
from itertools import product
from collections import Counter
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'K1_pipeline_detours_2026-10-23';rows=[]
facepairs={('i',0):('SE','SW'),('i',2):('NW','NE'),('o',1):('SE','NE'),('o',3):('NW','SW')}
for n in range(1,5):
 for heads in product((0,2),repeat=n):
  outs=[(h+(1 if k%2==0 else -1))%4 for k,h in enumerate(heads)];flows={('i',h):heads.count(h)for h in(0,2)}|{('o',h):outs.count(h)for h in(1,3)}
  ht={'NW':0}
  while len(ht)<4:
   for e,(c,l)in facepairs.items():
    if c in ht:ht.setdefault(l,ht[c]-flows[e])
    if l in ht:ht.setdefault(c,ht[l]+flows[e])
  assert all(ht[c]-ht[l]==flows[e]for e,(c,l)in facepairs.items())
  ords=Counter();ins=[];os=[]
  for hi,ho in zip(heads,outs):
   for typ,h,dest in [('i',hi,ins),('o',ho,os)]:ords[typ,h]+=1;dest.append(ht[facepairs[typ,h][0]]-ords[typ,h]+1)
  perm=list(range(n))
  if n>=3:perm[1],perm[2]=2,1
  high=max(ht['NW'],ht['SE']);assert os[0]==high
  canonical=[]
  for i,j in enumerate(perm):
   assert ins[i]==os[j];turn=(outs[j]-heads[i])%4;assert turn in(1,3)
   cornerC='SE'if heads[i]==0 else'NW'
   canonical.append((i,j,ins[i],turn,cornerC))
  assert sum(1 if t==1 else -1 for _,_,_,t,_ in canonical)==n%2
  assert all(t==1 for i,j,l,t,c in canonical if l==high)
  # For a global maximum M, only high=M or high=M-1 can touch sheet M-1.
  for M in(high,high+1):
   lev=M-1;left=[a for a in canonical if a[2]==lev and a[3]==3]
   right=[a for a in canonical if a[2]==lev and a[3]==1 and ht[a[4]]==M]
   assert len(left)<=2 and (not left or os[0]==M)
   if right:
    assert len(right)==1 and not left and abs(ht['NW']-ht['SE'])==2 and os[0]==M
    assert n>=3 and {os[1],os[2]}=={M-1,M-2}
    if right[0][1]==1:assert os[1]==M-1 and os[2]==M-2
    assert n==3 or os[3]in(M-2,M-3)
   if n in(2,4)and os[-1]==lev:assert os[0]==M
  rows.append(dict(headings=heads,heights=ht,incoming_levels=ins,outgoing_levels=os,canonical=canonical))
assert len(rows)==30
names=['max_turn_leaf_stock_balance.md','canonical_turn_balance_and_stock_hole_capacity.md','penultimate_leaf_top_R0_supplier_capacity.md','nonleaf_penultimate_R0_supplier_capacity.md']
out=dict(status='PASS independent thirty-row local supplier, multiplicity, root and aggregate-turn reconstruction',notes={n:hashlib.sha256((B/n).read_bytes()).hexdigest()for n in names},rows=rows,scope='Analytic global registers separately reviewed: leaf brackets, canonical node orientation, distinct occurrence sets, top birth reservation. Not a renewal-to-node injection or finite initial fuel theorem.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(out['notes'])
