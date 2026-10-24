from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'MT_COMPLETED_DROUGHT_INVENTORY_MANIFEST.json')=='ccf51906abe736062477ec93e694f7e3b17ab625e5b141f7f42be90bf880599c'
m=json.loads((D/'MT_COMPLETED_DROUGHT_INVENTORY_MANIFEST.json').read_text())
for kind in('files','dependencies'):
 for f,h in m[kind].items():assert sha(D/f)==h
q=R/'audits/check_phase13_double_scatter_independent.py';ns={'__file__':str(q)};exec(q.read_text().split('# Canonical source')[0],ns);K,xy,geometry,sim,cert=[ns[k]for k in('K','xy','geometry','sim','cert')]
A=json.loads((D/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());M=json.loads((D/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());J=json.loads((D/'MT_COMPLETED_DROUGHT_INVENTORY_CHECKED.json').read_text());W=sim(K,104)['word'];assert W==M['W'];d=2+2j;qm=202+201j
pre=W*100+W[:13]+M['modes']['M']['recovery_word'];P,_,pe,ph=geometry(0j,1,pre);fw=W[41:]+W[:41];F,_,_,_=geometry(pe,ph,fw)
T,_,te,th=geometry(0j,0,A['T_recovery']);SW,_,_,_=geometry(te,th,A['T_tail_word']);post,_,postend,posth=geometry(207+229j,1,A['postcollision_word']);NW=A['controls'][0]['complete_future_certificate']['tail_word'];Q,_,end,eh=geometry(postend,posth,NW)
assert postend==155+215j and posth==1 and end-postend==-d.conjugate()
# All-parameter affine endpoint inequalities, including complete old source and actual return.
checks=Counter()
def bound(p,ax,ay,upper,label):
 x,y=int(p.real),int(p.imag)
 for a,b in[(ax,x+1),(2-ax,upper[0]-x),(ay,y),(2-ay,upper[1]-y)]:assert a>=0 and 100*a+b>=0,(label,p,ax,ay,a,b);checks[label]+=1
for p in P+[pe]:bound(p,0,0,(242,241),'pre')
for p in F:bound(p,0,0,(242,241),'flightfirst');bound(p-d,2,2,(242,241),'flightlast')
for p in F[:77]:bound(p,2,2,(242,241),'flightpartial')
# T ray relative to qT=230+229i+2n(1+i); old E/N maxima are12/12.
mx=my=12;records=[]
for t,p in enumerate(T+[te]):
 if p.real>mx:assert p.real==mx+1;mx=p.real;records.append([t,1,int(mx)])
 if p.imag>my:assert p.imag==my+1;my=p.imag;records.append([t,0,int(my)])
 assert p.real+430>=-1 and p.imag+429>=0
assert records==J['T_records']and Counter(z[1]for z in records)=={0:21,1:8}and max(records[i+1][0]-records[i][0]for i in range(28))==3390
assert records[0][0]==1734 and records[-1]==[8470,0,33]
for p in SW:bound(230+229j+p,2,2,(250,262),'SWfirst');bound(246+245j+p,0,0,(250,262),'SWlast')
for p in SW[:101]:bound(244+243j+p,0,0,(250,262),'SWpartial')
for p in post+[postend]:bound(p,0,0,(250,262),'post')
dot=lambda p,a:[int(p.imag),int(p.real),-int(p.imag),-int(p.real)][a]
stable={};thresholds={}
for a in range(4):
 dv=dot(end-postend,a);vals=[dot(p,a)for p in Q];old=[462,450,0,1][a];assert max(vals)<=old
 if dv<=0:stable[a]=[];continue
 best=max(vals)-dv;got=[]
 for i,x in enumerate(vals):
  if x>best:got.append([i,x])
  best=max(best,x)
 stable[a]=got
 for i,x in got:
  # N's previous maximum is2n+262, W's is1.
  base=262 if a==0 else 1;k0=(base-x)//dv+1;thresholds[a,i]=(1 if a==0 else 0,k0)
assert stable=={0:[[43,219],[57,220]],1:[],2:[],3:[[90,-152],[100,-151]]}
assert thresholds=={(0,43):(1,22),(0,57):(1,22),(3,90):(0,77),(3,100):(0,77)}
controls=[]
for n in(100,137,500):
 qt=qm+(n+14)*d;seed=K|{qm+a*d for a in(0,1,6,8)}|{qt+a*d for a in(0,1,3,5,6)};assert(min(p.real for p in seed),max(p.real for p in seed),min(p.imag for p in seed),max(p.imag for p in seed))==(-1,2*n+242,0,2*n+241)
 e=80270+208*n;word=pre+fw*n+fw[:76]+A['T_recovery']+A['T_tail_word']*(n-7)+A['T_tail_word'][:100]+'L'+A['postcollision_word']+NW*(n+24);assert len(word)==e+104*(n+24)
 z=cert(sim(seed,len(word),expected=word),NW);hull=[max(dot(p,a)for p in seed|{0j})for a in range(4)];actual=[]
 for t,p in enumerate(z['pts']+[z['p']]):
  for a in range(4):
   x=dot(p,a)
   if x>hull[a]:assert x==hull[a]+1;hull[a]=x;actual.append([t,a])
 pred=[[21201+104*n+t,a]for t,a,x in records]
 for (a,i),(an,bn)in thresholds.items():
  for k in range(an*n+bn,n+25):
   t=e+104*k+i
   if t<=len(word):pred.append([t,a])
 pred.sort();assert actual==pred
 long=[actual[i+1][0]-actual[i][0]for i in range(len(actual)-1)if actual[i+1][0]-actual[i][0]>3390];assert long==[58697+104*n]
 controls.append(dict(n=n,full_original_reads=len(word),record_count=len(actual),unique_long_completed_gap=long[0],tail_parity_tests=z['tests']))
review=['The augmented hull includes every initial BLACK cell, so the all-n affine source/M and forward-flight bounds genuinely exclude all pre-T strict records; head-only records inside prepared input are not counted. T literal29 E/N records are parameter-independent after translation, and all return/recovery stages stay in their final historical hull.','For every positive-drift axis, the all104 phase comparison against the preceding period maximum lists every stable record phase, not only observed peaks. The initial full hull dominates the whole first tail period; negative/zero axes never record. Exact inequalities give W k>=77 at90/100 and N k>=n+22 at43/57.','The unique completed gap over3390 is58697+104n; all later W-only gaps are10/94, and adding N records only subdivides them. The possibly long initial wait is not an inter-record gap. K reset subwindows inside the pinned interval remain inside ONE completed drought, not a recurrence construction. All members capture.']
out=dict(status='PASS exact all-n MT one-long-completed-pristine-drought inventory',manifest=sha(D/'MT_COMPLETED_DROUGHT_INVENTORY_MANIFEST.json'),dependencies=m['dependencies'],affine_stages=checks,T_records=records,all104_tail_record_phases=stable,thresholds={str(k):v for k,v in thresholds.items()},controls=controls,analytic_review=review)
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
