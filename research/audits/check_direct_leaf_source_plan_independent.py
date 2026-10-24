from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');P=R/'global_attraction_bridge_2026-10-24';S=R/'sources/imfinn-two-black/lean/TwoBlack';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ns={};q=R/'audits/check_generic_P104_fixed_cohort_independent.py';exec(q.read_text().split('manifest=')[0],ns);literal=ns['literal'];V=ns['V'];parents=[];raised=[]
def cells1(F,n):
 dg,near,far=F;return sorted(map(list,set(map(tuple,near+[[z[i]+n*V[dg][i]for i in range(2)]for z in far]))))
def cells2(F,a,b):
 vs,bl=F;return sorted(map(list,{tuple(z[i]+sum([a,b][j]*V[vs[j]][i]for j in mask)for i in range(2))for z,mask in bl}))
def put(src,kind,idx,cells):raised.append(dict(id=len(raised),source=src,kind=kind,index=idx,cells=cells,period_budget=6000))
for p in sorted((S/'Parents').glob('Chunk*.lean')):
 src=str(p.relative_to(S))
 for i,(point,tau,H,fs)in enumerate(literal(p)):
  s,dg,A,t1,psi,tdiv,periods=H;assert periods==6000 and tdiv==tau+1
  parents.append(dict(id=len(parents),source=src,index=i,point=point,tdiv=tdiv,end=t1+4160,period_budget=periods,blank_first_time=tau))
  for k,(F,h)in enumerate(fs):
   for n in range(40,h[0]):put(src,'parent_raised',[i,k,n],cells1(F,n))
for p in sorted((S/'Chan').glob('Data*.lean')):
 src=str(p.relative_to(S));_,kids,_=literal(p)
 for i,(F,base,h)in enumerate(kids):
  for n in range(base,h[0]):put(src,'channel_raised',[i,n],cells1(F,n))
for name in('PerpData.lean','ParData.lean'):
 for i,row in enumerate(literal(S/name)):
  if name=='PerpData.lean':c,H,s1=row;s2=[]
  else:c,side,H,s1,s2=row
  F,bs=c
  for k,h in enumerate(s1):
   for n in range(bs[1],h[0]):put(name,'slab1_raised',[i,k,n],cells2(F,bs[0]+k,n))
  for k,h in enumerate(s2):
   for n in range(bs[0],h[0]):put(name,'slab2_raised',[i,k,n],cells2(F,n,bs[1]+k))
plan=json.loads((P/'TWO_BLACK_DIRECT_LEAF_SOURCE_PLAN.json').read_text());assert parents==plan['parents']and raised==plan['raised']and len(parents)==2432 and len(raised)==32824
assert sum(r['end']for r in parents)==plan['parent_fixed_replay_reads']==49090288
with (P/'TWO_BLACK_PARENT_LEAF_REPLAY_INPUT.txt').open()as f:
 for r,line in zip(parents,f,strict=True):assert list(map(int,line.split()))==[r['id'],*r['point'],r['tdiv'],r['end']]
run=P/'direct_leaf_complete_run';man=json.loads((run/'RUN_INPUT_MANIFEST.json').read_text());assert man['source_plan_sha256']==sha(P/'TWO_BLACK_DIRECT_LEAF_SOURCE_PLAN.json')and man['parent_obligation_file_sha256']==sha(P/'TWO_BLACK_PARENT_DIRECT_LEAVES.txt')
count=0;rc=0;pc=0
with (P/'TWO_BLACK_PARENT_DIRECT_LEAVES.txt').open()as lf:
 for chunk in man['chunks']:
  assert chunk['first_id']==count and sha(run/chunk['input'])==chunk['sha256'];n=0
  with (run/chunk['input']).open()as cf:
   for line in cf:
    z=list(map(int,line.split()));assert z[0]==count
    if chunk['kind']=='parent':assert z[1]==0 and z[2:]==list(map(int,next(lf).split()));pc+=1
    else:
     r=raised[rc];assert z[1:]==[1,len(r['cells'])]+[x for cell in r['cells']for x in cell];rc+=1
    count+=1;n+=1
  assert n==chunk['count']
 assert next(lf,None)is None
assert(pc,rc,count)==(4451091,32824,4483915)and count==man['total_obligations']
report={'status':'PASS literal source-plan and exact chunk input coverage; physical first-read enumeration and terminal outputs separate','script_sha256':sha(Path(__file__)),'source_plan_sha256':sha(P/'TWO_BLACK_DIRECT_LEAF_SOURCE_PLAN.json'),'run_input_manifest_sha256':sha(run/'RUN_INPUT_MANIFEST.json'),'parent_obligation_sha256':sha(P/'TWO_BLACK_PARENT_DIRECT_LEAVES.txt'),'parent_roles':len(parents),'parent_replay_reads':49090288,'parent_dynamic_obligations':pc,'raised_base_obligations':rc,'total':count,'source_direct_budget':6000,'source_scope':'Every direct Parent0.loop0 first-read obligation plus parent/channel/slab raised-base leaf is retained, no silent duplicate removal. Blank/singleton auxiliaries covered by separately signed all-position canonical one-black proof.','inputs':man['chunks']}
f=R/'audits/direct_leaf_source_plan_independent.json';f.write_text(json.dumps(report,indent=2)+'\n');print(sha(f));print(report['status'])
