from pathlib import Path
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];ns={'__file__':str(SELF.parent/'check_serial_bridge_archive_independent.py')};exec(Path(ns['__file__']).read_text().split('# Fixed local masks')[0],ns);graph,component,wvertex=[ns[k]for k in('graph','component','wvertex')]
D=R/'renewal_input_placement_2026-10-23';a=json.loads((D/'forced_input_cycle_templates.json').read_text());dirs=[1j,1,-1j,-1]
def trace(w,p,h):
 out=[]
 for c in w:out.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
 return out,p,h
def offset(q,p,d):
 x,y=int((q-p).real),int((q-p).imag);dx,dy=int(d.real),int(d.imag)
 if x*dy!=y*dx:return None
 if x%dx:return None
 z=x//dx;return z if y==z*dy else None
def occ(q,tr,d):
 out=[]
 for i,(p,h,c)in enumerate(tr):
  z=offset(q,p,d)
  if z is not None:out.append({'copy_offset':z,'slot':i,'turn':c,'relative_time':z*len(tr)+i})
 return sorted(out,key=lambda x:x['relative_time'])
counts=Counter();reports=[]
for P,fn,p,h in[(1564,'prepared_travelling_wave_certificate.json',-6-6j,0),(4352,'second_prepared_wave_certificate.json',-2+3j,3)]:
 w=json.loads((R/'nonlinear_global_budget_2026-10-23'/fn).read_text())['word'];assert len(w)==P;tr,end,eh=trace(w,p,h);assert eh==h;d=end-p;assert d=={1564:14+14j,4352:26+26j}[P];z=a[str(P)];assert hashlib.sha256(w.encode()).hexdigest()==z['word_sha256'];k=int(wvertex(p,h).real+wvertex(p,h).imag)%4
 core=z['core'];startup=z['startup_extra']+z['startup_overrides'];templates=core+startup;fringes=Counter();sizes=Counter()
 for c in templates:
  cells=[complex(*q)for q in c['cycle_cells']];assert len(cells)==len(set(cells))==c['edge_count'];assert cells[0]==complex(*c['target_cell'])==tr[c['slot']][0];g=graph(set(cells),k);assert all(len(v)==2 for v in g.values());assert component(set(cells),k,next(iter(g)))[1]==set(cells)
  oo=occ(cells[0],tr,d)
  if c['first_copy_only']:oo=[q for q in oo if q['copy_offset']>=0]
  assert(oo[0]['relative_time'],oo[0]['turn'])==(c['slot'],'L');offsets=[]
  for q,cert in zip(cells,c['black_edge_read_certificates']):
   oo=occ(q,tr,d)
   if c['first_copy_only']:oo=[v for v in oo if v['copy_offset']>=0]
   assert oo==cert['complete_occurrences'];before=[v for v in oo if v['relative_time']<c['slot']];wit=before[-1]if before else oo[0];assert wit==cert['witness'];assert cert['mode']==('last_prior_R'if before else'first_future_L')and wit['turn']==('R'if before else'L');offsets.append(wit['copy_offset'])
  l=0 if c['first_copy_only']else max(0,-min(offsets));r=max(0,max(offsets));assert(l,r)==(c['left_fringe'],c['right_fringe']);assert not c['first_copy_only']or(l,r)==(0,0)
  if not c['first_copy_only']:fringes[l,r]+=1
  sizes[len(cells)]+=1;counts['cycles']+=1;counts['cycle_edge_occurrences']+=len(cells)
 for i,c in enumerate(core):
  for b in core[:i]:assert offset(complex(*c['target_cell']),complex(*b['target_cell']),d)is None
 assert len({tuple(c['target_cell'])for c in startup})==len(startup)
 for c in startup:
  for b in core:
   off=offset(complex(*c['target_cell']),complex(*b['target_cell']),d)
   assert off is None or off<b['left_fringe']
 assert fringes==({(0,0):40}if P==1564 else{(0,0):96,(0,1):1,(1,0):5})
 assert(len(z['startup_extra']),len(z['startup_overrides']))==((0,0)if P==1564 else(21,4))
 tests=[]
 for N in(1,2,4):
  full,_,_=trace(w*N,p,h);last={};seed=set()
  for q,hh,c in full:
   if q in last:assert c!=last[q]
   elif c=='L':seed.add(q)
   last[q]=c
  B=set(seed);birth={q:None for q in B};obligations={}
  for c in templates:
   ks=[0]if c['first_copy_only']else range(c['left_fringe'],N-c['right_fringe'])
   for j in ks:
    tick=j*P+c['slot'];assert tick not in obligations;obligations[tick]=(j,c)
  assert len(obligations)==(40*N if P==1564 else 102*N+19)
  for tick,(q,hh,ch)in enumerate(full):
   assert(q in B)==(ch=='L')
   if tick in obligations:
    j,c=obligations[tick];assert ch=='L'and birth[q]is None;assert{complex(*v)+j*d for v in c['cycle_cells']}<=B;counts['literal_certified_deletions']+=1
   if ch=='R':birth[q]=tick
   else:del birth[q]
   B.symmetric_difference_update({q});counts['literal_reads']+=1
  tests.append({'N':N,'minimal_entry_mass':len(seed),'certified_entry_black_w_erasures':len(obligations)})
 reports.append({'word':P,'fringes':[(l,r,n)for(l,r),n in fringes.items()],'cycle_lengths':dict(sizes),'controls':tests})
