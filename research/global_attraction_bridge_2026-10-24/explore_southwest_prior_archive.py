from pathlib import Path
import json
from check_return_permanent_output_debt import DXY,future
from certified_comparison_perturbation import reference,perturbation_event
P=Path(__file__).parent;j=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());K=set(map(tuple,j['canonical_source']));W=j['W'];Q=[];p=(0,0);h=1
for c in W:Q.append(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
T=set()
for i,(x,y)in enumerate(Q):
 x-=2;y-=1
 for a in range(-((y+15)//2),1 if i<13 else 0):T.symmetric_difference_update({(x+2*a,y+2*a)})
T|={(2*a,2*a)for a in[0,1,3,5,6]}
def run(B,p,h,N,expect=None):
 word=[];born={};reads=[]
 for t in range(N):
  reads.append(p);a=B.pop(p,None)
  if a is None:B[p]=t;born[t]=p;h=(h+1)%4;c='R'
  else:h=(h-1)%4;c='L'
  if expect is not None:assert c==expect[t]
  word.append(c);p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return B,p,h,''.join(word),born,reads
B,p,h,prefix,_,_=run({q:-i-1 for i,q in enumerate(sorted(T))},(0,0),0,11232);tw,dr,_,_=future(B,p,h);ref=reference(T,(0,0),0,prefix,tw);print('T kernel',len(T),'tail',p,h,dr,flush=True)
out=[]
for labels in['','S','M','MM','SM','MS','MMM']:
 seed=set(K);seq='';pos=(0,0);phase=0;origins=[]
 for lab in labels+'T':
  n=100;q=(pos[0]+2*(n+int(13<phase))+Q[13][0]-Q[phase][0],pos[1]+2*(n+int(13<phase))+Q[13][1]-Q[phase][1]);flight=(W[phase:]+W[:phase])*n+(W[phase:]+W[:phase])[:(13-phase)%104];seq+=flight
  inds=[0,1,3,5,6]if lab=='T'else j['modes'][lab]['packet_black_indices'];seed|={(q[0]+2*a,q[1]+2*a)for a in inds};origins.append((q,lab,len(seq)))
  if lab=='T':break
  mode=j['modes'][lab];seq+=mode['recovery_word'];pos=(q[0]+mode['output_pose'][0][0],q[1]+mode['output_pose'][0][1]);phase=mode['output_phase']
 B,p,h,word,born,reads=run({q:-i-1 for i,q in enumerate(sorted(seed))},(0,0),1,len(seq),seq);assert(p,h)==(q,0)
 rel={(x-q[0],y-q[1]):v for(x,y),v in B.items()};assert T<=set(rel);assert{v for v in rel if v[1]>=-15}==T
 event=perturbation_event(ref,set(rel)-T);summary={k:v for k,v in event.items()if k not in['new_full_field_terms','retained_unread_extra','remaining_original_extra','word']}
 if event['kind'].startswith('EXACT'):
  cell=tuple(event['cell']);identity=rel[cell];summary['actual_birth']=identity;summary['age_at_hit']=len(seq)+event['time']-identity;summary['birth_stage']=next((lab0 for(q0,lab0,t0),(q1,lab1,t1)in zip(origins,origins[1:])if t0<=identity<t1),'source/flight')
 print(labels or'base',summary,flush=True)
 out.append(dict(prior_modes=labels,seed=sorted(seed),origins=origins,contact=len(seq),complete_contact_black=[[v,i]for v,i in sorted(rel.items())],event=summary))
(P/'SOUTHWEST_PRIOR_ARCHIVE_EXPLORATORY.json').write_text(json.dumps(dict(status='UNSIGNED targeted finite probes',kernel=sorted(T),prefix=prefix,tail_word=tw,controls=out),indent=2)+'\n')
