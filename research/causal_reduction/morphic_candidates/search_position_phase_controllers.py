"""Exact literal screening of deterministic k9,a3 heading-phase controllers.
Four rules, one for each (coarse R/L, fine-minus-coarse heading 0/2).
Each rule chooses one of15 eligible nine-turn words. Horizon is UNKNOWN only.
"""
import itertools,json,pathlib,time,sys,collections
from position_only_ownership import inventory
from free_inflation_generic_csp import trace
HERE=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
rows=inventory(9,(3,0),0)
keys=[('R',0),('R',2),('L',0),('L',2)]
opts=[[z['word'] for z in rows if z['Hc']==0 and z['c']==c and z['Hf']==h] for c,h in keys]
assert [len(x)for x in opts]==[15]*4

def check(words,root,limit):
 letters=[];poses=[(0,0,0)];last={};fuel=0;phase_counts=collections.Counter()
 for n in range(limit):
  c=root if n==0 else letters[n];x,y,h=poses[n];X,Y,H=poses[-1];delta=(H-h)%4
  assert delta in(0,2)
  key=(0 if c=='R' else 2)+delta//2;w=words[key]
  if n==0 and w[0]!=c:return None
  phase_counts[key]+=1
  for ch in w:
   X,Y,H=poses[-1];p=(X,Y)
   if p in last and last[p][0]==ch:
    return dict(status='CONFLICT',time=len(letters),cell=p,turn=ch,previous=last[p][1],fuel=fuel,phase_counts=dict(phase_counts))
   if p not in last and ch=='L':fuel+=1
   last[p]=(ch,len(letters));letters.append(ch);H=(H+(1 if ch=='R' else -1))%4;dx,dy=D[H];poses.append((X+dx,Y+dy,H))
  assert poses[-1][:2]==(3*poses[n+1][0],3*poses[n+1][1])
 return dict(status='HORIZON_ONLY',macros=limit,turns=len(letters),fuel=fuel,distinct_cells=len(last),phase_counts=dict(phase_counts),endpoint=poses[-1])

if __name__=='__main__':
 limit=int(sys.argv[1])if len(sys.argv)>1 else 10000;start=time.time();results=[];counts=collections.Counter();latest=0
 with open(HERE/'position_phase_controllers.jsonl','w')as log:
  for ids in itertools.product(range(15),repeat=4):
   words=[opts[j][ids[j]]for j in range(4)]
   for root in 'RL':
    result=check(words,root,limit)
    if result is None:continue
    result.update(ids=ids,words=words,root=root);counts[result['status']]+=1;latest=max(latest,result.get('time',0))
    log.write(json.dumps(result)+'\n')
    if result['status']=='HORIZON_ONLY':results.append(result);print('SURVIVOR',ids,root,result['fuel'],flush=True)
  log.flush()
 summary=dict(options=dict(zip([c+str(h)for c,h in keys],opts)),controllers=15**4,rooted_cases=sum(counts.values()),counts=dict(counts),latest_conflict=latest,seconds=time.time()-start,survivors=results)
 (HERE/'position_phase_controllers_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps({k:v for k,v in summary.items()if k not in('options','survivors')},indent=2))
