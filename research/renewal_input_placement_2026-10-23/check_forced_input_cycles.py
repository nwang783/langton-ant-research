"""Verify symbolic eligibility and cycles independently of the builder's search.
This is a finite certificate checker for all N via exact integer copy offsets.
"""
from build_forced_input_cycles import *
OUT=Path(__file__).parent

def same_orbit_offset(q,p,d):
 delta=(q[0]-p[0],q[1]-p[1])
 if delta[0]*d[1]!=delta[1]*d[0]:return None
 if delta[0]%d[0]:return None
 a=delta[0]//d[0]
 return a if delta[1]==a*d[1]else None

def verify_cycle(z,tr,d,k):
 cs=[tuple(q)for q in z['cycle_cells']];assert len(cs)==len(set(cs))==z['edge_count']
 assert tuple(z['target_cell'])==tr[z['slot']][0] and cs[0]==tuple(z['target_cell'])
 g=graph(set(cs),k);assert all(len(ns)==2 for ns in g.values())
 assert component(set(cs),k,next(iter(g)))==set(cs)
 target=occurrences(cs[0],tr,d)
 if z['first_copy_only']:target=[a for a in target if a['copy_offset']>=0]
 assert target[0]['relative_time']==z['slot'] and target[0]['turn']=='L'
 aa=[]
 for q,cert in zip(cs,z['black_edge_read_certificates']):
  occ=occurrences(q,tr,d)
  if z['first_copy_only']:occ=[a for a in occ if a['copy_offset']>=0]
  assert occ==cert['complete_occurrences']
  prior=[a for a in occ if a['relative_time']<z['slot']]
  w=prior[-1]if prior else occ[0]
  assert w==cert['witness'] and tuple(cert['cell'])==q
  assert (cert['mode'],w['turn'])==('last_prior_R','R')if prior else (cert['mode'],w['turn'])==('first_future_L','L')
  aa.append(w['copy_offset'])
 assert z['left_fringe']==(0 if z['first_copy_only']else max(0,-min(aa)))
 assert z['right_fringe']==max(0,max(aa))


def standard_lifetime_certificate():
 S=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());W=S['word'];tr,end,eh=deterministic_trace(W,(0,0),S['heading']);d=end
 out=[]
 for i,(q,h,c)in enumerate(tr):
  if c!='L':continue
  occ=occurrences(q,tr,d);prior=[a for a in occ if a['relative_time']<i];w=prior[-1]
  assert w['turn']=='R'and w['copy_offset']in(-1,0)
  assert 0<i-w['relative_time']<=116
  out.append({'L_slot':i,'cell':q,'prior_R':w,'age':i-w['relative_time'],'all_occurrences':occ})
 B,_,_,_=infer_input(W,(0,0),S['heading']);assert len(B)==13
 return {'period':104,'word_sha256':hashlib.sha256(W.encode()).hexdigest(),'initial_minimal_mass':13,'all_L_slots':out,'max_age':max(z['age']for z in out),'min_copy_offset':min(z['prior_R']['copy_offset']for z in out)}

if __name__=='__main__':
 J=json.loads((OUT/'forced_input_cycle_templates.json').read_text());report={};ncycle=nedges=0
 for wh in(1564,4352):
  W,p,h,tr,d=word_data(wh);a=J[str(wh)];k=wwhich(p,h)
  assert a['word_sha256']==hashlib.sha256(W.encode()).hexdigest()
  allz=a['core']+a['startup_extra']+a['startup_overrides']
  for z in allz:verify_cycle(z,tr,d,k);ncycle+=1;nedges+=z['edge_count']
  core=a['core'];startup=a['startup_extra']+a['startup_overrides']
  for i,z in enumerate(core):
   for y in core[:i]:assert same_orbit_offset(tuple(z['target_cell']),tuple(y['target_cell']),d)is None
  assert len({tuple(z['target_cell'])for z in startup})==len(startup)
  for z in startup:
   for y in core:
    off=same_orbit_offset(tuple(z['target_cell']),tuple(y['target_cell']),d)
    if off is not None:assert off<y['left_fringe']
  counts=[]
  for N in(1,2,3,5):
   lower=sum(max(N-z['left_fringe']-z['right_fringe'],0)for z in core)+sum(N>z['right_fringe']for z in startup)
   assert lower==(40*N if wh==1564 else 102*N+19)
   B,trN,_,_=infer_input(W*N,p,h);B0=set(B);r=0;G=FullGraph(B,k);born={q:None for q in B};oldE=0;poses=[]
   obligations={}
   for z in allz:
    ks=range(z['left_fringe'],N-z['right_fringe'])if not z['first_copy_only']else([0]if N>z['right_fringe']else[])
    for j in ks:obligations.setdefault(j*len(W)+z['slot'],[]).append((j,z))
   for t,(q,hh,c)in enumerate(trN):
    if t in obligations:
     assert c=='L'and born[q]is None
     for j,z in obligations[t]:
      cyc={(v[0]+j*d[0],v[1]+j*d[1])for v in z['cycle_cells']};assert cyc<=B
      assert q in cyc and tuple(z['target_cell'])==tr[z['slot']][0]
    if c=='R':r+=1;born[q]=t;G.add(q)
    else:
     wn=G.nonbridge(q);oldE+=(r>=3 or wn)and born[q]is None
     G.delete(q);del born[q];r=0
    # Toggle on fixed geometric trace; the inferred initial set must realize it.
    assert('L'if q in B else'R')==c;B.symmetric_difference_update({q})
   assert oldE>=lower
   counts.append({'N':N,'initial_mass':len(B0),'certified_old_input_w_erasures':lower,'actual_minimal_old_input_exceptionals':oldE})
  report[str(wh)]={'core':len(core),'startup_extra':len(a['startup_extra']),'startup_overrides':len(a['startup_overrides']),'fringe_hist':a['core_fringe_hist'],'cycle_edge_hist':dict(Counter(z['edge_count']for z in allz)),'finite_controls':counts}
 std=standard_lifetime_certificate();(OUT/'standard_self_fed_lifetime_certificate.json').write_text(json.dumps(std,indent=2)+'\n')
 out={'status':'all translated-cycle/read-chronology/fringe/disjoint-target certificates PASS','cycles_checked':ncycle,'cycle_edges_checked':nedges,'standard_L_slots':len(std['all_L_slots']),'standard_max_lifetime_age_after_first_period':std['max_age'],'waves':report}
 (OUT/'forced_input_cycle_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
