from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
R=Path(__file__).resolve().parents[1];U=R/'causal_reduction/unit_scale';J=json.loads((U/'forward108_domino_repair.json').read_text());H,LR,Q=J['words'];assert H==json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word']and LR=='LR'
reverse=lambda w:''.join('R'if c=='L'else'L'for c in w[::-1]);V=reverse(H);assert V[31]=='L'and Q==reverse(V[:31]+'LRRRR'+V[32:])
def trace(w,p=0j,h=1):
 out=[]
 for c in w:
  out.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 return out,p,h
def orbit(p):return(int(p.real-p.imag),int(p.real)%2)
def slots(w,p,h):
 d=defaultdict(list)
 for i,(q,hh,c)in enumerate(trace(w,p,h)[0]):d[orbit(q)].append((int(q.real)//2,i,c))
 return d
hs=slots(H,10j,1);qs=slots(Q,0j,1);rs=slots(LR,-1+6j,2)
assert set(hs)&(set(qs)|set(rs))=={(-8,1),(-7,0),(-7,1)}
actual={a:[sorted(v[0]for v in d.get(a,[]))for d in(hs,qs,rs)]for a in set(hs)&(set(qs)|set(rs))}
assert actual=={(-8,1):[[1,1,1],[0],[]],(-7,0):[[2],[0,1],[]],(-7,1):[[1],[0,0],[-1]]}
for a,es in hs.items():
 hist=[c for q,i,c in sorted(es,key=lambda t:(-t[0],t[1]))];assert hist==['RL'[i%2]for i in range(len(hist))]
# These exact extra-field sets are k<=-1, k=0, k<=t-2. Future minima l+2,l+3,l+2 differ by l+3,l+3,l-t+4>=2.
rr,end,h=trace(H);known={p:c=='R'for p,hh,c in rr};p=end;forced='';moves=[]
while p in known:
 c='L'if known[p]else'R';forced+=c;known[p]=not known[p];h=(h+(1 if c=='R'else-1))%4;moves.append(h);p+=(1j,1,-1j,-1)[h]
assert forced=='LRLLRRRRLLRLL'and(p-end,h)==(2+1j,0)and p not in{q for q,hh,c in rr}
assert Counter(moves)=={0:4,1:4,2:3,3:2}
controls=[]
for l,t in[(-1,1),(0,1),(0,2),(3,1),(3,5),(50,1),(50,52),(999,1001)]:
 def field(p):
  a=orbit(p);k=int(p.real)//2
  return(sum(k<=l+q for q,i,c in hs.get(a,[]))+sum(k<q for q,i,c in qs.get(a,[]))+sum(k<t+q for q,i,c in rs.get(a,[])))%2
 p=(2*l+2)+(2*l+12)*1j;h=1;flips=set()
 for c in H*23:
  assert bool(field(p)^(p in flips))==(c=='L');flips.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 controls.append((l,t,23*104))
# Future H positions lie at or above its starting y, whereas every connector target here is at least two rows below.
assert min(p.imag for p,h,c in trace(H)[0])>=0
O=json.loads((U/'pipeline_cut_continuation_exact.json').read_text());assert O['forced_prefix']==forced
out=dict(status='PASS independent infinite-cut orbit comparison and maximal forced endpoint prefix',note_sha256=hashlib.sha256((U/'pipeline_cut_continuation_theorem.md').read_bytes()).hexdigest(),overlap_inventory={str(k):v for k,v in actual.items()},forced_prefix=forced,forced_move_counts=dict(Counter(moves)),controls=controls,scope='Exact disconnected H-end semi-infinite field follows H forever for l>=-1,1<=t<=l+2. Last-read information alone forces13 turns and connector length>=27-4u. Does not include alterations by earlier genuine connectors or exclude general assembly; no finite-seed counterexample/capture claim.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
