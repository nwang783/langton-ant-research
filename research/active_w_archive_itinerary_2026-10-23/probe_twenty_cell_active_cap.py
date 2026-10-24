"""Targeted actual20-cell feedback controls; no all-n mass claim inferred."""
from check_active_itineraries import *
G0={(0,-1),(1,1),(2,2),(1,3)}
def rot(q,r):
 x,y=q
 for _ in range(r%4):x,y=y,-x
 return x,y

def probe(n):
 assert n>=20 and n%2==0
 poses=[((0,0),1),((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)]
 B=set()
 for p,h in poses:
  B|={(p[0]+v[0],p[1]+v[1])for z in G0 for v in[rot(z,h-1)]}
 assert len(B)==20
 p=(0,0);h=1;k=wwhich(p,h);G=FullGraph(B,k);e=624*n-1516;end=e+774+312;maxC=0;firstmax=None;r=0;renewals=0;birthrenew=None;deathrenew=None;runs=[];target=(0,2)
 for t in range(end):
  w=cursors(p,h)[1];C=edges(G,w)
  if len(C)>maxC:maxC=len(C);firstmax=t
  if 61<=t<=e:
   flag=target in C
   if not runs or runs[-1][0]!=flag:runs.append([flag,0,t])
   runs[-1][1]+=1
  q=p;c='L'if q in B else'R';u,v=endpoints(q,k);other=v if u==w else u
  if c=='L':
   nb=other in vertices(edges(G,w,skip=q),k);ex=r>=3 or nb
   if ex:renewals+=1
   if q==target:
    assert t==e;deathrenew=renewals
   B.remove(q);G.delete(q);h=(h-1)%4;r=0
  else:
   if t==60:assert q==target;birthrenew=renewals
   B.add(q);G.add(q);h=(h+1)%4;r+=1
  D=((0,1),(1,0),(0,-1),(-1,0));p=(p[0]+D[h][0],p[1]+D[h][1])
 assert sum(a[1]for a in runs)==e-60 and runs[0][0]and runs[-1][0]
 return{'n':n,'verified_physical_updates':end,'global_active_mass_max_through_control':maxC,'first_max_cut':firstmax,'target_R_birth':60,'target_consumption':e,'actual_lifetime_age':e-60,'actual_renewal_age':deathrenew-birthrenew,'target_active_dormant_episodes':runs,'scope':'actual finite prefix plus312 certified-standard-tail control updates; all-n cap not inferred'}
if __name__=='__main__':
 out=[probe(n)for n in(20,40,80)]
 (OUT/'twenty_cell_active_cap_probe.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
