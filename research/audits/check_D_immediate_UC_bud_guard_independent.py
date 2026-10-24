from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';p=SELF.parent/'check_returned_V_source_reduction_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('mins=')[0],ns)
walk,W,M,xy,raw,I,outputs,K=[ns[x]for x in('walk','W','M','xy','raw','I','outputs','K')]
source='UC';h=-raw[source]['h']%4;e=-raw[source]['p']*(-1j)**h;assert(e,h)==(-5+0j,1)
o=1+3j;bud=e+o*(-1j)**h;assert bud==-2-1j and o in outputs[source]
assert[(i,c)for i,(q,h,c)in enumerate(raw['U']['reads'])if q==o]==[(i,c)for i,(q,h,c)in enumerate(raw['UC']['reads'])if q==o]
assert[(i,c)for i,(q,h,c)in enumerate(raw[source]['reads'])if q==o][-1][1]=='R'
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';count5={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()};names=list(raw);assert names==['D','DC','V','VC','VCC','U','UC','UCC'];queries=[]
for age in range(5):
 h=-age%4
 for j,n in enumerate(names):
  for q in sorted(I[n],key=xy):
   p=o-q*(-1j)**h;key=(6,j,*xy(p),h,*xy(o),age)
   if(int(p.real+p.imag)+h)%2:kind='sector'
   else:assert key in count5;kind='COUNT5'
   queries.append((age,n,xy(q),xy(p),h,kind,key))
assert len(queries)==115 and Counter(q[-2]for q in queries)=={'sector':63,'COUNT5':52}
cat=json.loads((D/'first_returned_atom_contact.json').read_text())['old_source_contact_cases'];rows=[]
for ix,src in[(15,'D'),(15,'DC'),(75,'DC'),(76,'DC'),(77,'DC')]:
 r=cat[ix];f=r['foreign'];p=complex(*r['foreign_pose'][:2]);h=r['foreign_pose'][2]
 if r['source_atom']=='C':p+=raw['D']['p']
 assert h==1 and r['source_to_foreign_C_age']==3;loc=(bud-p)*1j;fr=walk(W[f]);tr=walk(W[f]+W['C']+M);assert tr['feasible']and loc not in fr['req']and tr['req'][loc]is False
 first=next((i,c)for i,(q,h,c)in enumerate(tr['reads'])if q==loc);assert first==(68 if ix==15 else{'F':78,'Q':86,'B':96}[f],'R')
 rawlen=len(W[f])+len(W['C']);owned=first[0]-len(W[f])if first[0]<rawlen else first[0]-rawlen
 assert owned==(12 if ix==15 else 7)
 rows.append({'case':ix,'selected_source':src,'foreign':f,'entry':xy(p),'UC_entry_to_foreign_clock':4,'current_black_bud':xy(bud),'combined_first_R_tick0':first[0],'owner':'returned C'if ix==15 else'actual next word after returned C','owner_tick0':owned,'owner_read1':owned+1})
p=3-4j;assert(bud-p)*1j not in walk(W['F']+W['V']+M)['req']
mp=D/'D_family_immediate_UC_bud_guard_manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='4c637484047db3c54674d0da48ec8948ec07f64329f2859623c26afd4e06f7c2';mf=json.loads(mp.read_text())
for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in mf['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS narrow immediate-UC original-bud guard for D15 and C75/76/77; D30 retained','manifest_sha256':mh,'all115_preforeign_full_input_queries':queries,'counts':{'sector':63,'COUNT5':52},'five_physical_owner_rows':rows,'analytic':['The complete UC immediately preceding selected D/DC is at(-5,0,E), and its own C changes clock by1 before selected entry. D base changes clock by0, so old C1 of DC has the same clock as selected entry. Every foreign target is therefore genuine UC full-entry age4, not3.','Original U-base output(1,3) is genuinely last-R and literally untouched by its own C tail. All23 actual full input slots at every age0..4 are tested. Sector or signed COUNT5 excludes all115 alignments, including marker-only residual absorption. Overincluding age0/unfinished consumers only weakens the necessary test; no forbidden age law is used after foreign entry.','The foreign RAW never reads the protected bud. Full foreign+returnedC+actual M11 first requires R, so its initial color at foreign entry must be WHITE. This contradicts the genuine retained BLACK birth identity before any foreign or returned action, without claiming it survives such actions.','Exact owners differ: D15 is returned-C tick12/read13; C75/76/77 are actual following-word tick7/read8, not foreign RAW or returned-C RAW. The verified M11 continuation, already required by the signed catalogue, is essential for those three exclusions.','D30 F+V+M11 genuinely misses the bud and remains open. The separate old beta=(1,-1) port of generic DC remains potentially older; no fresh-origin or deleted-source inference follows.'],'scope':'Immediate UC predecessor only, preserving all genuine old source clocks and continuation ownership. No generic earlier-U/UC exclusion, all-five-target closure, returned simplicity or global capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
