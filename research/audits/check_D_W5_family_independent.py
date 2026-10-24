from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/D_W5_family_frozen_20261023_1518';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
p=0j;h=c=0
for a in(1,0,5,5):p+=rotation(G[a][0],h);h=(h+G[a][1])%4;c+=counts[a]
assert(p,h,c)==(-5+0j,1,3)
ve=rotation(G[4][0],1);vw=rotation(G[4][0],3);assert ve==3-1j and vw==-ve
# Affine expression after V^(w+2), VCC, V^w: coefficient of w cancels exactly.
far_constant=p+2*ve;far_coefficient=ve;assert far_constant==1-2j
late_constant=far_constant+rotation(G[6][0],1);late_coefficient=far_coefficient+vw
assert late_constant==5-2j and late_coefficient==0 and(h+G[6][1])%4==3
q=4-2j
for a in(4,6):assert 3j in G[a][3]and 3j not in G[a][4]and far_constant+rotation(3j,1)==q
assert late_constant+rotation(1j,3)==q and oldages[0,1j]==3
out=dict(status='PASS independent all-parameter affine endpoints and ordered-age crossing',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),prefix_pose=[-5,0,1],prefix_clock=3,far_VCC_pose='(1+3*w,-2-w,E)',late_D_pose=[5,-2,3],late_D_clock=5,reused_cell=[4,-2],replacement_maximum_age=2,scope='Only DC,D,VC,VC,V^(w+2),VCC,V^w,D,V,V for all integers w>=0; impossible on every board. No general D/W5 gate closure.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
