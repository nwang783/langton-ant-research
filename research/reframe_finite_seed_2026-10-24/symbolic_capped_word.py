"""Exact finite Boolean/CNF reduction for an empty-to-empty capped ant word.
No SAT solver is used here. A satisfying model must pass literal complete-board
replay; unsatisfiability requires a separately checkable solver certificate.
"""
from pathlib import Path
from active_flight import DIR,rot,cursor,step,comp
import json
NEIGH=((1,0),(-1,0),(0,1),(0,-1))
def vphysical(v):return(1+2*(v[0]+v[1]),-1+2*(v[0]-v[1]))
def vgraph(v):
 x,y=v[0]-1,v[1]+1;assert(x+y)%4==0 and(x-y)%4==0
 return((x+y)//4,(x-y)//4)
def cell(u,v):
 a,b=vphysical(u),vphysical(v);assert(a[0]+b[0])%4==0 and(a[1]+b[1])%4==0
 return((a[0]+b[0])//4,(a[1]+b[1])//4)
def adjacent(v):return[(v[0]+a,v[1]+b)for a,b in NEIGH]

class Circuit:
 def __init__(self):
  self.n=1;self.clauses=[(1,)];self.gates=[];self.cache={};self.inputs={}
 def bit(self,q):
  if q not in self.inputs:self.n+=1;self.inputs[q]=self.n
  return self.inputs[q]
 def gate(self,op,ls):
  s=set(ls)
  if op=='and':
   if -1 in s or any(-x in s for x in s):return-1
   s.discard(1)
   if not s:return 1
  else:
   if 1 in s or any(-x in s for x in s):return 1
   s.discard(-1)
   if not s:return-1
  if len(s)==1:return next(iter(s))
  ls=tuple(sorted(s));key=(op,ls)
  if key in self.cache:return self.cache[key]
  self.n+=1;z=self.n;self.cache[key]=z;self.gates.append((z,op,ls))
  if op=='and':self.clauses.extend([(-z,x)for x in ls]);self.clauses.append((z,)+tuple(-x for x in ls))
  else:self.clauses.extend([(z,-x)for x in ls]);self.clauses.append((-z,)+ls)
  return z
 def AND(self,*ls):return self.gate('and',ls)
 def OR(self,*ls):return self.gate('or',ls)
 def require(self,x):self.clauses.append((x,))
 def atmost(self,ls,m):
  ls=[x for x in ls if x!=-1];m-=ls.count(1);ls=[x for x in ls if x!=1]
  if m<0:self.require(-1);return
  if len(ls)<=m:return
  a=[1]+[-1]*(m+1)
  for x in ls:a=[1]+[self.OR(a[j],self.AND(a[j-1],x))for j in range(1,m+2)]
  self.require(-a[m+1])
 def assignment(self,B):
  val={1:True};val.update({i:q in B for q,i in self.inputs.items()})
  def ev(x):return val[abs(x)]if x>0 else not val[abs(x)]
  for z,op,ls in self.gates:val[z]=all(ev(x)for x in ls)if op=='and'else any(ev(x)for x in ls)
  return val
 def check(self,val):
  return all(any(val[abs(x)]if x>0 else not val[abs(x)]for x in c)for c in self.clauses)
 def write_dimacs(self,path):
  with open(path,'w')as f:
   f.write(f'p cnf {self.n} {len(self.clauses)}\n')
   for c in self.clauses:f.write(' '.join(map(str,c))+' 0\n')

def build(word,M):
 assert M>=0 and word and set(word)<={'R','L'}
 C=Circuit();parity=set();p=(0,0);h=0;cuts=[]
 def b(q):
  x=C.bit(q);return-x if q in parity else x
 for t in range(len(word)+1):
  root=vgraph(cursor(p,h));ports=[cell(root,v)for v in adjacent(root)]
  if t in(0,len(word)):
   for q in ports:C.require(-b(q))
  else:
   C.require(C.OR(*(b(q)for q in ports)))
   V={(root[0]+x,root[1]+y)for x in range(-M,M+1)for y in range(-M,M+1)if abs(x)+abs(y)<=M}
   E={tuple(sorted((u,v)))for u in V for v in adjacent(u)}
   reach={v:(1 if v==root else-1)for v in sorted(V)}
   for d in range(M):
    reach={v:C.OR(reach[v],*(C.AND(reach[u],b(cell(u,v)))for u in adjacent(v)if u in V))for v in sorted(V)}
   active=[C.AND(b(cell(u,v)),C.OR(reach.get(u,-1),reach.get(v,-1)))for u,v in sorted(E)]
   C.atmost(active,M)
  cuts.append({'time':t,'pose':[p,h],'w_root':root,'read_parity':sorted(parity)})
  if t<len(word):
   c=word[t];C.require(b(p)if c=='L'else-b(p))
   if p in parity:parity.remove(p)
   else:parity.add(p)
   h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 C.word=word;C.M=M;C.cuts=cuts
 return C

def actual_property(seed,word,M):
 B=set(seed);p=(0,0);h=0;trace=[]
 for t in range(len(word)+1):
  A=comp(B,1,cursor(p,h));trace.append({'time':t,'pose':[p,h],'active_mass':len(A),'field':sorted(B)})
  if len(A)>M or(t in(0,len(word))and A)or(0<t<len(word)and not A):return False,trace
  if t<len(word):
   if('L'if p in B else'R')!=word[t]:return False,trace
   p,h=step(B,p,h)
 return True,trace

def verify_model(C,val):
 assert C.check(val),'CNF assignment not satisfying'
 seed={q for q,z in C.inputs.items()if val[z]};ok,trace=actual_property(seed,C.word,C.M)
 assert ok,'Model failed complete-board replay'
 return {'finite_seed':sorted(seed),'trace':trace}

if __name__=='__main__':
 import sys
 word=sys.argv[1]if len(sys.argv)>1 else'RRRRLRLRLRL';M=int(sys.argv[2])if len(sys.argv)>2 else 7
 c=build(word,M);path=Path(__file__).parent/'symbolic_capped_word.cnf';c.write_dimacs(path)
 out={'word':word,'cap':M,'variables':c.n,'initial_board_bits':len(c.inputs),'gate_count':len(c.gates),'clauses':len(c.clauses),'input_map':[{'cell':q,'variable':z}for q,z in sorted(c.inputs.items())],'cuts':c.cuts,'scope':'Exact fixed-word finite first-return constraint, not a global decision procedure. No solver outcome asserted.'};path.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('input_map','cuts')})
