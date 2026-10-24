"""Replace initial-far epsilon by its first literal packet with exact funding cut.
CLI FAR_HEIGHT_MODEL.json PREFIX. All residual inputs of the entire-prefix first
packet are initial, including forgotten transverse cells. Their activation is
therefore determined solely by retained height and heading. Ordinary later
geometric edges are unchanged. Initial near poses were already excluded.
"""
from pathlib import Path
import json,sys,hashlib,collections
from resource_profile import load_profile
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());assert J['format']=='guarded_reset_global_record_far_height_dfa_v1';B=json.loads(Path(J['base_model_file']).read_text());assert B['format']=='guarded_reset_global_record_initial_out_v1';P,D,M=load_profile(Path(B['resource_profile_file']));G=D['geometry']['geometry'];Q=json.loads(Path(J['literal_dfa_file']).read_text());W=json.loads(Path(B['potential_file']).read_text());v=W['values'];phase=B['target_global_phase'];S=B['record_threshold'];I=B['initial_token_weight'];A=B['core_offsets'];T={(a,h):z for a,h,z in B['created_peaks']};keep=B['keep'];near=len(B['poses']);far=[tuple(z)for z in J['far_controls']];fi={z:near+i for i,z in enumerate(far)};cut=J['lower_cutoff'];init=J['geometric_initial_control'];dummy=J['geometric_dummy_goal'];edges=[];provenance=[]
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(q):z=rot(q,phase);return v['ax']*z[0]+v['ay']*z[1]
def funding_bound(a,h):return (S-I-1)//2-max(ht(rot(q,h))for q in G[a]['inputs'])
for i,(e,why)in enumerate(zip(J['geometric_edges'],J['geometric_edge_provenance'])):
 if e[0]!=init:edges.append(e);provenance.append(['unchanged',i])
first=[]
def firstedge(to,a,why):
 row=[init,to,0,0,0,0,0,0,a];edges.append(row);provenance.append(why);first.append({'edge':row,'reason':why})
for h,q in far:
 for a in keep:
  e=G[a]['endpoint'];hh=(h+e[2])%4;delta=ht(rot(e[:2],h));record=(S-1-max(A[(h+phase)%4],T[a,(h+phase)%4]))//2;fuel=funding_bound(a,h);limit=min(record,fuel)
  if q is None:
   qm=min(cut,limit);qm-=(qm-h)%2;dest=[(hh,None)]+[(hh,z)for z in range(cut+1,qm+delta+1)if(z+hh)%2==0]
  elif q<=limit:qm=q;dest=[(hh,None if q+delta<=cut else q+delta)]
  else:continue
  for d in dest:
   assert d in fi
   firstedge(fi[d],a,['first_far',h,q,a,d[0],d[1],record,fuel,qm])
for e,why in zip(J['geometric_edges'],J['geometric_edge_provenance']):
 if why[0]!='entry':continue
 _,a,x,y,h,to=why;fuel=funding_bound(a,h);q=ht((x,y))
 if q<=fuel:firstedge(to,a,['first_entry',a,x,y,h,to,fuel])
# Exact deterministic-language product, with no initial epsilon left.
adj=collections.defaultdict(list)
for ei,e in enumerate(edges):adj[e[0]].append((ei,e))
empty=Q['initial_class'];pairs=[(init,empty)];ids={pairs[0]:0};queue=collections.deque(pairs);TT=[];emap=[]
while queue:
 p,c=queue.popleft();fr=ids[p,c]
 for ei,e in adj[p]:
  a=e[8];assert a in keep;cc=Q['transitions'][c][keep.index(a)]
  if cc<0:continue
  z=(e[1],cc)
  if z not in ids:ids[z]=len(pairs);pairs.append(z);queue.append(z)
  TT.append([fr,ids[z],*e[2:]]);emap.append([ei,c,cc])
OUT=len(pairs);N={**J,'format':'guarded_reset_global_record_far_height_first_funding_v1','far_height_base_file':str(src.resolve()),'far_height_base_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'out':OUT,'poses':[B['poses'][p]if p<near else None for p,c in pairs],'start':[0,*J['start'][1:]],'transitions':TT,'geometric_edges':edges,'geometric_edge_provenance':provenance,'position_map':pairs,'edge_map':emap,'first_packet_funding':{'initial_weight':I,'record_threshold':S,'heading_packet_height_bounds':[[h,a,funding_bound(a,h)]for h in range(4)for a in keep],'first_edges':first},'scope':J['scope']+' Initial far epsilon is contracted with the actual first packet, whose full physical residual inputs all have initial activation < threshold. Later far packets retain the original conservative abstraction.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {OUT+1} {len(TT)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in TT:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':N['n'],'positions':OUT+1,'edges':len(TT),'first_geometric_edges':len(first),'I':I}))
