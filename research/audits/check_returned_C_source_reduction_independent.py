from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];ns={'__file__':str(SELF.parent/'check_one_foreign_return_U_star_independent.py')};exec(Path(ns['__file__']).read_text().split('ports={}')[0],ns)
W,M,K,L,inv,raw,walk,xy,center,meet=[ns[k]for k in('W','M','K','L','inv','raw','walk','xy','center','meet')]
D=R/'seven_word_spatial_return_2026-10-23';cat=json.loads((D/'first_returned_atom_contact.json').read_text())['old_source_contact_cases'];a=json.loads((D/'returned_C_source_reduction.json').read_text());names=list(inv)
def pose(z,p,h):return p+z*(-1j)**h
def local(z,pp):return(z-complex(*pp[:2]))*1j**pp[2]
def counts(delta):
 x,y=xy(delta);tot=-y;out=[]
 for v in range(max(0,tot+1)):
  d=tot-v;r=x-d-3*v
  if r>=0 and not r%4:out.append((d,v,r//4))
 return out
def orders(d,v,u):
 if not d+v+u:return ['']
 return[b+s for b,c in [('D',d),('V',v),('U',u)]if c for s in orders(d-(b=='D'),v-(b=='V'),u-(b=='U'))]
def goodlast(f):return'VU'if f!='B'else'U'
# Independently reconstruct full fresh output masks and all seven containing C roles.
outputs={};roles=[]
for n in names:
 rr=raw[n];last={q:ch for q,h,ch in rr['reads']};ek={pose(z,rr['p'],rr['h'])for z in K};outputs[n]={q for q,ch in last.items()if ch=='R'}-ek
 p=0j;h=0;cc=0
 for b in n:
  if b=='C':
   fq=pose(-1-1j,p,h);assert last[fq]=='L'and fq not in outputs[n]and fq not in ek
   roles.append((n,cc+1,xy(p),h,xy(fq)));cc+=1
  z=walk(W[b]);p+=z['p']*(-1j)**h;h=(h+z['h'])%4
assert len(roles)==7
refG=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
for g in refG:
 if g['name']in outputs:assert outputs[g['name']]=={complex(*x)for x in g['outputs']}
classify=Counter();age1words=[];repair=[];res=[]
for i,r in enumerate(cat):
 if r['source_atom']!='C':continue
 f,t,n=r['foreign'],r['returned_atom'],r['source_to_foreign_C_age'];p=r['foreign_pose'];co=walk(W[f]+W[t]+M);assert co['feasible'];guards=([2,1-1j]if n<=2 else[])+([1+2j]if n<=3 else[])
 if any(local(q,p)in K or co['req'].get(local(q,p))is False for q in guards):classify['guard']+=1;continue
 if n==1:
  words=[]
  for cv in counts(-(complex(*p[:2])-1j)):
   for s in orders(*cv):
    if s and s[-1]in goodlast(f):
     lit=walk(W['C']+''.join(W[b]for b in s)+W[f]+W[t]+M);assert not lit['feasible'];words.append((s,lit['i'],xy(lit['q']),lit['first']))
  age1words.append((i,words));classify['age1']+=1;continue
 assert n==3
 if t=='C':res.append((i,f,p,r['returned_pose']));classify['residue']+=1;continue
 q=-1-1j;z=local(q,p);fc=walk(W[f]+M);assert z not in fc['req']and co['req'][z]and z not in K and local(q,r['returned_pose'])not in K
 repair.append((i,r));classify['repair']+=1
assert classify=={'guard':24,'age1':15,'repair':9,'residue':3};assert sum(len(w)for i,w in age1words)==22 and sum(not w for i,w in age1words)==2
# Last current q producer's entry clocks1/2/3, never a postforeign age bound.
q=-1-1j;c1=c2=c3=0;tworem=[];helpers=[]
for n,os in outputs.items():
 for z in os:
  p=q-z*1j;assert not(p.real<=0 and p.imag>=1);c1+=1
  p=q+z;c2+=1
  if n.count('C')>1 or(int(p.real+p.imag)+2)%2 or p.real>-1:continue
  assert z==0 and p==-1-1j and n in('V','VC','U','UC');tworem.append(n)
assert len(tworem)==4
for n in'DVU':
 for z in outputs[n]:
  p=q-z*(-1j);h=1;c3+=1
  if(int(p.real+p.imag)+h)%2:continue
  A=center(p,h);B=center(p+raw[n]['p']*(-1j),h)
  if meet((-1,-1),(1,1),xy(A),xy(B))is not None:continue
  helpers.append((n,z,p,p+raw[n]['p']*(-1j)))
assert set(helpers)=={('V',1j,-2-1j,1-2j),('U',-1+2j,-3-2j,1-2j),('U',2+1j,-2+1j,2+1j)}
helperwords=[]
for i,r in repair:
 f,t=r['foreign'],r['returned_atom'];fp=complex(*r['foreign_pose'][:2])
 for n,z,p,ep in helpers:
  found=[]
  for cv in counts(fp-ep):
   for s in orders(*cv):
    if(s[-1]if s else n)not in goodlast(f):continue
    lit=walk(W[n]+''.join(W[b]for b in s)+W[f]+W[t]+M);assert not lit['feasible'];found.append((s,lit['i'],xy(lit['q']),lit['first']))
  if ep==2+1j:assert not found
  helperwords.append((i,n,xy(p),found))
assert sum(len(w[-1])for w in helperwords)==12
assert{(f,tuple(p),tuple(rp))for i,f,p,rp in res}=={('F',(2,-5,1),(0,-1,3)),('Q',(4,-5,1),(0,-1,3)),('B',(5,-4,1),(0,-1,3))}
man=D/'returned_C_source_reduction_manifest.json';sh=hashlib.sha256(man.read_bytes()).hexdigest();assert sh=='c268e9e44a03348bce2645c29e1078f187128518eb288274c6a983a6515bcc6d';ma=json.loads(man.read_text())
for f,h in ma['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in ma['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS old-C returned first-contact reduction51 to3 necessary raw-C interfaces','manifest_sha256':sh,'counts':dict(classify),'containing_C_deleted_core_roles':roles,'age1_fixed_words':age1words,'fresh_producer_role_counts':[c1,c2,c3],'clock2_residual_types':tworem,'clock3_helpers':[(n,xy(z),xy(p),xy(ep))for n,z,p,ep in helpers],'helper_fixed_words':helperwords,'necessary_residues':res,'analytic':['The three old-C/incoming buds are protected only at foreign ENTRY at their signed atomic clocks, with all seven actual containing fullproducer shifts retained. Testing the actual concatenated foreign+returned atom+marker before-mask preserves all foreign toggles; a first L is allowed, and no postforeign maturity law is used.','The15 age-one cases reduce to exact zero-C W displacement counts. The y equation fixes d+v and the x equation fixes u; exhaustive multiset orders with genuine last-V/U adjacency give22 immutable RAW contradictions and2 rows with no allowed last packet. No length cap is assumed.','In all nine remaining D/V/U cases q=(-1,-1) is actually WHITE after every possible containing source: final RAW L, absent full fresh outputs and exit core. Foreign COMPLETE context misses q and both entry/exit cores miss it, while the later combined context requires black. Thus the last current q identity must genuinely be produced in the OLD eight interval after containing-source completion, at clock1,2 or3.','At1 every full-output W alignment misses x<=0,y>=1, including own tails. At2 all full-completable sector-valid alignments with x<=-1 reduce to r=(0,0),head(-1,-1,S) in V/VC/U/UC. Equality forces no preceding W base or S D/V, leaving y=1-4u, never-1. This is an all-u congruence.','At3 only plain sources complete before the foreign. Five of eight sector-valid V/U output roles contact the already actual old C chord; positive clock gap excludes adjacency. Three helpers remain; their exact E endpoint counts and all admissible multiset orders give12 literal contradictions. No returned simplicity is used.','The three survivors are age3 F(2,-5,E),Q(4,-5,E),B(5,-4,E), all followed by raw C(0,-1,W). They are necessary, not attained, and a returned standalone C is not relabelled as a full complete-eight packet.'],'scope':'Chronological first contact of the immediate returned raw ordinary atom with old C, after exactly one first foreign. Other old source types, later returns and additional foreign events remain open.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(classify)
