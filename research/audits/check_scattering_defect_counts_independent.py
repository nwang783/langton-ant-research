"""Exact counts on certified word templates; no author count code is imported."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
R=Path(__file__).resolve().parents[1];P=R/'causal_reduction/unit_scale';A=R/'global_architecture_2026-10-23'
H=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];assert len(H)==104
other=(R/'word_stabilization/standard_word.txt').read_text().strip();assert other in H+H
def value(w):return int(''.join('1'if c=='L'else'0'for c in w),2)
allowed={value((H+H)[i:i+10])for i in range(104)};assert len(allowed)==84
cost=[int(i>>1 not in allowed and i&1023 not in allowed)for i in range(2048)]
def count(history,word):
    z=value(history);answer=0
    for ch in word:z=((z<<1)|(ch=='L'))&2047;answer+=cost[z]
    return answer
dirs=(1j,1,-1j,-1)
def inverse_history(board,p,h):
    board=set(board);out=[]
    for _ in range(10):
        p-=dirs[h];post=p in board;out.append('R'if post else'L');h=(h+(-1 if post else 1))%4;board.symmetric_difference_update({p})
    return ''.join(reversed(out))
def literal(board,p,h,n):
    board=set(board);word=[]
    for _ in range(n):
        black=p in board;word.append('L'if black else'R');h=(h+(-1 if black else 1))%4;board.symmetric_difference_update({p});p+=dirs[h]
    return ''.join(word)
F=json.loads((P/'unequal_four_corner_loop_certificate.json').read_text())['seed_families_ar_as_bx_cr_cs_by']
C=json.loads((P/'four_corner_capture_word.json').read_text())['word'];DD=json.loads((P/'four_corner_capture_word2.json').read_text())['word']
fixed=set();separated=0
for ar,ass,bx,cr,cs,by in F:
    if ar==ass==cr==cs==0:fixed.add(complex(bx,by));continue
    assert any((min(u,v)>=0 and 50*(u+v)+c>12)or(max(u,v)<=0 and 50*(u+v)+c< -12)for u,v,c in ((ar,ass,bx),(cr,cs,by)))
    separated+=1
history=inverse_history(fixed,0j,0);assert history=='RLLLLRLLLL'and len(fixed)==13 and separated==30
def loop(r,s):return ''.join('R'+H*n+H[:tail]for n,tail in ((r,68),(s,68),(r,68),(s,60)))
compressed=loop(1,1)+C+H+DD+H[:10]
assert len(compressed)==15210 and count(history,compressed)==5963
for r,s in ((50,50),(63,91),(123,52),(51,201)):
    board={complex(ar*r+ass*s+bx,cr*r+cs*s+by)for ar,ass,bx,cr,cs,by in F}
    assert inverse_history(board,0j,0)==history and count(history,loop(r,s)+C+H*(s-10)+DD+H[:10])==5963
# The twenty-cell all-n geometry remains a retained, conditional dependency.
gate={-1j,1+1j,1+3j,2+2j};prelude=literal(gate,0j,1,182)
recovery=json.loads((A/'feedback20_recovery_word.json').read_text())['word'];assert len(recovery)==774
phase=H[103:]+H[:103]
def seed(n):
    poses=((0j,1),(complex(n-1,n),0),(complex(-n,3*n-4),3),(complex(-5*n+5,-n),2),(complex(-3*n,-3*n+8),1))
    return {p+z*((-1j)**(h-1))for p,h in poses for z in gate}
local=inverse_history(gate,0j,1);assert local=='RLLLLRLLLL'
for pose20,pose22,h in ((19+20j,21+22j,0),(-20+56j,-22+62j,3),(-95-20j,-105-22j,2),(-60-52j,-66-58j,1)):
    for z in gate:
        x=pose20+z*((-1j)**(h-1));slope=(pose22-pose20)/2
        assert any((u>=0 and v>12)or(u<=0 and v< -12)for u,v in ((slope.real,x.real),(slope.imag,x.imag)))
compressed20=''.join(prelude+H+H[:t]for t in (61,71,61,71,14))+recovery+phase[:10]
assert len(compressed20)==2492 and count(local,compressed20)==440
for n in (20,26,40):
    k=n//2;word=''.join(prelude+H*num+H[:tail]for num,tail in zip((k-4,2*k-5,4*k-6,2*k-7,3*k-4),(61,71,61,71,14)))+recovery+phase[:10]
    assert literal(seed(n),0j,1,len(word))==word and inverse_history(seed(n),0j,1)==local and count(local,word)==440
report={'status':'PASS independent exact defect counts and affine inverse-history separation',
        'signed_43_cell_family':{'domain':'r,s>=50','exact_K':5963,'compressed_length':15210,'fixed_inverse_history':history,'moving_points_separated':30},
        'conditional_20_cell_family':{'domain':'even n>=20, conditional on retained all-n execution theorem','exact_K':440,'compressed_length':2492,'fresh_literal_controls':[20,26,40]},
        'scope':'Fixed templates have constant defects despite unbounded flight lengths. No uniform scattering budget, and no new all-n geometry signoff for the twenty-cell source.',
        'note_sha256':hashlib.sha256((A/'fixed_mass_scattering_budget_controls.md').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
