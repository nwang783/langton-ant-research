"""Exact last-M register interface for finite protected S/M prefixes, then T."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
from certified_comparison_perturbation import geometry
P=Path(__file__).parent;R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());K=set(map(tuple,R['canonical_source']));W=R['W'];Q,_,_,_=geometry((0,0),1,W);Tword=A['T_recovery'];TW=A['T_tail_word'];post=A['postcollision_word'];base=A['controls'][0];baseM=(202,201)
baseQ={(x-baseM[0],y-baseM[1])for x,y in base['whole_post_event_black']if x<=baseM[0]+38 and y>=baseM[1]-43}
remote={(x-baseM[0],y-baseM[1])for x,y in A['exact_entry_pruning']['remote']};local=set(map(tuple,A['exact_entry_pruning']['local']));Tkernel=set(map(tuple,A['T_kernel']))
def run(seed,p,h,w,cuts=()):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};death={};states={};first={};reads=[]
 for t,c in enumerate(w):
  if t in cuts:states[t]=(dict(B),p,h)
  first.setdefault(p,t);reads.append(p);old=B.pop(p,None);assert(c=='L')==(old is not None)
  if old is None:B[p]=t;h=(h+1)%4
  else:death[old]=t;h=(h-1)%4
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return dict(B=B,p=p,h=h,death=death,states=states,first=first,reads=reads)
# Finite geometric premises for arbitrary protected prefixes and suffixes.
for name,m in R['modes'].items():
 B=set(map(tuple,m['complete_output_black']));assert max(y for x,y in B)<=31
 if name=='S':assert all(-8<=x-y<=4 for x,y in B)
 assert min(x for x,y in geometry(tuple(m['output_pose'][0]),m['output_pose'][1],m['tail_word'])[0])>=-23
m=R['modes']['M'];flightQ,_,_,_=geometry(tuple(m['output_pose'][0]),m['output_pose'][1],m['tail_word']);Qtail=[]
for i,q in enumerate(flightQ):
 for k in range(100):
  z=(q[0]+2*k,q[1]+2*k)
  if z[0]<=38 and z[1]>=-43:Qtail.append((104*k+i,z))
 assert q[0]+200>38
assert max(t for t,q in Qtail)<104*100
pr,_,_,_=geometry((5,28),1,post);tq,_,_,_=geometry((-47,14),1,base['complete_future_certificate']['tail_word']);assert max(x for x,y in pr+tq)==38 and min(y for x,y in pr+tq)==-43
controls=[]
jobs=[('',[100]),('SS',[100,101,137]),('M',[100,100]),('MS',[100,100,100]),('SMMSS',[101,137,100,101,110,100]),('MSMSM',[100,101,100,137,100,105])]
for labels,gaps in jobs:
 seed=set(K);word='';pos=(0,0);phase=0;packets=[]
 for lab,n in zip(labels+'T',gaps):
  q=(pos[0]+2*(n+int(13<phase))+Q[13][0]-Q[phase][0],pos[1]+2*(n+int(13<phase))+Q[13][1]-Q[phase][1]);word+=(W[phase:]+W[:phase])*n+(W[phase:]+W[:phase])[:(13-phase)%104]
  indices=[0,1,3,5,6]if lab=='T'else R['modes'][lab]['packet_black_indices'];bits={(q[0]+2*a,q[1]+2*a)for a in indices};assert not(seed&bits);seed|=bits;packets.append(dict(mode=lab,origin=q,time=len(word),indices=indices))
  if lab=='T':break
  mm=R['modes'][lab];word+=mm['recovery_word'];pos=(q[0]+mm['output_pose'][0][0],q[1]+mm['output_pose'][0][1]);phase=mm['output_phase']
 tT=len(word);qT=q;word+=Tword;lastM=next((a for a in reversed(packets)if a['mode']=='M'),None);event=None
 if lastM:
  qM=lastM['origin'];D=(qT[0]-qM[0])//2;assert qT[1]-qM[1]==2*D and D>=114
  word+=TW*(D-21)+TW[:100];event=len(word);assert event-tT==104*D+9148;word+='L';postcut=len(word);word+=post
 z=run(seed,(0,0),1,word,[tT]+([event,event+1]if event is not None else[]));fw,dr,dead,tests=future(z['B'],z['p'],z['h']);fates=dict(z['death']);fates.update({i:len(word)+tt for i,tt in dead.items()})
 B,p,h=z['states'][tT];assert(p,h)==(qT,0);assert{(x-qT[0],y-qT[1])for x,y in B if y>=qT[1]-15}==Tkernel
 for a in packets:
  assert all(z['first'][(a['origin'][0]+2*k,a['origin'][1]+2*k)]>=a['time']for k in a['indices'])
 C={q for q,i in B.items()if i in fates};expect={(qT[0]+x,qT[1]+y)for x,y in local}
 if lastM:
  expect|={(qM[0]+x,qM[1]+y)for x,y in remote};assert C==expect and len(C)==885
  bb,pp,hh=z['states'][event+1];inside={(x-qM[0],y-qM[1])for x,y in bb if x<=qM[0]+38 and y>=qM[1]-43};assert inside==baseQ
  before,pp,hh=z['states'][event];hit=(qM[0]+4,qM[1]+28);assert(pp,hh)==(hit,2)and before[hit]==lastM['time']+9752
  assert z['death'][lastM['time']+9752]==event and(z['p'],z['h'],dr)==((qM[0]-47,qM[1]+14),1,(-2,2))and fw==base['complete_future_certificate']['tail_word']
  rho=max(max(abs(x-qT[0]),abs(y-qT[1]))for x,y in C);assert rho==2*D+44
 else:
  assert C==expect and len(C)==99 and fw==TW and dr==(-2,-2);rho=18;inside=None
 controls.append(dict(prior_modes=labels,gaps=gaps,seed=sorted(seed),packets=packets,T_contact=tT,T_full_black=[[q,i]for q,i in sorted(B.items())],T_entire_pruning=sorted(C),T_entire_radius=rho,marked_event=event,last_M=lastM,event_full_black=sorted(z['states'][event][0])if lastM else None,post_event_quadrant=sorted(inside)if lastM else None,complete_word=word,terminal_cut=len(word),terminal_pose=[z['p'],z['h']],terminal_full_black=sorted(z['B']),tail_word=fw,tail_drift=dr,parity_tests=tests))
 print(labels+'T','reads',len(word),'C',len(C),'rho',rho,'event',event,flush=True)
files=['RECURSIVE_PHASE13_PACKET_MANIFEST.json','SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','RECURSIVE_PHASE13_PACKET_CHECKED.json','SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json','check_return_permanent_output_debt.py']
out=dict(status='AUTHOR all-word one-register theorem; independent audit pending',scope='Finite S/M prefix with gaps>=100, followed by T; no arbitrary western archive or infinite supplied train.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},registered_quadrant=sorted(baseQ),quadrant_bounds=dict(max_x=38,min_y=-43),last_NE_quadrant_read=max(t for t,q in Qtail),all_NE_quadrant_reads=Qtail,local_T_pruning=sorted(local),remote_last_M_pruning=sorted(remote),controls=controls)
(P/'LAST_M_REGISTER_SCATTERING_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
