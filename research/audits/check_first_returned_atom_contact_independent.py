from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import json,hashlib,math
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23'
s=(SELF.parent/'check_foreign_kinked_barrier_turn_independent.py').read_text();exec(s.split('geometries=[]')[0]);SELF=Path(__file__).resolve();a=json.loads((D/'first_returned_atom_contact.json').read_text());ranks={'U':0,'V':1,'D':2,'C':2};traces={x:walk(W[x])for x in'DCVUFQB'}
def chord(x,p=0j,h=0):
 start=center(p,h);delta=center(traces[x]['p'],traces[x]['h'])-center(0,0);return xy(start),xy(start+delta*(-1j)**h)
def pieces(f,p=0j,h=0):
 pts=[-1-1j,-7-3j]+([]if f=='F'else[center(traces[f]['p'],traces[f]['h'])]);pts=[xy(2*p+q*(-1j)**h)for q in pts];return list(zip(pts,pts[1:]))
def first(a,b,c,d):
 hit=meet(a,b,c,d)
 if hit is None:return None
 u=minus(b,a);v=minus(d,c)
 if cross(u,v):
  ss,tt,q=hit
  return(ss,tt,'point')if 0<=ss<1 and 0<tt<=1 else None
 if sum(u[i]*v[i]for i in(0,1))<=0:return None
 i=0 if v[0]else 1;t=F(a[i]-c[i],v[i]);return(F(0),t,'collinear_first_onset')if 0<t<=1 else None
