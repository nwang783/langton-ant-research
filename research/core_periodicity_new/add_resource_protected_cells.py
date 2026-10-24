"""Strengthen an anchored patch with additional literal protected output cells.
CLI BASE.json PREFIX 'x,y;x,y'. No unproved clauses are added.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
inp,out=map(Path,sys.argv[1:3]);J=json.loads(inp.read_text());profile,data,meta=load_profile(J['resource_profile_file']);G=data['geometry']['geometry'];F=data['ordinary'];FP=data['protected'];Q=[tuple(J['protected_q'])]+[tuple(map(int,c.split(',')))for c in sys.argv[3].split(';')if c];Q=list(dict.fromkeys(Q));assert all(list(q)in J['points']and list(q)in G[J['source']]['outputs']for q in Q)
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
tx,ty,th=J['target_pose'];assert all(list(rot((q[0]-tx,q[1]-ty),-th))in G[J['target']]['inputs']for q in Q)
def forbidden(a,b,p,h,q):return(a,b,*p,h)in F or(a,b,*p,h,*q)in FP
T=[]
for r in J['transitions']:
 sid,to,k,v,f,goal,a=r;x,y,h=J['poses'][sid]
 if goal:T.append(r);continue
 context={tuple(rr[:2])for rr in G[a]['requirements']};good=True
 for q in Q:
  z=rot((q[0]-x,q[1]-y),-h)
  if z in context or forbidden(J['source'],a,(x,y),h,q)or forbidden(a,J['target'],rot((tx-x,ty-y),-h),(th-h)%4,z):good=False;break
 if good:T.append(r)
J.update(transitions=T,protected_cells=Q,underlying_single_anchor_file=str(inp),underlying_single_anchor_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),scope='All listed source-output identities protected through every strict intermediate complete context. No-hit excludes only this compound event.')
out.with_suffix('.json').write_text(json.dumps(J,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{J['n']} {J['out']+1} {len(T)} {len(J['reentry'])}\n");f.write(' '.join(map(str,J['start']))+'\n')
 for r in T:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,J['reentry']))+'\n')
print(json.dumps({'variables':J['n'],'transitions':len(T),'protected_cells':Q}))
