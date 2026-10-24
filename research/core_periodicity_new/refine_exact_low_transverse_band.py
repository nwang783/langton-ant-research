"""Refine a colored/Q/clock model by exact transverse head coordinate in a band.
CLI MODEL.json BAND PREFIX.
Outside the band retain separate left/right rays and t mod4. Low-height SCCs
retain their prior exact mod4 compiler, conservatively forgetting the band.
This is a discovery refinement, not independently audited record integration.
"""
from pathlib import Path
from collections import Counter
import sys,json,hashlib
src=Path(sys.argv[1]);T=int(sys.argv[2]);out=Path(sys.argv[3]);J=json.loads(src.read_text());A=json.loads(Path(J['base_model_file']).read_text());B=json.loads(Path(A['base_model_file']).read_text());S=json.loads(Path(B['base_model_file']).read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];nearset=set(map(tuple,S['poses']));nn=len(S['poses']);phase=S['target_global_phase'];assert phase==1
assert all(abs(x+y)<=T for x,y,h in nearset),'Band must contain EVERY retained-context pose.'
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def info(old):
 z=J['positions'][old]
 if z[0]=='near':
  x,y,h=B['poses'][z[1]];return z[0],h,y-x,x+y
 if z[0]=='far':
  geo,d=B['position_map'][z[1]];h,q=B['far_controls'][geo-nn];return z[0],h,q,z[2]
 return z[0],None,None,None
P=[];byold=[];ix={};I=[info(p)for p in range(len(J['positions']))]
for old,z in enumerate(J['positions']):
 typ,h,q,t=I[old];bs=[]
 if typ=='unused_out':byold.append(bs);continue
 if typ=='near':bs=[t]
 elif typ=='far':
  bs=['left','right']
  for tt in range(-T,T+1):
   if tt%4!=t:continue
   x,y=(tt-q)//2,(tt+q)//2;assert x+y==tt and y-x==q
   if(x,y,h)not in nearset:bs.append(tt)
 else:bs=[None]
 for b in bs:ix[old,b]=len(P);byold.append([])if False else None;P.append([old,b])
 byold.append(bs)
oldout=len(J['positions'])-1;assert J['positions'][oldout][0]=='unused_out';ix[oldout,None]=len(P);P.append([oldout,None]);byold[oldout]=[None]
def reaches(b,dt,tt):
 if isinstance(b,int):
  x=b+dt;return(tt=='left'and x<-T)or(tt=='right'and x>T)or(isinstance(tt,int)and x==tt)
 if b=='left':return tt=='left'or(isinstance(tt,int)and tt-dt < -T)
 if b=='right':return tt=='right'or(isinstance(tt,int)and tt-dt > T)
 raise AssertionError(b)
E=[];stats=Counter()
for ei,e in enumerate(J['transitions']):
 fr,to=e[:2];a=e[8];sf,st=I[fr][0],I[to][0]
 if a in[99,104]or e[7]or sf=='low_scc'or st=='low_scc':
  # Initial high t is arbitrary. Low interfaces remember only the signed
  # old t mod4 profile, hence all compatible band/ray realizations may occur.
  for b in byold[fr]:
   for tt in byold[to]:E.append([ix[fr,b],ix[to,tt],ei])
  stats['identity_or_low_or_goal']+=1;continue
 assert sf in['near','far']and st in['near','far'];h=I[fr][1];dt=sum(rot(G[a]['endpoint'][:2],h))
 for b in byold[fr]:
  for tt in byold[to]:
   if reaches(b,dt,tt):E.append([ix[fr,b],ix[to,tt],ei])
 stats['high_packet']+=1
start=[ix[J['start'][0],None],*J['start'][1:]]
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{J["n"]} {len(P)} {len(E)} 0\n');f.write(' '.join(map(str,start))+'\n')
 for fr,to,ei in E:f.write(' '.join(map(str,[fr,to,*J['transitions'][ei][2:]]))+'\n')
 f.write('\n')
M=dict(format='transverse_band_refined_guarded_reset_v1',n=J['n'],start=start,out=len(P)-1,source_file=str(src.resolve()),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),band=T,positions=P,transitions=E,source_position_kinds=dict(Counter(z[0]for z in J['positions'])),source_edge_stats=dict(stats),scope='Discovery-only simulation refinement of the supplied exact-low colored/Q/clock finite model. Exact high transverse coordinate inside the band; separate unbounded outside rays with old mod4 residue. Ray transitions are existential one-step interval abstractions. Every low interface conservatively forgets the band but preserves the old signed residue. No record no-hit theorem or full transverse exactness.')
out.with_suffix('.json').write_text(json.dumps(M,separators=(',',':'))+'\n');print(dict(positions=len(P),edges=len(E),band=T,stats=stats))
