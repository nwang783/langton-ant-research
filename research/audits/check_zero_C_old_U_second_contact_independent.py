from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'second_ordinary_after_first_foreign_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
man=D/'zero_preforeign_C_old_U_slice_manifest.json';assert sha(man)=='7c5eeafdf6f4d298894ebdd35dfb2e5098e408806131e88e751b4aca8e9ad52d';mf=json.loads(man.read_text())
for p,h in mf['files'].items():assert sha(D/p)==h
for p,h in mf['dependencies'].items():assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_second_ordinary_small_interface_independent.py'))};exec(Path(ns['__file__']).read_text().split('triples=[]')[0],ns);W,M,walk,chord,pose,minus,cross,meet,xy=[ns[k]for k in ['W','M','walk','chord','pose','minus','cross','meet','xy']]
ref=json.loads((D/'zero_preforeign_C_old_U_slice.json').read_text());old=chord('U');assert old==((-1,-1),(-1,7));v=minus(old[1],old[0]);heads=[];counts=[];words=[];boxes=[]
for A in 'FQB':
 p,h=pose('C',*pose(A))
 for b2 in 'DCV':
  nc=chord(b2,p,h);nv=minus(nc[1],nc[0]);assert cross(v,nv)!=0
  corners=[tuple(F(old[0][k]+s*v[k]-nc[0][k]-t*nv[k],2)for k in (0,1))for s in(0,1)for t in(0,1)]
  bounds=[(math.floor(min(q[k]for q in corners)),math.ceil(max(q[k]for q in corners)))for k in (0,1)]
  boxes.append((A,b2,bounds))
  for x in range(bounds[0][0],bounds[0][1]+1):
   for y in range(bounds[1][0],bounds[1][1]+1):
    if x<0 or y<4 or(x+y)%2:continue
    hit=meet(*old,*[tuple(q[k]+2*(x,y)[k]for k in(0,1))for q in nc])
    if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
    sols=[]
    for vv in range(x+1):
     dd=x-vv;rem=y-4-dd-3*vv
     if rem<0 or rem%4:continue
     uu=rem//4;sols.append((dd,vv,uu));counts.append((A,b2,x,y,dd,vv,uu))
     for run in sorted(set(permutations('D'*dd+'V'*vv+'U'*uu))):
      last=run[-1]if run else'U'
      if last not in('VU'if A in'FQ'else'U'):continue
      tok=('U',)+run+(A,'C',b2);raw=''.join(W[z]for z in tok);z=walk(raw+M);assert not z['feasible'];pp=0j;hh=0;last={}
      for ii,cc in enumerate(raw+M):
       if ii==z['i']:break
       last[pp]=ii;hh=(hh+(1 if cc=='R'else-1))%4;pp+=1j*(-1j)**hh
      assert pp==z['q'];words.append((tok,x,y,z['i'],last[pp],xy(z['q'])))
      head=0j;hh=0
      for b in tok[:1+len(run)]:head,hh=pose(b,head,hh)
      assert(head,hh)==(complex(x,y),0)
    heads.append((A,b2,x,y,sols))
assert len(words)==4 and {z[0]for z in words}=={tuple(z)for z in ['UVQCV','UDVQCV','UUBCV','UDUBCV']}
assert {(z[0],z[3],z[4],z[5])for z in words}=={(tuple('UVQCV'),137,21,(-1,2)),(tuple('UDVQCV'),121,29,(-1,4)),(tuple('UUBCV'),157,21,(-1,2)),(tuple('UDUBCV'),141,29,(-1,4))}
refs={(z['foreign'],z['second_returned'],*z['foreign_entry'][:2],tuple(map(tuple,z['all_nonnegative_endpoint_count_solutions'])))for z in ref['all_geometrically_possible_old_U_outgoing_contact_heads']};assert refs=={(a,b,x,y,tuple(ss))for a,b,x,y,ss in heads}
assert len(boxes)==9
cu=walk(W['C']+W['U']+M);assert not cu['feasible']and(cu['i'],cu['first'])==(29,1)
# Explicitly resolve the rejected provisional old-U-END case without relabeling.
p=0j;h=0
for b in 'UDUQC':p,h=pose(b,p,h)
endhit=meet(*old,*chord('V',p,h));assert endhit[0]==1
out={'status':'PASS old-U zero-preforeign-C SECOND-contact slice only','author_manifest':sha(man),'endpoint_derived_boxes':boxes,'all_heads_and_count_solutions':heads,'all_four_words_and_conflicts':words,'provisional_UDUQCV_old_parameter':str(endhit[0]),'analytic_review':[
'With sourceU alpha0 and actual preforeign C countn0, signed Jordan angle condition excludes totalN0. Therefore first returned RAW mustC, N1. An actual complete preforeign source UC/UCC would have positiveCcount, so sourceplainU. The local CU immutable conflict excludes secondU without any postforeign identity law.',
'No preforeign C leaves arbitrary intervening plainD/V/U allheadingN. Exact head equations x=d+v, y=4+d+3v+4u plus exact translated-chord contact parallelogram yield finite bounds with no run-length assumption. For each head every v in[0,x] determinesd andu, and every multiset order is retained before checking actual lastV/U adjacency.',
'All nine contact determinants are nonzero. Closed source/new intersections are filtered to outgoing-old ownership0<=s<1 and positive newtime0<t<=1. SourceU end s1 is excluded because its next old atom owns that vertex, not because the geometry is impossible. UDUQCV explicitly lands at that endpoint.',
'The four surviving full literal words have consecutive equal read colors independent of arbitrary prior/exterior board. Two repeat sourceqR21 at secondV12/read13; two repeat source-contextL29 at firstC1/read2. Ucontext29 is physically the following oldD tick1/read2, not owned U RAW. All actual full-word lengths and M11 are retained.',
'No input-age or star-permanence law crosses the foreign. The arbitrary earlier prefix is irrelevant to immutable internal read contradictions. Only oldU n0 slice is excluded; n>=1, other old sources, general secondatom simplicity and capture remain open.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(heads),'geometric heads',len(counts),'count rows')
