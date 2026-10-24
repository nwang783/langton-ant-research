"""Intersect a guarded-reset graph with exact finite-window packet legality.
CLI BASE.json DFA.json PREFIX. An OUT reentry conservatively resets word memory.
No extra color bits. All near transitions append their actual packet label.
"""
from pathlib import Path
import sys,json,hashlib
source,dfa,out=map(Path,sys.argv[1:4]);J=json.loads(source.read_text());Q=json.loads(dfa.read_text());assert Q['format']=='literal_packet_window_dfa_v1';alphabet=Q['keep'];assert J.get('keep',alphabet)==alphabet;assert hashlib.sha256(Path(Q['geometry_file']).read_bytes()).hexdigest()==Q['geometry_sha256'];nc=len(Q['classes']);empty=Q['initial_class'];oldOUT=J['out'];OUT=oldOUT*nc;mapping=[(p,c)for p in range(oldOUT)for c in range(nc)];T=[];edge_map=[];excluded=0

def pos(p,c):return OUT if p==oldOUT else p*nc+c
for ei,row in enumerate(J['transitions']):
 p,to,k,v,f,cl,r,g,a=row;assert p!=oldOUT and a in alphabet, 'Use an unpruned residual/OUT-only model with literal packet edges.'
 for c in range(nc):
  cc=Q['transitions'][c][alphabet.index(a)]
  if cc<0:excluded+=1;continue
  T.append([pos(p,c),pos(to,cc),k,v,f,cl,r,g,a]);edge_map.append([ei,c,cc])
start=[pos(J['start'][0],empty),*J['start'][1:]];re=[pos(p,empty)for p in J['reentry']];poses=[J['poses'][p]if p<len(J['poses'])else None for p,c in mapping]
N={'format':'guarded_reset_literal_dfa_product_v1','n':J['n'],'out':OUT,'poses':poses,'points':J.get('points',[]),'start':start,'reentry':re,'transitions':T,'base_model_file':str(source.resolve()),'base_model_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'literal_dfa_file':str(dfa.resolve()),'literal_dfa_sha256':hashlib.sha256(dfa.read_bytes()).hexdigest(),'position_map':mapping,'edge_map':edge_map,'dfa_initial_class':empty,'resource_profile_file':J.get('resource_profile_file'),'resource_profile_sha256':J.get('resource_profile_sha256'),'scope':'Exact packet-window language intersection within each contiguous near block. OUT forgets all suffix memory; no constraint is asserted about unobserved hidden words.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {OUT+1} {len(T)} {len(re)}\n");f.write(' '.join(map(str,start))+'\n')
 for t in T:f.write(' '.join(map(str,t))+'\n')
 f.write(' '.join(map(str,re))+'\n')
print(json.dumps({'variables':N['n'],'positions':OUT+1,'dfa_classes':nc,'transitions':len(T),'forbidden_packet_steps':excluded}))
