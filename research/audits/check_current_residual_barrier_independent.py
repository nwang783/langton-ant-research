"""Exact rational atom-chord versus physical-edge contact inventory."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'core_periodicity_new/current_residual_barrier_frozen_20261023_1822';M=json.loads((D/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((D/f['frozen']).read_bytes()).hexdigest()==f['sha256']
K={q for q,b in walk(mark)[2].items()if b};corr=-1-1j;words=dict(D=raws[0],V=raws[4],U=raws[7],C=raws[1][len(raws[0]):])
def edge(q):
 x,y=xy(q);v=1+1j if(x+y)%2==0 else 1-1j;return 2*q-v,2*q+v
def det(a,b):return int(a.real*b.imag-a.imag*b.real)
def hit(a,b,c,d):
 u=b-a;v=d-c;w=c-a;den=det(u,v)
 if den:
  s=F(det(w,v),den);t=F(det(w,u),den)
  return ('point',str(s),str(t))if 0<s<1 and 0<=t<=1 else None
 if det(w,u):return None
 proj=lambda q:int(q.real)if u.real else int(q.imag)
 lo,hi=sorted([F(proj(c-a),proj(u)),F(proj(d-a),proj(u))]);lo=max(lo,F(0));hi=min(hi,F(1))
 return ('overlap',str(lo),str(hi))if hi>0 and lo<1 and hi>=lo else None
rows=[]
for name,w in words.items():
 ep,h,_,_=walk(w);end=2*ep+rotation(corr,h);req=walk(w+mark)[2];I={q for q,b in req.items()if b}-K
 assert {q for q,b in req.items()if b}==K|I
 bounds=[]
 for a,b in zip(xy(corr),xy(end)):bounds.append(((min(a,b)-1+1)//2,(max(a,b)+1)//2))
 candidates=[];contacts=[]
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   q=complex(x,y);candidates.append((x,y));r=hit(corr,end,*edge(q))
   if r:
    role='core'if q in K else'input'if q in I else'white'if req.get(q)is False else'bad';assert role!='bad';contacts.append(dict(cell=(x,y),role=role,contact=r))
 expected={(0,0):'core'}if name in('D','C')else{(0,1):'white'}if name=='V'else{(-1,1):'input',(-1,2):'input',(0,2):'input',(0,1):'white'}
 assert {r['cell']:r['role']for r in contacts}==expected
 initialstar={q for q in K if corr in edge(q)};assert len(initialstar)==4
 exitK={ep+rotation(q,h)for q in K};assert len({q for q in exitK if end in edge(q)})==4
 endpoint_inputs={q for q in I if end in edge(q)}
 assert endpoint_inputs==({'D':{1j},'V':{3j,1+2j},'U':{-1+4j,3j},'C':set()}[name])
 rows.append(dict(atom=name,chord=(xy(corr),xy(end)),candidate_cells=candidates,contacts=contacts,exit_input_contacts=sorted(map(xy,endpoint_inputs))))
assert sum(len(r['candidate_cells'])for r in rows)==45
out=dict(status='PASS independent exact45-cell contact enumeration and atomic endpoint stars',manifest_sha256=hashlib.sha256((D/'manifest.json').read_bytes()).hexdigest(),rows=rows,scope='Current ordered residual edge is disjoint from subsequent actual atomic center path strictly before its consuming base. Consumption and fresh recycling end/start different lifetimes. No historical wire or component connectivity is inferred.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
