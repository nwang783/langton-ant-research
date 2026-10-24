"""Exact possible coarse owners, including every allowed fine heading phase."""
import itertools,collections,json
from search_position_only_inflations import HERE,trace,seed,rotate,mul,D

def inventory(k,a,theta):
 words=[]
 for tup in itertools.product('RL',repeat=k):
  w=''.join(tup)
  if seed(w)is not None:words.append(w)
 rec=[]
 for Hc in range(4):
  for c in'RL':
   target=mul(a,D[(Hc+(1 if c=='R'else-1))%4])
   for Hf in range(4):
    if Hf%2!=((k%2)*Hc+theta)%2:continue
    for w in words:
     if rotate(*trace(w)[1][:2],Hf)!=target:continue
     events=[(*rotate(x,y,Hf),z)for x,y,h,z in trace(w)[0]]
     first={}
     for x,y,z in events:first.setdefault((x,y),z)
     rec.append(dict(Hc=Hc,Hf=Hf,c=c,word=w,firstL=[p for p,z in first.items()if z=='L'],offsets=sorted(first)))
 return rec

def check(k,a,theta):
 rec=inventory(k,a,theta);norm=sum(v*v for v in a);out=[]
 for target in rec:
  if target['Hc']!=0 or target['c']!='R':continue
  witnesses=[]
  for x,y in target['firstL']:
   own=set()
   for other in rec:
    for X,Y in other['offsets']:
     dx,dy=x-X,y-Y;u=dx*a[0]+dy*a[1];v=dy*a[0]-dx*a[1]
     if u%norm or v%norm:continue
     q=u//norm,v//norm
     if (q[0]+q[1]-other['Hc'])%2:continue
     own.add(q)
   witnesses.append(dict(cell=[x,y],owners=sorted(own),private=own=={(0,0)},forward=all(q[1]>=0 for q in own)))
  out.append(dict(word=target['word'],fine_heading=target['Hf'],witnesses=witnesses,protected=any(w['forward']for w in witnesses)))
 return dict(k=k,scale=a,theta=theta,records=len(rec),target_images=out,all_protected=bool(out)and all(r['protected']for r in out))
if __name__=='__main__':
 results=[]
 for k in range(2,6):
  for r in json.load(open(HERE/f'position_only_k{k}.json'))['results']:
   if r['status']=='EXHAUSTED':continue
   for theta in([0]if k%2 else[0,1]):
    z=check(k,tuple(r['scale']),theta);results.append(z);print(k,r['scale'],theta,z['all_protected'],[(r['word'],r['fine_heading'])for r in z['target_images']if not r['protected']],flush=True)
 (HERE/'position_only_ownership_2_5.json').write_text(json.dumps(results,indent=2))
