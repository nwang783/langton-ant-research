"""Independent literal check of the DCV five-cell-core replacement model."""
import itertools,json,hashlib,pathlib
P=pathlib.Path('/workspace/shared/langton')
W={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'}
M='LLLLRLRRRRL'; D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p
 for _ in range(h):x,y=y,-x
 return x,y
def trace(w):
 x=y=h=0; first={};last={};odd=set();reads=[]
 for i,c in enumerate(w):
  q=(x,y)
  if last.get(q)==c:return None
  first.setdefault(q,(c,i));last[q]=c;odd.symmetric_difference_update({q});reads.append((q,c))
  h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 return (x,y,h),first,last,odd,reads
K={q for q,(c,i) in trace(M)[1].items() if c=='L'}
assert K=={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def geom(s):
 w=''.join(W[c] for c in s);r=trace(w);a=trace(w+M)
 assert r and a
 (x,y,h),_,last,odd,reads=r
 newK={(x+rot(q,h)[0],y+rot(q,h)[1]) for q in K}
 seed={q for q,(c,i) in a[1].items() if c=='L'}
 assert K<=seed and newK<=seed^odd
 ins=seed-K;outs=(seed^odd)-newK
 assert not ins&outs and all(last.get(q)=='R' for q in outs)
 white={q for q,(c,i) in a[1].items() if c=='R'}
 # The transformation is exact for arbitrary extra black cells avoiding all guards.
 touched=set(a[1]);assert (K^newK^odd)==(ins|outs)
 assert (ins|outs)<=touched
 return r,ins,outs,white
rules={c:geom(c) for c in W}
res=json.loads((P/'word_stabilization/dcv_residual_core_resources.json').read_text())
assert {tuple(q) for q in res['core']}==K
for row in res['geometry']:
 r,ins,outs,white=geom(row['name'])
 assert tuple(row['endpoint'])==r[0]
 for key,val in [('inputs',ins),('outputs',outs),('forced_white',white)]:assert {tuple(q) for q in row[key]}==val,(row['name'],key)
 first=trace(''.join(W[c] for c in row['name'])+M)[1]
 assert row['input_first_phases']==[first[tuple(q)][1] for q in row['inputs']]
# Exact macro-by-macro replay, independent of packet grouping.
valid=0;bylen={};examples=[]
for n in range(1,10):
 count=0
 for tup in itertools.product('DCV',repeat=n):
  s=''.join(tup);t=trace(''.join(W[c] for c in s)+M)
  if not t:continue
  seed={q for q,(c,i) in t[1].items() if c=='L'};assert K<=seed
  board=set(seed);E={q:None for q in seed-K};x=y=h=0;charged=0
  for index,c in enumerate(s):
   r,ins,outs,white=rules[c]
   def at(q):
    a,b=rot(q,h);return x+a,y+b
   ii={at(q) for q in ins};oo={at(q) for q in outs};ww={at(q) for q in white}
   assert ii<=E.keys() and not oo&E.keys() and not ww&board
   charged+=sum(E[q] is None for q in ii)
   for q in ii:del E[q]
   for q in oo:E[q]=index
   # Replay every actual RAW read, not merely its parity mask.
   for q,turn in r[4]:
    a=at(q);assert (a in board)==(turn=='L');board.symmetric_difference_update({a})
   dx,dy=rot(r[0][:2],h);x+=dx;y+=dy;h=(h+r[0][2])%4
   nk={at(q) for q in K};assert nk<=board and set(E)==board-nk
  assert charged==len(seed)-5 and all(v is not None for v in E.values())
  count+=1
  if s in ['DCCCV','DDCDCDCDV','DCVCCVV','DVCCVCDDCD']:examples.append([s,len(seed),charged])
 bylen[n]=count;valid+=count
out={'status':'PASS','core':sorted(K),'macro_rules':{c:{'input':sorted(g[1]),'output':sorted(g[2]),'endpoint':g[0][0]} for c,g in rules.items()},'resource_rows':len(res['geometry']),'valid_marked_factors_through_length9':valid,'counts_by_length':bylen,'controls':examples,'source_sha256':hashlib.sha256((P/'word_stabilization/dcv_residual_core_resources.json').read_bytes()).hexdigest()}
(P/'audits/check_dcv_residual_model_independent.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
