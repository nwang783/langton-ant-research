"""A strict pristine historical record with all ORIGINAL inputs retired but remote self-written debt."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
from certified_comparison_perturbation import geometry
P=Path(__file__).parent;R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());K=set(map(tuple,R['canonical_source']));W=R['W'];Q,_,_,_=geometry((0,0),1,W);qm=(202,201);tm=10413;r=6009;relative_head=(13,10);remote=set(map(tuple,A['exact_entry_pruning']['remote']))
def replay(seed,p,h,word,snapcuts=()):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};death={};snap={};first={};initial_deaths=[];historical=[p[0],p[0],p[1],p[1]];records=[]
 for t,c in enumerate(word):
  fresh=[i for i,v in enumerate([p[0],p[0],p[1],p[1]])if (v<historical[i]if i%2==0 else v>historical[i])]
  if fresh:records.append(dict(time=t,pose=[p,h],normals=fresh))
  if t in snapcuts:snap[t]=dict(B=dict(B),p=p,h=h,strict_records=fresh,past_extrema=list(historical))
  historical=[min(historical[0],p[0]),max(historical[1],p[0]),min(historical[2],p[1]),max(historical[3],p[1])]
  first.setdefault(p,t);old=B.pop(p,None);assert(c=='L')==(old is not None)
  if old is None:B[p]=t;h=(h+1)%4
  else:
   death[old]=t;h=(h-1)%4
   if old<0:initial_deaths.append((old,t))
  p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 fw,dr,tail,tests=future(B,p,h);death.update({i:len(word)+tt for i,tt in tail.items()});return dict(B=B,p=p,h=h,death=death,snap=snap,first=first,initial_deaths=initial_deaths,records=records,tail_word=fw,drift=dr,tests=tests)
# Local comparison at the record, with its COMPLETE infinite future.
tref=replay(set(map(tuple,A['T_kernel'])),(0,0),0,A['T_recovery'],[r,6942]);st=tref['snap'][r];assert(st['p'],st['h'])==(relative_head,1)and st['strict_records']==[1]and st['past_extrema'][1]==12
local={q for q,i in st['B'].items()if i in tref['death']};assert all(x<13 for x,y in st['B'])
local_radius=max(max(abs(x-13),abs(y-10))for x,y in local)
assert max(y for x,y in st['B'])<=33 and min(x for x,y in st['B'])>=-38
north=tref['snap'][6942];assert(north['p'],north['h'])==((3,21),0)and north['strict_records']==[3]and north['past_extrema'][3]==20
localN={q for q,i in north['B'].items()if i in tref['death']};assert all(y<21 for x,y in north['B'])
controls=[]
for n in[100,137,500]:
 qt=(qm[0]+2*n+28,qm[1]+2*n+28);seed=K|{(qm[0]+2*a,qm[1]+2*a)for a in[0,1,6,8]}|{(qt[0]+2*a,qt[1]+2*a)for a in[0,1,3,5,6]};assert len(seed)==22
 pre=W*100+W[:13]+R['modes']['M']['recovery_word']+(W[41:]+W[:41])*n+(W[41:]+W[:41])[:76];tT=len(pre);t0=tT+r;last=tT+6000
 word=pre+A['T_recovery']+A['T_tail_word']*(n-7)+A['T_tail_word'][:100]+'L'+A['postcollision_word'];z=replay(seed,(0,0),1,word,[t0,tT+6942]);s=z['snap'][t0];p=s['p'];B=s['B'];assert(p,s['h'])==((qt[0]+13,qt[1]+10),1)
 assert s['strict_records']==[1]and s['past_extrema'][1]==p[0]-1 and max(x for x,y in seed)==p[0]-1
 assert not any(x>=p[0]for x,y in B)and all(i>=0 for i in B.values())
 assert len(z['initial_deaths'])==22 and max(t for i,t in z['initial_deaths'])==last
 first_after=next(a for a in z['records']if a['time']>=last+1);assert first_after['time']==t0
 C={q for q,i in B.items()if i in z['death']};expect={(qt[0]+x,qt[1]+y)for x,y in local}|remote;assert C==expect
 rho=max(max(abs(x-p[0]),abs(y-p[1]))for x,y in C);assert rho==2*n+85
 mark=(qm[0]+4,qm[1]+28);assert B[mark]==tm+9752 and z['death'][tm+9752]==tT+104*n+10604
 assert t0-(tm+9752)==104*n+7045 and z['death'][tm+9752]-t0==104*n+4595
 sn=z['snap'][tT+6942];pn=sn['p'];bn=sn['B'];assert(pn,sn['h'])==((qt[0]+3,qt[1]+21),0)and sn['strict_records']==[3]
 assert not any(y>=pn[1]for x,y in bn)and max(y for x,y in seed)<pn[1]
 assert next(a for a in z['records']if a['time']>=last+1 and 3 in a['normals'])['time']==tT+6942
 Cn={q for q,i in bn.items()if i in z['death']};assert Cn=={(qt[0]+x,qt[1]+y)for x,y in localN}|remote
 nr=max(max(abs(x-pn[0]),abs(y-pn[1]))for x,y in Cn);assert nr==2*n+88
 controls.append(dict(n=n,seed=sorted(seed),T_contact=tT,original_retirement_update=last,record_cut=t0,record_pose=[p,1],past_head_extrema=s['past_extrema'],initial_max_x=max(x for x,y in seed),first_record_after_retirement=first_after,whole_current_black=[[q,i]for q,i in sorted(B.items())],entire_current_pruning=sorted(C),pruning_mass=len(C),rho=rho,marked_input=dict(cell=mark,birth=tm+9752,death=z['death'][tm+9752],elapsed_age=104*n+7045,remaining_wait=104*n+4595),north_record=dict(time=tT+6942,pose=[pn,0],past_extrema=sn['past_extrema'],whole_black=[[q,i]for q,i in sorted(bn.items())],entire_pruning=sorted(Cn),relevant_mass=len(Cn),rho=nr),all_original_consumptions=sorted(z['initial_deaths']),terminal_cut=len(word),terminal_pose=[z['p'],z['h']],terminal_full_black=sorted(z['B']),tail_word=z['tail_word'],tail_drift=z['drift'],infinite_parity_tests=z['tests']))
 print('n',n,'retired',last,'first pristine record',t0,'C',len(C),'rho',rho,flush=True)
# The normalized TRUE-pruned fields have a finite local limit; the remote cluster escapes SW.
local_normalized={(x-13,y-10)for x,y in local};lim=replay(local_normalized,(0,0),1,A['T_recovery'][r:]);assert lim['tail_word']==A['T_tail_word']and lim['drift']==(-2,-2)
files=['SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','../audits/check_southwest_archive_import_independent.json','RECURSIVE_PHASE13_PACKET_MANIFEST.json','check_return_permanent_output_debt.py']
out=dict(status='AUTHOR all-n pristine-record compactness countercontrol; independent audit pending',scope='Uniform across-family next-record mechanism only; no counterexample to eventual compact recurrence in one finite orbit.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},relative_record_cut=r,relative_record_pose=[relative_head,1],local_record_pruning=sorted(local),local_mass=len(local),local_radius=local_radius,remote_pruning=sorted(remote),entire_mass=len(local)+len(remote),north_record_local=dict(cut=6942,pose=[[3,21],0],pruning=sorted(localN),local_mass=len(localN),entire_mass=len(localN)+786,rho='2n+88',normal='N, positive projection of final actual NW drift'),local_limit=dict(seed=sorted(local_normalized),pose=[[0,0],1],finite_prefix=A['T_recovery'][r:],terminal_full_black=sorted(lim['B']),terminal_pose=[lim['p'],lim['h']],tail_word=lim['tail_word'],tail_drift=lim['drift'],parity_tests=lim['tests']),controls=controls)
(P/'PRISTINE_RECORD_AFTER_RETIREMENT_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
