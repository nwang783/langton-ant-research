from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_one_foreign_return_U_star_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('ports={}')[0],ns)
W,M,K,L,walk,xy,raw=[ns[k]for k in('W','M','K','L','walk','xy','raw')]
def output(a):
 B={q for q,c in a['req'].items()if c}
 for q,h,ch in a['reads']:B.symmetric_difference_update({q})
 return B-{a['p']+q*(-1j)**a['h']for q in K}
AR={n:walk(W[n])for n in'DCVU'};AC={n:walk(W[n]+M)for n in'DCVU'};AO={n:output(AR[n])for n in'DCVU'}
g=2j
assert[(i,ch)for i,(q,h,ch)in enumerate(AR['U']['reads'])if q==g]==[(12,'L'),(16,'R'),(20,'L')]
for n in('U','UC','UCC'):
 a=raw[n];assert[(i,ch)for i,(q,h,ch)in enumerate(a['reads'])if q==g][-1]==(20,'L');assert g not in output(a)and g not in{a['p']+k*(-1j)**a['h']for k in K}
for n in'DCVU':assert all(q.imag>=0 and q.real+q.imag>=0 for q in AO[n])
roles=[];sur=[]
for h in(2,1):
 for n in'DCVU':
  for o in AO[n]:
   p=g-o*(-1j)**h;ep=p+AR[n]['p']*(-1j)**h
   why='sector'if(int(p.real+p.imag)+h)%2 else'held star'if L&{p+z*(-1j)**h for z in AC[n]['req']}else'late C4'if h==1 and n=='C'else'survivor'
   roles.append((h,n,xy(o),xy(p),xy(ep),why))
   if why=='survivor':sur.append((n,p,ep))
assert len(roles)==38 and len(sur)==3 and all(r[-1]in('sector','held star')for r in roles if r[0]==2)
assert set(sur)=={('V',-1+4j,2+3j),('U',-2+3j,2+3j),('U',-1+4j,3+4j)}
C=json.loads((ROOT/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json').read_text())['old_source_contact_cases'];miss=[];cases=[];ob=[]
for ix,r in enumerate(C):
 if r['source_atom']!='U':continue
 f,n=r['foreign'],r['returned_atom'];fp=complex(*r['foreign_pose'][:2]);fh=r['foreign_pose'][2];p=complex(*r['returned_pose'][:2]);h=r['returned_pose'][2]
 fc=walk(W[f]+M);rc=AC[n]
 if L&{fp+q*(-1j)**fh for q in fc['req']}or L&{p+q*(-1j)**h for q in rc['req']}:continue
 miss.append(ix);assert r['source_to_foreign_C_age']==3 and(fh,h)==(1,3)
 fr=walk(W[f]);assert fp+fr['p']*(-1j)**fh==p
 comb=walk(W[f]+W[n]+M);assert comb['feasible'];loc=(g-fp)/((-1j)**fh);assert comb['req'][loc]is True and loc not in K
 first=next((i,ch)for i,(q,hh,ch)in enumerate(comb['reads'])if q==loc)
 if loc in fc['req']:
  assert f in'QB'and loc not in fr['req']and first==(len(W[f])+1,'L');owner='returned RAW1, foreign marker-only input'
 else:assert n=='U'and first==(len(W[f])+13,'L');owner='returned U RAW13'
 cases.append((ix,f,xy(fp),n,xy(p),first,owner))
 last='U'if f=='B'else'VU'
 for b,bp,ep in sur:
  dx,down=int(fp.real-ep.real),int(ep.imag-fp.imag);sol=[]
  for v in range(max(down+1,0)):
   d=down-v;rem=dx-d-3*v
   if rem>=0 and rem%4==0:sol.append((d,v,rem//4))
  assert ep!=fp and all(not any(c and n in last for n,c in zip('DVU',t))for t in sol)
  ob.append((ix,b,xy(bp),sol))
assert miss==[297,298,351,352,362,363,364]and len(ob)==21
D=ROOT/'returned_U_source_deleted_guard_2026-10-23';mp=D/'manifest.json';sha=hashlib.sha256(mp.read_bytes()).hexdigest();assert sha=='992a5459549b09c62695998d5cbf5b49f1773088a43c9232c9f789ab7c920837'
for f,h in json.loads(mp.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS seven genuine source-deleted(0,2) returned-contact exclusions','manifest_sha256':sha,'atomic_output_roles':38,'role_split':dict(Counter(r[-1]for r in roles)),'seven_configurations':cases,'unbounded_endpoint_obligations':ob,'analytic':['Creating U actually deletes g=(0,2) at L20 after L12/R16; both actual C tails preserve that deletion and no full residual or exit-core g remains. Every combined foreign-plus-return before-mask needs g black outside foreign entry core. Thus an old residual rebirth is genuinely required before the foreign; no permanence of fine-time WHITE is asserted.','The first four guards are foreign Q/B marker-only inputs physically read by returned RAW1. The last three are returned U lower-q RAW13 and the foreign complete context misses g. Combined actual masks account for all foreign toggles and do not transfer a marker into the foreign RAW.','N0 output y>=4 and W1 H>=5 exclude early origins. All38 S/E atomic output alignments leave no S origin and only3 E3 plain bases; E C4 and positive full tails cannot finish before foreign C3. Source star is held only in the old-eight prefix.','Every arbitrary zero-C E continuation satisfies dx=d+3v+4u, down=d+v. All21 exact origin-to-target equations have no allowable last V/U before F/Q or U before B. There is no hidden zero-length exception. Hence all7 configurations are impossible even without a chronological first-contact or returned-simplicity premise.'],'scope':'Only these seven exact first-foreign/returned configurations after genuine U-family ancestry. No postforeign age/permanence theorem or all-return closure is inferred.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
