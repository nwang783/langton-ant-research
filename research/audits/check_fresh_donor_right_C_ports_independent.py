from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'fresh_RAW_donor_right_C_ports_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='48091fd4b07c314ca0c332a196ab38ec9815218876669a88c15d14e7d071f100';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
J=json.loads((D/'right_C_ports.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];I={a:{q for q,b in tr(W[a]+M)['req'].items()if b and q not in K}for a in'DCVU'};assert len(I['C'])==0 and sum(map(len,I.values()))==8
summ=[]
for src,anchors in(('V',{0j}),('U',{0j,1j})):
 raw=tr(W[src]);assert raw['last'][1+0j]==('R',9)and 1+0j not in{raw['p']+rot(raw['h'])*k for k in K};ref=next(r for r in J['all2_fresh_V_U_RIGHT_R9_guard_proofs']if r['actual_source_RAW']==src);rows={(r['consumer'],tuple(r['slot']),tuple(r['pose'])):r for r in ref['all32_earliest_RIGHT_CURRENT_loss_roles']};seen=set();counts=Counter();remaining=[]
 for atom in'DCVU':
  ctx=tr(W[atom]+M)
  for slot in I[atom]:
   for h in range(4):
    p=1-rot(h)*slot;key=(atom,tuple(xy(slot)),tuple(xy(p)+[h]));row=rows[key];seen.add(key)
    if(int(p.real+p.imag)+h)%2:why='sector'
    else:
     hit={q for q in anchors if(q-p)/rot(h)in ctx['req']}
     if hit:
      why='would_touch_independently_guarded_anchor';assert{tuple(xy(q))for q in hit}=={tuple(z['SAME_anchor'])for z in row['hits']}
      for item in row['hits']:
       q=complex(*item['SAME_anchor']);loc=(q-p)/rot(h);t,ch=next((t,c)for t,(z,hh,c)in enumerate(ctx['reads'])if z==loc);assert xy(loc)==item['local']and[ch,t]==item['actual_first']
     else:why='N0_endpoint_obligation';remaining.append((atom,p,h))
    assert why==row['classification'];counts[why]+=1
 assert set(rows)==seen and len(seen)==32 and counts=={'sector':16,'would_touch_independently_guarded_anchor':12,'N0_endpoint_obligation':4};assert set(remaining)=={('D',1-1j,0),('V',1-3j,0),('U',2-2j,0),('U',2-4j,0)}and raw['h']==0 and raw['p'].imag in(3,4)
 for atom in'DVU':assert tr(W[atom])['p'].imag>0 and tr(W[atom])['h']==0
 summ.append(dict(source=src,roles=32,counts=dict(counts)))
C=tr(W['C']);ek={C['p']+rot(C['h'])*q for q in K};O={q:t for q,(ch,t)in C['last'].items()if ch=='R'and q not in ek};assert C['p']==1j and C['h']==3 and len(O)==3 and min(q.real for q in O)>=1;assert{(tuple(xy(q)),t)for q,t in O.items()}=={(tuple(z['SAME_source_C_output']),z['birth_tick0'])for z in J['fresh_C_all3_output_births']}
cones=[]
for a in'DCVU':
 for slot in I[a]:
  wx=-slot.imag;sx=-1-slot.real;assert wx<=-1 and sx<=0;z=next(z for z in J['all8_plain_input_coordinate_supports']if z['ordinary_consumer']==a and z['input_slot']==xy(slot));assert wx==z['W_head_x_at_most0_input_x_at_most']and sx==z['S_head_x_at_most_minus1_input_x_at_most'];cones.append((a,xy(slot),int(wx),int(sx)))
for a in'DVU':
 for h in(2,3):assert tr(W[a],0j,h)['p'].real<=0
cc=tr(W['C'],0j,3);assert cc['p']==-1 and cc['h']==2;rk={2+rot(2)*q for q in K};assert 1 in rk and 2 in rk and sorted(map(xy,rk))==J['reader_C_source_relative']['actual_ENTRY_CORE']
out=dict(status='PASS fresh V/U right-throughC3 and fresh C outputs-throughone-postEXIT-C guards',manifest=sha(MF),script=sha(S),V_U=summ,C_input_cones=cones,analytic_review=['The actual selected V/U right cell1,0 is finalR9 external output. All8 real input slots and4 orientations are reconstructed, including marker-owned capture. SourceV r remains CURRENT throughC4; sourceU LEFT throughC3 by signed9cf. The12 anchor-touch cases are excluded by this independent CURRENT reserve at completed loss atoms, not by declaring true inputs intrinsically invalid.','Remaining four loss poses are N-facing negative-y heads. With deadlineC<=3 headingN forcesC0; source exitsy3/4 and every actual zero-C N base raisesy, so none is reachable. This proves right CURRENT throughC3 only, with simple source-prefix and no interveningFOREIGN as required. No rightC4/all-age extension.','Actual sourceC EXIT0,1W has three residual outputs withx>=1. W headsx<=0 give all inputx<=-1. One laterC movesxleft1 and turnsS; S headsx<=-1 give all inputx<=0. The complete8 input cone list includes physical and marker-owned CORE capture, C has no external I. Thus all3 SAME C outputs persist throughone postEXITC, without simplicity. SourceENTRYclock is2, not1.','Actual readerC2,0S CORE contains V/U right1,0 and C common2,0. At sourceENTRYage2 the respective guards imply CURRENT/CORE contradiction, not BLACK-versus-L. Application to another target still needs its exact source/reader frame, last-R and simple-prefix obligations.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
