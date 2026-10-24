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
(P/'OPPOSITE_EXACT_COMPLETION_PROBES.json').write_text(json.dumps(out,indent=2)+'\n')
