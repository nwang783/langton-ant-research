from pathlib import Path
import json,hashlib,ast
S=Path(__file__);D=S.parents[1]/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=D/'LL_reactivation_microblocks_are_occurrence_disjoint.md';Q=D/'positive_LL_reactivation_has_an_off_Gamma_R0_supplier.md';A=D/'check_LL_reactivation_disjoint_starts.json';assert sha(P).startswith('6145094d') and sha(Q).startswith('a6786957') and sha(D/'check_LL_reactivation_disjoint_starts.py').startswith('6c4ba3e1')
base=S.with_name('check_cyclic_LL_reactivation_independent.json');assert sha(base)=='fb74c8a00cfe84266ccbd0b30f8837d8e33eef7de1abf7093f4f56400771c817';J=json.loads(base.read_text());AJ=json.loads(A.read_text());H='NESW';V=[1j,1,-1j,-1];rows=[]
for row in J['necessary_inventories']:
 hs={complex(*ast.literal_eval(p)):w for p,w in row['histories'].items()};succ={}
 for p,w in hs.items():
  for h,v in enumerate(V):
   if p+v not in hs:continue
   outgoing=[i for i,c in enumerate(w) if (H.index(c)+(1 if i%2==0 else -1))%4==h];incoming=[i for i,c in enumerate(hs[p+v]) if H.index(c)==h];assert len(outgoing)==len(incoming)
   for i,j in zip(outgoing,incoming):succ[p,i]=(p+v,j)
 path=[(1+0j,2)]
 while path[-1]!=(1+0j,3):assert len(path)<10;path.append(succ[path[-1]])
 assert len(path)==(5 if row['kind']=='P' else 9)
 tests=[]
 for k,(p,r) in enumerate(path[1:],1):
  w=hs[p];aabb=len(w)==4 and w[0]==w[1] and w[2]==w[3] and w[0]!=w[2]
  if r!=2:why='not rank2'
  elif not aabb:why='not complete four-read AABB'
  else:assert k+1<len(path) and path[k+1][1]%2==1;why='next actual read is L, not required second R'
  tests.append({'event':[[int(p.real),int(p.imag)],r],'reason':why})
 got={'root':row['root'],'kind':row['kind'],'cleanup_events':[[[int(p.real),int(p.imag)],r]for p,r in path],'no_possible_later_postX_start':tests,'block_length':len(path)};assert got in AJ['rows'];rows.append(got)
assert len(rows)==6 and len(AJ['rows'])==6
out={'status':'PASS endpoint-inclusive LL reactivation occurrence partition, with mandatory positive-side clarification','proof':sha(P),'side_qualification':sha(Q),'script':sha(S),'signed_supplier_report':sha(base),'certificate':sha(A),'rows':rows,'analytic_review':['The complete actual ordinal successor graph, not a repaired lifetime path, independently yields all six endpoint-inclusive5/9 blocks. Every interior physical rank2 fails either complete AABB history or the required next actual R. Complete histories and physical ranks survive all full-drift identifications; different translated blocks therefore cannot overlap, since the later start would have to appear among these events. Equal starts imply the same actual event.','At a given post-LL flat X, the unique cyclic predecessor and its predecessor determine the same V/root unit. Hence distinct quotient roots do not double-charge a block, including full-drift aliases. No long-owner injection is used.','The signed critical first-track theorem places the entire block, including the final L3 departure, inside one actual LEFT-return interval. The block contains R reads, so that interval is not any four-L LL-root return. Critical LEFT intervals are occurrence-disjoint, hence the blocks, four-L roots and actual RIGHT time form disjoint reservations, yielding P>=L_RIGHT+9nP+13nN. This is not an added fuel charge or a bound on P.','Positive D.R0 is off this Gamma: its incoming Y.R2 edge is LEFT, while every Gamma R0 is RIGHT in either geometric role. R.L1 cannot be LEFT-V RIGHT-side because its successor X.R2 is LEFT. The already-signed final supplier report contains this strengthened qualification. Other curves and older stock remain unrestricted.']};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
