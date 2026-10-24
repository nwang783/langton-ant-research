"""Independent interval-relation reconstruction of labelled far-height controls.
Uses the independently replayed literal residual base and finite factor language.
No imports from the author generator; far steps are rebuilt by pairwise integer
interval intersection rather than its endpoint enumeration.
"""
from pathlib import Path
from collections import Counter,defaultdict,deque
import json,sys,subprocess
from check_dcuv_producer_model_independent import ROOT,geometry,core,rotation,xy,walk,raws,mark,digest,resolve_file
from check_global_record_initial_out_independent import check as initialcheck
from check_packet_window_dfa_independent import check as dfacheck
OUT=ROOT/'audits/record_far_height_replays';OUT.mkdir(exist_ok=True)
def datacheck(path,J):
 lines=[f"{J['n']} {J['out']+1} {len(J['transitions'])} {len(J['reentry'])}",' '.join(map(str,J['start']))]+[' '.join(map(str,t))for t in J['transitions']]+[' '.join(map(str,J['reentry']))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
def invariant(path,result):
 if path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');subprocess.run([str(ROOT/'audits/check_guarded_reset_bdd64_invariant_independent'),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True)
  result['invariant']=json.loads(dest.read_text());result['hashes'][str(path.with_suffix('.bdd').relative_to(ROOT))]=digest(path.with_suffix('.bdd'))
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_reset_global_record_far_height_dfa_v1'
 bp=resolve_file(path,J['base_model_file']);dp=resolve_file(path,J['literal_dfa_file']);assert digest(bp)==J['base_model_sha256']and digest(dp)==J['literal_dfa_sha256']
 initialcheck(bp);dfacheck(dp);B=json.loads(bp.read_text());Q=json.loads(dp.read_text())
 assert B['format']=='guarded_reset_global_record_initial_out_v1';assert B['keep']==Q['keep']==J['keep'];keep=B['keep']
 P=json.loads(Path(B['potential_file']).read_text());v=P['values'];phase=B['target_global_phase'];S=B['record_threshold'];A=B['core_offsets'];T={(a,h):t for a,h,t in B['created_peaks']}
 assert v['ax']%2==v['ay']%2==1
 height=lambda p:int(rotation(p,phase).real*v['ax']+rotation(p,phase).imag*v['ay'])
 poses=[tuple(p)for p in B['poses']];posindex={p:i for i,p in enumerate(poses)};patch={complex(*p)for p in B['points']};cut=J['lower_cutoff'];assert type(cut)is int
 upper=[(S-1-A[(h+phase)%4])//2 for h in range(4)]
 far=[(h,q)for h in range(4)for q in [None,*range(cut+1,upper[h]+1)]if q is None or(q-h)%2==0]
 assert J['height_upper_bounds']==upper and J['far_controls']==[list(t)for t in far]
 controls={z:len(poses)+i for i,z in enumerate(far)};init=len(poses)+len(far);goal=init+1
 assert J['geometric_initial_control']==init and J['geometric_dummy_goal']==goal
 literal=[]
 for a,raw in enumerate(raws):
  z,dh,_,_=walk(raw);req=walk(raw+mark)[2];literal.append((z,dh,req))
  if a in keep:assert core<=set(req)and set(geometry[a]['outputs'])<=set(req)and{z+rotation(c,dh)for c in core}<=set(req)
 def endpoint(p,a):
  x,y,h=p;z,dh,_=literal[a];return(*xy(complex(x,y)+rotation(z,h)),(h+dh)%4)
 def band(p):
  h=p[2];q=height(complex(*p[:2]));assert(q-h)%2==0 and q<=upper[h];return controls[h,None if q<=cut else q]
 expected=[];provenance=[]
 def add(row,why):expected.append(row);provenance.append(why)
 for ei,t in enumerate(B['transitions']):
  assert t[0]<len(poses)and t[8]in keep
  ep=endpoint(poses[t[0]],t[8]);dest=goal if t[7]else posindex.get(ep)
  if dest is None:dest=band(ep)
  if not t[7]:assert t[1]==posindex.get(ep,B['out'])
  add([t[0],dest,*t[2:]],['near',ei])
 # q lies in source interval, the strict pre-packet peak half-line, and
 # destination interval shifted by the exact displacement. All are integral.
 def interval(q):return(None,cut)if q is None else(q,q)
 for h,q in far:
  lo,hi=interval(q)
  for a in keep:
   z,dh,_=literal[a];hh=(h+dh)%4;delta=height(rotation(z,h));limit=(S-1-max(A[(h+phase)%4],T[a,(h+phase)%4]))//2
   assert(delta+hh-h)%2==0
   for desth,destq in far:
    if desth!=hh:continue
    dlo,dhi=interval(destq);lower=[x for x in [lo,None if dlo is None else dlo-delta]if x is not None];lower=max(lower)if lower else None
    high=min(hi,limit,dhi-delta)
    if lower is not None:
     lower+=(h-lower)%2
     if lower>high:continue
    add([controls[h,q],controls[hh,destq],0,0,0,0,0,0,a],['far',h,q,a,hh,destq])
 for i,p in enumerate(poses):
  for a in keep:
   z,dh,_=literal[a];h=(p[2]-dh)%4;pre=complex(*p[:2])-rotation(z,h);pred=(*xy(pre),h)
   if pred in posindex:continue
   q=height(pre)
   if(q-h)%2 or 2*q+max(A[(h+phase)%4],T[a,(h+phase)%4])>=S:continue
   assert all(not({pre+rotation(r,h)for r in literal[b][2]}&patch)for b in keep)
   add([band(pred),i,0,0,0,0,0,0,a],['entry',a,*pred,i])
 for f in controls.values():add([init,f,0,0,0,0,0,0,99],['initial_far',f])
 assert Counter(map(tuple,J['geometric_edges']))==Counter(map(tuple,expected))
 assert Counter((tuple(a),tuple(b))for a,b in zip(J['geometric_edges'],J['geometric_edge_provenance']))==Counter((tuple(a),tuple(b))for a,b in zip(expected,provenance))
 # Reconstruct the reachable product using stored geometric edge order only
 # after independently proving that exact labelled multiset complete.
 adj=defaultdict(list)
 for ei,e in enumerate(J['geometric_edges']):adj[e[0]].append((ei,e))
 pairs=[(init,Q['initial_class'])];ids={pairs[0]:0};rows=[];emap=[]
 for p,c in pairs:
  for ei,e in adj[p]:
   label=e[8];cc=c if label==99 else Q['transitions'][c][keep.index(label)]
   if cc<0:continue
   dest=e[1],cc
   if dest not in ids:ids[dest]=len(pairs);pairs.append(dest)
   rows.append([ids[p,c],ids[dest],*e[2:]]);emap.append([ei,c,cc])
 fields={'position_map':[list(t)for t in pairs],'edge_map':emap,'transitions':rows,'poses':[list(poses[p])if p<len(poses)else None for p,c in pairs],'out':len(pairs),'start':[0,(1<<B['n'])-1,0],'reentry':[],'points':B['points'],'n':B['n'],'resource_profile_file':B['resource_profile_file'],'resource_profile_sha256':B['resource_profile_sha256']}
 for k,val in fields.items():assert J[k]==val,k
 datacheck(path,J)
 result={'status':'PASS independently reconstructed integer-height/heading and literal-language product','target':B['target'],'phase':phase,'initial_weight':B['initial_token_weight'],'variables':B['n'],'near_poses':len(poses),'far_controls':len(far),'positions':J['out']+1,'geometric_edges':len(expected),'product_edges':len(rows),'hashes':{str(p.relative_to(ROOT)):digest(p)for p in(path,path.with_suffix('.dat'),bp,dp)}}
 invariant(path,result);(OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
