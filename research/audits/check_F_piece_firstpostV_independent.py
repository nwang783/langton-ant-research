from pathlib import Path
from fractions import Fraction
from collections import Counter
import hashlib,json,math
S=Path(__file__);R=S.parents[1];D=R/'firstpostV_F_piece_first_contact_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='3e25f195e03772f286d74181303d70f65fe94cf7e82dff721de76abdd482d67a'
m=json.loads(MF.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
assert sha(S.with_name('check_portable_F_scope_independent.json'))=='8806adb8525d41139108f88427db3b256d25f72323f4e06a6af6c208eab6bbfb'
ns={'__file__':str(S.with_name('check_Q_B_hook_owner_split_independent.py'))};exec(Path(ns['__file__']).read_text().split('summ=[]')[0],ns);W,M,K,tr,rot,center,xy,pieces,cross,contact=[ns[k]for k in('W','M','K','tr','rot','center','xy','pieces','cross','contact')]
J=json.loads((D/'F_piece_contact.json').read_text());g=tr(W['F']);a,b=[(z-2*g['p'])/rot(g['h'])for z in pieces('F')[0]];assert list(map(xy,(a,b)))==J['actual_F_piece_vertices']==[[-7,-3],[-1,-1]]
held={0j,1j,-3-1j,-2-1j};assert sorted(map(xy,held))==sorted(J['held_current_before_first_contact']);keys={(z['atom'],*z['head'],z['h']):z for z in J['all5_proper_Fsource_lower_output_guards']+J['all2_FOREIGN_EXIT_contacts_owned_by_firstpostV']};counts=Counter();found=set();total=0
windows=ns['windows'];I={z:{q for q,v in tr(W[z]+M)['req'].items()if v and q not in K}for z in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
for atom in'DCVU':
 ctx=tr(W[atom]+M)
 for h in range(4):
  z=tr(W[atom],0j,h);c=center(0j,h);d=center(z['p'],z['h']);corners=[(aa-bb)/2 for aa in(a,b)for bb in(c,d)]
  for x in range(math.floor(min(q.real for q in corners)),math.ceil(max(q.real for q in corners))+1):
   for y in range(math.floor(min(q.imag for q in corners)),math.ceil(max(q.imag for q in corners))+1):
    if(x+y+h)%2:continue
    p=complex(x,y);hit=contact(a,b,c+2*p,d+2*p)
    if hit is None:continue
    ss,tt,end,parallel=hit
    if tt==0:continue # The sole permitted origin adjacency has no positive overlap.
    total+=1;core={q for q in held if(q-p)/rot(h)in K};white={q for q in held if ctx['req'].get((q-p)/rot(h))is False}
    if core:counts['CORE']+=1;continue
    if white:counts['WHITE']+=1;continue
    counts['compatible']+=1;k=(atom,x,y,h);found.add(k);r=keys[k];assert sorted(map(xy,{q for q in held if(q-p)/rot(h)in I[atom]}))==r['hook_inputs'];encoded=[str(ss),str(tt)]+([str(end)]if parallel else[]);assert r['contacts']==[[0,encoded]]
    if ss==1:assert k in{('D',-1,0,1),('U',0,-2,0)}and r['actual_outgoing_owner']=='firstpostV_at_FOREIGN_EXIT_not_incomingF';continue
    win=next(z['allowed_C_counts_before_contact_ENTRY']for z in windows if z['source_class']=='Fprefix'and z['contact_atom']==atom);ks=[k for k in win if(-k)%4==h];assert ks==[r['exact_ordinary_C_clock']]and ks[0]in(2,3);clock=ks[0];tag=p+(-1-3j if clock==2 else 1-1j);assert tag.imag<=-1 and p.imag>tag.imag
    rawtag=g['p']+rot(g['h'])*tag;assert rawtag not in{g['p']+rot(g['h'])*z for z in K};c0,t0=g['last'][rawtag];assert c0=='R';rr=r['initial_SAME_FOREIGN_output_reserve'];assert rr==dict(postforeign_cell=xy(tag),F_cell=xy(rawtag),last_R_tick0=t0,last_R_read1=t0+1,external_CURRENT_at_F_exit=True)
    local=(tag-p)/rot(h);first=next((t,c)for t,(q,hh,c)in enumerate(ctx['reads'])if q==local);assert first==(26 if clock==2 else 6,'R')and first[0]<len(W[atom]);o=r['actual_first_R_owner'];assert o['owner_tick0']==first[0]and o['context_tick0']==first[0]and o['turn']=='R';assert xy(local)==r['target_white_local']
assert found==set(keys)and total==62 and dict(counts)==J['exact_context_classification']=={'CORE':27,'WHITE':28,'compatible':7}
# Direct true-input/CORE export domains and exact monotone displacement facts.
portrows=[]
for atom in'DVU':
 for inp in sorted(I[atom],key=lambda z:(z.real,z.imag)):
  assert inp.imag>=1 and inp.real>=-1
  se=tr(W[atom],-rot(2)*inp,2);ee=tr(W[atom],-rot(1)*inp,1);assert se['p'].imag<=0 and ee['p'].imag<=0
  portrows.append(dict(atom=atom,input=xy(inp),S_RAW_exit_relative_tag=xy(se['p'])+[se['h']],E_RAW_exit_relative_tag=xy(ee['p'])+[ee['h']]))
assert sorted(portrows,key=str)==sorted(J['all8_trueinput_RAW_exit_bounds_for_negative_y_reserve'],key=str)
for atom in'DVU':
 p=tr(W[atom])['p'];assert p.imag>0
 for h in(1,2,3):
  z=tr(W[atom],0j,h);assert z['h']==h
  if h==3:assert z['p'].imag>=0
  else:assert z['p'].imag<=0
assert (tr(W['C'])['p'],tr(W['C'])['h'])==(1j,3)
assert (tr(W['C'],0j,2)['p'],tr(W['C'],0j,2)['h'])==(-1j,1)
out=dict(status='PASS original F-piece first contact closure under genuine firstpostV ancestry only',manifest=sha(MF),script=sha(S),geometry_heads=total,classifications=dict(counts),proper=5,outgoing_V_terminals=2,true_input_bounds=8,analytic_review=['Exact rational parallelograms reconstruct every same-sector closed candidate with positive newtime. Nonadjacent t0 contacts already occurred by entry; only actual immediate F-exit adjacency could be harmless and contributes no later positive contact here. New terminal contacts remain included. Two old F-terminal cases have outgoing first-V owner and route to signeda227, not an F window.','The signed portable-F lift preserves actual U-entry complete8/FIRSTF/immediateV ancestry. Its four SAME CURRENT tags are used only at candidate ENTRY. TRUE inputs during the contact are retained. Five proper F candidates have unique S2/E3 clocks from the actual piece window, not a heading-only upper bound.','Any initially CURRENT negative-y tag cannot first lose in N0/W1: actual N input y>=1, W input heady<=tagy+1<=0 while W heads>=1. C has no external input. Every S/E CURRENT-to-CORE/physical input has actual RAW exit y<=tagy. Subsequent S motion cannot rise; the S-to-E C lowers y and E motion cannot rise. Thus such a loss cannot precede a same-clock target with heady>tagy, for arbitrary rail lengths.','All five additional witnesses are actual LAST-R full F outputs, initially outside exit CORE, not prepared substitutes. They demand WHITE in actual U R26 or D/V/U R6 inside RAW. No old-age law, postforeign maturation, unexecuted tail, whole-source permanence or secondforeign conclusion is used. Only original F-piece owner is closed under the stipulated history; other firstpost letters and other source owners remain separate.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
