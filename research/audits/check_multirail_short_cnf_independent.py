"""Independent standard-profile selectors on the already reconstructed event core."""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1];U=ROOT/'causal_reduction/unit_scale';O=U/'multirail_short_refinement'
# Execute only our independent palette/geometric/circuit definitions, not its tests.
s=(ROOT/'audits/check_short_refinement_cnf_independent.py').read_text();exec(compile(s.split('# White palette semantic reconstruction')[0],str(ROOT/'audits/check_short_refinement_cnf_independent.py'),'exec'))
A=json.loads((O/'architecture.json').read_text());res=json.loads((O/'result.json').read_text());_,_,groups,_=build(REV,(0,0),set(),False)
assert set(groups)=={(t,p)for t in range(-8,7)for p in (0,1)}
# Derive SW by proper half-turn from the independently literal NE profile.
NEread=set(g);NEblack=wake
rails=[]
for orientation,read,black in [('NE',NEread,NEblack),('SW',{(-t,p)for t,p in NEread},{(-t,p)for t,p in NEblack})]:
 shifts=sorted({(x-u,(y-v)%2)for x,y in groups for u,v in black if (x-u)%2==0})
 for t,p in shifts:
  rails.append({'orientation':orientation,'normal_shift':t,'x_parity_shift':p,'read':{(x+t,(y+p)%2)for x,y in read},'black':{(x+t,(y+p)%2)for x,y in black},'selector':1042+len(rails)})
assert len(rails)==48
for own,ref in zip(rails,A['rails']):
 assert own=={**ref,'read':set(map(tuple,ref['read'])),'black':set(map(tuple,ref['black']))}
C=[[1]]
for j in range(104):
 xs=list(range(2+10*j,12+10*j));C.append(xs);C.extend([[-a,-b]for a,b in combinations(xs,2)])
conflict=set()
for i,j in combinations(range(48),2):
 if rails[i]['read']&rails[j]['read']:C.append([-rails[i]['selector'],-rails[j]['selector']]);conflict.add((i,j))
assert len(conflict)==792
nv=1089;inputs={};gates=[]
for key,events in sorted(groups.items()):
 nv+=1;prev=nv;inputs[key]=prev;sel=[r['selector']for r in rails if key in r['black']]
 C.extend([[-x,prev]for x in sel]);C.append(sel+[-prev])
 for ev,xs in sorted(events.items()):
  active,nxt=nv+1,nv+2;nv+=2;C.extend([[-x,active]for x in xs]);C.append(xs+[-active]);C.append([-active,prev if ev[3]=='L'else-prev])
  for bp,ba,bn in product((False,True),repeat=3):
   if bn!=(bp!=ba):C.append([(-lit if bit else lit)for lit,bit in zip((prev,active,nxt),(bp,ba,bn))])
  gates.append((key,ev,xs,prev,active,nxt));prev=nxt
nv0,C0=read_cnf(O/'all_bundles.cnf');assert nv==nv0==9023 and len(C)==37367 and canon(C)==canon(C0)
assert hashlib.sha256((O/'all_bundles.cnf').read_bytes()).hexdigest()==res['cnf_sha256'];assert hashlib.sha256((O/'all_bundles.rup').read_bytes()).hexdigest()==res['rup_sha256']
chk=ROOT/'causal_reduction/morphic_candidates/check_drat';p=subprocess.run([str(chk),str(O/'all_bundles.cnf'),str(O/'all_bundles.rup')],capture_output=True,text=True,check=True);proof=json.loads(p.stdout);assert proof['valid']and proof['RUP']==316 and proof['RAT']==0 and proof['deletions']==0
# Exhaust all geometrically compatible bundles, not just assumed cardinality two.
compatible=[()]
for n in range(1,5):
 new=[c for c in combinations(range(48),n)if all((i,j)not in conflict for i,j in combinations(c,2))]
 if not new:break
 compatible+=new
assert max(map(len,compatible))==2 and len(compatible)==385
for bundle in compatible:
 B=set().union(*(rails[i]['black']for i in bundle));val={r['selector']:i in bundle for i,r in enumerate(rails)};val.update({var:key in B for key,var in inputs.items()})
 for key,var in inputs.items():assert val[var]==any(val[r['selector']]for r in rails if key in r['black'])
span=max(ev[0]for events in groups.values()for ev in events)-min(ev[0]for events in groups.values()for ev in events);assert span==4
out={'status':'PASS independent complete rail selectors, event CNF and retained RUP checker','architecture_sha256':hashlib.sha256((O/'architecture.json').read_bytes()).hexdigest(),'note_sha256':hashlib.sha256((U/'multirail_short_refinement_obstruction.md').read_bytes()).hexdigest(),'cnf_sha256':res['cnf_sha256'],'rup_sha256':res['rup_sha256'],'potential_read_classes':30,'normal_support':[-8,6],'global_phase_span':4,'rails':48,'incompatible_pairs':792,'compatible_bundles':385,'maximum_compatible_bundle_size':2,'variables':nv,'clauses':len(C),'RUP_additions':316,'scope':'Fixed inverse1041/5/9 exact-pose periodic architecture, any compatible finite standard NE/SW rail input. No output restriction, general consumer or capture claim.'}
(ROOT/'audits/check_multirail_short_cnf_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
