from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];ns={"__file__":str(SELF)}
exec((SELF.parent/'check_foreign_kinked_barrier_turn_independent.py').read_text().split('geometries=[]')[0],ns)
walk,W,M,xy=[ns[x]for x in('walk','W','M','xy')];D=ROOT/'seven_word_spatial_return_2026-10-23'
names=['D','DC','V','VC','VCC','U','UC','UCC'];K={-1-1j,-1,-1j,0,1};raw={};ctx={};I={};O={};tails={n:n.count('C')for n in names}
GP=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];keep=[0,1,4,5,6,7,8,9]
for n,gid in zip(names,keep):
 raw[n]=walk(''.join(W[c]for c in n));ctx[n]=walk(''.join(W[c]for c in n)+M);assert ctx[n]['feasible'];before={q for q,c in ctx[n]['req'].items()if c};I[n]=before-K
 endcore={raw[n]['p']+q*(-1j)**raw[n]['h']for q in K};O[n]=(before^raw[n]['odd'])-endcore
 assert set(map(xy,I[n]))==set(map(tuple,GP[gid]['inputs']));assert set(map(xy,O[n]))==set(map(tuple,GP[gid]['outputs']))
CP=ROOT/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';count={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()}
def key(s,c,o,p,h,a):return(names.index(s),names.index(c),*xy(p),h,*xy(o),a)
def why(s,c,o,p,h,a):return 'sector'if(int(p.real+p.imag)+h)%2 else 'COUNT5'if key(s,c,o,p,h,a)in count else None
ports=dict(zip(names,[1j,1j,1+2j,1+2j,3j,-1+4j,-1+4j,-1+4j]));portrows=[]
for n in names:
 q=ports[n];hits=[(i,c)for i,(z,h,c)in enumerate(ctx[n]['reads'])if z==q];birth=[(i,c)for i,(z,h,c)in enumerate(raw[n]['reads'])if z==2]
 assert q in I[n] and 2 in O[n] and birth[-1]==(8,'R');assert hits[0]==({'D':11,'DC':11,'V':13,'VC':13,'VCC':19,'U':29,'UC':29,'UCC':29}[n],'L')
 inside=hits[0][0]<len(raw[n]['reads']);assert inside==(n not in('D','U'))
 delta=2j-q*1j;assert delta.real>0 and delta.imag>0
 portrows.append((n,xy(q),hits[0][0],inside,xy(delta)))
same=[]
for s in('D','V','U'):
 for o in O[s]:
  for c in names:
   p=o-ports[c];r=why(s,c,o,p,0,0);assert r;same.append(r)
assert Counter(same)=={'sector':64,'COUNT5':64}
order=[]
for s in('D','V','U'):
 for c in names:
  step=raw[s]['p']*1j;di=ports[s]*1j-(step+ports[c]*1j);assert di.real>0 and step.real<0;order.append((s,c,int(di.real),int(-step.real)))
future={}
for f,p in [('F',2-5j),('Q',4-5j),('B',5-4j)]:
 tr=walk(W[f]+W['C']+M);assert tr['feasible'];future[f]={p+q*(-1j):v for q,v in tr['req'].items()};assert min(q.real for q in future[f])==-3 and max(q.imag for q in future[f])==1 and future[f][1j]is False
heads=[('',1j),('D',-1+2j),('DD',-2+3j),('DDD',-3+4j),('V',-3+2j)];assert all(q.imag>=0 for n in names for q in O[n]);vis=[];total=0
for f,ct in future.items():
 for pref,hp in heads:
  for n in names:
   for q in O[n]:
    total+=1;p=hp+q*1j
    if p in ct:
     assert pref==''and n not in('D','DC')and q in(0,1j,-1+2j)and ct[p]is False;vis.append((f,n,xy(q),xy(p)))
assert total==1020 and len(vis)==45
vr=[]
for s in('V','VC','VCC'):
 for a in range(3):
  h=(-a)%4
  for c in names:
   for i in I[c]:
    p=-i*(-1j)**h;r=why(s,c,0j,p,h,a);assert r;vr.append(r)
assert Counter(vr)=={'sector':120,'COUNT5':87}
# The subsequent transport statement is independently reconstructed, including
# actual full-source completion rather than an internal C physical birth.
young={a:Counter()for a in(0,1)}
for a in(0,1):
 h=(-a)%4
 for s in names:
  for o in O[s]:
   for c in names:
    for i in I[c]:
     p=o-i*(-1j)**h;r=why(s,c,o,p,h,a)
     if r is None:assert a<tails[s] and s in('VCC','UCC');r='uncompleted source'
     young[a][r]+=1
