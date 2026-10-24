"""On-demand synthesis of heading-dependent identity/nine unit transports.
Only growing fixed roots with incoming north are tested. Different headings
have independent choices. A prefix survivor is NOT an all-time certificate.
"""
import itertools,json,pathlib,time,hashlib,collections
D=((0,1),(1,0),(0,-1),(-1,0))
CAP=10000

def legal_image(w,target):
 x=y=h=0;last={}
 for c in w:
  if last.get((x,y))==c:return False
  last[x,y]=c;h=(h+(1 if c=='R' else -1))%4;x+=D[h][0];y+=D[h][1]
 return (x,y,h)==target

def inventories():
 r=[];l=[]
 for z in itertools.product('RL',repeat=9):
  w=''.join(z);e=w.count('R')-w.count('L')
  if e==1 and legal_image(w,(1,0,1)):r.append(w)
  if e==-1 and legal_image(w,(-1,0,3)):l.append(w)
 return [['R']+r,['L']+l]

def search(root,dom):
 ass=[None]*8;P=[root];board={};trail=[];records=[];survivors=[];nodes=0;latest=0;maxi=0;covered=0
 def go(i,t,x,y,h):
  nonlocal nodes,latest,maxi,covered
  nodes+=1;maxi=max(maxi,i)
  save=(len(P),len(trail));conf=None
  while t<CAP:
   assert i<len(P)
   s=P[i]
   if ass[s] is None:
    choices=dom[s%2]
    if i==0:choices=[w for w in choices if len(w)>1 and w[0]=='RL'[root%2]]
    for w in choices:
     ass[s]=w;go(i,t,x,y,h)
    ass[s]=None
    break
   assert h==s//2
   for c in ass[s]:
    actual=2*h+(c=='L')
    if t<len(P):
     if P[t]!=actual:conf=dict(kind='state',read=t);break
    else:P.append(actual)
    q=(x,y);old=board.get(q)
    if old==c:
     conf=dict(kind='color',read=t,cell=q,turn=c);break
    trail.append((q,old));board[q]=c
    h=(h+(1 if c=='R' else -1))%4;x+=D[h][0];y+=D[h][1];t+=1
    if t==CAP:break
   if conf is not None:break
   i+=1;maxi=max(maxi,i)
  if conf is not None:
   latest=max(latest,conf['read']);n=sum(w is None for w in ass);weight=7**n;covered+=weight
   records.append(dict(assignment=ass.copy(),unassigned=n,completion_weight=weight,**conf))
  elif t==CAP:
   survivors.append(dict(assignment=ass.copy(),reads=t,pose=(x,y,h),coarse_reads=i))
  while len(trail)>save[1]:
   q,old=trail.pop()
   if old is None:del board[q]
   else:board[q]=old
  del P[save[0]:]
 go(0,0,0,0,0)
 return dict(root=root,nodes=nodes,latest_conflict=latest,max_coarse_reads=maxi,covered_rooted_controllers=covered,expected_rooted_controllers=4*7**7,conflict_branches=len(records),survivors=survivors),records

def main():
 st=time.monotonic();dom=inventories();out=[];records=[]
 for root in [0,1]:
  a,b=search(root,dom);out.append(a);records.extend(dict(root=root,**q) for q in b)
 p=pathlib.Path(__file__);raw=(json.dumps(records,sort_keys=True,separators=(',',':'))+'\n').encode();p.with_suffix('.records.json').write_bytes(raw)
 ans=dict(scope='eight independent heading-turn images, identity or legal charge-preserving unit length9; growing fixed root only',state_order=['N-R','N-L','E-R','E-L','S-R','S-L','W-R','W-L'],domains=dom,prefix_cap=CAP,results=out,seconds=time.monotonic()-st,records_sha256=hashlib.sha256(raw).hexdigest())
 p.with_suffix('.json').write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps(ans))
if __name__=='__main__':main()
