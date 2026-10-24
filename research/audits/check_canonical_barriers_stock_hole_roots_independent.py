from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23'
v={'E':1+0j,'W':-1+0j,'N':1j,'S':-1j};name={z:k for k,z in v.items()};rows=[];right=[];odd=[]
for n in range(1,5):
 for hh in product('EW',repeat=n):
  h=''.join(hh);nr=Counter(h[::2]);nl=Counter(h[1::2]);a=-max(nr['E'],nr['W']);C={'NE':a+nr['W'],'SW':a+nr['E']};L={'NW':a-nl['E'],'SE':a-nl['W']};inc=Counter();out=Counter();events=[]
  for i,z in enumerate(h):
   o=name[v[z]*(-1j if i%2==0 else 1j)];inc[z]+=1;out[o]+=1
   il=C['SW'if z=='E'else'NE']-inc[z]+1;ol=C['SW'if o=='S'else'NE']-out[o]+1
   events.append((z,o,il,ol))
  for j in range(min(L.values())+1,max(C.values())+1):
   pairs=[]
   for i,e in enumerate(events):
    if e[2]!=j:continue
    k=3-i if n>=3 and i in(1,2)else i;f=events[k];assert f[3]==j
    assert v[f[1]]in(v[e[0]]*1j,v[e[0]]*(-1j));turn='R'if v[f[1]]==v[e[0]]*(-1j)else'L'
    pairs.append((i,k,turn))
   if not pairs:continue
   lo=max(L.values())<=j-2;hi=min(C.values())>=j+1
   if lo:
    assert all(z[2]=='R'for z in pairs)
    if len(pairs)==2:assert n==4 and set(C.values())=={j}and set(L.values())=={j-2}
   if hi:
    assert all(z[2]=='L'for z in pairs)
    if len(pairs)==2:assert n==4 and set(C.values())=={j+1}and set(L.values())=={j-1}
   rows.append({'word':h,'j':j,'C':C,'L':L,'pairs':pairs,'lowL':lo,'highC':hi})
  if n>=3 and h[0]==h[2]:
   rs=[r for r in rows if r['word']==h and r['j']==-1];assert len(rs)==1 and len(rs[0]['pairs'])==1 and rs[0]['pairs'][0][2]=='R'
   assert sorted(C.values())==[-2,0]and min(L.values())<=-3 and max(L.values())<=-2
   right.append({'word':h,'C':C,'L':L})
  if n%2:
   if n==1:kind='singleton';assert set(L.values())=={-1}
   elif h[0]!=h[2]:kind='oppositeR';assert sorted(L.values())==[-2,-1]
   else:kind='sameR';assert sorted(L.values())==[-3,-2]
   odd.append({'word':h,'kind':kind,'L':L,'can_root_low':min(L.values())<=-3})
assert len(rows)==78 and sum(z['lowL']for z in rows)==20 and sum(z['highC']for z in rows)==20
assert len(right)==12 and len(odd)==10 and all(z['kind']=='sameR'for z in odd if z['can_root_low'])
author=json.loads((D/'canonical_sheet_two_level_contact_barriers.json').read_text())
assert [(z['word'],z['j'],z['C'],z['L'],z['lowL'],z['highC'])for z in rows]==[(z['headings'],z['j'],z['C'],z['L'],z['L_contact_preserved'],z['C_contact_preserved'])for z in author['checks']]
for r,s in zip(rows,author['checks']):assert r['pairs']==[(z['in_rank'],z['out_rank'],z['turn'])for z in s['pairs']]
files=['canonical_sheet_two_level_contact_barriers.md','canonical_sheet_two_level_contact_barriers.py','canonical_sheet_two_level_contact_barriers.json','contractible_max_RIGHT_stock_holes_require_odd_roots.md','prepared_plateau_black_corner_alternative_and_reverse_output.md','penultimate_max_adjacent_contour_orientation.md','chronological_stream_sheet_exchange.md','triple_use_current_pairs_top_same_R_outputs.md']
hashes={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files}
out={'status':'PASS canonical two-level barriers and contractible max-RIGHT odd-root capacity','source_hashes':hashes,'all78_local_sheet_rows':rows,'all12_max_RIGHT_middle_rows':right,'all10_top_odd_histories':odd,'analytic':['Every physical sheet port is determined by h(L)<j<=h(C). Fresh complete30-history/78-sheet reconstruction uses the actual L1/R2 swapped successor, not just edge support. If both low L<=j-2, a two-port arc turns RIGHT around the sole highC; the sole possible four-port equality has C=j,L=j-2 and twoRIGHT arcs. Both L sectors connect in the complementary central patch. Dually both C>=j+1 are connected across a twoLEFT four-port equality or around the sole lowL arc. These local face-center connections embed the entire contact graphs in the complement of all sheet-j circles.','For j=M-1, each global-max C component stays on one side of any canonical circle and contains its signed essential first-L curve. A finite Jordan disk cannot contain it. At a max-RIGHT corner the maxC lies on the RIGHT side, so a contractible such circle must have its bounded disk LEFT (CCW). Both adjacent L sectors are on that LEFT side; at least one has height<=M-3 by the fresh full same-R inventory.','The L<=M-3 contact barrier keeps the low face component inside the bounded disk. A minimum plateau Q among all inside L faces is locally minimal in the full plane: any adjacent lower face would be in the same retained sublevel contact graph and therefore also inside. Q is finite physically. It cannot meet or become adjacent to a nonzero full-drift translate of itself at the same level, since equal connected components would imply an infinite translated physical set. Thus quotient projection cannot manufacture essential winding or an outside lower neighbor.','Apply the signed prepared reverse-plateau alternative with WHITE collar exactly when Q has no odd-output incident cell. It then gives an essential reverse birth curve in Q, impossible in a bounded physical disk. No inequality m>=c_left is silently assumed: the stronger no-black essential-curve alternative in that signed theorem applies at every height, with m<c_left as a consequence if no root. Hence this physically finite minimum must have an odd-output root.','All lifted sheet circles are disjoint. Nested disks are impossible: the inner max-RIGHT corner connects its maxC face center to its RIGHT sector without crossing another sheet contour, putting a maxC face inside the outer disk. Unique max-RIGHT local arc (otherC=M-2) prevents a second arc hiding in that corner connection. Thus all physical disks and all nonzero full-drift translates are disjoint. A root cell cannot serve two disks: if its two low L sectors do, the same retained contact joins them in the complement of all circles, contradiction. Full-quotient root aliasing is handled by translating the associated disk.','Fresh odd-history levels show top singleton L=-1,-1 and top opposite-R3 L=-2,-1 relativeM, too high to root Q. A top root must be same-R3 at low L=M-3 and is a G3(M) endpoint. The signed pairing preserves its ENTIRE connected L plateau, so the partner endpoint and finite path stay associated with this same Q. Distinct disks cannot spend the same path. Select a non-top root if available; otherwise assign its top G3 path. This yields h<=Nodd-Ntop+J=Nodd-Nshallow-J without adding endpoints again to other overlapping budgets.'],'scope':'Complete WHITE cap4 actual full nonzero-drift translating front, noK1/leftmost/leaf premise. H counts distinct contractible penultimate nodes with max-RIGHT corner. At zero odd output this family is empty even at nonleaf degree. Essential nodes, other contractible root geometries, graph-rank bounds and initial-fuel/capture claims remain outside scope.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(hashes)
