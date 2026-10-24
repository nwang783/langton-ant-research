"""Explicit Boolean CNF and solver-independent monotone RUP certificates.
Family: phasewise pose-preserving legal length1/5/9 images, not arbitrary words.
"""
from pathlib import Path
import json,itertools,collections,subprocess,hashlib,time
from probe_perpendicular_highway_wake import H
from certify_highway_wake_reflector import trace
from search_heading_transport import legal_image
P=Path(__file__).resolve().parent;HERE=P.parent/'morphic_candidates';OUT=P/'short_refinement_rup';OUT.mkdir(exist_ok=True)
dom={c:[w for n in[1,5,9]for z in itertools.product('RL',repeat=n)if legal_image(w:=''.join(z),target)]for c,target in[('R',(1,0,1)),('L',(-1,0,3))]}
wake=set(map(tuple,json.loads((P/'shifted_reverse104_bulk.json').read_text())['wake_black_classes']))
def cnf(word,start,input_black,nontrivial=True,only=None):
 names={};C=[]
 def var(n):
  if n not in names:names[n]=len(names)+1
  return names[n]
 true=var('TRUE');C.append([true]);groups=collections.defaultdict(lambda:collections.defaultdict(list));coarse,end,eh=trace(word,start,3)
 for j,(p,h,c)in enumerate(coarse):
  xs=[var(f'x{j}_{k}')for k in range(len(dom[c]))];C.append(xs)
  for x,y in itertools.combinations(xs,2):C.append([-x,-y])
  for k,w in enumerate(dom[c]):
   rr,e,g=trace(w,p,h);assert(e,g)==trace(c,p,h)[1:]
   for i,(q,hh,t)in enumerate(rr):groups[q[0]-q[1],q[0]%2][q[0]//2,j,i,t].append(xs[k])
 if nontrivial:C.append([-var(f'x{j}_0')for j in range(104)])
 for a,(orbit,events)in enumerate(sorted(groups.items())):
  if only is not None and orbit not in only:continue
  prev=true if orbit in input_black else-true
  for b,(event,xs)in enumerate(sorted(events.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}')
   for x in xs:C.append([-x,active])
   C.append(xs+[-active]);C.append([-active,prev if event[3]=='L'else-prev])
   C.extend([[prev,active,-nxt],[-prev,-active,-nxt],[prev,-active,nxt],[-prev,active,nxt]])
   prev=nxt
 return names,C,groups

def run(name,word,start,input_black,only=None):
 names,C,groups=cnf(word,start,input_black,only=only);text=f'p cnf {len(names)} {len(C)}\n'+''.join(' '.join(map(str,c))+' 0\n'for c in C)
 a=OUT/(name+'.cnf');b=OUT/(name+'.rup');a.write_text(text);st=time.monotonic()
 r=subprocess.run([str(HERE/'prove_cnf_rup'),str(a),str(b),'100000'],capture_output=True,text=True,timeout=120)
 z=dict(name=name,variables=len(names),clauses=len(C),producer=r.stdout.strip(),producer_returncode=r.returncode,seconds=time.monotonic()-st,orbits=sorted(groups)if only is None else sorted(only))
 if r.returncode==0:
  k=subprocess.run([str(HERE/'check_drat'),str(a),str(b)],capture_output=True,text=True,timeout=120);assert k.returncode==0,(k.stdout,k.stderr);v=json.loads(k.stdout);assert v['valid']and v['RAT']==0 and v['deletions']==0;z['checker']=v
 z.update(cnf_sha256=hashlib.sha256(a.read_bytes()).hexdigest(),rup_sha256=hashlib.sha256(b.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (OUT/(name+'.json')).write_text(json.dumps(z,indent=2)+'\n');print(z,flush=True)
if __name__=='__main__':
 rev=''.join('L'if c=='R'else'R'for c in H[::-1]);run('reverse_short',(rev),(0,6),wake)
 run('white_short',H,(0,0),set())
