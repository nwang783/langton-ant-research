from pathlib import Path
from fractions import Fraction
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'returned_D_entry_controls_2026-10-24';mf=D/'manifest.json';assert hashlib.sha256(mf.read_bytes()).hexdigest()=='8a7b1a1c567d0e8aff449c02eed63356c095f89809601652def459b1540b6e4c'
for f,h in json.loads(mf.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
ns={'__file__':str(SELF.parent/'check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns)
W,M,walk,xy,center,meet,dirs=[ns[x]for x in('W','M','walk','xy','center','meet','dirs')]
refs=json.loads((D/'D_entry_controls.json').read_text());names=('DCDVFV','DDCDUFV','DCDDUQV','DCVVQV','DDCVUQV','DCVUBV');packets=('D','DC','V','VC','VCC','U','UC','UCC');out=[];pre=[]
for name,ref in zip(names,refs['six_actual_controls']):
 raw=''.join(W[a]for a in name+'C');word=raw+M;tr=walk(word);assert tr['feasible'];seed={p for p,b in tr['req'].items()if b};assert sorted(map(xy,seed))==list(map(tuple,ref['initial_black_board']))
 board=set(seed);p=0j;h=0;tagreads=[];rawmass=None
 for t,ch in enumerate(word):
  if t==len(raw):rawmass=len(board)
  assert (p in board)==(ch=='L')
  rr=ref['all_fine_reads'][t];assert (xy(p),h,ch)==(tuple(rr['cell']),rr['heading_before'],rr['turn'])
  if p==2:tagreads.append([t,ch])
  board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 assert len(board)==ref['final_mass'];assert tagreads==ref['all_tag_reads'];assert tagreads[0]==[8,'R']
 # Compose raw geometry independently in complex coordinates.
 p=0j;h=0;t=0;atoms=[]
 for a in name:
  aa=walk(W[a]);pp=p+aa['p']*(-1j)**h;hh=(h+aa['h'])%4
  atoms.append((a,p,h,t,xy(center(p,h)),xy(center(pp,hh))))
  p,h,t=pp,hh,t+len(W[a])
 fi=next(i for i,a in enumerate(atoms)if a[0]in'FQB');f=atoms[fi];v=atoms[-1]
 assert v[0]=='V'and(v[1],v[2])==(-1+0j,1);assert sum(a[0]=='C'for a in atoms[:fi])==1
 assert tagreads[1]==[v[3]+19,'L'];assert len([z for z in tagreads if z[0]<v[3]])==1
 assert W['C'][1]=='L'and M[1]=='L'and len(W['V'])==18
 cut=xy(2*f[1]+(-7-3j)*(-1j)**f[2]);pieces=[(a[4],a[5])for a in atoms[:fi]]+[(f[4],cut)]
 if f[0]!='F':pieces.append((cut,f[5]))
 else:assert cut==f[5]
 for i,(a,b)in enumerate(pieces):
  for j in range(i+1,len(pieces)):
   z=meet(a,b,*pieces[j])
   if j==i+1:
    assert z is not None and a!=b
    assert pieces[i][1]==pieces[j][0]
    assert z==(Fraction(1),Fraction(0),tuple(map(Fraction,b))) or z==(b,)
   else:assert z is None
 contacts=[]
 for i,(a,b)in enumerate(pieces):
  z=meet(a,b,v[4],v[5])
  if z is not None:contacts.append((i,z))
 assert len(contacts)==2 and contacts[0]==(0,(Fraction(1,2),Fraction(1,2),(Fraction(0),Fraction(0))))
 assert contacts[-1][0]==len(pieces)-1 and contacts[-1][1][:2]==(1,0)
 # Reject prepends to the shortest NECESSARY V+M11, not the longer VC control.
 shortest=''.join(W[a]for a in name)+M
 for extra in(0,1):
  allowed=[]
  for packet in packets:
   a=walk(''.join(W[x]for x in packet)+W['D']*extra+shortest)
   if a['feasible']:allowed.append(packet);datum={'legal':True,'mass':sum(a['req'].values())}
   else:datum={'legal':False,'conflict_tick':a['i'],'cell':xy(a['q']),'first_tick':a['first']}
   pre.append({'control':name,'extra_D':extra,'preceding_packet':packet,**datum})
  assert allowed==(['D']if extra==0 else[])
 # Positive one-D extension also on a full physical board, including full returned VC.
 a=walk(W['D']+word);assert a['feasible'];bb={q for q,c in a['req'].items()if c};p=0j;h=0
 for ch in W['D']+word:
  assert (p in bb)==(ch=='L');bb.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 out.append({'word':name+'C','seed_mass':len(seed),'RAW_length':len(raw),'RAW_mass':rawmass,'after_marker_mass':len(board),'tag_reads':tagreads,'old_proxy_pieces':len(pieces),'returned_contact':{'old_atom':'D','both_parameters':'1/2','doubled_point':[0,0]}})
assert [x['seed_mass']for x in out]==[24,28,29,26,30,32] and len(pre)==96
report={'status':'PASS literal controls, exact geometry and finite predecessor closure; phase indexing qualification required','manifest_sha256':hashlib.sha256(mf.read_bytes()).hexdigest(),'six_controls':out,'all96_minimal_prefix_predecessor_queries':pre,'ownership':'All ticks are ZERO BASED. Source D tag is born at tick8. Returned V raw has18 reads; tag is first read at returned packet tick19. It is C-tail tick1, meaning the SECOND physical read of the C tail. In minimal V+M11 it is M11 tick1, the SECOND physical read of the actual following word, not its first read. Exact exit-core residual absorption is distinct from this later physical L.','analytic':['Complete minimal first-read boards were independently derived and directly physically replayed, all other cells WHITE. The six controls really attain young source-D lifetime consumption after foreign and a returned V proper crossing of the old D midpoint. Thus old-eight input lifetime and simple-path laws do not extend blindly through foreign.', 'The old path and actual F-prefix/Q/B-tail repaired geometry is simple; the returned V has exactly the old D midpoint crossing and its true adjacent foreign start endpoint. No unsafe whole Q/B chord or invented marker used.','The reverse obstruction tests every possible immediate full-eight predecessor against the NECESSARY shorter returned V+actual M11. Only D survives, and every one of the eight predecessors before that D conflicts. Therefore no longer uninterrupted old-eight prefix can exist, regardless length. The initial D/DC and unique D prepend cannot be a U-family factor entry.','The six cases are positive fixed controls and their exact reverse closure only. The separate endpoint-driven assertion that these exhaust three catalogue configurations is not certified by this bundle.'],'scope':'D-entry controls, not U-entry counterexamples. No general returned simplicity, arbitrary marker ancestry, universal foreign age law or seven-word termination.'}
SELF.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status'])
