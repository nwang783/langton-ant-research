from pathlib import Path
import json,hashlib
ROOT=Path('/workspace/shared/langton')
def run(w,z,h,B):
 hist={}
 for c in w:
  assert(z in B)==(c=='L'),(c,z,h)
  hist[z]=hist.get(z,'')+c;B.symmetric_difference_update({z});h*=(-1j if c=='R'else 1j);z+=h
 return z,h,B,hist
rows=[];growth=[]
for r in (1,2,3,4,5,8,16,31,64,257,1024):
 I={complex(x,0)for x in range(2*r+1)}|{-1+1j,2*r+1j};O={complex(x,0)for x in range(2*r)}|{-2,-2+1j,-1+1j}
 z,h,B,H=run('LRRL'*r+'LLLR'+'RLLR'*r+'RRRL',0j,1,set(I))
 assert(z,h)==(0,1) and B==O and I^O=={-2,-2+1j,2*r,2*r+1j}
 assert set(H)=={complex(x,y)for x in range(-2,2*r+1)for y in(0,1)}
 assert sum(map(len,H.values()))==8*r+8
 rows.append(dict(r=r,steps=8*r+8,input=len(I),output=len(B),xor=len(I^O),support=len(H)))
 J=I-{2*r+1j};expected=J|{-2,-2+1j,2*r+1,2*r+1+1j}
 zz,hh,BB,HH=run('LRRL'*r+'LRRRRLLR'+'RLLR'*r+'RRRL',0j,1,set(J))
 assert(zz,hh)==(0,1) and BB==expected and len(BB-J)==4 and not(J-BB)
 assert len(J)==2*r+2 and len(BB)==2*r+6
 growth.append(dict(r=r,steps=8*r+12,input=len(J),output=len(BB),xor=len(J^BB)))
# Literal generic stage traces without relying on a board, separate geometry.
traces=[]
for word,head in [('LRRL',1),('LLLR',1),('LRRRRLLR',1),('RLLR',-1),('RRRL',-1)]:
 z=0j;h=head;reads=[]
 for c in word:
  reads.append([int(z.real),int(z.imag),c]);h*=(-1j if c=='R'else 1j);z+=h
 traces.append(dict(word=word,reads=reads,endpoint=[int(z.real),int(z.imag)],heading=[int(h.real),int(h.imag)]))
J={'status':'PASS complete-field literal controls and reviewed disjoint-interval four-stage all-r induction','traces':traces,'controls':rows,'growth_cap_controls':growth,'scope':'Prepared closed-pose axial domino transfer and four-cell growth cap, exactly four changed cells; linear initial mass. Not renewal, growing root or finite-seed counterexample.','hashes':{'auditor':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'note':hashlib.sha256((ROOT/'causal_reduction/unit_scale/axial_domino_transport.md').read_bytes()).hexdigest()}}
Path(__file__).with_suffix('.json').write_text(json.dumps(J,indent=2)+'\n');print(json.dumps(J))
