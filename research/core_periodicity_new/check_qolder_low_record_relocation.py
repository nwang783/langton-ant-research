"""A finite free-core-relocation local-ledger countermodel, NOT an ant word.
All positions are explicit. Between packets the old core is removed and a
new one installed; the residual ledger is untouched. This deliberately
forgets physical endpoint transport and full-word chronological legality.
"""
from pathlib import Path
import json,collections,hashlib
W=Path(__file__).resolve().parent;J=json.load(open(W/'chronology_dcuv/literal_residual_geometry.json'));G=J['geometry'];K=set(map(tuple,J['core']));A=[0,22,20,10];Rmeta=json.load(open(W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json'));T={(a,h):v for a,h,v in Rmeta['created_peaks']};HB={tuple(map(int,l.split()[:7]))for l in (W/'chronology_dcuv/protected_patch2.tsv').read_text().splitlines()};COUNT={tuple(map(int,l.split()[:8]))for l in (W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};IDS=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(IDS)}
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def cells(P,p,h):return{(p[0]+rot(z,h)[0],p[1]+rot(z,h)[1])for z in P}
PP=Path(Rmeta['potential_file']);values=json.loads(PP.read_text())['values']
def potential_A(h):return sum(rot((-1,1),h))+values[f'c{h%4}']
def potential_T(a,h):
 dx,dy,dh=G[a]['endpoint']
 return max([2*sum(rot((dx,dy),h))+potential_A(h+dh)]+[2*sum(rot(z,h))+values[f'w_{a}_{j}_{h}']for j,z in enumerate(G[a]['outputs'])])
assert (values['ax'],values['ay'])==(1,1)and [potential_A(h)for h in range(4)]==A
assert all(potential_T(a,h)==T[a,h]for a in IDS for h in range(4))
S=[];C=0;h=2;padn=0;roots=[]
def add(a,p,hh,tag):
 global C,h
 assert hh==h,(a,p,hh,h)
 assert(sum(p)+h)%2==0,('sector',a,p,h)
 S.append(dict(packet=a,head=[*p,h],C=C,tag=tag));C+=G[a]['name'].count('C');h=(h+G[a]['endpoint'][2])%4
 return len(S)-1
def pads(n):
 global padn
 for _ in range(n):
  padn+=1;p=(100000*padn+h%2,100000*padn-1000);v=rot((0,1),h);roots.append((p[0]+v[0],p[1]+v[1]));add(1,p,h,'clock_padding')
def before(want,minimum):
 n=minimum
 while(h-n)%4!=want:n+=1
 pads(n)
def route(target,n,odd,tag,between=0):
 if S:before(2,between)
 pf=(target[0]+1,target[1]-2)if odd else(target[0]+2,target[1])
 p=(pf[0]+n-1,pf[1]-3*(n-1));roots.append((p[0],p[1]-1))
 for j in range(n):
  p=(pf[0]+n-1-j,pf[1]-3*(n-1-j));add(0,p,2,tag+'_S')
  if j<n-1 or odd:
   before(3,3);add(0,(p[0]-1,p[1]),3,tag+'_W')
  if j<n-1:before(2,5)
route((2,5),5,True,'main_input')
before(2,5);add(1,(2,6),2,'bd_birth')
route((-1,2),15,True,'q_birth',0)
route((0,2),25,False,'c_birth',5)
route((-1,1),35,False,'a_birth',4)
before(0,6);add(7,(0,0),0,'goal')
assert len(roots)==len(set(roots));R={p:dict(initial=True)for p in roots};first=S[0]['head'];B=set(R)|cells(K,first[:2],first[2]);initial_board=set(B);maxscore=-100000;newchecks=0;last_end=None;broken_junctions=0
assert len(initial_board)==646 and max(y-x for x,y in roots)==-17
assert all(48+2*(y-x)<30 for x,y in roots)
assert 2*(first[1]-first[0])+A[(first[2]+1)%4]<30
for i,r in enumerate(S):
 a=r['packet'];p=tuple(r['head'][:2]);hh=r['head'][2];kc=cells(K,p,hh)
 if last_end is not None:
  assert last_end[2]==hh # Global heading is NEVER reset.
  if last_end!=[*p,hh]:broken_junctions+=1
 assert not kc&set(R),(i,'core intersects',kc&set(R))
 B=set(R)|kc
 for x,y,b,*_ in G[a]['requirements']:
  z=rot((x,y),hh);q=p[0]+z[0],p[1]+z[1]
  assert (q in B)==b,(i,r,'req',q,b,q in R,R.get(q))
 ins=cells(G[a]['inputs'],p,hh);assert ins<=set(R)
 r['inputs']=[]
 for z in ins:
  v=R[z];age=None if v.get('initial')else r['C']-v['C'];slot=rot((z[0]-p[0],z[1]-p[1]),-hh)
  mn=3 if a in[0,1] else 5 if slot in[(-1,4),(0,2),(0,3)] else 3
  assert age is None or age>=mn,(i,'age',age,mn)
  if age is not None:
   dh=(hh-v['h'])%4;rel=rot((p[0]-v['head'][0],p[1]-v['head'][1]),-v['h']);key=(v['packet'],a,*rel,dh,*v['slot']);ck=(mp[v['packet']],mp[a],*rel,dh,*v['slot'],min(5,age))
   assert key not in HB,(i,'HB',key)
   assert ck not in COUNT,(i,'COUNT',ck)
   newchecks+=1
  r['inputs'].append(dict(cell=z,age=age,origin=v))
 for z in ins:del R[z]
 for slot in G[a]['outputs']:
  z=rot(slot,hh);z=p[0]+z[0],p[1]+z[1];assert z not in R;(R.__setitem__)(z,dict(packet=a,step=i,C=r['C'],h=hh,head=p,slot=slot))
 x,y=p;fh=hh;rawB=set(B);rawend=None
 for k,ch in enumerate(G[a]['word']+G[a]['marker']):
  z=x,y;black=z in rawB;assert ch==('L'if black else'R'),(i,k,z)
  if black:rawB.remove(z)
  else:rawB.add(z)
  fh=(fh+(-1 if black else 1))%4;dx,dy=rot((0,1),fh);x+=dx;y+=dy
  if k+1==len(G[a]['word']):rawend=(x,y,fh,set(rawB))
 x,y,eh,bb=rawend;assert bb==set(R)|cells(K,(x,y),eh)and not set(R)&cells(K,(x,y),eh),(i,'ledger')
 last_end=[x,y,eh];r['raw_exit']=last_end
 entry=2*(p[1]-p[0])+A[(hh+1)%4];created=2*(p[1]-p[0])+T[a,(hh+1)%4];r['record']=[entry,created]
 if i<len(S)-1:assert max(entry,created)<30,(i,'record',entry,created);maxscore=max(maxscore,entry,created)
goal={tuple(r['cell']):r for r in S[-1]['inputs']}
assert all(not r['origin'].get('initial')for r in goal.values())
ages={str(z):goal[z]['age']for z in [(-1,1),(-1,2),(-1,4),(0,2),(0,3)]}
assert list(ages.values())==[6,479,598,282,598]
a=goal[(-1,1)];q=goal[(-1,2)];c=goal[(0,2)];d=goal[(0,3)]
assert q['origin']['step']<=max(a['origin']['step'],c['origin']['step'])
assert q['origin']['step']<=max(a['origin']['step'],d['origin']['step'])
assert q['age']>=min(a['age'],c['age'])and q['age']>=min(a['age'],d['age'])
assert q['age']>a['age']and all(r['age']>=5 for r in goal.values())
assert S[-1]['record']==[22,30]and maxscore==26
assert broken_junctions==len(S)-1==796
assert collections.Counter(r['packet']for r in S)=={0:158,1:638,7:1}
assert len(R)==2559 and len(bb)==2564
summary=dict(packets=len(S),D=158,DC=638,U=1,clock_padding_DC=padn,initial_roots=len(roots),
             initial_total_mass=len(initial_board),initial_max_residual_height=-17,initial_weight=48,
             prior_core_and_creation_max=maxscore,goal_record=[22,30],C_before_goal=S[-1]['C'],
             goal_input_ages=ages,produced_input_HB_and_count_checks=newchecks,
             final_total_mass=len(bb),nonphysical_junctions=broken_junctions,
             raw_packet_reads=sum(len(G[r['packet']]['word'])for r in S),
             local_RAW_plus_marker_reads=sum(len(G[r['packet']]['word'])+len(G[r['packet']]['marker'])for r in S))
deps=[W/'chronology_dcuv/literal_residual_geometry.json',W/'chronology_dcuv/protected_patch2.tsv',
      W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv',
      W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json',PP,Path(__file__).resolve()]
O=dict(status='AUTHOR_LOCAL_RELOCATION_QOLDER_LOW_RECORD_COUNTERMODEL_PASS',
       scope='A finite free-core-relocation local-ledger relaxation ONLY. Every physical endpoint junction is broken. No actual ant word, full k6/k7 language, complete chronological kernel, unfunded physical record, capture or infinite renewal is asserted.',
       summary=summary,schedule=S,initial_residual_roots=roots,initial_actual_board=sorted(initial_board),
       dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
P=W/'chronology_dcuv/qolder_low_record_relocation.json';P.write_text(json.dumps(O,indent=2)+'\n')
print(json.dumps(summary,indent=2))
