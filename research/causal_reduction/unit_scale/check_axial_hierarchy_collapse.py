"""Check the finite local certificates used by the all-decoration collapse.
No author geometry imports. Prefix cubes certify every one of2^17 child maps.
"""
from pathlib import Path
import hashlib,json

P=Path(__file__).resolve().parent
J=json.loads((P/'axial_body_refinement_classification.json').read_text())
W='RRLRRRRLRLLRLLRLL'
swap=lambda w:w.translate(str.maketrans('RL','LR'))
assert J['body']==W

def trace(word,head=1j):
    p=0j;rows=[];last={};bad=None
    for n,c in enumerate(word):
        if p in last and last[p][1]==c and bad is None:
            bad=dict(cell=[int(p.real),int(p.imag)],previous=list(last[p]),current=[n,c])
        last[p]=(n,c);rows.append((p,head,c))
        head*= -1j if c=='R' else 1j;p+=head
    return rows,p,head,bad

def word_for(mask,n=17):
    return ''.join((W if c=='R' else swap(W)) if mask>>i&1 else c for i,c in enumerate(W[:n]))

cubes=[]
for r in J['conflict_cubes']:
    n=r['assigned'];m=r['mask'];word=word_for(m,n)
    b=trace(word)[3];assert b is not None
    assert b['cell']==r['conflict']['cell']
    assert b['previous']==r['conflict']['previous']
    assert b['current']==r['conflict']['current']
    cubes.append((n,m))
leaves=[]
for r in J['survivors']:
    m=r['mask'];word=word_for(m);rows,p,h,b=trace(word)
    assert b is None and (p,h)==(1+0j,1+0j)
    assert r['active']==[i for i in range(17) if m>>i&1]
    leaves.append(m)
assert sorted(leaves)==[0,1<<8,1<<11]
allc=cubes+[(17,m) for m in leaves]
for i,(n,m) in enumerate(allc):
    for nn,mm in allc[:i]:
        assert (m^mm)&((1<<min(n,nn))-1)
assert sum(1<<(17-n) for n,m in allc)==1<<17

chains=[]
for i in (8,11):
    for j in (8,11):
        child=W if W[i]=='R' else swap(W)
        grand=W if child[j]=='R' else swap(W)
        expanded=child[:j]+grand+child[j+1:]
        word=W[:i]+expanded+W[i+1:]
        rows,p,h,bad=trace(word)
        assert len(word)==49 and (p,h)==(1+0j,1+0j)
        assert (bad is not None)==(j==11)
        if bad is not None:
            assert bad==({ 'cell':[2,2],'previous':[32,'L'],'current':[44,'L']} if i==8 else
                         { 'cell':[0,1],'previous':[35,'L'],'current':[47,'L']})
        chains.append(dict(slots=[i,j],word=word,conflict=bad))

# Explicit rotations and finite-contract reflections preserve all local tests.
typed_controls=0
for head in (1j,1,-1j,-1):
    for reflect in (False,True):
        for n,m in allc:
            word=word_for(m,n)
            if reflect:word=swap(word)
            bad=trace(word,head)[3]
            assert (bad is None)==(n==17 and m in leaves)
            typed_controls+=1
        for r in chains:
            word=swap(r['word']) if reflect else r['word']
            assert (trace(word,head)[3] is not None)==(r['slots'][1]==11)
            typed_controls+=1

note=P/'axial_primitive_hierarchy_collapse.md'
out=dict(status='PASS complete local cover and all physical-type chain controls',
    scope=__doc__,covered=1<<17,cubes=len(cubes),survivors=leaves,chains=chains,
    typed_controls=typed_controls,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),
    classification_sha256=hashlib.sha256((P/'axial_body_refinement_classification.json').read_bytes()).hexdigest())
(P/'axial_hierarchy_collapse_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],out['cubes'],out['survivors'],typed_controls)