assert(counts['cycles'],counts['cycle_edge_occurrences'])==(167,992)
# Every standard L has its immediately previous actual R at copy offset0/-1.
s=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());w=s['word'];tr,d,hh=trace(w,0j,s['heading']);assert hh==s['heading'];sr=json.loads((D/'standard_self_fed_lifetime_certificate.json').read_text());standard=[];first={}
for i,(q,h,c)in enumerate(tr):
 first.setdefault(q,c)
 if c!='L':continue
 oo=occ(q,tr,d);prior=[x for x in oo if x['relative_time']<i];r=prior[-1];assert r['turn']=='R'and r['copy_offset']in(-1,0)and 0<i-r['relative_time']<=116
 standard.append({'L_slot':i,'cell':[int(q.real),int(q.imag)],'prior_R':r,'age':i-r['relative_time'],'all_occurrences':oo})
assert standard==sr['all_L_slots'];assert len(standard)==46 and max(v['age']for v in standard)==116 and sum(c=='L'for c in first.values())==13
proof=D/'PROOF.md';ph=hashlib.sha256(proof.read_bytes()).hexdigest();assert ph=='5f6eb7f5b57181fdf8de9bd2ddf3949b230801f2f20a443d385fd5c9eadce62e';source=R/'causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json';sh=hashlib.sha256(source.read_bytes()).hexdigest();assert sh=='90fcf1a66046418c38d07f7e935ea80cf873751aefae69a4b07af89ba3bd8399'
out={'status':'PASS all-N forced exceptional input-lifetime placement, standard bounded-age self-feeding and184-family unbounded lifetime-age countercontrol','proof_sha256':ph,'certificate_sha256':hashlib.sha256((D/'forced_input_cycle_templates.json').read_bytes()).hexdigest(),'standard_certificate_sha256':hashlib.sha256((D/'standard_self_fed_lifetime_certificate.json').read_bytes()).hexdigest(),'184_source_manifest_sha256':sh,'counts':dict(counts),'waves':reports,'standard_L_slots':46,'standard_max_R_to_L_age':116,'analytic':['Any actual literal finite word forces the complete entry board on READ exactly; all extra black cells lie outside READ and persist unchanged at every cut. A simple black cycle in the forced minimal field persists on adding those unread components, so its target L is genuinely w-nonbridge in every full realization. This monotonicity does not assert bridges survive extras.','Exact one-copy occurrence lists exhaust every possible read of a translated cycle cell. An eligible last-before R establishes its current black lifetime; when no earlier read exists, an eligible first-future L forces entry black. First-copy templates omit only negative-copy reads. Lower/upper copy inequalities retain every chosen witness, with no temporal cutoff.','Every target is its first eligible L, hence one entry-black lifetime. Core targets occupy distinct drift orbits; each startup overlap has offset strictly below its core first-copy eligibility. Thus target lifetimes are distinct, even if witness cycles overlap. The exact counts are40N and96N+6(N-1)+25=102N+19 for every N>=1.','All46 standard L slots have an immediately preceding R witness at copy offset0/-1 and age<=116. Thus after first104 updates every consumed lifetime is R-born inside the interval. Only13 first-period first-L cells can be entry-black, independent of unread archives.','For the signed184 original family and N>=5, the last five1564 copies consume200 distinct certified entry-black lifetimes at w erasures. At most184 can be unchanged original starting lifetimes, leaving at least16 genuinely R-born before wave entry. Each such death is at least1564(N-5) after entry and birth strictly earlier, so at least one exceptional R-to-L age is>=1564(N-5)+1. Original mass alone cannot bound exceptional consumed-lifetime age, even on this signed bi-standard family.','No equality for allN, classification of other words, bounded global renewal age, original-mass upper input budget or finite-seed noncapture follows. The large full-preparation controls are corroboration and were not duplicated.'],'scope':'The three supplied literal words and exact original184-family application. No generic nonstandard-word or capture theorem.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)
