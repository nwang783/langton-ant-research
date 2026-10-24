"""Exact all-parameter augmented-hull record inventory; not ordinary records inside prepared input."""
from pathlib import Path
import hashlib,json
from certified_comparison_perturbation import geometry
P=Path(__file__).parent;A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());J=json.loads((P/'JOINT_RECORD_DROUGHT_CHECKED.json').read_text());W=R['W']
pre,_,mp,mh=geometry((0,0),1,W*100+W[:13]+R['modes']['M']['recovery_word']);F,_,_,_=geometry(mp,mh,W[41:]+W[:41]);TP,_,_,_=geometry((0,0),0,A['T_recovery']);Z=A['controls'][0]['complete_future_certificate']['tail_word'];Q,_,end,eh=geometry((155,215),1,Z)
# Initial full seed hull[-1,2n+242]x[0,2n+241]; no source or forward-flight record.
ineq=[]
def nn(a,b,label):assert a>=0 and 100*a+b>=0,(label,a,b);ineq.append((label,a,b))
def inside(ax,bx,ay,by,label):
 for a,b in[(ax,bx+1),(2-ax,242-bx),(ay,by),(2-ay,241-by)]:nn(a,b,label)
for i,(x,y)in enumerate(pre):inside(0,x,0,y,f'pre{i}')
for i,(x,y)in enumerate(F):inside(0,x,0,y,f'flight_first{i}');inside(2,x-2,2,y-2,f'flight_last{i}')
for i,(x,y)in enumerate(F[:76]):inside(2,x,2,y,f'flight_partial{i}')
mx=my=12;records=[]
for t,(x,y)in enumerate(TP):
 if x>mx:assert x==mx+1;mx=x;records.append((t,1,x))
 if y>my:assert y==my+1;my=y;records.append((t,0,y))
 assert x+230+200>=-1 and y+229+200>=0
assert len(records)==29 and records[-1]==(8470,0,33) and max(records[i+1][0]-records[i][0]for i in range(28))==3390
stable={}
for a in range(4):
 dot=lambda q:(q[1],q[0],-q[1],-q[0])[a];delta=dot((end[0]-155,end[1]-215));v=[dot(q)for q in Q]
 if delta<=0:stable[a]=[];continue
 old=max(v)-delta;fresh=[]
 for i,z in enumerate(v):
  if z>old:fresh.append((i,z));old=max(old,z)
 stable[a]=fresh
assert stable=={0:[(43,219),(57,220)],1:[],2:[],3:[(90,-152),(100,-151)]}
for c in J['controls']:
 if not c['name'].startswith('MT_'):continue
 n=int(c['name'][3:]);tc=21201+104*n;e=80270+208*n;N=c['physical_reads'];pred=[(tc+t,a)for t,a,z in records]
 for k in range(77,(N-e)//104+2):
  pred.extend((e+104*k+i,3)for i in(90,100)if e+104*k+i<=N)
 for k in range(n+22,(N-e)//104+2):
  pred.extend((e+104*k+i,0)for i in(43,57)if e+104*k+i<=N)
 pred.sort();assert pred==[tuple(z)for z in c['pristine_support_hull_records']]
 gaps=[pred[i+1][0]-pred[i][0]for i in range(len(pred)-1)];assert [z for z in gaps if z>3390]==[58697+104*n]
# Exact inherited exit thresholds; later N records only subdivide the <=94 W gaps.
assert (1+152)//2+1==(1+151)//2+1==77
assert (262-219)//2+1==(262-220)//2+1==22
assert 104+90-100==94
files=['SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','../audits/check_southwest_archive_import_independent.json','JOINT_RECORD_DROUGHT_MANIFEST.json','../audits/check_joint_record_drought_independent.json','DROUGHT_BOUNDARY_PINNING_MANIFEST.json','DROUGHT_BOUNDARY_ORIENTATION_ADDENDUM.json','../audits/check_drought_boundary_pinning_independent.json']
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR exact MT one-long-completed-gap inventory; audit pending',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},domain='all integer n>=100',initial_augmented_hull='[-1,2n+242]x[0,2n+241]',T_contact='21201+104n',T_records=records,T_internal_gap_max=3390,capture_cut='80270+208n',infinite_tail_record_classes={'W':'k>=77, phases90/100','N':'k>=n+22, phases43/57','E_S':'none'},unique_gap_over3390='58697+104n',affine_count=len(ineq),affine_sha256=hashlib.sha256(json.dumps(ineq,separators=(',',':')).encode()).hexdigest(),scope='Complete pristine augmented-hull records only. Initial wait before FIRST record is not a completed inter-record gap. Ordinary head records inside prepared field are excluded. No universal family or global bound.')
(P/'MT_COMPLETED_DROUGHT_INVENTORY_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print('all-n29 finite events +4 half-ray classes; exactly ONE completed gap>3390')
