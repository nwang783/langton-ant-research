"""Complete southern capture guard for exactly the first exposed T port7 branch."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
from certified_comparison_perturbation import geometry
P=Path(__file__).parent;R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());K=set(map(tuple,R['canonical_source']));W=R['W'];Q,_,_,_=geometry((0,0),1,W);word=(P/'T_PORT7_RECOVERY_WORD.txt').read_text().strip();assert len(word)==37440 and word[:6044]==A['T_recovery'][:6044]and word[6044]=='L'and A['T_recovery'][6044]=='R'
B=set()
for i,(x,y)in enumerate(Q):
 x-=2;y-=1
 for a in range(-((y+27)//2),1 if i<13 else 0):B.symmetric_difference_update({(x+2*a,y+2*a)})
packet={(2*a,2*a)for a in[0,1,3,5,6,7]};assert not B&packet;kernel=B|packet
def run(seed,p,h,word,cuts=()):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};death={};first={};reads=[];snap={}
 for t,c in enumerate(word):
  if t in cuts:snap[t]=(dict(B),p,h)
  first.setdefault(p,t);reads.append(p);old=B.pop(p,None);assert(c=='L')==(old is not None)
  if old is None:B[p]=t;h=(h+1)%4
  else:death[old]=t;h=(h-1)%4
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 fw,dr,dead,tests=future(B,p,h);death.update({i:len(word)+tt for i,tt in dead.items()});return dict(B=B,p=p,h=h,death=death,first=first,reads=reads,snap=snap,tail=fw,drift=dr,tests=tests)
z=run(kernel,(0,0),0,word);assert(z['p'],z['h'],z['drift'])==((-32,34),2,(-2,2));tailQ,_,_,_=geometry(z['p'],z['h'],z['tail']);assert min(y for x,y in z['reads']+tailQ)==-27
C={q for i,q in enumerate(sorted(kernel))if -i-1 in z['death']};assert len(C)==157 and z['first'][(14,14)]==6044
assert all((2*a,2*a)not in z['first']or z['first'][(2*a,2*a)]>=0 for a in[0,1,3,5,6,7])
# All complete predecessor fields and omitted synthetic past are below the new guard.
interfaces=[]
for label,m in R['modes'].items():
 phase=m['output_phase'];v=tuple(m['output_pose'][0]);nextdelta=206 if label=='S'else 228
 actualmax=max(y for x,y in m['complete_output_black']);synthetic=max(v[1]+Q[i][1]-Q[phase][1]+(0 if i<phase else-2)for i in range(104));assert actualmax<=31 and synthetic<=31
 guard=nextdelta-27;assert guard>max(actualmax,synthetic)
 interfaces.append(dict(previous=label,minimum_origin_increment=nextdelta,new_southern_boundary=guard,previous_full_output_max_y=actualmax,omitted_synthetic_max_y=synthetic,strict_slack=guard-max(actualmax,synthetic)))
controls=[]
for labels,gaps in[('',[100]),('M',[100,100]),('SM',[100,111,100]),('MM',[100,100,100]),('MSMS',[101,137,100,104,101])]:
 seed=set(K);seq='';pos=(0,0);phase=0;packets=[]
 for label,n in zip(list(labels)+['T7'],gaps):
  q=(pos[0]+2*(n+int(13<phase))+Q[13][0]-Q[phase][0],pos[1]+2*(n+int(13<phase))+Q[13][1]-Q[phase][1]);fw=W[phase:]+W[:phase];seq+=fw*n+fw[:(13-phase)%104]
  inds=[0,1,3,5,6,7]if label=='T7'else R['modes'][label]['packet_black_indices'];bits={(q[0]+2*a,q[1]+2*a)for a in inds};assert not bits&seed;seed|=bits;packets.append(dict(mode=label,origin=q,time=len(seq),indices=inds))
  if label=='T7':break
  mm=R['modes'][label];seq+=mm['recovery_word'];pos=(q[0]+mm['output_pose'][0][0],q[1]+mm['output_pose'][0][1]);phase=mm['output_phase']
 t=len(seq);seq+=word;a=run(seed,(0,0),1,seq,[t]);field,p,h=a['snap'][t];assert(p,h)==(q,0)
 inside={(x-q[0],y-q[1])for x,y in field if y>=q[1]-27};assert inside==kernel
 actualC={r for r,i in field.items()if i in a['death']};expect={(q[0]+x,q[1]+y)for x,y in C};assert actualC==expect
 for m in packets:
  for k in m['indices']:assert a['first'][(m['origin'][0]+2*k,m['origin'][1]+2*k)]>=m['time']
  if m['mode']=='M':assert m['time']+9752 not in a['death'];assert all(not(m['time']<=i<m['time']+10712)for r,i in field.items()if i in a['death'])
 assert a['first'][(q[0]+14,q[1]+14)]==t+6044 and a['tail']==z['tail']and a['drift']==(-2,2)
 controls.append(dict(prefix=labels,gaps=gaps,seed=sorted(seed),packets=packets,entry=t,entry_full_black=[[q,i]for q,i in sorted(field.items())],entry_entire_pruning=sorted(actualC),complete_word_sha256=hashlib.sha256(seq.encode()).hexdigest(),terminal_cut=len(seq),terminal_pose=[a['p'],a['h']],terminal_full_black=sorted(a['B']),tail_word=a['tail'],tail_drift=a['drift'],parity_tests=a['tests']))
 print(labels+'T7',len(seed),len(seq),'true input',len(actualC),flush=True)
oldlocal=set(map(tuple,A['exact_entry_pruning']['local']));files=['RECURSIVE_PHASE13_PACKET_MANIFEST.json','../audits/check_recursive_phase13_packet_independent.json','SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','../audits/check_southwest_archive_import_independent.json','T_PORT7_RECOVERY_WORD.txt','check_return_permanent_output_debt.py']
out=dict(status='AUTHOR all-prefix T7 absorbing guard; independent audit pending',scope='All protected finite S/M prefixes then exactly T7, gaps>=100; arbitrary archive below current southern guard safe, arbitrary initial western archive NOT covered.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},kernel=sorted(kernel),packet=sorted(packet),whole_comparison_pruning=sorted(C),local_radius=max(max(abs(x),abs(y))for x,y in C),word=word,output_full_black=sorted(z['B']),output_pose=[z['p'],z['h']],tail_word=z['tail'],tail_drift=z['drift'],infinite_parity_tests=z['tests'],initial_first_reads=[dict(cell=q,time=z['first'].get(q))for q in sorted(kernel)],initial_consumption_fates=[dict(cell=q,time=z['death'].get(-i-1))for i,q in enumerate(sorted(kernel))],interfaces=interfaces,contrast=dict(T_local_count=len(oldlocal),T7_local_count=len(C),shared_local_count=len(C&oldlocal),T_only_local=sorted(oldlocal-C),T7_only_local=sorted(C-oldlocal),T_remote_count=786,T7_remote_count=0),controls=controls)
(P/'T_PORT7_ABSORBER_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
