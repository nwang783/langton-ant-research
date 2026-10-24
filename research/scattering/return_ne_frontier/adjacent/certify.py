"""Complete original finite three-black fields, all independent m,k>=100."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'));from bivariate import A,infinite_tail
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,P,plan
M=(1,0,100);K=(0,1,100);C=lambda a:(0,0,a)
def lin(a,b,c):return A.add(A.add(A.scale(M,a),A.scale(K,b)),C(c))
FRESH=plan(W,(0,0),1)[0]
def initial(r):
 Q=(lin(-2,-2,-33),lin(-2,-2,-14));s=(lin(-2,0,6+FRESH[r][0]),lin(-2,0,-43+FRESH[r][1]));off={15:1,45:-11,72:-33,29:-12,56:-12,62:-24}[r]
 T=(Q[0],lin(-2,2,off)) if r in [15,45,72] else (lin(-2,2,off),Q[1]);return [s,Q,T]
def main(r):
 TFILE=HERE/f'template_r{r}.json';T=json.loads(TFILE.read_text());points=initial(r);field=A.Field(points);assert len(field.points)==3
 for i,p in enumerate(points):
  for q in points[i+1:]:assert A.no_point_collision(p,q)
 for x in A.STATS:A.STATS[x]=0
 A.READ_POINTS.clear();A.READ_RAYS.clear();base=A.point(0,0);h=0;elapsed=C(0);first=[None]*3;records=[]
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'} and s['type'] in ['finite','periods'];data=A.word_data(word,h);count=None if s['type']=='finite' else lin(*s['count_m_k_constant'])
  for t,marker in enumerate(points):
   if first[t] is not None:continue
   hits=[]
   for j,q in enumerate(plan(word,(0,0),h)[0]):
    q=A.translate_local(q,base,0)
    if count is None:
     if q==marker:hits.append(A.add(elapsed,C(j)))
     else:assert A.no_point_collision(q,marker)
    else:
     k=A.line_coordinate(A.psub(marker,q),data[2])
     if k is not None and A.in_range(k,count):hits.append(A.add(A.add(elapsed,A.scale(k,104)),C(j)))
   if hits:
    first[t]=hits[0]
    for a in hits[1:]:first[t]=A.minimum(first[t],a)
  if count is None:base=A.apply_finite(field,data,base,0,'finite'+str(i));elapsed=A.add(elapsed,C(len(word)))
  else:
   assert len(word)==104 and word in {W[j:]+W[:j] for j in range(104)} and data[3]==h and A.nonneg(A.sub(count,C(1)));base=A.apply_periods(field,data,base,0,count,'period'+str(i));elapsed=A.add(elapsed,A.scale(count,104))
  h=data[3];records.append(dict(segment=i,time=elapsed,pose=[base,h]));print(json.dumps(records[-1]),flush=True)
 assert all(x is not None for x in first)
 tw=T['infinite_tail_word'];assert tw in {W[j:]+W[:j] for j in range(104)};phase=next(j for j in range(104) if tw==W[j:]+W[:j]);data=A.word_data(tw,h);assert data[3]==h;proof=infinite_tail(field,data,base)
 bounds={v:None for v in ['u_min','u_max','z_min','z_max']}
 def collect(q):
  u=A.sub(*q);z=A.add(*q)
  for key,a,fn in [('u_min',u,A.minimum),('u_max',u,A.maximum),('z_min',z,A.minimum),('z_max',z,A.maximum)]:bounds[key]=a if bounds[key] is None else fn(a,bounds[key])
 for q in A.READ_POINTS:collect(q)
 for b,d,count in A.READ_RAYS:collect(b);collect(tuple(A.add(v,A.scale(A.sub(count,C(1)),di)) for v,di in zip(b,d)))
 # Bind to the literal four discovery outputs, but do not use them to prove.
 for m,k in [(100,100),(101,100),(100,101),(101,101)]:
  old=json.loads((HERE/f'r{r}_m{m}_k{k}.json').read_text());ev=lambda a:a[0]*(m-100)+a[1]*(k-100)+a[2];assert ev(first[2])==old['first_contact']
 tail=[A.translate_local(q,base,0) for q in data[0]]
 out=dict(status='exact complete original finite three-cell capture for all m,k>=100',phase=r,domain='m=U+100,k=V+100,n=m+k, independent U,V>=0',initial_points=points,first_contacts=first,capture_time=elapsed,capture_pose=[base,h],tail_phase=phase,tail=proof,finite_prefix_bounds=bounds,tail_read_points=tail,records=records,statistics=A.STATS.copy(),template_sha256=hashlib.sha256(TFILE.read_bytes()).hexdigest())
 (HERE/f'certificate_r{r}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['tail_read_points','records']},indent=2))
if __name__=='__main__':main(int(sys.argv[1]))
