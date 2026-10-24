from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for line in(P/'DRIFT31_SINGLE_USED_SHAPES_SHA256SUMS').read_text().splitlines():
 h,f=line.split(None,1);assert sha(P/f)==h
J=json.loads((P/'drift31_single_used_g8_shapes_certificate.json').read_text());v=[1j,1,-1j,-1];d=3+1j;xy=lambda z:[int(z.real),int(z.imag)];T=lambda z:int(3*z.imag-z.real);canon=lambda z:json.dumps(z,sort_keys=True);out=lambda h,r:(h+(1 if r%2==0 else-1))%4
cover={};stats=Counter();simple=[]
for m in(3,5,7):
 for phase in(0,1):
  hs=list(range(phase,2*m,2));vs=list(range(1-phase,2*m,2))
  for east in combinations(hs,(m-3)//2):
   for north in combinations(vs,(m-1)//2):
    word=tuple((1 if k in east else 3)if k in hs else(0 if k in north else 2)for k in range(2*m));p=0j;pts=[]
    for h in word:pts.append(p);p+=v[h]
    assert p==-d;lev=list(map(T,pts));cover[word]=(pts,lev);stats[len(word),'raw']+=1
    if len(set(lev))==len(lev):simple.append(word)
assert len(cover)==1576 and len(simple)==6
for row in J['all_geometric_cases']:
 w=tuple(row['directions']);pts,lev=cover.pop(w);assert list(map(xy,pts))==row['points']and lev==row['levels']
 if row['outcome']=='repeated_full_class':
  a,b=row['witness_indices'];assert 0<=a<b<len(w)and lev[a]==lev[b]
 else:
  i=row['minimum_start_index'];assert lev[i]==min(lev)and tuple(row['canonical_directions'])==w[i:]+w[:i]==(3,0,3,2,3,2)
assert not cover
word=(3,0,3,2,3,2);p=0j;pts=[]
for h in word:pts.append(p);p+=v[h]
lev=list(map(T,pts));turn=[(h-word[i-1])%4 for i,h in enumerate(word)];assert turn.count(1)==turn.count(3)==3
left=[t for t,tr in zip(lev,turn)if tr==3];assert sorted(left)==[3,4,5]
def net(H):
 succ={};pred={};bad=[]
 for t,hs in H.items():
  for h in range(4):
   q=-t+v[h];u=T(q);lift=int(q.imag)
   if u not in H:continue # UNKNOWN, never empty by omission
   a=[r for r,x in enumerate(hs)if out(x,r)==h];b=[r for r,x in enumerate(H[u])if x==h]
   if len(a)!=len(b):bad.append((t,u,h,lift,a,b));continue
   for r,s in zip(a,b):succ[t,r]=((u,s),lift);pred[u,s]=((t,r),lift)
 if bad:return bad,None,None
 events={(t,r)for t,h in H.items()for r in range(len(h))};chains=[];seen=set()
 for e in sorted(events-set(pred)):
  seq=[];cur=e;k=0
  while True:
   assert cur not in seen;seen.add(cur);seq.append((cur,k))
   if cur not in succ:break
   cur,a=succ[cur];k+=a
  prev={}
  for(t,r),k in seq:
   p=-t+k*d
   if p in prev:assert r==prev[p]+1
   prev[p]=r
  chains.append(seq)
 assert seen==events # no closed components
 return [],succ,chains
placements=[];domainsizes=[]
for k in(2,3):
 for Q in combinations(left,k):
  Q=set(Q);H={}
  for t,h,tr in zip(lev,word,turn):
   a=(h-1)%4;H[t]=[a]if tr==1 else[a,a,(a+2)%4]+([a]if t in Q else[])
  row=next(r for r in J['all_quadruple_placements']if r['quadruple_levels']==sorted(Q));assert row['complete_circle_histories']=={str(t):H[t]for t in sorted(H)}
  qx=[sum((-1)**t for t in Q if(-t)%3==i)for i in range(3)];qy=sum((-1)**t for t in Q);dist=lambda n:min(n%4,-n%4);px=sum(dist(2+a)for a in qx);py=dist(2+qy)
  assert [qx,qy,px,py,6-k+max(px,py)]==[row['quadruple_signed_x_fibres'],row['quadruple_signed_y_fibre'],row['Phi_x'],row['Phi_y'],row['exact_charge_lower_bound']]
  bad,succ,chains=net(H)
  if bad:
   w=row['witness'];assert (w['source_level'],w['target_level'],w['heading'],w['voltage'],w['source_complete_ranks'],w['target_complete_ranks'])in bad
   assert row['outcome']=='internal_port_mismatch'
  else:
   assert row['outcome']=='OPEN_circle_interface';ret=[]
   for seq in chains:
    (t,r),k0=seq[0];h=H[t][r];start=-t-v[h]
    (u,s),kk=seq[-1];hh=out(H[u][s],s);end=-u+kk*d+v[hh]
    if T(start)!=6 or start!=end:continue
    assert all(-a+z*d!=start for(a,b),z in seq)
    depordinal=[a for a,x in enumerate(H[t])if x==h].index(r);inordinal=[a for a,x in enumerate(H[u])if out(x,a)==hh].index(s)
    assert(h,hh,depordinal,inordinal,len(seq)+1)==(1,0,0,1,4);ret.append((depordinal,inordinal))
   assert ret==[(0,1)]
   bound=2*(3+H[5].count(1))+1;dom=[]
   for n in range(bound+1):
    for hs in product((0,2),repeat=n):
     ni=[r for r,h in enumerate(hs)if h==0];eo=[r for r,h in enumerate(hs)if out(h,r)==1]
     if len(ni)==3 and len(eo)==H[5].count(1)and ni[1]==eo[0]+1:dom.append(list(hs));assert not net({**H,6:hs})[0]
   ext=row['first_exterior_cell_T6'];assert ext['derived_read_bound']==bound and ext['all_complete_domains']==dom;domainsizes.append(len(dom))
  placements.append({'Q':sorted(Q),'outcome':row['outcome']})
assert sorted(domainsizes)==[7,13]
report={'status':'PASS conditional single-used F-circle g8/full d(3,1) finite shape and port cover','script_sha256':sha(Path(__file__)),'proof_sha256':sha(P/'DRIFT31_G8_SINGLE_USED_CIRCLE_SHAPE_COVER.md'),'raw_counts':{str(k):v for k,v in stats.items()},'simple_paths':6,'repeated_full_class_paths':1570,'sole_normalized_circle':'WNWSWS','placements':placements,'next_cell_domains':domainsizes,'scope':['Signed single-use charge bounds ONLY circle lengths6/10/14 and at most one triple; no unknown period or exterior bound','T=3y-x is the full quotient invariant, not a primitive replacement; all translations and two axis phases enumerated','All omitted classes UNKNOWN including below the selected circle; complete-known internal ports alone reject two placements','Physical four-step return to the same T6 cell gives consecutive ranks; all20 complete next histories derive from exact mandatory port counts'],'not_claimed':['existence of any single-used F circle for arbitrary drift(3,1) fronts','completion of either open interface','growth8 exclusion','universal capture']}
f=R/'audits/drift31_single_used_shapes_independent.json';f.write_text(json.dumps(report,indent=2)+'\n');print(sha(f));print(report['status'])
