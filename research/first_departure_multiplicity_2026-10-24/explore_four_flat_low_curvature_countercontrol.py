"""Discovery of the FOUR-flat low-curvature countercontrol probe between high ends.
All candidate internal gap words with cluster R-minus-L <=1; signed existing global-M/critical local gates
prune primary histories before all count-forced corner readers are tested.
Not a period/radius/front scan. OPEN patches remain necessary controls only.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json,time
base=Path(__file__).parent;lib={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],lib)
H=lib['H'];V=lib['V'];rot=lib['rot'];dom=lib['dom'];prop=lib['propagate'];check=lib['check'];sidecheck=lib['sidecheck']
FW={'X':'NNSS','Y':'NSSN'};LW={'O':'WEE','U':'WEEW','V':'WWEE'}
def allowed(gs,fs,ls):
 if any(gs[i]==gs[i+1]==0 for i in range(len(gs)-1)):return False
 # signed LL complete relation and critical second LEFT V.
 for i,g in enumerate(gs):
  if g==2:
   if ls[i][1]!='V'or fs[i]!='Y':return False
   if fs[i+1]!=('Y'if ls[i][0]=='V'else'X'):return False
 # signed general RR LEFT ends are V.
 for i,g in enumerate(gs):
  if g==0:
   if i>0 and ls[i-1][-1]!='V':return False
   if i+1<len(gs)and ls[i+1][0]!='V':return False
 # singleton flow2 island: middle O, preceding Y, outer immediate LEFTs V.
 for i,g in enumerate(gs):
  if g!=1:continue
  touchesRR=(i>0 and gs[i-1]==0)or(i+1<len(gs)and gs[i+1]==0)
  if touchesRR:
   if ls[i]!=('V',):return False
  else:
   if ls[i]!=('O',)or fs[i]!='Y':return False
   if i>0 and ls[i-1][-1]!='V':return False
   if i+1<len(gs)and ls[i+1][0]!='V':return False
 return True

def build(gs,fs,ls,nb,ns):
 spec=[('R','N'*nb,'sink'),('L','WWEE','Vcap')]
 for i,f in enumerate(fs):
  spec.append(('R',FW[f],'flat'))
  if i<3:spec.extend(('L',LW[k],'middle')for k in ls[i])
 spec.extend([('L','WWEE','Vcap'),('R','EWE'if ns==3 else'EWEW','source')])
 p=(-1,-1);ci='N';nodes=[]
 for j,(t,h,role)in enumerate(spec):
  h=h if j==0 else rot(h,ci,'N'if role=='flat'else'E')
  co=H[(H.index(ci)+(1 if t=='R'else-1))%4]
  nodes.append(dict(cell=p,turn=t,history=h,role=role,ci=ci,co=co));p=p[0]+V[co][0],p[1]+V[co][1];ci=co
 return nodes
stats=Counter();rows=[];t=time.time()
for gs in product(range(3),repeat=3):
 gain=4-sum(gs)
 if gain>1:continue
 for fs in product('XY',repeat=4):
  for x in product('OUV',repeat=sum(gs)):
   ls=[];j=0
   for g in gs:ls.append(tuple(x[j:j+g]));j+=g
   if not allowed(gs,fs,ls):continue
   for nb,ns in product([3,4],repeat=2):
    nodes=build(gs,fs,ls,nb,ns);fixed={tuple(n['cell']):n['history']for n in nodes}
    if len(fixed)!=len(nodes):
     stats['PRIMARY_GEOMETRY']+=1;continue
    pts=set(fixed)
    while True:
     ca={(p[0]+v[0],p[1]+v[1])for p in pts for v in V.values()}-pts
     ad={q for q in ca if sum((q[0]+v[0],q[1]+v[1])in pts for v in V.values())>=2}
     if not ad:break
     pts|=ad
    ds=prop({p:([fixed[p]]if p in fixed else dom(p))for p in sorted(pts)})
    ct=Counter();sample=[]
    def rec(ds):
     if all(len(a)==1 for a in ds.values()):
      hs={p:a[0]for p,a in ds.items()};a=check(hs)
      if a=='open':a=sidecheck(hs,nodes)or'open'
      ct[a]+=1
      if a=='open'and not sample:sample.append({str(p):h for p,h in hs.items()})
      return
     p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
     for h in ds[p]:
      nd=prop(ds|{p:[h]})
      if nd is not None:rec(nd)
    if ds is None:ct['PRIMARY_PORT']+=1
    else:rec(ds)
    row=dict(gaps=gs,flat_words=fs,left_words=ls,sink=nb,source=ns,cluster_turn=gain,counts=dict(ct),nodes=nodes,closure_cells=sorted(pts),open_sample=sample)
    rows.append(row);stats.update(ct)
    if ct['open']:print('OPEN',gs,fs,ls,nb,ns,'gain',gain,'n',ct['open'],'cells',len(pts),flush=True)
 print('GAPS DONE',gs,'elapsed',time.time()-t,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,summary=dict(stats),primary_count=len(rows),rows=rows),indent=2)+'\n');print('DONE',len(rows),dict(stats),time.time()-t)
