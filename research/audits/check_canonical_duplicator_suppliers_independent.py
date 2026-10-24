from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';old=R/'audits/check_canonical_birth_rank3_balance_independent.py';ns={'__file__':str(old)};exec(old.read_text().split('rows=[];candidates=0')[0],ns);choices,departures=(ns[k]for k in('choices','departures'));data=json.loads((D/'canonical_duplicator_upper_supplier_ports.json').read_text())
ports=[('A','W','Z','W'),('Z','N','Y','N'),('Y','E','B','E'),('B','S','A','S'),('Y','W','u','W'),('u','N','t','N'),('t','E','a','E'),('a','S','Y','S'),('B','N','v','N'),('v','W','a','W')]
def closure(h,birth):
 out={v:departures(s)for v,s in h.items()};nodes=[(v,i)for v,s in h.items()for i in range(len(s))];edges=[]
 for v,s in h.items():edges.extend(((v,i),(v,i+1),4)for i in range(len(s)-1))
 for v,dh,w,ih in ports:
  aa=[(v,i)for i,c in enumerate(out[v])if c==dh];bb=[(w,i)for i,c in enumerate(h[w])if c==ih]
  if len(aa)!=len(bb):return
  for x,y in zip(aa,bb):edges.extend([(x,y,1),(y,x,-1)])
 for pairs,start in[([('A','W'),('Z','N'),('Y','E'),('B','S')],('A',1)),([('u','N'),('t','E'),('a','S'),('Y','W')],(birth,1))]:
  first=[next(((v,i)for i,c in enumerate(out[v])if c==dh),None)for v,dh in pairs]
  if None in first or start not in first:return
  edges.extend((start,q,1)for q in first if q!=start)
 vv=next((( 'v',i)for i,c in enumerate(out['v'])if c=='E'),None)
 if vv is None:return
 edges.append((('B',1),vv,1));n=len(nodes);idx={q:i for i,q in enumerate(nodes)};inf=-10**9;d=[[0 if i==j else inf for j in range(n)]for i in range(n)]
 for x,y,k in edges:d[idx[x]][idx[y]]=max(d[idx[x]][idx[y]],k)
 for k in range(n):
  for i in range(n):
   if d[i][k]==inf:continue
   for j in range(n):
    if d[k][j]!=inf:d[i][j]=max(d[i][j],d[i][k]+d[k][j])
  if any(d[i][i]>0 for i in range(n)):return
 return idx,d
rows=[];count=0
for u,t,a,v,birth in product(choices('W'),choices('N'),choices('E'),choices('N'),['u','t','a']):
 if a[1]!=v[1]:continue
 if not {'u':u[0],'t':t[0],'a':a[0]}[birth].startswith({'u':'EEW','t':'SSN','a':'WWE'}[birth]):continue
 count+=1;h=dict(A='NNSN',Z='WWEW',Y='NSSS',B='EEWE',u=u[0],t=t[0],a=a[0],v=v[0]);sol=closure(h,birth)
 if sol is None:continue
 idx,d=sol
 def exact(x,y,k):assert d[idx[x]][idx[y]]==k and d[idx[y]][idx[x]]==-k
 exact(('B',1),('a',0),-2);exact(('B',1),(birth,1),-4 if birth=='u'else-3)
 rows.append((u[0],t[0],a[0],v[0],birth,u[1],t[1],a[1]))
expected={(r['headings']['u'],r['headings']['t'],r['headings']['a'],r['headings']['v'],r['birth'],r['u_other'],r['t_other'],r['a_other'])for r in data['rows']};assert set(rows)==expected and(count,len(rows))==(39690,14);assert all(r[7]=='M-2'and r[3]in('NNN','NNNS')and r[4]!='a'for r in rows)
# Align lower SW E canonical entries with upper NW S entries. Clockwise
# rotation around the face center sends the original SE Y=NSSS to SW EWWW.
head='NESW';rot=lambda s:''.join(head[(head.index(c)+1)%4]for c in s)
assert rot('NSSS')=='EWWW'
for lower in rows:
 if lower[4]!='u':continue
 entry=rot(lower[0]);assert entry in('SSN','SSNS')
 for upper in rows:
  if upper[4]=='t'and upper[1]==entry:assert upper[0]=='W'and upper[0]!=rot('NSSS')
# Independently identify each possible canonical rank1 child of I.
rface={'N':-1j,'E':-1-1j,'S':-1,'W':0};dest={'N':-1,'E':0,'S':-1j,'W':-1-1j}
def negative(q,h):return(q+rface[h[0]],q+dest[h[0]])if len(h)>=3 and h[0]==h[1]and head[(head.index(h[0])+2)%4]==h[2]else None
classes=[]
for row in rows:
 u,t,a,v,birth,*_=row;hs={0:u,1j:t,1+1j:a,1:'NSSS'};entry=u if birth=='u'else t;flag=len(entry)==4 and entry[3]==entry[1];out=[(q,s)for q,s in hs.items()if(e:=negative(q,s))and e[0]==0];childflags=sum(len(s)==4 and s[3]==s[1]for q,s in out)
 if flag:assert not out
 else:assert childflags==0
 classes.append((row[:5],int(flag),childflags-int(flag)))
note=D/'canonical_duplicator_opposite_supplier_seven_profiles.md';notehash=hashlib.sha256(note.read_bytes()).hexdigest();assert notehash.startswith('9868024f')
out={'status':'PASS all-K actual duplicator opposite-supplier seven profiles and injection','note_sha256':notehash,'candidates':count,'rows':rows,'flag_classes':classes,'analytic':'Complete ordinal boundary ports, same-cell gaps and canonical minima are imposed without K1 or a successor table. Shared a/v opposite height is retained. Max-plus closure proves exact aR0=beta-2 and actual I birth beta-4/beta-3 in every feasible clock assignment. Same-entry lower-vs-upper alternatives force SW EWWW versus W, yielding D-to-I injectivity under full-drift translation. Flag1 I rows are genuine leaves; all other I rows have flag0 and no flag1 child. The all-four-read lower row is retained.','scope':'Necessary local capacity interface, not an actual complete white front, early-parent iteration, original fuel or an additive odd-output reservation without separate disjointness.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(count,len(rows),notehash)
