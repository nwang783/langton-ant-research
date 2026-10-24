from pathlib import Path
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'fresh_RAW_V_U_early_donor_guards_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='9cfdd2c86cdd06cf42d184dbe69fd61a49887fff4a137b3b3a1bc80095f2f6cf'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
JV=json.loads((D/'fresh_r.json').read_text());JU=json.loads((D/'fresh_U_LEFT.json').read_text())
for J in(JV,JU):
 for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet')]
I={a:{q for q,b in tr(W[a]+M)['req'].items()if b and q not in K}for a in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
for a in'DCVU':
 z=tr(W[a]);ek={z['p']+rot(z['h'])*q for q in K};ctx=tr(W[a]+M)
 for q in ek-K:assert q in ctx['req']and(not ctx['req'][q]or q in I[a])
def chord(a,p=0j,h=0):z=tr(W[a],p,h);return center(p,h),center(z['p'],z['h'])
def fields(held,a,p,h):return any((q-p)/rot(h)in K or tr(W[a]+M)['req'].get((q-p)/rot(h))is False for q in held)
results={}
for src,held,J,key in [('V',{0j},JV,'all32_plain_first_CURRENT_loss_roles'),('U',{0j,1j},JU,'all64_plain_FIRST_CURRENT_loss_roles')]:
 z=tr(W[src]);ek={z['p']+rot(z['h'])*q for q in K}
 for q in held:assert q not in ek and z['last'][q]==('R',4 if q==0 else 19)
 ref={((tuple(r['SAME_original_U_LEFT_cell'])if src=='U'else(0,0)),r['consumer'],tuple(r['input_slot']),r['pose'][2]):r for r in J[key]};seen=set();ct=Counter();gates=[]
 for q in held:
  for a in'DCVU':
   for inp in I[a]:
    for h in range(4):
     ky=(tuple(xy(q)),a,tuple(xy(inp)),h);seen.add(ky);r=ref[ky];p=q-rot(h)*inp;assert r['pose']==xy(p)+[h]
     if(int(p.real+p.imag)+h)%2:kind='unreachable_sector'if src=='V'else'sector'
     elif src=='U'and fields(held,a,p,h):kind='SAME_LEFT_initial_CORE_or_WHITE'
     else:
      assert(p,h)!=(z['p'],z['h']);contact=meet(*chord(src),*chord(a,p,h))
      if contact is not None:kind='nonadjacent_source_'+src+'_proxy_contact'
      else:kind='noncontact_marker_r_loss_gate'if src=='V'else'sole_noncontact_N_U_gate';gates.append((a,p,h))
     assert r['classification']==kind;ct[kind]+=1
     owner=r['actual_input_first_read']if src=='V'else r['physical_first_L_owner'];tick=next(i for i,(qq,hh,c)in enumerate(tr(W[a]+M)['reads'])if qq==inp);assert owner['context_tick0']==tick and owner['turn']=='L'
 assert seen==set(ref)and len(seen)==32*len(held);results[src]=dict(counts=dict(ct),gates=[[a,xy(p),h]for a,p,h in gates])
 if src=='V':assert set(gates)=={('D',1+0j,3),('V',3+0j,3),('U',4+1j,3)}
 else:assert gates==[('U',1-1j,0),('U',1-1j,0)]
# Independent principal join computation, with source whole-chord actual interface.
E=-1-1j;L=1+1j;old=chord('V');assert meet(*old,L,E)==(0,1);beta=math.atan(1/3);theta={'D':math.pi/4,'C':math.pi/4,'V':math.pi/2-beta,'U':math.pi/2}
for a in'DCVU':
 for b in'DCVU':
  z=tr(W[a]);u,v=chord(a);s,t=chord(b,z['p'],z['h']);rr=(t-s)/(v-u);assert abs(math.atan2(rr.imag,rr.real)-(theta[b]-theta[a]+(math.pi/2 if a=='C'else 0)))<1e-12
for r in JV['all3_marker_loss_Jordan_interfaces']:
 a=r['consumer'];p=complex(*r['pose'][:2]);h=r['pose'][2];z=tr(W[a],p,h);assert(z['p'],z['h'])==(1j,3)and center(z['p'],z['h'])==L and meet(*chord(a,p,h),L,E)==(1,0)
 loc=-p/rot(h);assert loc not in tr(W[a])['req'];t=len(W[a])+1;assert tr(W[a]+M)['reads'][t][0]==loc and tr(W[a]+M)['reads'][t][2]=='L'and r['SAME_r_physical_L']['context_tick0']==t
 vv=[chord(a,p,h)[1]-chord(a,p,h)[0],E-L,old[1]-old[0]];closing=sum(math.atan2((b/a).imag,(b/a).real)for a,b in zip(vv,vv[1:]));assert abs(closing+theta[a]-theta['V']+math.pi/2)<1e-12
 assert r['open_delta_pi_over4_beta'][0]+r['closing_pi_over4_beta'][0]==-2 and r['open_delta_pi_over4_beta'][1]+r['closing_pi_over4_beta'][1]==0
# U gate simultaneous true inputs and actual zero-C monotonicity.
assert tr(W['U'])['p']==4j and tr(W['U'])['h']==0
assert{(q-(1-1j))for q in(0j,1j)}<=I['U']
for a in'DVU':z=tr(W[a]);assert z['h']==0 and z['p'].imag>=1
core={1+rot(1)*q for q in K};assert{0j,1j}<=core
out=dict(status='PASS fresh RAW V r through C4 and fresh RAW U LEFT through C3 under simple ordinary source-prefix',manifest=sha(MF),script=sha(S),results=results,analytic_review=['Every plain true I role and outsideentry/newexitCORE slot reconstructed from actual RAW+M. SourceV r is finalR4; sourceU LEFT finalR4/R19. These are fresh source-relative identities; earlier foreign words are outside the interval and no old-eight age law is imported.','V32 roles leave only W D1,0/V3,0/U4,1 gates. Source chord and final consumer meet the SAME r-edge closure only at their endpoints; all intervening chords avoid it by the signed fresh ordinary RAW barrier. The edge need not have existed at the source ENTRY: the historical source-chord interface is checked directly.','All ordinary principal joins telescope. Actual edge L1,1 toE-1,-1 closes with total(K-1)pi/2, whose only +/-2pi solution forK>=0 isK5. The gate leaves original r physically alive in RAWexitCORE and deletes it at actual next read2. Thus no CURRENT loss at completed cuts of source clock0..4, not a physical death theorem or K5 attainment claim.','U64 earliest pair roles preserve simultaneous true inputs, leaving only U1,-1N twice. DeadlineK<=3 plus headingN givesK0, but sourceEXIT0,4N and every zero-C N base increasesy. Thus original LEFT remains CURRENT throughC3; no K4/all-age persistence asserted.','At relative D1,0E the protected V r and both U LEFT cells lie in true entryCORE. Applying this reader-independent guard requires the separately established simple source-prefix, actual marker completion and correct fresh source clock. It does not prove arbitrary-tail simplicity or a foreign-crossing maturation law.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
