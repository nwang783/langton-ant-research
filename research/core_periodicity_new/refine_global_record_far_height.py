"""Replace instantaneous OUT jumps by conservative height/heading packet walks.
CLI OUT_ONLY_BASE.json DFA.json PREFIX [LOWER_CUTOFF].
The transverse coordinate is forgotten only at poses whose EVERY complete packet
context avoids the retained patch. Actual packet labels remain visible to DFA.
Discovery model pending independent reconstruction; never claims no-hit at a cap.
"""
from pathlib import Path
import sys,json,hashlib,collections
from resource_profile import load_profile
src,df,out=map(Path,sys.argv[1:4]);J=json.loads(src.read_text());Q=json.loads(df.read_text());assert J.get('initial_out_normalization');assert J['start'][0]==J['out'] and J['start'][1]==(1<<J['n'])-1 and J['start'][2]==0
P,D,M=load_profile(Path(J['resource_profile_file']));G=D['geometry']['geometry'];K=set(map(tuple,D['geometry']['core']));W=json.loads(Path(J['potential_file']).read_text());v=W['values'];keep=P['keep'];assert keep==Q['keep'];assert hashlib.sha256(Path(Q['geometry_file']).read_bytes()).hexdigest()==Q['geometry_sha256'];phase=J['target_global_phase'];S=J['record_threshold'];A=J['core_offsets'];T={(a,h):z for a,h,z in J['created_peaks']};pts=set(map(tuple,J['points']));poses=list(map(tuple,J['poses']));si={p:i for i,p in enumerate(poses)};oldOUT=J['out'];assert all(t[8] in keep for t in J['transitions']);assert v['ax']%2 and v['ay']%2

def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(q):x,y=rot(q,phase);return v['ax']*x+v['ay']*y
def add(q,z):return q[0]+z[0],q[1]+z[1]
def end(p,a):x,y,h=p;ex,ey,eh=G[a]['endpoint'];z=rot((ex,ey),h);return x+z[0],y+z[1],(h+eh)%4
cut=int(sys.argv[4])if len(sys.argv)>4 else min(ht(p[:2])for p in poses)-2
upper=[(S-1-A[(h+phase)%4])//2 for h in range(4)];far=[]
for h in range(4):
 far.append((h,None))
 far.extend((h,q)for q in range(cut+1,upper[h]+1)if(q+h)%2==0)
fi={z:len(poses)+i for i,z in enumerate(far)};init=len(poses)+len(far);dummy=init+1;edges=[];provenance=[]
def farid(p):
 x,y,h=p;q=ht((x,y));assert(q+h)%2==0 and q<=upper[h],(p,q,upper[h]);return fi[h,None if q<=cut else q]
def edge(t,why):edges.append(t);provenance.append(why)
for a in keep:
 g=G[a];C={tuple(z[:2])for z in g['requirements']};ex,ey,eh=g['endpoint'];assert K<=C and set(map(tuple,g['outputs']))<=C and {add((ex,ey),rot(q,eh))for q in K}<=C
# Existing exact near packet edges, changing only endpoints formerly mapped OUT.
for ei,t in enumerate(J['transitions']):
 t=t[:];p=poses[t[0]];ep=end(p,t[8]);assert t[0]<len(poses)
 if t[7]:t[1]=dummy
 elif t[1]==oldOUT:t[1]=farid(ep)
 else:assert poses[t[1]]==ep
 edge(t,['near',ei])
# Every far head can perform a packet only under the strict record cut.
# At any fixed height, arbitrary transverse translation avoids the finite patch.
for (h,q),p in fi.items():
 for a in keep:
  eh=G[a]['endpoint'][2];hh=(h+eh)%4;delta=ht(rot(G[a]['endpoint'][:2],h));limit=(S-1-max(A[(h+phase)%4],T[a,(h+phase)%4]))//2
  if q is None:
   qm=min(cut,limit);qm-=(qm-h)%2;dest=[(hh,None)]+[(hh,z)for z in range(cut+1,qm+delta+1)if(z+hh)%2==0]
  elif q<=limit:dest=[(hh,None if q+delta<=cut else q+delta)]
  else:continue
  for d in dest:
   assert d in fi,(h,q,a,d,upper)
   edge([p,fi[d],0,0,0,0,0,0,a],['far',h,q,a,d[0],d[1]])
# An entry into an exact near pose must be an actual one-packet predecessor.
for to,p in enumerate(poses):
 for a in keep:
  ex,ey,eh=G[a]['endpoint'];h=(p[2]-eh)%4;z=rot((ex,ey),h);pred=(p[0]-z[0],p[1]-z[1],h)
  if pred in si:continue
  q=ht(pred[:2])
  if(q+h)%2 or 2*q+max(A[(h+phase)%4],T[a,(h+phase)%4])>=S:continue
  assert not({add(pred[:2],rot(r[:2],h))for r in G[a]['requirements']}&pts)
  edge([farid(pred),to,0,0,0,0,0,0,a],['entry',a,*pred,to])
for f in fi.values():edge([init,f,0,0,0,0,0,0,99],['initial_far',f])
# Regular-language product. Here 99 is truly epsilon, not a hidden excursion.
adj=collections.defaultdict(list)
for ei,e in enumerate(edges):adj[e[0]].append((ei,e))
empty=Q['initial_class'];pairs=[(init,empty)];ids={pairs[0]:0};pd=collections.deque(pairs);outedges=[];emap=[]
while pd:
 p,c=pd.popleft();fr=ids[p,c]
 for ei,e in adj[p]:
  a=e[8];cc=c if a==99 else Q['transitions'][c][keep.index(a)]
  if cc<0:continue
  dest=(e[1],cc)
  if dest not in ids:ids[dest]=len(pairs);pairs.append(dest);pd.append(dest)
  outedges.append([fr,ids[dest],*e[2:]]);emap.append([ei,c,cc])
OUT=len(pairs);outposes=[list(poses[p])if p<len(poses)else None for p,c in pairs]
N={'format':'guarded_reset_global_record_far_height_dfa_v1','n':J['n'],'out':OUT,'poses':outposes,'points':J['points'],'start':[0,*J['start'][1:]],'reentry':[],'transitions':outedges,'keep':keep,'base_model_file':str(src.resolve()),'base_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'literal_dfa_file':str(df.resolve()),'literal_dfa_sha256':hashlib.sha256(df.read_bytes()).hexdigest(),'resource_profile_file':J['resource_profile_file'],'resource_profile_sha256':J['resource_profile_sha256'],'lower_cutoff':cut,'height_upper_bounds':upper,'far_controls':far,'geometric_initial_control':init,'geometric_dummy_goal':dummy,'geometric_edges':edges,'geometric_edge_provenance':provenance,'position_map':pairs,'edge_map':emap,'scope':'All physical packets are retained, even far from the color patch. Far controls forget transverse position and collapse lower heights by existential interval transitions. DFA history is never reset. Initial far position is arbitrary and all retained residual bits are white.'}
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {OUT+1} {len(outedges)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in outedges:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':N['n'],'near_poses':len(poses),'far_controls':len(far),'lower_cutoff':cut,'positions':OUT+1,'edges':len(outedges)}))
