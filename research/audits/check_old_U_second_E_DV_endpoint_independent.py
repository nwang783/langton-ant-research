from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'second_ordinary_after_first_foreign_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'old_U_second_E_DV_endpoint_guard_manifest.json';assert sha(man)=='ca9ed116cdb0eb6ddf72dbc416ce8d53e9001b45f3a5a5f35da82334982fb7d6';mf=json.loads(man.read_text())
for p,h in mf['files'].items():assert sha(D/p)==h
for p,h in mf['dependencies'].items():assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_second_ordinary_small_interface_independent.py'))};exec(Path(ns['__file__']).read_text().split('triples=[]')[0],ns);W,M,walk,chord,minus,cross,meet,xy=[ns[k]for k in['W','M','walk','chord','minus','cross','meet','xy']];K={-1-1j,-1,-1j,0j,1};old=chord('U');ov=minus(old[1],old[0]);geoms=[];surv={}
for b2 in'DV':
 cc=chord(b2,0j,1);nv=minus(cc[1],cc[0]);assert cross(ov,nv)
 corners=[tuple(F(old[0][k]+s*ov[k]-cc[0][k]-t*nv[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(math.floor(min(q[k]for q in corners)),math.ceil(max(q[k]for q in corners)))for k in(0,1)];first={}
 for t,(q,h,c)in enumerate(walk(W[b2]+M)['reads']):first.setdefault(q,(t,c))
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-1)%2:continue
   hit=meet(*old,*[(q[0]+2*x,q[1]+2*y)for q in cc])
   if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
   witnesses=[]
   for tag in(0j,1j):
    loc=(tag-complex(x,y))/(-1j)
    if loc in K or loc in first and first[loc][1]=='R':witnesses.append((xy(tag),xy(loc),'CORE'if loc in K else first[loc]))
   geoms.append((b2,x,y,str(hit[0]),str(hit[1]),witnesses))
   if not witnesses:assert b2 not in surv;surv[b2]=complex(x,y);assert hit[:2]==(F(0),F(1))
assert len(geoms)==8 and surv=={'D':-1+0j,'V':-3+0j}
assert (walk(W['U'])['p'],walk(W['U'])['h'])==(4j,0)
inc={h:{b:ns['pose'](b,0j,h)for b in'DVU'}for h in(0,3)}
assert inc=={0:{'D':(1+1j,0),'V':(1+3j,0),'U':(4j,0)},3:{'D':(-1+1j,3),'V':(-3+1j,3),'U':(-4+0j,3)}}
assert walk(W['C'])['p']==1j and walk(W['C'])['h']==3
ob=[];words=[]
for b2,p2 in surv.items():
 for b1 in'DVU':
  for A in'FQB':
   a=walk(W[A]+W[b1]);assert a['feasible'];q=(a['p']*(-1j)**3,(a['h']+3)%4);assert q[1]==1;pA=p2-q[0];assert pA.imag<=5
   if pA.imag==5:
    assert pA.real<0
    if int(pA.real)%4==0:
     u=-int(pA.real)//4;assert u>0;toks='UC'+'U'*u+A+b1+b2;raw=''.join(W[a]for a in toks);tr=walk(raw+M);assert not tr['feasible']and(tr['i'],tr['first'],tr['q'])==(57,29,-1+4j)
     p=0j;h=0;occ=[]
     for i,c in enumerate(raw[:58]):
      if p==-1+4j:occ.append((i,c))
      h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
     assert occ==[(29,'L'),(57,'L')];assert pA==complex(-4*u,5);words.append(toks)
   ob.append((b2,b1,A,xy(pA)))
assert set(words)=={'UCUFDD','UCUUQVD','UCUUQDV','UCUUFVV'}and len(ob)==18
ref=json.loads((D/'old_U_second_E_DV_endpoint_guard.json').read_text());assert len(ref['signed8_angle_interfaces'])==8
for q in ref['signed8_angle_interfaces']:assert q['total_ordinary_C_before_second']==1 and q['actual_old_source_to_FOREIGN_C_age']==1-(q['first_ordinary']=='C')
out={'status':'PASS old-U source second E-facing D/V first-contact exclusion, exact all-length one-C endpoints','author_manifest':sha(man),'eight_geometries':geoms,'eighteen_foreign_obligations':ob,'four_words':words,'analytic_review':[
'Signed angle clock yields effectiveN1 for E-facing secondD/V. b1C means truepreforeignn0, handled by separate signedzeroC U theorem. Otherwise true n1. Ufullsourceentry equals its Ubaseentry, including ownfirstCtail. Signedstarfirsteffect>=5 plus CUT2foreigncontextMISS gives originalLEFT currentoutsideactualsecondK. No lifetimeage beyondforeign imported.',
'Fresh two exact parallelograms and activeparity produce2D/6V outgoing-owned poses;6 contradict fixedLEFT by entryK or fullcontextfirstR, two survive at D(-1,0,E),V(-3,0,E),oldparameter0/new1. Vmarker-ownedL is not falsely called RAWretirement. All first-read constraints use the actual followingM, not executed prematurely.',
'After Uexit0,4N, exactlyone actualC splits any fullpacket history into N and W primitivebases. Its ownfullproducerrole changes no primitive displacement. Nonnegative counts give yA=5+dN+3vN+4uN+dW+vW and xA=dN+vN-dW-3vW-4uW without any runlengthcap.',
'All18 exact A+b1inverseendpoint obligations havey<=5. Equalityforcesallpositiveycounts0; everyequalityhead hasxnegative, so nonemptyW U-onlyrun. ActualCU RAW repeatsL Ctick1/U tick14 with no interveningread; impossiblewhetherC is fullstandaloneorownfulltail. No fictitiousCentrymarker needed. Emptyrunx0cannotmatch.',
'Fourexactwholewords merely corroborateuniversalendpoint proof; allglobal57/29 repeatedL at(-1,4), Ctailtick1/read2 thenU tick14/read15. No positiveboard/controller inferred. Otherheadings/sources andn>=othercases andgeneral secondatomsimplicity remainopen.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
