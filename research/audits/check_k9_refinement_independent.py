"""Independent prefix inventory and integer-choice/XOR refinement audit.
No imports of source geometry or source SMT construction.
"""
import itertools,json,ctypes,time,re
from pathlib import Path
from collections import defaultdict,Counter
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'causal_reduction/morphic_candidates'
D=((0,1),(1,0),(0,-1),(-1,0))
def walk(w,h=0,p=(0,0)):
 reads=[];heads=[]
 for c in w:
  reads.append(p);heads.append(h);h=(h+(1 if c=='R' else -1))%4;p=p[0]+D[h][0],p[1]+D[h][1]
 return reads,heads,p,h

def valid(w):
 qs,_,_,_=walk(w);last={}
 for p,c in zip(qs,w):
  if last.get(p)==c:return False
  last[p]=c
 return True
opts={'R':[],'L':[]}
for z in itertools.product('RL',repeat=9):
 w=''.join(z);qs,hs,p,h=walk(w)
 if valid(w):
  for c,target in [('R',((3,0),1)),('L',((-3,0),3))]:
   if (p,h)==target:opts[c].append(w)
assert len(opts['R'])==len(opts['L'])==9
prefixes=[];nodes=0

def dfs(words,text,p,h,last):
 global nodes
 if len(words)==9:prefixes.append(tuple(words));return
 nodes+=1;n=len(words)
 choices=opts[text[n]] if n else opts['R']+opts['L']
 for w in choices:
  if n==0 and w not in opts[w[0]]:continue
  qs,hs,end,eh=walk(w,h,p);new=dict(last)
  for q,c in zip(qs,w):
   if new.get(q)==c:break
   new[q]=c
  else:
   s=text+w;cs,ch,ce,che=walk(s);target=cs[n+1] if n+1<len(cs) else ce;th=ch[n+1] if n+1<len(ch) else che
   assert end==(3*target[0],3*target[1]) and eh==th
   dfs(words+[w],s,end,eh,new)
dfs([],'',(0,0),0,{})
assert nodes==12697 and len(prefixes)==len(set(prefixes))==1280
source=next(z['images'] for z in json.loads((SRC/'free_inflations_k9.json').read_text())['results'] if z['scale']==[3,0]);assert all(set(opts[c])==set(source[c]) for c in opts)
order=source['R']+source['L'];saved={tuple(order[int(i)] for i in line.split(',')) for line in (SRC/'free_nine_coarse81_prefixes.csv').read_text().splitlines()}
assert set(prefixes)==saved
Z=ctypes.CDLL('libz3.so.4');Z.Z3_mk_config.restype=ctypes.c_void_p;Z.Z3_del_config.argtypes=[ctypes.c_void_p];Z.Z3_mk_context.argtypes=[ctypes.c_void_p];Z.Z3_mk_context.restype=ctypes.c_void_p;Z.Z3_del_context.argtypes=[ctypes.c_void_p];Z.Z3_eval_smtlib2_string.argtypes=[ctypes.c_void_p,ctypes.c_char_p];Z.Z3_eval_smtlib2_string.restype=ctypes.c_char_p

def solve(coarse,fixed):
 qs,hs,_,_=walk(coarse);ls=['(set-option :timeout 10000)'];state={};serial=0
 for i,(p,h,c) in enumerate(zip(qs,hs,coarse)):
  words=opts[c];ls.extend([f'(declare-const d{i} Int)',f'(assert (and (<= 0 d{i}) (< d{i} 9)))'])
  if i<len(fixed):ls.append(f'(assert (= d{i} {words.index(fixed[i])}))')
  by=defaultdict(dict)
  for j,w in enumerate(words):
   rr,_,_,_=walk(w,h,(3*p[0],3*p[1]));local=defaultdict(str)
   for q,a in zip(rr,w):local[q]+=a
   for q,s in local.items():
    assert all(a!=b for a,b in zip(s,s[1:]));by[q][j]=s
  for q,changes in sorted(by.items()):
   if q not in state:
    state[q]=f'b{serial}';serial+=1;ls.append(f'(declare-const {state[q]} Bool)')
   old=state[q]
   for j,s in changes.items():ls.append(f'(assert (=> (= d{i} {j}) {old if s[0]=="L" else "(not "+old+")"}))')
   flips=[f'(= d{i} {j})' for j,s in changes.items() if len(s)%2]
   if flips:
    new=f'b{serial}';serial+=1;flip=flips[0] if len(flips)==1 else '(or '+' '.join(flips)+')'
    ls.append(f'(define-fun {new} () Bool (xor {old} {flip}))');state[q]=new
 ls.append('(check-sat)');config=Z.Z3_mk_config();ctx=Z.Z3_mk_context(config);Z.Z3_del_config(config)
 result=Z.Z3_eval_smtlib2_string(ctx,'\n'.join(ls).encode()).decode().strip()
 assert result in ('sat','unsat','unknown'),result
 if result=='sat':
  model=Z.Z3_eval_smtlib2_string(ctx,('(get-value ('+' '.join('d'+str(i) for i in range(len(coarse)))+'))').encode()).decode();values={int(i):int(j) for i,j in re.findall(r'\(d(\d+) (\d+)\)',model)}
  assert len(values)==len(coarse);fine=''.join(opts[c][values[i]] for i,c in enumerate(coarse));assert valid(fine) and fine[:len(coarse)]==coarse
 Z.Z3_del_context(ctx);return result
start=time.time()
for row in prefixes[:12]:assert solve(row[0],row)=='sat'
print('Independent1280 inventory and12 positive controls PASS',flush=True)
counts=Counter();outp=Path(__file__).with_suffix('.jsonl')
with outp.open('w') as f:
 for i,row in enumerate(prefixes):
  status=solve(''.join(row),row);counts[status]+=1;f.write(json.dumps({'index':i,'choices':row,'status':status})+'\n');f.flush()
  if i%50==0 or status!='unsat':print(i,dict(counts),round(time.time()-start,2),flush=True)
assert counts=={'unsat':1280},counts
out={'status':'independent exhaustive inventory and complete refinement exclusion passed','prefix_nodes':nodes,'coarse81_prefixes':1280,'positive_controls':12,'refinement_counts':dict(counts),'seconds':time.time()-start,'scope':'No729-turn prefix on ANY initial coloring can satisfy p(9n)=3p(n), h(9n)=h(n) through all81 coarse moves. Trusted solver: installed Z3; independent integer-choice/XOR encoding, no shared construction imports.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
