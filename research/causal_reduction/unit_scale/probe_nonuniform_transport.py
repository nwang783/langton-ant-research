"""One concrete variable-length unit-transport architecture; finite conflicts only.
Fixed R image is the nine-step three-corner-to-four-corner transport.  The L
image alone varies, at length13 and exact charge-1.  This is not an all-length
unit-scale classification or an all-time positive verifier.
"""
import hashlib,itertools,json,pathlib,time
D=((0,1),(1,0),(0,-1),(-1,0))
U='RLLLLRRRR'

def replay(word,cap=None):
 x=y=h=0;last={};fuel=[];n=0
 for t,c in enumerate(word if cap is None else itertools.islice(word,cap)):
  q=(x,y)
  if q in last and last[q][0]==c:
   return dict(status='CONFLICT',read=t,previous=last[q][1],cell=q,turn=c,first_L=len(fuel))
  if q not in last and c=='L':fuel.append(q)
  last[q]=(c,t);h=(h+(1 if c=='R' else -1))%4
  x+=D[h][0];y+=D[h][1];n=t+1
 return dict(status='PREFIX SURVIVOR',reads=n,pose=(x,y,h),first_L_cells=fuel)

def main():
 start=time.monotonic();V=[];raw=0
 for slots in itertools.combinations(range(13),6):
  z=set(slots);v=''.join('R' if i in z else 'L' for i in range(13))
  h=x=y=0
  for c in v:
   h=(h+(1 if c=='R' else -1))%4;x+=D[h][0];y+=D[h][1]
  if (x,y,h)!=(-1,0,3):continue
  raw+=1
  if replay(v)['status']=='PREFIX SURVIVOR':V.append(v)
 records=[]
 for v in V:
  im={'R':U,'L':v}
  def letters(c,r):
   if r==0:yield c
   else:
    for d in im[c]:yield from letters(d,r-1)
  a=replay(letters('R',6),100000);a['L']=v;records.append(a)
 p=pathlib.Path(__file__);b=(json.dumps(records,sort_keys=True,separators=(',',':'))+'\n').encode();p.with_suffix('.records.json').write_bytes(b)
 out=dict(scope='fixed R length9 transport, independent L length13, unit scale and exact charges',R=U,raw_geometric_L_images=raw,legal_L_images=V,cases=len(records),survivors=[z for z in records if z['status']!='CONFLICT'],latest_conflict=max((z.get('read',-1) for z in records),default=None),records_sha256=hashlib.sha256(b).hexdigest(),seconds=time.monotonic()-start)
 p.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