rows={};angles=[];disc=0
for src in'DCVU':
 for tar in'DCVU':
  for n in range(5):
   if src=='C'and n==0:continue
   if not(n in(1,2,3)or n==0 and ranks[src]>ranks[tar]or n==4 and ranks[src]<ranks[tar]):continue
   h=(2-n)%4;hf=(-n)%4;angles.append((src,tar,n,h));aa,bb=chord(src);u=minus(bb,aa);off=xy((-1-1j)*(-1j)**h);v=minus(*chord(tar,0j,h)[::-1])
   corners=[tuple(aa[j]+s*u[j]-off[j]-t*v[j]for j in(0,1))for s in(0,1)for t in(0,1)];bounds=[(-((-min(c[j]for c in corners))//2),max(c[j]for c in corners)//2)for j in(0,1)]
   for x in range(bounds[0][0],bounds[0][1]+1):
    for y in range(bounds[1][0],bounds[1][1]+1):
     if(x+y+h)%2:continue
     p=complex(x,y);hit=first(aa,bb,*chord(tar,p,h))
     if hit is None:continue
     for f in'FQB':
      fp=p-traces[f]['p']*(-1j)**hf;clear=True;adj=[]
      for i,(cc,dd)in enumerate(pieces(f,fp,hf)):
       prior=meet(aa,bb,cc,dd)
       if prior is None:continue
       legal=cross(minus(bb,aa),minus(dd,cc))!=0 and prior[:2]==(F(1),F(0))and i==0 and(src in'VU')and(fp,hf)==(traces[src]['p'],traces[src]['h'])
       if not legal:clear=False;break
       adj.append(i)
      if not clear:disc+=1;continue
      key=(src,tar,f,n,x,y,h);assert key not in rows;rows[key]=(hit,(*xy(fp),hf),bounds,adj)
assert len(angles)==56 and len(rows)==371
assert Counter(k[0]for k in rows)=={'D':60,'C':51,'V':112,'U':148}
for ref in a['old_source_contact_cases']:
 key=(ref['source_atom'],ref['returned_atom'],ref['foreign'],ref['source_to_foreign_C_age'],*ref['returned_pose']);hit,fp,bounds,adj=rows.pop(key)
 assert hit==(F(ref['contact']['s']),F(ref['contact']['t']),ref['contact']['kind']);assert fp==tuple(ref['foreign_pose'])and bounds==list(map(tuple,ref['exact_candidate_bounds']));assert adj==[r['piece']for r in ref['legal_foreign_initial_adjacencies']]
assert not rows and disc==sum(a['discarded_by_clearance'].values())
local=[]
for f in'FQB':
 t=traces[f]
 for b in'DCVU':
  c,d=chord(b,t['p'],t['h']);hs=[]
  for i,(aa,bb)in enumerate(pieces(f)):
   hit=meet(aa,bb,c,d)
   if hit is not None:
    assert i==len(pieces(f))-1 and bb==c
    if cross(minus(bb,aa),minus(d,c)):assert hit[:2]==(F(1),F(0))
    else:assert hit==(c,)
    hs.append(i)
  assert len(hs)==1;lit=walk(W[f]+W[b]+M);assert lit['feasible'];local.append((f,b,sum(lit['req'].values())))
full=[];G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
for f in'FQB':
 for i in(0,1,4,5,6,7,8,9):
  lit=walk(W[f]+G[i]['word']+M);assert lit['feasible'];full.append((f,G[i]['name'],sum(lit['req'].values())))
for ref in a['actual_old_fullproducer_clock_annotations']:
 row=a['old_source_contact_cases'][ref['case']];n=row['source_to_foreign_C_age'];src=row['source_atom']
 if src=='C':
  expected=[]
  for name in('DC','VC','VCC','UC','UCC'):
   for j in range(1,name.count('C')+1):expected.append({'full_packet':name,'C_index':j,'full_source_C_age':n+j-1,'full_source_completed':n>=1+name.count('C')-j})
 else:expected=[{'full_packet':name,'full_source_C_age':n,'full_source_completed':n>=name.count('C')}for name in{'D':['D','DC'],'V':['V','VC','VCC'],'U':['U','UC','UCC']}[src]]
 assert ref['roles']==expected
man=D/'first_returned_atom_contact_manifest.json';sha=hashlib.sha256(man.read_bytes()).hexdigest();assert sha=='374591ca34e64828b03948596df0faa587e79264538a74807f084b57e5d98089';m=json.loads(man.read_text())
for f,h in m['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in m['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS one-first-foreign immediate returned-atom necessary contact catalogue','manifest_sha256':sha,'angle_cases':len(angles),'old_source_cases':371,'foreign_clearance_discards':disc,'local_foreign_returned_controls':local,'prepared_full_successors':full,'analytic':['The signed old-plus-one-foreign path is simple. Every immediate returned chord meets each foreign piece only at its actual terminal adjacent endpoint; Q-to-U is collinear forward continuation, not reversal. Therefore any first new contact is with the older eight path.','With exactly one foreign and actual preceding-C bit0, the tangent lift from outgoing source to target is (n+2)pi/2+alpha(source)-alpha(target). Target C is not included, source C is. This follows the literal repaired turn formula, not an imported old-eight age bound.','At a chronological first contact the intervening simple subarc closes to a Jordan loop. Opposite closing tangents would force earlier overlap, so closing principal turn is strictly in(-pi,pi). Since n>=0, negative Jordan rotation is impossible. Hence pi<L<3pi, yielding n0..4 with strict endpoint alpha rankings and excluding source-C n0.','Exact rational intersection boxes are derived from the four parallelogram corners, with conserved-sector parity. Nonparallel contacts use outgoing-source parameter[0,1) and new parameter(0,1]. Collinear same-direction first onset is at the old START; opposite entry at old END belongs to the next outgoing atom. Already-simple foreign clearance excludes zero-time overlap.','Any earlier foreign-piece/source intersection rejects the case unless it is the true initial adjacent V/U endpoint with matching physical head and heading. Corrected-center coincidence alone is insufficient. This gives exactly371 necessary geometries from56 angle cases.','All seven old actual fullproducer C roles have full age n+j-1 and completion condition n>=1+remaining tails. D/V/U full types retain n>=tail count. Target raw C after foreign is only a literal atom here, not a newly invented fullproducer or marker reset.'],'scope':'Necessary geometry only for FIRST immediate returned raw atom after exactly one first complete foreign. No contact excluded or attained, no later returned atom, postforeign star/lifetime authority, second foreign, mixed-language termination or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
