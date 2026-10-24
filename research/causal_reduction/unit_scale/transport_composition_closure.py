"""Exact legal composition semigroup, not a word-length exclusion.
Every phase has independent R/L images from identity plus the six internally
legal charge-preserving unit-nine words. We append phases on the RIGHT.
Caps are inconclusive, never proofs. No prior generator is imported.
"""
import itertools,json,pathlib,hashlib,time,argparse
from collections import deque,Counter
D=((0,1),(1,0),(0,-1),(-1,0))
def trace(w):
 x=y=h=0;seen={}
 for t,c in enumerate(w):
  q=(x,y)
  if q in seen and seen[q][0]==c:return {'conflict':t,'previous':seen[q][1],'cell':q,'turn':c}
  seen[q]=(c,t);h=(h+(1 if c=='R' else -1))%4;x+=D[h][0];y+=D[h][1]
 return {'pose':(x,y,h)}
def palette():
 out={'R':['R'],'L':['L']}
 for z in itertools.product('RL',repeat=9):
  w=''.join(z);charge=w.count('R')-w.count('L')
  if charge not in (1,-1):continue
  tr=trace(w)
  if 'pose' not in tr:continue
  if tr['pose']==(charge,0,charge%4):out['R' if charge==1 else 'L'].append(w)
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--states',type=int,default=100000);ap.add_argument('--length',type=int,default=10000);ap.add_argument('--ballot',action='store_true');args=ap.parse_args()
 pal=palette()
 def ballot(w,c):
  q=0
  for z in w:
   q+=1 if z=='R' else -1
   if q<min(0,c):return False
  return True
 phases=[(u,v) for u in pal['R'] for v in pal['L'] if not args.ballot or ballot(u,1) and ballot(v,-1)]
 states=[('R','L')];ids={states[0]:0};parents=[None];depth=[0];q=deque([0]);edges=[];conflicts=[];caps=[];start=time.monotonic()
 while q:
  i=q.popleft();u,v=states[i];f={'R':u,'L':v}
  for j,(a,b) in enumerate(phases):
   ws=tuple(''.join(f[c] for c in z) for z in (a,b))
   ans=[trace(w) for w in ws]
   bad=next((k for k in (0,1) if 'conflict' in ans[k]),None)
   if bad is not None:
    conflicts.append([i,j,bad,ans[bad]]);continue
   if ws in ids:edges.append([i,j,ids[ws]]);continue
   if max(map(len,ws))>args.length or len(states)>=args.states:
    caps.append([i,j,list(map(len,ws))]);continue
   ni=len(states);ids[ws]=ni;states.append(ws);parents.append([i,j]);depth.append(depth[i]+1);q.append(ni);edges.append([i,j,ni])
 outdir=pathlib.Path(__file__).parent;name='transport_composition_ballot' if args.ballot else 'transport_composition_all'
 data={'palette':pal,'phases':phases,'states':[{'images':s,'parent':p,'depth':d} for s,p,d in zip(states,parents,depth)],'edges':edges,'conflicts':conflicts,'caps':caps}
 raw=json.dumps(data,sort_keys=True,separators=(',',':')).encode()+b'\n';(outdir/(name+'.records.json')).write_bytes(raw)
 out={'status':'COMPLETE FINITE CLOSURE' if not caps else 'INCONCLUSIVE CAP','phase_count':len(phases),'state_count':len(states),'legal_edges':len(edges),'conflicts':len(conflicts),'caps':len(caps),'max_image_length':max(max(map(len,s)) for s in states),'max_depth':max(depth),'length_histogram':dict(Counter(max(map(len,s)) for s in states)),'records_sha256':hashlib.sha256(raw).hexdigest(),'seconds':time.monotonic()-start}
 (outdir/(name+'.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
