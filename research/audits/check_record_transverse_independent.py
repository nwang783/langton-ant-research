"""Independent conservative transverse-box lift of reviewed far-height graphs."""
from pathlib import Path
from collections import Counter,defaultdict
import json,sys
from check_dcuv_producer_model_independent import ROOT,rotation,xy,walk,raws,digest,resolve_file
from check_record_far_height_independent import check as farcheck,datacheck,invariant,OUT
from check_record_far_first_independent import check as firstcheck

def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_reset_global_record_far_transverse_bands_v1'
 hp=resolve_file(path,J['height_model_file']);assert digest(hp)==J['height_model_sha256'];H=json.loads(hp.read_text())
 if H['format']=='guarded_reset_global_record_far_height_first_funding_v1':firstcheck(hp)
 else:assert H['format']=='guarded_reset_global_record_far_height_dfa_v1';farcheck(hp)
 B=json.loads(Path(H['base_model_file']).read_text());Q=json.loads(Path(H['literal_dfa_file']).read_text());v=json.loads(Path(B['potential_file']).read_text())['values'];assert v['ax']==v['ay']==1
 phase=B['target_global_phase'];near=len(B['poses']);oldfar=[tuple(z)for z in H['far_controls']];oldinit=H['geometric_initial_control'];oldgoal=H['geometric_dummy_goal'];assert oldinit==near+len(oldfar)
 bounds=J['transverse_boundaries'];assert all(type(t)is int for t in bounds)and bounds==sorted(set(bounds));intervals=[]
 for i in range(len(bounds)+1):intervals.append([None if i==0 else bounds[i-1]+1,None if i==len(bounds)else bounds[i]])
 assert J['transverse_intervals']==intervals
 def exists(lo,hi,parity):
  return lo is None or hi is None or lo+(parity-lo)%2<=hi
 controls=[]
 for f,(h,q)in enumerate(oldfar):
  for band,(lo,hi)in enumerate(intervals):
   if exists(lo,hi,h):controls.append([f,h,q,band])
 ids={(f,b):near+i for i,(f,h,q,b)in enumerate(controls)};init=near+len(controls);goal=init+1
 assert J['far_controls']==controls and J['geometric_initial_control']==init and J['geometric_dummy_goal']==goal
 def coordinate(z):z=rotation(z,phase);return int(z.real-z.imag)
 def which(z):return sum(z>b for b in bounds)
 ends=[walk(raw)[:2]for raw in raws]
 def translated_possible(i,j,delta,h):
  lo,hi=intervals[i];lo2,hi2=intervals[j]
  lows=[t for t in [lo,None if lo2 is None else lo2-delta]if t is not None];highs=[t for t in [hi,None if hi2 is None else hi2-delta]if t is not None]
  return exists(max(lows)if lows else None,min(highs)if highs else None,h)
 expected=[]
 for e in H['geometric_edges']:
  fr,to=e[:2];a=e[8]
  if fr<near:
   if to<near:expected.append(e)
   elif to==oldgoal:assert e[7];expected.append([fr,goal,*e[2:]])
   else:
    p=B['poses'][fr];z,dh=ends[a];end=complex(*p[:2])+rotation(z,p[2]);expected.append([fr,ids[to-near,which(coordinate(end))],*e[2:]])
  elif fr==oldinit:
   if to<near:expected.append([init,to,*e[2:]])
   else:
    for b in range(len(intervals)):
     if(to-near,b)in ids:expected.append([init,ids[to-near,b],*e[2:]])
  else:
   assert near<=fr<oldinit;f=fr-near;h=oldfar[f][0]
   if to<near:
    p=B['poses'][to];z,dh=ends[a];assert (p[2]-dh)%4==h;pre=complex(*p[:2])-rotation(z,h)
    expected.append([ids[f,which(coordinate(pre))],to,*e[2:]])
   else:
    assert near<=to<oldinit;g=to-near;delta=coordinate(rotation(ends[a][0],h));hh=oldfar[g][0];assert(delta+h-hh)%2==0
    for i in range(len(intervals)):
     for j in range(len(intervals)):
      if(f,i)in ids and(g,j)in ids and translated_possible(i,j,delta,h):expected.append([ids[f,i],ids[g,j],*e[2:]])
 assert Counter(map(tuple,J['geometric_edges']))==Counter(map(tuple,expected))
 adj=defaultdict(list)
 for ei,e in enumerate(J['geometric_edges']):adj[e[0]].append((ei,e))
 pairs=[(init,Q['initial_class'])];pi={pairs[0]:0};rows=[];emap=[]
 for p,c in pairs:
  for ei,e in adj[p]:
   cc=c if e[8]==99 else Q['transitions'][c][B['keep'].index(e[8])]
   if cc<0:continue
   dest=e[1],cc
   if dest not in pi:pi[dest]=len(pairs);pairs.append(dest)
   rows.append([pi[p,c],pi[dest],*e[2:]]);emap.append([ei,c,cc])
 for k,val in [('transitions',rows),('position_map',[list(p)for p in pairs]),('edge_map',emap),('poses',[B['poses'][p]if p<near else None for p,c in pairs]),('out',len(pairs)),('start',[0,*H['start'][1:]]),('reentry',[])]:assert J[k]==val,k
 for k in ['n','points','keep','base_model_file','base_model_sha256','literal_dfa_file','literal_dfa_sha256','resource_profile_file','resource_profile_sha256']:assert J[k]==H[k],k
 datacheck(path,J);result={'status':'PASS independent transverse interval lift','target':B['target'],'phase':phase,'variables':J['n'],'initial_weight':B['initial_token_weight'],'far_controls':len(controls),'positions':J['out']+1,'geometric_edges':len(expected),'edges':len(rows),'hashes':{str(p.relative_to(ROOT)):digest(p)for p in[path,path.with_suffix('.dat'),hp]}}
 invariant(path,result);(OUT/(path.stem+'.transverse_model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
