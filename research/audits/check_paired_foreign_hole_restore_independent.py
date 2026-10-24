from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'paired_foreign_hole_RAW_and_C_restore_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='fa88856d5698e4324f1734c07c22121f13fefdc67d31d5bfcc4d643cf5dd8ef6';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'paired_hole_restore.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,meet,pieces=[ns[k]for k in('W','M','K','tr','rot','xy','meet','pieces')];V=(1j,1,-1j,-1);G={a:tr(W[a])for a in W};canon=lambda o:json.dumps(o,sort_keys=True)
NE={complex(x,y)for x,y in [(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)]};old=(NE|{-2-1j})-{2+0j,2+1j};ek={G['U']['p']+rot(G['U']['h'])*q for q in K};new={3-1j+q for q,(c,t)in G['U']['last'].items()if c=='R'and q not in ek};field=old|new;assert len(field)==18 and sorted(map(xy,field))==J['post_gate_FIELD18_CURRENT']and max(q.imag for q in field)==2
# Solve exact displacement equations by a vertical-budget DP over NONNEGATIVE multiplicities.
def domains(p,h):
 x,y=map(int,(p.real-3,p.imag-3));ans=[]
 if h==0:
  for u in range(max(0,y//4+1)):
   v=(y-4*u-x)//2;d=x-v
   if v>=0 and d>=0 and d+3*v+4*u==y:ans.append(dict(N=[d,v,u],W=None))
 else:
  y-=1
  for un in range(max(0,y//4+1)):
   for vn in range(max(0,(y-4*un)//3+1)):
    for dn in range(max(0,y-4*un-3*vn+1)):
     yy=y-4*un-3*vn-dn;xx=dn+vn-x
     for vw in range(yy+1):
      dw=yy-vw;uw=(xx-dw-3*vw)//4
      if uw>=0 and dw+3*vw+4*uw==xx:ans.append(dict(N=[dn,vn,un],W=[dw,vw,uw]))
 return ans
found={};counts=Counter()
for h in(0,3):
 for a in'FQB':
  g=G[a];ct=tr(W[a]+M)
  for q,black in g['req'].items():
   if black:continue
   tick=next(i for i,(r,hh,c)in enumerate(g['reads'])if r==q);p=2j-rot(h)*q;key=(a,*xy(p),h,*xy(q));row=next(z for z in J['all106_next_FOREIGN_first_R_hole_alignments']if(z['actor'],*z['ENTRY'],*z['hole_local_cell'])==key)
   assert row['first_R']['owner_tick0']==tick and row['RAW_last_read']==list(g['last'][q])
   if(int(p.real+p.imag)+h)%2:why='sector'
   else:
    dom=domains(p,h);assert set(map(canon,dom))==set(map(canon,row['all_nonnegative_endpoint_count_tuples']))
    if not dom:why='post_gate_endpoint_impossible'
    else:
     bad=[]
     for f in sorted(field,key=lambda q:(q.real,q.imag)):
      u=(f-p)/rot(h)
      if u in K or ct['req'].get(u)is False:
       first=next(([c,i]for i,(r,hh,c)in enumerate(ct['reads'])if r==u),None)
       bad.append(dict(SAME_CURRENT=xy(f),local=xy(u),reason='ENTRY_CORE'if u in K else'first_WHITE',first=first))
     assert bad==row['conflicts'];why='held_18_field'
   assert why==row['route'];found[key]=why;counts[why]+=1
assert len(found)==106 and counts==dict(sector=53,post_gate_endpoint_impossible=32,held_18_field=21)
for row in J['all_actual_ordinary_R_supports']:
 rr=[dict(own_tick0=i,local_cell=xy(q))for i,(q,h,c)in enumerate(G[row['atom']]['reads'])if c=='R'];assert rr==row['all_actual_R_cells']and all(q['local_cell'][0]>=-1 and q['local_cell'][1]>=0 for q in rr)
controls=[]
for au in J['all2_genuine_complete_restoration_controls']:
 seq=au['packet'];raw=''.join(W[a]for a in seq);t=tr(raw+M);assert t['bad']is None;seed={q for q,b in t['req'].items()if b};assert sorted(map(xy,seed))==au['complete_seed'];bt=tr(''.join(W[a]for a in seq[:-1])+M);assert{q for q,b in bt['req'].items()if b}==seed
 B={q:['initial',xy(q)]for q in seed};p=0j;h=0;tick=0;selected={};hist={6j:[], -1+6j:[], -4+7j:[]};snap=[]
 for index,a in enumerate(seq):
  if index==0:selected.update({q:G['U']['last'][q][1]for q in[0j,1j,1+0j,1+1j]})
  if index==1:
   assert p==4j and h==0
   selected.update({p+q:tick+G['Q']['last'][q][1]for q in[-1-1j,-2-1j,-3-1j,-3-2j]})
  for own,c in enumerate(W[a]):
   assert(p in B)==(c=='L')
   if p in hist:hist[p].append((tick,index,a,own,c,B.get(p)))
   if c=='L':B.pop(p)
   else:B[p]=tick
   h=(h+(1 if c=='R'else-1))%4;p+=V[h];tick+=1
  ec={p+rot(h)*q for q in K}
  if index in(1,9,len(seq)-2,len(seq)-1):
   r=next(z for z in au['all_relevant_actual_cut_states']if z['after_atom_index0']==index);assert r['cut_tick0']==tick and r['head']==[*xy(p),h]
   assert r['hole_h_physically_BLACK']==(6j in B)and r['hole_h_present_R_identity']==B.get(6j)and r['hole_h_current']==(6j in B and 6j not in ec)
   assert r['side_hole_r_physically_BLACK']==(-4+7j in B)and r['side_hole_r_present_R_identity']==B.get(-4+7j)
   for z in r['selected_old_Ustar_Qhook_SAME_CURRENT']:
    q=complex(*z['cell']);assert selected[q]==z['birth'] and z['SAME_CURRENT']==(B.get(q)==selected[q]and q not in ec)
   snap.append(dict(t=tick,mass=len(B),field=sorted([[*xy(q),v]for q,v in B.items()],key=lambda z:z[:2])))
  if index==len(seq)-2:assert 6j not in B and -1+6j not in B and B[-4+7j]==au['side_hole_r_new_Q_R54_global_tick0']
  if index==len(seq)-1:assert B[6j]==au['hole_h_new_actual_C_R7_global_tick0']and B[-1+6j]==au['hole_k_new_actual_C_R8_global_tick0']and not{6j,-1+6j}&ec
 for row in au['source_hole_read_histories']:
  q=complex(*row['cell']);assert hist[q]==[(z['global_tick0'],z['atom_index0'],z['atom'],z['actual_read']['owner_tick0'],z['turn'],z['previous_identity'])for z in row['all_actual_reads']]
 for c in M:
  assert(p in B)==(c=='L')
  if c=='L':B.pop(p)
  else:B[p]=tick
  h=(h+(1 if c=='R'else-1))%4;p+=V[h];tick+=1
 assert len(seed)==au['seed_mass']and tick==au['all_actual_reads']and all(B.get(q)==v for q,v in selected.items())
 ps=pieces(seq);assert len(ps)==len(au['all_repaired_proxy_pieces'])
 for (a,b),r in zip(ps,au['all_repaired_proxy_pieces']):assert xy(a)==r['start']and xy(b)==r['end']
 for i,(a,b)in enumerate(ps):
  for j in range(i+1,len(ps)):assert meet(a,b,*ps[j])==((1,0)if j==i+1 else None)
 controls.append(dict(packet=seq,seed=sorted(map(xy,seed)),reads=tick,cuts=snap,terminal_field=sorted([[*xy(q),v]for q,v in B.items()],key=lambda z:z[:2])))
for row in J['all14_prescribed_actual_next_G7_ports']:
 raw=''.join(W[a]for a in row['base']);a=row['next_atom'];t=tr(raw+W[a]+M);assert(t['bad']is None)==row['feasible']==(a=='C')
 if t['bad']:assert row['actual_owner']['context_tick0']==t['bad'][0]-len(raw)
O=dict(status='PASS conditional paired-rewrite source hole is unread by next FOREIGN RAW ONLY, with two same-board genuine C restorations',manifest=sha(mf),script=sha(S),role_counts=counts,controls=controls,analytic_review=[
'Signed158/f24 supply h physically WHITE after genuine N2 paired U and eighteen SAME CURRENT old/new outputs at the next foreign entry, under at most three ordinary Cs. Remaining N R supports have y>=3, C3 the same bound, W R supports y>=3, so no physical R including CORE can restore h beforehand.',
'The next FOREIGN first read of h cannot be L. Every actual RAW first-R cell is rebuilt, including temporary writes not in outputs. Exact N and N-C-W displacement equations are solved by nonnegative vertical budgets, without a rail length bound or order assumption. All reachable alignments conflict with the genuine current field at entry or within its complete RAW+actualM context.',
'The guard stops at the FOREIGN RAW exit. The same full58/61 seeds actually supply the next C and its own M, with sourceL35 reborn by Q ownR54 and sourceL28/L29 by C ownR7/R8, external CURRENT at actual C exit. The real C owns the earlier supplied marker; its embedded D10 is not a complete marked D.',
'Every finite read/identity and proxy pair is reconstructed. The two source initial-U stars and Q hooks remain SAME; new repairs are not old-identity revival. No general following-marker hole guard, arbitrary foreign iteration, language entry or capture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(counts);print(sha(S.with_suffix('.json')))
