from pathlib import Path
import json,collections,random
import certify_short_refinement_rup as core
P=Path(__file__).resolve().parent;Q=json.loads((P/'forward108_prepared_control.json').read_text())['word'];O=P/'q_self_rewrite'
B=set(map(tuple,json.loads((P/'forward108_self_interfaces.json').read_text())['source_output']))
def literal(ch):
 w=''.join(core.dom[c][k]for c,k in zip(Q,ch));rr,e,g=core.trace(w,(0,14),3);assert(e,g)==((-2,12),3);by=collections.defaultdict(list)
 for t,(p,h,c)in enumerate(rr):by[p[0]-p[1],p[0]%2].append((t+len(w)*(p[0]//2),c))
 I=set();bad=False
 for a,es in by.items():
  es.sort();bad|=any(x[1]==y[1]for x,y in zip(es,es[1:]));
  if es[0][1]=='L':I.add(a)
 return w,by,I,bad

def check(ch,B):
 ns,C,gs=core.cnf(Q,(0,14),B,nontrivial=False);vals={ns['TRUE']:True};vals.update({ns[f'x{j}_{k}']:ch[j]==k for j,c in enumerate(Q)for k in range(len(core.dom[c]))});ok=True
 for a,(orb,ev)in enumerate(sorted(gs.items())):
  color=orb in B
  for b,(event,xs)in enumerate(sorted(ev.items())):
   active=any(vals[x]for x in xs);vals[ns[f'a{a}_{b}']]=active
   if active:
    ok&=color==(event[3]=='L');color=not color
   vals[ns[f'b{a}_{b}']]=color
 cnfok=all(any(vals[abs(x)]==(x>0)for x in cc)for cc in C);w,by,I,bad=literal(ch);physical=(not bad and(B&set(by))==I);assert ok==cnfok==physical
 return dict(choice=ch,length=len(w),legal=ok,input=sorted(B),minimal_black=sorted(I),internal_conflict=bad)
base=[0]*108;_,_,I,_=literal(base);records=[check(base,I),check(base,B)];c=base.copy();c[72]=core.dom['L'].index('RRRRL');records.append(check(c,B));rng=random.Random(10814)
for z in range(24):
 c=base.copy()
 for t in rng.sample(range(108),z+1):c[t]=rng.randrange(1,10)
 records.append(check(c,B))
assert records[0]['legal'];assert not records[1]['legal'];assert records[2]['internal_conflict']
out=dict(controls=len(records),legal=sum(x['legal']for x in records),records=records);(O/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out['controls'],out['legal'])
