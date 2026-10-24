"""Independent literal rows and exact ledger control for the all-word height proof."""
from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/v1_last_helper_frozen_20261023_1049';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'v1_dc_age3_last_helper.json').read_text());ids=(0,1,4,5,6,7,8,9);cc=dict(zip(ids,(0,1,0,1,2,0,1,2)))
core={z for z,b in walk(mark)[2].items()if b};G={}
for a in ids:
    end,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];black={z for z,b in req.items()if b}
    G[a]=(black-core,(black^flip)-{end+rotation(z,h)for z in core},end,h,req)
C=raws[1][len(raws[0]):];assert len(C)==15
for a,base in ((1,0),(5,4),(6,4),(8,7),(9,7)):assert raws[a]==raws[base]+C*cc[a]
ce,ch,*_=walk(C);center=-.5-.5j;delta=ce+rotation(center,ch)-center
assert ce==1j and ch==3 and delta==1+1j
height=lambda z:int(z.real+z.imag)
table={h:{a:height(rotation(G[a][2],h))for a in (0,4,7)}for h in (3,2,1)}
assert table=={3:{0:0,4:-2,7:-4},2:{0:-2,4:-4,7:-4},1:{0:0,4:2,7:4}}
assert [height(rotation(delta,h))for h in (3,2)]==[0,-2]
assert height(G[1][2])==3 and G[1][3]==3
masks=[]
for a,offset,slot,age in ((4,-2,3j,2),(7,-4,-1+4j,5)):
    I,O,*_=G[a];ih=sorted(offset+height(rotation(z,1))for z in I);oh=sorted(offset+height(rotation(z,1))for z in O)
    assert offset+height(rotation(slot,1))==1 and max(oh)==-1
    masks.append(dict(packet=a,offset=offset,input_heights=ih,output_heights=oh,critical_age=age,score_minus_2H=2*offset+(26 if a==4 else 30)))
assert {height(rotation(z,1))for z in G[0][1]}=={-2}
assert all(m['score_minus_2H']==22 for m in masks)
seed=core|{-2+2j,-1+1j,-1+3j,1j};assert len(seed)==9
board=set(seed);res={z:None for z in seed-core};pos=0j;h=0;clock=time=0;control={}
for k,a in enumerate((1,6,4,4)):
    I,O,end,dh,req=G[a];assert all((pos+rotation(z,h)in board)==v for z,v in req.items())
    assert board==set(res)|{pos+rotation(z,h)for z in core}and not(set(res)&{pos+rotation(z,h)for z in core})
    if k==2:
        assert (pos,h,clock,time)==(-3+2j,1,3,73)
        ages={str(xy(z)):clock-res[z]for z in (2,2j,3+1j)}
        assert ages=={'(2, 0)':3,'(0, 2)':2,'(3, 1)':3};control=ages
    for z in I:del res[pos+rotation(z,h)]
    for z in O:
        p=pos+rotation(z,h);assert p not in res;res[p]=clock
    for c in raws[a]:
        assert c==('L'if pos in board else'R');board.symmetric_difference_update({pos});h=(h+(-1 if c=='L'else 1))%4;pos+=(1j,1,-1j,-1)[h];time+=1
    clock+=cc[a]
for c in mark:
    assert c==('L'if pos in board else'R');board.symmetric_difference_update({pos});h=(h+(-1 if c=='L'else 1))%4;pos+=(1j,1,-1j,-1)[h];time+=1
assert time==120
out={'status':'PASS independent literal masks and actual sharp identity control; all-word balance proof separately reviewed',
     'manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),
     'base_height_table':table,'helper_masks':masks,'sharp_prehelper_ages':control,
     'scope':'Exact DC-output(3,1) to V-input(0,3), age3 branch. Requires simultaneous prehelper resources, not new roots or a funding contradiction.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
