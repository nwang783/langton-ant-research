from pathlib import Path
import json,itertools,hashlib
from check_return_permanent_output_debt import DXY,rot,future
P=Path(__file__).parent;G={(0,-1),(1,1),(1,3),(2,2)}
B=set(G);p=(0,0);h=1;Q=[];Qh=[];A='';U=''
for t in range(286):
 if t>=182:Q.append(p);Qh.append(h)
 old=p in B
 if old:B.remove(p);h=(h-1)%4
 else:B.add(p);h=(h+1)%4
 if t<182:A+='L' if old else 'R'
 else:U+='L' if old else 'R'
 p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
phases={U[i:]+U[:i] for i in range(104)}
records=[]
for joins in itertools.product([61,71],repeat=3):
 n=20;r=[7*n//2-4,n-5,2*n-6];poses=[((0,0),1)]
 for i,j in enumerate(joins):
  o,hh=poses[-1];q=rot((Q[j][0]+2*r[i],Q[j][1]+2*r[i]),hh-1);poses.append(((o[0]+q[0],o[1]+q[1]),(Qh[j]+hh-1)%4))
 seed={(o[0]+rot(g,hh-1)[0],o[1]+rot(g,hh-1)[1]) for o,hh in poses for g in G};assert len(seed)==16
 expected=''.join(A+U*r[i]+U[:j] for i,j in enumerate(joins));T=len(expected);B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;history='';first={};mis=None;contact=None;initcontact=None
 for t in range(T+200000):
  if p in seed and p not in first:first[p]=t
  want=expected[t] if t<T else (A[t-T] if t<T+182 else U[(t-T-182)%104])
  ch='L' if p in B else 'R'
  if mis is None and ch!=want:
   mis=dict(time=t,relative_last=t-T,cell=p,heading=h,wanted=want,actual=ch,lifetime=B.get(p));contact=dict(B);initcontact=(p,h)
   if t<T:break
  old=B.pop(p,None)
  if old is None:B[p]=t;h=(h+1)%4
  else:h=(h-1)%4
  history+=ch;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
  if mis and t>mis['time']+312 and (t-mis['time'])%104==0 and history[-104:] in phases and history[-312:]==history[-104:]*3:
   try:w,dr,death,tests=future(B,p,h)
   except AssertionError:continue
   lastmis=t
   while lastmis>=0 and history[lastmis]==w[(lastmis-(t+1))%104]:lastmis-=1
   d=dict(joins=joins,n=n,poses=poses,seed=sorted(seed),first_contact=mis,source_prefix_preserved=mis['time']>=T,last_port_entry=T,exact_onset=lastmis+1,certification_cut=t+1,tail_pose=[p,h],tail_drift=dr,tail_word=w,terminal_black_count=len(B),contact_full_black=[dict(cell=q,lifetime=i) for q,i in sorted(contact.items())],contact_future_word=history[mis['time']:lastmis+1],all_initial_first_reads=[dict(cell=q,time=first.get(q))for q in sorted(seed)],full_terminal_black=[dict(cell=q,lifetime=i)for q,i in sorted(B.items())]);records.append(d)
   print(json.dumps({k:v for k,v in d.items() if k not in ['seed','contact_full_black','contact_future_word','tail_word','full_terminal_black','all_initial_first_reads']}),flush=True);break
 else:records.append(dict(joins=joins,n=n,poses=poses,first_contact=mis,status='UNKNOWN no certified tail in bounded budget'))
 if mis and mis['time']<T:
  records.append(dict(joins=joins,n=n,poses=poses,first_contact=mis,status='PREFIX MISMATCH'));print(records[-1],flush=True)
(P/'TRANSVERSE_JOIN_QUOTIENT_PROBES.json').write_text(json.dumps(dict(status='AUTHOR eight finite causal join probes, no universal quotient claim',records=records),indent=2)+'\n')
