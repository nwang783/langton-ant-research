"""First unit-scale charge-preserving turn substitutions; finite conflicts only."""
import itertools,json,pathlib,hashlib,time
D=((0,1),(1,0),(0,-1),(-1,0));K=9

def replay(word,cap=None):
 x=y=h=0;last={};fuel=[]
 for t,c in enumerate(word if cap is None else itertools.islice(word,cap)):
  q=(x,y)
  if q in last and last[q][0]==c:return dict(status='CONFLICT',read=t,previous=last[q][1],cell=q,turn=c,first_L=len(fuel))
  if q not in last and c=='L':fuel.append(q)
  last[q]=(c,t);h=(h+(1 if c=='R' else 3))%4;x+=D[h][0];y+=D[h][1]
 return dict(status='PREFIX SURVIVOR',reads=t+1,pose=(x,y,h),first_L_cells=fuel)

def main():
 st=time.monotonic();R=[];L=[]
 for tup in itertools.product('RL',repeat=K):
  w=''.join(tup);e=w.count('R')-w.count('L');r=replay(w)
  if r['status']!='PREFIX SURVIVOR':continue
  if tuple(r['pose'])==(1,0,1) and e==1:R.append(w)
  if tuple(r['pose'])==(-1,0,3) and e==-1:L.append(w)
 records=[];survivors=[]
 for u in R:
  if u[0]!='R':continue
  for v in L:
   im={'R':u,'L':v}
   def letters(z,r):
    if not r:yield z
    else:
     for d in im[z]:yield from letters(d,r-1)
   ans=replay(letters('R',6),100000);ans.update(R=u,L=v)
   if ans['status']=='PREFIX SURVIVOR':survivors.append(ans)
   records.append(ans)
 p=pathlib.Path(__file__);raw=json.dumps(records,sort_keys=True,separators=(',',':')).encode()+b'\n';p.with_suffix('.records.json').write_bytes(raw)
 out=dict(k=K,scale=1,charge_preserving=True,R_images=R,L_images=L,cases=len(records),survivors=survivors,latest_conflict=max((r.get('read',-1) for r in records),default=None),records_sha256=hashlib.sha256(raw).hexdigest(),seconds=time.monotonic()-st)
 p.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
