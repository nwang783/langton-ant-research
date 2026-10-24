"""Independently regenerate all possible relaxed final origins of one saved word."""
from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/saved_u1_origin_frozen_20261023_1040'
manifest=json.loads((B/'manifest.json').read_text())
for f in manifest['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
for f in manifest['dependencies']:assert hashlib.sha256((ROOT/'core_periodicity_new'/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_u1_k5_joint_origin_obstruction.json').read_text())
for f,h in J['dependencies'].items():
    if f!='check_saved_u1_origin_obstruction.py':assert hashlib.sha256((ROOT/'core_periodicity_new'/f).read_bytes()).hexdigest()==h
ids=(0,1,4,5,6,7,8,9);cc=dict(zip(ids,(0,1,0,1,2,0,1,2)))
core={z for z,b in walk(mark)[2].items()if b};G={}
for a in ids:
    end,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];black={z for z,b in req.items()if b}
    out=(black^flip)-{end+rotation(z,h)for z in core}
    G[a]=(black-core,out,end,h)
HB={tuple(map(int,l.split()[:7]))for l in (ROOT/'core_periodicity_new/chronology_dcuv/protected_patch2.tsv').read_text().splitlines()}
word=J['word_including_goal'];assert len(word)==350 and word[-1]==7
# Choose one representative of the initial height/residue class, then follow
# literal endpoints.  Only height and residue will be used for eligibility.
pos=5-5j;heading=2;C=0;outputs=[];starts=[]
def project(z):return int(z.imag-z.real),int(z.real+z.imag)%4
for k,a in enumerate(word):
    I,O,delta,dh=G[a];starts.append((pos,heading,C))
    if k<len(word)-1:
        for o in sorted(O,key=xy):outputs.append((k,a,heading,o,pos+rotation(o,heading),C))
    pos+=rotation(delta,heading);heading=(heading+dh)%4;C+=cc[a]
goal,gh,gc=starts[-1];assert gh==0 and project(goal)==(0,0)and gc==122
assert project(starts[0][0])==(-10,0)
answer={}
for slot in sorted(G[7][0],key=xy):
    minimum=5 if slot in(-1+4j,2j,3j)else 3
    target=goal+slot;height,residue=project(target);assert height>-10
    eligible=[]
    for k,a,h,o,cell,birth in outputs:
        age=gc-birth
        if project(cell)!=(height,residue)or age<minimum:continue
        dh=(-h)%4;p=o-rotation(slot,dh)
        query=(a,7,*xy(p),dh,*xy(o))
        if query in HB:continue
        eligible.append((k,a,h,xy(o),age,query))
    key=str(xy(slot));author=J['origins'][key]
    expected=[(v['step'],v['packet'],v['heading'],tuple(v['slot']),v['age'],tuple(v['protected_transfer']))for v in author['eligible_outputs']]
    assert eligible==expected,(key,eligible,expected)
    answer[key]={'ages':sorted({v[4]for v in eligible}),'birth_steps':sorted({v[0]for v in eligible}),'candidate_count':len(eligible)}
A=answer[str((-1,1))]['ages'];Q=answer[str((-1,2))]['ages'];CC=answer[str((0,2))]['ages']
assert max(Q)<min(A)and max(Q)<min(CC)
result={'status':'PASS independent literal-endpoint all-origin superset replay',
        'manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),
        'packets':len(word),'C_before_goal':gc,'all_earlier_output_births_considered':len(outputs),
        'origins':answer,'contradiction':'Every eligible lower-middle age is strictly below every eligible lower-a and upper-c age, violating LN.',
        'scope':'One old saved U1 resource word with zero initial tokens above height -10. Reuses only signed HB and individual age minima; no U1 closure or novelty of this word exclusion.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
