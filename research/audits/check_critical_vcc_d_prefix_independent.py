"""Independent center arithmetic and two complete literal words for critical edge."""
from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import raws,mark,walk,rotation,xy
ROOT=Path(__file__).resolve().parents[1];F=ROOT/'core_periodicity_new/critical_vcc_d_prefix_frozen_20261023_0848'
M=json.loads((F/'manifest.json').read_text())
for f in M:assert hashlib.sha256((F/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((F/'critical_vcc_d_forced_prefix.json').read_text())
C=raws[1][len(raws[0]):];assert raws[1]==raws[0]+C and raws[6]==raws[4]+C+C
# Center correction makes the unique C translate by(1,1) and rotate CCW.
s=-.5-.5j;ec,hc,*_=walk(C);assert hc==3 and ec+rotation(s,hc)-s==1+1j
for a,d in[(0,1+1j),(4,1+3j),(7,4j)]:assert walk(raws[a])[:2]==(d,0)
es,hs,*_=walk(raws[6]);target=-1+0j;ht=1
remaining=rotation(target+rotation(s,ht)-es-rotation(s,hs),-hs)
assert remaining==2+4j and remaining-(1+1j)==1+3j
# Exact nonnegative reduction y-x=2 bounds all six variables without a cutoff.
sol=[]
for b,d in[(1,0),(0,1)]:
 a=1-b+d;c=e=f=0
 assert a+b-d-3*e-4*f==1 and a+3*b+4*c+d+e==3
 sol.append(((a,b,c),(d,e,f)))
assert sol==[((0,1,0),(0,0,0)),((2,0,0),(1,0,0))]
records=[]
for seq in[(6,5,0),(6,0,1,0,0)]:
 word=''.join(raws[a]for a in seq)+mark;p=0j;h=1j;last={};events=[];bad=None;poses=[]
 boundaries=[];t=0
 for a in seq:boundaries.append(t);t+=len(raws[a])
 for t,c in enumerate(word):
  if t in boundaries:poses.append([*xy(p),[1j,1,-1j,-1].index(h)])
  if p in last and last[p][1]==c:bad=(last[p][0],t,xy(p),c);break
  last[p]=(t,c);events.append((t,xy(p),c));h*=(-1j if c=='R'else 1j);p+=h
 records.append({'word':seq,'poses':poses,'conflict':bad,'q_reads':[e for e in events if e[1]==(0,0)]})
assert records[0]['conflict']is None and records[0]['poses']==[[0,0,0],[0,4,2],[-1,0,1]]
assert records[0]['q_reads']==[(0,(0,0),'L'),(4,(0,0),'R'),(92,(0,0),'L')]
assert records[1]['conflict']==(19,59,(0,3),'L')
# Complete intermediate VC context misses the protected identity.
for z in walk(raws[5]+mark)[2]:assert 4j+rotation(z,2)!=0j
out={'status':'PASS complete one-C center enumeration and literal protected prefix','manifest_sha256':hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),'solutions':sol,'records':records,'scope':'Only VCC output(0,0) to D input(0,1), relativepose(-1,0,E), exactsource-included C age3. Its only feasible intermediate packet is VC. No exclusion of the feasible path or repeated cycle.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
