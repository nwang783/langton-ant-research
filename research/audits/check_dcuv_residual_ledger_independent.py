"""Independent complex-coordinate reconstruction of all ten DCUV packets."""
from pathlib import Path
import json,hashlib,random
P=Path(__file__).resolve().parents[1];D=P/'core_periodicity_new/chronology_dcuv';G=json.loads((D/'literal_residual_geometry.json').read_text())
raw={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR','U':'LLLLRLRRRRLRLLLLRRRRLRRLRRRR'}
names=['D','DC','DCC','DCCC','V','VC','VCC','U','UC','UCC'];M='LLLLRLRRRRL'
def xy(z):return[int(z.real),int(z.imag)]
def order(points):return sorted(map(xy,points))
def trace(w):
 p=0j;h=1j;first={};last={};flip=set();reads=[]
 for i,c in enumerate(w):
  assert last.get(p)!=c
  first.setdefault(p,(c=='L',i));last[p]=c;flip.symmetric_difference_update({p});reads.append((p,c));h*=(-1j if c=='R'else 1j);p+=h
 return p,h,first,last,flip,reads
core={z for z,(b,t)in trace(M)[2].items()if b};assert order(core)==G['core']
rng=random.Random(125987);cases=[];boardchecks=0
for i,name in enumerate(names):
 w=''.join(raw[c]for c in name);p,h,_,last,flip,reads=trace(w);_,_,req,_,_,_=trace(w+M)
 B={z for z,(b,t)in req.items()if b};K={p+h/1j*z for z in core};I=B-core;O=(B^flip)-K;F=set(req)
 assert core<=B and K<=B^flip and core|K|flip|I|O<=F
 assert all(last[z]=='R'for z in O)
 assert I&O==({-1+2j}if name.startswith('U')else set())
 expected={'packet':i,'name':name,'word':w,'marker':M,'endpoint':xy(p)+[[1j,1,-1j,-1].index(h)],'inputs':order(I),'outputs':order(O),'recycled':order(I&O),'requirements':[[*xy(z),b,t]for z,(b,t)in sorted(req.items(),key=lambda kv:xy(kv[0]))],'raw_odd':order(flip),'mass_change':len(O)-len(I)}
 assert expected==G['geometry'][i]
 for _ in range(100):
  X={complex(rng.randint(-20,20),rng.randint(-20,20))for _ in range(20)}-F
  Bfull=B|X;E=Bfull-core;labels={z:('old',z)for z in E};after=set(Bfull)
  for z,c in reads:
   assert(z in after)==(c=='L');after.symmetric_difference_update({z})
  assert after-K==(E-I)|O==O|X
  for z in I:del labels[z]
  for z in O:labels[z]=('new',i)
  assert set(labels)==after-K and all(labels[z][0]=='old'for z in X)
  assert all(labels[z][0]=='new'for z in I&O)
  boardchecks+=1
 cases.append({'packet':name,'mass_change':len(O)-len(I),'input_output_overlap':order(I&O),'context_cells':len(F)})
profile=json.loads((D/'profile.json').read_text())
for v in profile['files'].values():assert hashlib.sha256(Path(v['path']).read_bytes()).hexdigest()==v['sha256']
# Rebuild the full candidate adjacency input, rather than trusting a pruned grammar.
lines=[str(len(names))]+[''.join(raw[c]for c in name)+' '+M for name in names]+['100']+[f'{a} {b}'for a in range(10)for b in range(10)]
assert(D/'literal.input').read_text().split()==('\n'.join(lines)).split()
out={'status':'PASS exact all-ten-packet residual ledger, source geometry, and full unpruned literal kernel input','packets':cases,'random_complete_boards':boardchecks,'hashes':profile['files'],'scope':'All-board identity plus finite controls. No DCUV capture or recurrent-type pruning is inferred.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
