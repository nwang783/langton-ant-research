"""Independent SMT-expression evaluation and physical replay of compact positives."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import re,json,hashlib
ROOT=Path('/workspace/shared/langton');P=ROOT/'periodic_classification_new'
def sexprs(text):
 ts=re.findall(r'\(|\)|[^\s()]+',text);i=0
 def one():
  nonlocal i
  t=ts[i];i+=1
  if t!='(':return t
  a=[]
  while ts[i]!=')':a.append(one())
  i+=1;return a
 out=[]
 while i<len(ts):out.append(one())
 return out

def ev(x,env):
 if isinstance(x,str):
  if x=='true':return True
  if x=='false':return False
  if x in env:return env[x]
  return Fraction(x)
 op,*args=x
 if op=='ite':return ev(args[1]if ev(args[0],env)else args[2],env)
 if op=='=>':return not ev(args[0],env)or ev(args[1],env)
 a=[ev(t,env)for t in args]
 if op=='+':return sum(a)
 if op=='-':return -a[0]if len(a)==1 else a[0]-a[1]
 if op=='*':
  z=1
  for t in a:z*=t
  return z
 if op=='/':return a[0]/a[1]
 if op=='mod':return a[0]%a[1]
 if op=='and':return all(a)
 if op=='or':return any(a)
 if op=='not':return not a[0]
 if op=='=':return all(t==a[0]for t in a[1:])
 if op=='<=':return all(x<=y for x,y in zip(a,a[1:]))
 if op=='>=':return all(x>=y for x,y in zip(a,a[1:]))
 if op=='<':return all(x<y for x,y in zip(a,a[1:]))
 if op=='>':return all(x>y for x,y in zip(a,a[1:]))
 raise ValueError(op)
D=[1j,1,-1j,-1];records=[]
for copies in (1,2,3):
 prefix=P/f'compact_clock_standard{104*copies}';env={}
 for line in prefix.with_suffix('.model').read_text().splitlines():
  name,sep,value=line.partition(' -> ')
  if sep:env[name]=ev(sexprs(value)[0],{})
 assertions=0
 for expr in sexprs(prefix.with_suffix('.smt2').read_text()):
  if expr[0]=='define-fun':assert expr[2]==[];env[expr[1]]=ev(expr[4],env)
  if expr[0]=='assert':assert ev(expr[1],env),expr;assertions+=1
 width=2*copies;H=12;poses=[complex(x,x+y)for y in range(H)for x in range(width)];ix={p:i for i,p in enumerate(poses)};events={};outgoing=defaultdict(list);incoming=defaultdict(list)
 for i,p in enumerate(poses):
  n=int(env[f'n{i}']);axis=1-int(p.real+p.imag)%2
  for j in range(n):
   h=axis+2*int(env[f'b{i}_{j}']);turn=1 if j%2==0 else-1;o=(h+turn)%4;t=env[f't{i}_{j}'];assert t.denominator==1
   events[i,j]=(h,o,int(t));outgoing[i,o].append((i,j));incoming[i,h].append((i,j))
 total=int(env['P']);assert total==len(events)==104*copies;succ={}
 for (i,h),ss in outgoing.items():
  z=poses[i]+D[h];k=int(z.real)//width;q=complex(int(z.real)%width,z.imag-k*width);ii=ix[q];tt=incoming[ii,h];assert len(ss)==len(tt)
  for s,t in zip(ss,tt):
   assert events[t][2]-k*total==events[s][2]+1
   succ[s]=(t,-k)
 assert len(succ)==total
 start=min(events);cur=start;seen=[];vol=0;word=[];z=poses[start[0]];h=events[start][0];seenpos=[]
 while cur not in seen:
  seen.append(cur);hh,o,_=events[cur];assert h==hh;word.append('R'if cur[1]%2==0 else'L');seenpos.append(z);h=o;z+=D[h];cur,v=succ[cur];vol+=v
 assert cur==start and len(seen)==total and vol==1 and z==poses[start[0]]-width-width*1j
 # Derive a finite seed from100 complete cycles, then replay200 cycles without
 # inventing any extra initial cells. This is a positive implementation control.
 def requirements(cycles):
  z=poses[start[0]];h=events[start][0];last={};seed=set()
  for c in word*cycles:
   if z in last:assert last[z]!=c
   elif c=='L':seed.add(z)
   last[z]=c;h=(h+(1 if c=='R'else-1))%4;z+=D[h]
  return seed
 seed=requirements(100);assert requirements(200)==seed
 board=set(seed);z=poses[start[0]];h=events[start][0]
 for c in word*200:
  assert(z in board)==(c=='L')
  if z in board:board.remove(z)
  else:board.add(z)
  h=(h+(1 if c=='R'else-1))%4;z+=D[h]
 records.append({'period':total,'drift':[-width,-width],'SMT_assertions_checked':assertions,'events':len(events),'seed_mass':len(seed),'literal_steps':total*200})
res={'status':'PASS independent compact positive models and literal replay','controls':records,'scope':'Positive implementation controls plus analytic encoding review. No independently checked finite-strip UNSAT proof or unrestricted exclusion.','source_sha256':hashlib.sha256((P/'synthesize_axis_compact_clock.py').read_bytes()).hexdigest()}
(ROOT/'audits/compact_clock_independent.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
