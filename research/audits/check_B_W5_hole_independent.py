from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'foreign_B_W5_deleted_q_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='1fbc4b193d4de9a800f493cb7272b07c8008a8e5c9e71be3e3927a1457edfcbe';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'B_W5_deleted_q_guard.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet,pieces=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces')]
b=tr(W['B']);hole=-1-3j;physical=b['p']+rot(b['h'])*hole;assert physical==-2-2j and b['last'][physical]==tr(W['B']+M)['last'][physical]==('L',60)and hole not in K
hook={-2-4j,-1-4j,-4j,-3j};target=1-2j;local=(hole-target)/rot(3);assert local==-1+2j and local not in K and next((t,c)for t,(q,h,c)in enumerate(tr(W['U']+M)['reads'])if q==local)==(13,'L')
fore=[((a-2*b['p'])/rot(b['h']),(c-2*b['p'])/rot(b['h']))for a,c in pieces('B')];assert fore==[(-5-9j,1-7j),(1-7j,-1-1j)]
rows={(r['atom'],r['k'],tuple(r['write'])):r for r in J['all208_last_RAW_R_origin_deadline_and_context_alignments']};seen=set();counts=Counter();remain=[];allwrites={}
for a in'DCVU':
 raw=tr(W[a]);ctx=tr(W[a]+M);writes={q:t for q,(c,t)in raw['last'].items()if c=='R'};allwrites[a]=len(writes)
 for clock in range(6):
  if a=='C'and clock==5:continue
  h=(-clock)%4
  for q,t in writes.items():
   key=(a,clock,tuple(xy(q)));seen.add(key);r=rows[key];p=hole-rot(h)*q;assert r['head']==xy(p)and r['h']==h and r['R_tick']==t;z=tr(W[a],p,h);ch=center(p,h),center(z['p'],z['h'])
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif clock==0 and p.imag<0:why='N0_y_negative'
   elif clock==1 and p.imag<1:why='W1_below_y1'
   elif any((tag-p)/rot(h)in K or(tag-p)/rot(h)in ctx['req']for tag in hook):why='current_hook_context_hit'
   else:
    contacts=[(i,meet(*seg,*ch))for i,seg in enumerate(fore)if meet(*seg,*ch)is not None]
    if contacts:
     why='earlier_FOREIGN_contact';assert(a,clock,p,h)==('U',3,-2-1j,1);assert contacts==[(1,(1,1/2))];assert p!=0 or h!=0
    else:why='NECESSARY';remain.append((a,clock,p,t,z['p'],z['h']));assert r['exit']==xy(z['p'])+[z['h']]
   assert r['why']==why;counts[why]+=1
assert seen==set(rows)and len(seen)==208 and dict(counts)==J['counts'];assert set(remain)=={('D',4,-3-3j,8,-2-2j,0),('V',4,-3-3j,8,-2+0j,0),('U',4,-3-3j,8,-3+1j,0),('C',3,-2-1j,7,-1-1j,0),('C',4,-3-3j,8,-3-2j,3)}
for a,clock,p,t,e,h in remain:
 if h==0:assert clock+(a=='C')==4 and e.imag+1>target.imag
 else:assert clock==4 and a=='C'and e.real<target.real
for a in'DVU':
 z=tr(W[a]);assert z['h']==0 and z['p'].imag>=0;z=tr(W[a],0j,3);assert z['p'].real<0 and z['p'].imag>=0
assert tr(W['C'])['p']==1j
out=dict(status='PASS exact B W5 first-B-contact deleted-hole funding exclusion',manifest=sha(MF),script=sha(S),all_RAW_final_R_slots=allwrites,roles=208,counts=dict(counts),five_survivors=[[a,c,xy(p),t,xy(e),h]for a,c,p,t,e,h in remain],analytic_review=['Actual B L60 at local-2,-2 is postexit hole-1,-3, physically WHITE after the whole B RAW and actual marker. Target U1,-2W needs the same coordinate as true lower-q input local-1,2 at RAWL13. No initial untouched identity can fund that deleted cell.','In a valid target history choose its LAST later R before target ENTRY. Every physical update before that cut belongs to a completed earlier ordinary RAW; actual markers are later RAW prefixes, not extra producer types. The producer must finish with R at that coordinate. All RAW-final-R positions, including exitCORE writes, are exhaustively enumerated. C startingclock5 cannot fully finish by targetclock5.','Before FIRST nonadjacent contact with the CLOSED original B proxy, signed four-tag hook is CURRENT at every entry and completed preceding cut. EntryCORE/firstWHITE hits contradict it. A true hook input would already lose CURRENT at producerEXIT, forcing an earlier B contact even if its physical death is marker-owned. Thus complete preceding contexts must miss every hook tag. No ordinary-ordinary simplicity is assumed.','The one geometric survivor removed by contact is U-2,-1E atclock3, crossing B terminal at newparameter1/2. It is not legitimate immediate adjacency: actual Bexit is0,0N. The hypothesis concerns the original closed B proxy, including a nonadjacent return to that endpoint.','All208 roles split104sector,18N0cone,18W1cone,62hook,1earlierBcontact,5remaining. Four remaining N exits atclock4 havey>=-2, and exactlyone laterC raisesy before nondecreasing W motion, so cannot reachy-2. FifthC exitsx-3 and Wmotion strictly decreasesx, so cannotreachx1. Arbitrary lengths/orders are covered, with no age/depth scan.','Conclusion only this B W5 first-B-proxy-contact target under actual ordinary suffix+terminalM. Q, other contact geometry, a second foreign, full-tail simplicity and capture remain open. Physical core repair is allowed generally; only this last-R funding is excluded.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
