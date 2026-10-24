"""Independent direct arithmetic replay of a positive height-Petri path."""
from pathlib import Path
import json,sys
src,txt,out=map(Path,sys.argv[1:4]);J=json.loads(src.read_text());ss=txt.read_text().splitlines();start=int(next(s for s in ss if s.startswith('start ')).split()[1]);assert start in J['initial_controls'];p=start;C=[0]*len(J['places']);rows=[];w=[]
for s in ss:
 if not s.startswith('EDGE '):continue
 z=list(map(int,s.split()[1:]));ei,fr,to,a=z[:4];assert [fr,to,a]==J['transitions'][ei][:3];assert p==fr;assert z[4:]==C
 _,_,_,ins,outs=J['transitions'][ei];assert all(x>=y for x,y in zip(C,ins));before=C[:];C=[x-y+z for x,y,z in zip(C,ins,outs)];p=to;w.append(a);rows.append({'edge':ei,'packet':a,'from':J['poses'][J['positions'][fr][0]],'to':J['poses'][J['positions'][to][0]],'counts_before':before,'counts_after':C[:]})
assert any(pp==p and all(x>=y for x,y in zip(C,r))for pp,r in J['goal_requirements']);R={'status':'PASS_EXACT_PETRI_PATH','start':start,'goal':p,'word_before_goal':w,'states':rows,'scope':'This independently replays exact untruncated high-height counts and fixed Petri edges. It is not a physical ant path.'};out.write_text(json.dumps(R,indent=2)+'\n');print(json.dumps({'status':R['status'],'packets_before_goal':len(w),'word':w,'start_pose':rows[0]['from'],'goal_pose':rows[-1]['to'],'max_exact_count':max(max(r['counts_after'])for r in rows)},indent=2))
