"""Finite exact control for a K-renewal rank's time-orientation obstruction."""
import json
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
def step(s):
 B,p,h=s; a=-1 if p in B else 1
 return (B^{p},(p[0]+D[(h+a)%4][0],p[1]+D[(h+a)%4][1]),(h+a)%4), ('R' if a==1 else 'L')
def inverse(s):
 B,p,h=s; q=(p[0]-D[h][0],p[1]-D[h][1]);a=1 if q in B else -1
 return B^{q},q,(h-a)%4
def reversal(s):
 B,p,h=s;return B,(p[0]-D[h][0],p[1]-D[h][1]),(h+2)%4
W=json.loads((Path(__file__).resolve().parents[1]/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
F={(W+W)[i:i+10] for i in range(104)}
def event(s):
 p=s
 for _ in range(10):p=inverse(p)
 word=''
 for _ in range(11):p,a=step(p);word+=a
 return {'eleven':word,'left_J':word[:10] not in F,'right_J':word[1:] not in F}
def serial(s):
 B,p,h=s;return {'black':sorted(B),'position':p,'heading':h}
s=(frozenset((1,y) for y in range(40)),(0,0),0)
word=''
for _ in range(40):s,a=step(s);word+=a
assert word=='RLLR'*10
X=s;Y,a=step(X);IY=reversal(Y);IX=reversal(X)
assert step(IY)[0]==IX
assert reversal(reversal(X))==X
ex=event(X);ey=event(IY)
assert ex['left_J'] and ex['right_J'] and ey['left_J'] and ey['right_J']

# A separate two-board toggle witness stays within one invariant sector.
Z=(X[0]^{X[1]},X[1],X[2]);Q,b=step(Z);ez=event(Z)
assert ez['left_J'] and ez['right_J']
assert Z[0]==Y[0] and Q[0]==X[0]
assert (Z[2]-sum(Z[1]))%2==(X[2]-sum(X[1]))%2
out={'status':'exact finite witness; no global termination claim',
     'standard_factor_count':len(F),'X':serial(X),'Y':serial(Y),
     'IY':serial(IY),'IX':serial(IX),'event_X':ex,'event_IY':ey,
     'same_sector_toggle_Z':serial(Z),'same_sector_toggle_Q':serial(Q),'event_Z':ez,
     'forward_turn':a,'reverse_turn':step(IY)[1],
     'S_phases_bad':all((('RLLR'*4)[i:i+10] not in F) for i in range(4))}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ('X','Y','IY','IX')},indent=2))
