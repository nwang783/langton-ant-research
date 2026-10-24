"""Exact close-input recursive mode and two-mode full-field closure, no broad state cover."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,future
P=Path(__file__).parent;old=json.loads((P/'ALL_LENGTH_TWO_SIDED_MINIMUM_CHECKED.json').read_text());K=set(map(tuple,old['base']));W=old['base_word'];Q=[];HH=[];p=(0,0);h=1
for c in W:Q.append(p);HH.append(h);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
assert Q[13]==(2,1)and HH[13]==0
assert min(q[0]for q in Q)==-1 and max(q[0]for q in K)==2

def geom(p,h,w):
 R=[]
 for c in w:R.append(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return R,p,h

def run(seed,p,h,N,expected=None,snapcuts=()):
 B={q:-i-1 for i,q in enumerate(sorted(seed))};word=[];reads=[];first={};death={};snap={}
 for t in range(N):
  if t in snapcuts:snap[t]=(dict(B),p,h)
  reads.append(p);first.setdefault(p,t);i=B.pop(p,None)
  if i is None:B[p]=t;h=(h+1)%4;c='R'
  else:death[i]=t;h=(h-1)%4;c='L'
  if expected is not None:assert c==expected[t]
  word.append(c);p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
 return dict(B=B,p=p,h=h,word=''.join(word),reads=reads,first=first,death=death,snap=snap)

def cert(z):
 w,dr,dead,tests=future(z['B'],z['p'],z['h']);z.update(tail_word=w,drift=dr,tests=tests);z['death'].update({i:len(z['word'])+t for i,t in dead.items()});return z

def mature(g):
 M=set()
 for i,q in enumerate(Q):
  r=(q[0]-Q[13][0],q[1]-Q[13][1]);lo=-((r[0]-g)//2);hi=0 if i<13 else -1
  for k in range(lo,hi+1):M.symmetric_difference_update({(r[0]+2*k,r[1]+2*k)})
 return M

modes={}
for name,g,A,N,phase in [('S',-3,[0],312,97),('M',-23,[0,1,6,8],10712,41)]:
 seed=mature(g)|{(2*a,2*a)for a in A};assert not(mature(g)&{(2*a,2*a)for a in A})
 z=cert(run(seed,(0,0),0,N));assert z['tail_word']==W[phase:]+W[:phase]and z['drift']==(2,2)
 expected_pose=((2,6),2)if name=='S'else((26,28),0);assert(z['p'],z['h'])==expected_pose
 TQ,_,_=geom(z['p'],z['h'],z['tail_word']);assert min(x for x,y in z['reads']+TQ)>=g
 origin=(z['p'][0]-Q[phase][0],z['p'][1]-Q[phase][1]);assert origin[0]-origin[1]==-1 and origin[0]%2==0
 first=[z['first'][(2*a,2*a)]for a in A];assert first==([0]if name=='S'else[0,124,1272,5028])
 oldinputs=[q for i,q in enumerate(sorted(seed))if q not in{(2*a,2*a)for a in A}and -i-1 in z['death']]
 C={q for i,q in enumerate(sorted(seed))if -i-1 in z['death']}
 modes[name]=dict(guard=g,black_indices=A,seed=seed,z=z,N=N,phase=phase,origin=origin,inputs=first,oldinputs=oldinputs,pruning=C,input_fates={q:z['death'].get(-i-1)for i,q in enumerate(sorted(seed))})
 print('mode',name,'kernel',len(seed),'true input',len(C),'old',len(oldinputs),'output',z['p'],z['h'],'virtual',origin,flush=True)

# Finite geometric universal freshness proof for phase13 rays.
fresh_checks=[]
for i,q in enumerate(Q):
 dx,dy=Q[13][0]-q[0],Q[13][1]-q[1]
 if dx%2==0 and dx==dy:
  epoch=dx//2;offset=104*epoch+i;assert offset>=13;fresh_checks.append([i,epoch,offset])

# Pair/source equalities at n100 plus monotone affine bounds for every n>=100.
pairs=[];initial=[]
for name,s in modes.items():
 q=(202,201);flight=W*100+W[:13];seed=K|{(q[0]+2*a,q[1]+2*a)for a in s['black_indices']};z=run(seed,(0,0),1,len(flight),flight)
 assert(z['p'],z['h'])==(q,0)and all((q[0]+2*a,q[1]+2*a)not in z['first']for a in s['black_indices'])
 inside={r for r in z['B']if r[0]>=q[0]+s['guard']};assert inside=={(r[0]+q[0],r[1]+q[1])for r in s['seed']}
 omitted=max(max(x for x,y in K),max(Q[i][0]+(0 if i<0 else-2)for i in range(104)))
 assert q[0]+s['guard']>omitted
 initial.append(dict(mode=name,marker=q,guard_boundary=q[0]+s['guard'],old_source_max_x=omitted,read_max_x=max(x for x,y in z['reads']),inside=sorted(inside)))
for rn,r in modes.items():
 for sn,s in modes.items():
  phase=r['phase'];n=100
  q=(r['z']['p'][0]+2*(n+int(13<phase))+Q[13][0]-Q[phase][0],r['z']['p'][1]+2*(n+int(13<phase))+Q[13][1]-Q[phase][1])
  assert q[0]==q[1]and q[0]==(206 if rn=='S' else 228)
  flight=(W[phase:]+W[:phase])*n+(W[phase:]+W[:phase])[:(13-phase)%104]
  seq=r['z']['word']+flight;nextbits={(q[0]+2*a,q[1]+2*a)for a in s['black_indices']};assert not(nextbits&r['seed'])
  z=run(r['seed']|nextbits,(0,0),0,len(seq),seq)
  assert(z['p'],z['h'])==(q,0)and not(nextbits&set(z['reads']))
  inside={v for v in z['B']if v[0]>=q[0]+s['guard']};assert inside=={(v[0]+q[0],v[1]+q[1])for v in s['seed']}
  synthetic=r['z']['p'][0]+max(Q[i][0]-Q[phase][0]+(0 if i<phase else-2)for i in range(104))
  oldmax=max(r['guard'],max(x for x,y in r['z']['reads']),max(x for x,y in r['z']['B']),synthetic)
  boundary=q[0]+s['guard'];assert boundary>oldmax
  advance=boundary-r['guard'];assert advance>=186
  assert max(t for t in r['input_fates'].values()if t is not None)<len(seq)
  assert max(x for x,y in z['reads'])<=q[0]+20 and min(x for x,y in z['reads'])>=r['guard']
  assert max(y for x,y in r['z']['reads'])<=64 and max(y for x,y in r['z']['B'])<=64
  pairs.append(dict(previous=rn,next=sn,n100_marker=q,flight_reads=len(flight),all_reads=len(seq),previous_generated_max_x=oldmax,next_guard_boundary=boundary,guard_slack=boundary-oldmax,frontier_increase=advance,synthetic_past_max_x=synthetic,full_read_min_x=min(x for x,y in z['reads']),full_read_max_x=max(x for x,y in z['reads']),complete_inside=sorted(inside),all_n_extension='marker and next guard increase by2(n-100); previous finite objects unchanged'))

# Actual full finite sources for mixed/repeated packet words, not cropped concatenations.
controls=[]
jobs=[(labels,[100]*len(labels),set())for labels in['M','MM','SMMS','MSM','SSM']]
jobs.append(('MMS',[101,137,104],{(-2,10**9),(-2,-10**9),(-10**6,10**9),(-6,1)}))
for labels,gaps,archive in jobs:
 assert all(x<-1 for x,y in archive)
 pos=(0,0);phase=0;seed=set(K)|archive;seq='';markers=[];starts=[]
 for label,n in zip(labels,gaps):
  mode=modes[label];q=(pos[0]+2*(n+int(13<phase))+Q[13][0]-Q[phase][0],pos[1]+2*(n+int(13<phase))+Q[13][1]-Q[phase][1])
  flight=(W[phase:]+W[:phase])*n+(W[phase:]+W[:phase])[:(13-phase)%104];seq+=flight;starts.append(len(seq));bits={(q[0]+2*a,q[1]+2*a)for a in mode['black_indices']};assert not(seed&bits);seed|=bits;markers.append([q,label,sorted(bits)])
  seq+=mode['z']['word'];pos=(q[0]+mode['z']['p'][0],q[1]+mode['z']['p'][1]);phase=mode['phase']
 z=cert(run(seed,(0,0),1,len(seq),seq,starts));assert z['tail_word']==W[phase:]+W[:phase]and z['drift']==(2,2)
 contacts=[];last_marker_x=max(v[0]for qq,ll,bb in markers for v in bb)
 for t,(q,label,bits)in zip(starts,markers):
  mode=modes[label];B,p,h=z['snap'][t];assert(p,h)==(tuple(q),0)
  for a,tt in zip(mode['black_indices'],mode['inputs']):assert z['first'][(q[0]+2*a,q[1]+2*a)]==t+tt
  futurebits={tuple(v)for qq,ll,bb in markers for v in bb if z['first'][tuple(v)]>=t}
  inside={v for v in B if v[0]>=q[0]+mode['guard']};expected={(v[0]+q[0],v[1]+q[1])for v in mode['seed']}|(futurebits-{tuple(v)for v in bits});assert inside==expected
  actualC={v for v,i in B.items()if i in z['death']};expectedC={(v[0]+q[0],v[1]+q[1])for v in mode['pruning']}|futurebits;assert actualC==expectedC
  radius=max(max(abs(v[0]-q[0]),abs(v[1]-q[1]))for v in actualC)
  local_radius=max(max(abs(v[0]),abs(v[1]))for v in mode['pruning'])
  assert radius==max(local_radius,last_marker_x-q[0])
  potential=max(radius-22,0);assert potential==max(last_marker_x-q[0]-22,0)
  if contacts:
   prev=contacts[-1];step=q[0]-prev['pose'][0][0];assert step>=206
   assert potential==max(prev['clipped_radius_potential']-step,0)
  contacts.append(dict(time=t,mode=label,pose=[q,0],complete_current_black=sorted(B),unread_original_markers=sorted(futurebits),guard_boundary=q[0]+mode['guard'],entire_pruning=sorted(actualC),entire_relevant_radius=radius,clipped_radius_potential=potential))
 assert contacts[-1]['clipped_radius_potential']==0
 controls.append(dict(modes=labels,gaps=gaps,retained_western_archive=sorted(archive),fixed_last_marker_x=last_marker_x,seed=sorted(seed),mode_contacts=contacts,complete_prefix_word=seq,terminal_cut=len(seq),terminal_pose=[z['p'],z['h']],terminal_full_black=sorted(z['B']),tail_word=z['tail_word'],tail_drift=z['drift'],full_future_parity_tests=z['tests']))
 print('train',labels,'inputs',len(seed),'reads',len(seq),'tail full mass',len(z['B']),flush=True)

sourcefiles=['ALL_LENGTH_TWO_SIDED_MINIMUM_MANIFEST.json','../audits/check_all_length_two_sided_minimum_independent.json','PHASE13_DOUBLE_SCATTER_MANIFEST.json','../audits/check_phase13_double_scatter_independent.json','check_return_permanent_output_debt.py']
record_modes={}
for name,m in modes.items():
 z=m['z'];record_modes[name]=dict(guard=m['guard'],packet_black_indices=m['black_indices'],kernel=sorted(m['seed']),entire_comparison_pruning=sorted(m['pruning']),old_input_cells=sorted(m['oldinputs']),first_packet_reads=m['inputs'],initial_input_fates=[dict(cell=q,first_read=t)for q,t in sorted(m['input_fates'].items())],comparison_pruned_radius=max(max(abs(q[0]),abs(q[1]))for q in m['pruning']),last_initial_consumption=max(t for t in m['input_fates'].values()if t is not None),recovery_word=z['word'],recovery_length=m['N'],full_read_bbox=[min(x for x,y in z['reads']),max(x for x,y in z['reads']),min(y for x,y in z['reads']),max(y for x,y in z['reads'])],complete_output_black=sorted(z['B']),output_pose=[z['p'],z['h']],output_phase=m['phase'],output_virtual_origin=m['origin'],tail_word=z['tail_word'],tail_drift=z['drift'],full_tail_tests=z['tests'])
out=dict(status='AUTHOR recursive two-mode theorem; independent audit pending',scope='Any finite S/M packet word and all gaps n>=100, with full guard closure; not all ray cohorts or arbitrary old archive inside guards. Finite control retains unbounded pending cohort geometry.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in sourcefiles},canonical_source=sorted(K),W=W,phase13_freshness=fresh_checks,modes=record_modes,initial_interfaces=initial,pair_interfaces=pairs,controls=controls,analytic_constants=dict(local_radius_bound=22,minimum_head_advance=206,minimum_guard_advance=186,source_min_read_x=-1,source_omitted_max_x=2),exact_entry_invariant='Entire C* equals translated comparison pruning union all unread original packets; max(rho-22,0)=max(fixed_last_marker_x-head_x-22,0).')
(P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
