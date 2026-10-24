from pathlib import Path
import json,sys,hashlib
src,dfa,out=map(Path,sys.argv[1:4]);J=json.loads(src.read_text());D=json.loads(dfa.read_text());B=src.parents[1] if False else Path('/workspace/shared/langton/core_periodicity_new/chronology_dcuv');G=json.loads((B/'literal_residual_geometry.json').read_text())['geometry'];phase=J['target_global_phase'];S=J['record_threshold'];I=J['initial_token_weight'];A=J['core_offsets'];T={(a,h):t for a,h,t in J['created_peaks']};keep=J['keep'];F=(S-I-1)//2
rules={0:{(0,1):3},1:{(0,1):3},4:{(0,3):2,(1,2):3},5:{(0,3):2,(1,2):3},6:{(0,3):4,(1,2):4},**{a:{(-1,1):3,(-1,2):3,(-1,4):4,(0,2):4,(0,3):4}for a in [7,8,9]}}
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
acts=[]
for h in range(4):
 for a in keep:
  g=G[a];mins=[-999]*5
  for p in g['inputs']:
   r=rules[a][tuple(p)];mins[r]=max(mins[r],ht(rot(p,h)))
  mo=max(ht(rot(p,h))for p in g['outputs']);dq=ht(rot(g['endpoint'][:2],h));dh=g['endpoint'][2];c=g['name'].count('C');lim=(S-1-max(A[(h+phase)%4],T[a,(h+phase)%4]))//2
  acts.append([h,a,c,dq,dh,mo,lim,*mins])
cap=max([F]+[v[6]-(v[6]-v[0])%2+v[5]for v in acts]);mindq=min(v[3]for v in acts);maxdq=max(v[3]for v in acts);cut=F-max(abs(x)for v in acts for x in v[3:6])-8;qtop=max((S-1-a)//2 for a in A);target=J['target'];target=target[0] if isinstance(target,list) else target
N=dict(format='delayed_height_geometry_probe_v1',initial_bound=F,height_cap=cap,lower_cutoff=cut,qtop=qtop,target=target,phase=phase,threshold=S,old_core_limits=[(S-1-A[(h+phase)%4])//2 for h in range(4)],actions=acts,dfa_file=str(dfa),dfa_sha256=hashlib.sha256(dfa.read_bytes()).hexdigest(),source=str(src),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),scope='Discovery-only overapproximation retaining heading, height, packet DFA and five global historical height envelopes for token ages>=0..4. No colors or transverse coordinate; no ant witness claim.')
out.with_suffix('.json').write_text(json.dumps(N,indent=2)+'\n')
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{F} {cap} {cut} {qtop} {target} {D["initial_class"]} {len(D["transitions"])}\n');f.write(' '.join(map(str,N['old_core_limits']))+'\n')
 for v in acts:f.write(' '.join(map(str,v))+'\n')
 for tr in D['transitions']:
  f.write(' '.join(map(str,tr))+'\n')
print({k:N[k]for k in ['initial_bound','height_cap','lower_cutoff','qtop','target']})
