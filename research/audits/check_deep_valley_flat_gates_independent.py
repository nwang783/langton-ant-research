from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'K1_pipeline_detours_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=P/'deep_rootfree_valley_extra_retreat_requires_four_flat_gates.md';assert sha(note)=='26c66e042020dab168357be0b09206d884d8a662d2719840f82f6f08c5466dd9';ref=json.loads((P/'deep_rootfree_no_triple_exit_gate_inventory.json').read_text());basefile=P/'canonical_max_face_child_ports.json';assert sha(basefile)==ref['source_sha256']=='f6e8ee4f04c2a94aafb3783472885773c1db989c1a888d02befaef87a698ecdc';base=json.loads(basefile.read_text())['rows'];assert len(base)==110
ns={'__file__':str(S.parent/'check_triple_staircase_extrema_independent.py')};src=(S.parent/'check_triple_staircase_extrema_independent.py').read_text();exec(src[:src.index('A=words(')],ns);levels=ns['levels'];V=ns['V'];out=ns['out'];letters='NESW';named=ns['named']
local=[]
for axis in(0,1):
 Lfaces=('NE','SW')if axis==0 else('NW','SE')
 for n in(2,4):
  for w in product((axis,axis+2),repeat=n):
   z=levels(w,Lfaces[0]);triple=[]
   for h in range(4):
    ni=sum(v==(h+2)%4 for v in w);no=sum(out(v,j)==h for j,v in enumerate(w));flow=no+ni
    if flow!=3:continue
    v=V[h];adj={v/2-1j*v/2,v/2+1j*v/2};lf=next(a for a in Lfaces if named[a]in adj);triple.append((h,lf))
   if triple:
    candidates=[a for a in Lfaces if z[a]<=z[next(b for b in Lfaces if b!=a)]]
    assert all(any(lf==a for h,lf in triple)for a in candidates)
    local.append({'headings':''.join(letters[h]for h in w),'L_levels':{a:z[a]for a in Lfaces},'each_possible_minimum_sector_touches_a_triple_port':candidates,'triple_ports':triple})
coords={'A':1+0j,'Z':0j,'Y':1j,'B':1+1j};at={q:v for v,q in coords.items()};profiles=[];exits=[]
for row in base:
 hs={v:tuple(letters.index(h)for h in w)for v,w in row['headings'].items()}
 if any(len(w)%2 for w in hs.values()):continue
 if any(3 in list(Counter(w).values())+list(Counter(out(h,j)for j,h in enumerate(w)).values())for w in hs.values()):continue
 assert row['headings']['A']=='NNSS';profiles.append(row);su={}
 for v,w in hs.items():
  for h in range(4):
   q=coords[v]+V[h]
   if q not in at:continue
   vv=at[q];ss=[j for j,a in enumerate(w)if out(a,j)==h];tt=[j for j,a in enumerate(hs[vv])if a==h];assert len(ss)==len(tt)
   for j,jj in zip(ss,tt):su[v,j]=(vv,jj)
 for child in row['potential_children']:
  p=(child,0);route=[p]
  while p!=('A',2)and p in su:
   p=su[p];assert p not in route;route.append(p)
  forced=p==('A',2);flow4=any(4 in list(Counter(w).values())+list(Counter(out(h,j)for j,h in enumerate(w)).values())for w in hs.values())
  if forced:assert 1<=len(route)-1<=3 and all(rank==0 for v,rank in route[:-1])
  rec={'headings':row['headings'],'exit':child,'forced_adjacent':forced,'actual_boundary_prefix':[list(q)for q in route],'terminal':list(p),'has_flow4':flow4};exits.append(rec)
assert profiles==ref['rows']and exits==ref['exits']and len(profiles)==17 and len(exits)==16 and sum(z['forced_adjacent']for z in exits)==12
assert sum(z['has_flow4']for z in exits)==1 and all(z['forced_adjacent']for z in exits if z['has_flow4'])
opens=[z for z in exits if not z['forced_adjacent']];assert len(opens)==4
# Independently preserve the disconnected continuation after each genuine wait.
resume=[]
for row in opens:
 hs={v:tuple(letters.index(h)for h in w)for v,w in row['headings'].items()};su={}
 for v,w in hs.items():
  for h in range(4):
   q=coords[v]+V[h]
   if q not in at:continue
   vv=at[q];ss=[j for j,a in enumerate(w)if out(a,j)==h];tt=[j for j,a in enumerate(hs[vv])if a==h]
   assert len(ss)==len(tt);su.update({(v,j):(vv,jj)for j,jj in zip(ss,tt)})
 if row['headings']['B']=='WEEW':assert su['B',2]==('A',2);resume.append({'gate':row['headings'],'resume_B_R2_to_A_R2':True})
 else:
  assert su['B',1]==('A',2)and su['B',2]==('A',3)
  if row['headings']['Y']=='SNNS':assert su['Y',2]==('B',2)
  resume.append({'gate':row['headings'],'A_R2_supplied_by_B_L1':True,'B_R2_lands_A_L3':True})
outp={'status':'PASS prepared deep root-free valley17 profiles/16 exits, four necessary flat gates and extra-retreat identity; no span bound','note':sha(note),'signed110_source':sha(basefile),'all_local_even_triple_port_lower_sector_checks':local,'profiles':17,'exit_pairs':16,'forced_adjacent_R0_to_R2':12,'four_open_flat_gates':opens,'actual_wait_continuations':resume,'analytic_review':[
'Signed depth split gives noG3 incident to deep root-free Q. Independently every possible locally minimal L sector of a WHITE-even cap4 corner with any triple port touches at least one such port. When the two L heights tie they belong to the same diagonal component and each touches a triple port; no false unique-lower assertion is used. Hence noG3 incident toQ excludes every triple port at its corner. Reverse read conjugacy preserves port multiplicities and WHITE-evenness on Q only; BLACK reverse cells offQ remain unrestricted.',
'A selected reverse first-L entry has complete even prefixNNS; noG3 excludesNNSN, leavingNNSS and RIGHTL3/state0. This is NOT K1 and the old constant-zero K1 exclusion is not imported. The signed110 local canonical face inventory applies only to the four Q corners, not to the whole reverse board.',
'Fresh filtered110 source gives17 profiles,12 with possible cycleexit and16 profile/exits. All within-face directed ports were independently paired by actual occurrence ordinal. Twelve routes go from selectedexitR0 to entryA.R2 in1..3 consecutive physical moves, every intermediate rank0. Those other corners cannot be selected contacts: each would contribute a third selected incidence at this same physical face in the embedded birth curve. This uses physical face incidence, not a guessed lower bound on full drift.',
'The unique flow4 profile NNSS/WWEE/NSNS/EEEE has the forced3-step R0 corridor. Thus flow4 alone supplies no extra retreat. The four remaining flat gates retain the exact B.L1-toR2 or Y.L1-toR2 waits, and two land at entryA.L3 instead ofR2; in those A.R2 is supplied separately byB.L1. No missing L supplier is dropped.',
'From the signed prepared cursor retreat mapE(j)<j and averageK_L, sum(d_j-1)=(K_L-1)*ell. Forced faces have d=1. Hence all extra retreat is carried by the unforced four-gate occurrences, at least one on each selected cycle whenK_L>=2. No bound on any d_j, wait, repeated stock, same-component transfer or period is supplied. This is a necessary gate interface, not exterior realization, output payment, fuel or capture.'
]};S.with_suffix('.json').write_text(json.dumps(outp,indent=2)+'\n');print(outp['status'])
