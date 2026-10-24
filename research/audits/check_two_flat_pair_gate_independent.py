from pathlib import Path
from itertools import product
from collections import Counter,deque
import json,hashlib,time
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'adjacent_two_flat_pair_gates_leave_only_RR_open.md';C=D/'check_two_flat_pair_reader_closure.json';assert sha(P)=='94b498abfda220c2ff3e08d634d12ea5057c314166ed546213ff738015ba2d15';assert sha(C)=='d5a356fb4a2a18825aea46bf4882bb6e57358158a5843c0d801e4d164720f899';J=json.loads(C.read_text());H='NESW';dv=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];rotate=lambda w,n:''.join(H[(H.index(c)+n)%4]for c in w)
words={z:['']+[''.join(w)for n in range(1,5)for w in product('NS'if z==0 else'EW',repeat=n)]for z in(0,1)}
out={w:tuple((H.index(c)+(1 if i%2==0 else-1))%4 for i,c in enumerate(w))for ww in words.values()for w in ww};inc={w:tuple(w.count(c)for c in H)for w in out};otc={w:tuple(out[w].count(k)for k in range(4))for w in out}
def ports(w,p,k):return otc[w][k]if(k%2)!=int(p.real+p.imag)%2 else inc[w][(k+2)%4]
def geom(t,b,s,fs,ms):
 turns={'RR':'RLRRLR','RLR':'RLRLRLR','RLLR':'RLRLLRLR'}[t];p=-1-1j;ci=0;fi=mi=0;nodes=[]
 for i,c in enumerate(turns):
  if i==0:w='N'*b;role='sink'
  elif i==len(turns)-1:w=rotate('EWE'if s==3 else'EWEW',ci-1);role='source'
  elif c=='R':w=rotate(fs[fi],ci);fi+=1;role='flat'
  elif i in(1,len(turns)-2):w=rotate('WWEE',ci-1);role='Vcap'
  else:w=rotate(ms[mi],ci-1);mi+=1;role='middle'
  co=(ci+(1 if c=='R'else-1))%4;assert w[0]==H[ci if c=='R'else(ci+2)%4];nodes.append(dict(cell=xy(p),turn=c,history=w,role=role,ci=H[ci],co=H[co]));p+=dv[co];ci=co
 assert len({tuple(n['cell'])for n in nodes})==len(nodes);return nodes

def audit(hs):
 ev=[(p,i)for p,w in hs.items()for i in range(len(w))];ix={v:i for i,v in enumerate(ev)};succ={};edges=[]
 for p,w in hs.items():
  for i in range(len(w)-1):edges.append((ix[p,i],ix[p,i+1],4))
  for k in range(4):
   q=p+dv[k]
   if q not in hs:continue
   a=[i for i,z in enumerate(out[w])if z==k];b=[i for i,z in enumerate(hs[q])if z==H[k]];assert len(a)==len(b)
   for i,j in zip(a,b):u=ix[p,i];v=ix[q,j];assert u not in succ;succ[u]=v;edges.extend(((u,v,1),(v,u,-1)))
 for start,(p,r)in enumerate(ev):
  seen={start};cur=start
  while cur in succ:
   cur=succ[cur]
   if ev[cur][0]==p:
    if ev[cur][1]!=r+1:return'skipped_rank'
    break
   if cur in seen:return'event_cycle'
   seen.add(cur)
 dist=[0]*len(ev)
 for _ in ev:
  changed=False
  for u,v,k in edges:
   if dist[v]<dist[u]+k:dist[v]=dist[u]+k;changed=True
  if not changed:break
 else:return'clock_cycle'
 return'open'

