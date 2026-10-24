"""Local test for the genuinely non-unit heading-flip route.
Seven periods; all headings between pairs and all input colors are free,
subject only to exact adjacent heading compatibility. The central period
must contain a six-read bridge whose first movement opposes the coarse one.
The other two six-read bridges are square insertions, potentially recut.
"""
from pathlib import Path
import collections,itertools,json,hashlib,subprocess,time
import synthesize_heading_defect_pairs as s
P=Path(__file__).resolve().parent;O=P/'heading_defect_backward_window';O.mkdir(exist_ok=True)
s.old.old.O=O

def build(cut):
 names={};C=[]
 def var(t):
  if t not in names:names[t]=len(names)+1
  return names[t]
 coarse,_,_=s.old.old.core.trace(s.old.V,(0,0),3);h0=coarse[cut][1];W=s.old.V[cut:]+s.old.V[:cut]
 rows,e,hh=s.old.old.core.trace(W,(0,0),h0)
 bounds=[var(f'h{j}') for j in range(365)]
 groups=collections.defaultdict(lambda:collections.defaultdict(list));domains=[];bad_center=[]
 for r in range(7):
  rowdomains=[]
  for j in range(52):
   p,h=rows[2*j][:2];p=(p[0]-2*r,p[1]-2*r);pair=W[2*j:2*j+2]
   coarse_rr,ce,ch=s.old.old.core.trace(pair,p,h);first=coarse_rr[1][0]
   domain=[]
   for eps in [0,1]:
    a=s.pal[pair][str(eps)];domain.append((eps,0,a['reset']))
    domain.extend((eps,1,w) for w in a['flip'])
   rowdomains.append(domain);xx=[var(f'x{r}_{j}_{k}') for k in range(8)]
   C.append(xx);C.extend([-a,-b] for a,b in itertools.combinations(xx,2))
   for k,(eps,delta,w) in enumerate(domain):
    C.append([-xx[k],bounds[52*r+j] if eps else -bounds[52*r+j]])
    C.append([-xx[k],bounds[52*r+j+1] if delta else -bounds[52*r+j+1]])
    rr,ee,gg=s.old.old.core.trace(w,p,(h+2*eps)%4);assert(ee,gg)==(ce,(ch+2*delta)%4)
    bad=(rr[1][0]!=first)
    if bad:assert len(w)==6 and delta==1
    if r==3 and bad:bad_center.append(xx[k])
    for i,(q,gh,c) in enumerate(rr):groups[q][r,j,i,c].append(xx[k])
  domains.append(rowdomains)
 C.append(bad_center)
 for a,(q,ev) in enumerate(sorted(groups.items())):
  prev=var(f'input{a}')
  for b,(event,xs) in enumerate(sorted(ev.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}');C.extend([-x,active] for x in xs);C.append(xs+[-active]);C.append([-active,prev if event[3]=='L' else -prev])
   C.extend([[prev,active,-nxt],[-prev,-active,-nxt],[prev,-active,nxt],[-prev,active,nxt]]);prev=nxt
 return names,C,groups,domains,W,h0,bad_center

def run(cut):
 names,C,groups,domains,W,h0,bad_center=build(cut);tag=f'cut{cut}';cnf=O/(tag+'.cnf');cnf.write_text(s.old.old.dimacs(names,C))
 manifest=dict(scope=__doc__,cut=cut,coarse_word=W,coarse_start_heading=h0,domains=domains[0],periods=7,central_period=3,physical_cells=sorted(groups),variables=len(names),clauses=len(C),central_backward_selectors=bad_center)
 (O/(tag+'.architecture.json')).write_text(json.dumps(manifest,indent=2)+'\n')
 out,model=s.old.old.z3solve(names,C,tag,timeout=30000);out.update(cut=cut,variables=len(names),clauses=len(C),cells=len(groups))
 if model:
  images=[[next(a for k,a in enumerate(d) if model[names[f'x{r}_{j}_{k}']]) for j,d in enumerate(row)] for r,row in enumerate(domains)]
  w=''.join(a[2] for row in images for a in row);h=(h0+2*int(model[names['h0']]))%4;rr,e,hh=s.old.old.core.trace(w,(0,0),h)
  last={};I=set();B=set();reads=set()
  for q,g,c in rr:
   if q not in last and c=='L':I.add(q);B.add(q)
   assert(q in B)==(c=='L')
   if q in B:B.remove(q)
   else:B.add(q)
   last[q]=c;reads.add(q)
  assert e==(-14,-14)
  out.update(images=images,word=w,length=len(w),start_heading=h,final_heading=hh,input_black=sorted(I),output_black=sorted(B),read_support=sorted(reads))
 elif out['result']=='UNSAT_ARCHITECTURE':
  proof=O/(tag+'.rup');t=time.monotonic();p=subprocess.run([str(s.old.old.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120)
  out.update(producer=p.stdout.strip(),producer_returncode=p.returncode,proof_seconds=time.monotonic()-t)
  if p.returncode==0:
   c=subprocess.run([str(s.old.old.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120);assert c.returncode==0,(c.stdout,c.stderr);out['checker']=json.loads(c.stdout)
  out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest())
 (O/(tag+'.result.json')).write_text(json.dumps(out,indent=2)+'\n')
 print({k:v for k,v in out.items() if k not in ['images','word','input_black','output_black','read_support','producer']},flush=True)
if __name__=='__main__':
 for cut in [0,1]:run(cut)
