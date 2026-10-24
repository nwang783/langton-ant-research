"""Derived seven-period rigidity test with arbitrary monomer/dimer tiling.
Both pairing parities may change at every occurrence. Boundary-spanning pairs
are included explicitly; all initial cell colors and all output are free.
"""
from pathlib import Path
import collections,itertools,json,hashlib,subprocess,time
import synthesize_pair_bypass_scaffold as s
P=Path(__file__).parent;O=P/'pair_bypass_flexible_tiling';O.mkdir(exist_ok=True);s.old.O=O
N=7*104
base=s.old.core.trace(s.V*2,(0,0),3)[0]
def pose(i):
 r,j=divmod(i,104);p,h,c=base[j];return (p[0]-2*r,p[1]-2*r),h,c

def build(require_center=True):
 names={};C=[]
 def var(t):
  if t not in names:names[t]=len(names)+1
  return names[t]
 pairs={};presence={};identity={};groups=collections.defaultdict(lambda:collections.defaultdict(list));blocks={}
 for i in range(-1,N):
  xs=[var(f'x{i}_{k}')for k in range(2)];b=var(f'pair{i}');pairs[i]=xs;presence[i]=b
  C += [[-xs[0],-xs[1]],[-xs[0],b],[-xs[1],b],[xs[0],xs[1],-b]]
 for i in range(-1,N-1):C.append([-presence[i],-presence[i+1]])
 for i in range(N):
  m=var(f'mono{i}');identity[i]=m
  C += [[-m,-presence[i-1]],[-m,-presence[i]],[m,presence[i-1],presence[i]]]
  p,h,c=pose(i);rr,end,head=s.old.core.trace(c,p,h);blocks[i,-1]=rr
  for j,(q,hh,t)in enumerate(rr):groups[q][i,j,t].append(m)
 for i,xs in pairs.items():
  p,h,c=pose(i);pair=c+pose(i+1)[2]
  for k,w in enumerate(s.PAL[pair][1:]):
   rr,end,head=s.old.core.trace(w,p,h);assert(end,head)==s.old.core.trace(pair,p,h)[1:];blocks[i,k]=rr
   for j,(q,hh,t)in enumerate(rr):groups[q][i,j,t].append(xs[k])
 if require_center:C.append([x for i in range(312,416) for x in pairs[i]])
 for a,(q,ev)in enumerate(sorted(groups.items())):
  prev=var(f'input{a}')
  for b,(event,xs)in enumerate(sorted(ev.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}')
   C.extend([-x,active]for x in xs);C.append(xs+[-active])
   C.append([-active,prev if event[2]=='L'else-prev])
   C.extend([[prev,active,-nxt],[-prev,-active,-nxt],[prev,-active,nxt],[-prev,active,nxt]])
   prev=nxt
 return names,C,groups,blocks

def horizon():
 d=collections.defaultdict(set)
 for i in range(104):
  p,h,c=pose(i)
  for w in [c]+s.PAL[c+pose(i+1)[2]][1:]:
   for q,hh,t in s.old.core.trace(w,p,h)[0]:d[q[0]-q[1],q[0]%2].add(q[0]//2)
 assert max(max(v)-min(v)for v in d.values())==3
 return [dict(orbit=a,minimum=min(v),maximum=max(v))for a,v in sorted(d.items())]

def run():
 names,C,g,blocks=build();tag='flexible';cnf=O/(tag+'.cnf');cnf.write_text(s.old.dimacs(names,C))
 manifest=dict(scope=__doc__,periods=7,central_period=3,coarse_word=s.V,coarse_heading=3,pair_start_indices=[-1,N-1],identity_indices=[0,N-1],palettes=s.PAL,horizon=horizon(),variables=len(names),clauses=len(C),physical_cells=sorted(g))
 (O/(tag+'.architecture.json')).write_text(json.dumps(manifest,indent=2)+'\n')
 out,model=s.old.z3solve(names,C,tag,timeout=30000);out.update(variables=len(names),clauses=len(C),cells=len(g))
 if model:
  chosen={i:k for i in range(-1,N)for k in range(2)if model[names[f'x{i}_{k}']]};literal=[];tiles=[]
  for i in range(-1,N):
   if i in chosen:literal+=blocks[i,chosen[i]];tiles.append([i,chosen[i]])
   elif i>=0 and model[names[f'mono{i}']]:literal+=blocks[i,-1];tiles.append([i,-1])
  last={};I=set();B=set()
  for t,(q,h,c)in enumerate(literal):
   if q not in last:
    if c=='L':I.add(q);B.add(q)
   assert(q in B)==(c=='L')
   if q in B:B.remove(q)
   else:B.add(q)
   last[q]=t
  out.update(tiles=tiles,length=len(literal),input_black=sorted(I),output_black=sorted(B),bypasses=sorted(chosen.items()))
 elif out['result']=='UNSAT_ARCHITECTURE':
  proof=O/(tag+'.rup');t=time.monotonic();p=subprocess.run([str(s.old.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120)
  out.update(producer=p.stdout.strip(),producer_returncode=p.returncode,proof_seconds=time.monotonic()-t)
  if p.returncode==0:
   c=subprocess.run([str(s.old.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120);assert c.returncode==0,(c.stdout,c.stderr);out['checker']=json.loads(c.stdout)
  out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();out['cnf_sha256']=hashlib.sha256(cnf.read_bytes()).hexdigest()
 (O/(tag+'.result.json')).write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in['producer','tiles','input_black','output_black','bypasses']},flush=True)
if __name__=='__main__':run()
