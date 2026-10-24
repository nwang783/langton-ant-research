from pathlib import Path
import json
exec(Path('check_transverse_first_contact_quotient.py').read_text().split('out=[];class_words={}')[0])
data=json.loads((P/'OPPOSITE_TRANSVERSE_FEEDBACK_CHECKED.json').read_text());out=[]
for c in data['controls']:
 B={tuple(z['cell']):z['lifetime']for z in c['first_contact_full']};gens=[(tuple(a),tuple(v),b)for a,v,b in c['pure_generators']];F=set(map(tuple,c['pure_finite']));q=tuple(c['first_contact']['cell']);word=c['pure_transient'];H=c['pure_word'];p,h,reads=move_word(q,0,word);p2,h2,tailreads=move_word(p,h,H);dr=sub(p2,p);assert dr==tuple(c['pure_tail_drift'])
 def ideal(x):
  ans=x in F
  for a,v,up in gens:
   dx,dy=sub(x,a)
   if dx%v[0]==0 and dy==(dx//v[0])*v[1]and(up is None or dx//v[0]<=up):ans=not ans
  return ans
 plus=set();minus=set()
 def test(x):
  if ideal(x)!=(x in B):(plus if ideal(x)else minus).add(x)
 for x in reads:test(x)
 for base in tailreads:
  ints=[]
  for a,v,up in gens:
   iv=line_interval(base,dr,a,v,up)
   if iv is not None:ints.append(iv)
  for x in F^set(B):
   dx,dy=sub(x,base)
   if dx%dr[0]==0 and dy==(dx//dr[0])*dr[1]and dx//dr[0]>=0:k=dx//dr[0];ints.append((k,k))
  critical={0}
  for a,b in ints:
   critical.add(a)
   if b is not None:critical.add(b+1)
  ks=sorted(critical)
  for i,k in enumerate(ks):
   if sum(k>=a and(b is None or k<=b)for a,b in ints)%2:
    assert i+1<len(ks),'infinite completion difference'
    for j in range(k,ks[i+1]):test(add(base,(j*dr[0],j*dr[1])))
 # Determine whether all desired edits are possible as initially unread additions.
 seed=set(map(tuple,c['initial_black']));BB=set(seed);pp=(0,0);hh=1;read=set()
 for t in range(c['first_contact']['time']):
  read.add(pp);old=pp in BB
  if old:BB.remove(pp);hh=(hh-1)%4
  else:BB.add(pp);hh=(hh+1)%4
  pp=add(pp,DXY[hh])
 assert BB==set(B)
 firsttimes={}
 for t,v in enumerate(reads):firsttimes.setdefault(v,t)
 for v in plus|minus:
  for i,base in enumerate(tailreads):
   dx,dy=sub(v,base)
   if dx%dr[0]==0 and dy==(dx//dr[0])*dr[1]and dx//dr[0]>=0:
    tt=len(word)+104*(dx//dr[0])+i
    firsttimes[v]=min(firsttimes.get(v,tt),tt)
 hard=(plus|minus)&read;earliest=min(hard,key=lambda v:firsttimes[v])
 r=dict(first_hard_difference=dict(cell=earliest,offset=firsttimes[earliest],global_ideal_time=c['first_contact']['time']+firsttimes[earliest],actual_cut_black=earliest in B,ideal_cut_black=ideal(earliest),current_lifetime=B.get(earliest)),residue=c['residue'],plus=sorted(plus),minus=sorted(minus),plus_already_read=sorted(plus&read),minus_already_read=sorted(minus&read));out.append(r)
 print('hard',r['first_hard_difference'],flush=True)
 print(c['residue'],'plus',len(plus),'minus',len(minus),'plusread',len(plus&read),'minusread',len(minus&read),'plus',sorted(plus)if len(plus)<30 else'',flush=True)
expected={(1,3):(0,34,0,34,29280),(1,1):(152,47,9,47,33280),(3,3):(0,30,0,30,5812),(3,1):(0,30,0,30,5840)}
for row in out:
 vals=(len(row['plus']),len(row['minus']),len(row['plus_already_read']),len(row['minus_already_read']),row['first_hard_difference']['offset'])
 assert vals==expected[tuple(row['residue'])]
 assert set(map(tuple,row['minus']))<=set(map(tuple,row['minus_already_read']))
# Tiny missing-input control: the next supposedly missing predecessor bit is FIXED WHITE.
base={(0,-1),(1,1),(1,3),(2,2)};p=(0,0);h=1;hits=[]
for t in range(182):
 black=p in base
 if p==(4,6):hits.append([t,'L'if black else'R'])
 if black:base.remove(p);h=(h-1)%4
 else:base.add(p);h=(h+1)%4
 p=add(p,DXY[h])
assert hits==[[136,'R'],[140,'L']] and (4,6)not in base
hard=next(x for x in out if x['residue']==[1,1])['first_hard_difference'];assert hard['cell']==(159,52) and not hard['actual_cut_black'] and hard['ideal_cut_black']
# Literal one-addition experiment preserves the full prefix, repairs exactly the first discrepancy,
# and then fails on that fixed WHITE bit. It is not an asserted working continuation.
c=next(x for x in data['controls']if x['residue']==[1,1]);joins=c['joins'];rvec=[100,30,150,60,100]
pre=''.join(A+U*rvec[i]+U[:j]for i,j in enumerate(joins));left=c['first_contact']['time']-len(pre);pre+=A+U*((left-182)//104)+U[:(left-182)%104]
board=set(map(tuple,c['initial_black']))|{(159,51)};p=(0,0);h=1;first_added=None;failure=None
for t,ch in enumerate(pre+c['pure_transient']):
 if p==(159,51)and first_added is None:first_added=t
 actual='L'if p in board else'R'
 if actual!=ch:failure=dict(time=t,cell=p,actual=actual,wanted=ch);break
 if p in board:board.remove(p);h=(h-1)%4
 else:board.add(p);h=(h+1)%4
 p=add(p,DXY[h])
assert first_added==82998 and failure==dict(time=82999,cell=(159,52),actual='R',wanted='L')
report=dict(status='AUTHOR exact fixed-prehistory incompatibility; independent audit requested',scope='Any initial board with the same initial pose and entire prescribed precontact turn word cannot realize the specified pure continuation through its first hard read. This is a fixed-word obstruction, not global regeneration or an actual clearing count.',source_hash=hashlib.sha256((P/'OPPOSITE_TRANSVERSE_FEEDBACK_CHECKED.json').read_bytes()).hexdigest(),controls=out,local_fixed_white_history=hits,single_unread_addition=dict(cell=[159,51],first_read=first_added,first_failure=failure))
(P/'OPPOSITE_PREHISTORY_OBSTRUCTION_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
