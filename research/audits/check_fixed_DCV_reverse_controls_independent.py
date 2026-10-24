from pathlib import Path
from fractions import Fraction
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'postforeign_DCV_boundary_controls_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='cae8084dcbcea916b67abd37d1748d2b8d2125730fe93c3f7624b021dfaefe98';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(P/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
ref=json.loads((P/'fixed_contact_control_predecessors.json').read_text());source=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text());W={a:r['word']for a,r in zip('DCVUFQB',source['macro_words'])};M='LLLLRLRRRRL';V=(1j,1,-1j,-1);xy=lambda q:(int(q.real),int(q.imag));raw=lambda token:''.join(W[a]for a in token)
def inspect(w):
 p=0j;h=0;first={};last={};trace=[]
 for i,c in enumerate(w):
  if p in last and last[p][1]==c:return{'feasible':False,'i':i,'previous':last[p][0],'cell':xy(p),'turn':c}
  first.setdefault(p,c);last[p]=(i,c);trace.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 return{'feasible':True,'seed':{q for q,c in first.items()if c=='L'},'trace':trace,'p':p,'h':h}
controls=[]
for z in ref['three_actual_complete_finite_board_positive_replays']:
 toks=''.join(z['tokens']);rw=raw(toks);ctx=rw+M;zz=inspect(ctx);assert zz['feasible'];B={complex(*q)for q in z['complete_initial_black']};assert B==zz['seed'];p=0j;h=0
 for i,c in enumerate(ctx):
  assert c==('L'if p in B else'R')
  if c=='L':B.remove(p);h=(h-1)%4
  else:B.add(p);h=(h+1)%4
  p+=V[h]
  if i+1 in(len(rw),len(ctx)):
   rr=z['RAW_exit'if i+1==len(rw)else'actual_next_M11_exit'];assert [*xy(p)]==rr['position']and h==rr['heading']and{xy(q)for q in B}==set(map(tuple,rr['complete_black']))and len(B)==rr['mass']
 controls.append({'tokens':toks,'initial_mass':len(zz['seed']),'RAW_length':len(rw),'actual_reads':len(ctx)})
assert [(z['initial_mass'],z['RAW_length'])for z in controls]==[(10,103),(10,113),(13,149)]
nodes={'T10':'DCDCDCDV','D_T10':'DDCDCDCDV','T13':'DCDVCVCVCC'};queries=[];edges=[]
for name,token in nodes.items():
 for pred in'DCVUFQB':
  toks=pred+token;zz=inspect(raw(toks)+M);rr=next(z for z in ref['all21_exact_predecessor_queries']if(z['suffix_node'],z['predecessor_RAW_atom'])==(name,pred));assert zz['feasible']==rr['feasible_on_some_complete_finite_board']
  if zz['feasible']:edges.append((name,pred))
  else:
   assert zz['i']<len(raw(toks));a=rr['immutable_conflict'];assert zz['i']==a['conflict_read']and zz['previous']==a['previous_read']and list(zz['cell'])==a['cell']and zz['turn']==a['turn']
   for t,label in((zz['previous'],'earlier_actual_read_owner'),(zz['i'],'later_actual_read_owner')):
    offset=0
    for k,atom in enumerate(toks):
     if t<offset+len(W[atom]):break
     offset+=len(W[atom])
    owner=rr[label];assert owner['actual_atom_index0']==k and owner['actual_RAW_atom']==atom and owner['actual_atom_start_tick0']==offset;can=owner['canonical_physical_read'];assert can['context_tick0']==t-offset and can['owner_tick0']==t-offset and can['owner_read_number1']==t-offset+1 and can['turn']==zz['turn']
  queries.append({'suffix':name,'predecessor':pred,'result':zz if not zz['feasible']else{'feasible':True}})
assert edges==[('T10','D')] and len(queries)==21
out={'status':'PASS literal retained DCV controls and CLOSED21-query seven-atom reverse relation only','manifest':sha(mf),'positive_controls':controls,'queries':queries,'only_reverse_edge':edges,'analytic_review':[
'All three minimal finite fields and every physical RAW+actualM read were independently replayed with every unlisted cell WHITE. The positive10/10/13-black controls remain actual, not refuted by their missing ancestry.',
'All seven possible last RAW atoms are tested at EACH of the three fixed suffixes. T10 has exactlyD leading to the explicitly tested D_T10 node; D_T10 and T13 have no parent. Thus this reverse relation is genuinely closed and any longer seven-atom prefix is impossible, not merely unobserved beyond a chosen depth.',
'Every one of20 rejected queries has consecutive same-color reads of one physical cell inside the actual concatenated RAWs. Both zero-based offsets and generated one-based owners are independently checked. Adding unread exterior cells cannot fix such a parity conflict; no marker-only execution shortcut is used.',
'Only these FIXED words fail a U-entry/firstforeign seven-atom lift. Other histories through their contact geometry, outside-seven return words, arbitrary ordinary-tail simplicity and capture remain open. Old atomic1344 already handled four-C full-pose returns; the retained center-contact controls are not relabeled as new full-pose failures.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
