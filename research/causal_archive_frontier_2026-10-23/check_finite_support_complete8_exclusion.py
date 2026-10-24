"""Literal first-U/no-U split, plus the already signed HS cut interface."""
from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
GP=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9)
D=G[0]['word'];C=G[1]['word'][len(D):];V=G[4]['word'];U=G[7]['word']
assert D=='LLLLRLRRRR'and C=='LLLLRLRRRRLRRRR'and V=='LLLLRLRRRRLRRLRRRR'
assert U=='LLLLRLRRRRLRLLLLRRRRLRRLRRRR' and len(U)==28
assert ('U='+U+'.') in (HERE/'finite_support_complete8_exclusion.md').read_text()
# Bind the actual U literal as well as its packet-family name.
rows=[]
for a in IDS:
 b=0 if a in(0,1) else 4 if a in(4,5,6) else 7
 tails=G[a]['name'].count('C');base=G[b]['word']
 assert G[a]['word']==base+C*tails
 rows.append(dict(packet=a,name=G[a]['name'],base=G[b]['name'],C_tails=tails,word=G[a]['word'],length=len(G[a]['word']),U_family=(b==7)))
assert {r['name']for r in rows if not r['U_family']}=={'D','DC','V','VC','VCC'}
assert {r['name']for r in rows if r['U_family']}=={'U','UC','UCC'}
def F(m,u=0):
 B=57+38*(m-5)+60*u;R=(2*B+4)//5;t=(2*R+1)**2//3
 return 20*R*(t+1)+28*t
for m in range(5,200):
 assert F(m)>0 and F(m+1)>=F(m)
# Union6 presentation is not silently identified with T8.
assert len(V+'LRRRR')==23 and all(len(G[a]['word'])!=23 for a in IDS)
deps=[HERE/'finite_support_U_entry_exclusion_manifest.json',ROOT/'word_stabilization/dcv_finite_tail_theorem.md',ROOT/'word_stabilization/dcv_producer_closed_family_manifest.json',ROOT/'word_stabilization/dcv_producer_closed_family_signoff.md',ROOT/'word_stabilization/dcuv_epoch_reset_bound_manifest.json',GP]
out=dict(status='AUTHOR_FINITE_SUPPORT_ALL_COMPLETE8_EXCLUSION_PENDING_INDEPENDENT_AUDIT',scope='Finite COMPLETE black support at actual context-complete T8 factor entry. No infinite prepared-board, arbitrary eventual-language, label-union or universal-capture inference.',rows=rows,base_words=dict(D=D,C=C,V=V,U=U),first_U='Finite-prefix actual flips preserve finite complete support, so the first U suffix is covered by signed U-entry exclusion.',no_U='Expands literally to D/C/V; signed finite-tail exclusion, equivalently HS F(m,0) on every complete prefix.',first_U_interface=dict(T='<=F(m,0)',mass_at_U='<=m+T',radius_about_U_head='<=R0+T'),dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(HERE/'finite_support_complete8_exclusion_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],U_literal=U,U_length=len(U),T8=[r['name']for r in rows]),indent=2))
