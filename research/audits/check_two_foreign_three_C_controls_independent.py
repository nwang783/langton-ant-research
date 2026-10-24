from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'two_foreign_three_C_rewrite_controls_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json'
assert sha(mf)=='3b10b4e4a90b690fa3084edc3bd30165d3bfeebc48ff049fb517cb806eca68ea';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'three_C_controls.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,rot,xy,meet=[ns[k]for k in ('W','M','K','tr','rot','xy','meet')];G={a:tr(W[a])for a in W};out=[]
canon=lambda x:json.loads(json.dumps(x))
for au in J['all3_complete_controls']:
 seq=au['packet'];assert seq in ['UQCDDVCVUUC'+'D'*12+suffix for suffix in ['VF','UF','UQ']]and seq.count('C')==3
 raw=''.join(W[a]for a in seq);t=tr(raw+M);assert t['bad']is None
 seed={q for q,b in t['req'].items()if b};assert sorted(map(xy,seed))==au['complete_seed']and len(seed)==au['seed_mass']
 B={q:['initial',xy(q)]for q in seed};p=0j;h=0;tick=0;tracked=[];deaths=[];cuts=[]
 for index,a in enumerate(seq):
  start=p;start_h=h;startt=tick;e=au['all_actual_atom_entries'][index];assert e['ENTRY']==[*xy(p),h]and e['global_start_tick0']==tick
  if index in(0,1,9):
   ek={G[a]['p']+rot(G[a]['h'])*q for q in K};O={q for q,(c,t0)in G[a]['last'].items()if c=='R'and q not in ek}
   tags=[z for z in au['all_original_output_definitions']if z['source_atom_index0']==index]
   assert {tuple(xy(q))for q in O}=={tuple(z['source_local_cell'])for z in tags}
   for z in tags:
    q=complex(*z['source_local_cell']);world=p+rot(h)*q;birth=tick+G[a]['last'][q][1]
    assert z['cell']==xy(world)and z['source_R_global_tick0']==birth and z['source_R_own_tick0']==G[a]['last'][q][1];tracked.append(z)
  for local,c in enumerate(W[a]):
   assert(p in B)==(c=='L')
   if c=='L':
    ident=B.pop(p)
    for z in tracked:
     if z['cell']==xy(p)and z['source_R_global_tick0']==ident:deaths.append((index,a,local,z['source_atom_index0'],tuple(z['source_local_cell']),tick,ident))
   else:B[p]=tick
   h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h];tick+=1
  ec={p+rot(h)*q for q in K};ac=au['all_marked_cut_ID_states'][index]
  assert ac['cut_tick0']==tick and ac['actual_head']==[*xy(p),h]
  own=[]
  for z in tracked:
   q=complex(*z['cell']);birth=z['source_R_global_tick0'];same=B.get(q)==birth
   own.append(dict(source_atom_index0=z['source_atom_index0'],source_local_cell=z['source_local_cell'],cell=z['cell'],source_R_global_tick0=birth,SAME_physically_BLACK=same,CURRENT=same and q not in ec,alive_CORE=same and q in ec,actual_present_R_identity=B.get(q)))
  assert own==ac['tracked_original_ID_states'];cuts.append(dict(tick=tick,head=[*xy(p),h],mass=len(B)))
 assert tick==au['RAW_length']and[*xy(p),h]==au['RAW_EXIT'];rawfield=dict(B)
 assert deaths==[(z['reader_atom_index0'],z['reader_atom'],z['actual_owner']['owner_tick0'],z['source_atom_index0'],tuple(z['source_local_cell']),z['death_global_tick0'],z['source_R_global_tick0'])for z in au['all_original_output_deaths']]
 keep=[z for z in tracked if z['is_initial_U_star']or z['is_first_Q_hook']];assert len(keep)==8
 assert B.get(2+5j)==227 and 2+4j not in B
 for c in M:
  assert(p in B)==(c=='L')
  if c=='L':B.pop(p)
  else:B[p]=tick
  h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h];tick+=1
 assert tick==au['all_actual_physical_reads']and[*xy(p),h]==au['after_actual_M_fine_pose']and len(B)==au['final_physical_mass']
 assert all(B.get(complex(*z['cell']))==z['source_R_global_tick0']for z in keep)
 ps=ns['pieces'](seq);aps=au['all_actual_repaired_proxy_pieces'];assert len(ps)==len(aps)
 for (a,b),r in zip(ps,aps):assert xy(a)==r['start']and xy(b)==r['end']
 checks=0
 for i,a in enumerate(ps):
  for j in range(i+1,len(ps)):
   co=meet(*a,*ps[j]);checks+=1
   if j==i+1:assert co==(1,0)
   else:assert co is None
 assert checks==len(au['all_closed_proxy_pair_checks'])
 ne=[z for z in deaths if z[3]==1 and z[4]in[(2,0),(2,1)]];assert{(z[4],z[5])for z in ne}=={((2,1),219),((2,0),220)}
 out.append(dict(word=seq,seed=sorted(map(xy,seed)),reads=tick,raw_field=sorted([[*xy(q),v]for q,v in rawfield.items()],key=lambda z:z[:2]),final_field=sorted([[*xy(q),v]for q,v in B.items()],key=lambda z:z[:2]),all_cut_masses=cuts,all_tracked_deaths=deaths,source_pair_deaths=ne,new_q_birth=227,preserved_original_hook_and_star=8,proxy_pairs=checks))
O=dict(status='PASS three fixed complete two-foreign three-C full-field controls',manifest=sha(mf),script=sha(S),controls=out,scope='Exactly prescribed D^12 rails and VF/UF/UQ endings. Literal second FOREIGN+actualM completes, genuine original Q pair dies219/220 and new qR227 is distinct. All initialUstar and firstQhook originals survive. Direct finite proxy checks do not iterate any first-FOREIGN theorem. No all-length family, minimality, future capture, hook erosion or global simplicity claim.')
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(sha(S.with_suffix('.json')))
