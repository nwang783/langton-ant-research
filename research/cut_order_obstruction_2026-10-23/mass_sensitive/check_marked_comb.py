#!/usr/bin/env python3
"""Literal finite controls; all-n proof is in the companion note."""
from pathlib import Path
from collections import Counter, defaultdict
import json
ROOT=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0)); O=((0,-1),(-1,-1),(-1,0),(0,0))
W=(ROOT.parents[1]/'word_stabilization/standard_word.txt').read_text().strip()
F={(W*2)[i:i+10] for i in range(104)}
SIX={'RRRLLRLLRLR','LLRLRLLRRLL','RRRRLRLLRLL','RRRLRRRRLRL','RRRLRRRRLRR','LRRLRRRRLRR'}
LABELS={'RLLRRLLRLLR','LLRRLLRLLRR','LRRLLRLLRRL','LLRRLLRLLRL','RRLLRRLLRLL','LRLLRRLLRLL'}
assert all(z[:10]not in F and z[1:]not in F and z not in SIX for z in LABELS)

def build(w):
 p=(0,0);h=0;last={};seed=set();reads=[];poses=[]
 for t,a in enumerate(w):
  if p in last:assert a!=last[p]
  elif a=='L':seed.add(p)
  last[p]=a;reads.append(p);poses.append((p,h))
  h=(h+(1 if a=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 roots={q:-(i+1)for i,q in enumerate(sorted(seed))};owner=dict(roots)
 par={0:None};ch=defaultdict(list);start={0:0};r=Counter();marks=Counter();born={q:None for q in seed};ages={};i=0
 for t,(q,a) in enumerate(zip(reads,w)):
  if t>=10 and w[t-10:t]not in F and w[t-9:t+1]not in F and w[t-10:t+1]not in SIX:marks[i]+=1
  if a=='R':
   assert q not in owner;owner[q]=i;born[q]=t;r[i]+=1
  else:
   assert q in owner
   if born[q] is not None:ages[q]=(born[q],t,t-born[q])
   parent=owner.pop(q);born.pop(q);i+=1;par[i]=parent;ch[parent].append(i);start[i]=t+1
 return locals()

def skeleton(par,ch,marks,select=None):
 selected=set(marks) if select is None else set(marks)&set(select)
 active=set(selected)
 for a in list(selected):
  while a is not None:active.add(a);a=par.get(a)
 cc={a:[b for b in ch[a]if b in active]for a in active}
 rr=sum(par.get(a)is None for a in active)
 ss=sum(max(len(cc[a])-1,0)for a in active)
 ii=sum(bool(cc[a])for a in selected)
 assert len(selected)==rr+ss+ii
 bb={};dd={}
 for a in sorted(active):
  p=par.get(a);bb[a]=bb.get(p,0)+(a in selected);dd[a]=dd.get(p,0)+(len(cc[a])>=2)
 return rr,ss,ii,max(bb.values(),default=0),max(dd.values(),default=0)

summary={'status':'PASS','parameter_cases':0,'literal_updates':0,'comb_nodes':0,'all_prefix_skeleton_controls':0,'labels_checked':len(LABELS)}
for n in range(2,66):
 w=''.join('RLLR'*j+'L'+'RLLR'*j+'RLL'+'RLLR'*j+'L'+'RLLR'*j+'L'for j in range(n,0,-1))
 a=build(w);globals_ = a
 par=a['par'];ch=a['ch'];start=a['start'];r=a['r'];marks=a['marks'];poses=a['poses'];roots=a['roots'];ages=a['ages']
 assert len(a['seed'])==11*n+2
 index={t:v for v,t in start.items()}
 P=[];Q=[]
 for k in range(n):
  j=n-k;t=k*(16*n+6)-8*k*(k-1);tau=t+8*j+7
  pk=index[tau];P.append(pk)
  v=(-2*n-3+k,2*n-2-k)
  p,h=poses[tau];assert (p[0]+O[h][0],p[1]+O[h][1])==v
  assert r[pk]==(1 if k==n-1 else 2)
  assert marks[pk]==(2 if k==n-1 else 3)
  if k:
   qk=index[tau-1];Q.append(qk)
   assert par[pk]==P[k-1] and par[qk]==P[k-1]
   assert r[qk]==0 and marks[qk]==1
   p,h=poses[tau-1]
   assert (p[0]+O[h][0],p[1]+O[h][1])==(-2*n-4+k,2*n-1-k)
  if k<n-1:
   aa=(-2*n-2+k,2*n-1-k);bb=(-2*n-2+k,2*n-2-k)
   assert ages[aa][2]==ages[bb][2]==16*j-4
 root=roots[-2*n-3,2*n-1]
 assert par[P[0]]==root
 component=set();todo=list(ch[root])
 while todo:
  v=todo.pop();component.add(v);todo+=ch[v]
 assert component==set(P+Q)
 assert sum(marks[v]for v in component)==4*n-2
 assert skeleton(par,ch,marks,component)==(1,n-1,n-1,n,n-1)
 assert skeleton(par,ch,marks)[0]<=len(a['seed'])+1
 # Check prefix monotonicity on every node boundary for smaller parameters.
 if n<=10:
  before=(0,0,0)
  for t in range(len(w)+1):
   pm=Counter()
   for read in range(10,t):
    if w[read-10:read]not in F and w[read-9:read+1]not in F and w[read-10:read+1]not in SIX:
     # The latest node-start at or before this read owns the mark.
     node=max(v for v,ts in start.items() if ts<=read);pm[node]+=1
   vals=skeleton(par,ch,pm)[:3]
   assert all(x<=y for x,y in zip(before,vals));before=vals
   summary['all_prefix_skeleton_controls']+=1
 summary['parameter_cases']+=1;summary['literal_updates']+=len(w);summary['comb_nodes']+=len(component)
(ROOT/'check_marked_comb.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
