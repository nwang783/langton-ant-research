"""A supplied three two-corner old-side routing itinerary, retaining whole history.
This is a finite control and reports its FIRST ownership conflict. No route
search or inference of a finite-seed wave from disconnected endpoint inputs.
"""
from pathlib import Path
import runpy,json
P=Path(__file__).resolve().parent;G=P.parents[1]/'nonlinear_global_budget_2026-10-23'
R=runpy.run_path(str(P/'check_prepared1564_router_geometry.py'));H,V,ROUTES=(R[x]for x in['H','V','ROUTES'])
C=runpy.run_path(str(G/'changed_endpoint_catalog.py'));E=C['E']

def actual(rows,B,p,h,n):
 w=''
 for _ in range(n):
  c='L'if C['initial_color'](p,rows,B)else'R';w+=c;C['toggle'](B,p);h=(h+(1 if c=='R'else-1))%4;u,v=V[h];p=p[0]+u,p[1]+v
 return w,p,h

def prefix(N):assert N>=0;return H*(N//104)+H[:N%104]
orig=json.loads((G/'endpoint_catalog_results.json').read_text())['results'];ra=next(x for x in orig if x['channel']==[-12,0]);rb=next(x for x in orig if x['channel']==[26,0])
rows,bb,p,h,taua,phia=E['make_initial']((-12,0));wa,pa,ha=actual(rows,bb,p,h,ra['entry']);assert[list(pa),ha]==ra['pose']
rowsa,capa,_=C['normalized_endcap'](ra);rows,bb,p,h,taub,phib=C['incoming'](rowsa,capa,(26,0));wb,pb,hb=actual(rows,bb,p,h,rb['entry']);assert[list(pb),hb]==rb['pose']
node=next(z for z in json.loads((G/'endpoint_return_closure_results.json').read_text())['states']if z['state_sha256'].startswith('425bd79'))
rows,bb,p,h,tauc,phic=C['incoming']({tuple(z):[0]for z in node['profiles']},set(map(tuple,node['cap'])),(12,1));wc,pc,hc=actual(rows,bb,p,h,83);assert(pc,hc)==((-6,-6),0)
# Reconstruct the frozen pristine exceptional literal word, without discarding its field.
S=R['infer'](H,(-15,10),3)['input'];B=S|{(-39,-20)}
assert len(B)==14
stable,sp,sh=actual({},B,(-15,10),3,52262);assert(sp,sh)==((0,-49),1)

def run(n,T):
 t1,t2,t3=T
 pieces=[('initial_H',H*n),('pristine_exception',stable),('initial_return',H*(n+t1)),
 ('router1',ROUTES[0][1]+H*ROUTES[0][2]+ROUTES[0][3]),('A_incoming',prefix(104*(n+t1-17)+taua)),
 ('A_response',wa),('A_to_phase0',ra['tail_word'][:74]),('A_return',H*(n+t2-4)),
 ('router2',ROUTES[1][1]+H*ROUTES[1][2]+ROUTES[1][3]),('B_incoming',prefix(104*(n+t2-4)+taub)),
 ('B_response',wb),('B_to_phase0',rb['tail_word'][:101]),('B_return',H*(n+t3-4)),
 ('router3',ROUTES[2][1]+H*ROUTES[2][2]+ROUTES[2][3]),('C_incoming',prefix(104*(n+t3-3)+tauc)),('C_prefix',wc)]
 last={};first={};seed=set();p=(-15,10);h=3;i=0;stages=[]
 for label,w in pieces:
  stages.append(dict(stage=label,time=i,pose=[p,h],length=len(w)))
  for j,c in enumerate(w):
   if p in last and last[p]['turn']==c:
    return dict(n=n,T=T,status='CONFLICT',at=dict(stage=label,within=j,time=i,cell=p,heading=h,turn=c),previous=last[p],inferred_seed_mass=len(seed),stages=stages)
   if p not in first:
    first[p]=c
    if c=='L':seed.add(p)
   last[p]=dict(stage=label,within=j,time=i,cell=p,heading=h,turn=c)
   h=(h+(1 if c=='R'else-1))%4;u,v=V[h];p=(p[0]+u,p[1]+v);i+=1
 return dict(n=n,T=T,status='PASS FINITE PREFIX ONLY',seed_mass=len(seed),seed=sorted(seed),stages=stages,end=[p,h])
if __name__=='__main__':
 out=[run(100,T)for T in[(200,400,600),(600,400,200)]]
 (P/'prepared1564_connected_itinerary.json').write_text(json.dumps(out,indent=2)+'\n')
 for x in out:print({k:v for k,v in x.items()if k not in['stages','seed']})
