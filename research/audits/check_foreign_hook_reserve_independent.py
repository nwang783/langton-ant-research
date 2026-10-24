from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'foreign_Q_B_hook_contact_reserve_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='715bdcf34f862e357bfb0a46ad8415635fd998b9dbb36d072455e76e7a1ed720';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,tr,K,rot,center,xy,meet,pieces,G=[ns[k]for k in('W','M','tr','K','rot','center','xy','meet','pieces','G')];vec=[1j,1,-1j,-1];J=json.loads((D/'hook_contact_reserve.json').read_text());raw=lambda ts:''.join(W[a]for a in ts)
I={a:{q for q,black in tr(W[a]+M)['req'].items()if black and q not in K}for a in'DCVU'};assert I['C']==set()and sum(map(len,I.values()))==8
# Every possible unvisited exit-core capture is constrained by the ACTUAL following M.
for a in'DCVU':
 z=tr(W[a]);ctx=tr(W[a]+M);ek={z['p']+rot(z['h'])*k for k in K}
 for q in ek-K:assert q in ctx['req']and(q in I[a]if ctx['req'][q]else q not in I[a])
hooks={'Q':{-3-3j,-2-3j,-1-3j,-1-2j},'B':{-2-4j,-1-4j,-4j,-3j}};summaries=[]
for A,hook in hooks.items():
 ar=tr(W[A]);normal=lambda q:(q-ar['p'])/rot(ar['h']);segments=[]
 # A doubled corrected point transforms by subtracting2*physicalexit, then rotating.
 segments=[((c-2*ar['p'])/rot(ar['h']),(d-2*ar['p'])/rot(ar['h']))for c,d in pieces(A)]
 ek={ar['p']+rot(ar['h'])*k for k in K};sourceO={normal(q)for q,(c,t)in ar['last'].items()if c=='R'and q not in ek};assert hook<=sourceO and not hook&K
 ref=next(r for r in J['foreign_cases']if r['foreign']==A);assert [xy(segments[0][0])]+[xy(d)for c,d in segments]==ref['actual_piece_vertices']
 for r in ref['guaranteed_same_original_hook_tags']:
  q=complex(*r['postforeign_cell']);orig=ar['p']+rot(ar['h'])*q;assert q in hook and xy(orig)==r['original_A_cell']and ar['last'][orig]==('R',r['last_R_tick0'])and tr(W[A]+M)['last'][orig]==('R',r['last_R_tick0'])
 keys={(tuple(r['tag']),r['atom'],tuple(r['input']),r['heading'],tuple(r['head'])):r for r in ref['all128_input_first_CURRENT_loss_alignments']};seen={};counts=Counter();contactposes=set()
 for atom in'DVU':
  ctx=tr(W[atom]+M)
  for h in range(4):
   for q in hook:
    for inp in I[atom]:
     head=q-rot(h)*inp;key=(tuple(xy(q)),atom,tuple(xy(inp)),h,tuple(xy(head)));r=keys[key]
     core={p for p in hook if(p-head)/rot(h)in K};white={p for p in hook if ctx['req'].get((p-head)/rot(h))is False}
     if(int(head.real)+int(head.imag)+h)%2:why='sector'
     elif core:why='held_CURRENT_in_entry_CORE';assert set(map(tuple,r['witnesses']))=={tuple(xy(p))for p in core}
     elif white:why='held_BLACK_first_required_WHITE';assert set(map(tuple,r['witnesses']))=={tuple(xy(p))for p in white}
     else:
      why='ordinary_consumer_chord_contacts_actual_FOREIGN_proxy';z=tr(W[atom],head,h);chord=(center(head,h),center(z['p'],z['h']));contacts=[]
      for j,(a,b)in enumerate(segments):
       hit=meet(a,b,*chord)
       if hit is None:continue
       if hit[0]=='OVERLAP':contacts.append((j,'positive_overlap'))
       elif hit!=(1,0):contacts.append((j,str(hit[0]),str(hit[1])))
      assert contacts;contactposes.add((atom,tuple(xy(head)),h));assert r['ordinary_chord']==[xy(q)for q in chord]
     assert r['reason']==why;seen[key]=why;counts[why]+=1
 assert len(seen)==128 and counts==ref['counts']=={'sector':64,'held_BLACK_first_required_WHITE':39,'held_CURRENT_in_entry_CORE':13,'ordinary_consumer_chord_contacts_actual_FOREIGN_proxy':12}and len(contactposes)==8
 summaries.append(dict(foreign=A,counts=dict(counts),distinct_contact_poses=8))
