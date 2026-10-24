"""Independent discrete-height reconstruction and finite-cube verification."""
from pathlib import Path
from collections import Counter
import json,sys,bisect
from check_dcuv_producer_model_independent import ROOT,digest,resolve_file,geometry,rotation,walk,raws
from check_record_transverse_independent import check as basecheck
from check_record_far_height_independent import datacheck,invariant,OUT
CACHE={}
def exact(path):
 path=Path(path).resolve()
 if path in CACHE:return CACHE[path]
 J=json.loads(path.read_text());assert J['format']=='guarded_reset_global_record_residual_height_bound_v1'
 bp=resolve_file(path,J['base_model_file']);assert digest(bp)==J['base_model_sha256'];basecheck(bp);B=json.loads(bp.read_text())
 H=json.loads(resolve_file(bp,B['height_model_file']).read_text());R=json.loads(resolve_file(bp,B['base_model_file']).read_text())
 phase=R['target_global_phase'];S=R['record_threshold'];I=R['initial_token_weight'];F=(S-I-1)//2;A=R['core_offsets'];T={(a,h):t for a,h,t in R['created_peaks']};keep=R['keep'];near=len(R['poses']);cut=H['lower_cutoff']
 def height(z):z=rotation(z,phase);return int(z.real+z.imag)
 ins={(a,h):max(height(rotation(z,h))for z in geometry[a]['inputs'])for a in keep for h in range(4)}
 outs={(a,h):max(height(rotation(z,h))for z in geometry[a]['outputs'])for a in keep for h in range(4)}
 tops={(a,h):(S-1-max(A[(h+phase)%4],T[a,(h+phase)%4]))//2 for a in keep for h in range(4)}
 cap=max([F]+[q-(q-h)%2+outs[a,h]for(a,h),q in tops.items()]);bits=max(1,(cap-F).bit_length());mask=(1<<bits)-1
 assert J['initial_height_bound']==F and J['height_upper_bound']==cap and J['height_bits']==J['color_bit_shift']==bits
 def domain(p):
  if p<near:
   x,y,h=R['poses'][p];q=height(complex(x,y));return h,q,q
  _,h,q,_=B['far_controls'][p-near];return h,q,cut if q is None else q
 expected=[];probes=0
 for ei,e in enumerate(B['geometric_edges']):
  fr,to=e[:2];a=e[8];goal=bool(e[7]);first=fr==B['geometric_initial_control']
  if first:
   old=B['geometric_edge_provenance'][ei][1];why=H['geometric_edge_provenance'][old]
   if why[0]=='first_far':h,q=why[1:3];lo=q;hi=cut if q is None else q
   else:
    assert why[0]=='first_entry';_,aa,x,y,h,*_=why;assert aa==a;lo=hi=height(complex(x,y))
  else:h,lo,hi=domain(fr)
  z,dh=walk(raws[a])[:2];delta=height(rotation(z,h))
  if not goal:
   hh,dl,du=domain(to);assert hh==(h+dh)%4
   if dl is not None:lo=dl-delta if lo is None else max(lo,dl-delta)
   hi=min(hi,du-delta,tops[a,h])
  if first:hi=min(hi,F-ins[a,h])
  relation=set()
  for old in ([F]if first else range(F,cap+1)):
   upper=min(hi,old-ins[a,h])
   # Below old-max_output every admissible q has the identical new value old.
   # One extra parity pair below that threshold exactly represents the whole
   # unbounded lower tail. All remaining distinct q are enumerated literally.
   lower=lo if lo is not None else min(upper,old-outs[a,h])-2
   for q in range(lower,upper+1):
    if(q-h)%2:continue
    new=old if goal else max(old,q+outs[a,h]);assert F<=new<=cap
    relation.add((old,new));probes+=1
  assert set(map(tuple,J['geometric_height_relations'][ei]))==relation,(ei,relation,J['geometric_height_relations'][ei])
  expected.append(relation)
 assert len(J['geometric_height_relations'])==len(B['geometric_edges'])
 rows=0
 for ti,t in enumerate(B['transitions']):
  gi=B['edge_map'][ti][0]
  for old,new in sorted(expected[gi]):
   fr,to,k,v,f,c,r,g,a=t;wanted=[fr,to,(k<<bits)|mask,(v<<bits)|(old-F),f<<bits,(c<<bits)|mask,(r<<bits)|(new-F),g,a]
   assert J['transitions'][rows]==wanted and J['edge_map'][rows]==[ti,old,new];rows+=1
 assert rows==len(J['transitions']) and J['n']==B['n']+bits and J['out']==B['out'] and J['reentry']==[]
 assert J['start']==[B['start'][0],(B['start'][1]<<bits)|mask,B['start'][2]<<bits]
 datacheck(path,J)
 result={'status':'PASS independent global residual-height interval relations and full graph lifting','variables':J['n'],'height_range':[F,cap],'geometric_relations':len(expected),'literal_height_probes':probes,'edges':rows,'hashes':{str(p.relative_to(ROOT)):digest(p)for p in(path,path.with_suffix('.dat'),bp)},'scope':'Monotone historical residual-height upper bound, not an exclusion without invariant.'}
 invariant(path,result);(OUT/(path.stem+'.height_model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
 CACHE[path]=(J,B,expected);return CACHE[path]
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text())
 if J['format']=='guarded_reset_global_record_residual_height_bound_v1':exact(path);return
 coarse=J['format']=='guarded_reset_global_record_residual_height_coarse_v1'
 assert coarse or J['format']=='guarded_reset_global_record_residual_height_compressed_v1'
 key='exact_height_model'if coarse else'uncompressed_model';ep=resolve_file(path,J[key+'_file']);assert digest(ep)==J[key+'_sha256'];E,B,relations=exact(ep)
 F=E['initial_height_bound'];cap=E['height_upper_bound'];vals=J['height_values']if coarse else list(range(F,cap+1));assert vals==sorted(set(vals)) and vals[0]==F and vals[-1]==cap
 bits=J['height_bits'];assert bits==max(1,(len(vals)-1).bit_length());mask=(1<<bits)-1;ix={v:i for i,v in enumerate(vals)};ops=J['height_cube_operations'];assert len(ops)==len(relations);tests=0
 for ri,relation in enumerate(relations):
  expected={(ix[x],bisect.bisect_left(vals,y))for x,y in relation if x in ix};actual=set()
  for old in range(1<<bits):
   for k,v,c,r in ops[ri]:
    assert not((k|v|c|r)>>bits) and v&~k==r&~c==0
    if(old&k)==v:actual.add((old,(old&~c)|r))
   tests+=1
  assert expected==actual,ri
  if coarse:assert set(map(tuple,J['geometric_height_relations'][ri]))==expected
 row=0
 for ti,t in enumerate(B['transitions']):
  gi=B['edge_map'][ti][0]
  for oi,(qk,qv,qc,qr)in enumerate(ops[gi]):
   fr,to,k,v,f,c,r,g,a=t;wanted=[fr,to,(k<<bits)|qk,(v<<bits)|qv,f<<bits,(c<<bits)|qc,(r<<bits)|qr,g,a]
   assert J['transitions'][row]==wanted and J['edge_map'][row]==[ti,gi,oi];row+=1
 assert row==len(J['transitions']) and J['n']==B['n']+bits and J['out']==B['out'] and J['reentry']==[]
 assert J['start']==[B['start'][0],(B['start'][1]<<bits)|mask,B['start'][2]<<bits]
 datacheck(path,J);result={'status':'PASS independent '+('upward coarse-height rounding'if coarse else'exact finite-height cube compression'),'variables':J['n'],'height_values':vals,'binary_truth_tests':tests,'edges':row,'hashes':{str(p.relative_to(ROOT)):digest(p)for p in(path,path.with_suffix('.dat'),ep)},'scope':'No case exclusion without checked invariant.'}
 invariant(path,result);(OUT/(path.stem+'.height_model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
