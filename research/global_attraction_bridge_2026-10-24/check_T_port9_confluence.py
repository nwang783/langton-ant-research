"""Exact T9 confluence and complete single-extra forward-ray-bit cover."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
from certified_comparison_perturbation import geometry
P=Path(__file__).parent;R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());K=set(map(tuple,R['canonical_source']));W=R['W'];Q,_,_,_=geometry((0,0),1,W);Tword=(P/'T_PORT9_RECOVERY_WORD.txt').read_text().strip();TW=W[85:]+W[:85];post=A['postcollision_word'];base=A['controls'][0];baseM=(202,201)
baseQ={(x-baseM[0],y-baseM[1])for x,y in base['whole_post_event_black']if x<=baseM[0]+38 and y>=baseM[1]-43}
remote={(x-baseM[0],y-baseM[1])for x,y in A['exact_entry_pruning']['remote']};local=set(map(tuple,A['exact_entry_pruning']['local']))|{(18,18)};Tkernel=set(map(tuple,A['T_kernel']))|{(18,18)}
def run(seed,p,h,w,cuts=()):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};death={};states={};first={};reads=[]
 for t,c in enumerate(w):
  if t in cuts:states[t]=(dict(B),p,h)
  first.setdefault(p,t);reads.append(p);old=B.pop(p,None);assert(c=='L')==(old is not None)
  if old is None:B[p]=t;h=(h+1)%4
  else:death[old]=t;h=(h-1)%4
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return dict(B=B,p=p,h=h,death=death,states=states,first=first,reads=reads)
# Exact finite confluence at6600 versus6516, both after the exposed port9.
from certified_comparison_perturbation import reference,first_hit
assert Tword[6600:]==A['T_recovery'][6516:]+A['T_tail_word'][:20]
assert len(Tword)==11336 and Tword[:6496]==A['T_recovery'][:6496]and Tword[6496]=='L'and A['T_recovery'][6496]=='R'
zt=run(set(map(tuple,A['T_kernel'])),(0,0),0,A['T_recovery'][:6516]);z9=run(Tkernel,(0,0),0,Tword[:6600]);assert(zt['p'],zt['h'])==(z9['p'],z9['h'])
patch=set(zt['B'])^set(z9['B']);assert len(patch)==23 and min(x for x,y in patch)==14 and max(x for x,y in patch)==21 and min(y for x,y in patch)==15 and max(y for x,y in patch)==22
oldref=reference(set(zt['B']),zt['p'],zt['h'],A['T_recovery'][6516:],A['T_tail_word']);assert first_hit(oldref,patch)is None
added=set(z9['B'])-set(zt['B']);removed=set(zt['B'])-set(z9['B']);assert len(added)==18 and len(removed)==5
pure9=run(Tkernel,(0,0),0,Tword);assert min(y for x,y in pure9['reads'])==-15
fw9,dr9,die9,test9=future(pure9['B'],pure9['p'],pure9['h']);assert fw9==TW and dr9==(-2,-2)and(pure9['p'],pure9['h'])==((-34,-10),2)
f9=dict(pure9['death']);f9.update({i:len(Tword)+tt for i,tt in die9.items()});assert{q for i,q in enumerate(sorted(Tkernel))if -i-1 in f9}==local
first9={}
for t,(x,y)in enumerate(pure9['reads']):
 if x==y and x>=0 and x%2==0:first9.setdefault(x//2,t)
assert sorted(first9)==list(range(11)) and first9[10]==6540
QQ,_,_,_=geometry(pure9['p'],pure9['h'],TW);assert all(x!=y for x,y in QQ)
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
  indices=[0,1,3,5,6,9]if lab=='T'else R['modes'][lab]['packet_black_indices'];bits={(q[0]+2*a,q[1]+2*a)for a in indices};assert not(seed&bits);seed|=bits;packets.append(dict(mode=('T9'if lab=='T'else lab),origin=q,time=len(word),indices=indices))
  if lab=='T':break
  mm=R['modes'][lab];word+=mm['recovery_word'];pos=(q[0]+mm['output_pose'][0][0],q[1]+mm['output_pose'][0][1]);phase=mm['output_phase']
 tT=len(word);qT=q;word+=Tword;lastM=next((a for a in reversed(packets)if a['mode']=='M'),None);event=None
 if lastM:
  qM=lastM['origin'];D=(qT[0]-qM[0])//2;assert qT[1]-qM[1]==2*D and D>=114
  word+=TW*(D-21)+TW[:80];event=len(word);assert event-tT==104*D+9232;word+='L';postcut=len(word);word+=post
 z=run(seed,(0,0),1,word,[tT]+([event,event+1]if event is not None else[]));fw,dr,dead,tests=future(z['B'],z['p'],z['h']);fates=dict(z['death']);fates.update({i:len(word)+tt for i,tt in dead.items()})
 B,p,h=z['states'][tT];assert(p,h)==(qT,0);assert{(x-qT[0],y-qT[1])for x,y in B if y>=qT[1]-15}==Tkernel
 for a in packets:
  assert all(z['first'][(a['origin'][0]+2*k,a['origin'][1]+2*k)]>=a['time']for k in a['indices'])
 C={q for q,i in B.items()if i in fates};expect={(qT[0]+x,qT[1]+y)for x,y in local}
 if lastM:
  expect|={(qM[0]+x,qM[1]+y)for x,y in remote};assert C==expect and len(C)==886
  bb,pp,hh=z['states'][event+1];inside={(x-qM[0],y-qM[1])for x,y in bb if x<=qM[0]+38 and y>=qM[1]-43};assert inside==baseQ
  before,pp,hh=z['states'][event];hit=(qM[0]+4,qM[1]+28);assert(pp,hh)==(hit,2)and before[hit]==lastM['time']+9752
  assert z['death'][lastM['time']+9752]==event and(z['p'],z['h'],dr)==((qM[0]-47,qM[1]+14),1,(-2,2))and fw==base['complete_future_certificate']['tail_word']
  rho=max(max(abs(x-qT[0]),abs(y-qT[1]))for x,y in C);assert rho==2*D+44
 else:
  assert C==expect and len(C)==100 and fw==TW and dr==(-2,-2);rho=18;inside=None
 controls.append(dict(prior_modes=labels,gaps=gaps,seed=sorted(seed),packets=packets,T_contact=tT,T_full_black=[[q,i]for q,i in sorted(B.items())],T_entire_pruning=sorted(C),T_entire_radius=rho,marked_event=event,last_M=lastM,event_full_black=sorted(z['states'][event][0])if lastM else None,post_event_quadrant=sorted(inside)if lastM else None,complete_word=word,terminal_cut=len(word),terminal_pose=[z['p'],z['h']],terminal_full_black=sorted(z['B']),tail_word=fw,tail_drift=dr,parity_tests=tests))
 print(labels+'T9','reads',len(word),'C',len(C),'rho',rho,'event',event,flush=True)
files=['RECURSIVE_PHASE13_PACKET_MANIFEST.json','SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','RECURSIVE_PHASE13_PACKET_CHECKED.json','SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json','check_return_permanent_output_debt.py','T_PORT9_RECOVERY_WORD.txt','LAST_M_REGISTER_SCATTERING_MANIFEST.json','../audits/check_last_M_register_scattering_independent.json','T_PORT7_ABSORBER_MANIFEST.json','T_PORT8_ABSORBER_MANIFEST.json','T_TERMINAL_RAY_EXPOSURE_MANIFEST.json','../audits/check_T_port7_absorber_independent.json','../audits/check_T_port8_absorber_independent.json','../audits/check_T_ray_exposure_independent.json']
out=dict(status='AUTHOR exact T9 confluence and single-extra forward-bit cover; independent audit pending',scope='Finite protected S/M prefix then T plus at most one extra BLACK at index>=7; lower WHITE2/4 fixed; no arbitrary multiple near inputs.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},registered_quadrant=sorted(baseQ),quadrant_bounds=dict(max_x=38,min_y=-43),last_NE_quadrant_read=max(t for t,q in Qtail),all_NE_quadrant_reads=Qtail,confluence=dict(T_cut=6516,T9_cut=6600,pose=[zt['p'],zt['h']],complete_T_field=sorted(zt['B']),complete_T9_field=sorted(z9['B']),patch=sorted(patch),added=sorted(added),removed=sorted(removed),entire_T_future_patch_hit=None),T9_kernel=sorted(Tkernel),T9_word=Tword,T9_output_black=sorted(pure9['B']),T9_output_pose=[pure9['p'],pure9['h']],T9_tail_word=TW,T9_parity_tests=test9,T9_ray_first_reads=sorted(first9.items()),local_T9_pruning=sorted(local),remote_last_M_pruning=sorted(remote),controls=controls)
(P/'T_PORT9_CONFLUENCE_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
