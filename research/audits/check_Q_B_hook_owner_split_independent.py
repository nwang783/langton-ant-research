from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'Q_B_foreign_first_contact_hook_split_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='ff80d3161d9e0a50ba6ed77b665f7bce470383c72b06d8a70542882873ec7392';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,center,xy,pieces,cross=[ns[k]for k in('W','M','K','tr','rot','center','xy','pieces','cross')]
J=json.loads((D/'hook_split.json').read_text());windows=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];hooks={'Q':{-3-3j,-2-3j,-1-3j,-1-2j},'B':{-2-4j,-1-4j,-4j,-3j}}
# Independently parametrize all closed intersections by NEW segment time, including positive collinear onset.
def contact(a,b,c,d):
 u=b-a;v=d-c;z=c-a;den=cross(u,v)
 if den:
  s=F(cross(z,v),den);t=F(cross(z,u),den)
  return(s,t,t,False)if 0<=s<=1 and 0<=t<=1 else None
 if cross(z,u):return None
 axis=0 if v.real else 1;co=lambda q:int(q.real)if axis==0 else int(q.imag);t0=F(co(a-c),co(v));t1=F(co(b-c),co(v));lo=max(F(0),min(t0,t1));hi=min(F(1),max(t0,t1))
 if lo>hi:return None
 ax=0 if u.real else 1;cc=lambda q:int(q.real)if ax==0 else int(q.imag)
 # All vectors integral and the resulting point is a rational endpoint. Avoid float in s.
 ss=(F(cc(c-a))+lo*cc(v))/cc(u)
 return ss,lo,hi,True
