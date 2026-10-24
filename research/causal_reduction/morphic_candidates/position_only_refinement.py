"""Exact refinement for pure POSITION inflation, with free boundary headings.
All initial cell colors are unconstrained. SAT models are literally replayed.
"""
import collections,itertools,json,pathlib,re,time,sys
from search_position_only_inflations import D,mul,rotate,trace,seed
from smt_inflation_refinement import Z3
HERE=pathlib.Path(__file__).resolve().parent

def build(k,a,coarse,fixed):
 names=[];clauses=[];cells=collections.defaultdict(dict)
 def var(name):names.append(name);return len(names)
 allwords=[]
 for letters in itertools.product('RL',repeat=k):
  w=''.join(letters)
  if seed(w) is not None:allwords.append((w,trace(w)))
 options=[];cv=[];N=len(coarse)
 hv=[var(f'h{i}') for i in range(N+1)];clauses.append([-hv[0]])
 fixed_head=0
 for i,(x,y,h,c) in enumerate(trace(coarse)[0]):
  move=D[(h+(1 if c=='R' else -1))%4];target=mul(a,move);entries=[]
  for H in ((k*i)%2,(k*i)%2+2):
   for w,(reads,end) in allwords:
    if rotate(end[0],end[1],H)!=target:continue
    entries.append(dict(word=w,heading=H,end_heading=(H+end[2])%4,reads=reads))
  assert entries
  options.append(entries);vs=[var(f'c{i}_{j}') for j in range(len(entries))];cv.append(vs);clauses.append(vs[:])
  for j,v in enumerate(vs):
   for u in vs[:j]:clauses.append([-u,-v])
   option=entries[j];H=option['heading'];E=option['end_heading']
   clauses.append([-v,hv[i] if H>=2 else -hv[i]])
   clauses.append([-v,hv[i+1] if E>=2 else -hv[i+1]])
   by=collections.defaultdict(str);ox,oy=mul(a,(x,y))
   for X,Y,hh,z in option['reads']:
    X,Y=rotate(X,Y,H);by[ox+X,oy+Y]+=z
   for p,s in by.items():cells[p].setdefault(i,['']*len(entries))[j]=s
  if i<len(fixed):
   matches=[j for j,z in enumerate(entries) if z['heading']==fixed_head and z['word']==fixed[i]]
   assert len(matches)==1
   clauses.append([vs[matches[0]]]);fixed_head=entries[matches[0]]['end_heading']
 for cell,(p,vv) in enumerate(sorted(cells.items())):
  events=sorted(vv.items());bv=[var(f'b{cell}_{j}') for j in range(len(events)+1)]
  for j,(i,ss) in enumerate(events):
   before,after=bv[j:j+2]
   for u,s in enumerate(ss):
    v=cv[i][u]
    if s:
     assert all(x!=y for x,y in zip(s,s[1:]));b=s[0]=='L';e=b^(len(s)%2==1)
     clauses.append([-v,before if b else -before]);clauses.append([-v,after if e else -after])
    else:
     clauses.append([-v,-before,after]);clauses.append([-v,before,-after])
 return names,clauses,options,cv

def solve(k,a,coarse,fixed,timeout=30000):
 start=time.time();names,clauses,options,cv=build(k,a,coarse,fixed)
 def literal(x):return f'v{x}' if x>0 else f'(not v{-x})'
 lines=[f'(set-option :timeout {timeout})']+[f'(declare-const v{i} Bool)' for i in range(1,len(names)+1)]
 lines+=['(assert '+(literal(c[0]) if len(c)==1 else '(or '+' '.join(map(literal,c))+')')+')' for c in clauses]
 Z=Z3();status=Z.run('\n'.join(lines)+'\n(check-sat)').strip()
 out=dict(k=k,scale=a,status=status,variables=len(names),clauses=len(clauses),seconds=time.time()-start)
 if status=='sat':
  text=Z.run('(get-value ('+' '.join(f'v{v}' for row in cv for v in row)+'))')
  true={int(v) for v in re.findall(r'\(v(\d+) true\)',text)}
  chosen=[]
  for entries,row in zip(options,cv):
   ids=[j for j,v in enumerate(row) if v in true];assert len(ids)==1;chosen.append(entries[ids[0]])
  word=''.join(z['word'] for z in chosen);black=seed(word);assert black is not None and word[:len(coarse)]==coarse
  fine=[(x,y,h) for x,y,h,c in trace(word)[0]]+[trace(word)[1]]
  old=[(x,y,h) for x,y,h,c in trace(coarse)[0]]+[trace(coarse)[1]]
  for n,p in enumerate(old):assert fine[k*n][:2]==mul(a,p[:2])
  out.update(choices=[z['word'] for z in chosen],entry_headings=[z['heading'] for z in chosen],word=word,seed=black,seed_size=len(black))
 elif status!='unsat':out['reason']=Z.run('(get-info :reason-unknown)')
 Z.close();return out
if __name__=='__main__':
 k=int(sys.argv[1]);a=tuple(map(int,sys.argv[2].split(',')));index=int(sys.argv[3]) if len(sys.argv)>3 else 0
 source=json.load(open(HERE/f'position_only_prefixes_k{k}_a{a[0]}_{a[1]}.json'))['prefixes'][index]
 result=solve(k,a,source['word'],source['choices']);(HERE/f'position_only_refinement_k{k}_{index}.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({key:value for key,value in result.items() if key not in ('word','choices','entry_headings','seed')},indent=2))
