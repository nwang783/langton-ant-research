"""Seven coarse periods, independent pair choices, arbitrary entry colors.
A required central bypass tests local nonstationary deployment. The seven
periods are the full radius-three same-cell overlap neighborhood.
"""
from pathlib import Path
import collections,itertools,json,hashlib,subprocess,time
import synthesize_pair_bypass_scaffold as s
P=Path(__file__).resolve().parent;O=P/'pair_bypass_local_window';O.mkdir(exist_ok=True)
s.old.O=O

def build(cut):
 names={};C=[]
 def var(t):
  if t not in names:names[t]=len(names)+1
  return names[t]
 coarse,_,_=s.old.core.trace(s.V,(0,0),3);h0=coarse[cut][1];word=s.V[cut:]+s.V[:cut]
 rows,e,h=s.old.core.trace(word,(0,0),h0);assert(e,h)==((-2,-2),h0)
 groups=collections.defaultdict(lambda:collections.defaultdict(list));center=[]
 for r in range(7):
  for j in range(52):
   p,h=rows[2*j][:2];p=(p[0]-2*r,p[1]-2*r);pair=word[2*j:2*j+2]
   xx=[var(f'x{r}_{j}_{k}') for k in range(3)]
   C.append(xx);C.extend([-a,-b] for a,b in itertools.combinations(xx,2))
   if r==3:center+=xx[1:]
   for k,w in enumerate(s.PAL[pair]):
    rr,ee,gg=s.old.core.trace(w,p,h)
    assert(ee,gg)==s.old.core.trace(pair,p,h)[1:]
    for i,(q,hh,c) in enumerate(rr):groups[q][r,j,i,c].append(xx[k])
 C.append(center)
 for a,(q,ev) in enumerate(sorted(groups.items())):
  prev=var(f'input{a}')
  for b,(event,xs) in enumerate(sorted(ev.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}')
   C.extend([-x,active] for x in xs);C.append(xs+[-active])
   C.append([-active,prev if event[3]=='L' else -prev])
   C.extend([[prev,active,-nxt],[-prev,-active,-nxt],[prev,-active,nxt],[-prev,active,nxt]])
   prev=nxt
 return names,C,groups,word,h0

def run(cut):
 names,C,g,word,h=build(cut);tag=f'cut{cut}';cnf=O/(tag+'.cnf');cnf.write_text(s.old.dimacs(names,C))
 (O/(tag+'.architecture.json')).write_text(json.dumps(dict(scope=__doc__,cut=cut,word=word,start_heading=h,palettes=s.PAL,periods=7,central_period=3,physical_cells=sorted(g),variables=len(names),clauses=len(C)),indent=2)+'\n')
 out,model=s.old.z3solve(names,C,tag,timeout=30000);out.update(cut=cut,variables=len(names),clauses=len(C),cells=len(g))
 if model:
  images=[[next(w for k,w in enumerate(s.PAL[word[2*j:2*j+2]]) if model[names[f'x{r}_{j}_{k}']]) for j in range(52)] for r in range(7)]
  ww=''.join(w for row in images for w in row);rr,e,hh=s.old.core.trace(ww,(0,0),h)
  known={};I=set();black=set();reads=set()
  for q,g,c in rr:
   if q not in known:
    if c=='L':I.add(q);black.add(q)
   assert (q in black)==(c=='L')
   if q in black:black.remove(q)
   else:black.add(q)
   known[q]=c;reads.add(q)
  assert(e,hh)==((-14,-14),h)
  out.update(images=images,word=ww,length=len(ww),input_black=sorted(I),output_black=sorted(black),read_support=sorted(reads),nonidentity_counts=[sum(len(w)>2 for w in row) for row in images])
 else:
  if out['result']=='UNSAT_ARCHITECTURE':
   proof=O/(tag+'.rup');t=time.monotonic();p=subprocess.run([str(s.old.core.HERE/'prove_cnf_rup'),str(cnf),str(proof),'100000'],capture_output=True,text=True,timeout=120)
   out.update(producer=p.stdout.strip(),producer_returncode=p.returncode,proof_seconds=time.monotonic()-t)
   if p.returncode==0:
    c=subprocess.run([str(s.old.core.HERE/'check_drat'),str(cnf),str(proof)],capture_output=True,text=True,timeout=120);assert c.returncode==0,(c.stdout,c.stderr);out['checker']=json.loads(c.stdout)
   out['rup_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
 out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();out['cnf_sha256']=hashlib.sha256(cnf.read_bytes()).hexdigest()
 (O/(tag+'.result.json')).write_text(json.dumps(out,indent=2)+'\n')
 print({k:v for k,v in out.items() if k not in ['images','word','input_black','output_black','read_support','producer']},flush=True)
if __name__=='__main__':
 for cut in [0,1]:run(cut)
