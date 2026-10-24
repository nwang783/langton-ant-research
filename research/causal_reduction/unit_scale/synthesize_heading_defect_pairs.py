"""Minimal persistent heading defects along inverse104 pair endpoints.
Each pair preserves its spatial endpoint but its incoming/final heading may
be the coarse heading or its opposite. Minimal images: length2 resets the
heading, length6 flips it (three geometric routes). A cyclic binary boundary
state supplies exact context, not independently chosen incompatible images.
"""
from pathlib import Path
import collections,itertools,json,hashlib,subprocess,time
import synthesize_pair_bypass_scaffold as old
from minimal_pair_heading_bridge import periodic,old_alignment
P=Path(__file__).resolve().parent;O=P/'heading_defect_pairs';O.mkdir(exist_ok=True)
old.old.O=O
pal=json.loads((P/'minimal_pair_heading_bridge.json').read_text())['palettes']

def build(cut,rootflip,mode):
 names={};C=[]
 def var(t):
  if t not in names:names[t]=len(names)+1
  return names[t]
 coarse,_,_=old.old.core.trace(old.V,(0,0),3);h0=coarse[cut][1];W=old.V[cut:]+old.V[:cut]
 rows,e,g=old.old.core.trace(W,(0,0),h0);assert(e,g)==((-2,-2),h0)
 boundaries=[var(f'h{j}') for j in range(52)];C.append([boundaries[0] if rootflip else -boundaries[0]])
 groups=collections.defaultdict(lambda:collections.defaultdict(list));domains=[]
 for j in range(52):
  pair=W[2*j:2*j+2];p,h=rows[2*j][:2];domain=[]
  for eps in [0,1]:
   a=pal[pair][str(eps)];domain.append((eps,0,a['reset']))
   domain.extend((eps,1,w) for w in a['flip'])
  domains.append(domain);xx=[var(f'x{j}_{k}') for k in range(8)]
  C.append(xx);C.extend([-a,-b] for a,b in itertools.combinations(xx,2))
  for k,(eps,delta,w) in enumerate(domain):
   C.append([-xx[k],boundaries[j] if eps else -boundaries[j]])
   C.append([-xx[k],boundaries[(j+1)%52] if delta else -boundaries[(j+1)%52]])
   rr,ee,hh=old.old.core.trace(w,p,(h+2*eps)%4)
   ce,ch=old.old.core.trace(pair,p,h)[1:];assert(ee,hh)==(ce,(ch+2*delta)%4)
   for i,(q,g,c) in enumerate(rr):groups[old.old.key(q)][q[0]//2,j,i,c].append(xx[k])
 C.append(boundaries) # genuine heading defect somewhere
 rails=[];conflicts=[]
 if mode=='rails':
  for label,h in [('NE',1),('SW',3)]:
   R,B=old.old.standard_profile(h)
   shifts={(a[0]-b[0],(a[1]-b[1])%2) for a in groups for b in B if (a[0]-b[0]+h-h0)%2==0}
   for n,p in sorted(shifts):
    tr=lambda q:(q[0]+n,(q[1]+p)%2)
    rails.append(dict(orientation=label,normal_shift=n,x_parity_shift=p,read=set(map(tr,R)),black=set(map(tr,B))))
  for i,r in enumerate(rails):r['selector']=var(f'rail{i}')
  for i,j in itertools.combinations(range(len(rails)),2):
   if rails[i]['read']&rails[j]['read']:
    C.append([-rails[i]['selector'],-rails[j]['selector']]);conflicts.append((i,j))
 for a,(orb,ev) in enumerate(sorted(groups.items())):
  prev=var(f'input{a}')
  if mode=='rails':
   xs=[r['selector'] for r in rails if orb in r['black']];C.extend([[-x,prev] for x in xs]+[xs+[-prev]])
  elif mode!='free':raise ValueError(mode)
  for b,(event,xs) in enumerate(sorted(ev.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}');C.extend([-x,active] for x in xs);C.append(xs+[-active])
   C.append([-active,prev if event[3]=='L' else -prev])
   C.extend([[prev,active,-nxt],[-prev,-active,-nxt],[prev,-active,nxt],[-prev,active,nxt]]);prev=nxt
 return names,C,groups,domains,W,(h0+2*rootflip)%4,rails,conflicts

def run(cut,rootflip,mode):
 names,C,groups,domains,W,h,rails,conflicts=build(cut,rootflip,mode);tag=f'cut{cut}_root{rootflip}_{mode}'
 cnf=O/(tag+'.cnf');cnf.write_text(old.old.dimacs(names,C))
 manifest=dict(scope=__doc__,cut=cut,rootflip=rootflip,mode=mode,coarse_word=W,start_heading=h,domains=domains,orbits=sorted(groups),variables=len(names),clauses=len(C),rails=[{**{k:v for k,v in r.items() if k not in ('read','black')},'read':sorted(r['read']),'black':sorted(r['black'])} for r in rails],rail_conflicts=conflicts)
 (O/(tag+'.architecture.json')).write_text(json.dumps(manifest,indent=2)+'\n')
 out,model=old.old.z3solve(names,C,tag,timeout=30000);out.update(cut=cut,rootflip=rootflip,mode=mode,variables=len(names),clauses=len(C))
 if model:
  images=[next(a for k,a in enumerate(d) if model[names[f'x{j}_{k}']]) for j,d in enumerate(domains)]
  w=''.join(a[2] for a in images);literal=periodic(w,h);assert literal['status']=='LEGAL_PREPARED'
  out.update(images=images,literal=literal,old_unit_alignment=(not rootflip and old_alignment(w,W)),heading_defects=[j for j in range(52) if model[names[f'h{j}']]])
  if mode=='rails':
   sel=[i for i,r in enumerate(rails) if model[r['selector']]];B=set().union(*(rails[i]['black'] for i in sel)) if sel else set()
   read=set(tuple(v['orbit']) for v in literal['complete_histories']);assert B&read==set(map(tuple,literal['input_black_classes']))
   out.update(selected_rails=sel,input_black_classes=sorted(B))
 elif out['result']=='UNSAT_ARCHITECTURE':
  proof=O/(tag+'.rup');t=time.monotonic();p=subprocess.run([str(old.old.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120)
  out.update(producer=p.stdout.strip(),producer_returncode=p.returncode,proof_seconds=time.monotonic()-t)
  if p.returncode==0:
   c=subprocess.run([str(old.old.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120);assert c.returncode==0,(c.stdout,c.stderr);out['checker']=json.loads(c.stdout)
  out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest())
 (O/(tag+'.result.json')).write_text(json.dumps(out,indent=2)+'\n')
 print(tag,{k:v for k,v in out.items() if k not in ['literal','images','producer']},flush=True)
 return out
if __name__=='__main__':
 for cut in [0,1]:
  for root in [0,1]:
   out=run(cut,root,'free')
   if out['result']=='SAT_BULK_ONLY':run(cut,root,'rails')
