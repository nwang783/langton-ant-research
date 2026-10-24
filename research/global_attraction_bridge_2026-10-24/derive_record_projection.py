"""All-parameter integer-affine projection for three signed finite-seed families."""
from pathlib import Path
import json,hashlib
from record_event_projection import trace,stats
P=Path(__file__).parent;U=P.parent/'causal_reduction/unit_scale'
add=lambda a,b:(a[0]+b[0],a[1]+b[1]);mul=lambda a,c:(a[0]*c,a[1]*c)
def dot(q,a):return(q[1],q[0],mul(q[1],-1),mul(q[0],-1))[a]
def rotate(q,k):
 for _ in range(k%4):q=(q[1],-q[0])
 return q

def model184():
 d=json.load(open(U/'prepared1564_uniform_support_manifest.json'));e=json.load(open(U/'prepared1564_source_endpoint_family.json'));st=[]
 for i,s in enumerate(d['stages']):st.append((str(i)+':'+s['kind'],s['word'],tuple(s['count_N_constant'])))
 st += [('endpoint_response',e['after_checkpoint_word'],(0,1)),('tail',e['capture_word'],None)]
 return dict(name='184',n0=4,seed=d['seed_families'],pose=[d['initial_pose']['x_N_constant'],d['initial_pose']['y_N_constant']],heading=3,stages=st)
def model394():
 d=json.load(open(U/'prepared4352_capture_manifest.json'));st=[(str(i)+':'+s['kind'],s['word'],tuple(s['count_N_constant']))for i,s in enumerate(d['stages'])]+[('tail',d['tail_word'],None)]
 return dict(name='394',n0=1,seed=d['seed_families'],pose=[d['initial_pose']['x_N_constant'],d['initial_pose']['y_N_constant']],heading=3,stages=st)
def model16():
 # Signed literal four-cell reference. No unknown future is simulated here.
 g={(0,-1),(1,1),(1,3),(2,2)};b=set(g);p=(0,0);h=1;w='';V=((0,1),(1,0),(0,-1),(-1,0))
 for _ in range(286):
  c='L'if p in b else'R';w+=c;b.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
 A,W=w[:182],w[182:];poses=[((0,0),(0,0)),((14,-1),(14,0)),((10,0),(18,-4)),((2,5),(10,0))];heads=[1,0,3,2];R=[(7,-4),(2,-5),(4,-6),(2,-6)];part=[61,71,61,56];seed=[];st=[]
 for j in range(4):
  for q in g:
   q=rotate(q,heads[j]-1);seed.append([add(poses[j][0],(0,q[0])),add(poses[j][1],(0,q[1]))])
  st.extend([(f'port{j}',A,(0,1)),(f'flight{j}',W,R[j]),(f'partial{j}',W[:part[j]],(0,1))])
 e=json.load(open(P/'TRANSVERSE_FAR_MODULE_SOURCE.json'));st += [('recovery',e['post_contact_word'],(0,1)),('tail',e['tail_word'],None)]
 return dict(name='16',n0=10,parameter='n=2k, parameter here k',seed=seed,pose=((0,0),(0,0)),heading=1,stages=st)

def project_affine(model):
 n0=model['n0'];ineq=[];p=tuple(tuple(q)for q in model['pose']);h=model['heading'];T=(0,0)
 def ev(q):return q[0]*n0+q[1]
 def nonnegative(q,label):
  assert q[0]>=0 and ev(q)>=0,(model['name'],label,q,'not uniform')
  ineq.append([label,q]);return True
 def maxline(xs,label):
  xs=list(xs);best=max(xs,key=lambda q:(ev(q),q[0]))
  for q in xs:nonnegative(add(best,mul(q,-1)),label)
  return best
 def positive(q,label):
  if q[0]>=0 and ev(q)>0:nonnegative(add(q,(0,-1)),label);return True
  if q[0]<=0 and ev(q)<=0:nonnegative(mul(q,-1),label);return False
  raise AssertionError((model['name'],label,q,'sign changes'))
 seed=[tuple(tuple(v)for v in q)for q in model['seed']]
 M=[maxline([dot(q,a)for q in seed+[p]],'seed_hull')for a in range(4)];initial=M[:];out=[];stageproof=[]
 for j,(name,w,C)in enumerate(model['stages']):
  P0=len(w);q,end,hh=trace(w,(0,0),h);d=end
  if C is None or C!=(0,1):assert hh==h
  first=[];rays=[];oldM=M[:]
  for a in range(4):
   vals=[(x[1],x[0],-x[1],-x[0])[a]for x in q];B=max(vals);dd=(d[1],d[0],-d[1],-d[0])[a];start=dot(p,a);prefix=-10**20
   for i,v in enumerate(vals):
    if v>prefix and positive(add(add(start,(0,v)),mul(M[a],-1)),f'{j}:{a}:first{i}'):first.append([i,a])
    prefix=max(prefix,v)
   if dd>0 and C!=(0,1):
    prefix=B-dd
    for i,v in enumerate(vals):
     if v>prefix:
      z=add(M[a],mul(add(start,(0,v)),-1));assert z[0]%dd==0,(name,a,z,dd)
      low=maxline([(0,1),(z[0]//dd,z[1]//dd+1)],f'{j}:{a}:low{i}')
      if C is None or positive(add(C,mul(low,-1)),f'{j}:{a}:nonempty{i}'):rays.append(dict(phase=i,normal=a,lo=low,hi=C))
     prefix=max(prefix,v)
   if C is not None:
    high=add(start,(0,B))
    if dd>0:high=add(high,mul(add(C,(0,-1)),dd))
    M[a]=maxline([M[a],high],f'{j}:{a}:hull')
  out.append(dict(stage=name,start=T,period=P0,count=C,first=sorted(first),rays=rays))
  stageproof.append(dict(stage=name,start_pose=p,heading=h,drift=d,old_hull=oldM,end_hull=M[:]))
  if C is None:break
  T=add(T,mul(C,P0));p=tuple(add(p[i],mul(C,d[i]))for i in range(2));h=hh
 return dict(name=model['name'],domain_start=n0,initial_hull=initial,stages=out,geometry=stageproof,inequality_count=len(ineq),inequality_sha256=hashlib.sha256(json.dumps(ineq,separators=(',',':')).encode()).hexdigest(),inequalities=ineq)
if __name__=='__main__':
 for fn in [model184,model394,model16]:
  r=project_affine(fn());print(r['name'],'PASS inequalities',r['inequality_count'],'initialhull',r['initial_hull'])
  for st in r['stages']:
   if st['first']or st['rays']:print(st)
  (P/f'RECORD_PROJECTION_{r["name"]}_DRAFT.json').write_text(json.dumps(r,indent=2)+'\n')
