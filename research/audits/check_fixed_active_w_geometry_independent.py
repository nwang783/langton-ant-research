from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve(); ROOT=SELF.parents[1]
p=SELF.parent/'check_young_token_old_support_allN_independent.py'; ns={'__file__':str(p)};exec(p.read_text().split('ref=json.loads')[0],ns)
ends,graph,component,families,dominates,eq,J,beta,now,target,k=[ns[x]for x in('ends','graph','component','families','dominates','eq','J','beta','now','target','k')]
D=ROOT/'active_w_archive_itinerary_2026-10-23';ref=json.loads((D/'fixed_active_geometry_allN_certificate.json').read_text());C={complex(*q)for q in ref['component_edges']};V=set(graph(C,k));ports=set()
for v in V:
 for a in(-1,1):
  for b in(-1,1):
   q=(v+complex(a,b))/2
   assert q.real.is_integer()and q.imag.is_integer()
   if v in ends(q,k):ports.add(q)
assert(len(C),len(V),len(ports))==(59,54,139)
assert component(C,k,ns['wvertex'](target,0))[1]==C
assert {complex(*v)for v in ref['component_vertices']}==V
assert {complex(*q)for q in ref['complete_incident_ports']}==ports
rqueries={complex(*r['cell']):r for r in ref['queries']};unread=0;nf=0;births={}
for q in ports:
 fs=families(q);nf+=len(fs)
 rs={(f['stage'],f['slot'],f['turn'],tuple(f['copy_N_constant']),tuple(f['time_N_constant']),tuple(f['domain_N']))for f in rqueries[q]['families']}
 assert set(fs)==rs
 if not fs:
  unread+=1
  for sx,sy in J['seed_families']:
   assert eq(eq((1,None),sx[0],sx[1]-int(q.real)),sy[0],sy[1]-int(q.imag)) is None
  black=False
 else:
  eligible=[f for f in fs if f[5]==(1,None)];assert eligible
  winner=max(eligible,key=lambda f:sum(f[4]))
  assert all(dominates(winner[4],f[4],f[5])for f in fs)
  black=winner[2]=='R';assert rqueries[q]['last_read']['time_N_constant']==list(winner[4])
  if black:births[q]=winner[4];assert dominates(winner[4],beta,(1,None))
 assert black==(q in C)
assert unread==35 and beta in births.values()
assert tuple(now[i]-beta[i]for i in(0,1))==(2912,11316)
sha=hashlib.sha256((D/'FIXED_GEOMETRY_CONTROL.md').read_bytes()).hexdigest();assert sha=='897fd314ef8b8323a030a361b61ecd2820a9b5c9cfdb1d745dbe7f7a9de99c6c'
out={'status':'PASS all-N complete fixed active w geometry at isolated cuts','note_sha256':sha,'author_certificate_sha256':hashlib.sha256((D/'fixed_active_geometry_allN_certificate.json').read_bytes()).hexdigest(),'independent_ownership_helper_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'edges':59,'vertices':54,'rank':6,'incident_ports':139,'unread_ports_excluded_from_every_original_seed_family':unread,'all_N_read_families':nf,'oldest_birth':beta,'now':now,'maximum_lifetime_age':[2912,11316],'analytic':['All possible read families are independently reconstructed from the signed sixteen-stage literal geometry, and their exact integer domains are solved rather than sampled. Every chosen last read is present for every N>=1 and dominates every other possible read on its full domain.','The displayed connected graph contains the actual w cursor. Every incident nonedge is white, including all thirty-five unread ports proven absent from every affine original seed family. Thus the component is the entire full-board active component, with no possible remote attachment.','Every current edge is R-born; all birth clocks are at least beta and equality is attained. Its embedded graph and pose are fixed but maximum current lifetime age grows linearly in N.'],'scope':'Isolated cuts on the original mass184 finite bi-standard family only. Not a sustained bounded-active-component counterexample, noncapture orbit, or age bound for entire episodes.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(nf)
