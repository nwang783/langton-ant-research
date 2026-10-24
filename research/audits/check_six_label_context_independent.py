"""Independent context-pair certificate verification; no discovery imports."""
import json,hashlib
from pathlib import Path
from collections import Counter,defaultdict
R=Path(__file__).resolve().parents[1];P=R/'word_stabilization';stem='direct_six_labels_packets_context2_'
manifest=json.loads((P/'six_label_union_manifest.json').read_text());assert all(hashlib.sha256((P/f).read_bytes()).hexdigest()==h for f,h in manifest.items())
M='LLLLRLRRRRLR'
C='LLLLRLRRRRLRRRR';V='LLLLRLRRRRLRRLRRRR';U='LLLLRLRRRRLRLLLLRRRRLRRLRRRR';Q='LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRRLRRRR';B='LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR'
X='LLLLRLRRRRLRLLLLRRRRLRRRRLRRRR';base=[C,V,V+'LRRRR',U,X,U+'LRRRR',Q,B];start=[M]*8;finish=[M]*8
old=json.loads((P/'direct_six_labels_packets_port_quotient.json').read_text());edges=list(map(tuple,old['quotient_edges']));assert old['classes']==65 and len(edges)==239
assert [(z['word'],z['start_marker'],z['end_marker']) for z in old['macro_words']]==list(zip(base,start,finish))
paths={n:set() for n in range(1,5)}
def grow(v,s):
 if s:paths[len(s)].add(tuple(s))
 if len(s)==4:return
 for u,a,w in edges:
  if u==v:grow(w,s+[a])
for v in range(65):grow(v,[])
contexts=sorted(paths[2]);assert len(contexts)==32
ctxidx={v:i for i,v in enumerate(contexts)};A=range(32);words={i:base[a] for i,(a,b) in enumerate(contexts)};EM={i:base[b]+finish[b] for i,(a,b) in enumerate(contexts)}
rawG={(ctxidx[(a,b)],ctxidx[(b,c)]) for a,b,c in paths[3]}
rawT={(ctxidx[(a,b)],ctxidx[(b,c)],ctxidx[(c,d)]) for a,b,c,d in paths[4]}
rows=json.loads((P/(stem+'port_quotient.json')).read_text())['macro_words']
assert [(r['word'],r['end_marker'],r['context']) for r in rows]==[(words[i],EM[i],list(contexts[i])) for i in A]
D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p
 for _ in range(h%4):x,y=y,-x
 return x,y
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def tr(w):
 p=(0,0);h=0;first={};last={};vis=[];ok=True
 for i,c in enumerate(w):
  if last.get(p)==c:ok=False
  first.setdefault(p,(c,i));last[p]=c;vis.append((p,c));h=(h+(1 if c=='R' else -1))%4;p=add(p,D[h])
 return dict(first=first,last=last,end=(p,h),vis=vis,ok=ok)
raw={a:tr(words[a]) for a in A};tar={a:tr(words[a]+EM[a]) for a in A}
assert all(z['ok'] for z in list(raw.values())+list(tar.values()))
for i,(a,b) in enumerate(contexts):assert (words[i]+EM[i]).startswith(start[a]) and finish[a]==start[b]
def feasible(seq):return tr(''.join(words[a] for a in seq)+EM[seq[-1]])['ok']
G={s for s in rawG if feasible(s)};T={s for s in rawT if feasible(s)}
T_over={(a,b,d) for a,b in G for c,d in G if b==c and feasible((a,b,d))};assert T<=T_over;T=T_over
j=json.loads((P/(stem+'grammar.json')).read_text());assert G==set(map(tuple,j['pairs'])) and T==set(map(tuple,j['triples']))
# Check exported geometry, especially RAW endpoints and actual two-word targets.
tokens=iter(map(int,(P/(stem+'kernel.input')).read_text().split()));assert next(tokens)==32
for a in A:
 assert (next(tokens),next(tokens),next(tokens))==(*raw[a]['end'][0],raw[a]['end'][1]);n=next(tokens);last={(next(tokens),next(tokens)):'L' if next(tokens) else 'R' for _ in range(n)};assert last==raw[a]['last']
 n=next(tokens);first={}
 for _ in range(n):
  p=(next(tokens),next(tokens));c='L' if next(tokens) else 'R';phase=next(tokens);first[p]=(c,phase)
 assert first==tar[a]['first']
