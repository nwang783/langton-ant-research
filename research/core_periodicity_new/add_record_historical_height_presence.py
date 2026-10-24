"""Historical residual-height presence, retaining holes ignored by scalar Q.
CLI UNCOMPRESSED_Q_MODEL.json PREFIX. Adds one high bit per possible height>F.
All retained spatial colors remain unchanged. Initial high heights absent;
actual packet residual inputs require their levels, outputs install levels.
Deletions are ignored, hence this is a conservative historical resource.
"""
from pathlib import Path
import sys,json,hashlib
src,out=map(Path,sys.argv[1:3]);Q=json.loads(src.read_text());assert Q['format']=='guarded_reset_global_record_residual_height_bound_v1';B=json.loads(Path(Q['base_model_file']).read_text());O=json.loads(Path(B['base_model_file']).read_text());G=json.loads((Path(O['resource_profile_file']).parent/'literal_residual_geometry.json').read_text())['geometry'];phase=O['target_global_phase'];F=Q['initial_height_bound'];cap=Q['height_upper_bound'];nb=cap-F;n=B['n'];assert n+nb<=50;hm=((1<<nb)-1)<<n

def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(z):return sum(rot(z,phase))
relations=[];details=[]
for ei,(e,d)in enumerate(zip(B['geometric_edges'],Q['geometric_relation_details'])):
 a=e[8];h=d['heading'];ins=[ht(rot(z,h))for z in G[a]['inputs']];outs=[ht(rot(z,h))for z in G[a]['outputs']];lo=d['source_height_lower'];hi=d['source_height_upper'];deep=F-max(ins+outs);qq=[]
 q=min(hi,deep);q-=(q-h)%2
 if lo is None or q>=lo:qq.append(q)
 q=deep+1 if lo is None else max(lo,deep+1);q+=(h-q)%2
 qq.extend(range(q,hi+1,2));ops={}
 for q in qq:
  if max(q+x for x in ins)>cap:continue
  req=sum(1<<(q+x-F-1+n)for x in set(ins)if q+x>F)
  setout=sum(1<<(q+x-F-1+n)for x in set(outs)if q+x>F)if not e[7]else 0
  assert not(setout&~hm)
  ops.setdefault((req,setout),[]).append(q)
 relations.append([list(op)for op in ops]);details.append([{'required_mask':k,'output_mask':r,'representative_heights':qs}for(k,r),qs in ops.items()])
TT=[];emap=[]
for ti,e in enumerate(B['transitions']):
 ei=B['edge_map'][ti][0]
 for oi,(req,put)in enumerate(relations[ei]):
  fr,to,k,v,f,c,r,g,a=e;TT.append([fr,to,k|req,v|req,f,c|put,r|put,g,a]);emap.append([ti,ei,oi])
sid,sk,sv=B['start'];N={'format':'global_record_historical_height_presence_v1','n':n+nb,'out':B['out'],'start':[sid,sk|hm,sv],'reentry':[],'transitions':TT,'base_Q_file':str(src.resolve()),'base_Q_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'base_model_file':Q['base_model_file'],'base_model_sha256':Q['base_model_sha256'],'color_bits':n,'height_bit_offset':n,'height_levels':list(range(F+1,cap+1)),'geometric_presence_operations':relations,'geometric_presence_details':details,'edge_map':emap,'scope':'Initial residual identities at height>F are whitened globally. Every actual later high residual input requires a historical output at that exact height. Outputs set presence, never clear it. Source intervals are existential and parity-compatible, with actual packet/DFA/spatial constraints unchanged. No count multiplicity or lifetime is asserted.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {N['out']+1} {len(TT)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in TT:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':N['n'],'color_bits':n,'height_bits':nb,'edges':len(TT),'positions':N['out']+1}))
