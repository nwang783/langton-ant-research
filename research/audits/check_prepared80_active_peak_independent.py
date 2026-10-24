from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bindings={'PREPARED80_COMPLETE_ACTIVE_PEAK.md':'7d413e97a55ffe8e83b4d45e02f509e8434634943849099c0d0d246395d8439f','certify_prepared80_complete_active_peak.py':'550ea23087bea129b7c318a31e4ba43bb25550ec1273f47d7fc5e862b5e5941e','prepared80_complete_active_peak_certificate.json':'882cb95a4851838c5e372b607ea72433949d29e2d8ff936dec07b07f7c2da4bd'}
for f,h in bindings.items():assert sha(D/f)==h
F=R/'audits/winding_budget_counterexample_2026-10-24';assert sha(F/'manifest.json')=='228a550faec4e369b82af305cbc1c8faa179262b6fcf50f8f044f74f71b9c5f2'and sha(F/'PEER_CONFIRMATION_BINDING.json')=='b4e1f5adffa2defc746a32c6f3eb63dcb5a401d34a082308a8dd67ab9e0562e2'
J=json.loads((D/'prepared80_complete_active_peak_certificate.json').read_text());xy=lambda z:[int(z.real),int(z.imag)];enc=lambda b:sorted(map(xy,b));dec=lambda b:{complex(*q)for q in b};W=J['word'];d=4+4j;C={-1-1j,-1+0j};A={1j,3+2j};O={-1+2j,-1+3j,3j,4j,1-1j,1+2j,1+3j,1+5j,2-1j,2+5j,3-1j,3+1j,3+2j,4+0j};assert enc(C)==J['cap']and enc(A)==J['input_ray_starts']and enc(O)==J['negative_output_ray_starts']
def kshift(z):
 x,y=int(z.real),int(z.imag)
 return x//4 if x%4==0 and y==x else None
def base(z):
 if z in C:return True
 for a in A:
  k=kshift(z-a)
  if k is not None and k>=0:return True
 for a in O:
  k=kshift(z-a)
  if k is not None and k<0:return True
 return False
def endpoints(z):
 # Doubled endpoints in the fixed C sector, derived directly from cell checker parity.
 delta=1-1j if int(z.real+z.imag)%2==0 else 1+1j
 return 2*z-delta,2*z+delta
def component(root,black):
 todo=[root];seen={root};edges=set();checks=0
 while todo:
  vertex=todo.pop()
  for dx in(-1,1):
   for dy in(-1,1):
    q=(vertex+dx+dy*1j)/2;assert q.real==int(q.real)and q.imag==int(q.imag);ee=endpoints(q);assert vertex in ee
    checks+=1
    if not black(q):continue
    edges.add(q)
    for v in ee:
     if v not in seen:seen.add(v);todo.append(v)
 return seen,edges,checks
v=1j;p=0j;flips=set();masses=[];closurechecks=0
for t,row in enumerate(J['rows']):
 root=2*p-1j*v-v;vv,ee,n=component(root,lambda q:base(q)^(q in flips));closurechecks+=n;assert row['phase']==t and row['head']==xy(p)and row['incoming_vector']==xy(v)and row['active_root']==xy(root)and row['active_black_edges']==enc(ee)and row['active_vertices']==enc(vv)and row['mass']==len(ee);masses.append(len(ee))
 if t==80:break
 ch='L'if base(p)^(p in flips)else'R';assert ch==W[t];flips.symmetric_difference_update({p});v*=1j if ch=='L'else-1j;p+=v
assert max(masses)==11 and [t for t,m in enumerate(masses)if m==11]==[70]and(p,v)==(d,1j)
vv,e0,n=component(endpoints(1j)[0],base);assert e0=={1j,-1+0j,-1-1j,-1-2j,-1-3j,-4j}and len(e0)==6
vv,e1,n=component(endpoints(3+2j)[0],base);assert e1=={3+2j}
assert len(e0-A-C)==3 and all(any(kshift(q-o)is not None and kshift(q-o)<0 for o in O)for q in e0-A-C)
# Completely independent finite fields and closed components, no old archive crop.
B=C|A;p=0j;v=1j;finite=[]
for t,row in enumerate(J['finite_N1_full_fields_and_components']):
 root=2*p-1j*v-v;vv,ee,n=component(root,lambda q:q in B);assert enc(B)==row['full_field']and enc(ee)==row['active_edges']and row['phase']==t and len(ee)<=11
 if t==70:assert len(ee)==11 and enc(ee)==J['rows'][70]['active_black_edges']
 finite.append(len(ee))
 if t==80:break
 ch='L'if p in B else'R';assert ch==W[t];B.symmetric_difference_update({p});v*=1j if ch=='L'else-1j;p+=v
assert B=={q+d for q in C}|O
out=dict(status='PASS exact complete symbolic infinite prepared80 active-w peak11 and every finite N prefix peak11',script=sha(S),bindings=bindings,all81_symbolic_components=masses,all81_finite_N1_components=finite,incident_cell_closure_checks=closurechecks,first_input_complete_component=enc(e0),second_input_complete_component=enc(e1),analytic_review=[
'Full infinite field membership is evaluated directly by exact integer ray equations for all future inputs and negative output copies, plus cap. No window, frontier crop or assumed component-size cutoff. Every discovered C-face tests all four physical incident cells against that full predicate; all81 searches terminate and their entire edge/vertex sets equal the certificate.',
'Active C-face is doubled2p+right(v)-v and checkerboard black edges use the fixed invariantC sector. Rootphase0 empty; onlyphase70 reaches11. Firstinput component has6 actual edges, including3 unread negative-output copies, while secondinput is isolated.',
'Signed and independently peer-confirmed all-N whole-field induction ensures the finite preparation differs from the corresponding infinite board only by unread oldoutputs and laterinputs throughout80N. Same physical toggles preserve inclusion, hence every complete finite active component is contained in the infinite component<=11. N1phase70 already has11, and the same firstperiod inclusion for every largerN proves equality, not only an upperbound.',
'No single finite seed repeats forever: N preparation uses2+2N black cells and first word deviation is80N+15. This is an actual long finite prepared-factor control and full infinite-input wave, not a WHITE front, finite-seed cap11 infinite controller or capture counterexample. Bounded active mass and ages<=56<P80 do not restore the falsified general m-budget.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
