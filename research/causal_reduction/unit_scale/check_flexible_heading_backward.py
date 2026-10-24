"""Arbitrary monomer/six-read-flip tilings of inverse104, with free boundary headings.
The central period must contain a genuinely backward six-read tile.
"""
from pathlib import Path
import collections,itertools,json,hashlib,subprocess,time
import check_pair_bypass_flexible_tiling as geom
import synthesize_heading_defect_pairs as s
P=Path(__file__).parent;O=P/'flexible_heading_backward';O.mkdir(exist_ok=True);s.old.old.O=O;N=728

def build(require_backward=True):
 names={};C=[]
 def var(t):
  if t not in names:names[t]=len(names)+1
  return names[t]
 heads={i:var(f'h{i}')for i in range(-1,N+2)}
 pairs={};bp={};monos={};blocks={};domains={};groups=collections.defaultdict(lambda:collections.defaultdict(list));bad=[]
 for i in range(-1,N):
  p,h,c=geom.pose(i);pair=c+geom.pose(i+1)[2];first=geom.pose(i+1)[0]
  domain=[(eps,1,w)for eps in(0,1)for w in s.pal[pair][str(eps)]['flip']];domains[i]=domain
  xs=[var(f'x{i}_{k}')for k in range(6)];b=var(f'pair{i}');pairs[i]=xs;bp[i]=b
  C.extend([-a,-b]for a,b in itertools.combinations(xs,2));C.extend([-x,b]for x in xs);C.append(xs+[-b])
  for k,(eps,delta,w)in enumerate(domain):
   x=xs[k];C += [[-x,heads[i]if eps else-heads[i]],[-x,heads[i+2]]]
   rr,end,head=geom.s.old.core.trace(w,p,(h+2*eps)%4);assert(end,head)==(geom.pose(i+2)[0],(geom.pose(i+2)[1]+2)%4);blocks[i,k]=rr
   backward=rr[1][0]!=first
   if 312<=i<416 and backward:bad.append(x)
   for j,(q,gh,t)in enumerate(rr):groups[q][i,j,t].append(x)
 for i in range(-1,N-1):C.append([-bp[i],-bp[i+1]])
 for i in range(N):
  m=var(f'mono{i}');xs=[var(f'z{i}_{eps}')for eps in(0,1)];monos[i]=xs
  C += [[-xs[0],-xs[1]],[-xs[0],m],[-xs[1],m],[xs[0],xs[1],-m],[-m,-bp[i-1]],[-m,-bp[i]],[m,bp[i-1],bp[i]]]
  p,h,c=geom.pose(i)
  for eps,x in enumerate(xs):
   w=c if not eps else('L'if c=='R'else'R');rr,end,head=geom.s.old.core.trace(w,p,(h+2*eps)%4)
   assert(end,head)==geom.pose(i+1)[:2];blocks[i,6+eps]=rr
   C += [[-x,heads[i]if eps else-heads[i]],[-x,-heads[i+1]]]
   for j,(q,gh,t)in enumerate(rr):groups[q][i,j,t].append(x)
 if require_backward:C.append(bad)
 for a,(q,ev)in enumerate(sorted(groups.items())):
  prev=var(f'input{a}')
  for b,(event,xs)in enumerate(sorted(ev.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}');C.extend([-x,active]for x in xs);C.append(xs+[-active]);C.append([-active,prev if event[2]=='L'else-prev])
   C.extend([[prev,active,-nxt],[-prev,-active,-nxt],[prev,-active,nxt],[-prev,active,nxt]]);prev=nxt
 return names,C,groups,blocks,domains,bad

def run():
 names,C,g,blocks,domains,bad=build();tag='flexible_heading';cnf=O/(tag+'.cnf');cnf.write_text(s.old.old.dimacs(names,C))
 (O/(tag+'.architecture.json')).write_text(json.dumps(dict(scope=__doc__,periods=7,central_period=3,coarse_word=s.old.V,pair_indices=[-1,N-1],monomer_indices=[0,N-1],free_heading_indices=[-1,N+1],palettes=s.pal,backward_selectors=bad,variables=len(names),clauses=len(C),cells=sorted(g)),indent=2)+'\n')
 out,model=s.old.old.z3solve(names,C,tag,timeout=30000);out.update(variables=len(names),clauses=len(C),cells=len(g))
 if model:
  chosen={i:k for i in range(-1,N)for k in range(6)if model[names[f'x{i}_{k}']]};tiles=[];rr=[];word=''
  for i in range(-1,N):
   if i in chosen:k=chosen[i];tiles.append([i,k]);rr+=blocks[i,k];word+=domains[i][k][2]
   elif i>=0:
    active=[eps for eps in(0,1)if model[names[f'z{i}_{eps}']]]
    if active:
     k=6+active[0];tiles.append([i,k]);rr+=blocks[i,k];word+=blocks[i,k][0][2]
  start=tiles[0][0];p,h,c=geom.pose(start);h=(h+2*model[names[f'h{start}']])%4;direct,end,head=geom.s.old.core.trace(word,p,h);assert direct==rr
  I=set();B=set();last={}
  for q,h,c in rr:
   if q not in last and c=='L':I.add(q);B.add(q)
   assert(q in B)==(c=='L')
   if q in B:B.remove(q)
   else:B.add(q)
   last[q]=c
  out.update(tiles=tiles,word=word,input_black=sorted(I),output_black=sorted(B),length=len(word))
 elif out['result']=='UNSAT_ARCHITECTURE':
  proof=O/(tag+'.rup');t=time.monotonic();p=subprocess.run([str(s.old.old.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120);out.update(producer=p.stdout.strip(),producer_returncode=p.returncode,proof_seconds=time.monotonic()-t)
  if p.returncode==0:
   c=subprocess.run([str(s.old.old.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120);assert c.returncode==0;(out.update(checker=json.loads(c.stdout)))
  out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest());(O/(tag+'.result.json')).write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in['producer','tiles','word','input_black','output_black']},flush=True)
if __name__=='__main__':run()
