from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'original_FOREIGN_all_owners_2026-10-24'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((D/'manifest.json').read_text());assert sha(D/'manifest.json')=='8da70589000d626b0b97d2f65df863a0a78bea36d14bfebf4d650b9746b803dc'
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
for f in m['dependencies']:
 if f.startswith('audits/'):
  assert json.loads((R/f).read_text())['status'].startswith('PASS')
J=json.loads((D/'FOREIGN_join.json').read_text())
ns={'__file__':str(R/'audits/check_Q_B_hook_owner_split_independent.py')};exec(Path(ns['__file__']).read_text().split('summ=[]')[0],ns)
W,M,K,tr,rot,center,xy,pieces,contact=[ns[k]for k in('W','M','K','tr','rot','center','xy','pieces','contact')]
hooks={'Q':{-3-3j,-2-3j,-1-3j,-1-2j},'B':{-2-4j,-1-4j,-4j,-3j}}
closed={};charts={};properF=[];aliasesF=[];qbproper=[];qbalias=[];qbcounts=Counter();fcounts=Counter()
for A in'FQB':
 source=tr(W[A]);assert source['h']==2
 segs=[((a-2*source['p'])/rot(source['h']),(b-2*source['p'])/rot(source['h']))for a,b in pieces(A)]
 verts=[segs[0][0]]+[b for a,b in segs];charts[A]=list(map(xy,verts));assert charts[A]=={'F':[[-7,-3],[-1,-1]],'Q':[[-7,-7],[-1,-5],[-1,-1]],'B':[[-5,-9],[1,-7],[-1,-1]]}[A]
 heads=[]
 for atom in'DCVU':
  ctx=tr(W[atom]+M);I={p for p,v in ctx['req'].items()if v and p not in K}
  for h in range(4):
   t=tr(W[atom],0j,h);c=center(0j,h);d=center(t['p'],t['h']);cand=set()
   for a,b in segs:
    corners=[(u-v)/2 for u in(a,b)for v in(c,d)]
    for x in range(math.floor(min(p.real for p in corners)),math.ceil(max(p.real for p in corners))+1):
     for y in range(math.floor(min(p.imag for p in corners)),math.ceil(max(p.imag for p in corners))+1):
      if(x+y+h)%2==0:cand.add(complex(x,y))
   for head in cand:
    hits=[(i,z)for i,(a,b)in enumerate(segs)if(z:=contact(a,b,c+2*head,d+2*head))is not None]
    if not hits:continue
    if any(tt==0 and not(ss==1 and i==len(segs)-1 and head==0 and h==0 and hi==0)for i,(ss,tt,hi,parallel)in hits):continue
    hits=[(i,z)for i,z in hits if z[1]>0]
    if not hits:continue
    mint=min(z[1]for i,z in hits);owners={i+int(z[0]==1)for i,z in hits if z[1]==mint};assert len(owners)==1;owner=owners.pop();key=(atom,*xy(head),h);heads.append(key)
    if A=='F':
     (aliasesF if owner==1 else properF).append(key)
     continue
    hook=hooks[A];core=[q for q in hook if(q-head)/rot(h)in K];white=[q for q in hook if ctx['req'].get((q-head)/rot(h))is False]
    if core:qbcounts['CORE']+=1;continue
    if white:qbcounts['WHITE']+=1;continue
    qbcounts['compatible']+=1;inputs={q for q in hook if(q-head)/rot(h)in I}
    if owner==2:assert not inputs;qbalias.append((A,*key));continue
    route='independently_signed_16_hook_LOSS_join'if inputs else'independently_signed_5_full_context_hook_MISS_closure'
    if not inputs:assert all((q-head)/rot(h)not in ctx['req']and(q-head)/rot(h)not in K for q in hook)
    qbproper.append(dict(key=(A,*key),route=route,hook_inputs=sorted(map(xy,inputs))))
 closed[A]=len(heads);assert len(heads)==len(set(heads))
