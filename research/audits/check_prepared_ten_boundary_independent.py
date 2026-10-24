from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'PREPARED_TEN_HIGH_BOUNDARY_WINDING_COUNTERCONTROL.md':'6523e1b531d5859e59ccdf361ef2f2d6c51f1c293a941df7d94cf346c2fabe00','certify_prepared_ten_boundary_winding.py':'3505150c66cca008f2fe3fd565a4fc0f154c39647dea68988f662810b886a2a8','prepared_ten_boundary_winding_certificate.json':'33330d07c4e865039935d4d06eab173987b6c344852f0529e881c55c1d1b5a4b'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'prepared_ten_boundary_winding_certificate.json').read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_lifetime_boundary_graph_independent.py'))};exec(Path(ns['__file__']).read_text().split('\nW={')[0],ns);analyze=ns['analyze'];xy=ns['xy'];quo=ns['quo'];V=[1j,1,-1j,-1];w=J['word'];assert w=='RRRRLLLLRL'
E,d,I,O,paths,cyc,rc,H=analyze(w);assert d==1+1j and I=={5}and O=={2}and not cyc and rc==[((2,5),3,1,1)]
assert set(paths)==set(map(ns['normalized_path'],J['graph']['root_pairing_edges']))
assert {(a,b,v,axis)for a,b,v,axis,z in paths}=={(2,5,2,'V'),(2,5,-1,'H')}
assert sorted(''.join(w[i]for t,i in sorted(rows))for rows in H.values())==['L','R','RLRL','RLRL']
C=-1-1j;inp=-1+0j;out=1-1j
# Prove all-N interference: exactly one event in each full input/output orbit.
for q,t in [(inp,5),(out,2)]:assert [e['t']for e in E if quo(complex(*e['p']),d)[0]==quo(q,d)[0]]==[t]and complex(*E[t]['p'])==q
assert len({quo(q,d)[0]for q in(C,inp,out)})==3
controls=[]
for z in J['finite_controls']:
 n=z['n'];B={C}|{inp+k*d for k in range(n)};assert sorted(map(xy,B))==z['full_initial_black'];p=0j;h=0;trace=[]
 for t in range(10*n+6):
  c='L'if p in B else'R'
  if t<10*n+5:assert c==w[t%10]
  else:assert p==inp+n*d and c=='R'and w[5]=='L'
  if t<10 and n==1:trace.append(dict(t=t,p=xy(p),hi=h,turn=c))
  if t>=10*n:assert dict(relative_t=t-10*n,p=xy(p),turn=c)==z['next_reads'][t-10*n]
  B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
  if t==10*n-1:assert B=={C+n*d}|{out+k*d for k in range(n)}and sorted(map(xy,B))==z['full_final_black']and(p,h)==(n*d,0)
 if n==1:assert trace==J['literal_two_cell_control']['trace']
 controls.append(n)
out=dict(status='PASS prepared ten-read boundary winding3 and exact finite-fuel induction only',files=files,script=sha(S),control_n=controls,paths=[list(p[:4])for p in paths],analytic_review=['The complete alpha/beta graph is independently rebuilt, with one input and one output, no internal component, full vertical voltage+2 and horizontal-1. Its winding3 is an actual prepared complete translating-word diagnostic, not a WHITE front.','The literal two-black field relation is exact. The input/output full-drift classes each contain precisely one period event and are distinct from each other and the C class. Therefore future inputs and previously written outputs cannot interfere with a later one-period induction step, proving the full all-n formula without discarding fields.','After n periods the next five moves agree; the missing next input is first read at10n+5 and is WHITE. An infinite repeat needs infinitely many prelaid inputs. No finite-seed autonomous controller, new wave, regeneration or complete-WHITE unit-winding counterexample is claimed.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
