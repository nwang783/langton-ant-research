"""Enumerate only literal raised-base leaves and finite parent replay obligations."""
from pathlib import Path
import json,hashlib
P=Path(__file__).parent
scope={'__file__':str(P/'extract_two_black_word_jobs.py')};exec((P/'extract_two_black_word_jobs.py').read_text().split('jobs=[];')[0],scope)
R=scope['R'];parse=scope['load_literal'];V=scope['V'];parents=[];raised=[]
def cells1(F,n):
 dg,near,far=F;v=V[dg];return sorted(set(map(tuple,near+[[q[0]+n*v[0],q[1]+n*v[1]]for q in far])))
def cells2(F,a,b):
 vs,bs=F;return sorted(set((q[0]+sum([a,b][i]*V[vs[i]][0]for i in mask),q[1]+sum([a,b][i]*V[vs[i]][1]for i in mask))for q,mask in bs))
def add(src,kind,index,cells):raised.append(dict(id=len(raised),source=src,kind=kind,index=index,cells=cells,period_budget=6000))
for path in sorted((R/'Parents').glob('Chunk*.lean')):
 src=str(path.relative_to(R))
 for j,(point,tau,H0,fs)in enumerate(parse(path)):
  s,dg,A,t1,psi,tdiv,periods=H0;assert periods==6000
  parents.append(dict(id=len(parents),source=src,index=j,point=point,tdiv=tdiv,end=t1+104*40,period_budget=periods,blank_first_time=tau))
  for k,(F,H)in enumerate(fs):
   for n in range(40,H[0]):add(src,'parent_raised',[j,k,n],cells1(F,n))
for path in sorted((R/'Chan').glob('Data*.lean')):
 src=str(path.relative_to(R));_,kids,_=parse(path)
 for j,(F,base,H)in enumerate(kids):
  for n in range(base,H[0]):add(src,'channel_raised',[j,n],cells1(F,n))
for name in['PerpData.lean','ParData.lean']:
 for j,row in enumerate(parse(R/name)):
  if name=='PerpData.lean':c,H,s1=row;s2=[]
  else:c,side,H,s1,s2=row
  F,bases=c
  for k,h in enumerate(s1):
   for n in range(bases[1],h[0]):add(name,'slab1_raised',[j,k,n],cells2(F,bases[0]+k,n))
  for k,h in enumerate(s2):
   for n in range(bases[0],h[0]):add(name,'slab2_raised',[j,k,n],cells2(F,n,bases[1]+k))
assert len(parents)==2432
with open(P/'TWO_BLACK_PARENT_LEAF_REPLAY_INPUT.txt','w')as f:
 for r in parents:f.write(' '.join(map(str,[r['id'],*r['point'],r['tdiv'],r['end']]))+'\n')
(P/'TWO_BLACK_DIRECT_LEAF_SOURCE_PLAN.json').write_text(json.dumps(dict(parents=parents,raised=raised,separate_blank_singleton_branches='already independently canonical one-black result',parent_fixed_replay_reads=sum(r['end']for r in parents)),separators=(',',':'))+'\n')
print(json.dumps(dict(parents=len(parents),parent_fixed_replay_reads=sum(r['end']for r in parents),raised_leaf_obligations=len(raised))))
