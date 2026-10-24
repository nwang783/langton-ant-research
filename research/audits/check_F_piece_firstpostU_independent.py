from pathlib import Path
from fractions import Fraction
from collections import Counter
import hashlib,json,math
S=Path(__file__);R=S.parents[1];D=R/'firstpostU_F_piece_first_contact_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='a08c276e417ffbe0166ccddc484da9f01c96f5160d3554eaca3b7f6b32c6ff68'
m=json.loads(MF.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
assert sha(S.with_name('check_fresh_U_LEFT_all_length_independent.json'))=='2720193d1f51956e0ea40bba8b3a1193775b50cbefc4bc2d19238c862f45c9b0'
ns={'__file__':str(S.with_name('check_Q_B_hook_owner_split_independent.py'))};exec(Path(ns['__file__']).read_text().split('summ=[]')[0],ns);W,M,K,tr,rot,center,xy,pieces,cross,contact=[ns[k]for k in('W','M','K','tr','rot','center','xy','pieces','cross','contact')]
J=json.loads((D/'F_piece_firstpostU.json').read_text());g=tr(W['F']);a,b=[(z-2*g['p'])/rot(g['h'])for z in pieces('F')[0]];assert list(map(xy,(a,b)))==[[-7,-3],[-1,-1]]
held={0j,1j,-3-1j,-2-1j};keys={(z['atom'],*z['head'],z['h']):z for z in J['all5_proper_F_source_coordinate_guards']+J['all2_FOREIGN_EXIT_contacts_outgoing_b1U']};counts=Counter();found=set();total=0
windows=ns['windows'];I={z:{q for q,v in tr(W[z]+M)['req'].items()if v and q not in K}for z in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
# Actual first-U entry/exit preserves two genuine F identities.
tags={-3-1j,-2-1j};LEFT={0j,1j};u=tr(W['U']);uc=tr(W['U']+M)
assert tags.isdisjoint(uc['req'])and tags.isdisjoint({u['p']+rot(u['h'])*q for q in K})
for tag in tags:
 q=g['p']+rot(g['h'])*tag;assert g['last'][q][0]=='R'and tag not in K
 r=next(z for z in J['genuine_F_pair_births']if z['postF_cell']==xy(tag));assert r['F_entry_cell']==xy(q)and r['F_last_R_tick0']==g['last'][q][1]
assert sorted(g['last'][g['p']+rot(g['h'])*q][1]for q in tags)==[46,47]
refs={(tuple(z['F_original']),z['consumer'],tuple(z['input_slot']),tuple(z['entry'])):z for z in J['all64_F_pair_FIRST_CURRENT_loss_roles']};seen=set();rolecounts=Counter()
for tag in tags:
 for atom in'DCVU':
  ctx=tr(W[atom]+M)
  for slot in I[atom]:
   lt=next(t for t,(q,h,c)in enumerate(ctx['reads'])if q==slot);assert ctx['reads'][lt][2]=='L'
   for h in range(4):
    p=tag-rot(h)*slot;key=(tuple(xy(tag)),atom,tuple(xy(slot)),tuple(xy(p)+[h]));seen.add(key);row=refs[key];assert row['physical_first_L']['context_tick0']==lt
    if lt>=len(W[atom]):assert row['physical_first_L']['next_word_tick0']==lt-len(W[atom])
    if int(p.real+p.imag+h)%2:why='sector'
    else:
     bad=[]
     for q in held:
      loc=(q-p)/rot(h)
      if loc in K or ctx['req'].get(loc)is False:bad.append((q,loc,'ENTRY_CORE'if loc in K else'first_WHITE'))
     if bad:
      why='held_LEFT_or_F_pair_CORE_WHITE';assert {(tuple(xy(q)),tuple(xy(l)),k)for q,l,k in bad}=={(tuple(z['SAME_held']),tuple(z['local']),z['role'])for z in row['conflicts']}
     else:
      zz=tr(W[atom],p,h);hit=contact(a,b,center(p,h),center(zz['p'],zz['h']));assert hit is not None and p!=0j
      ss,tt,end,parallel=hit;assert not parallel;assert row['contact']==[str(ss),str(tt)];why='earlier_actual_F_proxy_contact'
    assert row['classification']==why;rolecounts[why]+=1
assert seen==set(refs)and len(seen)==64 and dict(rolecounts)==J['exact_reserve_counts']
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
    if ss==1:assert k in{('D',-1,0,1),('U',0,-2,0)}and r['actual_outgoing_owner']=='firstpostU_at_FOREIGN_EXIT_not_incomingF';continue
    win=next(z['allowed_C_counts_before_contact_ENTRY']for z in windows if z['source_class']=='Fprefix'and z['contact_atom']==atom);ks=[k for k in win if(-k)%4==h];assert ks==[r['exact_ordinary_C_clock']]and ks[0]in(2,3);clock=ks[0];tag=p+(-1-3j if clock==2 else 1-1j);assert tag.imag<=-1 and p.imag>tag.imag
    rawtag=g['p']+rot(g['h'])*tag;assert rawtag not in{g['p']+rot(g['h'])*z for z in K};c0,t0=g['last'][rawtag];assert c0=='R';rr=r['initial_SAME_FOREIGN_output_reserve'];assert rr==dict(postforeign_cell=xy(tag),F_cell=xy(rawtag),last_R_tick0=t0,last_R_read1=t0+1,external_CURRENT_at_F_exit=True)
    local=(tag-p)/rot(h);first=next((t,c)for t,(q,hh,c)in enumerate(ctx['reads'])if q==local);assert first==(26 if clock==2 else 6,'R')and first[0]<len(W[atom]);o=r['actual_first_R_owner'];assert o['owner_tick0']==first[0]and o['context_tick0']==first[0]and o['turn']=='R';assert xy(local)==r['target_white_local']
assert found==set(keys)and total==62 and dict(counts)==J['exact_current_field_context_counts']=={'CORE':27,'WHITE':28,'compatible':7}
# Direct true-input/CORE export domains and exact monotone displacement facts.
portrows=[]
for atom in'DVU':
 for inp in sorted(I[atom],key=lambda z:(z.real,z.imag)):
  assert inp.imag>=1 and inp.real>=-1
  se=tr(W[atom],-rot(2)*inp,2);ee=tr(W[atom],-rot(1)*inp,1);assert se['p'].imag<=0 and ee['p'].imag<=0
  portrows.append(dict(atom=atom,input=xy(inp),S_RAW_exit_relative_tag=xy(se['p'])+[se['h']],E_RAW_exit_relative_tag=xy(ee['p'])+[ee['h']]))
assert sorted(portrows,key=str)==sorted(J['all8_actual_input_RAW_exit_bounds'],key=str)
for atom in'DVU':
 p=tr(W[atom])['p'];assert p.imag>0
 for h in(1,2,3):
  z=tr(W[atom],0j,h);assert z['h']==h
  if h==3:assert z['p'].imag>=0
  else:assert z['p'].imag<=0
assert (tr(W['C'])['p'],tr(W['C'])['h'])==(1j,3)
assert (tr(W['C'],0j,2)['p'],tr(W['C'],0j,2)['h'])==(-1j,1)
# Full prepared UFUCC regression: every bit and SAME birth identity retained.
reg=J['positive_regression'];word=reg['word'];raw=''.join(W[x]for x in word)+M;tt=tr(raw);assert not tt['bad'];seed={q for q,v in tt['req'].items()if v};assert sorted(map(xy,seed))==reg['complete_seed']and len(seed)==29 and len(raw)==153
B={q:('initial',xy(q))for q in seed};p=0j;h=0;t=0;tracked={};cutrows=[]
for idx,atom in enumerate(word):
 z=tr(W[atom],p,h)
 if idx==1:
  for tag in tags:
   q=z['p']+rot(z['h'])*tag;tracked[q]=t+z['last'][q][1]
 if idx==2:
  assert xy(p)+[h]==reg['new_U_entry']and t==reg['new_U_start_tick0']
  for q in LEFT:tracked[p+rot(h)*q]=t+tr(W['U'])['last'][q][1]
 for c in W[atom]:
  assert(p in B)==(c=='L')
  if c=='L':del B[p]
  else:B[p]=t
  h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j;t+=1
 if idx>=2:
  core={p+rot(h)*q for q in K};assert all(B.get(q)==birth and q not in core for q,birth in tracked.items());row=reg['actual_current_cut_states'][idx-2];assert row['RAW_cut_tick0']==t and row['actual_head']==xy(p)+[h]and row['SAME_current_ids']==[dict(cell=xy(q),birth_tick0=birth)for q,birth in sorted(tracked.items(),key=lambda z:(z[0].real,z[0].imag))];cutrows.append(row)
for c in M:
 assert(p in B)==(c=='L')
 if c=='L':del B[p]
 else:B[p]=t
 h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j;t+=1
assert t==153
out=dict(status='PASS original F-source global first contact exclusion after genuine immediate fresh U',manifest=sha(MF),script=sha(S),new_first_loss_roles=64,role_counts=dict(rolecounts),all_closed_heads=total,field_counts=dict(counts),proper_cases=5,outgoing_U_terminals=2,complete_regression=dict(seed_size=len(seed),reads=t,cuts=cutrows,final_black=sorted(map(xy,B))),analytic_review=[
'The pair reserve is rebuilt independently for actual immediateU, not copied from a first-V title. F R46/R47 are real external outputs, and actual U RAW+M/exitCORE miss both. Fresh-U SAMELEFT applies at all earlier simple completed cuts. Choose the first later loss of either F tag: the64 input roles include all marker-owned CURRENT-to-CORE capture, simultaneous pair inputs, and physical loss.32sector/26held-field conflicts leave6 earlier genuine F contacts, impossible before the global-first candidate. This induction requires no postforeign age.',
'At the candidate ENTRY all four coordinates are therefore current, for the newly proved U-specific reason. Contact TRUE inputs are retained. Rational closed-contact parallelograms regenerate all62 heads,27CORE/28WHITE and7compatible. Two F-terminal contacts belong to outgoing firstU and invoke the already signed real base-cut grammar/U-entry theorem. They are not discarded or assigned F-piece angle windows.',
'For five proper cases the signed one-foreign F-piece angle window gives exactlyS2/E3. Every additional negative-y witness is an actual external lastR of F. The eight true-input/marker bounds give RAWexit_y<=tag_y inS/E; N0/W1 cannot consume a negative tag, C has no external input, and remaining S/E plain rails cannot rise. Thus loss cannot precede the specific target with head_y>tag_y. This coordinate statement is first-letter independent and allows arbitrary epoch lengths.',
'The literal U R26 and D/V/U R6 WHITE conflicts are inside actual targetRAW. Full29-black153-readUFUCC, all four SAME births and every actual U/C cut are independently replayed. No virtual futureM, source-V r/A or V-hole premise is used.',
'Retains actual U-entry complete8/FIRSTF history, immediateU, arbitrary finite ordinary suffix, actual finalM and GLOBAL-first-contact stopping. No firstpostD/C closure, earlier-source closure, through-contact permanence, full-tail simplicity, secondforeign, language coverage or attraction follows.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
