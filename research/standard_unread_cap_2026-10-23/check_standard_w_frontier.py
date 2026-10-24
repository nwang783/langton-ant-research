"""Complete w-frontier transport for H; arbitrary finite unread archives retained."""
from check_standard_unread_cap import *
from check_cycle_birth import cursors,rank
OUT=Path(__file__).parent

def vertex_offsets(A,B):
 # all m with A intersect (B+2m*d) nonempty, for finite doubled vertex sets
 out=set();dd=(2*d[0],2*d[1])
 for u in A:
  for v in B:
   z=(u[0]-v[0],u[1]-v[1])
   if z[0]*dd[1]==z[1]*dd[0]and z[0]%dd[0]==0:out.add(z[0]//dd[0])
 return sorted(out)

def main():
 tr,end,eh=deterministic_trace(H,(0,0),3);B=set(I);p=(0,0);h=3
 for c in H*2:assert c==('L'if p in B else'R');p,h=step(B,p,h)
 # All three current components meeting translated minimal input; their whole fields are retained.
 A=set()
 for q in sh(I,2):A|=component(B,0,endpoints(q,0)[0])
 K=sh(A,-2);G=B-A;assert len(K)==28 and len(G)==9 and B==sh(K,2)|G
 G_reads=[]
 for q in sorted(G):
  occ=occurrences(q,tr,d);assert not any(z['copy_offset']>=2 for z in occ)
  G_reads.append({'cell':q,'complete_occurrences':occ})
 # Exact one-period stable frontier update.
 B=set(K);p=(0,0);h=3;phases=[];birth_records=[];Y=set();maxage=0;maxmass=0
 for i,c in enumerate(H):
  assert c==('L'if p in B else'R');w=cursors(p,h)[1]
  phase_births=[]
  for q in sorted(B):
   occ=occurrences(q,tr,d);prior=[z for z in occ if z['relative_time']<i];assert prior
   prev=prior[-1];assert prev['turn']=='R'and prev['copy_offset']>=-2
   age=i-prev['relative_time'];maxage=max(maxage,age)
   phase_births.append({'cell':q,'last_R_relative_time':prev['relative_time'],'copy_offset':prev['copy_offset'],'slot':prev['slot'],'age':age,'complete_occurrences':occ})
  phases.append({'phase':i,'pose':[p,h],'w_cursor':w,'black_frontier':sorted(B),'birth_certificates':phase_births})
  Y|=vertices(B,0)|{w};maxmass=max(maxmass,len(B));p,h=step(B,p,h)
 assert sh(K,1)<=B
 T=B-sh(K,1);assert len(T)==12 and rank(T,0)==0 and all_connected(T,0)
 assert vertex_offsets(vertices(T,0),vertices(T,0))==[0]
 assert not vertices(T,0)&vertices(sh(K,1),0)
 permanent=[]
 for q in sorted(T):
  occ=occurrences(q,tr,d);assert not any(z['copy_offset']>=1 for z in occ)
  permanent.append({'cell':q,'complete_occurrences':occ})
 # ALL phases: current entire frontier INCLUDING isolated active w vertex has
 # no vertex contact with ANY past T translate, not just a chosen finite number.
 for a in phases:
  vv=vertices({tuple(q)for q in a['black_frontier']},0)|{tuple(a['w_cursor'])}
  offsets=vertex_offsets(vv,vertices(T,0));assert all(m>=0 for m in offsets),(a['phase'],offsets)
  a['all_possible_T_vertex_contact_offsets']=offsets
 assert maxmass==42 and maxage==240
 Amax=max(sum(v)for v in Y)
 # Literal complete24-cell cap control; threshold also handles its w archives.
 E=G|F;M=min(sum(v)for v in vertices(E,0));N=max(2,(Amax-M)//8+1)
 full=I|F;p=(0,0);h=3;checked=0
 for n in range(N+3):
  for i,c in enumerate(H):
   if n>=N:
    w=cursors(p,h)[1];actual=component(full,0,w)
    canon=sh(component({tuple(q)for q in phases[i]['black_frontier']},0,tuple(phases[i]['w_cursor'])),n)
    assert actual==canon;checked+=1
   assert c==('L'if p in full else'R');p,h=step(full,p,h)
 out={'status':'PASS exact standard w-frontier transport with all-phase no-return emitted trees and complete finite-archive forgetting','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'frontier_K':sorted(K),'frontier_mass':28,'startup_archive_G':sorted(G),'G_no_future_read_certificates':G_reads,'emitted_w_tree_T':sorted(T),'T_pair_contact_offsets':[0],'T_permanent_read_certificates':permanent,'maximum_entire_frontier_mass':maxmass,'maximum_frontier_lifetime_age_after_period2':maxage,'all_phase_frontier_vertex_sum_max':Amax,'all_phase_frontier_vertices':sorted(Y),'phases':phases,'arbitrary_archive_scope':'Any finite E retained disjoint from all future H reads; at original H entry the exact state after2 periods is K+2d union E with E=G union unread F','archive_clearance_rule':'For n>=2 and Amax-8n<min_{v in vertices(E)}(v_x+v_y), the complete active w component equals its translated finite K_phase component at every phase','cap24_control':{'fixed_archive_mass':len(E),'archive_vertex_sum_min':M,'sufficient_period_threshold':N,'full_active_component_comparisons':checked}}
 (OUT/'standard_w_frontier_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k not in('phases','all_phase_frontier_vertices','T_permanent_read_certificates','G_no_future_read_certificates')},indent=2))
if __name__=='__main__':main()
