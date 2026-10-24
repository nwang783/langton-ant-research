from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'returned_D_forced_core_ports_2026-10-24';p=SELF.with_name('check_D15_UCC_V_core_guard_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('xp=')[0],ns)
W,M,walk,xy,K,trace,at,raw=[ns[k]for k in('W','M','walk','xy','K','trace','at','raw')]
beta=1-1j;b=2+0j;previous=[]
for a in'DCVU':
 h=(-raw[a]['turn'])%4;p=-at(raw[a]['end'],0j,h);slot={'D':2,'C':1+2j,'V':2+2j,'U':1+3j}[a];assert at(slot,p,h)==beta and raw[a]['reads'][slot][-1][1]=='R';previous.append((a,xy(p),h,xy(slot),raw[a]['reads'][slot][-1]))
assert raw['D']['reads'][b][-1]==(8,'R')
def ec(ep,goal):
 dx=int((goal-ep).real);down=int((ep-goal).imag);sol=[]
 for v in range(max(0,down+1)):
  d=down-v;rem=dx-d-3*v
  if rem>=0 and rem%4==0:sol.append((d,v,rem//4))
 return sol
endpoints=[]
for ix,goal,q in [(15,2-5j,beta),(30,3-4j,beta),(30,3-4j,b)]:
 for a in'DVU':
  for slot in sorted(raw[a]['I'],key=xy):
   p=q-at(slot,0j,1);end=at(raw[a]['end'],p,1);sol=ec(end,goal);assert end!=goal and all(v==u==0 for d,v,u in sol);endpoints.append((ix,xy(q),a,xy(slot),xy(p),xy(end),sol))
assert len(endpoints)==24
fr=trace(W['F']);EK={at(q,fr[2],fr[3])for q in K};out=({q for q,black in trace(W['F']+M)[0].items()if black}^fr[1])-EK
rows=[]
for ix,goal,ret in [(15,2-5j,'C'),(30,3-4j,'V'),(75,3-4j,'C')]:
 comb=trace(W['F']+W[ret]+M);port=-4-1j;marker=-3-2j
 assert fr[4][port]==[(51,'L'),(55,'R')]and comb[4][port]==[(51,'L'),(55,'R'),(59,'L')]
 assert port in EK and port not in out and port not in K
 assert marker not in fr[0]and marker in EK and comb[4][marker][0]==(57,'L')and comb[0][marker]
 assert at(port,goal,1)==(beta if ix==15 else b)
 if ix in[30,75]:assert at(marker,goal,1)==beta
 rows.append({'case':ix,'F':xy(goal),'return':ret,'original_input':xy(at(port,goal,1)),'F_raw_reads':fr[4][port],'next_actual_RAW_delete':[3,4],'marker_original_beta':ix in[30,75],'marker_owner_tick0_read1':[1,2],'port_in_exit_core_not_residual':True})
A=json.loads((D/'D_forced_core_ports.json').read_text());mp=D/'manifest.json';mf=json.loads(mp.read_text());mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='799c002770b7cc7358e9563be3ce06205fb9fdf336a7b18f5666957ab368a6ed'
for f in mf['files']:assert hashlib.sha256((D/f['file']).read_bytes()).hexdigest()==f['sha256']
for f,h in A['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS genuine preforeign bud currentness and exact F EXIT-CORE reset, with reader-independent C75 lift','manifest_sha256':mh,'all_four_genuine_predecessor_exit_bud_frames':previous,'24_exact_age3_E_consumer_endpoint_obligations':endpoints,'two_submitted_and_one_compatible_C75_port_transcript':rows,'analytic_review':[
'At any genuine selectedD full entry on the U-entry old factor, the actual preceding atom exists. Its exit bud is beta=(1,-1), as all four actual predecessor frames confirm. The signed protection clock is that ATOMIC EXIT clock, not its containing full-source entry. This remains correct for C2 of VCC/UCC. SelectedD commonb=(2,0) is its genuine R8/read9 output at entryclock0.',
'Before clock3 the respective signed atomic-exit/common laws prevent retirement. At clock3 only plainE full consumers can finish beforeF; all8 true inputs for each of the three target/tag choices give exits from which exact remaining E counts cannot reachF with an allowed finalV/U. Marker-only inputs and the possible zero-length suffix are retained. Thus beta is current before either targetF and b beforeF(3,-4).',
'This preforeign lemma uses only genuine selectedD0,N, actual prior-exit bud, foreign heading/pose and clock3, and the signed allowed lastV/U. It does NOT depend on the returned reader or which old outgoing source owns the eventual contact. Consequently the same beta/b lemma applies to C75 in its genuine containingD frame. No old-D contact theorem is transplanted.',
'At F local(-4,-1), originalBLACK is consumed at51/read52, then rewrittenR55/read56 into active EXITCORE, not residualO. The actual following C or V deletes that changed core at its own3/read4, combined59. This is not consumption of the old source lifetime afterF.',
'At local(-3,-2), F has no RAW read, but its complete context absorbs the current residual into EXITCORE. Actual following C/V owns tick1/read2, combined57. In the F(3,-4) frame this is originalbeta. The two submitted rows and C75 compatible reader are all independently replayed.',
'These are conditional exact core histories, not attainment or exclusions. Genuine finite D-entry positive controls are consistent and do not establish a U-entry lift. No postforeign age law or returned simplicity is inferred.'
],'scope':mf['scope'],'dependencies':A['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
