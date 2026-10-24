"""Full3x3 stock-reader domain at a cyclic LL-first O/U reset.
All complete WHITE cap4 histories, zero ports and physical ordinals retained.
Finite junction cover, not a period/radius scan. Cyclic reductions use the
separately stated signed critical/global-M/no-one-use gates.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
base=Path(__file__).parent;lib={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],lib)
H=lib['H'];V=lib['V'];dom=lib['dom'];prop=lib['propagate'];check=lib['check'];out=lib['out'];rows=[];tot=Counter()
for root in['EWW','EWWE']:
 fixed={(0,0):'NNSS',(0,1):root,(1,0):'EEWW',(1,1):'SNNS'};ds=prop({p:([fixed[p]]if p in fixed else dom(p))for p in product(range(3),repeat=2)})
 ct=Counter();local=[];surv=[]
 def rec(ds):
  if all(len(v)==1 for v in ds.values()):
   hs={p:v[0]for p,v in ds.items()};a=check(hs);ct[a]+=1
   if a!='open':return
   local.append(hs)
   # Necessary cyclic predecessor closure from the HUMAN signed-gate proof:
   # U is the LEFT-V predecessor of Y; T must depart W and cannot be SNN.
   if hs[(1,2)]!='EEWW'or hs[(2,2)]not in['SNNS','SSNN']:return
   C,D,R,T=hs[(0,2)],hs[(2,1)],hs[(2,0)],hs[(2,2)]
   assert C==('SSN'if root=='EWW'else'SSNN')
   if T=='SNNS':
    assert(D,R)==('EWWE','NNSS');kind='P';tags=['T_RIGHT_Y_with_preceding_flat_RR']
   else:
    assert(D,R)in[('WEE','NNS'),('WEEW','NNSS')];kind='N';tags=['T_RIGHT_X_with_preceding_flat_RR']
    if D=='WEEW':tags.append('T_LEFT_V_with_D_RIGHT_Y')
   su={}
   for p,h in hs.items():
    for dr,v in V.items():
     q=p[0]+v[0],p[1]+v[1]
     if q not in hs:continue
     sr=[r for r in range(len(h))if out(h,r)==dr];tr=[r for r,z in enumerate(hs[q])if z==dr];assert len(sr)==len(tr)
     su.update({(p,r):(q,s)for r,s in zip(sr,tr)})
   cur=((2,0),1);path=[cur]
   while cur!=((1,0),3):
    assert cur in su and len(path)<20;cur=su[cur];path.append(cur)
   word=''.join('R'if r%2==0 else'L'for p,r in path)
   assert word==('LRRRRL'if kind=='P'else'LRRLLLLRRL')
   x2=path.index(((1,0),2));x3=len(path)-1
   assert x3-x2==(4 if kind=='P' else 8)
   surv.append(dict(kind=kind,placement_tags=tags,histories={str(p):h for p,h in sorted(hs.items())},actual_reactivation_channel=path,word=word,X_age23=x3-x2,Y_age23=4 if kind=='N'else'at_least4_unbounded',tail_Y3_minus_X3=-3 if kind=='N'else'Y_age23_minus3_positive'))
   return
  p=min((p for p in ds if len(ds[p])>1),key=lambda p:len(ds[p]))
  for h in ds[p]:
   z=prop(ds|{p:[h]})
   if z is not None:rec(z)
 rec(ds);tot.update(ct);assert len(local)==(24 if root=='EWW' else 22)and len(surv)==3
 rows.append(dict(root=root,full_count_compatible_rejections=dict(ct),open_local_profiles=len(local),cyclic_necessary_profiles=surv))
assert sum(len(r['cyclic_necessary_profiles'])for r in rows)==6
# Minimum owner frames for the six- and ten-event ACTUAL channels.
def walk(word,p,h):
 start=p;early=False
 for i,a in enumerate(word):
  h=H[(H.index(h)+(1 if a=='R'else-1))%4];p=p[0]+V[h][0],p[1]+V[h][1]
  if p==start and i<len(word)-1:early=True
 return p,h,early
frames=[]
for C in['LRRRRL','LRRLLLLRRL']:
 ff=[]
 for i in[1,2]:
  for pre in product('LR',repeat=i):
   for post in product('LR',repeat=2-i):
    if pre[0]!='L':continue
    net=sum(1 if q=='R'else-1 for q in pre);hi=H[(-net)%4]
    dp,hh,_=walk(''.join(pre),(0,0),hi);assert hh=='N';root=(2-dp[0],-dp[1]);w=''.join(pre)+C+''.join(post)
    p,h,early=walk(w,root,hi)
    if p==root and h==hi and not early:ff.append(dict(root=root,incoming=hi,word=w))
 assert len(ff)==2 and {(tuple(f['root']),f['incoming'])for f in ff}=={((2,-1),'E'),((1,-1),'S')}
 frames.append(dict(channel=C,excluded_minimum_owner_span=len(C)+2,only_frames=ff,required_owner_span_at_least=len(C)+6))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,all_stock_count_compatible_counts=dict(tot),roots=rows,cyclic_profiles=6,tagged_cyclic_placements=8,owner_frames=frames,warning='Six necessary local inventories/eight cyclic placement tags, not completed WHITE fronts or actual prepared factors. Signed-gate cyclic reductions and owner exclusions require the human proof.'),indent=2)+'\n');print('PASS',dict(tot),'46 local -> six cyclic inventories/eight placements; reactivation4/8')
