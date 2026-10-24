from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'second_ordinary_after_first_foreign_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'old_U_second_C_left_pair_guard_manifest.json';assert sha(man)=='036ef9ca2e9f4b2289b867a4c08dc1e2c30793d8a4340ae4ffdbcd7030a52ce9';mf=json.loads(man.read_text())
for p,h in mf['files'].items():assert sha(D/p)==h
for p,h in mf['dependencies'].items():assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_second_ordinary_small_interface_independent.py'))};exec(Path(ns['__file__']).read_text().split('triples=[]')[0],ns);W,M,walk,chord,minus,cross,meet,xy=[ns[k]for k in['W','M','walk','chord','minus','cross','meet','xy']];K={-1-1j,-1,-1j,0j,1};old=chord('U');ov=minus(old[1],old[0]);raw=walk(W['C']);first={}
for t,(q,h,c)in enumerate(raw['reads']):first.setdefault(q,(t,c))
rows=[]
for N in range(1,5):
 h=(2-N)%4;rot=(-1j)**h;cc=chord('C',0j,h);nv=minus(cc[1],cc[0]);assert cross(ov,nv)
 corners=[tuple(F(old[0][k]+s*ov[k]-cc[0][k]-t*nv[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(math.floor(min(q[k]for q in corners)),math.ceil(max(q[k]for q in corners)))for k in(0,1)]
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-N)%2:continue
   shift=lambda q:(q[0]+2*x,q[1]+2*y);hit=meet(*old,*map(shift,cc))
   if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
   obs=[]
   for tag in(0j,1j):
    local=(tag-complex(x,y))/rot
    if local in K:obs.append((xy(tag),'entryCORE',None))
    elif local in first and first[local][1]=='R':assert first[local][0]<15;obs.append((xy(tag),'ownRAW-firstR',first[local][0]))
   assert obs and hit[1]==1 and hit[0]in(F(0),F(1,2));rows.append((N,x,y,h,str(hit[0]),str(hit[1]),obs))
assert {(N,x,y,h)for N,x,y,h,*z in rows}=={(1,-1,0,1),(1,-1,2,1),(2,-1,-1,0),(2,-1,1,0),(3,0,-1,3),(3,0,1,3),(4,0,0,2),(4,0,2,2)}
ref=json.loads((D/'old_U_second_C_left_pair_guard.json').read_text());assert len(ref['signed16_angle_interfaces'])==16
for q in ref['signed16_angle_interfaces']:
 n,N=q['actual_old_source_to_FOREIGN_C_age'],q['total_ordinary_C_before_second'];assert n==N-(q['first_ordinary']=='C')and 1<=N<=4 and 0<=n<=4
out={'status':'PASS old-U source exclusion for chronological first SECOND RAW C contact only','author_manifest':sha(man),'exact_eight_poses_and_obstructions':rows,'analytic_review':[
'For oldU alpha0 and secondC alphaD, the signed angleinterface requires1<=effectiveN<=4. Truepreforeignn=N-1[b1=C] is at most4. A U/UC/UCC fullpacket begins at its Ubase, so the genuine creatingU entryclock is exactly that n clock, with ownCtails included. No postforeign age is used.',
'Signed firstFOREIGN originalstar-effect>=5 implies COMPLETE foreigncontextMISS at true age<=4. Signed exactCUT2 transfer then preserves SAME originalLEFT identities physicallyBLACK and CURRENT outside the ACTUAL secondentryK. This is stronger than finalblackcolor and does not count futureM11 as executed.',
'Four exact rational contact parallelograms, activeparity x+y=Nmod2 and outgoingold0<=s<1/new0<t<=1 give exactlyeight Cposes. All determinantsnonzero; all contacts secondendpointt1 and olds0 or1/2, never reowning oldUend. Everypose has a fixedLEFT member in entryK or requiringWHITE at an actual firstR withinC15 RAW.',
'EntryK contradicts the exactoutsideCORE premise at the samecut; firstR contradicts the unread originalBLACK label. Neither uses an edgebarrier throughsecondC, laterM execution or newcompletedproducer. Only oldU/newC firstcontacts close; othertargets andsources and general secondatomsimplicity remainopen.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
