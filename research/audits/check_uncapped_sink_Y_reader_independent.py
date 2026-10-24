from pathlib import Path
from itertools import combinations,product
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'local_sink_Y_source_uncapped_reader_requires_higher_C.md';assert sha(P)=='17e8d2fd81c4bcebe8d167717e4b44d55a684d96e6a528ba2eee5b9e405c0be5'
J=json.loads((D/'check_local_sink_Y_source_uncapped_reader.json').read_text());H='NESW';vec=dict(N=1j,E=1,S=-1j,W=-1);out=lambda w:[H[(H.index(c)+(1 if r%2==0 else-1))%4]for r,c in enumerate(w)];pos=dict(F=0j,L0=1j,Q=-1+1j,L2=-1+0j);inv={v:k for k,v in pos.items()};rows={(z['L0'],z['L2'],z['Q']):z for z in J['all_derived_reader_rows']};seen=set();survivors=[];rejected=0
for I,J0 in product((3,4),repeat=2):
 l0='E'*J0;l2='WEW'if I==3 else'WEWE'
 # Generate from counts of even and odd N positions, independently deriving n bound.
 for n in range(1,2*(I+J0)+2):
  ell=n//2;num=I+J0-ell
  if num%2:continue
  rn=num//2;ln=I-rn
  if not(0<=rn<=(n+1)//2 and 0<=ln<=ell):continue
  for even in combinations(range(0,n,2),rn):
   for odd in combinations(range(1,n,2),ln):
    Ns=set(even)|set(odd);q=''.join('N'if k in Ns else'S'for k in range(n));key=(l0,l2,q);seen.add(key);r=rows[key];assert q.count('N')==I and out(q).count('E')==J0;rs=(n+1)//2-rn;assert(r['R_N'],r['R_S'],r['opposite_C_raise'])==(rn,rs,rs-rn)
    hs=dict(F='NSSN',L0=l0,Q=q,L2=l2);succ={};edge=set()
    for a,w in hs.items():
     for d in H:
      z=pos[a]+vec[d]
      if z not in inv:continue
      b=inv[z];depart=[k for k,c in enumerate(out(w))if c==d];arrive=[k for k,c in enumerate(hs[b])if c==d];assert len(depart)==len(arrive)
      for ord0,(k,l)in enumerate(zip(depart,arrive)):succ[a,k]=(b,l);edge.add((a,k,b,l,d,ord0+1))
    assert edge==set(map(tuple,r['all_internal_edges']))
    failed=False
    for a,w in hs.items():
     for k in range(len(w)):
      at=(a,k);path=[at]
      while at in succ:
       at=succ[at]
       if at[0]==a:
        failed|=at[1]!=k+1;break
       if at in path:failed=True;break
       path.append(at)
    if 'collision_route'in r:
     path=list(map(tuple,r['collision_route']));assert all(succ[a]==b for a,b in zip(path,path[1:]));assert all(z[0]!=path[0][0]for z in path[1:-1]);assert(path[-1][0]==path[0][0]and path[-1][1]!=path[0][1]+1)or path[-1]in path[:-1];assert failed;rejected+=1
    else:
     assert not failed
     # C_NW-L_SW=Wout, C_SE-L_SW=Nin; no cap or first-R maximum used.
     jump=out(q).count('W')-q.count('N');assert jump==rs-rn>=3;assert out('NSSN').count('W')-'NSSN'.count('N')==0
     survivors.append(dict(L0=l0,L2=l2,Q=q,C_raise=jump))
assert seen==set(rows)and len(seen)==1014 and rejected==1010;assert {z['Q']for z in survivors}=={'SSSSSSNNSN','SSSSSSNNSNS','SSSSSSNNSNSN','SSSSSSNNSNSNS'};assert sorted(z['C_raise']for z in survivors)==[3,4,4,5]
obj=dict(status='PASS derived uncapped local reader domain leaves only four higher-C necessary shields',proof=sha(P),script=sha(S),author_checker=sha(D/'check_local_sink_Y_source_uncapped_reader.py'),author_certificate=sha(D/'check_local_sink_Y_source_uncapped_reader.json'),derived_domain=1014,literal_rank_collisions=1010,necessary_controls=survivors,analytic_review=['NinI=RN+LN and EoutJ=RN+LS give I+J=2RN+floor(n/2), hence n<=2(I+J)+1<=17 without an imposed visit cap. Independent even/odd N-position generation exhausts the same1014 complete histories. L0/L2 short domains were already uncapped count-derived.','All physical internal edge counts and actual ordinal successors are independently reconstructed; every one of1010 recorded collision paths is an actual contiguous read sequence that skips/backtracks the first return rank or closes a positive finite actual event cycle. The four remaining profiles have no such local collision, not an asserted complete realization.','At Q, shared C_SE minus L_SW equals Nin, while opposite C_NW minus the SAME L_SW equals Wout. Therefore opposite-minus-shared=RS-RN=3/4/4/5, with the physical square face shared with F. F RN=RS makes both F incident C equalc. No all-cap firstR maximization theorem or zero-port omission is used.','Thus GLOBAL-C-maximal c excludes this exact rail even with unbounded auxiliary multiplicity/old stock. At nonmaximal height, four ten-to-thirteen-read shields remain necessary local interfaces, not board factors/fronts. Whole-boundary scope still needs its independently stated geometric assumptions.']);S.with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(obj['status']);print(sha(S.with_suffix('.json')))
