from pathlib import Path
import json,hashlib
S=Path(__file__);D=S.parents[1]/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();F=D/'check_prepared_nested_LL_reader_factors.json';assert sha(F).startswith('fc10d3a8')and sha(D/'check_prepared_nested_LL_reader_factors.py').startswith('f13d317a');J=json.loads(F.read_text());V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)];rows=[]
for r in J['cases']:
 B={complex(*p)for p in r['initial_black']};p=complex(*r['start'][0]);h='NESW'.index(r['start'][1]);start=p;reads={}
 for i,c in enumerate(r['word']):
  assert(c=='L')==(p in B);assert r['trace'][i]==dict(t=i,cell=xy(p),incoming='NESW'[h],turn=c,black_before=sorted(map(xy,B)));reads[p]=reads.get(p,0)+1;B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 assert(p,h)==(start,1)and p not in B and sorted(map(xy,B))==r['final_black']and[len(r['initial_black']),len(B)]==r['mass']and max(reads.values())==2;rows.append(dict(word=r['word'],mass=r['mass'],end_root_WHITE=True))
O={'status':'PASS ONLY literal prepared8/12 nested-word factors, not complete supplier inventories','script':sha(S),'certificate':sha(F),'rows':rows,'scope':'All full fields and each read replayed. Both return fullpose with rootWHITE and cannot immediately repeat. Earlier complete-WHITE R0 and optionalfutureL3 obligations are absent. No completion of the nested-reader72 interface, front or controller is claimed.'};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(sha(S.with_suffix('.json')))
