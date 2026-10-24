"""Refine a frozen height/DFA model by canonical transverse interval controls.
CLI FAR_HEIGHT[_FIRST].json PREFIX [comma,separated,integer,upper,boundaries].
Preserves existing height/funding edges exactly and lifts only far controls.
Discovery implementation: any theorem requires independent model reconstruction.
"""
from pathlib import Path
import sys,json,hashlib,collections
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text())
assert J['format'] in ('guarded_reset_global_record_far_height_dfa_v1','guarded_reset_global_record_far_height_first_funding_v1')
B=json.loads(Path(J['base_model_file']).read_text());Q=json.loads(Path(J['literal_dfa_file']).read_text())
from resource_profile import load_profile
P,D,M=load_profile(Path(B['resource_profile_file']));G=D['geometry']['geometry'];V=json.loads(Path(B['potential_file']).read_text())['values'];assert V['ax']==V['ay']==1
phase=B['target_global_phase'];keep=B['keep'];near=len(B['poses']);far=[tuple(x)for x in J['far_controls']];oldinit=J['geometric_initial_control'];olddummy=J['geometric_dummy_goal'];assert oldinit==near+len(far)
bounds=sorted(set(map(int,sys.argv[3].split(','))))if len(sys.argv)>3 else [0,8]
intervals=[[None,bounds[0]]]+[[a+1,b]for a,b in zip(bounds,bounds[1:])]+[[bounds[-1]+1,None]] if bounds else [[None,None]]
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def transverse(q):x,y=rot(q,phase);return x-y
def band(z):return next(i for i,(lo,hi)in enumerate(intervals)if(lo is None or lo<=z)and(hi is None or z<=hi))
def possible(i,j,delta,h):
 lo,hi=intervals[i];a,b=intervals[j]
 los=[z for z in (lo,None if a is None else a-delta)if z is not None]
 his=[z for z in (hi,None if b is None else b-delta)if z is not None]
 if not los or not his:return True
 l=max(los);u=min(his);l+=(h-l)%2;return l<=u
lift=[];fi={}
for k,(h,q)in enumerate(far):
 for bi,(lo,hi)in enumerate(intervals):
  if lo is not None and hi is not None and lo+(h-lo)%2>hi:continue
  fi[k,bi]=near+len(lift);lift.append([k,h,q,bi])
init=near+len(lift);dummy=init+1;edges=[];prov=[]
def emit(e,fr,to,why):edges.append([fr,to,*e[2:]]);prov.append(why)
def target_endpoint(p,a):
 dx,dy=rot(G[a]['endpoint'][:2],p[2]);return[p[0]+dx,p[1]+dy,(p[2]+G[a]['endpoint'][2])%4]
def predecessor(p,a):
 h=(p[2]-G[a]['endpoint'][2])%4;dx,dy=rot(G[a]['endpoint'][:2],h);return[p[0]-dx,p[1]-dy,h]
for ei,e in enumerate(J['geometric_edges']):
 fr,to=e[:2];a=e[8]
 if fr<near:
  if to<near:emit(e,fr,to,['near_near',ei])
  elif to==olddummy:assert e[7];emit(e,fr,dummy,['goal',ei])
  else:
   assert near<=to<oldinit;ep=target_endpoint(B['poses'][fr],a);bi=band(transverse(ep[:2]));emit(e,fr,fi[to-near,bi],['near_far',ei,ep,bi])
 elif fr==oldinit:
  if to<near:emit(e,init,to,['initial_near',ei])
  else:
   assert near<=to<oldinit
   for bi in range(len(intervals)):
    if(to-near,bi)in fi:emit(e,init,fi[to-near,bi],['initial_far',ei,bi])
 else:
  assert near<=fr<oldinit;fk=fr-near;h,q=far[fk]
  if to<near:
   pred=predecessor(B['poses'][to],a);assert pred[2]==h;bi=band(transverse(pred[:2]));emit(e,fi[fk,bi],to,['far_near',ei,pred,bi])
  else:
   assert near<=to<oldinit;tk=to-near;hh=far[tk][0];delta=transverse(rot(G[a]['endpoint'][:2],h));assert(delta+h-hh)%2==0
   for bi in range(len(intervals)):
    if(fk,bi)not in fi:continue
    for bj in range(len(intervals)):
     if(tk,bj)in fi and possible(bi,bj,delta,h):emit(e,fi[fk,bi],fi[tk,bj],['far_far',ei,bi,bj,delta])
# Literal regular-language product, preserving every real packet.
adj=collections.defaultdict(list)
for ei,e in enumerate(edges):adj[e[0]].append((ei,e))
pairs=[(init,Q['initial_class'])];ids={pairs[0]:0};todo=collections.deque(pairs);TT=[];emap=[]
while todo:
 p,c=todo.popleft();fr=ids[p,c]
 for ei,e in adj[p]:
  a=e[8];cc=c if a==99 else Q['transitions'][c][keep.index(a)]
  if cc<0:continue
  z=(e[1],cc)
  if z not in ids:ids[z]=len(pairs);pairs.append(z);todo.append(z)
  TT.append([fr,ids[z],*e[2:]]);emap.append([ei,c,cc])
OUT=len(pairs)
N={'format':'guarded_reset_global_record_far_transverse_bands_v1','n':J['n'],'out':OUT,'poses':[B['poses'][p]if p<near else None for p,c in pairs],'points':B['points'],'start':[0,*J['start'][1:]],'reentry':[],'transitions':TT,'keep':keep,'height_model_file':str(src.resolve()),'height_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'base_model_file':J['base_model_file'],'base_model_sha256':J['base_model_sha256'],'literal_dfa_file':J['literal_dfa_file'],'literal_dfa_sha256':J['literal_dfa_sha256'],'resource_profile_file':J['resource_profile_file'],'resource_profile_sha256':J['resource_profile_sha256'],'transverse_boundaries':bounds,'transverse_intervals':intervals,'far_controls':lift,'geometric_initial_control':init,'geometric_dummy_goal':dummy,'geometric_edges':edges,'geometric_edge_provenance':prov,'position_map':pairs,'edge_map':emap,'scope':'Canonical transverse coordinate x-y after target phase rotation is retained in finite intervals. All prior height, strict-record and initial-funding constraints are unchanged. Far-to-far edges require a nonempty translated interval intersection with heading parity; near endpoints and far predecessors choose exact bands. Initial far destination bands are all admitted conservatively. Literal DFA history is never reset.'}
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {OUT+1} {len(TT)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in TT:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':N['n'],'far_controls':len(lift),'positions':OUT+1,'edges':len(TT),'transverse_intervals':intervals}))
