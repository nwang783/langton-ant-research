"""Exact all-future check of the supplied finite inverse launch candidate.
Uses the retained independent threshold/ray checker in addition to a literal
full-field replay. Prepared five-band scope; no connected finite producer yet.
"""
from pathlib import Path
import json,runpy,hashlib
import inverse_wave_tail_completion as T
P=Path(__file__).resolve().parent;G=T.G
S=json.loads((P/'LLR_inverse_completion_search.json').read_text())['found'];assert S
edits={tuple(p)for p in S['initial_wave_XOR_edits']};assert all(not T.future_read(q)for q in edits)
C=runpy.run_path(str(G/'certify_prepared_travelling_wave.py'))
def color(q,rows,F):return T.bulk(q)^(q in F)
C['cert_parallel'].__globals__['color']=color
F=T.BASE^edits;p=(-6,-7);h=2;visited=[]
for c in S['inverse_prefix']:
 actual='L'if color(p,{},F)else'R';assert actual==c,(p,h,c,actual)
 visited.append(p);F.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=T.V[h];p=p[0]+v[0],p[1]+v[1]
assert [list(p),h]==S['prefix_pose']
cert=C['cert_parallel']({},F,p,h,S['inverse_tail_word']);assert cert
# Verify the unchanged wave independently with the full modified field.
wc=C['cert_parallel']({},T.BASE^edits,tuple(T.N['pose'][0]),T.N['pose'][1],T.J['word']);assert wc
# Physical reversal of the complete finite bridge, board unchanged.
forward=S['inverse_prefix'][::-1].translate(str.maketrans('RL','LR'))
fp=(p[0]-T.V[h][0],p[1]-T.V[h][1]);fh=(h+2)%4;entry=[fp,fh];FF=set(F)
for c in forward:
 actual='L'if color(fp,{},FF)else'R';assert actual==c
 FF.symmetric_difference_update({fp});fh=(fh+(1 if c=='R'else-1))%4;v=T.V[fh];fp=fp[0]+v[0],fp[1]+v[1]
assert [list(fp),fh]==T.N['pose'] and FF==T.BASE^edits
# Direct complete-field controls, retaining every earlier flip.
controls=[]
for word,pp,hh,init,count in [(S['inverse_tail_word'],p,h,F,40),(T.J['word'],tuple(T.N['pose'][0]),T.N['pose'][1],T.BASE^edits,10)]:
 field=set(init)
 for i,c in enumerate(word*count):
  assert color(pp,{},field)==(c=='L'),(i,pp)
  field.symmetric_difference_update({pp});hh=(hh+(1 if c=='R'else-1))%4;v=T.V[hh];pp=pp[0]+v[0],pp[1]+v[1]
 controls.append({'period':len(word),'periods':count,'reads':len(word)*count,'end':[pp,hh]})
out={'scope':__doc__,'search_result_sha256':hashlib.sha256((P/'LLR_inverse_completion_search.json').read_bytes()).hexdigest(),
 'status':'PASS author all-future prepared inverse-H ancestry and forward-wave certificate',
 'inverse_prefix':S['inverse_prefix'],'inverse_tail_pose':[p,h],'inverse_tail_word':S['inverse_tail_word'],'inverse_certificate':cert,
 'wave_certificate':wc,'initial_wave_XOR_edits':sorted(edits),'initial_wave_total_cap':sorted(T.BASE^edits),
 'forward_entry_pose':entry,'forward_prelude_word':forward,'forward_entry_cap_vs_full_bulk':sorted(F),'forward_wave_pose':T.N['pose'],
 'literal_controls':controls}
(P/'LLR_inverse_completion_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in('inverse_tail_word','initial_wave_XOR_edits','initial_wave_total_cap','forward_entry_cap_vs_full_bulk')},indent=2))
