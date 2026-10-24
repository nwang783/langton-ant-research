"""Only the verified first extra T ray port7. Bounded literal full-source probes."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
from certified_comparison_perturbation import geometry
P=Path(__file__).parent;R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());K=set(map(tuple,R['canonical_source']));W=R['W'];Q,_,_,_=geometry((0,0),1,W);PH={W[i:]+W[:i]for i in range(104)}
jobs=[('',[100]),('M',[100,100]),('SM',[100,111,100]),('MM',[100,100,100])];out=[]
for labels,gaps in jobs:
 seed=set(K);expected='';pos=(0,0);phase=0;packets=[]
 for lab,n in zip(labels+'T7',gaps):
  # iterate explicit modes, because T7 is one packet, not two letters
  pass
 for lab,n in zip(list(labels)+['T7'],gaps):
  q=(pos[0]+2*(n+int(13<phase))+Q[13][0]-Q[phase][0],pos[1]+2*(n+int(13<phase))+Q[13][1]-Q[phase][1]);fw=W[phase:]+W[:phase];expected+=fw*n+fw[:(13-phase)%104]
  inds=[0,1,3,5,6,7]if lab=='T7'else R['modes'][lab]['packet_black_indices'];bits={(q[0]+2*a,q[1]+2*a)for a in inds};assert not(seed&bits);seed|=bits;packets.append(dict(mode=lab,origin=q,time=len(expected),indices=inds))
  if lab=='T7':break
  m=R['modes'][lab];expected+=m['recovery_word'];pos=(q[0]+m['output_pose'][0][0],q[1]+m['output_pose'][0][1]);phase=m['output_phase']
 tT=len(expected);qT=q;expected+=A['T_recovery'][:6044]+'L';B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;words=[];death={};birth={};snap={};first={};result=None;readbox=[0,0,0,0]
 for t in range(tT+200000):
  if t==tT:snap=dict(B)
  first.setdefault(p,t);old=B.pop(p,None)
  if old is None:B[p]=t;birth[t]=p;h=(h+1)%4;c='R'
  else:death[old]=t;h=(h-1)%4;c='L'
  if t<len(expected):assert c==expected[t]
  words.append(c)
  if t>=tT:
   x=p[0]-qT[0];y=p[1]-qT[1];readbox=[min(readbox[0],x),max(readbox[1],x),min(readbox[2],y),max(readbox[3],y)]
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1]);N=t+1
  if N>tT+312 and(N-tT)%104==0:
   recent=''.join(words[-104:])
   if recent in PH and ''.join(words[-312:])==recent*3:
    try:fw,dr,dead,tests=future(B,p,h)
    except AssertionError:continue
    if fw not in PH:continue
    death.update({i:N+tt for i,tt in dead.items()});result=dict(kind='CERTIFIED full future',cut=N,post_T_reads=N-tT,pose=[p,h],drift=dr,tail_word=fw,tests=tests);break
 if result is None:result=dict(kind='UNKNOWN fixed200000post-T budget',cut=len(words),pose=[p,h])
 relevant={q for q,i in snap.items()if i in death};imports=[]
 for a in packets:
  if a['mode']=='M':
   deaths=[dict(cell=q,birth=i,death=death[i])for q,i in snap.items()if a['time']<=i<a['time']+10712 and i in death]
   imports.append(dict(M_origin=a['origin'],M_contact=a['time'],actual_future_inputs_from_M_body=len(deaths),marked_R9752_death=death.get(a['time']+9752),cells=deaths))
 rec=dict(prior_modes=labels,gaps=gaps,seed=sorted(seed),packets=packets,T_contact=tT,T_full_field=[[q,i]for q,i in sorted(snap.items())],T_first_extra_read=first[(qT[0]+14,qT[1]+14)],complete_prefix_word=''.join(words),post_T_prefix_sha256=hashlib.sha256(''.join(words[tT:]).encode()).hexdigest(),complete_current_field=[[q,i]for q,i in sorted(B.items())],post_T_readbox=readbox,result=result,imports=imports,T_relevant_known=sorted(relevant),relevance_complete=result['kind'].startswith('CERTIFIED'))
 out.append(rec);print(labels or'pure',result,'imports',[(x['actual_future_inputs_from_M_body'],x['marked_R9752_death'])for x in imports],flush=True)
(P/'T_PORT7_FULL_ARCHIVE_EXPLORATORY.json').write_text(json.dumps(dict(status='UNSIGNED bounded full-source branch probes, no all-word inference',budget=200000,controls=out),indent=2)+'\n')