summary=Counter();row_results=[];refs={(z['template'],z['sink'],z['source'],tuple(z['flat_words']),tuple(z['middle_words'])):z for z in J['primary_rows']};start=time.time()
for tmpl in('RR','RLR','RLLR'):
 for b,s in product((3,4),repeat=2):
  for fs in product(('NNSS','NSSN'),repeat=2):
   for ms in product(('WEE','WEEW','WWEE'),repeat={'RR':0,'RLR':1,'RLLR':2}[tmpl]):
    key=tmpl,b,s,fs,ms;ref=refs[key];nodes=geom(*key);assert nodes==ref['known_nodes'];fixed={complex(*n['cell']):n['history']for n in nodes};pts=set(fixed)
    while True:
     cand={p+v for p in pts for v in dv}-pts;add={q for q in cand if sum(q+v in pts for v in dv)>=2}
     if not add:break
     pts|=add
    pts=sorted(pts,key=lambda p:(p.real,p.imag));assert list(map(xy,pts))==ref['closure_cells'];assert len(pts)=={'RR':8,'RLR':16,'RLLR':12}[tmpl];adj={p:[(p+v,k)for k,v in enumerate(dv)if p+v in pts]for p in pts};ds={p:[fixed[p]]if p in fixed else words[int(p.real+p.imag)%2][:]for p in pts}
    def reduce(ds):
     queue=deque(ds)
     while queue:
      p=queue.popleft()
      for q,k in adj[p]:
       allowed={ports(w,p,k)for w in ds[p]};keep=[w for w in ds[q]if ports(w,q,(k+2)%4)in allowed]
       if not keep:return None
       if len(keep)<len(ds[q]):ds[q]=keep;queue.append(q)
     return ds
    counts=Counter();good=[]
    def search(ds):
     ds=reduce(ds)
     if ds is None:return
     undec=[p for p in pts if len(ds[p])>1]
     if undec:
      p=min(undec,key=lambda p:len(ds[p]))
      for w in ds[p]:search(ds|{p:[w]})
      return
     hs={p:v[0]for p,v in ds.items()};ans=audit(hs);counts[ans]+=1
     if ans=='open':good.append({f'{int(p.real)},{int(p.imag)}':w for p,w in hs.items()})
    search(ds);assert counts==ref['counts'],(key,counts,ref['counts']);assert {json.dumps(g,sort_keys=True)for g in good}=={json.dumps(g,sort_keys=True)for g in ref['open']};summary.update(counts);summary['primary']+=1;row_results.append({'key':[tmpl,b,s,fs,ms],'counts':dict(counts),'open':len(good)})
 print(tmpl,dict(summary),time.time()-start,flush=True)
assert summary==J['summary'];assert len(refs)==208 and summary['open']==64 and sum(v for k,v in summary.items()if k!='primary')==170592
O=dict(status='PASS exact local cap-four adjacent two-flat stencil only',proof=sha(P),certificate=sha(C),script=sha(S),summary=dict(summary),independently_rebuilt_rows=row_results,analytic_scope=['All208 complete primary histories, physical coordinates/rotations and distinct vertices are regenerated. Added corners are the finite two-neighbor closure, not a radius cutoff. All empty and1..4 WHITE alternating histories on each actual incoming axis are included.','Arc-consistency only deletes unsupported exact internal port counts; recursive assignment exhausts every remaining finite domain. Successor ordinal matching is on the same physical edge and zero counts are retained.','Independent physical successor walks reject every non-next same-cell rank or closed event path; remaining positive max-plus cycles use exact one-step edges and universal same-cell gap>=4. No stream-height/global-maximum check and no critical-side check are used anywhere. Thus the result truly has neither global-M nor critical-level nor period/drift premises.','All170592 complete count-compatible patches reproduce author counts, including64 RR-only open patches. Each of16 RR primaries retains exactly WEW/WEWE at(-1,0) andSSS/SSSS at(2,0). Open means necessary exterior-port network only, not a physical factor or global phase assignment.','Applying this local gate to a full b-circle still requires its exact sink/V/flat/middle/flat/V/source roles, neighborhood ownership and full-drift alias handling. It does not exhaust global two-flat motifs or require a third flat.']);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
