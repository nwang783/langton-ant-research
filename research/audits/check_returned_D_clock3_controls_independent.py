from pathlib import Path
from fractions import Fraction
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];ns={'__file__':str(SELF.parent/'check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns)
W,M,walk,xy,center,meet,dirs=[ns[x]for x in('W','M','walk','xy','center','meet','dirs')]
D=R/'returned_D_clock3_controls_2026-10-24';ref=json.loads((D/'D_clock3_controls.json').read_text());names=('DCDDCVVCDDUFC','DCDDCDDDCDDDDUFV');packets=('D','DC','V','VC','VCC','U','UC','UCC');results=[];queries=[]
for k,(name,completion,rr)in enumerate(zip(names,('D','C'),ref['two_actual_controls'])):
 word=''.join(W[a]for a in name+completion)+M;a=walk(word);assert a['feasible'];seed={q for q,b in a['req'].items()if b};assert len(seed)==(34 if k==0 else 35)and set(map(xy,seed))==set(map(tuple,rr['initial_black_board']))
 B=set(seed);p=0j;h=0;reads=[];life={q:('initial',q)for q in B};bud=[]
 for t,ch in enumerate(word):
  assert (p in B)==(ch=='L');r=rr['all_fine_reads'][t];assert(xy(p),h,ch)==(tuple(r['cell']),r['heading_before'],r['turn'])
  if p==2:bud.append((t,ch,life.get(p)))
  if ch=='L':B.remove(p);del life[p]
  else:B.add(p);life[p]=('R',t)
  h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 assert len(B)==rr['final_mass']
 p=0j;h=0;t=0;atoms=[]
 for n in name:
  w=walk(W[n]);end=p+w['p']*(-1j)**h;hh=(h+w['h'])%4;atoms.append((n,p,h,t,xy(center(p,h)),xy(center(end,hh))));p,h,t=end,hh,t+len(W[n])
 fi=next(i for i,z in enumerate(atoms)if z[0]=='F');assert sum(z[0]=='C'for z in atoms[:fi])==3
 pieces=[(z[4],z[5])for z in atoms[:fi+1]];ret=atoms[fi+1]
 for i,(aa,bb)in enumerate(pieces):
  for j in range(i+1,len(pieces)):
   hit=meet(aa,bb,*pieces[j])
   if j==i+1:assert hit is not None and (hit[:2]==(1,0) or hit==(bb,)),(i,j,hit)
   else:assert hit is None
 contacts=[(i,meet(aa,bb,ret[4],ret[5]))for i,(aa,bb)in enumerate(pieces)if meet(aa,bb,ret[4],ret[5])is not None]
 assert len(contacts)==2 and contacts[0][0]==0 and contacts[0][1][:2]==((0,1)if k==0 else(Fraction(1,2),Fraction(1,2)))and contacts[-1][1][:2]==(1,0)
 # Independent complete BFS, no prescribed depth or accepted-child list.
 todo=[()];seen=set();edges={}
 while todo:
  pref=todo.pop(0);assert pref not in seen;seen.add(pref);good=[]
  tail=''.join(W[c]for n in pref for c in n)+''.join(W[c]for c in name)+M
  assert walk(tail)['feasible']
  for packet in packets:
   q=walk(''.join(W[c]for c in packet)+tail)
   if q['feasible']:good.append(packet);todo.append((packet,)+pref);entry={'legal':True,'mass':sum(q['req'].values())}
   else:entry={'legal':False,'tick0':q['i'],'cell':xy(q['q']),'first_tick0':q['first']}
   queries.append({'control':k,'prefix':pref,'prepend':packet,**entry})
  edges[str(pref)]=good
 assert seen==({(),('D',),('DC','D'),('V','D'),('D','DC','D')}if k==0 else{(),('V',)})
 assert not any(n.startswith('U')for pref in seen for n in pref)
 results.append({'word':name+completion,'seed_mass':len(seed),'updates':len(word),'final_mass':len(B),'foreign_pose':[xy(atoms[fi][1]),atoms[fi][2]],'returned_pose':[xy(ret[1]),ret[2]],'old_source_contact_parameters':list(map(str,contacts[0][1][:2])),'actual_source_bud_lifetime_reads':[(t,ch,str(l))for t,ch,l in bud],'complete_reverse_tree':edges})
assert len(queries)==56
mp=D/'manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='e117d854a0d158e67e0ed04859d43ca28aa3fdfb15487238c8c8d0903710e47e'
for a in json.loads(mp.read_text())['files']:assert hashlib.sha256((D/a['file']).read_bytes()).hexdigest()==a['sha256']
for f,h in ref['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS two complete finite D-entry clock3 controls and complete56-query no-U-entry fixed-word predecessor closure','manifest_sha256':mh,'controls':results,'all56_predecessor_queries':queries,'scope':['Complete boards34/35 execute every prescribed fine read, including actual following D or own returned VC tail and actual M11 prefix. Old+F proxy is simple; returned rawC hits oldD start, returnedV crosses its midpoint.','Original D bud identity is tracked through actual reads, not inherited after replacement. In control2 F consumes the original token, writes a replacement, and returnedV reads that replacement.','Reverse predecessor BFS exhausts every feasible node using shortest necessary returned-atom+M11 suffix, with no depth limit and no U-family node. These FIXED words cannot have an earlier uninterrupted U-entry eight prefix.','The two target geometries are physically attained from D-entry. This does not prove U-entry attainment or exclude different histories reaching the same poses. No returned simplicity or global capture inference.']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
