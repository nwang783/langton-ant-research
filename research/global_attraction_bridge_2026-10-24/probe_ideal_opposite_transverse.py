import json
from pathlib import Path
from check_return_permanent_output_debt import rot,DXY
P=Path(__file__).parent;d=json.loads((P/'WRITTEN_WAKE_PORT_OBSTRUCTION_CHECKED.json').read_text());Q=list(map(tuple,d['Q']));W=[tuple(z['cell'])for z in d['W']];C=set(map(tuple,d['C']));U=d['U'];refs=json.loads((P/'OPPOSITE_TRANSVERSE_JOIN_PROBES.json').read_text())['records']
add=lambda a,b:(a[0]+b[0],a[1]+b[1]);sub=lambda a,b:(a[0]-b[0],a[1]-b[1]);dotS=lambda q:q[0]+q[1];dotT=lambda q:q[0]-q[1]
def old(q):return any(q[0]-w[0]==q[1]-w[1] and (q[0]-w[0])%2==0 for w in W)
out=[]
for ref in refs:
 z=tuple(ref['poses'][5][0]);q=tuple(ref['first_contact']['cell']);inc=ref['first_contact']['relative_last']-182;r,phi=divmod(inc,104);base=add(z,(-2*r,2*r));fringe=set(C)
 for v in Q[:phi]:
  if v in fringe:fringe.remove(v)
  else:fringe.add(v)
 F={add(base,rot(v,3))for v in fringe}
 def prev(p):
  for v in W:
   v=add(z,rot(v,3));dx,dy=p[0]-v[0],p[1]-v[1]
   if dx==-dy and dx%2==0 and dx//(-2)<=r-1:return True
  return False
 initial=lambda p:old(p)^(p in F)^prev(p)
 hits=[]
 for i,v in enumerate(Q):
  v=add(z,rot(v,3))
  for w in W:
   delta=dotT(w)-dotT(v)
   if delta%4:continue
   j=delta//(-4);pt=add(v,(-2*j,2*j));dd=pt[0]-w[0]
   if dd%2==0 and pt[1]-w[1]==dd:hits.append((104*j+i,i,j,pt))
 hit=min(hits);assert hit[0]==inc and hit[3]==q,(ref['joins'],hit,inc,q)
 pp=q;hh=0;toggle=set();mismatch=None;word=ref['contact_future_word']+ref['tail_word']*((ref['certification_cut']-ref['exact_onset'])//104+2)
 # tail_word starts at certification cut, not the earliest onset. Replay exactly recorded F then actual phase inferred from source word.
 L=ref['certification_cut']-ref['exact_onset'];tw=ref['tail_word'];startword=tw[(-L)%104:]+tw[:(-L)%104]
 word=ref['contact_future_word']+startword*3
 for t,ch in enumerate(word):
  actual=initial(pp)^(pp in toggle)
  if actual!=(ch=='L'):mismatch=dict(offset=t,cell=pp,expected=ch,actual='L'if actual else'R');break
  if pp in toggle:toggle.remove(pp)
  else:toggle.add(pp)
  hh=(hh+(-1 if actual else 1))%4;pp=add(pp,DXY[hh])
 print(ref['joins'],'class',(sum(z)%4,(z[0]-z[1])%4),'rphi',r,phi,'first',hit,'mismatch',mismatch,flush=True)
 out.append(dict(joins=ref['joins'],residue=[sum(z)%4,(z[0]-z[1])%4],r=r,phi=phi,earliest_contact=hit,mismatch=mismatch))
(P/'IDEAL_OPPOSITE_TRANSVERSE_QUOTIENT_PROBES.json').write_text(json.dumps(out,indent=2)+'\n')
