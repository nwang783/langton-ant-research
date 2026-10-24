from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'first_foreign_VCCV_terminal_ports_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='8a0fe4d62a1045049aac28bcfb67843f3fc438b9f29ca55f0cf3f09d28ee00c3'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'terminal_ports.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,tr,rot,K,center,xy,meet=[ns[k]for k in('W','M','tr','rot','K','center','xy','meet')];raw=lambda ts:''.join(W[a]for a in ts);vec=[1j,1,-1j,-1]
def own(ts,t):
 for i,a in enumerate(ts):
  if t<len(W[a]):return i,a,t,W[a][t]
  t-=len(W[a])
 return None,'actual next word',t,M[t]
def checkown(ts,t,z):
 i,a,k,c=own(ts,t);assert a==z['atom']
 if i is None:assert(z['tick0'],z['read_number1'],z['turn'])==(k,k+1,c)
 else:assert z['actual_atom_index0']==i and(z['canonical']['context_tick0'],z['canonical']['turn'])==(k,c)
for r in J['all3_actual_postFOREIGN_current_COLOR_CORE_fields']:
 a=r['foreign'];vp=tr(W[a]);t=tr(raw(a+'VCCV'));assert tr(raw(a+'VCCV')+M)['bad']is None
 for z in r['old_CORE_holes']:
  q=vp['p']+rot(vp['h'])*complex(*z['first_V_chart_cell']);assert xy(q)==z['physical_cell'] and t['last'][q]==('L',z['actual_V_L_deletion_tick0'])
 q=complex(*r['first_V_original_A_cell']);core={t['p']+rot(t['h'])*k for k in K};assert q in core and t['last'][q]==('R',len(W[a])+11)
rows=J['all21_exact_next_seven_atom_cases'];assert{(r['foreign'],r['next_atom'])for r in rows}=={(a,b)for a in'FQB'for b in'DCVUFQB'};stats={}
for r in rows:
 ts=r['tokens'];a,b=r['foreign'],r['next_atom'];assert ts==a+'VCCV'+b;z=tr(raw(ts)+M);assert (z['bad']is None)==r['feasible']
 if z['bad']:
  t,u,q,ch=z['bad'];b0=r['literal_conflict'];assert (t,u,xy(q),ch)==(b0['conflict_read'],b0['previous_read'],b0['cell'],b0['turn']);checkown(ts,t,r['required_read_owner']);checkown(ts,u,r['actual_previous_read_owner'])
  if b=='D':assert u==len(W[a])+1 and t==len(raw(ts))+1 and ch=='L'
  elif b in'UFQB':assert u==len(W[a])+2 and t==len(raw(ts[:-1]))+12 and ch=='L'
  else:assert b in'CV' and u<len(W[a]) and ch=='R'
 else:assert(a,b)==('B','V')
 stats[a+b]='feasible' if z['bad']is None else own(ts,z['bad'][0])
G8=('D','DC','V','VC','VCC','U','UC','UCC');assert {r['actual_full_G8']for r in J['all8_actual_G8_to_B_immediate_predecessor_queries']}==set(G8);assert[g for g in G8 if tr(raw(g+'B')+M)['bad']is None]==['U']
z=tr(raw('UBVCCVV')+M);assert z['bad']==(181,1,-1+0j,'L');checkown('UBVCCVV',181,J['unique_B_V_escape_killed_by_true_preFOREIGN_U']['required_next_V_owner'])
e=J['complete_prepared_B_shadow_erosion_regression'];ts=e['tokens'];assert ts=='BVCCVV';word=raw(ts)+M;seed={complex(*q)for q in e['complete_finite_seed']};assert seed=={q for q,b in tr(word)['req'].items()if b};B={q:['initial',None]for q in seed};p=0j;h=0;g=-2-3j
for t,ch in enumerate(word):
 prev=B.get(p);assert(ch=='L')==(p in B)
 if ch=='L':B.pop(p);h=(h-1)%4
 else:B[p]=['R',t];h=(h+1)%4
 rr=e['all_RAW_plus_actual_M11_reads'][t];assert(rr['cell'],rr['turn'],rr['before_identity'],rr['after_identity'])==(xy(p),ch,prev,B.get(p));checkown(ts,t,rr['physical_owner'])
 if t==67:assert p==g and ch=='R'
 if t==len(raw(ts))+1:assert p==g and prev==['R',67] and ch=='L'
 p+=vec[h]
 if str(t+1)in e['exact_cut_snapshots']:
  r=e['exact_cut_snapshots'][str(t+1)];core={p+rot(h)*q for q in K};assert(r['SAME_B_R67_alive'],r['inside_active_core'],r['CURRENT_same_B_R67'])==(B.get(g)==['R',67],g in core,B.get(g)==['R',67]and g not in core)
p=0j;h=0;segments=[]
for a in ts:
 z=tr(W[a],p,h)
 if a=='B':m=tr(W['F'],p,h);segments.extend([(center(p,h),center(m['p'],m['h'])),(center(m['p'],m['h']),center(z['p'],z['h']))])
 else:segments.append((center(p,h),center(z['p'],z['h'])))
 p,h=z['p'],z['h']
for k,(a,b)in enumerate(segments):
 for i,(c,d)in enumerate(segments[:k]):
  hit=meet(c,d,a,b);assert hit is None or(k==i+1 and d==a and hit==(1,0))
out=dict(status='PASS exact first-foreign VCCV marked-terminal morphology, not arbitrary erosion terminality',manifest=sha(MF),script=sha(S),all21=stats,sole_prepared_escape='BVCCVV+actualM11',all8_predecessors=G8,forced_predecessor='U',genuine_ancestry_conflict=[181,1,[-1,0],'L'],prepared_escape_seed_mass=len(seed),prepared_escape_reads=len(word),analytic_review=['All21 exact next ordinary/foreign RAW+actualM11 targets are reconstructed; only preparedB,V survives. D and someC RAWs really finish before marker failure, and no unexecuted marker is treated as already read.','The fixed U,B,V,C,C,V,V substring has immutable U L1 / lastV ownL13 repeated-L conflict independent of any earlier exterior. Signed completeG8-to-firstB adjacency is independently replayed over all8 full source types and only plainU survives.','The sole prepared escape is physically real on its full finite board and has a simple repaired proxy. Its SAME B R67 shadow is aliveCORE at lastV exit and physically dies at next-word read2; it is not part of the separately signed four-tag hook.','Terminality is only for the stipulated firstforeign+VCCV morphology and another marked G7 target. No general erosion, RAW-only impossibility, fourth-atom simplicity, arbitrary tail, secondforeign or postforeign age statement follows.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
