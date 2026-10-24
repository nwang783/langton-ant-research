from pathlib import Path
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_one_foreign_return_U_star_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('ports={}')[0],ns);W,M,K,L,walk,xy=[ns[k]for k in('W','M','K','L','walk','xy')]
C=json.loads((ROOT/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json').read_text())['old_source_contact_cases'];O=json.loads((ROOT/'one_foreign_return_U_star_2026-10-23/one_foreign_return_U_star.json').read_text())['rows'];old={(r['foreign'],tuple(r['foreign_pose']),r['returned_packet'],tuple(r['returned_entry_pose'])):r for r in O};rows=[];counts=Counter()
for ix,r in enumerate(C):
 if r['source_atom']!='U':continue
 f,n=r['foreign'],r['returned_atom'];fp=complex(*r['foreign_pose'][:2]);fh=r['foreign_pose'][2];p=complex(*r['returned_pose'][:2]);h=r['returned_pose'][2];age=r['source_to_foreign_C_age'];assert 0<=age<=4
 a=walk(W[f]+M);b=walk(W[n]+M);ar=walk(W[f]);assert p==fp+ar['p']*(-1j)**fh and h==(fh+ar['h'])%4
 actx={fp+q*(-1j)**fh:c for q,c in a['req'].items()};bctx={p+q*(-1j)**h:c for q,c in b['req'].items()};Ah=L&actx.keys();Bh=L&bctx.keys();entry={fp+q*(-1j)**fh for q in K};exit={p+q*(-1j)**h for q in K};assert exit<=actx.keys()
 if Ah:
  if L&entry:why='foreign core'
  elif any(not actx[q]for q in Ah):why='foreign before WHITE'
  else:
   assert age<5 and all(actx[q]and q not in entry for q in Ah);why='foreign first effect below5'
 elif not Bh:assert ix in(297,298,351,352,362,363,364);why='deleted02'
 elif n=='C':
  assert not L&exit
  phases=[]
  for q in Bh:
   local=(q-p)/((-1j)**h);assert not bctx[q]and local not in K
   phase,ch=next((i,c)for i,(z,hh,c)in enumerate(b['reads'])if z==local);assert ch=='R';phases.append(phase)
  assert min(phases)<15
  why='returned raw C before WHITE'
 else:
  comb=walk(W[f]+W[n]+M);assert comb['feasible'];cc={fp+q*(-1j)**fh:c for q,c in comb['req'].items()}
  if any(q in cc and not cc[q]for q in L):why='combined before WHITE'
  else:
   rr=old[(f,tuple(r['foreign_pose']),n,tuple(r['returned_pose']))]
   if age==1:assert rr['classification']=='necessary_foreign_clock_at_least5';why='east signed5'
   else:assert age==4 and n in'DV'and h==2 and p==(2j if n=='D'else 4j);why='south D/V signed8'
 rows.append((ix,why));counts[why]+=1
assert len(rows)==148 and counts=={'foreign core':2,'foreign before WHITE':58,'foreign first effect below5':6,'combined before WHITE':54,'east signed5':9,'south D/V signed8':6,'returned raw C before WHITE':6,'deleted02':7}
D=ROOT/'returned_U_source_all_contact_join_2026-10-23';mp=D/'manifest.json';sha=hashlib.sha256(mp.read_bytes()).hexdigest();assert sha=='13e9c2cef2592679931825f4b72559c5c2313ed91133cf1b4fc150891c4e0ba5'
for f,h in json.loads(mp.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS all148 old U-source first returned-contact exclusions','manifest_sha256':sha,'class_counts':dict(counts),'rows':rows,'analytic':['Every outgoing old U base is the actual beginning of U/UC/UCC, so the genuine-source relative clock/identity laws can be applied to its suffix without resetting original provenance or grouping historical components. Its first foreign remains the first foreign after that cut.','Foreign entry-core and before-WHITE contradictions are at the actual preforeign cut. The six first foreign effects at ages<=4 contradict the signed first-effect>=5 theorem, with actual RAW/marker ownership. Combined-return WHITE contradictions are also pulled back to foreign ENTRY; no old-eight law is carried through the foreign.','The six returned raw-C cases have original star outside foreign exit core and missed by all foreign reads. Its required WHITE contradiction is in genuine C15 RAW, not a fictitious internal marker. The nine east and six D/V south cases are exactly the already signed5/8 ancestry bounds. The remaining seven use independently signed genuine deleted02 rebirth guards.','The signed necessary contact catalogue374591ca supplies the geometric horizon and outgoing-source assignment only for a chronological FIRST new contact of the immediate returned raw atom. Exhausting all148 U labels therefore excludes an old U source for that first contact, not arbitrary later U contacts after another source is hit.'],'scope':'One first foreign followed by one immediate raw atom, after an actual U-entry complete-eight path. D/C/V old sources remain open. No returned-path simplicity, second-foreign extension or capture claim. No dependency on rejected51018788 or its separate repaired composition.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