controls=[]
for row in J['two_genuine_U_entry_positive_controls']:
 ts=row['word'];A=ts[1];ctx=tr(raw(ts)+M);assert ctx['bad']is None;seed={q for q,b in ctx['req'].items()if b};assert sorted(map(xy,seed))==row['complete_seed'];B={q:('seed',q)for q in seed};p=0j;h=0;ends={};off=0
 for i,a in enumerate(ts):off+=len(W[a]);ends[off]=(i,a)
 held={};checks=[]
 for t,c in enumerate(raw(ts)+M):
  assert(c=='L')==(p in B)
  if c=='L':B.pop(p);h=(h-1)%4
  else:B[p]=('R',t);h=(h+1)%4
  p+=vec[h]
  if t+1 in ends:
   i,a=ends[t+1]
   if i==1:held={p+rot(h)*q:B[p+rot(h)*q]for q in hooks[A]}
   if i>=1:
    core={p+rot(h)*k for k in K};assert all(B.get(q)==tag and q not in core for q,tag in held.items());checks.append((i,a,xy(p)+[h]))
 assert len(checks)==5;controls.append(dict(word=ts,reads=len(raw(ts)+M),all_five_cuts_current=True))
out=dict(status='PASS four SAME Q/B hook identities persist CURRENT until the first atom contacting the actual foreign proxy',manifest_sha256=sha(MF),script_sha256=sha(S),input_roles={a:sorted(map(xy,ss))for a,ss in I.items()},cases=summaries,complete_controls=controls,analytic_review=[
'Each hook was reconstructed directly from actual foreign RAW last-R output, normalized at its actual exit. All four are external toK and survive the genuine following context. True Q/B geometry retains both F56 and tail pieces, never declaring the internal bend a marked core.',
'The independent ordinary input table uses actualRAW plus actualM first-L outsideentryK, including marker-owned CORE absorption. Every exitK-minus-entryK position is explicitly first-color constrained in that context; external BLACK enteringcore therefore appears in a true input or contradicts firstWHITE. C has zero externalBLACK input. This covers firstCURRENT loss even if physical death is delayed.',
'All128 alignments perforeign were recomputed from four heldIDs,fourheadings andeightD/V/Uinputroles.64sector,39firstWHITE,13entryCORE and12genuine-contact alternatives at8poses exhaust them. The contact branch remains possible; it is not mislabelled a color contradiction.',
'Closed endpoints and positive collinear overlaps are included. The implementation conservatively ignores even more oldterminal/newentry singleton adjacencies than the theorem permits; every surviving first-loss row nevertheless has another retained contact. Thus legitimate initial terminal adjacency causes no false rejection, while later repeated terminal already constitutes contact at the preceding atom exit.',
'Choose earliest ordinary atom whose completed cut loses a hook CURRENT identity. Its entry has all four, so the exact input table forces that atom to contact the specified foreign. This establishes persistence at every entry through the first-contact atom, not its exit, without assuming ordinary self-simplicity or a bounded C clock. All contexts are supplied by actual laterRAWs plus the actualterminalM, including D10spill.',
'Both complete genuine UQ/UB VCCV boards retain all four original R IDs at all five actual cuts. This is a fixed-subset reserve, not whole-output persistence, a proof that contacts are impossible, arbitrary-tail simplicity, another-foreign transfer or global capture.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
