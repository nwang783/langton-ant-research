from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201'
ns={'__file__':str(R/'audits/check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns)
W,M,walk,center,xy=(ns[k]for k in('W','M','walk','center','xy'))
K={-1-1j,-1,-1j,0,1};names=['D','DC','V','VC','VCC','U','UC','UCC'];inv={}
for name in names:
 word=''.join(W[c]for c in name);raw=walk(word);full=walk(word+M);assert raw['feasible']and full['feasible'];inputs={q for q,b in full['req'].items()if b}-K;field={q for q,b in full['req'].items()if b}^raw['odd'];core={raw['p']+q*(-1j)**raw['h']for q in K};outputs=field-core
 inv[name]={'inputs':inputs,'outputs':outputs,'p':raw['p'],'h':raw['h'],'raw':raw,'full':full}
COUNT={tuple(map(int,line.split()[:8]))for line in(R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()}
def guard(sources,q,ages):
 rows=[]
 for source in sources:
  assert q in inv[source]['outputs']
  for n in ages:
   h=(-n)%4;turn=(-1j)**h
   for target in names:
    for z in inv[target]['inputs']:
     p=q-z*turn;key=(names.index(source),names.index(target),*xy(p),h,*xy(q),n)
     why='sector'if(int(p.real+p.imag)+h)%2 else'count'if key in COUNT else'OPEN';assert why!='OPEN',key
     rows.append((source,target,n,xy(z),xy(p),h,why))
 return rows
bud=1+3j;rows=guard(['U','UC','UCC'],bud,[3,4]);assert len(rows)==138 and Counter(r[-1]for r in rows)=={'sector':69,'count':69}
for name in('U','UC','UCC'):
 reads=[(i,ch)for i,(p,h,ch)in enumerate(inv[name]['raw']['reads'])if p==bud];assert reads[-1][1]=='R'and reads[-1][0]<28
ports=[('F',1+3j),('Q',1+3j),('B',1+3j),('F',2+4j),('Q',2+4j),('F',3+3j)];cuts=[]
for name,p in ports:
 t=walk(W[name]+M);local=bud-p;first=next((i,ch)for i,(q,h,ch)in enumerate(t['reads'])if q==local)
 if local in K:why='core'
 else:assert t['req'][local]is False and first==(44,'R');why='white'
 cuts.append((name,xy(p),why,first))
# Entire atomic zero-C cones, not sampled words.
steps=[inv[a]['p']for a in('D','V','U')];assert steps==[1+1j,1+3j,4j];assert all(z.imag>=0 and(z*1j).imag>=0 for z in steps)
assert walk(W['C'])['p']==1j and walk(W['C'])['h']==3
assert 4+1>3
cleanup=-1+5j;fh=3;fp=-2+3j;q=-1+2j;assert(q-fp)/((-1j)**fh)==-1-1j
assert(fp-cleanup)/(-1)==1+2j and(fh-2)%4==1
common=2;commonrows=guard(['V','VC'],common,range(3));assert len(commonrows)==138 and Counter(r[-1]for r in commonrows)=={'sector':80,'count':58}
ends=[]
for a in('D','V','U'):
 for slot in inv[a]['inputs']:
  p=common-slot*(-1j);end=p+inv[a]['p']*(-1j);assert end.real>=2;ends.append((a,xy(slot),xy(p),xy(end)))
assert len(ends)==8 and all((z*(-1j)).real>=0 for z in steps)
z=cleanup-common;local=(z-fp)/((-1j)**fh);assert z==-3+5j and local==2+1j
f=walk(W['F']+M);assert next((i,ch)for i,(q,h,ch)in enumerate(f['reads'])if q==local)==(7,'R')and f['req'][local]is False
manifest=D/'manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='adf3dfa34019a3ff443b22b6ca664fe918f4a8ce755b358fc61e5db16f14c956'
for name,expected in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==expected
out={'status':'PASS genuine U-source F-prefix bud and q-cleanup cuts','manifest_sha256':sha,'creator_bud_queries':{'count':len(rows),'reasons':dict(Counter(r[-1]for r in rows))},'age4_port_cuts':cuts,'cleanup_common_queries':{'count':len(commonrows),'reasons':dict(Counter(r[-1]for r in commonrows))},'cleanup_age3_endpoints':ends,'remaining_after_signed_predecessors':[['F',[2,4,0],8],['F',[3,3,0],8],['Q',[2,4,0],8]],'analytic':['The U-base exit bud is freshly installed before any source C tail; full-source entry and atomic U start share clock0. Signed1325 covers ages0..2 and all literal COUNT5 queries cover3/4. No core absorption is omitted from full input alignments.','At age1 from U-base exit, N and W zero runs never decrease y and the one C adds1. Target y3 is impossible even with arbitrary zero-C lengths and source internal tails.','At west age5, original q must retire before foreign core entry. Signed1954/2027 restrict actual cleanup to V/VC at(-1,5,S), clock2, excluding UC creators. Its current common output cannot retire before relative age3.','A relative-age3 consumer before the full foreign entry must have no positive C tail. All eight zero-C E input roles exit at x>=2, and subsequent zero-C E motion cannot decrease x to foreign x1. Thus the common output survives to actual F RAW7, which requires it white.','Only the signed predecessor lemma removes the six remaining N age8 ports at(1,3,N), leaving the three displayed interfaces. No cycle renewal is inferred from a missing gate inventory.'],'scope':'Common F-prefix first contacts with a genuine U source only. No Q/B-tail closure, full proxy simplicity, arbitrary seven-word coverage or universal capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
