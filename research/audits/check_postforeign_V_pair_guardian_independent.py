from pathlib import Path
from fractions import Fraction
from collections import Counter
import hashlib,json,math
S=Path(__file__);R=S.parents[1];D=R/'postforeign_V_rA_nonterminal_guardian_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='25a349fdd27b4cd9b16b2cae54c47d191742ce4d0a0e7d9493c36352b3f7f8a5'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'rA_guardian.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,tr,K,rot,xy,center,meet=[ns[k]for k in('W','M','tr','K','rot','xy','center','meet')]
I={a:{q for q,b in tr(W[a]+M)['req'].items()if b and q not in K}for a in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
edge=lambda q:(2*q-1-1j,2*q+1+1j)if int(q.real+q.imag)%2==0 else(2*q-1+1j,2*q+1-1j)
def chord(a,p=0j,h=0):z=tr(W[a],p,h);return center(p,h),center(z['p'],z['h'])
barriers=[]
for a in'DCVU':
 s,e=chord(a);v=e-s;ctx=tr(W[a]+M);z=tr(W[a]);ek={z['p']+rot(z['h'])*q for q in K};opened={}
 for x in range(math.floor((min(s.real,e.real)-1)/2),math.ceil((max(s.real,e.real)+1)/2)+1):
  for y in range(math.floor((min(s.imag,e.imag)-1)/2),math.ceil((max(s.imag,e.imag)+1)/2)+1):
   q=complex(x,y);u,w=edge(q);hit=meet(u,w,s,e)
   if hit is None:continue
   if hit[0]=='OVERLAP':
    k='real'if v.real else'imag';ts=sorted([Fraction(int(getattr(u-s,k)),int(getattr(v,k))),Fraction(int(getattr(w-s,k)),int(getattr(v,k)))]);inside=max(0,ts[0])<min(1,ts[1])
   else:inside=0<hit[1]<1
   if not inside:continue
   role='entry_CORE'if q in K else'TRUE_residual_input'if q in I[a]else'before_WHITE'if ctx['req'].get(q)is False else'BAD';assert role!='BAD';opened[tuple(xy(q))]=role
 ref=next(z for z in J['fresh_plain_RAW_current_edge_barrier']if z['ordinary_RAW']==a);assert opened=={tuple(z['cell']):z['actual_before_role']for z in ref['all_open_chord_edge_contacts']}
 for c,core in[(s,K),(e,ek)]:
  incident={complex(x,y)for x in range(int(c.real)//2-2,int(c.real)//2+3)for y in range(int(c.imag)//2-2,int(c.imag)//2+3)if c in edge(complex(x,y))};assert len(incident)==4 and incident<=core
 for q in ek-K:assert q in ctx['req']and(q in I[a]if ctx['req'][q]else q not in I[a])
 barriers.append([a,len(opened)])
assert [n for a,n in barriers]==[1,1,1,4]
for h,p in[(0,0j),(1,1+0j),(2,0j),(3,1+0j)]:
 for x in range(-2,4):
  for y in range(-2,4):q=complex(x,y);assert set(edge(p+rot(h)*q))=={2*p+rot(h)*z for z in edge(q)}
pair={0j,1j};src=tr(W['V']);ek={src['p']+rot(src['h'])*q for q in K};assert src['last'][0j]==('R',4)and src['last'][1j]==('R',11)and not pair&ek;old=chord('V');rows={(tuple(r['SAME_lost_pair_identity_cell']),r['consumer_RAW'],tuple(r['input_slot']),r['consumer_pose'][2]):r for r in J['all64_plain_earliest_CURRENT_loss_roles']};seen=set();counts=Counter();gates=[]
for tag in pair:
 for a in'DCVU':
  ctx=tr(W[a]+M)
  for inp in I[a]:
   for h in range(4):
    key=(tuple(xy(tag)),a,tuple(xy(inp)),h);seen.add(key);r=rows[key];p=tag-rot(h)*inp;assert r['consumer_pose']==xy(p)+[h]
    if(int(p.real+p.imag)+h)%2:why='unreachable_sector'
    elif any((q-p)/rot(h)in K or ctx['req'].get((q-p)/rot(h))is False for q in pair):why='initial_SAME_pair_CORE_or_WHITE_conflict'
    else:
     assert(p,h)!=(1+3j,0);hit=meet(*old,*chord(a,p,h))
     if hit is not None:why='actual_nonadjacent_source_V_proxy_contact'
     else:why='noncontact_A_loss_gate';assert tag==1j;gates.append((a,p,h))
    assert r['classification']==why;counts[why]+=1
assert seen==set(rows)and len(seen)==64 and dict(counts)=={'unreachable_sector':32,'initial_SAME_pair_CORE_or_WHITE_conflict':18,'actual_nonadjacent_source_V_proxy_contact':12,'noncontact_A_loss_gate':2};assert set(gates)=={('V',4j,2),('U',-1+5j,2)}
P=2j;ww=-1+3j;ll=1+1j;assert set(edge(1j))=={ww,ll};assert meet(*old,ww,ll)==(Fraction(1,2),Fraction(1,2));assert meet(P,old[1],ww,P)==(0,1)
for a,p,h in gates:
 z=tr(W[a],p,h);assert(z['p'],z['h'],center(z['p'],z['h']))==(-1+1j,2,ww);assert meet(*chord(a,p,h),ww,P)==(1,0);ctx=tr(W[a]+M,p,h);assert all(q!=1j for q,hh,c in z['reads'])and ctx['reads'][len(W[a])+1][0]==1j and ctx['reads'][len(W[a])+1][2]=='L';assert all(q.imag>=1 for q,hh,c in z['reads'])
 for base in'DVU':
  b=tr(W[base]);assert all(p.imag+b['p'].imag-q.imag>=p.imag for q,hh,c in b['reads'])
# Every ordinary join has its literal principal turn equal to the telescoping angle.
beta=math.atan(Fraction(1,3));theta=dict(D=math.pi/4,C=math.pi/4,V=math.pi/2-beta,U=math.pi/2)
for a in'DCVU':
 for b in'DCVU':
  raw=theta[b]-theta[a]+(math.pi/2 if a=='C' else 0);assert -math.pi<raw<math.pi
  z=tr(W[a]);s,e=chord(a);u,v=chord(b,z['p'],z['h']);ratio=(v-u)/(e-s);actual=math.atan2(ratio.imag,ratio.real);assert abs(actual-raw)<1e-12
for a,p,h in gates:
 v=chord(a,p,h)[1]-chord(a,p,h)[0];bridge=P-ww;start=old[1]-P;closing=sum(math.atan2((b/a).imag,(b/a).real)for a,b in[(v,bridge),(bridge,start)]);assert abs(closing-(math.pi-(beta if a=='U' else 0)))<1e-12
# All21 guards have y<=0 and same actualhelperEXIT, so signed cone transfers literally.
assert len(J['all21_inherited_common_EXIT_terminal_port_obligations'])==21 and all(r['actual_first_V_chart_guard'][1]<=0 for r in J['all21_inherited_common_EXIT_terminal_port_obligations'])
out=dict(status='PASS conditional SAME first-postforeign V r/A guardian at simple nonterminal marked cuts',manifest=sha(MF),script=sha(S),fresh_RAW_barrier_contacts=barriers,sector_cases=144,first_loss_counts=dict(counts),gates=[[a,xy(p),h]for a,p,h in gates],analytic_review=['The plain RAW+actualM survivor-edge barrier is freshly rebuilt at all open-edge contacts and all four incident edges of each endpoint, with sector covariance. Every outsideentryK/newexitK cell is actual first-color constrained. TrueI includes physicalL/recycling and marker-only aliveCORE capture; no old-eight barrier authority is transported through the foreign.','All64 earliest pair-loss roles retain simultaneous possibilities. The only noncontact feasible losses are A intoV0,4S orU-1,5S; both endat correctedW-1,3 and leave SAMEA physically aliveCORE until actualnextread2. SourceV outputR11 edge meets sourcechord atP0,2; the sourcepartial and finalconsumer meet its closinghalf only atP/W.','Between sourceV and firstloss there is noforeign. Whole executedproxy simplicity gives a simple sourceP-to-W arc. While SAMEA isCURRENT all intermediate ordinary openchords/endpoints avoid it by the fresh barrier. Together with the explicit boundary interfaces this gives an actual Jordan closure, not a historical ghost or claim that A was alreadyborn at the artificial source midpoint.','Every one of16 ordinary joins has exact principal turn theta_next-theta_prev+1[C]pi/2, so openturn isKpi/2 forV orKpi/2+beta forU. Closing turns arepi orpi-beta with the actual orientedhalfedgeW->P. Thus total(K+2)pi/2 must be+/-2pi; K>=0 leaves exactly2. No hidden2pi or postforeignage substitution.','AtK2 the completeN/W/S supportcone applies. Uhelper has precedingSexit y>=5 and finalRAW y>=1, while Vuses4/1; both share actualEXIT-1,1S. All21 inherited y<=0 guards and mandatorypreB U hole survive, so the firstloss endpoint cannot have an IMMEDIATE completedG7 RAW+M continuation.','If loss were beforethe stipulatedsimplecut, either an intervening ordinaryword or the stipulated nextcompletedG7 would supply exactly that impossible immediatecontinuation. PairthereforeCURRENT at thecut/firstcontactENTRY. Erosion in a terminalhistory remainslegal; no persistence throughcontact, arbitrarytailsimplicity, otherforeign transfer or unconditional seal follows.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
