from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';a=json.loads((D/'canonical_max_face_child_ports.json').read_text());head='NESW'
def opposite(h):return head[(head.index(h)+2)%4]
def choices(h):
 o=opposite(h);out=[]
 for n in range(1,5):
  for ls in product((h,o),repeat=n//2):
   s=''.join(h if r%2==0 else ls[r//2]for r in range(n));out.append((s,'M-'+str((n+1)//2)))
 for n in(3,4):
  for first in(h,o):
   for ls in product((h,o),repeat=n//2):out.append((first+ls[0]+opposite(first)+(ls[1]if n==4 else''),'M'))
 assert len(out)==21 and len(set(out))==21;return out
def departures(hist):return ''.join(head[(head.index(h)+(1 if i%2==0 else-1))%4]for i,h in enumerate(hist))
ports=[('A','W','Z','W'),('Z','N','Y','N'),('Y','E','B','E'),('B','S','A','S')]
def possible(h):
 outs={v:departures(s)for v,s in h.items()};nodes=[(v,i)for v,s in h.items()for i in range(len(s))];edges=[]
 for v,s in h.items():edges.extend(((v,i),(v,i+1),4)for i in range(len(s)-1))
 for v,dh,w,ih in ports:
  a=[(v,i)for i,c in enumerate(outs[v])if c==dh];b=[(w,i)for i,c in enumerate(h[w])if c==ih]
  if len(a)!=len(b):return False
  for x,y in zip(a,b):edges.extend([(x,y,1),(y,x,-1)])
 first=[next((v,i)for i,c in enumerate(outs[v])if c==dh)for v,dh,w,ih in ports]
 if ('A',1)not in first:return False
 edges.extend((('A',1),v,1)for v in first if v!=('A',1))
 # Transitive max-plus closure independently detects inconsistent clocks.
 n=len(nodes);idx={v:i for i,v in enumerate(nodes)};inf=-10**9;dist=[[0 if i==j else inf for j in range(n)]for i in range(n)]
 for x,y,k in edges:dist[idx[x]][idx[y]]=max(dist[idx[x]][idx[y]],k)
 for k in range(n):
  for i in range(n):
   if dist[i][k]==inf:continue
   for j in range(n):
    if dist[k][j]!=inf:dist[i][j]=max(dist[i][j],dist[i][k]+dist[k][j])
  if any(dist[i][i]>0 for i in range(n)):return False
 return True
rows=[];candidates=0
for ah,z,y,b in product(['NNS','NNSN','NNSS'],choices('W'),choices('N'),choices('E')):
 candidates+=1;h={'A':ah,'Z':z[0],'Y':y[0],'B':b[0]}
 if not possible(h):continue
 potential=[v for v,pref in [('Z','WWE'),('Y','NNS'),('B','EEW')]if h[v].startswith(pref)];sf=int(ah=='NNSN');childflags=[v for v in potential if len(h[v])==4 and h[v][3]==h[v][1]];q=len(childflags)-sf
 rows.append((tuple(h[v]for v in'AZYB'),(z[1],y[1],b[1]),tuple(potential),q,tuple(childflags)))
expected={(tuple(r['headings'][v]for v in'AZYB'),tuple(r['other'][v]for v in'ZYB'),tuple(r['potential_children']))for r in a['rows']};assert{r[:3]for r in rows}==expected;assert(candidates,len(rows))==(27783,110);assert Counter(len(r[2])for r in rows)=={0:36,1:55,2:17,3:2}
positive=[r for r in rows if r[3]>0];assert len(positive)==5 and max(r[3]for r in rows)==1
assert{r[0]for r in positive}=={('NNS','WW','NSSS','EEWE'),('NNS','WWE','NSSS','EEWE'),('NNS','WWEE','NSN','EEWE'),('NNS','EWW','SSNS','EEWE'),('NNSN','WWEW','NSSS','EEWE')}
assert all(r[3]==0 and not r[4]and r[0][0]!='NNSN'for r in rows if len(r[2])==3)
for r in positive:
 if r[0][0]=='NNSN':assert r[4]==('Z','B')and all(h=='M'for h in r[1])
 else:assert r[0][0]=='NNS'and r[4]==('B',)
note=D/'canonical_birth_rank3_flag_balance.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='d1f7304b2d8938137d6117b338f6d003d481a9c7541e784587a7e883e18eb0b3'
out={'status':'PASS complete local canonical rank3-flag inventory and actual-child global balance','note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'candidates':candidates,'necessary_profiles':len(rows),'positive_potential_profiles':positive,'three_child_profiles':[r for r in rows if len(r[2])==3],'analytic':'Actual child-flag sum is bounded by potential-child sum. Every actual q lies[-1,1], and positive q occurs only at one of four three-read-entry producers or the unique four-read duplicator with BOTH flag1 children actually canonical. Finite indegree-one canonical quotient gives exact zero total q. The distinct early leaves all have flag1, forcing N_O+N_D>=n_A. O-entry three-read opposite-R classes are disjoint from same-R strict-fall reservations and singleton ancestor reservations. Rise faces are a subset of O.','bounds':['N_O+N_D=sum negative(-q)>=n_A','N_odd>=N_O+n_SB+n_Sanc','N_odd>=max(n_up,n_A-N_D)+n_SB+n_Sanc'],'scope':'Local histories are necessary overapproximations, not realized fronts. Potential duplicators are counted only if both children are actually canonical. No fuel, original-root, duplication attainability, iterative supplier or general K1 exclusion.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(candidates,len(rows))
