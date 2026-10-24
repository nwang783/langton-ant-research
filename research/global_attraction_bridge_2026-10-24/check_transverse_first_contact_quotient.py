"""Exact clockwise transverse completed-wake quotient and eight finite realizations."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,rot,future
P=Path(__file__).parent;src=json.loads((P/'WRITTEN_WAKE_PORT_OBSTRUCTION_CHECKED.json').read_text());Q=list(map(tuple,src['Q']));W=[tuple(z['cell']) for z in src['W']];C=set(map(tuple,src['C']));A,U=src['A'],src['U'];G=set(map(tuple,src['G']));refs=json.loads((P/'TRANSVERSE_JOIN_QUOTIENT_PROBES.json').read_text())['records']
add=lambda a,b:(a[0]+b[0],a[1]+b[1]);sub=lambda a,b:(a[0]-b[0],a[1]-b[1]);det=lambda a,b:a[0]*b[1]-a[1]*b[0]
def move_word(p,h,w):
 reads=[]
 for ch in w:
  reads.append(p);h=(h+(1 if ch=='R'else-1))%4;p=add(p,DXY[h])
 return p,h,reads
Qh=[];hh=1
for ch in U:Qh.append(hh);hh=(hh+(1 if ch=='R'else-1))%4
firstG={tuple(z['cell']):z['first'] for z in src['first'] if z['black']};assert set(firstG)==G

def line_interval(p,dr,a,v,upper):
 """k>=0 for which p+k dr=a+j v, j any integer <=upper (or all)."""
 dd=det(dr,v);b=sub(a,p)
 if dd:
  kn,jn=det(b,v),det(b,dr)
  if kn%dd or jn%dd:return None
  k,j=kn//dd,jn//dd
  return (k,k)if k>=0 and(upper is None or j<=upper)else None
 b=sub(p,a)
 if det(b,v) or b[0]%v[0]:return None
 j=b[0]//v[0];sigma=dr[0]//v[0];assert sigma in(-1,1)
 if upper is None:return 0,None
 if sigma==1:
  top=upper-j;return (0,top) if top>=0 else None
 return max(0,j-upper),None

def infinite_tail(generators,finite,p,h,word):
 pend,hend,reads=move_word(p,h,word);dr=sub(pend,p);assert hend==h and abs(dr[0])==abs(dr[1])==2
 tests=[]
 for i,q in enumerate(reads):
  intervals=[]
  for a,v,bound in generators:
   iv=line_interval(q,dr,a,v,bound)
   if iv is not None:intervals.append(iv)
  for z in finite:
   d=sub(z,q)
   if d[0]%dr[0]==0 and d[1]==(d[0]//dr[0])*dr[1] and d[0]//dr[0]>=0:
    k=d[0]//dr[0];intervals.append((k,k))
  thresholds=[]
  for j,z in enumerate(reads):
   d=sub(z,q)
   if d[0]%dr[0]==0 and d[1]==(d[0]//dr[0])*dr[1]:
    m=d[0]//dr[0]
    if m>0 or m==0 and j<i:thresholds.append(m)
  critical={0}|set(thresholds)
  for a,b in intervals:
   critical.add(a)
   if b is not None:critical.add(b+1)
  for k in sorted(critical):
   parity=(sum(k>=a and(b is None or k<=b)for a,b in intervals)+sum(k>=m for m in thresholds))%2
   assert parity==(word[i]=='L'),(i,k,word[i],intervals,thresholds)
  tests.append(dict(phase=i,critical_copies=sorted(critical),input_intervals=intervals,prior_read_thresholds=thresholds))
 return dr,tests

out=[];class_words={};seen=set()
for ref in refs:
 joins=ref['joins'];n=20;r=[66,15,34];poses=[((0,0),1)];entries=[0]
 for i,j in enumerate(joins):
  o,h=poses[-1];q=rot(add(Q[j],(2*r[i],2*r[i])),h-1);poses.append((add(o,q),(Qh[j]+h-1)%4));entries.append(entries[-1]+182+104*r[i]+j)
 seed={add(o,rot(g,h-1))for o,h in poses for g in G};assert seed==set(map(tuple,ref['seed'])) and len(seed)==16
 z,h3=poses[3];assert h3==2
 residue=(sum(z)%4,(z[0]-z[1])%4);assert residue in((1,1),(1,3),(3,1),(3,3));seen.add(residue)
 contact=ref['first_contact'];c=contact['time'];q=tuple(contact['cell']);rr,phi=divmod(c-entries[3]-182,104);assert phi in(46,56)
 # Exact all-past incoming ray collision inventory. No supplied old bit was read earlier.
 hits=[]
 for i,v in enumerate(Q):
  v=add(z,rot(v,1))
  for wi,w in enumerate(W):
   delta=(w[0]-w[1])-(v[0]-v[1])
   if delta%4:continue
   j=delta//4;pt=add(v,(2*j,-2*j));dd=sub(pt,w)
   if dd[0]==dd[1] and dd[0]%2==0:hits.append(dict(time=104*j+i,phase=i,period=j,cell=pt,old_W_index=wi))
 hits.sort(key=lambda v:(v['time'],v['old_W_index']));assert hits[0]['time']==104*rr+phi and tuple(hits[0]['cell'])==q
 # Assemble complete two-wake comparison field before that first read.
 fringe=set(C)
 for v in Q[:phi]:
  if v in fringe:fringe.remove(v)
  else:fringe.add(v)
 base=add(z,(2*rr,-2*rr));finite={add(base,rot(v,1)) for v in fringe}
 generators=[(w,(2,2),None)for w in W]+[(add(z,rot(w,1)),(2,-2),rr-1)for w in W]
 def initial(p):
  ans=p in finite
  for a,v,bound in generators:
   d=sub(p,a)
   if d[0]%v[0]==0 and d[1]==(d[0]//v[0])*v[1] and(bound is None or d[0]//v[0]<=bound):ans=not ans
  return ans
 # Freeze actual full history, including no earlier port reads and both L/R conditions.
 pre=''.join(A+U*r[i]+U[:j]for i,j in enumerate(joins));lastlen=c-len(pre)
 pre+=A+U*((lastlen-182)//104)+U[:(lastlen-182)%104];assert len(pre)==c
 F=ref['contact_future_word'];offset=ref['certification_cut']-ref['exact_onset'];tw=ref['tail_word'];shift=(-offset)%104;H=tw[shift:]+tw[:shift];assert H in{U[i:]+U[:i]for i in range(104)}
 allword=pre+F+H*2;B={u:-i-1 for i,u in enumerate(sorted(seed))};p=(0,0);h=1;first={};contact_board=None;birthpos={}
 for t,ch in enumerate(allword):
  if p in seed and p not in first:first[p]=t
  if t==c:
   contact_board=dict(B);assert p==q and h==2 and B[p]==contact['lifetime'] and contact['lifetime']>=0
  old=B.pop(p,None);assert (old is None)==(ch=='R'),(joins,t,p,ch,old)
  if old is None:B[p]=t;birthpos[t]=p;h=(h+1)%4
  else:h=(h-1)%4
  p=add(p,DXY[h])
 assert contact_board=={tuple(a['cell']):a['lifetime']for a in ref['contact_full_black']}
 for i,(o,hh) in enumerate(poses):
  for g in G:assert first[add(o,rot(g,hh-1))]==entries[i]+firstG[g]
 fw,fd,deaths,ft=future(B,p,h);assert fw==H and fd==tuple(ref['tail_drift'])
 # Fresh infinite comparison replay, then exact infinite input-line parity.
 pp=q;hh=2;changes=set()
 for i,ch in enumerate(F):
  b=initial(pp)^(pp in changes);assert b==(ch=='L'),(joins,i,pp,ch)
  if pp in changes:changes.remove(pp)
  else:changes.add(pp)
  hh=(hh+(-1 if b else 1))%4;pp=add(pp,DXY[hh])
 ideal_tail_finite=finite^changes;idrift,itests=infinite_tail(generators,ideal_tail_finite,pp,hh,H);assert idrift==fd
 assert F[-1]!=H[-1]
 # No actual encountered G launch, including crossings of the terminal cut.
 after=F+H*3
 assert not any(after.startswith(A[:33],i)for i in range(len(F)))
 assert not any((H*2).startswith(A[:33],i)for i in range(104))
 # Quotient duplicates agree on whole post-contact words, not merely period labels.
 value=(F,H,tuple(idrift),sub(pp,q),hh)
 if residue in class_words:assert class_words[residue]==value
 else:class_words[residue]=value
 out.append(dict(joins=joins,residue=residue,initial_black=sorted(seed),poses=poses,port_entry_times=entries,initial_first_reads=[dict(cell=v,time=first[v])for v in sorted(seed)],first_contact=contact,marked_birth_cell=birthpos[contact['lifetime']],old_phase=src['W'][hits[0]['old_W_index']]['phase'],incoming_phase=phi,all_past_first_contact_hits=hits,full_contact_black=[dict(cell=v,lifetime=i)for v,i in sorted(contact_board.items())],comparison_generators=generators,comparison_finite=sorted(finite),postcontact_word=F,exact_postcontact_delay=len(F),exact_onset=c+len(F),canonical_word=H,canonical_entry_pose=[pp,hh],canonical_drift=idrift,ideal_tail_finite=sorted(ideal_tail_finite),ideal_infinite_ray_tests=itests,full_finite_tail_parity_tests=ft,full_finite_terminal_black=[dict(cell=v,lifetime=i)for v,i in sorted(B.items())],full_finite_terminal_pose=[p,h],physical_updates=len(allword),no_encountered_G_prefix33=True))
 print(joins,residue,'old',out[-1]['old_phase'],'incoming',phi,'delay',len(F),'idealtests',sum(len(z['critical_copies'])for z in itests),'finite',ft,flush=True)
assert seen=={(1,1),(1,3),(3,1),(3,3)} and len(out)==8
# Positive regression to the independently signed330 source.
oldsrc=json.loads((P/'TRANSVERSE_FAR_MODULE_SOURCE.json').read_text());reg=next(r for r in out if r['joins']==[61,71,61]);assert reg['postcontact_word']==oldsrc['post_contact_word'] and reg['canonical_word']==oldsrc['tail_word']
report=dict(status='AUTHOR exact clockwise first-transverse-contact quotient; independent audit requested',scope='Four same-sector completed-old-wake / standard-incoming-wake classes, clockwise transverse approach only. Each has two literal n20 finite16-cell realizations with whole future canonical. No arbitrary archives, opposite transverse approach, or universal n-family claim.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in ['WRITTEN_WAKE_PORT_OBSTRUCTION_CHECKED.json','TRANSVERSE_JOIN_QUOTIENT_PROBES.json','TRANSVERSE_FAR_MODULE_SOURCE.json']},quotient_residues=sorted(seen),controls=out)
(P/'TRANSVERSE_FIRST_CONTACT_QUOTIENT_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
