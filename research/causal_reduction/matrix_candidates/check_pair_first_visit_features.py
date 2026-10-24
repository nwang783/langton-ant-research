"""Finite functional graph necessary conditions, not a trajectory existence test."""
import json,itertools,pathlib,time
P=pathlib.Path(__file__).parent;D=((0,1),(1,0),(0,-1),(-1,0));L=(0,3,2,3)
def qid(h,d):return 2*h+int((d-h)%4==3)
dom=json.loads((P/'mixed_k13_3_2_2_7_inventory.json').read_text())['domains'];features=[]
for h in range(4):
 for c in (1,3):
  z=(h+c)%4;data={}
  for w in dom[z]:
   if w[-1]!=L[z]:continue
   end=tuple(sum(D[d][a] for d in w) for a in range(2));x=y=0;j=None;r=0
   for i,d in enumerate(w):
    if (x,y)==end:r+=1
    x+=D[d][0];y+=D[d][1]
    if (x,y)==end and j is None:j=i+1
   assert j>=2
   H=w[j-1];sig=((w[-1]-H)%4+2*r)%4 # 0 or2 sign rotation
   data.setdefault((w[0],w[j-2],H,sig),''.join(map(str,w)))
  features.append(data)
triples=[(w,u,v) for u in range(4) for w in range(4) if (w-u)%2 for v in range(4) if (v-u)%2];idx={q:i for i,q in enumerate(triples)};isR=[(v-u)%4==1 for w,u,v in triples]

def record_ok(safe,u):
 v=(u+1)%4;z=(u+2)%4
 return idx[u,v,z] in safe and any(idx[w,u,v] in safe for w in range(4) if(w-u)%2)
st=time.monotonic();count=passed=0;hist={};examples=[]
for ff in itertools.product(*(list(f) for f in features)):
 if ff[0][0]!=1:continue # fixed white horizontal root
 count+=1;T=[]
 for w,u,v in triples:
  F,M,H,sig=ff[qid(w,u)];out=(ff[qid(u,v)][0]+sig)%4;T.append(idx[M,H,out])
 safe=set(i for i in range(16) if isR[i]);change=True
 while change:
  nxt={i for i in safe if T[i] in safe};change=nxt!=safe;safe=nxt
 key=tuple(u for u in range(4) if record_ok(safe,u));hist[str(key)]=hist.get(str(key),0)+1
 ok=any(u in key for u in (0,2)) and any(u in key for u in (1,3))
 if ok:
  passed+=1
  if len(examples)<3:examples.append(dict(features=ff,images=[features[q][ff[q]] for q in range(8)],safe=[triples[i] for i in sorted(safe)],record_directions=key))
r=dict(matrix=[[3,2],[2,7]],k=13,last_map=L,feature_domain_sizes=list(map(len,features)),fixed_white_horizontal_root=True,feature_assignments=count,record_filter_survivors=passed,record_direction_histogram=hist,examples=examples,status='NECESSARY FILTER ONLY',seconds=time.monotonic()-st)
(P/'pair_first_visit_features.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='examples'}))
