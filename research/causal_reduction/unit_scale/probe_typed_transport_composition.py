"""Local gluing test: independent physical-state refinement of a primitive9.
No global controller claim or arbitrary finite-fuel conclusion from survivors.
"""
import json,pathlib,time,hashlib,collections
from search_heading_transport import inventories,D

def search(w,dom):
 h=0;states=[]
 for c in w:
  states.append(2*h+(c=='L'));h=(h+(1 if c=='R' else -1))%4
 ass=[None]*8;board={};trail=[];out=[];records=[];survivors=[];nodes=0;covered=0
 def go(i,t,x,y,h):
  nonlocal nodes,covered
  nodes+=1;save=len(trail);sv=len(out)
  if i==len(states):
   assert all(a is not None for a in ass)
   survivors.append(dict(assignment=ass.copy(),word=''.join(out),length=t));return
  s=states[i];assert s//2==h
  choices=dom[s%2] if ass[s] is None else [ass[s]];new=ass[s] is None
  for a in choices:
   ass[s]=a;xx,yy,hh,tt=x,y,h,t;conf=None
   for c in a:
    q=(xx,yy);old=board.get(q)
    if old==c:conf=dict(read=tt,cell=q,turn=c);break
    trail.append((q,old));board[q]=c;out.append(c)
    hh=(hh+(1 if c=='R' else -1))%4;xx+=D[hh][0];yy+=D[hh][1];tt+=1
   if conf is None:go(i+1,tt,xx,yy,hh)
   else:
    u=sum(z is None for z in ass);covered+=7**u
    records.append(dict(assignment=ass.copy(),completion_weight=7**u,**conf))
   while len(trail)>save:
    q,old=trail.pop()
    if old is None:del board[q]
    else:board[q]=old
   del out[sv:]
  if new:ass[s]=None
 go(0,0,0,0,0)
 assert covered+len(survivors)==7**8
 return dict(primitive=w,nodes=nodes,conflict_cubes=len(records),covered=covered,survivors=len(survivors),latest_conflict=max(r['read'] for r in records),length_histogram=dict(collections.Counter(z['length'] for z in survivors))),records,survivors

def main():
 start=time.monotonic();dom=inventories();results=[];records=[];survivors=[]
 for words in dom:
  for w in words[1:]:
   a,b,c=search(w,dom);results.append(a);records.extend(dict(primitive=w,**v) for v in b);survivors.extend(dict(primitive=w,**v) for v in c);print(json.dumps(a),flush=True)
 p=pathlib.Path(__file__);r=(json.dumps(records,sort_keys=True,separators=(',',':'))+'\n').encode();s=(json.dumps(survivors,sort_keys=True,separators=(',',':'))+'\n').encode()
 p.with_suffix('.records.json').write_bytes(r);p.with_suffix('.survivors.json').write_bytes(s)
 ans=dict(scope='one typed outer phase applied to each primitive nine-image; initial heading N by global rotational symmetry',results=results,seconds=time.monotonic()-start,records_sha256=hashlib.sha256(r).hexdigest(),survivors_sha256=hashlib.sha256(s).hexdigest())
 p.with_suffix('.json').write_text(json.dumps(ans,indent=2)+'\n')
 print(json.dumps(ans),flush=True)
if __name__=='__main__':main()