assert closed==dict(F=62,Q=84,B=100)and len(properF)==42 and len(aliasesF)==20
assert qbcounts==dict(WHITE=78,CORE=65,compatible=41)and len(qbalias)==20 and len(qbproper)==21
assert Counter(z['route']for z in qbproper)==dict(independently_signed_16_hook_LOSS_join=16,independently_signed_5_full_context_hook_MISS_closure=5)
au={ (z['exact_signed_owner_aware_foreign_contact']['foreign'],z['exact_signed_owner_aware_foreign_contact']['atom'],*z['exact_signed_owner_aware_foreign_contact']['head'],z['exact_signed_owner_aware_foreign_contact']['h']):z for z in J['all21_proper_Q_B_FOREIGN_owned_compatible_contact_routes']}
for z in qbproper:
 a=au[z['key']];assert a['route']==z['route']and a['exact_signed_owner_aware_foreign_contact']['hook_inputs']==z['hook_inputs']
assert set(au)=={z['key']for z in qbproper}
F=J['F_all_four_first_ordinary_source_cover'];fk=lambda z:(z['actor'],*z['pose'])
assert set(properF)=={fk(z)for z in F['all42_proper_F_owned_heads']}
for first in'DC':assert set(properF)=={fk(z['actual_geometry'])for z in F['all84_actual_first_D_C_corrected_routes']if z['key'][0]==first}
assert F['original143d_universal_pair_proof_remains_rejected']
held={0j,1j,-3-1j,-2-1j};subsets={}
for first in'VU':
 rows={fk(z['proper_F_head']):z for z in F['all42_actual_first_'+first+'_proper_routes']};counts=Counter();surv=[]
 for key in properF:
  atom,x,y,h=key;head=complex(x,y);ctx=tr(W[atom]+M);bad=[q for q in held if(q-head)/rot(h)in K or ctx['req'].get((q-head)/rot(h))is False]
  route='signed_current_four_tag_colour_cut'if bad else'signed_actual_negative_y_FOREIGN_output_guard';assert rows[key]['route']==route;counts[route]+=1
  if not bad:surv.append(key)
 assert counts==dict(signed_current_four_tag_colour_cut=37,signed_actual_negative_y_FOREIGN_output_guard=5);subsets[first]=dict(counts=counts,lower_guard_heads=surv)
oldaliases=J['actual_FOREIGN_EXIT_alias_owner_routes'];assert len(oldaliases['all20_F_closed_EXIT_alias_geometries'])==20 and len(oldaliases['all20_Q_B_colour_compatible_closed_EXIT_aliases'])==20
review=[
'Fresh exact rational intersections use all sector-compatible integer heads in complete affine parallelograms. Earliest positive NEW-chord time and outgoing old-piece ownership distinguish true F56 kink, proper foreign pieces and final EXIT. Nonadjacent entry intersections are earlier contacts, not new onset. Target-terminal and positive collinear cases remain included.',
'FOREIGN EXIT normalization is checked on each literal RAW. All actual first ordinary D/C/V/U start at0N in this EXIT chart; a leading C is not reanchored at its later BASE. The previous source-entry chart has headingS at these actual EXITs.',
'Q/B hooks are CURRENT at global-first actorENTRY, not through contact. Exact143 CORE/first-WHITE cuts use no false retirement assertion. True inputs are retained as16 LOSS actors and bound to the later signed closure; the fiveMISS actors miss the entire real RAW+M11 context and bind the separate reader-specific proof.',
'F firstD/C uses only the corrected81+1+2 join, with original143d universalpair/full84 still rejected. FirstV and firstU have separately signed actual source reserves; identical coordinates do not justify renaming either source. The fresh42-head before-mask reconstruction gives37+5 in each case.',
'Every foreign EXIT alias has actual outgoingb1 owner, now covered by signed90716130 for all actual b1 letters including leadingC. These aliases are never forced into a proper-foreign angle window. Proper foreign and ordinary-source conclusions compose only at the same GLOBAL-first stopping cut.',
'All dependencies retain actual U-entry completeG8 prefix, its FIRST foreign, ordinary-only suffix and actual finalM11. They make no through-contact persistence claim and invoke no postforeign old-eight maturity. The result leaves preFOREIGN old owners open and does not prove arbitrary-tail simplicity, secondFOREIGN behavior or universal attraction.'
]
out=dict(status='PASS scoped all-length originalFOREIGN owner composition',manifest=sha(D/'manifest.json'),dependencies=m['dependencies'],actual_EXIT_charts=charts,geometry_heads=closed,Q_B_current_counts=qbcounts,Q_B_proper_routes=qbproper,Q_B_EXIT_alias_keys=qbalias,F_proper_keys=properF,F_EXIT_alias_keys=aliasesF,F_V_U_partitions=subsets,analytic_review=review,conclusion=m['scope'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
