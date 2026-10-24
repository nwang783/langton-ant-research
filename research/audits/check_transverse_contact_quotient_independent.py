from pathlib import Path
from collections import Counter
from itertools import product
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'TRANSVERSE_FIRST_CONTACT_QUOTIENT_MANIFEST.json';assert sha(MF)=='6ebce42eb42e960f9471c9ac4c46c4b7ed9c0645d9adf36a4e6bb30c7efc4388'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'TRANSVERSE_FIRST_CONTACT_QUOTIENT_CHECKED.json').read_text())
for f,h in J['source_hashes'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_return_permanent_debt_independent.py'))};exec(Path(ns['__file__']).read_text().split('def check_case')[0],ns);verify=ns['verify_future'];vec=(1j,1,-1j,-1);xy=lambda q:[int(q.real),int(q.imag)];order=lambda q:(q.real,q.imag)
source=json.loads((D/'WRITTEN_WAKE_PORT_OBSTRUCTION_CHECKED.json').read_text());A,U=source['A'],source['U'];Q=list(map(lambda q:complex(*q),source['Q']));W={complex(*z['cell']):z['phase']for z in source['W']};C={complex(*q)for q in source['C']};G={-1j,1+1j,1+3j,2+2j};firstG={complex(*z['cell']):z['first']for z in source['first']if z['black']};heads=[];h=1
for ch in U:heads.append(h);h=(h+(1 if ch=='R'else-1))%4
assert len({U[i:]+U[:i]for i in range(104)})==104

def walk(p,h,w):
 pts=[]
 for ch in w:pts.append(p);h=(h+(1 if ch=='R'else-1))%4;p+=vec[h]
 return p,h,pts

def line_hits(p,d,a,v,bound):
 # Use input-line normal x-sign*y, independently of a determinant implementation.
 sign=int(v.imag/v.real);den=int(d.real-sign*d.imag);num=int(a.real-sign*a.imag-p.real+sign*p.imag)
 if den:
  if num%den:return None
  k=num//den
  if k<0:return None
  delta=p+k*d-a
  if int(delta.real)%int(v.real):return None
  j=int(delta.real)//int(v.real)
  if delta!=j*v or bound is not None and j>bound:return None
  return(k,k)
 if num:return None
 delta=p-a
 if int(delta.real)%int(v.real):return None
 j=int(delta.real)//int(v.real)
 if delta!=j*v:return None
 if bound is None:return(0,None)
 sig=int(d.real/v.real);assert sig in(-1,1)
 if sig==1:return(0,bound-j)if bound>=j else None
 return(max(0,j-bound),None)

def ideal_tail(gens,F,p,h,H):
 end,hh,pts=walk(p,h,H);dr=end-p;assert hh==h and abs(dr.real)==abs(dr.imag)==2;tested=0
 for i,q in enumerate(pts):
  flips=Counter({0:0});intervals=[];thresholds=[]
  for a,v,b in gens:
   iv=line_hits(q,dr,a,v,b)
   if iv is not None:
    lo,hi=iv;flips[lo]+=1
    if hi is not None:flips[hi+1]+=1
    intervals.append(iv)
  for z in F:
   delta=z-q
   if int(delta.real)%int(dr.real):continue
   k=int(delta.real)//int(dr.real)
   if k>=0 and delta==k*dr:flips[k]+=1;flips[k+1]+=1;intervals.append((k,k))
  for j,z in enumerate(pts):
   delta=z-q
   if int(delta.real)%int(dr.real):continue
   m=int(delta.real)//int(dr.real)
   if delta==m*dr and(m>0 or m==0 and j<i):flips[m]+=1;thresholds.append(m)
  parity=0
  for k,n in sorted(flips.items()):parity^=n%2;assert parity==(H[i]=='L'),(i,k);tested+=1
 return dr,tested

assert {tuple(r['joins'])for r in J['controls']}==set(product((61,71),repeat=3));counts=[66,15,34];seen={};results=[]
for r in J['controls']:
 joins=r['joins'];poses=[(0j,1)];entries=[0]
 for j,n in zip(joins,counts):
  o,h=poses[-1];poses.append((o+(-1j)**(h-1)*(Q[j]+n*(2+2j)),(heads[j]+h-1)%4));entries.append(entries[-1]+182+104*n+j)
 seed={o+(-1j)**(h-1)*g for o,h in poses for g in G};assert len(seed)==16 and sorted(map(xy,seed))==r['initial_black'];assert [[[int(o.real),int(o.imag)],h]for o,h in poses]==r['poses']and entries==r['port_entry_times'];z,h=poses[-1];assert h==2 and int(z.real+z.imag)%2==1
 residue=(int(z.real+z.imag)%4,int(z.real-z.imag)%4);assert list(residue)==r['residue'];hits=[]
 for i,q in enumerate(Q):
  v=z-1j*q
  for wi,w in enumerate(W):
   delta=int(w.real-w.imag-v.real+v.imag)
   if delta%4:continue
   k=delta//4;p=v+k*(2-2j);diff=p-w
   if diff.real==diff.imag and int(diff.real)%2==0:hits.append(dict(time=104*k+i,phase=i,period=k,cell=xy(p),old_W_index=wi))
 hits.sort(key=lambda x:(x['time'],x['old_W_index']));assert hits==r['all_past_first_contact_hits'];first=hits[0];kk,phi=first['period'],first['phase'];contact=complex(*first['cell']);ct=entries[-1]+182+104*kk+phi;assert ct==r['first_contact']['time']and phi==r['incoming_phase']and U[phi]=='R'
 fringe=set(C)
 for p in Q[:phi]:fringe.symmetric_difference_update({p})
 finite={z+kk*(2-2j)-1j*p for p in fringe};gens=[(w,2+2j,None)for w in W]+[(z-1j*w,2-2j,kk-1)for w in W];assert sorted(map(xy,finite))==r['comparison_finite'];assert [[xy(a),xy(v),b]for a,v,b in gens]==r['comparison_generators']
 pre=''.join(A+U*n+U[:j]for j,n in zip(joins,counts));assert len(pre)==entries[-1];last=ct-len(pre);assert last>=182;pre+=A+U*((last-182)//104)+U[:(last-182)%104];assert len(pre)==ct
 F,H=r['postcontact_word'],r['canonical_word'];assert F[0]=='L'and F[-1]!=H[-1]and H in{U[i:]+U[:i]for i in range(104)}and len(F)==r['exact_postcontact_delay'];word=pre+F+H*2
 B={p:-i-1 for i,p in enumerate(sorted(seed,key=order))};p=0j;h=1;firsts={};births={};snapshot=None
 for t,ch in enumerate(word):
  if p in seed and p not in firsts:firsts[p]=t
  if t==ct:
   assert p==contact and h==2 and B[p]==r['first_contact']['lifetime']>=0;snapshot=dict(B)
  assert(ch=='L')==(p in B),(joins,t,p)
  if ch=='L':B.pop(p);h=(h-1)%4
  else:B[p]=t;births[t]=p;h=(h+1)%4
  p+=vec[h]
 assert snapshot=={complex(*a['cell']):a['lifetime']for a in r['full_contact_black']};assert B=={complex(*a['cell']):a['lifetime']for a in r['full_finite_terminal_black']}and[xy(p),h]==r['full_finite_terminal_pose'];assert len(word)==r['physical_updates']
 for ei,(o,hh)in zip(entries,poses):
  for g in G:assert firsts[o+(-1j)**(hh-1)*g]==ei+firstG[g]
 assert [dict(cell=xy(q),time=firsts[q])for q in sorted(seed,key=order)]==r['initial_first_reads'];assert xy(births[r['first_contact']['lifetime']])==r['marked_birth_cell']==xy(contact)
 hw,dr,fates,checks=verify(B,p,h);assert hw==H and xy(dr)==r['canonical_drift']and checks==r['full_finite_tail_parity_tests']
 def initial(q):
  b=q in finite
  for a,v,upper in gens:
   delta=q-a
   if int(delta.real)%int(v.real):continue
   j=int(delta.real)//int(v.real)
   if delta==j*v and(upper is None or j<=upper):b=not b
  return b
 changes=set();p0=contact;h0=2
 for ch in F:
  b=initial(p0)^(p0 in changes);assert b==(ch=='L');changes.symmetric_difference_update({p0});h0=(h0+(-1 if b else 1))%4;p0+=vec[h0]
 assert [xy(p0),h0]==r['canonical_entry_pose'];ending=finite^changes;assert sorted(map(xy,ending))==r['ideal_tail_finite'];idr,it=ideal_tail(gens,ending,p0,h0,H);assert idr==dr
 assert not any((F+H*2).startswith(A[:33],k)for k in range(len(F)))and not any((H*2).startswith(A[:33],k)for k in range(104))
 value=(F,H,dr,p0-contact,h0)
 if residue in seen:assert seen[residue]==value
 else:seen[residue]=value
 results.append(dict(joins=joins,residue=residue,actual_reads=len(word),contact_time=ct,old_R_birth=r['first_contact']['lifetime'],old_R_cell=xy(contact),incoming_phase=phi,delay=len(F),onset=ct+len(F),drift=xy(dr),finite_checks=checks,ideal_ray_breakpoint_checks=it))
assert set(seen)=={(1,1),(1,3),(3,1),(3,3)};assert {r['delay']for r in results}=={2136,8986,9081,19198};old=json.loads((D/'TRANSVERSE_FAR_MODULE_SOURCE.json').read_text());assert seen[(1,1)][0]==old['post_contact_word']and seen[(1,1)][1]==old['tail_word']
out=dict(status='PASS four pure clockwise first-transverse comparison classes and eight full finite causal realizations',manifest=sha(MF),script=sha(S),source_independent_wake_report=sha(S.with_name('check_written_wake_port_independent.json')),controls=results,analytic_review=['Full d=(2,2) and e=(2,-2) generate an index8 lattice; Smod4,Tmod4 with same parity are its exact cosets. Same orbit invariant h+x+y modulo2 leaves precisely the four odd/odd cosets for the clockwise incomingS origin. Translations by d move the whole interface; by e merely relabel the incoming period. Opposite approach is not included.','For each oldW class and incomingphase the T equation uniquely fixes the incoming integerperiod. All104x12 possibilities over ALL integers, not a finite past scan, are generated. Their globalminimum is unperturbedR versus oldBLACK actualL. No earlier incoming read touches oldwake, so all prior incoming-written bits are genuinely preserved in the XOR comparison field.','All12 bi-infinite oldrays,12 backward incoming half-rays and finite phasecorrection are retained. Independent normal-coordinate intersection algebra and parity flip-breakpoints certify every infinite finalphase, including drift opposite to incoming. No infinite archive is cropped or mistaken for a finite seed.','Eight literal16cell boards independently replay every pre/postcontact read, all originalport first-read times, same oldR3061/3183 lifetime and entire contact/terminalfields. Both realizations perclass agree on postcontact word/relativepose, not globally on their boards. Independent full finite-field tail parity proves observational equivalence on the ENTIRE future. This supplies no all-n extrapolation.','Primitive104 cyclic words and the immediate preceding-letter mismatch certify exact onset delays. Every actual postcontact start, including all104 infinite-tail phases, avoids Gprefix33; this does not rule out unused static motifs. Extra archive, finite wake endpoints not discharged by these controls, altered wakes, another approach/protocol and globalattraction remainOPEN.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