n=next(tokens);assert {(next(tokens),next(tokens)) for _ in range(n)}==G
n=next(tokens);assert {(next(tokens),next(tokens),next(tokens)) for _ in range(n)}==T
assert list(tokens)==[]
def aligned(p,h):return (sum(p)-h)%2==0
def end(a,p=(0,0),h=0):return add(p,rot(raw[a]['end'][0],h)),(h+raw[a]['end'][1])%4
def norm(a,p,h,b,q,k):return a,b,*rot(sub(q,p),-h),(k-h)%4
cand=set()
for a in A:
 for b in A:
  for h in range(4):
   for q in raw[a]['first']:
    for z in tar[b]['first']:
     p=sub(q,rot(z,h))
     if aligned(p,h):cand.add((a,b,*p,h))
short=set()
for a,b in G:
 p,h=end(a);short.add((a,b,*p,h))
for a,c,b in T:
 p,h=end(a);q,k=end(c,p,h);short.add((a,b,*q,k))
cert=[tuple(map(int,s.split())) for s in (P/(stem+'kernel.tsv')).read_text().splitlines()];S={r[:5]:r[5:] for r in cert}
assert len(S)==len(cert)==213558 and len(cand)==230460 and len(short&cand)==184
assert set(S)<=cand and not(set(S)&short)
outs={a:{b for aa,b in G if aa==a} for a in A};ins={b:{a for a,bb in G if bb==b} for b in A}
reader_cache={};counts=Counter();neighbor_options=reader_options=0
for key,proof in S.items():
 a,b,x,y,h=key;p=(x,y);kind,qx,qy=proof
 if kind==1:
  pc,hc=end(a)
  for c in outs[a]:
   for d in ins[b]:
    hd=(h-raw[d]['end'][1])%4;pd=sub(p,rot(raw[d]['end'][0],hd));neighbor_options+=1
    assert (a,d,*pd,hd) in S or norm(c,pc,hc,b,p,h) in S or norm(c,pc,hc,d,pd,hd) in S,key
 elif kind==2:
  q=qx,qy;local=rot(sub(q,p),-h);assert raw[a]['last'][q]==tar[b]['first'][local][0]
  if q not in reader_cache:
   readers=set()
   for c in A:
    for hc in range(4):
     for z in raw[c]['first']:
      pc=sub(q,rot(z,hc))
      if aligned(pc,hc):readers.add((c,pc,hc))
   reader_cache[q]=readers
  for c,pc,hc in reader_cache[q]:
   reader_options+=1;assert (a,c,*pc,hc) in S or norm(c,pc,hc,b,p,h) in S,key
 else:raise AssertionError(proof)
 counts[kind]+=1

overlaps=0;marks={}
for b,(label,succ) in enumerate(contexts):
 if label==0 and succ!=0:continue
 marker,phase=((-1,0),1) if label in {0,4,6,7} else ((1,2),13) if label in {1,2} else ((0,3),23)
 assert raw[b]['first'][marker]==('L',phase);marks[b]=[list(marker),phase]
 for a in A:
  for h in range(4):
   for oldcell in raw[a]['first']:
    p=sub(oldcell,rot(marker,h))
    if aligned(p,h):assert (a,b,*p,h) in S;overlaps+=1
assert all(a in marks or b in marks for a,b in G)
assert max(len(words[a]) for a in marks)==74
assert max(len(words[a]) for a in A if a not in marks)==15
assert {b for a,b in paths[2] if a==0}<={0,1,2}
out={'status':'independent six-label eight-packet context certificate verified','context_count':32,'actual_quotient_states':65,'actual_quotient_edges':239,'candidate_types':len(cand),'short_types':len(short&cand),'forbidden_types':len(S),'clause_counts':dict(counts),'neighbor_options':neighbor_options,'reader_options':reader_options,'raw_marker_contexts':marks,'marker_overlap_types':overlaps,'uncharged_contexts':[contexts[a] for a in A if a not in marks],'fuel_bound':'At most 2m+1 counted raw blocks and 89m+15 raw turns, with one full actual successor and its endpoint marker beyond each counted target.','scope':'Standalone 65-state eight-packet quotient with actual successor context. Global marker coverage and forced packet contraction require separate audit. NOT arbitrary raw-five factors.','certificate_sha256':hashlib.sha256((P/(stem+'kernel.tsv')).read_bytes()).hexdigest(),'quotient_sha256':hashlib.sha256((P/'direct_six_labels_packets_port_quotient.json').read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
