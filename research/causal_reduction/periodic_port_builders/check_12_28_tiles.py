"""Finite tile identities proving the externally reset all-n composition."""
import json,pathlib
from check_12_28_pair import reads,A,B
P=pathlib.Path(__file__).resolve().parent

def board(*tiles):
 return {(2*j+k,y) for j,t in enumerate(tiles) for k,m in enumerate(t) for y in range(4) if m>>y&1}
def run(w,entry,C):
 C=set(C);rr,end=reads(w,entry)
 for x,y,c in rr:
  assert ((x,y)in C)==(c=='L'),(w,(x,y),c)
  C.symmetric_difference_update({(x,y)})
 return C,end
I=(1,7);M=(8,14);C=(6,12);D=(0,6);Z=(7,13)
a,e=run(A,(0,0,1),board(I));assert a==board(M) and e==(2,0,1)
b,e=run(B,(2,2,1),board(C,M));assert b==board(D,Z) and e==(4,2,1)
b,e=run(B,(2,2,1),board(Z,M));assert b==board(I,Z) and e==(4,2,1)
checks=[]
for n in range(1,101):
 initial={(x-2,y)for x,y in board(C,*([I]*n))}
 out,e=run(A*n,(0,0,1),initial);assert e==(2*n,0,1)
 out,e=run(B*n,(0,2,1),out);assert e==(2*n,2,1)
 expected={(x-2,y)for x,y in board(D,*([I]*(n-1)),Z)}
 assert out==expected and len(initial)==len(out)==4*n+4
 patch={(-2,1),(-2,2),(-1,1),(-1,3)}
 assert initial^out==patch|{(x+2*n,y)for x,y in patch}
 checks.append([n,len(initial),len(initial^out)])
(P/'12_28_tile_certificate.json').write_text(json.dumps(dict(local_identities=3,controls=checks),indent=2))
print('PASS: 3 literal tile identities and 100 controlled finite compositions')
