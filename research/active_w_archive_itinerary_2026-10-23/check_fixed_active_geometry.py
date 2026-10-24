"""All-N exact full active component at the original184 wave126 cut."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'renewal_input_placement_2026-10-23'))
from certify_all_n_young_token_old_support import *
OUT=Path(__file__).parent

def main():
 B,q,h,b,t,en,seed=state_with_births(3,126);k=wwhich(q,h);beta=[21112,80557]
 C=component(B,k,endpoints(q,k)[0]);V=vertices(C,k);ports=set()
 for X,Y in V:
  for a in(-1,1):
   for z in(-1,1):
    cell=((X+a)//2,(Y+z)//2)
    if(X,Y)in endpoints(cell,k):ports.add(cell)
 J=json.loads(MAN.read_text());queries=[]
 for z in sorted(ports):
  r=query(z,beta);last=r['last_read'];black=last is not None and last['turn']=='R'
  if last is None:
   exclusions=[]
   for j,s in enumerate(J['seed_families']):
    dom=intersect(equality_domain([s[0][0],s[0][1]-z[0]]),equality_domain([s[1][0],s[1][1]-z[1]]));assert dom is None,(z,j,dom)
    exclusions.append(None)
   r['all_initial_seed_membership_domains']=exclusions
  assert black==(z in C),(z,last)
  if z in C:assert linear_nonnegative(sub(last['time_N_constant'],beta))
  r['black_at_cut']=black;queries.append(r)
 assert len(C)==59 and len(V)==54 and len(ports)==139 and component(C,k,endpoints(q,k)[0])==C
 assert any(r['last_read']and r['last_read']['time_N_constant']==beta for r in queries if tuple(r['cell'])in C)
 out={'status':'PASS all-N COMPLETE identical embedded active w component, all139 incident ports and initial-seed exclusions','source_manifest_sha256':hashlib.sha256(MAN.read_bytes()).hexdigest(),'domain':'all integers N>=1, original184 family wave126','pose':[q,h],'w_lattice':k,'component_edges':sorted(C),'component_vertices':sorted(V),'complete_incident_ports':sorted(ports),'edge_count':59,'vertex_count':54,'cycle_rank':6,'current_time_N_constant':[24024,91873],'oldest_current_R_birth_N_constant':beta,'maximum_current_lifetime_age_N_constant':[2912,11316],'queries':queries}
 (OUT/'fixed_active_geometry_allN_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k not in('component_edges','component_vertices','complete_incident_ports','queries')},indent=2))
if __name__=='__main__':main()
