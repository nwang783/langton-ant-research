"""Independent exact tensor product, preserving OUT's deliberate suffix forgetfulness."""
from pathlib import Path
import json,sys,subprocess
from check_dcuv_producer_model_independent import ROOT,digest,resolve_file
from check_packet_window_dfa_independent import check as dfacheck
from check_global_record_initial_out_independent import check as outcheck
from check_global_record_first_funding_independent import check as firstcheck
OUT=ROOT/'audits/record_dfa_product_replays';OUT.mkdir(exist_ok=True)
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_reset_literal_dfa_product_v1'
 bp=resolve_file(path,J['base_model_file']);dp=resolve_file(path,J['literal_dfa_file']);assert digest(bp)==J['base_model_sha256']and digest(dp)==J['literal_dfa_sha256']
 B=json.loads(bp.read_text());Q=json.loads(dp.read_text());dfacheck(dp)
 if B['format']=='guarded_reset_global_record_initial_out_v1':outcheck(bp)
 elif B['format']=='guarded_reset_global_record_first_funding_v1':firstcheck(bp)
 else:raise AssertionError('Unreviewed product base '+B['format'])
 nc=len(Q['classes']);initial=Q['initial_class'];alphabet=Q['keep'];o=B['out']*nc
 positions=[(p,c)for p in range(B['out'])for c in range(nc)]
 def idx(p,c):return o if p==B['out']else p*nc+c
 rows=[];edge_map=[]
 for i,row in enumerate(B['transitions']):
  p,to,k,v,f,cl,r,g,a=row;assert p!=B['out']and a in alphabet
  for c in range(nc):
   dest=Q['transitions'][c][alphabet.index(a)]
   if dest<0:continue
   rows.append([idx(p,c),idx(to,dest),k,v,f,cl,r,g,a]);edge_map.append([i,c,dest])
 poses=[B['poses'][p]if p<len(B['poses'])else None for p,c in positions]
 start=[idx(B['start'][0],initial),*B['start'][1:]];reentry=[idx(p,initial)for p in B['reentry']]
 for key,value in [('n',B['n']),('out',o),('poses',poses),('points',B['points']),('start',start),('reentry',reentry),('transitions',rows),('position_map',[list(q)for q in positions]),('edge_map',edge_map),('dfa_initial_class',initial),('resource_profile_file',B['resource_profile_file']),('resource_profile_sha256',B['resource_profile_sha256'])]:assert J[key]==value,key
 lines=[f"{B['n']} {o+1} {len(rows)} {len(reentry)}",' '.join(map(str,start))]+[' '.join(map(str,r))for r in rows]+[' '.join(map(str,reentry))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 result={'status':'PASS independent literal-window graph product','variables':B['n'],'positions':o+1,'window':Q['window'],'classes':nc,'edges':len(rows),'reentries':len(reentry),'hashes':{str(p.relative_to(ROOT)):digest(p)for p in(path,path.with_suffix('.dat'),bp,dp)},'scope':'Necessary finite factor constraints within near blocks only. No whole-case exclusion without a checked invariant.'}
 if path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');subprocess.run([str(ROOT/'audits/check_guarded_reset_bdd64_invariant_independent'),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True);result['invariant']=json.loads(dest.read_text())
 (OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 for path in sys.argv[1:]:check(path)
