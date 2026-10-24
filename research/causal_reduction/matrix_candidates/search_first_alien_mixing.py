"""First alien-coarse-vertex member of a justified mixing family, half-turn class."""
import itertools,json,pathlib,time,hashlib
P=pathlib.Path(__file__).parent;D=((0,1),(1,0),(0,-1),(-1,0));K=17;A=((3,2),(2,9));DET=23

def replay(word,h,cap=None):
 x=y=0;seen={}
 for t,d in enumerate(word if cap is None else itertools.islice(word,cap)):
  c=(d-h)%4
  if c not in (1,3):return dict(status='AXIS',read=t)
  if (x,y) in seen and seen[x,y][0]==c:return dict(status='CONFLICT',read=t,previous=seen[x,y][1],cell=[x,y],turn=c)
  seen[x,y]=(c,t);x+=D[d][0];y+=D[d][1];h=d
 return dict(status='PREFIX SURVIVOR',reads=t+1)

def inventory(z):
 tx=A[0][0]*D[z][0]+A[0][1]*D[z][1];ty=A[1][0]*D[z][0]+A[1][1]*D[z][1]
 nh=K//2+(z%2);nv=K-nh;out=[];raw=0
 for west in itertools.combinations(range(nh),(nh-tx)//2):
  for south in itertools.combinations(range(nv),(nv-ty)//2):
   raw+=1;w=[];h=v=0
   for j in range(K):
    if (j+z)%2:w.append(3 if h in west else 1);h+=1
    else:w.append(2 if v in south else 0);v+=1
   hs=[h for h in range(4) if(h-z)%2 and replay(w,h)['status']=='PREFIX SURVIVOR']
   if not hs:continue
   x=y=0;hits=[]
   for j,d in enumerate(w):
    if (A[1][1]*x-A[0][1]*y)%DET==0 and(-A[1][0]*x+A[0][0]*y)%DET==0:
     u,v=(A[1][1]*x-A[0][1]*y)//DET,(-A[1][0]*x+A[0][0]*y)//DET
     if (u,v) not in ((0,0),D[z]):hits.append([j,x,y,u,v])
    x+=D[d][0];y+=D[d][1]
   out.append(dict(word=w,headings=hs,alien_hits=hits))
 return raw,out

def main():
 st=time.monotonic();re,E=inventory(1);rn,N=inventory(0);p=P/f'first_alien_mixing_k{K}';p.mkdir(exist_ok=True)
 inv=dict(k=K,matrix=A,raw=[re,rn],legal=[len(E),len(N)],alien_images=[sum(bool(z['alien_hits']) for z in E),sum(bool(z['alien_hits']) for z in N)],E=E,N=N)
 (p/'inventory.json').write_text(json.dumps(inv,indent=2)+'\n');print({k:v for k,v in inv.items() if k not in('E','N')},flush=True)
 cases=[];surv=[];pruned=0
 for i,u in enumerate(E):
  for j,v in enumerate(N):
   if not u['alien_hits'] and not v['alien_hits']:pruned+=1;continue
   im={1:tuple(u['word']),0:tuple(v['word']),3:tuple((d+2)%4 for d in u['word']),2:tuple((d+2)%4 for d in v['word'])}
   def letters(z,l):
    if l==0:yield z
    else:
     for d in im[z]:yield from letters(d,l-1)
   for root in(1,0):
    per=1 if im[root][0]==root else 2
    for h in ((root+1)%4,(root+3)%4):
     r=replay(letters(root,4),h,10000);r.update(east=i,north=j,root=root,heading=h,period=per);cases.append(r)
     if r['status']=='PREFIX SURVIVOR':surv.append(r)
 raw=json.dumps(cases,sort_keys=True,separators=(',',':')).encode()+b'\n';(p/'records.json').write_bytes(raw)
 out=dict(k=K,matrix=A,total_pairs=len(E)*len(N),theorem_excluded_pairs=pruned,residual_pairs=len(E)*len(N)-pruned,cases=len(cases),latest_conflict=max((r.get('read',-1) for r in cases),default=None),survivors=surv,records_sha256=hashlib.sha256(raw).hexdigest(),seconds=time.monotonic()-st)
 (p/'result.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
