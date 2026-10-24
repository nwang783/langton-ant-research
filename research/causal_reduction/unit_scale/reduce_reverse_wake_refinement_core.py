"""Greedy local-orbit UNSAT reduction for one frozen short-refinement family.
This is an explanatory solver control, not an independent UNSAT certificate.
"""
from pathlib import Path
import json,re,time,hashlib
from synthesize_reverse_wake_short_refinement import build,mkconfig,mkcontext,mksolver,inc,parse,solve
P=Path(__file__).resolve().parent
text,coarse,events=build((1,6),'all');rows=text.splitlines();starts=[i for i,s in enumerate(rows)if re.match(r'\(declare-fun b\d+_0 ',s)];groups=[rows[a:b]for a,b in zip(starts,starts[1:]+[len(rows)])];prefix=rows[:starts[0]];keys=sorted(events)
def test(indices):
 txt='\n'.join(prefix+sum((groups[i]for i in indices),[]))+'\n';ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,txt.encode());return solve(ctx,s),txt
active=list(range(len(groups)));assert test(active)[0]==-1;checks=[]
for i in list(active):
 z=[j for j in active if j!=i];ans,_=test(z);checks.append(dict(removed=keys[i],result=ans))
 if ans==-1:active=z
ans,txt=test(active);assert ans==-1
(P/'reverse_wake_refinement_minimal_core.smt2').write_text(txt)
used=sorted({int(x)for x in re.findall(r'x(\d+)_\d+', '\n'.join(sum((groups[i]for i in active),[])))})
out=dict(scope=__doc__,orbits=[keys[i]for i in active],coarse_phases=used,checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'reverse_wake_refinement_minimal_core.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
