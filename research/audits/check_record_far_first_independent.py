"""Independent first-far funding interval intersection and labelled product."""
from pathlib import Path
from collections import Counter,defaultdict
import json,sys
from check_record_far_height_independent import check as basecheck,datacheck,invariant,OUT
from check_dcuv_producer_model_independent import ROOT,geometry,rotation,xy,walk,raws,digest,resolve_file

def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_reset_global_record_far_height_first_funding_v1'
 fp=resolve_file(path,J['far_height_base_file']);assert digest(fp)==J['far_height_base_sha256'];basecheck(fp);F=json.loads(fp.read_text())
 B=json.loads(Path(F['base_model_file']).read_text());Q=json.loads(Path(F['literal_dfa_file']).read_text());v=json.loads(Path(B['potential_file']).read_text())['values']
 phase=B['target_global_phase'];S=B['record_threshold'];I=B['initial_token_weight'];keep=B['keep'];A=B['core_offsets'];T={(a,h):t for a,h,t in B['created_peaks']};cut=F['lower_cutoff'];near=len(B['poses']);far=[tuple(t)for t in F['far_controls']];idx={t:near+i for i,t in enumerate(far)};init=F['geometric_initial_control']
 height=lambda z:int(rotation(z,phase).real*v['ax']+rotation(z,phase).imag*v['ay'])
 bound={(h,a):min((S-I-1-2*height(rotation(z,h)))//2 for z in geometry[a]['inputs'])for h in range(4)for a in keep}
 assert J['first_packet_funding']['initial_weight']==I and J['first_packet_funding']['record_threshold']==S
 assert J['first_packet_funding']['heading_packet_height_bounds']==[[h,a,bound[h,a]]for h in range(4)for a in keep]
 expected=[e for e in F['geometric_edges']if e[0]!=init];first=[]
 # Each source and destination bin is an arithmetic interval. Intersect with
 # EVERY input-funding inequality before abstracting its exact endpoint.
 def interval(q):return(None,cut)if q is None else(q,q)
 for h,q in far:
  lo,hi=interval(q)
  for a in keep:
   z,dh=walk(raws[a])[:2];hh=(h+dh)%4;delta=height(rotation(z,h));record=(S-1-max(A[(h+phase)%4],T[a,(h+phase)%4]))//2
   for h2,q2 in far:
    if h2!=hh:continue
    dl,du=interval(q2);low=[x for x in [lo,None if dl is None else dl-delta]if x is not None];low=max(low)if low else None;high=min(hi,du-delta,record,bound[h,a])
    if low is not None:
     low+=(h-low)%2
     if low>high:continue
    first.append([init,idx[h2,q2],0,0,0,0,0,0,a])
 for e,why in zip(F['geometric_edges'],F['geometric_edge_provenance']):
  if why[0]!='entry':continue
  _,a,x,y,h,to=why
  if height(complex(x,y))<=bound[h,a]:first.append([init,to,0,0,0,0,0,0,a])
 expected+=first
 assert Counter(map(tuple,J['geometric_edges']))==Counter(map(tuple,expected))
 assert Counter(tuple(z['edge'])for z in J['first_packet_funding']['first_edges'])==Counter(map(tuple,first))
 assert all(e[8]in keep for e in J['geometric_edges'])
 adj=defaultdict(list)
 for ei,e in enumerate(J['geometric_edges']):adj[e[0]].append((ei,e))
 pairs=[(init,Q['initial_class'])];ids={pairs[0]:0};rows=[];emap=[]
 for p,c in pairs:
  for ei,e in adj[p]:
   cc=Q['transitions'][c][keep.index(e[8])]
   if cc<0:continue
   dest=e[1],cc
   if dest not in ids:ids[dest]=len(pairs);pairs.append(dest)
   rows.append([ids[p,c],ids[dest],*e[2:]]);emap.append([ei,c,cc])
 for k,val in [('transitions',rows),('position_map',[list(p)for p in pairs]),('edge_map',emap),('poses',[B['poses'][p]if p<near else None for p,c in pairs]),('out',len(pairs)),('start',[0,(1<<B['n'])-1,0]),('reentry',[])]:assert J[k]==val,k
 for k in ['n','points','keep','base_model_file','base_model_sha256','literal_dfa_file','literal_dfa_sha256','resource_profile_file','resource_profile_sha256','lower_cutoff','height_upper_bounds','far_controls','geometric_initial_control','geometric_dummy_goal']:assert J[k]==F[k],k
 datacheck(path,J);result={'status':'PASS independent first-far funding composition','variables':J['n'],'target':B['target'],'phase':phase,'initial_weight':I,'positions':J['out']+1,'first_geometric_edges':len(first),'edges':len(rows),'hashes':{str(p.relative_to(ROOT)):digest(p)for p in[path,path.with_suffix('.dat'),fp]}}
 invariant(path,result);(OUT/(path.stem+'.first_model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
