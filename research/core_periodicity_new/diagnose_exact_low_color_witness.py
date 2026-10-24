"""Independently replay a saved finite colored/Q/clock path and expose geometry loss.
CLI MODEL.json TRACE.txt OUTPUT.json. No actual ant-path claim.
"""
from pathlib import Path
import sys,json,hashlib
from collections import Counter
src,txt,out=map(Path,sys.argv[1:5]);J=json.loads(src.read_text());A=json.loads(Path(J['base_model_file']).read_text());B=json.loads(Path(A['base_model_file']).read_text());S=json.loads(Path(B['base_model_file']).read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];nnear=len(S['poses']);fc=B['far_controls'];phase=S['target_global_phase'];F=J['Q_initial'];cb=J['color_bits'];qs=J['Q_shift'];as_=J['clock_shift'];rows=[];lines=txt.read_text().splitlines();trace=[list(map(int,s.split()[1:]))for s in lines if s.startswith('EDGE ')];goal=list(map(int,next(s for s in lines if s.startswith('GOAL ')).split()[1:]));start=list(map(int,next(s for s in lines if s.startswith('START ')).split()[1:]));p,v=start
assert[p,v]==[J['start'][0],J['start'][2]]
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def coord(z):x,y=rot(z,phase);return x+y,x-y
def info(p):
 z=J['positions'][p]
 if z[0]=='near':
  x,y,h=B['poses'][z[1]];geo,d=B['position_map'][z[1]];return dict(kind='near',h=h,q=coord((x,y))[0],tr=z[2],dfa=d,xy=[x,y])
 if z[0]=='far':
  geo,d=B['position_map'][z[1]];h,q=fc[geo-nnear];return dict(kind='far',h=h,q=q,tr=z[2],dfa=d)
 return dict(kind=z[0])
for step,z in enumerate(trace):
 ei,fr,to,a,bef,aft=z;e=J['transitions'][ei];assert e[:2]==[fr,to]and e[8]==a and not e[7]and[p,v]==[fr,bef]and(v&e[2])==e[3];vv=((v^e[4])&~e[5])|(e[6]&e[5]);assert vv==aft
 if a!=99 and a!=104:rows.append(dict(edge=ei,packet=a,source=fr,destination=to,model_source=info(fr),registers_before=dict(colors=v&((1<<cb)-1),Q=F+((v>>qs)&31),joint_age=(v>>as_)&7)))
 else:assert info(fr)['kind']!='low_scc'and info(to)['kind']!='low_scc','This diagnostic needs low-summary unfolding first.'
 p,v=to,vv
assert goal[1]==p and goal[3]==v;e=J['transitions'][goal[0]];assert e[7]and e[0]==p and e[8]==goal[2]and(v&e[2])==e[3]
rows.append(dict(edge=goal[0],packet=goal[2],source=p,destination=1,model_source=info(p),registers_before=dict(colors=v&((1<<cb)-1),Q=F+((v>>qs)&31),joint_age=(v>>as_)&7)))
x=y=0;h=rows[0]['model_source']['h'];anchors=[];C=0
for i,r in enumerate(rows):
 assert r['model_source']['h']==h;r['relative_pose']=[x,y,h];r['C_before']=C
 if r['model_source']['kind']=='near':
  u,w=r['model_source']['xy'];anchors.append(dict(packet_index=i,translation=[u-x,w-y]))
 dx,dy,dh=G[r['packet']]['endpoint'];dx,dy=rot((dx,dy),h);x+=dx;y+=dy;h=(h+dh)%4;C+=G[r['packet']]['name'].count('C')
anchor=anchors[0]['translation'];mismatches=[]
for i,r in enumerate(rows):
 x,y,h=r['relative_pose'];r['actual_pose_from_first_near_anchor']=[x+anchor[0],y+anchor[1],h]
 u,w=r['actual_pose_from_first_near_anchor'][:2];q,t=coord((u,w));assert r['model_source']['q']==q and r['model_source']['tr']==t%4
 if r['model_source']['kind']=='near'and r['model_source']['xy']!=[u,w]:mismatches.append(dict(packet_index=i,packet=r['packet'],actual=[u,w,h],projected=r['model_source']['xy']+[h],transverse_jump=r['model_source']['xy'][0]+r['model_source']['xy'][1]-u-w))
word=[r['packet']for r in rows]
def legal(seq):
 x=y=h=t=0;last={}
 for a in seq+[-1]:
  for c in('LLLLRLRRRRL'if a<0 else G[a]['word']):
   if(x,y)in last and last[x,y][0]==c:return False,dict(cell=[x,y],previous_read=last[x,y][1],conflicting_read=t,turn=c)
   last[x,y]=c,t;h=(h+(1 if c=='R'else-1))%4;dx,dy=[(0,1),(1,0),(0,-1),(-1,0)][h];x+=dx;y+=dy;t+=1
 return True,None
ok,first=legal(word);bad=[]
for n in range(1,len(word)+1):
 for s in range(len(word)-n+1):
  oo,bb=legal(word[s:s+n])
  if not oo:bad.append(dict(start=s,word=word[s:s+n],conflict=bb))
 if bad:break
O=dict(status='PASS_FINITE_MODEL_PATH_NOT_PHYSICAL_ANT_PATH',model_file=str(src.resolve()),model_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),trace_file=str(txt.resolve()),trace_sha256=hashlib.sha256(txt.read_bytes()).hexdigest(),packets_including_goal=len(word),strict_packets=len(word)-1,total_C_before_goal=rows[-1]['C_before'],packet_counts=dict(Counter(word)),low_zone_used=False,near_anchors=anchors,transverse_reset_mismatches=mismatches,any_board_literal_legal=ok,first_literal_conflict=first,minimal_illegal_factors=bad,word_including_goal=word,rows=rows,scope='Every exact finite-model transition is directly replayed. All global q and t mod4 match a single cumulative path, but absolute transverse projection may reset on far-to-near transitions. Any-board literal conflicts are separately checked. No physical ant witness or model exclusion is asserted.')
out.write_text(json.dumps(O,indent=2)+'\n');print({k:v for k,v in O.items()if k not in ['rows','word_including_goal','near_anchors','minimal_illegal_factors']});print('shortest_bad_count',len(bad),'length',len(bad[0]['word'])if bad else None)