assert young=={0:Counter({'sector':760,'COUNT5':770,'uncompleted source':34}),1:Counter({'sector':804,'COUNT5':748,'uncompleted source':12})}
repro=Counter();exceptions=[]
for s in names:
 for o in O[s]:
  for c,i in [('V',1+2j),('U',3j)]:
   assert i in I[c];p=o+i;r=why(s,c,o,p,2,2)
   if r is None:
    assert(s,o)in[('VCC',1j),('UCC',-1+2j)];r='V A lock'if s=='VCC'else'U q port law';exceptions.append((s,xy(o),c,xy(i),xy(p)))
   repro[r]+=1
assert repro=={'sector':64,'COUNT5':68,'V A lock':2,'U q port law':2}
relay=[];relaytotal=0
for f,ct in future.items():
 for pref,hp in heads[:3]:
  for s in names:
   if not pref and s not in('D','DC'):continue
   for o in O[s]:
    relaytotal+=1;q=hp+o*1j;out=q-1-2j
    if out in ct:
     # D input relative W producer frame: output o, antiparallel input -i.
     p=o+1j;assert why(s,'D',o,p,2,2)=='sector';relay.append((f,pref,s,xy(o),xy(q),xy(out)))
assert len(relay)==24
bound={}
for stem,sha in [('ordered_W_archive_matching','bf616fdc960c8e24a259b2581c92a3d0eee02e6a06c31e43ed1e71493e6aed8e'),('ordered_W_transport_bottleneck','ef64552072ac5b42a452815a86c903e4be26469d5450b2222008668209acc97c')]:
 mp=D/(stem+'_manifest.json');assert hashlib.sha256(mp.read_bytes()).hexdigest()==sha;mf=json.loads(mp.read_text())
 for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
 for f,h in mf['dependencies'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
 bound[stem]=sha
out={'status':'PASS all-length ordered W archive and preforeign actual identity transport bottleneck','manifests':bound,'literal_full_ports':portrows,'same_clock':dict(Counter(same)),'adjacent_order_checks':len(order),'visibility_queries':total,'visible_roles':len(vis),'young_V_r':dict(Counter(vr)),'young_all_outputs':{str(a):dict(v)for a,v in young.items()},'reproductive_queries':dict(repro),'four_signed_port_exceptions':exceptions,'visible_D_relays':len(relay),'relay_total':relaytotal,'analytic':['After the actual containing source completes, a nonempty W stage starts at old C exit (0,1,W). C1 within a double-tail source instead leaves no W stage, so there is no fictitious internal marker reset. All entries at W stage have full-source clock1, including the final tail-bearing packet.','No earlier W full output can fund a chosen input at age0. The ordered residual ledger therefore identifies all chosen inputs as distinct unchanged W-entry identities. Marker-only physical reads may occur after the source common R8 birth; the assertion is ledger exchange, not chronological L-before-R.','Common outputs have y>=3 and cannot retire before full-source-entry age3; foreign entry age2 protects them in the old eight factor. Complete foreign+returnedC+M11 reads have y<=1, so the original birth lifetimes remain current throughout the continuation.','All full outputs have local y>=0. Future min x=-3 bounds A<=3, giving exactly empty,D,DD,DDD,V head prefixes for ANY W length. Only first V/U base roles can meet context, and their held r requires white there. Hence first D; all W outputs directly avoid future physical context.','The full-source completion test is needed only for source VCC/UCC. Age0/1 exclusions remove W-to-S, S-to-E, same-stage identity supplies. Actual E reproductive selected ports are V(1,2), U(0,3), irrespective informal lower/upper labels. Four remaining W-to-E roles are eliminated by signed all-age V-A and U-q causal laws. Every selected E input is therefore an additional unchanged W-entry identity, disjoint from W spent choices.','An E-D maps its actual input q to sole output q-(1,2). Future visibility forces W-head A<=2, exactly empty,D,DD. All24 visible alignments have wrong conserved sector. This excludes only direct input-output ancestry, not counterfactual guard effects or S/E work.'],'scope':'Arbitrary finite W length in the three signed old-C first-return residues. No whole-ledger contraction, second foreign, returned maturity, finite-state quotient, or global capture claim.'}
ep=D/'ordered_W_U_role_label_erratum_manifest.json';eh=hashlib.sha256(ep.read_bytes()).hexdigest();assert eh=='f2ff1b4df6f8fe968ec379ad639cdd98f6b5836c54b11dd8485ca83850ff2cae'
for f,h in json.loads(ep.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out['mandatory_role_label_erratum_manifest_sha256']=eh
out['role_label_correction']='U (0,3) is the usual upper d input, not lower a/q. Both frozen coordinate calculations remain unchanged.'
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(young,repro)