summ=[];routes=Counter();miss=[];onsets=[]
for A,hook in hooks.items():
 g=tr(W[A]);segs=[((a-2*g['p'])/rot(g['h']),(b-2*g['p'])/rot(g['h']))for a,b in pieces(A)];actual=next(r for r in J['foreign_cases']if r['foreign']==A);keys={(r['atom'],*r['head'],r['h']):r for r in actual['all_colour_compatible_earliest_contact_owners_and_clock_routes']};found={};counts=Counter();heads=set()
 for atom in'DCVU':
  full=tr(W[atom]+M);I={p for p,v in full['req'].items()if v and p not in K}
  for h in range(4):
   base=tr(W[atom],0j,h);c=center(0j,h);d=center(base['p'],base['h']);candidates=set()
   for a,b in segs:
    corners=[(aa-bb)/2 for aa in(a,b)for bb in(c,d)]
    for x in range(math.floor(min(q.real for q in corners)),math.ceil(max(q.real for q in corners))+1):
     for y in range(math.floor(min(q.imag for q in corners)),math.ceil(max(q.imag for q in corners))+1):
      if(x+y+h)%2==0:candidates.add(complex(x,y))
   for head in candidates:
    hits=[(j,z)for j,(a,b)in enumerate(segs)if(z:=contact(a,b,c+2*head,d+2*head))is not None]
    if not hits:continue
    if any(t==0 and not(s==1 and j==1 and head==0 and h==0 and hi==0)for j,(s,t,hi,parallel)in hits):continue
    hits=[(j,z)for j,z in hits if z[1]>0]
    if not hits:continue
    key=(atom,*xy(head),h);assert key not in heads;heads.add(key)
    core={q for q in hook if(q-head)/rot(h)in K};white={q for q in hook if full['req'].get((q-head)/rot(h))is False}
    if core:counts['CORE']+=1;continue
    if white:counts['WHITE']+=1;continue
    counts['compatible']+=1;row=keys[key];lost={q for q in hook if(q-head)/rot(h)in I};assert sorted(map(xy,lost))==row['hook_inputs'];t=min(z[1]for j,z in hits);earliest=[(j,z)for j,z in hits if z[1]==t];owners={j+(z[0]==1)for j,z in earliest};assert len(owners)==1;owner=owners.pop();label='Fprefix'if owner==0 else A+'tail'if owner==1 else'outgoing_first_postFOREIGN_atom_b1';assert label==row['actual_outgoing_owner']and str(t)==row['first_foreign_contact_new_t']
    encoded=[(j,tuple(map(str,(z[0],z[1],z[2])if z[3]else z[:2])))for j,z in hits];assert json.loads(json.dumps(encoded))==row['contacts']
    ismiss=not lost
    if ismiss:assert all((q-head)/rot(h)not in full['req']and(q-head)/rot(h)not in K for q in hook)
    assert row['all4_hook_complete_RAW_plus_actual_M11_context_MISS']==ismiss
    if owner==2:assert ismiss;route='FOREIGN_EXIT_contact_owned_by_b1_not_discarded'
    else:
     ww=next(w for w in windows if w['source_class']==label and w['contact_atom']==atom);win=ww['allowed_C_counts_before_contact_ENTRY'];clock=[k for k in win if(-k)%4==h];assert win==row['signed_piece_C_window']and clock==row['heading_compatible_C_counts']
     if lost:
      old=[k for k in clock if k>=4];assert old==row['after_signed_hook_min4']
      if not old:route='excluded_by_piece_window_and_hook_min4'
      elif h==0:assert atom=='U'and old==[4]and head in({'Q':(-1-5j,-4j),'B':(-6j,1-5j)}[A]);route='excluded_by_signed_R39_R54_N4_guard'
      else:assert atom=='U'and h==3 and old==[5]and head==({'Q':-1j,'B':1-2j}[A]);route='excluded_by_signed_B_W5_hole'if A=='B'else'OPEN_Q_W5_hook_loss_funding'
     else:assert h==3 and clock==[5];route='OPEN_W5_hook_MISS_tail_contact';miss.append((A,atom,*xy(head),h))
    assert route==row['route'];routes[route]+=1;found[key]=route
    if any(z[3]for j,z in earliest):onsets.append(dict(A=A,key=key,owner=label,newtime=str(t)))
 assert len(heads)==actual['exact_geometry_head_count']and counts==actual['held_hook_context_classification']and set(found)==set(keys)
 summ.append(dict(foreign=A,heads=len(heads),classifications=dict(counts),proper_owner=len(found)-sum(v=='FOREIGN_EXIT_contact_owned_by_b1_not_discarded'for v in found.values())))
assert dict(routes)==J['exact_disjoint_routes']and len(miss)==5
out=dict(status='PASS owner-aware Q/B hook split; six proper-source cases remain open',manifest=sha(MF),script=sha(S),summaries=summ,routes=dict(routes),open_context_miss=miss,parallel_earliest_onsets=onsets,analytic_review=['Exact affine parallelogram bounds cover every integer same-sector target head. Closed rational intersections are ordered by NEW chord time. A candidate already in nonadjacent contact at entry is not a new positive first onset; the only harmless origin adjacency is the actual immediate FOREIGN EXIT successor. Positive collinear onsets are retained.','At the F56 kink, old prefix terminal is assigned to the outgoing Q/B tail. At the final FOREIGN EXIT, the actual outgoing owner is b1. All20 such compatible cases are routed rather than discarded or assigned an inappropriate foreign-piece turn window. A target terminal at positive newtime still counts as contact.','Hook715 gives SAME CURRENT at target ENTRY under no earlier foreign contact, not persistence THROUGH the contact. Complete RAW plus actual M11 first colors and entry CORE detect both physical and marker-owned capture. True hook inputs are retained. MISS is absence from the ENTIRE context, not merely RAW.','Signed minimum4 plus actual piece-specific Jordan windows and heading congruence close ten; signed7eed closes exactly four N4 gates; signed1fbc closes only the B W5 loss. Q W5 loss and five W5 MISS cases remain necessary OPEN interfaces. No earlier-source, b1-source, arbitrary-tail simplicity, secondFOREIGN or capture conclusion follows.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
