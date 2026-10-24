from pathlib import Path
import sys,json,hashlib
src,out=map(Path,sys.argv[1:3]);Q=json.loads(src.read_text());assert Q['format']=='guarded_reset_global_record_residual_height_bound_v1';B=json.loads(Path(Q['base_model_file']).read_text());G=json.loads(Path('/workspace/shared/langton/core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];root=json.loads(Path(B['base_model_file']).read_text());phase=root['target_global_phase'];rules=json.loads(Path('/workspace/shared/langton/core_periodicity_new/chronology_dcuv/counted_input_age_rules.json').read_text());R={a:{}for a in root['keep']}
# Complete independently signed age inventory, including D and lower U inputs.
for a in [0,1]:R[a][(0,1)]=3
for a in [4,5]:R[a]={(0,3):2,(1,2):3}
R[6]={(0,3):4,(1,2):4}
for a in [7,8,9]:R[a]={(-1,1):3,(-1,2):3,(-1,4):4,(0,2):4,(0,3):4}
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
C=B
if len(sys.argv)>3:
 C=json.loads(Path(sys.argv[3]).read_text());assert C['format']=='global_record_historical_height_presence_v1' and Path(C['base_Q_file']).resolve()==src.resolve() and C['out']==B['out']
E=[]
for ti,t in enumerate(C['transitions']):
 bi=ti if C is B else C['edge_map'][ti][0]
 ei=B['edge_map'][bi][0];d=Q['geometric_relation_details'][ei];a=t[8];h=d['heading'];mi=[-999]*5
 for p in G[a]['inputs']:
  r=R[a][tuple(p)];mi[r]=max(mi[r],ht(rot(p,h)))
 E.append(t+[h,-999999 if d['source_height_lower']is None else d['source_height_lower'],d['source_height_upper'],d['output_offset'],G[a]['name'].count('C'),*mi])
N=dict(format='delayed_height_color_probe_v1',n=C['n'],out=C['out'],start=C['start'],Q_initial=Q['initial_height_bound'],Q_cap=Q['height_upper_bound'],base_Q_file=str(src.resolve()),base_Q_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),base_color_file=str(Path(sys.argv[3]).resolve()) if len(sys.argv)>3 else Q['base_model_file'],base_spatial_file=Q['base_model_file'],base_spatial_sha256=Q['base_model_sha256'],transition_details=E,scope='Discovery finite model: retains original literal colors, actual far packet height/transverse/DFA constraints, and five monotone historical token-age height envelopes. All input age necessities independently signed. No closure claim without checked invariant.')
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{N["n"]} {N["out"]+1} {len(E)} {N["Q_initial"]} {N["Q_cap"]}\n');f.write(' '.join(map(str,N['start']))+'\n')
 for e in E:f.write(' '.join(map(str,e))+'\n')
print({'bits':N['n'],'positions':N['out']+1,'edges':len(E),'Q_range':[N['Q_initial'],N['Q_cap']]})
