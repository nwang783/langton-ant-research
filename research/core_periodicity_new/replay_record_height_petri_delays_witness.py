"""Independent arithmetic replay of exact count and delayed-envelope witness."""
from pathlib import Path
import sys,json
src,txt,out=map(Path,sys.argv[1:4]);J=json.loads(src.read_text());m=len(J['places']);ss=txt.read_text().splitlines();p=int(next(s for s in ss if s.startswith('start ')).split()[1]);assert p in J['initial_controls'];C=[0]*m;Q=[0]*5;rows=[];w=[]
for s in ss:
 if not s.startswith('EDGE '):continue
 v=list(map(int,s.split()[1:]));ei,fr,to,a=v[:4];assert [fr,to,a]==J['transitions'][ei][:3];assert p==fr and v[4:]==C+Q
 _,_,_,ii,oo,c,H,*needs=J['transitions'][ei];assert all(x>=y for x,y in zip(C,ii));assert all(x>=y for x,y in zip(Q,needs));before=C+Q;C=[x-y+z for x,y,z in zip(C,ii,oo)];old=Q[:];Q=[max(old[max(j-c,0)],H if c>=j else 0)for j in range(5)];assert Q==sorted(Q,reverse=True);p=to;w.append(a);rows.append({'edge':ei,'packet':a,'from':J['poses'][J['positions'][fr][0]],'to':J['poses'][J['positions'][to][0]],'before':before,'after':C+Q})
assert any(pp==p and all(x>=y for x,y in zip(C+Q,r))for pp,r in J['goal_requirements']);R={'status':'PASS_EXACT_COUNTS_AND_ENVELOPES','word_before_goal':w,'states':rows,'scope':'Positive abstract control only, with full untruncated height counts and all five signed-age global height envelopes. Not an ant trajectory.'};out.write_text(json.dumps(R,indent=2)+'\n');print(json.dumps({'status':R['status'],'packets_before_goal':len(w),'max_actual_count':max(max(r['after'][:m])for r in rows),'word':w},indent=2))
