import json,collections
from pathlib import Path
P=Path(__file__).parent;plan=json.loads((P/'TWO_BLACK_DIRECT_LEAF_SOURCE_PLAN.json').read_text());counts=collections.Counter();starts={};total=0
with open(P/'TWO_BLACK_PARENT_DIRECT_LEAVES.txt')as f:
 for i,line in enumerate(f):
  a=list(map(int,line.split()));pid=a[0];assert 0<=pid<2432
  starts.setdefault(pid,i);counts[pid]+=1;total+=1
assert total==4451091 and len(counts)==2432
sel={starts[pid]+counts[pid]//2 for pid in counts}|{i*(total-1)//1023 for i in range(1024)}
rows=[]
with open(P/'TWO_BLACK_PARENT_DIRECT_LEAVES.txt')as f:
 for i,line in enumerate(f):
  if i not in sel:continue
  pid,t,fx,fy,x,y=map(int,line.split());rows.append(dict(id=i,kind='parent_dynamic',parent=pid,first_read=t,cells=[(fx,fy),(x,y)],budget=624000))
raised=plan['raised']
for k in sorted({i*(len(raised)-1)//511 for i in range(512)}):
 r=raised[k];rows.append(dict(id=total+k,kind=r['kind'],source=r['source'],index=r['index'],cells=r['cells'],budget=624000))
with open(P/'TWO_BLACK_DIRECT_LEAF_BENCHMARK.txt','w')as f:
 for r in rows:f.write(' '.join(map(str,[r['id'],len(r['cells']),*[a for q in r['cells']for a in q],r['budget']]))+'\n')
(P/'TWO_BLACK_DIRECT_LEAF_BENCHMARK_JOBS.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')
meta=dict(parent_dynamic_obligations=total,raised_direct_obligations=len(raised),total_direct_obligations=total+len(raised),parent_count=2432,parent_counts=dict(counts),benchmark_jobs=len(rows),coverage='Every Parent0 loop0 first-read obligation plus every literal raised-base direct call; repeated obligations may share a board but are not silently deduplicated.')
(P/'TWO_BLACK_DIRECT_LEAF_INVENTORY.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps({k:v for k,v in meta.items()if k!='parent_counts'}))
